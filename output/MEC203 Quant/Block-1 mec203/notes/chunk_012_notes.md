# Chunk 012 — Coordinate Geometry, Linear Graphing & Start of Non-Linear Graphing
<!-- Pages: 111-120 -->
<!-- Source: chunk_012.txt -->
<!-- Continuity: Continues Unit 4. Picks up Section 4.2 Coordinate Geometry (Cartesian system, translating figures to equations), then 4.3 Graphing Linear Functions (with absolute-value and step functions), and opens 4.4 Graphing Non-Linear Functions (even/odd, quadratic). Continues into chunk 013 with cubic, asymptotic, piecewise functions etc. -->

## Section: Coordinate Geometry — Big Picture & History 🟡

### Core Idea
**Coordinate geometry** (also called **analytical geometry** or **Cartesian geometry**) translates geometric objects into algebraic expressions using a coordinate system, then attacks geometric problems with algebraic tools. This contrasts with **synthetic geometry**, which proves results from axioms without coordinates.

> **In Simple Terms:** Instead of drawing and reasoning about shapes directly, label every point with numbers (coordinates) and reason about the numbers using algebra.

### Definitions
- **Coordinate / analytical / Cartesian geometry**: approach in which geometric objects (lines, planes, curves) are represented by algebraic equations, and problems are solved algebraically.
- **Synthetic geometry**: traditional axiomatic geometry (Euclidean style) using postulates and proofs without coordinates.

### Key Concepts
- Discipline named after **René Descartes** (17th-century French philosopher and mathematician); independently invented by **Pierre de Fermat** in the same century.
- Earlier traces in Greek mathematics and the work of 11th-century Persian mathematician **Omar Khayyam**.
- Other coordinate systems exist (polar, cylindrical, spherical, homogeneous, curvilinear) — each useful for specific problems.

---

## Section: Cartesian Coordinate System (2D) 🔴

### Core Idea
The 2D Cartesian (rectilinear) coordinate system uses two **mutually perpendicular** real number lines (axes) intersecting at the **origin**. Every point in the plane is uniquely identified by an ordered pair (x, y).

> **In Simple Terms:** Two perpendicular rulers, one horizontal and one vertical, meeting at zero. Any point's address is "(go x right, go y up)".

### Definitions
- **x-axis**: the horizontal number line. ⭐
- **y-axis**: the vertical number line. ⭐
- **Origin**: the intersection of the axes; both x = 0 and y = 0 there.
- **Quadrants**: four regions (numbered I, II, III, IV — usually with Roman numerals) bounded by the axes.
- **Abscissa**: the x-value of point P(x, y); perpendicular distance of P from the y-axis.
- **Ordinate**: the y-value of point P(x, y); perpendicular distance of P from the x-axis.
- **Coordinates of P**: the ordered pair (x, y).

### Key Concepts
- Convention: independent variable on the **horizontal** axis (x); dependent variable on the **vertical** axis (y).
- Order matters: x is **always** written first in the pair (x, y).
- Called "rectangular" because both axes use evenly-spaced scales.

### Examples
Points and their interpretations:
- (2, 3) — 2 right, 3 up (quadrant I).
- (−3, 1) — 3 left, 1 up (quadrant II).
- (−1.5, −2.5) — 1.5 left, 2.5 down (quadrant III).

> **Quick Recall:**
> - x first, y second.
> - Origin = (0, 0).
> - Abscissa = horizontal distance; ordinate = vertical distance.

### Connections
- Builds on real number line (Unit 1).
- Prerequisite for: graphing all functions (later sections).

---

## Section: Translating Geometric Figures to Algebraic Equations 🔴

### Core Idea
To convert a geometric figure into an algebraic equation, embed it in a coordinate system, take an arbitrary point P(x, y) on (or related to) the figure, and use the figure's geometric definition (similar triangles, distance, etc.) to derive an equation linking x and y.

### Mechanisms / Processes
1. Place the figure in a coordinate system; record coordinates of any "anchor" points.
2. Pick an arbitrary point P(x, y) on the figure.
3. Apply known geometric facts (similar triangles, Pythagoras, etc.).
4. Solve for the relation between x and y.

### Examples
**Example: Line through A(0, −2) and B(2, 0) (Fig 4.7)**
- Take P(x, y) outside segment AB; drop perpendicular PQ to x-axis at Q(x, 0).
- Triangles AOB and AQP are similar.
- |AO|/|AQ| = |BO|/|PQ|, i.e. 2/(x − 2) = 2/y.
- Cross-multiplying: 2y = 2(x − 2) ⇒ **y = x − 2**.

### Standard Algebraic Forms (memorize) ⭐

| Curve | Equation |
|---|---|
| Circle (centred at origin) | x² + y² = a² |
| Ellipse | (x/a)² + (y/b)² = 1 |
| Parabola | y² = 4ax (a > 0) |
| Hyperbola | (x/a)² − (y/b)² = 1 |
| Rectangular hyperbola | xy = c² |
| Sphere (3D) | (x − a)² + (y − b)² + (z − c)² = d², d > 0 |

