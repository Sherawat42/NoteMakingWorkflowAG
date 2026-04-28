# Chunk 010 — Hasse Diagrams, Operations on Relations & Introduction to Functions
<!-- Pages: 91-100 -->
<!-- Source: chunk_010.txt -->
<!-- Continuity: Continues Section 3.2.4 (Partial Order, started in chunk 009) by introducing Hasse diagrams and order-theoretic special elements. Then covers Section 3.2.5 (Operations on Relations) and opens Section 3.3 (Functions): conceptualisation, definition, operations as functions, and types — injective, surjective, bijective. Continues into chunk 011 with answers, exercises and Unit 4. -->

## Section: Hasse Diagrams & Special Elements of a Poset 🔴

### Core Idea
A **Hasse diagram** is a stripped-down picture of a finite poset: nodes are elements of X, and an upward edge is drawn from x to y whenever x R y (omitting reflexive loops and transitively-implied edges). The diagram makes it easy to spot "extremes" — minimal, maximal, minimum (least) and maximum (greatest) elements.

> **In Simple Terms:** A Hasse diagram is a layered ladder of a partial order. Bottom rungs = elements nobody is below; top rungs = elements nobody is above.

### Definitions
- **Hasse diagram**: graphical representation of a finite poset (X, R); draw an upward line from x to y whenever (x,y) ∈ R (after suppressing reflexive loops and edges implied by transitivity).
- **Minimal element**: a ∈ X such that there is no x ∈ X (x ≠ a) with (x, a) ∈ R, i.e. nothing is strictly "below" a. ⭐
- **Maximal element**: a ∈ X such that there is no y ∈ X (y ≠ a) with (a, y) ∈ R, i.e. nothing is strictly "above" a. ⭐
- **Minimum / least element**: the unique minimal element when only one exists.
- **Maximum / greatest element**: the unique maximal element when only one exists.

### Examples

**Example: Divisors of 12 under proper-divisor (Fig. 3.5)**
X = {1, 2, 3, 4, 6, 12}. Diagram has 1 at bottom, then 2 and 3, then 4 and 6, then 12 at top. Single maximum = 12 (greatest), single minimum = 1 (least).

**Example: Power set of {x, y, z} under ⊆ (Fig. 3.6)**
8 elements from ∅ to {x,y,z}. Bottom = ∅, top = {x,y,z}. A "cube"-shaped Hasse diagram.

**Example: X = {3, 4, 12, 24, 48, 72} under proper-divisor (Fig. 3.7)**
Two minimal elements: 3 and 4 (neither divides anything smaller in X).
Two maximal elements: 48 and 72.
No least/greatest element (because more than one minimal/maximal).

### Edge Cases & Caveats
- A poset can have multiple minimal or maximal elements.
- "Minimum/least" exists only when there is exactly **one** minimal element; same for maximum.
- Reflexive self-loops and transitively-derived edges are NOT drawn in a Hasse diagram (otherwise it would be cluttered and uninformative).

> **Quick Recall:**
> - Minimal = nothing below it in R.
> - Maximal = nothing above it in R.
> - Least/greatest = unique minimal/maximal.

### Check Your Progress 5
Hasse diagrams of (X, is-proper-divisor-of):
1. X = divisors of 30 = {1,2,3,5,6,10,15,30} → minimal = 1, maximal = 30.
2. X = divisors of 24 = {1,2,3,4,6,8,12,24} → minimal = 1, maximal = 24.
3. X = divisors of 60 → minimal = 1, maximal = 60.
4. X = divisors of 32 = {1,2,4,8,16,32} → minimal = 1, maximal = 32 (this is a chain, hence totally ordered).

### Connections
- Builds on partial order (Chunk 009).
- Prerequisite for: lattices, lub/glb concepts.

---

## Section: Operations on Relations 🔴

### Core Idea
Operations take relations as input and produce new relations as output. They split into three families: **set-type** (union, intersection, difference, complement) treat a relation as a set of pairs; **mapping-type** (inverse, composition) flip or chain relations like functions; **closure** operations (reflexive-, symmetric-, transitive-closure) add the minimum number of pairs needed to enforce a given property.

