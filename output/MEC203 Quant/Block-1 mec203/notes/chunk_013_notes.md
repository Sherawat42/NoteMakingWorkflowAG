# Chunk 013 — Quadratic Vertex, Cubic Functions, Asymptotic & Piecewise Graphs
<!-- Pages: 121-130 -->
<!-- Source: chunk_013.txt -->
<!-- Continuity: Continues Unit 4 "Coordinate Geometry and Representation of Functions" from earlier chunks. Builds on quadratic graphs introduced in Section 4.4.2 (parabolas, vertex shifting). Extends into cubic functions (4.4.3), asymptotic functions (4.5), and piecewise/rational functions (4.6). -->

## Section: Vertex Shifting and Axis of Symmetry of Parabolas 🔴

### Core Idea
A parabola y = x² has its vertex at the origin (0,0). Replacing x with (x−h) and adding k shifts the vertex to (h, k); these shifts preserve the U-shape. The axis of symmetry is the vertical line x = h that splits the parabola into mirror halves. Understanding shifts lets us sketch any quadratic without re-plotting from scratch.

> **In Simple Terms:** Think of y = x² as a paper cup template. Adding a number outside the squared term moves the cup up/down; subtracting inside the squared term slides it sideways. The "spine" of the cup (axis of symmetry) is always a vertical line through its lowest (or highest) point.

### Key Concepts

#### Vertical Shift
- Graph of y = x² + 3: same shape as y = x², shifted **up 3 units**; vertex moves to (0, 3).

#### Horizontal Shift
- Graph of y = (x + 3)²: shape unchanged, shifted **left 3 units**; vertex (−3, 0).
- Graph of y = (x − 3)²: shifted **right 3 units**; vertex (3, 0).
- Note the counter-intuitive sign: (x + 3)² shifts LEFT, not right.

#### Combined Shift
- y = (x − 2)² + 1: vertex (2, 1); axis of symmetry x = 2.

| Function form | Vertex | Direction of opening |
|---|---|---|
| y = x² | (0,0) | Upward (a > 0) |
| y = x² + k | (0, k) | Upward |
| y = (x − h)² | (h, 0) | Upward |
| y = (x − h)² + k | (h, k) | Upward |
| y = a(x − h)² + k, a < 0 | (h, k) | Downward |

### Definitions
- **Vertex**: the lowest point on an upward-opening parabola, the highest point on a downward-opening one. ⭐
- **Axis of symmetry**: the vertical line x = h that divides the parabola into two mirror-image halves. ⭐

> **Quick Recall:**
> - Vertex of y = a(x−h)² + k is (h, k).
> - Axis of symmetry: x = h.
> - "+k" lifts up; "(x − h)" slides right by h.

---

## Section: Computing the Vertex of a Generic Quadratic 🔴

### Core Idea
For any quadratic y = ax² + bx + c, completing the square produces y = a[(x + b/2a)² + k]. The squared term equals zero at x = −b/2a, so the parabola attains its extremum there. This gives a closed-form formula for the vertex coordinate without graphing.

> **In Simple Terms:** Every quadratic, no matter how messy, has a simple "balance point" at x = −b/2a. Plug that x back in to find the y. That's the tip of the cup.

### Mechanisms / Processes
1. Start with y = ax² + bx + c.
2. Factor a: y = a[x² + (b/a)x + c/a].
3. Complete the square: y = a[(x + b/2a)² − (b/2a)² + c/a].
4. Replace the constant tail with k: y = a[(x + b/2a)² + k].
5. Minimum (a > 0) or maximum (a < 0) occurs when (x + b/2a)² = 0, i.e., **x = −b/2a**.
6. y-coordinate: substitute x = −b/2a back into the original equation.

### Examples

**Example: Vertex of y = 3x² + x − 2**

Identify a = 3, b = 1, c = −2.

x-coordinate: x = −b/(2a) = −1/(2·3) = **−1/6**.

y-coordinate: substitute x = −1/6:
y = 3(−1/6)² + (−1/6) − 2
   = 3·(1/36) − 1/6 − 2
   = 1/12 − 2/12 − 24/12
   = **−25/12**

Vertex: **(−1/6, −25/12)**.

T-chart for plotting:

| x | y = 3x² + x − 2 |
|---|---|
| −2 | 8 |
| −1 | 0 |
| 0 | −2 |
| 1 | 2 |
| 2 | 12 |

### ⚠️ Common Mistakes
- ❌ Using x = +b/2a → ✅ Use x = −b/2a (note the negative sign).
- ❌ Confusing "axis x = h" with "x-intercept" — the axis is a vertical line, not a point.