> **Quick Recall:**
> - Circle: sum of squares = constant.
> - Ellipse: sum of normalized squares = 1.
> - Parabola (right-opening): y² = 4ax.
> - Hyperbola: difference of normalized squares = 1.

### Check Your Progress 1
Draw graph of y² = x + 5 and decide if it is a function.
**Hint:** y = ±√(x + 5). For each x > −5, two y-values exist → fails vertical line test → **NOT a function** (only a relation; specifically, a sideways parabola).

### Connections
- Builds on standard formulas from school geometry.
- Prerequisite for: graphing parabola, hyperbola, circle (Section 4.7).

---

## Section: Graphing Linear Functions 🔴

### Core Idea
A function y = f(x) is **linear** if x appears with power ≤ 1; it corresponds to a linear equation Ax + By + C = 0 where degrees of x and y are ≤ 1. The graph is always a **straight line** — and a straight line is determined by just two points.

### Definitions
- **Linear function**: y = f(x) where the highest power of x is 1.
- **Linear equation**: Ax + By + C = 0 with A, B, C constants and degrees of x, y at most 1.
- **t-chart**: a small table of (x, y) values used to plan a plot.
- **x-intercept**: point where graph crosses the x-axis (y = 0).
- **y-intercept**: point where graph crosses the y-axis (x = 0).

### Mechanisms / Processes
1. Pick any two values of x (often x = 0 and one other).
2. Compute corresponding y from y = f(x).
3. Plot the two points; draw a straight line through them.

For finding intercepts of Ax + By = C:
- **x-intercept**: set y = 0, solve for x.
- **y-intercept**: set x = 0, solve for y.

### Examples
**Example: y = 7 − 5x (t-chart)**

| x | y = 7 − 5x |
|---|---|
| −1 | 12 |
| 0 | 7 |
| 1 | 2 |
| 2 | −3 |
| 3 | −8 |

Only two points are strictly needed; e.g. x = −1 → y = 12 and x = 0 → y = 7 give the entire line.

**Example: 3x + 4y = 12 — find intercepts**
- x-intercept: y = 0 ⇒ 3x = 12 ⇒ x = 4 → point (4, 0).
- y-intercept: x = 0 ⇒ 4y = 12 ⇒ y = 3 → point (0, 3).
Plot (4, 0) and (0, 3); join with a line (Fig 4.9).

> **Quick Recall:**
> - Two points determine a line.
> - Intercept method: set the other variable = 0.

---

## Section: Absolute Value Function 🔴

### Core Idea
The absolute-value (modulus) function f(x) = |x| returns x without its sign, and splits into two linear pieces (one for x ≥ 0, one for x < 0). Its graph is a "V" — two straight rays meeting at a corner.

### Definitions
- **Absolute value**: |x| = x if x ≥ 0; |x| = −x if x < 0; |0| = 0.
- f(x) = |x| is defined piecewise:
  - y = x for x ≥ 0
  - y = −x for x < 0

### Examples
**Example: f(x) = |x|** — graph is a V with vertex at the origin (Fig 4.10).

**Example: f(x) = |x − 2|** (Fig 4.11)
- y-intercept: f(0) = |−2| = 2 → (0, 2).
- x-intercept: solve |x − 2| = 0 → x = 2 → (2, 0).
- Domain: all real numbers.
- Range: [0, ∞) (modulus is never negative).
- Graph: V-shape with vertex shifted to (2, 0).

### ⚠️ Common Mistakes
- ❌ Using the x-intercept / y-intercept method without checking that the line meets both axes → ✅ For f(x) = |x − 2|, equation y = 0 has solution x = 2 (the unique x-intercept), but the curve has only one y-intercept; intercept-only method may miss the V-corner.
- ❌ Forgetting the range is non-negative → ✅ |x| ≥ 0 always.

> **Quick Recall:**
> - |x| graph: V at the origin.
> - |x − a| graph: V at (a, 0).
> - Two linear pieces stitched at the corner.

---

## Section: Step Function (Greatest Integer Function) 🔴

### Core Idea
A **step function** (staircase function) is a piecewise function that takes constant values across adjacent intervals, jumping discretely from one constant to the next. It is **discontinuous** — you cannot draw it without lifting your pencil.

> **In Simple Terms:** Imagine a staircase: walk flat across each step, then suddenly jump up (or down) to the next.

### Definitions
- **Step / staircase function**: piecewise function whose pieces are all constants on adjacent intervals.

### Mechanisms / Processes (Floor / Greatest Integer)
1. For any real x, write x = Int-x + Fraction-x with 0 ≤ Fraction-x < 1.
2. Define f(x) = Int-x.

### Examples
- For x = 5.46: Int-x = 5, Fraction-x = 0.46 → f(5.46) = 5.
- For x = −3.87: Int-x = −4, Fraction-x = 0.13 → f(−3.87) = −4. (Note: floor of a negative non-integer rounds **down** to a more negative integer.)

**Domain**: union of all individual interval domains. **Range**: union of all output values across pieces.

