# Chunk 011 — Unit 3 Wrap-Up + Start of Unit 4: Coordinate Geometry & Function Representation
<!-- Pages: 101-110 -->
<!-- Source: chunk_011.txt -->
<!-- Continuity: Wraps Unit 3 with Key Words glossary, full Answers/Hints to all Check Your Progress exercises (CYP 1-6), and Unit 3 end-of-unit Exercises (Q1-Q7). Then opens Unit 4 "Coordinate Geometry and Representation of Functions" with structure, objectives, introduction, vertical line test, and the relationship between equation and function. Continues into chunk 012 with Coordinate Geometry, Cartesian system, linear/non-linear graphing. -->

## Section: Unit 3 — Key Words (Glossary) 🟡

### Core Idea
Glossary capturing the central definitions of Unit 3 in a compact, exam-ready form.

### Definitions
- **Equivalence Relation**: R on X is reflexive, symmetric, and transitive simultaneously: (i) ∀x ∈ X, (x,x) ∈ R; (ii) (x,y) ∈ R ⇒ (y,x) ∈ R; (iii) (x,y) ∈ R ∧ (y,z) ∈ R ⇒ (x,z) ∈ R. ⭐
- **Equivalence Class**: [a] = {x : (x,a) ∈ R} for an equivalence relation R. ⭐
- **Function**: f: X → Y, a rule associating each x ∈ X with a unique y ∈ Y, written y = f(x). ⭐
- **Injective Function**: f: X → Y with x₁ ≠ x₂ ⇒ f(x₁) ≠ f(x₂); equivalently f(x₁) = f(x₂) ⇒ x₁ = x₂. ⭐
- **Partition of a Set**: collection P = {Xᵢ} of non-empty mutually disjoint subsets of X whose union is X. ⭐
- **Partial Order Relation**: R on X is reflexive, antisymmetric, and transitive. ⭐
- **Partially Ordered Set (Poset)**: ordered pair (X, R) with R a partial order on X.
- **Surjective Function**: f: X → Y where for every y ∈ Y there exists x ∈ X with f(x) = y. ⭐

---

## Section: Answers / Hints to Check Your Progress (CYP 1–6) 🔴

### Check Your Progress 1 — Representations & Reflexivity
1. R on X = {1,2,3,4} with R = {(1,2),(2,1),(2,3),(3,1),(3,2),(3,4),(4,3)}.
   - **Graphic representation**: arrows between elements as listed.
   - **Matrix representation** (rows/cols indexed 1–4):

     | | 1 | 2 | 3 | 4 |
     |---|---|---|---|---|
     |1| 0 | 1 | 0 | 0 |
     |2| 1 | 0 | 1 | 0 |
     |3| 1 | 1 | 0 | 1 |
     |4| 0 | 0 | 1 | 0 |

2. Classifications:
   - is-congruent-to on triangles → **symmetric** (and also reflexive, transitive).
   - ≤ on numbers → **not symmetric** (3 ≤ 4 true, 4 ≤ 3 false). Also **antisymmetric** (x ≤ y and y ≤ x ⇒ x = y).
   - is-brother-of on all males → **symmetric** (every male is his own brother by formal definition); **not antisymmetric** (for distinct x, y, both brothers of each other).

### Check Your Progress 2 — Symmetric / Antisymmetric
1. {(1,1),(2,2),(3,3)} is **both symmetric and antisymmetric**.
2. {(1,2),(2,3),(1,3)} is **antisymmetric, not symmetric**.
3. {(1,2),(2,1),(1,3),(3,1)} is **symmetric, not antisymmetric** (since (1,2),(2,1) ∈ R but 1 ≠ 2).

### Check Your Progress 3 — Transitivity
- R defined by "angle between lines a and b = 30°" → **NOT transitive** (chain of two 30° angles can give 60° or 0°).
- ≤ on numbers → **transitive**.
- is-brother-of on all humans → **transitive**.

### Check Your Progress 4 — Independence of three properties
1. Each property is independent of the other two.
   - **Reflexive only** (not symmetric, not transitive): on Z, define (a,b) ∈ R iff 0 ≤ a − b < 1.
     - Reflexive: 0 = a − a < 1 ✓
     - Not symmetric: (4, 3) ∈ R since 0 ≤ 1 < 1... [OCR unclear — text reads "0 ≤ a − b < 1"; likely meant 0 ≤ a − b ≤ 1 or similar]; (3,4) ∉ R.
     - Not transitive: (4,3) ∈ R, (3,2) ∈ R, but (4,2) ∉ R since 4 − 2 = 2 ≥ 1.
   - **Symmetric only**: "is-perpendicular-to" on lines in a plane.
   - **Transitive only**: < on rationals (Q).