> **In Simple Terms:** Set-type ops treat relations as bags of pairs; mapping-type ops let you walk the arrows backwards or in sequence; closure ops are the smallest "patches" that force a missing property to hold.

### Definitions
- **Set-type operations**: union (R ∪ S), intersection (R ∩ S), difference (R − S), complement (Rᶜ = U − R, where U is the universal relation X × Y).
- **Inverse R⁻¹**: from Y to X, where (y,x) ∈ R⁻¹ iff (x,y) ∈ R.
- **Composition R ∘ S** (with cod(R) = dom(S)): new relation from dom(R) to cod(S) such that (x,z) ∈ R ∘ S iff ∃ y with (x,y) ∈ R and (y,z) ∈ S. ⭐
- **Reflexive closure** of R: smallest reflexive relation containing R; add all (x,x) not yet in R.
- **Symmetric closure** of R: smallest symmetric relation containing R; for each (x,y) ∈ R add (y,x) if missing.
- **Transitive closure** of R: smallest transitive relation containing R; add all chains-of-pairs implied by composing R with itself.

### Examples (Set-type)
Let X = {1,2,3,4}, Y = {a,b,c}.
- R = {(1,a),(2,a),(2,c),(3,b),(4,b),(4,c)}
- S = {(1,b),(2,a),(3,a),(3,b),(4,a)}
- Universal U: 4 × 3 = 12 pairs.

| Op | Result |
|---|---|
| R ∪ S | {(1,a),(2,a),(2,c),(3,b),(4,b),(4,c),(1,b),(3,a),(4,a)} |
| R ∩ S | {(2,a),(3,b)} |
| R − S | {(1,a),(2,c),(4,b),(4,c)} |
| S − R | {(1,b),(3,a),(4,a)} |
| Rᶜ | {(1,b),(1,c),(2,b),(3,a),(3,c),(4,a)} |

### Examples (Mapping-type)
**Inverse:** R = {(1,a),(2,a),(2,c),(3,b),(4,b),(4,c)}.
R⁻¹ = {(a,1),(a,2),(c,2),(b,3),(b,4),(c,4)}.

**Composition:**
R from X = {1,2,3,4} to Y = {a,b,c}: R = {(1,a),(2,a),(2,c),(4,c)}.
S from Y to Z = {triangle, square}: S = {(a,triangle),(b,square),(b,triangle),(c,square)}.
R ∘ S = {(1,triangle),(2,triangle),(2,square),(4,square)}.

### Examples (Closures)
For R = {(2,2),(3,3),(2,3),(3,1)} on {1,2,3}:
- **Reflexive closure**: add (1,1) → {(2,2),(3,3),(2,3),(3,1),(1,1)}.
- **Symmetric closure**: add (3,2) and (1,3) → {(2,2),(3,3),(2,3),(3,1),(3,2),(1,3)}.
- **Transitive closure**: chain (2,3),(3,1) ⇒ add (2,1) → {(2,2),(3,3),(2,3),(3,1),(2,1)}.

### ⚠️ Common Mistakes
- ❌ Confusing inverse R⁻¹ with complement Rᶜ → ✅ R⁻¹ swaps coordinates of each pair; Rᶜ contains pairs **not** in R.
- ❌ Adding too many pairs in closure → ✅ Closures are "minimal" — add only what's needed.
- ❌ Composing relations when codomain of R ≠ domain of S → ✅ Composition R ∘ S requires cod(R) = dom(S).

> **Quick Recall:**
> - Closure = minimum extra pairs to enforce the property.
> - R⁻¹: swap each (x,y) → (y,x).
> - Composition: chain through a middle element y.

### Connections
- Builds on set operations from Unit 1.
- Prerequisite for: function composition, group operations.

---

## Section: Conceptualising Functions 🟡

### Core Idea
A **function** is a unique-valued rule that links each value of an independent variable to one and only one value of a dependent variable. Many real-world relationships fit this mould: distance as a function of time at constant speed; loan amount as a function of time at simple interest; area of a circle as a function of radius.

> **In Simple Terms:** A function is a one-output machine — feed it any allowed input and you always get exactly one answer back, with no surprises.