> **Quick Recall:**
> - Vertex x = −b/2a for y = ax² + bx + c.
> - Sign of a determines max (a < 0) vs min (a > 0).

---

## Section: Cubic Functions 🔴

### Core Idea
A cubic function has the form f(x) = ax³ + bx² + cx + d. Cubics matter in microeconomics for total cost curves. The basic cubic f(x) = x³ passes through the origin with one x-intercept at (0, 0); the graph rises to the right and falls to the left when the leading coefficient is positive.

> **In Simple Terms:** A cubic looks like an "S lying on its side". For x³, both the domain and the range are all real numbers — it stretches from −∞ to +∞ in both directions.

### Key Concepts

#### Tracing f(x) = x³
- **y-intercept**: (0, f(0)) = (0, 0).
- **x-intercept**: solve x³ = 0 → only (0, 0).
- **Domain**: all real numbers.
- **Range**: all real numbers (because leading coefficient is positive, graph goes up on right, down on left).
- **Symmetry**: f(−x) = −f(x), so f is odd; graph is symmetric about origin.

| x | f(x) = x³ |
|---|---|
| −2 | −8 |
| −1 | −1 |
| 0 | 0 |
| 1 | 1 |
| 2 | 8 |

### Connections
- Connects to economics: cubic total cost curves (TC = aQ³ + bQ² + cQ + d) appear in microeconomic production theory.
- Builds on: odd/even function classification (earlier chunks).

### Check Your Progress 3
1) **Draw the graph for y = x³ − 2x.** [Solution from answer key: an "S"-shaped curve passing through origin with two extrema.]

---

## Section: Graphs of Asymptotic Functions — Horizontal & Vertical Asymptotes 🔴

### Core Idea
An asymptote is a line that a graph approaches but never touches. Horizontal asymptotes appear when a fraction's numerator stays bounded while the denominator grows without bound. Vertical asymptotes appear where the denominator approaches zero. The simplest example is y = 1/x, which has both x = 0 (vertical) and y = 0 (horizontal) as asymptotes.

> **In Simple Terms:** An asymptote is like a "wall the graph keeps getting infinitely close to but never crashes into".

### Definitions
- **Asymptote**: a line that a curve approaches arbitrarily closely as it heads toward infinity. ⭐
- **Horizontal asymptote**: a horizontal line y = L the graph approaches as x → ±∞.
- **Vertical asymptote**: a vertical line x = a the graph approaches as y → ±∞.

### Examples

**Example: y = 1/x**
- As x → +∞, y → 0⁺ (gets values 1/2, 1/3, 1/10, 1/10000, never quite 0).
- As x → 0⁺, y → +∞.
- Horizontal asymptote: y = 0. Vertical asymptote: x = 0.

**Example: y = 4/(x − 2)**
- Horizontal asymptote: y = 0. Vertical asymptote: x = 2.
- As x → 2⁻, denominator → 0⁻, fraction → −∞.
- At x = 2 exactly, function is undefined (division by zero).
- As x → 2⁺, fraction → +∞.

### Edge Cases & Caveats
- A function can have only horizontal, only vertical, both, or neither.
- (i) y = 1/(x−2) for 0 < x < 2: only x = 2 (vertical asymptote).
- (ii) x = 1/(y−2) for 0 < y < 2: only y = 2 (horizontal asymptote).

> **Quick Recall:**
> - Horizontal asymptote = behaviour at infinity (y-value).
> - Vertical asymptote = where denominator vanishes (x-value).

---

## Section: Square Root, Exponential, and Logarithmic Functions 🔴

