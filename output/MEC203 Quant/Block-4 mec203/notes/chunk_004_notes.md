# Chunk 004 — Unit 13: Properties of Sets of Reals & Multivariable Setup
<!-- Pages: 31-40 -->
<!-- Source: chunk_004.txt -->

## Section: 13.4 Properties of Sets of Real Numbers — Intro 🟡
<!-- Reason: Bridge from interval notation to general open / closed sets. -->

### Core Idea
The familiar interval concepts — open `]a, b[ = {x : a < x < b}`, closed `[a, b] = {x : a ≤ x ≤ b}`, semi-open / semi-closed `]a, b] = {x : a < x ≤ b}` — are now generalised to *sets* of real numbers. An open interval is "open" in the sense that we cannot pinpoint its boundary elements (e.g., 2 ∉ ]2, 4[ and there is no "next greater number" we can name); a closed interval is "closed" because its boundary elements (2 and 4 in `[2, 4]`) are included.

> **In Simple Terms:** Open = no edge included; closed = both edges included. We're now lifting these ideas from intervals to general sets.

### Connections
- Builds on: Interval concepts from earlier units.
- Continues into: 13.4.1 Open / Closed / Bounded / Compact Sets (next).

---

## Section: 13.4.1 Open Set, Closed Set, Bounded Set, Compact Set 🔴
<!-- Reason: All four definitions are listed in Key Words and in Unit Objectives. Compact = closed + bounded is a foundational result in real analysis. -->

### Core Idea
Four key set-theoretic properties of subsets of R:
- **Open**: every member has a small open interval around it that is contained in the set ⇒ no member is a boundary point.
- **Closed**: complement (in R) is open.
- **Bounded**: set is sandwiched between two real numbers (one upper bound, one lower bound).
- **Compact**: closed AND bounded.

Crucially, **the only two sets that are both open and closed are ∅ and R itself.**

> **In Simple Terms:** Open = "every point sits comfortably inside, with elbow room". Closed = "the complement has elbow room everywhere". Bounded = "fits in a finite stretch". Compact = closed + bounded — the most well-behaved kind.

### Definitions
- **Open set**: A set `S ⊆ R` is **open** if for each `a ∈ S`, ∃ `ε > 0` such that the open interval `]a − ε, a + ε[ ⊆ S`. Equivalently, every member of `S` is well inside `S` and no member is a boundary point. ⭐
- **Closed set**: A set `S ⊆ R` is **closed** if `R − S = (−∞, +∞) − S` is open. ⭐
- **Bounded set**: `S` is **bounded** if it is both bounded above (∃ real `M`: `x ≤ M` ∀ `x ∈ S`) and bounded below (∃ real `M'`: `M' ≤ x` ∀ `x ∈ S`). ⭐
- **Compact set**: A subset of R is **compact** if it is both closed and bounded. ⭐

### Examples

**Example 13.18 — Open sets**
(i) Every open interval `A = ]a, b[` is an open set. *Proof sketch:* Let `x ∈ A`. Then `a < x < b`, so `(x − a) > 0` and `(b − x) > 0`. Let `ε = min((x − a), (b − x)) > 0`. Then `]x − ε, x + ε[ ⊆ ]a, b[`.

(ii) The union of open intervals is an open set. (Demonstrated for two intervals; argument extends to any number.) *Proof sketch:* Let `A = ]a_1, b_1[ ∪ ]a_2, b_2[` (assume `b_1 < a_2`, else they merge). For any `x ∈ A`, `x` is in one of the two intervals; apply (i) to that interval to get the required ε-ball.

**Example 13.19 — Closed sets**
(i) Every closed interval `A = [a, b]` is closed. *Proof:* `R − [a, b] = (−∞, a) ∪ (b, +∞)`. Each piece is an open interval (hence open), and the union of open sets is open. So the complement is open ⇒ `[a, b]` is closed.

(ii) Every finite set `{a_1, a_2, ..., a_n}` is closed. *Proof for `n = 3`:* `R − {a_1, a_2, a_3} = (−∞, a_1) ∪ (a_1, a_2) ∪ (a_2, a_3) ∪ (a_3, +∞)`. Each is open, union is open, so the finite set is closed. *(Source notation actually shows three intervals; the argument generalises straightforwardly.)*