2. Partition of X = {1,2,3,4} from R = {(1,1),(2,2),(3,3),(4,4),(1,3),(3,1),(2,4),(4,2)}: equivalence classes are {1,3} and {2,4}, so partition = **{{1,3}, {2,4}}**.

### Check Your Progress 5 — Hasse Diagrams
| Set | Minimal | Maximal |
|---|---|---|
| Divisors of 30 | 1 | 30 |
| Divisors of 24 | 1 | 24 |
| Divisors of 60 | 1 | 60 |
| Divisors of 32 | 1 | 32 |

### Check Your Progress 6 — Functions
1. **(i) f(x) = −|x|**: Domain = R; Range = {x ∈ R : x ≤ 0} = (−∞, 0].
2. **(ii) f(x) = +√(9 − x²)**: Domain = [−3, 3] (so 9 − x² ≥ 0); Range = [0, 3].
   - Note: For complex-valued complex function f: C → C, range = domain = C.
3. f(x) = 2x − 5:
   - f(0) = −5
   - f(7) = 9
   - f(−3) = −11
4. **f: N → N, f(x) = x − 3**: not a function (f(0) = −3 ∉ N).
   - **f: N → Z, f(x) = x − 3**: is a function (image always lies in Z).

---

## Section: Unit 3 — End-of-Unit Exercises (Q1–Q7) 🔴

### Q1. Reflexivity classification
- (i) R = {(1,1),(2,2),(1,3),(2,3)} on X = {1,2,3}: (3,3) ∉ R → **not reflexive**; (1,1), (2,2) ∈ R → **not anti-reflexive**.
- (ii) is-brother-of on humans: **not reflexive** (fails for females); **not anti-reflexive** (holds for males).

### Q2. Symmetry classification (on X = {1,2,3})
- (i) {(1,1),(2,2),(3,3)} → **both symmetric and antisymmetric**.
- (ii) {(1,2),(2,3),(1,3)} → **antisymmetric, not symmetric**.
- (iii) {(1,2),(2,1),(1,3),(3,1)} → **symmetric, not antisymmetric**.

### Q3. Transitivity classification (on X = {1,2,3})
- (i) {(1,1),(2,2),(3,3)} → **transitive**.
- (ii) {(1,2),(2,3),(1,3)} → **transitive**.
- (iii) {(1,2),(2,1),(1,3),(3,1)} → **not transitive** ((1,2),(2,1) ∈ R but (1,1) ∉ R).

### Q4. Examples — properties independent
On {1,2,3}:
- (i) Reflexive + symmetric, not transitive: R = {(1,1),(2,2),(3,3),(1,2),(2,1),(1,3),(3,1)} — (2,1),(1,3) ∈ R but (2,3) ∉ R.
- (ii) Reflexive + transitive, not symmetric: R = {(1,1),(2,2),(3,3),(1,2),(1,3),(2,3)} — (2,3) ∈ R but (3,2) ∉ R.
- (iii) Symmetric + transitive, not reflexive: R = {(1,1),(2,2)} — (3,3) ∉ R.

### Q5. Hasse diagram for X = {1,2,3,...,10} under proper-divisor
- Minimal element = 1.
- Maximal elements = 5, 6, 7, 8, 9, 10 (no element of X strictly above any of them).

### Q6. f: Z → R, f(x) = x² — injective?
Suppose f(x₁) = f(x₂) ⇒ x₁² = x₂² ⇒ x₁ = ±x₂. So f(5) = f(−5) = 25 → **NOT injective**.

### Q7. f: C → R, f(x) = x² — surjective?
Take arbitrary x ∈ R; then √x ∈ C, and f(√x) = (√x)² = x. So every real x is hit → **surjective**.

> **Quick Recall:**
> - To prove **not injective**: produce one pair x ≠ y with f(x) = f(y).
> - To prove **surjective**: given y in codomain, exhibit x in domain with f(x) = y.

---

## Section: Unit 4 — Structure & Objectives 🟢