### Examples
- **(a)** Vehicle at 50 km/h: d = 50t. Plug t = 3 → d = 150; t = 5 → d = 250. Each input gives exactly one output. Write d = f(t) with f(t) = 50t.
- **(b)** Simple interest: A = 50000(1 + 6/100)ᵗ. Define g(t) = 50000(1 + 6/100)ᵗ; then A = g(t).
- **(c)** Area of circle: Area = π r². Define h(r) = π r²; then Area = h(r).

### Definitions
- **Function name**: the symbol (f, g, h, ...) labelling the rule.
- **Independent variable**: the input (e.g., t, r).
- **Dependent variable**: the output (e.g., d, A, Area).
- **Functional dependence**: the relationship "y is uniquely determined by x".

---

## Section: Function — Formal Definition 🔴

### Core Idea
A function f: X → Y is a special kind of relation in which every element of X has exactly one partner in Y. Two requirements: existence (each x has at least one image) and uniqueness (each x has at most one image).

### Definitions
- **Function f: X → Y**: rule associating to each x ∈ X a unique y ∈ Y, written y = f(x). ⭐
- **Domain** of f: the set X.
- **Codomain** of f: the set Y.
- **Image** of x under f: f(x); equivalently, "value of x under f".
- **Pre-image** of y: any x with f(x) = y.
- **Range** of f: {f(x) : x ∈ X} ⊆ Y — the actual outputs achieved.
- **Map / mapping**: synonyms for function.
- **Real function**: any function whose domain is R (or a subset of R).
- **Real-valued function**: any function whose codomain is R.
- **Complex-valued, integer-valued, rational-valued**: codomain is C, Z, Q respectively.

### Key Concepts

**Function vs Relation**:
| | Relation | Function |
|---|---|---|
| Each x in domain | may have any number of partners | must have exactly one partner |
| Each y in codomain | unrestricted | unrestricted (may have zero or many pre-images) |

**Multi-variable functions**: a function may have several independent variables.
- Area of rectangle: A_Rect = f₁(l, b) = l × b.
- Volume of container: v = f₂(l, b, h) = l × b × h.

But in this unit, we focus on single-variable functions f: R → Y.

### Examples
1. **f: N → N, f(x) = 2x + 1**. For each x ∈ N, 2x + 1 ∈ N and unique → function. ✓
2. **f: Z → N, f(x) = x² + 3**. For each x ∈ Z, x² + 3 ∈ N → function. ✓
3. **f: Z → N, f(x) = x² − 3**. For x = 0, x² − 3 = −3 ∉ N → **not a function** (image escapes the codomain). ✗
4. **f: Z → Z, f(x) = x² − 3**. Now image is in Z → function. ✓ (Note: changing codomain converted a non-function into a function.)

### ⚠️ Common Mistakes
- ❌ Forgetting that the image must lie in the codomain → ✅ A rule like f(x) = √x is NOT a function from Z to N (negative inputs have no real square root).
- ❌ Reading "→" in f: X → Y as logical implication → ✅ "→" here is just notation: X is on the left (domain), Y on the right (codomain).

> **Quick Recall:**
> - Function = relation + (existence + uniqueness of image).
> - Range ⊆ Codomain (range may be a strict subset).
> - Same rule + different codomain can change "function or not".

---

## Section: Operations as Functions 🟡

### Core Idea
A binary (or k-ary) operation on a set X is itself a function — its domain is the cross-product X × X (or X × X × ... × X) and its codomain is X (or wherever the result lives). This perspective unifies operations and functions.

### Examples
- Addition on N: Plus: N × N → N, Plus(x, y) = x + y.
- Set union on the power set P of a universe U: Union: P × P → P, Union(X, Y) = X ∪ Y.
- Squaring on N: SQ: N → N, SQ(n) = n². (Here domain = codomain.)

> **Quick Recall:**
> - An "operation" is a function whose domain is a (Cartesian power of) the codomain.

---

## Section: Injective Functions 🔴

### Core Idea
A function f: X → Y is **injective** (or one-to-one, "1-1") if distinct inputs give distinct outputs — no two different x's are sent to the same y.