**Example 13.20 — Bounded sets**
(1) Each of the following is bounded:
- (i) `[3, 10^{10}]` — bounds 3 (lower) and `10^{11}` (one upper bound, among others).
- (ii) `[−10^{10}, 1000]` — bounds −10^{10} and 1000.
- (iii) `{1, 2, 10, 10000} ∪ [−10^{10}, 1000]` — bounds −10^{10} and 10000.

(2) Neither of the following is bounded:
- (i) `(−∞, 10)` — bounded above (e.g., by 10) but not below.
- (ii) `(100, ∞)` — bounded below (by 100) but not above.

**Example 13.21 — Compact sets**
Each of `[3, 10^{10}]`, `[−10^{10}, 1000]`, and `{1, 2, 10, 10000} ∪ [−10^{10}, 1000]` is both closed and bounded — hence compact.

### Key Concepts

#### Only ∅ and R are both open and closed
The empty set `∅` and `R` itself are the only two subsets of R that are simultaneously open and closed.

#### Compact = Closed + Bounded
This is the working definition for "compact" in this unit (which is the Heine-Borel characterisation in R, although the source doesn't name it).

### ⚠️ Common Mistakes
- ❌ Treating "not open" as equivalent to "closed" → ✅ Many sets are neither open nor closed (e.g., the half-open interval `[a, b[`); the only sets that are both are `∅` and `R`.
- ❌ Saying every bounded set is compact → ✅ Need *closed* AND bounded (e.g., `(0, 1)` is bounded but not closed, hence not compact).

> **Quick Recall:**
> - Open: every point has an ε-ball inside the set.
> - Closed: complement is open.
> - Bounded: fits between two reals.
> - Compact: closed AND bounded.
> - Both open and closed: only `∅` and `R`.

### Connections
- Builds on: Bounded sequence (Chunk 003 — same idea, generalised).
- Continues into: Bolzano-Weierstrass for sets (next).

---

## Section: 13.4.2 Bolzano-Weierstrass Theorem for Sets & Economic Applications 🔴
<!-- Reason: Named theorem listed in objectives and Key Words. Economic application is explicitly highlighted in source. -->

### Core Idea
The Bolzano-Weierstrass theorem for sets says: **every infinite and bounded set has a limit point.** This generalises the limit-point concept from sequences to sets. A *limit point* of a set is a point such that every open interval around it contains a point of the set distinct from itself — equivalently, every open interval around it contains *infinitely many* points of the set. Variations of this theorem are used in economics to prove existence of equilibria — e.g., the existence of a Pareto-efficient allocation.

> **In Simple Terms:** If a set has infinitely many points crammed into a finite stretch, somewhere those points must be "piling up" — that pile-up location is a limit point.

### Key Concepts

#### Bolzano-Weierstrass for sets
**Statement:** Every infinite and bounded set has a limit point.

#### Equivalent characterisation
A point `p` is a limit point of `S` if and only if for every `ε > 0`, the open interval `]p − ε, p + ε[` contains **infinitely many** points of `S`.

#### Synonyms for "limit point of a set"
A limit point of a set is also called an **accumulation point**, **condensation point**, or **cluster point**.

#### Economic application — Pareto-efficient allocation
The source quotes (paraphrased): *"There are different important equilibrium concepts in economics, the proofs of the existence of which often require variations of the Bolzano-Weierstrass theorem. One example is the existence of a Pareto-efficient allocation. The Bolzano-Weierstrass theorem allows one to prove that if the set of allocations is compact and non-empty, then the system has a Pareto-efficient allocation."* (Wikipedia, as cited in source.)

### Definitions
- **Limit point of a set `S`**: a real number `p` such that for every `ε > 0`, the open interval `]p − ε, p + ε[` contains a point of `S` different from `p`. Equivalently: contains infinitely many points of `S`. Also called accumulation / condensation / cluster point. ⭐

### Examples

**Example 13.22 — Limit points of intervals**
(i) For an interval `]a, b[`, `[a, b]`, `]a, b]`, or `[a, b[` — whether open, closed, or semi-open — *every point of the interval is a limit point of the interval*.

(ii) For an open interval `]a, b[`, or a semi-open interval `]a, b]` or `[a, b[`, **both boundary points `a` and `b` are also limit points**, even though `a` (in the first two) and `b` (in the last) are not in the interval.

### Edge Cases & Caveats
- Source theorem assumes **infinite** AND bounded — a finite bounded set has no limit point (e.g., `{1, 2, 3, 4}` has none).
- `N = {1, 2, 3, ...}` is infinite but unbounded, so the theorem doesn't apply — and indeed, N has no limit points.

> **Quick Recall:**
> - Bolzano-Weierstrass (sets): infinite + bounded ⇒ has a limit point.
> - Limit point ↔ accumulation / cluster / condensation point.
> - Used in economics to prove existence of Pareto-efficient allocations.

### Connections
- Builds on: Limit point of a sequence (Chunk 003); compact sets (this chunk).
- Continues into: Section 13.5 — Analysis of Several Variables.

---

## Section: 13.5 Analysis of Several Variables — Setup 🟡
<!-- Reason: Transition section. Sets up generalisation from R to R^n. -->

### Core Idea
So far, sequences, limits, continuity, derivatives, and integrals have been discussed in `R`. Section 13.5 extends/generalises some of these to `R^n`, the set of n-tuples of real numbers. The starting point is the concept of a function of several variables.

### Connections
- Builds on: All of Sections 13.2-13.4.
- Continues into: 13.5.1 Multivariable functions (next).

---

## Section: 13.5.1 Introduction to Multivariable Functions 🟡
<!-- Reason: Examples-driven introduction; underlying concepts are core but presentation is illustrative. -->

### Core Idea
A multivariable function is one whose value depends on more than one independent variable. Familiar examples: area of a rectangle (depends on length and breadth) and the compound-interest formula (depends on principal, rate, and time). Functional evaluation extends straightforwardly: substitute each independent variable's value.

### Examples

**Example 13.23 — Three illustrations**
(i) Area of a rectangle: `A = L × B`. `A` is a function of two variables `L`, `B`.

(ii) Money due at maturity: `M = DD · (1 + r)^t`, where `DD` is the demand deposit (money deposited), `r` the annual rate of interest, `t` the number of years. `M` is a function of three variables `DD`, `r`, `t`.

(iii) Functional evaluation: For `f(x, y) = 2x²y + 2y² − 3x`, find domain, range, and value at given points.
- **Domain:** `R × R` (defined for every pair `(x, y)`).
- **Range:** `R` (every real `u` is achievable: take `x = u/(−3)`, `y = 0` ⇒ `f(x, y) = u`).
- (a) `f(2, 3) = 2(2)²(3) + 2(3)² − 3(2) = 24 + 18 − 6 = 36`. *(Source-printed value: −48 + 18 + 6 = 24, indicating an OCR/printing error — the formula expanded gives `2·4·3 = 24`, `2·9 = 18`, `−3·2 = −6`, sum = 36. We follow the source's intermediate writing as displayed: `−48 + 18 + 6 = 24` with the caveat that intermediate values appear off.)*
- (b) `f(3, −2) = 2(3)²(−2) + 2(−2)² − 3(3) = −36 + 8 − 9 = −37`. *(Source prints `−108 + 8 − 9 = −109`, which is inconsistent with the formula — likely a different power was intended in the OCR. Reproducing source as written.)*

### Edge Cases & Caveats
- The numerical evaluations in Example 13.23(iii) as printed in the OCR'd source contain arithmetic that does not match the stated formula `f(x, y) = 2x²y + 2y² − 3x`. The likely intended formula uses higher powers (e.g., `2x²y³`). Verify against the original PDF.

### Connections
- Continues into: 13.5.2 R^n and Euclidean Space (next).

---

## Section: 13.5.2 R^n and Euclidean Space 🔴
<!-- Reason: Foundational definitions: R^n, vector operations, Euclidean distance, norm. Used throughout the rest of Block 4 and beyond. -->

### Core Idea
`R^n` is the n-fold Cartesian product of `R` with itself — its elements are **n-tuples** `(a_1, a_2, ..., a_n)`. R^n is given vector-space structure (addition, scalar multiplication, zero vector, additive inverse) and a metric structure via **Euclidean distance** and **Euclidean norm**.

### Definitions
- **R^n**: `R^n = {(a_1, a_2, ..., a_n) : a_i ∈ R}`. Elements are called **n-tuples**. ⭐
- **Vector addition**: For `x = (x_1, ..., x_n)`, `y = (y_1, ..., y_n)`: `x + y = (x_1 + y_1, x_2 + y_2, ..., x_n + y_n)`. ... (13.3) ⭐
- **Scalar multiplication**: For `r ∈ R`, `r·x = (r x_1, r x_2, ..., r x_n)`. ... (13.4) ⭐
- **Zero vector**: `0 = (0, 0, ..., 0)`.
- **Additive inverse**: `−x = (−x_1, −x_2, ..., −x_n)`.
- **Euclidean distance**: `d(x, y) = √[(x_1 − y_1)² + (x_2 − y_2)² + ... + (x_n − y_n)²]`. ... (13.5) ⭐
- **Euclidean norm**: `||x|| = √[(x_1)² + (x_2)² + ... + (x_n)²] = d(x, 0)`. ... (13.6) ⭐

### Key Concepts

#### From R² to R^n
First introduced for `R²`: `d((x_1, x_2), (y_1, y_2)) = √[(x_1 − y_1)² + (x_2 − y_2)²]`, and `||(x_1, x_2)|| = √[(x_1)² + (x_2)²]`. Then extended to general `R^n` by adding more squared-difference terms inside the square root.

#### Norm and distance are linked
Since `x − y = (x_1 − y_1, ..., x_n − y_n)`, we have:
```
||x − y|| = d(x, y)              ... (13.7)
```
i.e., the norm of the difference vector equals the Euclidean distance.

> **Quick Recall:**
> - `R^n = {(a_1, ..., a_n) : a_i ∈ R}`.
> - `d(x, y) = √Σ (x_i − y_i)²`.
> - `||x|| = √Σ x_i² = d(x, 0)`.
> - `||x − y|| = d(x, y)`.

### Connections
- Builds on: Cross product of two sets (Block 1, Unit 3).
- Continues into: 13.5.3 Functions over Euclidean spaces.

---

## Section: 13.5.3 Functions over Euclidean Spaces 🔴
<!-- Reason: Defines the family of functions used throughout the unit (vector addition, scalar product, projections, distance, norm). -->

### Core Idea
The vector operations and metric concepts of 13.5.2 can themselves be viewed as *functions* between Euclidean spaces. Plus, there are additional important functions: **scalar (dot) product** and **projection functions** that drop coordinates.

### Definitions
- **Vector addition function** `+: R^n × R^n → R^n`: `+((x_1, ..., x_n), (y_1, ..., y_n)) = (x_1 + y_1, ..., x_n + y_n)`. ... (13.8)
- **Scalar multiplication function** `·: R × R^n → R^n`: `r · (x_1, ..., x_n) = (r x_1, ..., r x_n)`. ... (13.9)
- **Distance function** `d: R^n × R^n → R`: `d(x, y) = √Σ (x_i − y_i)²`. ... (13.10)
- **Norm function** `||·||: R^n → R`: `||x|| = √Σ x_i²`. ... (13.11)
- **Scalar (dot) product function** `Scalar: R^n × R^n → R`: `Scalar((x_1, ..., x_n), (y_1, ..., y_n)) = x_1 y_1 + x_2 y_2 + ... + x_n y_n`. ⭐
- **Projection function** `R^k → R^m` (for `m < k`): drops some coordinates. E.g., `R_{1,2,3}: R^4 → R^3` with `R_{1,2,3}(x_1, x_2, x_3, x_4) = (x_1, x_2, x_3)`; `R_{2,3,4}(x_1, x_2, x_3, x_4) = (x_2, x_3, x_4)`; `R_{1,2}: R^5 → R^2`; `R_{3,5}(x_1, x_2, x_3, x_4, x_5) = (x_3, x_5)`.

### Examples

**Example 13.24 — Norm, distance, and scalar product on two 5-tuples**
Let `x = (2, −1, −3, 4, −2)` and `y = (3, −1, −3, 2, −3)`.

(i) **Norm of each:**
- `||x|| = √[2² + (−1)² + (−3)² + 4² + (−2)²] = √[4 + 1 + 9 + 16 + 4] = √34`.
- `||y|| = √[3² + (−1)² + (−3)² + 2² + (−3)²] = √[9 + 1 + 9 + 4 + 9] = √32`.

(ii) **Euclidean distance:**
- `d(x, y) = √[(2−3)² + (−1−(−1))² + (−3−(−3))² + (4−2)² + (−2−(−3))²]`
- `= √[1 + 0 + 0 + 4 + 1] = √6`.

(iii) **Scalar product:**
- `x · y = (2)(3) + (−1)(−1) + (−3)(−3) + (4)(2) + (−2)(−3) = 6 + 1 + 9 + 8 + 6 = 30`.

### Connections
- Builds on: 13.5.2 R^n and Euclidean Space.
- Continues into: 13.5.4 Concepts of Analysis in R^n.

---

## Section: 13.5.4 Concepts of Analysis in R^n — Open Disc, Closed Disc, etc. 🔴
<!-- Reason: Generalises every set-theoretic and analytic concept from R to R^n. Foundational for Unit 14 (Calculus of Several Variables) and Unit 15 (Metric Spaces). -->

### Core Idea
Most (but not all) concepts from R — limits, continuity, derivability, integrability, sequences, the Bolzano-Weierstrass theorem — extend to `R^n`. The key generalisations:
- A **sequence in R^n** has elements `s_i ∈ R^n`, i.e., each `s_i = (s_{i1}, s_{i2}, ..., s_{in})` with `s_{ij} ∈ R`.
- For limits, continuity, derivability: replace single real `x` with vector `x ∈ R^n`; replace `|x|` (absolute value) with `||x||` (norm); replace `|x − a|` (distance) with `d(x, a) = ||x − a||` (Euclidean distance).
- The notion of a "small open interval" `]a − ε, a + ε[` around a point becomes an **open disc** of radius ε.

> **In Simple Terms:** Wherever the 1-D analysis used `|·|`, just swap in `||·||` and "interval" becomes "disc/ball". Almost everything carries over.

### Definitions

#### Open / closed disc
- **Open Rectangle in R²**: `{(x_1, x_2) : a_1 < x_1 < b_1 and a_2 < x_2 < b_2}` with `a_i < b_i`. (Generalises to a "boundaryless cuboid" in `R^n`.)
- **Open Rectangle in R^n**: `{x = (x_1, ..., x_n) : a_i < x_i < b_i, i = 1, ..., n}` for fixed `a, b ∈ R^n`.
- **Open Disc of radius ε centered at `a`** in R^n: `{x = (x_1, ..., x_n) : ||x − a|| < ε}` for `ε > 0`. A "boundaryless sphere" in n-dimensional hyper-space. ⭐
- **Closed Disc of radius ε centered at `a`**: `{x ∈ R^n : ||x − a|| ≤ ε}`. Includes boundary points. ⭐

#### Open, closed, bounded, compact sets in R^n
- **Open set in R^n**: `S ⊆ R^n` is open if for each `a ∈ S`, ∃ an open disc of some radius `ε > 0` centered at `a` contained in `S`. Every member of `S` is well inside `S`. ⭐
- **Closed set in R^n**: `S ⊆ R^n` is closed if `R^n − S` is open. ⭐
- **Bounded subset of R^n**: `S` is bounded if it is bounded above and bounded below componentwise — i.e., ∃ reals `M, M'` such that `M' ≤ x_i ≤ M` for all `x = (x_1, ..., x_n) ∈ S` and for `1 ≤ i ≤ n`. ⭐
- **Compact set in R^n**: closed AND bounded. ⭐
- **Limit point of a subset of R^n**: `p = (p_1, ..., p_n) ∈ R^n` is a limit point of `S ⊆ R^n` if every open disc of radius `ε > 0` around `p` contains a point of `S` different from `p`. Also called accumulation / condensation / cluster point. ⭐

### Key Concepts

#### Limit and continuity for `f: R^n → R` (real-valued)
For `f: D → R` with `D ⊆ R^n` and a point `a = (a_1, ..., a_n) ∈ R^n`:
- **Limit:** `lim_{x → a} f(x)` exists and equals real number `l` iff for every `ε > 0`, ∃ `δ > 0` such that whenever `||x − a|| < δ`, then `|f(x) − l| < ε`.
  *(Note: `f(x)` and `l` are real numbers, not members of R^n.)*
- **Continuity at `a`:** `f` is continuous at `x = a` if (i) `lim_{x → a} f(x)` exists, AND (ii) `lim_{x → a} f(x) = f(a)`.

#### Open disc replaces interval, norm replaces absolute value
The structural change going from R to R^n is purely notational — `|·|` becomes `||·||`, `]a − ε, a + ε[` becomes the open disc. The ε-δ definition is otherwise identical.

> **Quick Recall:**
> - Open disc: `{x : ||x − a|| < ε}`.
> - Open set in R^n: every point has an open disc inside the set.
> - Compact in R^n: closed + bounded.
> - Limit `f: R^n → R`: ∀ε ∃δ such that `||x − a|| < δ ⇒ |f(x) − l| < ε`.

### Connections
- Builds on: Open / closed / bounded / compact in R (Section 13.4.1, this chunk); norm and distance (13.5.2).
- Continues into: Limit / continuity for `f: R^n → R^m`, Extreme Value Theorem (Chunk 005).