### Core Idea
Unit 4 ("Coordinate Geometry and Representation of Functions") teaches how to draw and interpret graphs of single- and two-variable functions. It uses Cartesian coordinates to translate algebraic equations into geometric pictures and vice versa, and surveys linear, non-linear, asymptotic, and piecewise function graphs.

### Unit 4 Objectives
After this unit, you should be able to:
1. Apply the **vertical line test** to identify a non-function.
2. Explain how **coordinate geometry** differs from conventional/synthetic geometry.
3. Obtain **algebraic equations** corresponding to simple geometric figures.
4. Graphically represent various types of functions of a single variable.
5. Handle graphs of two-variable functions at a preliminary level.

### Unit 4 Structure (sub-sections)
- 4.1 Introduction (4.1.1 Vertical Line Test; 4.1.2 Equation vs Function)
- 4.2 Coordinate Geometry (4.2.1 Cartesian Coordinate System; 4.2.2 Translating geometric figures to algebraic equations)
- 4.3 Linear Functions (4.3.1 Absolute Value; 4.3.2 Step Function)
- 4.4 Non-Linear Functions (Even/Odd, Quadratic, Cubic)
- 4.5 Asymptotic Functions (Square Root, Exponential, Logarithmic)
- 4.6 Piecewise Functions (Rational, Discontinuous — asymptotic / point / jump discontinuities)
- 4.7 Hyperbola & Parabola
- 4.8 Two-Variable Functions (Level Curves)

---

## Section: Vertical Line Test 🔴

### Core Idea
A graph in the (x, y) plane represents a function y = f(x) only if **no vertical line crosses the graph at more than one point**. The test is a quick way to detect failure of "single-valued output" — which is the defining property of a function.

> **In Simple Terms:** Drag a vertical ruler across the graph. If at any position it touches the graph in more than one place, the rule isn't a function — that x has multiple y's.

### Definitions
- **Vertical line test**: A relationship f(x) is NOT a function of x if some vertical line x = a meets the graph at two or more points.

### Examples
- The graph of x² + y² = 4 (a circle) **fails** the vertical line test (two y's for most x's) → not a function.
- The graph in Fig. 4.4 (a single curve passing the test) **is** a function.
- Important standard equations that are **not** functions of x: ellipses, circles, sideways parabolas (y² = 4ax).

### ⚠️ Common Mistakes
- ❌ Using the vertical line test to prove something IS a function → ✅ The test detects only failure. Passing the test plus being defined for every x in the domain is needed for it to be a function.

> **Quick Recall:**
> - Two intersection points with any vertical line ⇒ not a function.
> - Some equations like a circle look like nice curves but are NOT functions.

---

## Section: Equation vs Function — How to Tell 🔴

### Core Idea
An equation in x and y becomes a candidate for a function of x only after isolating y on the LHS with exponent 1. If the resulting expression assigns more than one y to some x, the equation defines a relation but not a function.

### Mechanisms / Processes
1. Start with the equation, e.g. X² + Y² = 4.
2. Isolate Y² (or whichever variable will be dependent): Y² = 4 − X².
3. Reduce LHS to power 1 by extracting a root: Y = ±√(4 − X²).
4. Check single-value rule:
   - If LHS gives one Y for each X → function.
   - If LHS gives multiple Y's (e.g., the ± above) → relation but NOT function.

### Examples
**Example: Circle**
1. X² + Y² = 4
2. Y² = 4 − X²
3. Y = ±√(4 − X²)

Two values of Y for most X (e.g., X = 0 → Y = +2 and Y = −2) ⇒ **not a function**, only a relation. The roles of X and Y can be swapped to make X the dependent variable; the conclusion is the same.

**Example: Sphere in 3D**
1. X² + Y² + Z² = 4
2. Z = ±√(4 − X² − Y²)

Z is determined up to a sign by X and Y → **not** a function of (X, Y).

### Edge Cases & Caveats
- Restricting the codomain (e.g., to non-negative reals) can convert a relation back into a function: Y = +√(4 − X²) is a function (the upper semicircle).
- Functions of more than one independent variable are allowed: Z = f(X, Y).

> **Quick Recall:**
> - Step 1: solve for the dependent variable.
> - Step 2: reduce its power to 1.
> - Step 3: check whether the result is single-valued.

### Connections
- Builds on function definition (Chunk 010).
- Prerequisite for: graphing standard curves in 4.2.2 (Chunk 012).

### Open Questions
- For y² = x + 5, is this a function? (No — for any x > −5 there are two y values.)