### Core Idea
Three building-block "asymptotic" functions appear repeatedly in economics: the square-root function f(x) = √x (used in isoclines), the natural exponential f(x) = eˣ (growth and compounding), and the logarithm f(x) = log_b x (the exponential's inverse). Each has a distinctive graph shape and well-defined domain/range constraints.

> **In Simple Terms:** Square root grows slowly forever; exponential explodes upward; logarithm rises slowly but never stops, hugging the y-axis on the way up.

### Key Concepts

#### Square Root Function: f(x) = √x
- **Domain/Range**: [0, ∞).
- **Intercept**: (0, 0).
- Neither even nor odd; **strictly increasing** on (0, ∞).
- **Economics use**: depicts an isocline (locus where iso-quants relate). Converges to a point where output is maximised and marginal product is zero.

#### Exponential Function: y = aˣ (general form), y = eˣ (natural)
- e ≈ 2.718281828 (Euler's number).
- **Domain**: (−∞, ∞). **Range**: (0, ∞).
- Graph never touches or goes below x-axis (y > 0 always).
- **Applications**: compound interest, population growth, GDP growth, inflation, carbon dating.

#### Logarithmic Function: y = log_b x
- Inverse of exponential: if y = bˣ = f(x), then x = log_b y = g(y), and f(g(y)) = y, g(f(x)) = x.
- **Conditions**: b > 0, b ≠ 1, x > 0.
- **Behaviour**: when b > 1, log values increase; when 0 < b < 1, they decrease.
- Slowly tends to +∞ as x → ∞; tends to −∞ as x → 0⁺.
- **Domain**: positive reals (never zero). **Range**: all real numbers.
- Graph is **asymptotic to the y-axis** (gets close but never touches).

#### Three Common Bases
| Base b | Name | Used in |
|---|---|---|
| 10 | Common (decimal) logarithm | Science, engineering |
| e ≈ 2.718 | Natural logarithm (ln) | Mathematics, physics |
| 2 | Binary logarithm | Computer science |

For all bases: **log_b 1 = 0**.

### Check Your Progress 4
1) **f(x) = (x+1)/(x−1). Find x and y intercepts.**
   - x-intercept: f(x) = 0 ⇒ x + 1 = 0 ⇒ x = −1. So (−1, 0).
   - y-intercept: f(0) = 1/(−1) = −1. So (0, −1).
2) **Average fixed cost (AFC) curve — why asymptotic?**
   - AFC = TFC/Q. Since TFC is constant, AFC steadily falls as Q increases but never reaches zero (asymptotic to x-axis).

> **Quick Recall:**
> - √x defined for x ≥ 0.
> - eˣ > 0 always; y = 0 is its horizontal asymptote.
> - log_b 1 = 0 for any valid base; log graph asymptotic to y-axis.

---

## Section: Rational Functions and Piecewise Functions 🟡

### Core Idea
A rational function is the ratio of two polynomials, y = g(x)/h(x), with h(x) ≠ 0. Its domain excludes any x making h(x) = 0; near those values vertical asymptotes appear. Piecewise functions are defined by different formulas on different sub-intervals of the domain — graphed piece by piece.

> **In Simple Terms:** Rational functions are "polynomial fractions" — domain restrictions and asymptotes come from forbidding division by zero. Piecewise functions are like a recipe with different rules in different pages of the cookbook.

### Definitions
- **Rational function**: f(x) = g(x)/h(x) where g, h are polynomials and h ≠ 0. ⭐
- **Piecewise function** (split function): a function defined by different equations on different parts of the domain. ⭐

### Examples

**Example: y = 1/x (rational)**

T-chart:

| x | f(x) |
|---|---|
| −4 | −0.25 |
| −2 | −0.5 |
| −1 | −1 |
| −0.1 | −10 |
| −0.01 | −100 |
| 0.01 | 100 |
| 0.1 | 10 |
| 1 | 1 |
| 2 | 0.5 |
| 4 | 0.25 |

Graph splits into **two pieces** (one in each of two opposite quadrants). No intercepts. Vertical asymptote x = 0; horizontal asymptote y = 0.

**Example: Piecewise**

y = { x² − 2 if x ≤ 1 ; −2x + 4 if x > 1 }

Build separate T-charts for each piece, then graph each on its own interval. The "break" is at x = 1.

| x | y = x² − 2 |
|---|---|
| −4 | 14 |
| −3 | 7 |
| −2 | 2 |
| −1 | −1 |
| 0 | −2 |
| 1 | −1 |

| x | y = −2x + 4 |
|---|---|
| 1 | 2 |
| 2 | 0 |
| 3 | −2 |
| 4 | −4 |

### ⚠️ Common Mistakes
- ❌ Forgetting to exclude x-values where the denominator vanishes from the domain.
- ❌ Plotting both pieces of a piecewise function on the wrong interval — always restrict each formula to its prescribed range.

### Edge Cases & Caveats
- For y = 1/x, neither numerator nor denominator can produce an intercept; both axes are asymptotes.
- Piecewise functions may or may not be continuous at the break-point (continuity discussed in chunk 014).

### Connections
- Builds on: function definition and domain restrictions (Unit 3, earlier chunks).
- Prerequisite for: discontinuous functions (chunk 014), hyperbolas (chunk 014).

### Open Questions
- Why exactly two branches for y = 1/x and not more?
- How do horizontal asymptotes relate to the degrees of numerator and denominator?
