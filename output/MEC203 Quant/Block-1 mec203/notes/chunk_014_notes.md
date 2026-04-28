# Chunk 014 — Discontinuities, Hyperbola, Parabola, Rectangular Hyperbola, 3D Graphs
<!-- Pages: 131-140 -->
<!-- Source: chunk_014.txt -->
<!-- Continuity: Continues Unit 4. Builds directly on rational and piecewise functions from chunk 013 (Sections 4.6.1, 4.6.2 begin here) and asymptotes. Introduces conic-section graphs (4.7) and functions of two variables (4.8). -->

## Section: Continuous vs Discontinuous Functions 🔴

### Core Idea
A continuous function is a single unbroken curve — drawable in one stroke without lifting the pen. A discontinuous function has a break, and there are exactly **three types** of discontinuities: asymptotic, point, and jump. Identifying which type appears at a given x helps interpret behaviour for calculus, integration, and economic models.

> **In Simple Terms:** "Continuous" = pencil never leaves the page. "Discontinuous" = at some x, the graph either shoots to infinity (asymptotic), has a missing dot (point), or suddenly leaps to a new height (jump).

### Definitions
- **Continuous function**: a function whose graph can be drawn without lifting the pen. ⭐
- **Discontinuous function**: a function that does not vary continuously through some value(s) of the variable. ⭐

### Key Concepts: Three Types of Discontinuities

#### 1. Asymptotic Discontinuity 🔴
The graph shoots to ±∞ near a forbidden x-value (vertical asymptote).

**Example**: f(x) = (x+4) / [(x−1)(x+8)]. Domain excludes x = 1 and x = −8.

Values approaching x = 1:

| x | y |
|---|---|
| 0.25 | −0.687 |
| 0.5 | −1.059 |
| 0.75 | −2.171 |
| 1.0 | Undefined |
| 1.25 | 2.270 |
| 1.5 | 1.158 |
| 1.75 | 0.786 |

As x → 1⁻, y → −∞; as x → 1⁺, y → +∞. The dotted vertical line at x = 1 is the asymptote.

**Horizontal asymptotic example**: f(x) = 2x/(x + 4) has horizontal asymptote y = 2.

#### 2. Point Discontinuity 🔴
The graph is continuous except at a single point — a tiny "hole" in the curve.

**Example A** — value redefined:
f(x) = { 1 if x = 3 ; x² for all other real x }
Graph is x² everywhere except a single redefined point at x = 3 (or x = 1 in original text).

**Example B** — denominator-cancellable hole:
f(x) = x²(x − 2)/(x − 2). At x = 2: f(2) = 0/0 = undefined. Cancelling gives:
f(x) = { x² if x ≠ 2 ; undefined if x = 2 }
The function behaves like x² everywhere except at x = 2 where it is undefined.

#### 3. Jump Discontinuity 🔴
The two pieces of a piecewise function have **different values** at the joining x.

**Continuous piecewise (no jump)**:
f(x) = { x² if x ≤ 1 ; 2 − x if x > 1 }
At x = 1, both pieces give 1 → continuous.

**Jump example**:
f(x) = { x² if x ≤ 1 ; −x if x > 1 }
At x = 1: left piece → 1, right piece → −1. The graph "jumps" between branches.

### Examples

**Example: Detect all discontinuities**

f(x) = { (x + 4)/x if x < 2 ; x² + 1 if x ≥ 2 }

- **First branch**: has x in the denominator → asymptotic discontinuity at **x = 0**.
- **At x = 2**: left branch → (2 + 4)/2 = 3; right branch → 2² + 1 = 5. Different values → **jump discontinuity at x = 2**.
- No other discontinuities.

### ⚠️ Common Mistakes
- ❌ Calling all breaks "asymptotic" → ✅ Distinguish: asymptotic (→ ±∞), point (single hole), jump (finite leap).
- ❌ Forgetting to test denominators of every piece in piecewise functions.

### Check Your Progress 5
1) **Draw graph of f(x) = −x³ + 4.** [From answer key: write as ax³ + c with a = −1, c = 4. Reflect y = x³ across x-axis (because a = −1) and translate up 4 units.]

> **Quick Recall:**
> - 3 discontinuity types: asymptotic, point, jump.
> - Hole at x = a where g(x) = h(x)·(x − a) cancels.
> - Continuous if pieces of a piecewise function meet at the boundary.