### Edge Cases & Caveats
- The function is defined for all real x but is discontinuous at every integer.
- For piecewise functions in general, domain = union of all sub-domains; range = union of all sub-ranges.

### ⚠️ Common Mistakes
- ❌ Computing Int-x of −3.87 as −3 → ✅ It's −4 (the integer part rounded **down**).

> **Quick Recall:**
> - Step function = constant on each interval.
> - Discontinuous at every step jump.
> - Floor of negative: round more negative (−3.87 → −4).

### Check Your Progress 2
1. Graph y = (−5/3)x − 2 — straight line through (0, −2) and (3, −7).
2. Truck rental: Rs. 25 + Rs. 0.30/mile for 0–500 miles; Rs. 100 + Rs. 0.15/mile for >500 and <1000 miles. Step (piecewise) function:

   f(m) = { 25 + 0.30 m,   if 0 ≤ m ≤ 500
         { 100 + 0.15 m,  if 500 < m < 1000

---

## Section: Graphing Non-Linear Functions — Setup 🟡

### Core Idea
Non-linear functions (curves) require **more than two points** to graph reliably. Three points are usually still too few — the curvature can mislead. Plot a generous t-chart before sketching.

### ⚠️ Common Mistakes
- ❌ Plotting only 3 points of a quadratic and connecting them with straight lines → ✅ Use a denser t-chart (5–7 points spanning negative and positive x) and draw a smooth curve.

---

## Section: Even and Odd Functions 🔴

### Core Idea
Even and odd are **symmetry properties** of a function's graph. Even functions reflect across the **y-axis**; odd functions are symmetric about the **origin** (rotate 180° and you get the same picture).

> **In Simple Terms:** Even = mirror-image left-right. Odd = upside-down version of itself when flipped through the centre.

### Definitions
- **Even function**: f(−x) = f(x) for all x ∈ domain. ⭐ Graph is symmetric about the y-axis.
- **Odd function**: f(−x) = −f(x) for all x ∈ domain. ⭐ Graph is symmetric about the origin.

> **Note (chunk says even is "symmetric about origin"; this appears to be an OCR/textbook slip — the standard convention is even ↔ y-axis symmetry, odd ↔ origin symmetry, which is what the figures Fig 4.13 (even, y-axis symmetric) and Fig 4.14 (odd, origin symmetric) actually illustrate.)**

### Examples
- f(x) = x² is even: f(−3) = 9 = f(3).
- f(x) = x³ is odd: f(−3) = −27 = −f(3).
- f(x) = x³ − x is odd: f(−x) = −x³ + x = −(x³ − x) = −f(x).

### ⚠️ Common Mistakes
- ❌ Claiming a function is "either even or odd" → ✅ Most functions are neither (e.g., f(x) = x² + x).

> **Quick Recall:**
> - Even: f(−x) = f(x); y-axis mirror.
> - Odd: f(−x) = −f(x); origin (point) symmetry.

---

## Section: Quadratic Functions 🔴

### Core Idea
A **quadratic function** has the form f(x) = ax² + bx + c with a ≠ 0. Its graph is a **parabola** — opening upward if a > 0, downward if a < 0. The slope is not constant: as x grows by 1 the increase in y itself grows.

### Definitions
- **Quadratic function**: f(x) = ax² + bx + c with a ≠ 0.
- **Parabola**: the curve y = ax² + bx + c (or any rotation thereof).

### Examples
**Example: y = x² t-chart**

| x | −3 | −2 | −1 | 0 | 1 | 2 |
|---|---|---|---|---|---|---|
| y | 9 | 4 | 1 | 0 | 1 | 4 |

(Fig 4.15 shows the parabola.) As x increases by 1 starting at 0, y increases by 1, 3, 5, 7, ... (odd numbers — the differences increase). Same pattern as x decreases by 1 from 0.

### Key Concepts

| Sign of a | Parabola opens | Vertex is |
|---|---|---|
| a > 0 | upward | minimum |
| a < 0 | downward | maximum |

(See Fig 4.16.) Quadratic functions describe demand, cost, revenue, profit in microeconomics.

### ⚠️ Common Mistakes
- ❌ Connecting only three points of a parabola with straight segments → ✅ A parabola has continuously varying slope; plot more points and draw a smooth curve.
- ❌ Assuming "quadratic ⇒ symmetric about y-axis" → ✅ Only y = ax² is symmetric about the y-axis. The general y = ax² + bx + c is symmetric about the vertical line x = −b/(2a).

> **Quick Recall:**
> - Parabola: opens up if a > 0, down if a < 0.
> - Differences of y for unit steps in x form an arithmetic progression (odd numbers for y = x²).

### Connections
- Builds on basic algebra (factoring, completing the square — earlier units).
- Prerequisite for: vertex computation (Section 4.4.2.1, next chunk), conic sections (Section 4.7).

### Open Questions
- How do you locate the vertex of y = ax² + bx + c without graphing? (Answer: x = −b/(2a) — to be covered in chunk 013, Section 4.4.2.1 Computation of Vertex.)
- How does the parabola's "width" depend on a?