> **In Simple Terms:** No collisions. Every input claims its own private output.

### Definitions
- **Injective (1-1)**: f: X → Y is injective if x₁ ≠ x₂ ⇒ f(x₁) ≠ f(x₂). Equivalently, f(x₁) = f(x₂) ⇒ x₁ = x₂. ⭐

**Note on terminology**: Avoid using "1-1" and "1-to-1" interchangeably — "1-to-1" typically refers to **bijective** (a different concept).

### Mechanisms / Processes (proving injectivity)
1. Assume f(x) = f(y) for arbitrary x, y in domain.
2. Manipulate algebraically to deduce x = y.
3. Conclude f is injective.

To **disprove** injectivity, exhibit a single pair x ≠ y with f(x) = f(y).

### Examples
1. **f: N → N, f(x) = 2x + 1.** Suppose f(x) = f(y): 2x + 1 = 2y + 1 ⇒ x = y. ✓ Injective.
2. **f: N → R, f(x) = √x.** f(x) = f(y) ⇒ √x = √y ⇒ x = y (squaring). ✓ Injective.
3. **f: N → R, f(x) = x².** f(x) = f(y) ⇒ x² = y² ⇒ x = ±y. But −y ∉ N, so x = y. ✓ Injective on N.
4. **f: Z → R, f(x) = x²** is **NOT** injective: f(2) = f(−2) = 4.

---

## Section: Surjective (Onto) Functions 🔴

### Core Idea
A function f: X → Y is **surjective** (or onto) if every element of the codomain Y is hit — for every y ∈ Y there is some x ∈ X with f(x) = y. The range equals the codomain.

> **In Simple Terms:** No leftovers in the codomain. Every potential output is actually produced by some input.

### Definitions
- **Surjective (onto)**: f: X → Y is surjective if for every y ∈ Y, there exists x ∈ X with f(x) = y. ⭐

### Mechanisms / Processes (proving surjectivity)
1. Take an arbitrary y in codomain Y.
2. Solve f(x) = y for x in terms of y.
3. Verify the solved x lies in domain X.
4. If yes for all y, f is surjective; if any y has no x in X, f is not surjective.

### Examples
- **f: N → N, f(x) = 2x + 1.** For y = 4 in N, x = 3/2 ∉ N → **not surjective**.
- **Mod: Z → N**, Mod(x) = |x|. For y ∈ N, x = y ∈ Z gives Mod(x) = y. ✓ Surjective.
- **f: Z → C, f(x) = √x (positive root).** Take y = 3.75 ∈ C; we need x = (3.75)² = 14.0625 ∉ Z → **not surjective**.
- **f: C → C, f(x) = √x.** Surjective (every complex number is a square root of its square).

---

## Section: Bijective Functions / 1-to-1 Correspondence 🔴

### Core Idea
A function is **bijective** if it is both injective and surjective. It pairs up elements of X and Y perfectly: every x has a unique partner in Y, and every y has a unique partner in X.

### Definitions
- **Bijective**: injective + surjective. ⭐
- **1-to-1 correspondence**: synonym for bijective.

### Edge Cases & Caveats
- A bijection between X and Y means |X| = |Y| (when finite), and both sets have "the same size" in general (cardinality).

> **Quick Recall:**
> - Injective: distinct inputs → distinct outputs (no collisions).
> - Surjective: every codomain element is hit (range = codomain).
> - Bijective: both — perfect pairing.

### Check Your Progress 6 (preview — answers in chunk 011)
1. Domain & range of (i) f(x) = −|x|; (ii) f(x) = +√(9 − x²).
2. f(x) = 2x − 5: compute f(0), f(7), f(−3).
3. Function or not? (i) f: N → N, f(x) = x − 3; (ii) f: N → Z, f(x) = x − 3.

### Connections
- Builds on relations (chunk 009).
- Prerequisite for: invertibility (a function has an inverse iff it is bijective), composition (chunk 010 set-type ops), graphing functions (Unit 4 / chunk 011-012).

### Open Questions
- For finite sets, when does injective ⇒ surjective?
- How do we test bijectivity graphically? (Hint: vertical line test + horizontal line test, treated in Unit 4.)