---

## Section: Hyperbola — Equations, Vertices, Foci, Asymptotes 🔴

### Core Idea
A hyperbola is the locus of points whose **difference** of distances from two fixed foci is constant. It has two mirrored branches and comes in horizontal or vertical forms. Plotting requires identifying centre, vertices, foci, the helper rectangle, and the asymptotes through which the branches are guided.

> **In Simple Terms:** A hyperbola looks like two parabolas back-to-back. Imagine two satellites orbiting in opposite directions, never crossing certain diagonal "guide rails" (the asymptotes).

### Definitions
- **Hyperbola**: set of all points where the **difference** of distances to two fixed foci is constant. ⭐
- **Transverse axis**: axis of symmetry passing through both foci and the centre.
- **Conjugate axis**: axis of symmetry perpendicular to the transverse axis through the centre.
- **Vertices**: the two points where the hyperbola crosses its transverse axis.

### Standard Equations
- **Horizontal hyperbola**: (x − h)²/a² − (y − v)²/b² = 1
- **Vertical hyperbola**: (y − v)²/a² − (x − h)²/b² = 1

The **centre** is (h, v) for both; x and y switch places (along with h and v) between the two forms.

| Feature | Horizontal hyperbola | Vertical hyperbola |
|---|---|---|
| Transverse axis | y = v (horizontal) | x = h (vertical) |
| Conjugate axis | x = h | y = v |
| Vertices | (h ± a, v) | (h, v ± a) |
| Foci | (h ± F, v) | (h, v ± F) |

### Mechanisms / Processes

**Computing F (distance from centre to a focus):**
**a² + b² = F²** (so F = √(a² + b²)).

**Steps to graph a hyperbola:**
1. Mark the centre (h, v).
2. From centre, mark a-distance along transverse axis (vertices) and b-distance along conjugate axis.
3. Draw a rectangle with sides through these four points (parallel to x- and y-axes).
4. Draw the diagonals of the rectangle extended — these are the **asymptotes**.
5. Sketch each branch starting at a vertex, hugging the asymptotes farther out.

**Slopes of asymptotes**: m = ± a/b (the chunk text gives this for both vertical and horizontal cases — likely an OCR/typesetting issue; conventionally m = ± b/a for horizontal and m = ± a/b for vertical hyperbolas).

### Examples

**Example: (y − 3)²/16 − (x + 1)²/9 = 1** (vertical hyperbola)

- Centre: (h, v) = (−1, 3).
- a² = 16 ⇒ a = 4 (vertical direction, since under y).
- b² = 9 ⇒ b = 3 (horizontal direction).
- Vertices: (−1, 3 + 4) and (−1, 3 − 4) = **(−1, 7) and (−1, −1)**.
- Foci: a² + b² = F² ⇒ 16 + 9 = 25 ⇒ F = 5. Foci: (−1, 3 + 5) and (−1, 3 − 5) = **(−1, 8) and (−1, −2)**.

### Edge Cases & Caveats
- a may be greater than, less than, or equal to b (unlike an ellipse).
- The curves never cross the asymptotes.
- If the equation is not in standard form, **complete the square** to put it there before identifying parameters.

### Economics Applications
- **Portfolio theory / efficient frontiers**: combinations of risk and return often shaped as partial hyperbolas.
- **Production frontiers**: combinations of capital and labour producing a given output.

> **Quick Recall:**
> - F² = a² + b² (note: opposite of ellipse, where it's F² = a² − b²).
> - Vertices at distance a along transverse axis.
> - Asymptotes are the rectangle's diagonals extended.

---

## Section: Hyperbola vs Parabola 🟡

### Core Idea
Although both are conic sections, parabolas and hyperbolas have fundamentally different defining geometries: parabolas use a single focus and a directrix; hyperbolas use two foci. Parabolas all share the same essential shape (only scaled); hyperbolas can be of various shapes.

> **In Simple Terms:** A parabola is "one focus + one straight-line guide". A hyperbola is "two foci, with a constant difference rule".

### Comparison Table

| Feature | Parabola | Hyperbola |
|---|---|---|
| Definition | Locus of points equidistant from a fixed focus and a fixed directrix line | Locus of points where difference of distances to two foci is a positive constant |
| Number of foci | 1 | 2 |
| Standard equation (simple) | y² = x | xy = 1 |
| Shape variability | All parabolas same shape (only scaled) | Hyperbolas have different shapes |
| Arm behaviour at infinity | Two arms become parallel | Arms diverge (do not become parallel) |

### Definitions
- **Directrix**: line perpendicular to the axis of symmetry of a parabola.
- **Focus** (parabola): the fixed point referenced in the definition.

---

## Section: Rectangular Hyperbola 🔴

### Core Idea
A rectangular (or "equilateral") hyperbola is one whose asymptotes are perpendicular to each other (orthogonal). The simplest examples take the form y = 1/xⁿ, where n is a positive integer. These graphs have the coordinate axes as asymptotes (when n ≥ 1) and no intercepts.

> **In Simple Terms:** A rectangular hyperbola is the "ideal" hyperbola whose asymptotes meet at right angles — most cleanly seen as y = 1/x.

### Definitions
- **Rectangular hyperbola**: a hyperbola for which the asymptotes are perpendicular (orthogonal). ⭐

### Key Concepts

#### Two Types based on parity of n in y = 1/xⁿ
- **n = 2k + 1 (n odd)**: e.g., y = 1/x. Branches lie in opposite quadrants.
- **n even**: e.g., y = 1/x². Branches lie in the same upper half (both positive y when n = 2).

#### Properties of Rectangular Hyperbola y = 1/xⁿ
1. Vertical asymptote at x = 0.
2. Horizontal asymptote at y = 0.
3. No stationary points.
4. No intercepts (when axes are the asymptotes).
5. **n odd**: gradient always decreasing throughout defined x.
6. **n even**: gradient increasing for x < 0; decreasing for x > 0.

### Examples

**Example: Graph y = (x − 1)/(x + 1)**

- **Intercepts**: x = 0 ⇒ y = −1; y = 0 ⇒ x = 1. So (0, −1) and (1, 0).
- **Turning points**: none.
- **Asymptotes**: as x → ∞, y → 1 (horizontal asymptote y = 1). As y → ∞, x → −1 (vertical asymptote x = −1).
- **Gradient**: always increasing.

### Economics Applications
- Unitary price elasticity of demand (rectangular hyperbola demand curve).
- Average fixed cost (AFC) curve.
- Production transformation curve.
- Indifference map components.

### Check Your Progress 6
1) **Difference between hyperbola and rectangular hyperbola.**
   - A rectangular hyperbola is a special case of hyperbola in which the asymptotes are **orthogonal** (perpendicular). General hyperbolas have asymptotes that need not be perpendicular.
2) **Price elasticity of a rectangular-hyperbola-shaped demand curve?**
   - **Unitary** (= 1) at every point.
3) **Hint**: write the standard form of a hyperbola with a horizontal transverse axis.

> **Quick Recall:**
> - Rectangular hyperbola ⇔ asymptotes orthogonal.
> - y = 1/x ⇒ price elasticity = 1 (unitary) when used as demand curve.

---

## Section: Graphing Functions of Two Variables 🟡

### Core Idea
A function of two variables z = f(x, y) defines a **surface in three dimensions**. To visualise it on a 2D page, we use **contour lines** (level curves) — curves connecting all (x, y) values that produce the same z. This collapses 3D information into a 2D map, like geographical contour maps.

> **In Simple Terms:** A 3D surface is hard to draw on paper. So we slice it horizontally at fixed heights and project the slices down — that's a contour map.

### Definitions
- **Level curve (contour line)**: for a function f of two variables and a constant c, the set of pairs (x, y) such that f(x, y) = c. ⭐
- **Contour diagram (contour map)**: a 2D graph showing several level curves at various values of c.

### Examples

**Example: 3D graph of z = 2x² + 2y² − 4** — bowl-shaped (paraboloid) surface in 3D.

**Example (level curve)**: f(x, y) = x² + y².

The level curve for value 1 is x² + y² = 1, a circle of radius 1 centred at the origin.

### Connections
- Builds on: graphs of single-variable functions (earlier chunks).
- Prerequisite for: indifference curves, isoquants, Cobb-Douglas (chunk 015).

> **Quick Recall:**
> - z = f(x, y) ⇒ surface in 3D.
> - Level curve: f(x, y) = c (a constant). Different c values give different curves.
> - Economists' indifference curves and isoquants are level curves.
