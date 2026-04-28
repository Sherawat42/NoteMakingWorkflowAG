# Complete Notes


## Section: Block 3 Roadmap & Unit 9 Front Matter 🟢

### Core Idea
Block 3 of MEC203 is *Calculus*. It is organised into four units that progress from limits, to single-variable derivatives, to multivariable derivatives, and finally to integration. Unit 9 lays the foundation: limits and continuity.

> **In Simple Terms:** Before you can do calculus, you must understand what it means for a function to "approach" a value (limit) and what it means for a function to be "smooth with no jumps" (continuity). Everything else — derivatives, integrals — is built on top of these two ideas.

### Key Concepts
- Block 3 contents: Unit 9 (Limit & Continuity), Unit 10 (Differential Calculus: One Variable), Unit 11 (Differential Calculus: Several Variables), Unit 12 (Integration).
- Unit 9 objectives: identify limit; evaluate left/right-hand limits; examine continuity; state properties of continuous functions; locate points of discontinuity.

---

## Section: Limit of a Function (§9.2) 🔴

### Core Idea
The limit captures the value a function "heads toward" as the input approaches a target — without requiring the function to be defined at that target. The phrase "x tends to a" means |x − a| can be made arbitrarily small. The limit `lim_{x→a} f(x) = t` exists when, for every preassigned ε > 0, there is a δ > 0 such that |f(x) − t| < ε whenever 0 < |x − a| < δ.

> **In Simple Terms:** Imagine walking toward a doorway. The limit is "what value the function would take if you arrived at the door". You don't need to actually walk through it — you just need to see where the path is heading.

### Key Concepts

#### One-sided approach
- Approach from the right: `x → a+` (also written `x → a + 0`), values strictly greater than a.
- Approach from the left: `x → a−` (also written `x → a − 0`), values strictly less than a.

#### ε–δ definition (analytical form)
The limit is t if, given any ε > 0 (no matter how small), we can choose δ > 0 such that `|f(x) − t| < ε` for all x with `0 < |x − a| < δ`. The notation `∀` reads "for all".

### Definitions
- **Limit of f(x) as x → a**: the unique number t (when it exists) such that f(x) can be made arbitrarily close to t by taking x sufficiently close to a (but not equal to a). ⭐ (exam-important)

### Examples
**Example 9.1(i): `lim_{x→1} (x² − 1)/(x − 1) = 2`**
At x = 1 + δ (δ small, ≠ 0): (x²−1)/(x−1) = 2 + δ. Taking δ → 0 makes this arbitrarily close to 2. The function itself is **not defined at x = 1** (0/0), yet the limit is 2.

**Example 9.1(ii): `lim_{x→1} (2x − 1) = 1`**
|f(x) − 1| = |2x − 2| = 2|x − 1|. For any ε > 0, choose δ = ε/2. Then |x − 1| < δ ⇒ |f(x) − 1| < ε.

> **Quick Recall:**
> - Limit answers "where is f(x) heading?" — does not require f(a) to exist.
> - ε–δ form: `∀ ε > 0, ∃ δ > 0 : 0 < |x − a| < δ ⇒ |f(x) − t| < ε`.

---

## Section: Right-Hand and Left-Hand Limits (§9.3) 🔴

### Core Idea
A two-sided limit exists only when both one-sided limits exist *and* are equal. They are written `f(a+0)` for the right-hand limit (RHL) and `f(a−0)` for the left-hand limit (LHL).

> **In Simple Terms:** Walk to the same door from two different sides of a hallway. If both directions lead you to the same spot, the "limit" exists. If they lead to different spots, there is no single limit.

### Key Concepts

#### Right-Hand Limit
For any ε > 0, ∃ δ > 0 such that |f(x) − t₁| < ε whenever `0 < x − a < δ` (i.e., `a < x < a + δ`). Denoted f(a + 0).

#### Left-Hand Limit
For any ε > 0, ∃ δ > 0 such that |f(x) − t₂| < ε whenever `0 < a − x < δ` (i.e., `a − δ < x < a`). Denoted f(a − 0).

#### Existence condition
`lim_{x→a} f(x)` exists ⟺ both `lim_{x→a+} f(x)` and `lim_{x→a−} f(x)` exist and are equal.

### Examples
**`lim_{x→0} |x|/x` does not exist.**
- RHL: for x > 0, |x|/x = +1, so `lim_{x→0+} = 1`.
- LHL: for x < 0, |x|/x = −1, so `lim_{x→0−} = −1`.
- Since 1 ≠ −1, the two-sided limit fails. Note also f(0) is undefined.

> **Quick Recall:**
> - Two-sided limit exists ⟺ RHL = LHL.
> - One-sided limits use only one approach direction.

---

## Section: Functions Tending to Infinity (§9.4) 🟡

### Core Idea
We say `lim_{x→a} f(x) = ∞` when, for any preassigned N (however large), there is a δ such that f(x) > N whenever 0 < |x − a| < δ. Symmetric definitions for −∞ and for x → ∞.

### Definitions
- **Limit at infinity**: `lim_{x→∞} f(x) = t` when, for every ε > 0, ∃ M > 0 such that |f(x) − t| < ε for all x > M.

### Examples
**Example 9.2(i):**
- `lim_{x→0+} 1/x = ∞` and `lim_{x→0−} 1/x = −∞`. Hence `lim_{x→0} 1/x` does **not** exist.

**Example 9.3:**
- `lim_{x→∞} 1/x = 0`; `lim_{x→−∞} 1/x = 0`.
- `lim_{x→∞} eˣ = ∞`; `lim_{x→−∞} x³ = −∞`.

> **Quick Recall:**
> - "Limit is ∞" is a *behaviour* statement, not a value — the limit technically does not exist as a finite number.

---

## Section: Fundamental Theorems on Limit (§9.5) 🔴

### Core Idea
If `lim f(x) = t₁` and `lim φ(x) = t₂` (both finite), the limit operator distributes over algebraic operations and many composite forms. Together with a small set of standard limits, these theorems mechanise most limit calculations.

### Key Concepts

#### Algebra of limits
1. `lim {f + φ} = t₁ + t₂` (sum)
2. `lim {f · φ} = t₁ · t₂` (product)
3. `lim {f / φ} = t₁ / t₂`, provided t₂ ≠ 0 (quotient)
4. `lim F[f(x)] = F[lim f(x)]` (continuous outer)
5. **Sandwich (squeeze) theorem**: if φ(x) ≤ f(x) ≤ ψ(x) near a, and `lim φ = lim ψ = t`, then `lim f = t`.
6. Order: if φ ≤ ψ near a, then t₁ ≤ t₂.

#### Standard limits to memorise
| Limit | Value |
|---|---|
| `lim_{x→0} sin x / x` | 1 (x in radians) |
| `lim_{x→∞} (1 + 1/x)^x` | e |
| `lim_{x→0} (1 + x)^{1/x}` | e |
| `lim_{x→0} log(1+x) / x` | 1 |
| `lim_{x→0} (eˣ − 1) / x` | 1 |
| `lim_{x→a} (xⁿ − aⁿ) / (x − a)` | n a^{n−1} (a > 0) |
| `lim_{x→0} ((1+x)ⁿ − 1) / x` | n |
| `lim_{n→∞} xⁿ / n!` | 0 |

### Examples
**Example 9.4(i): rational function with leading coefficients.**
`lim_{x→∞} (a₀ xⁿ + a₁ x^{n−1} + … + aₙ) / (b₀ xⁿ + b₁ x^{n−1} + … + bₙ) = a₀/b₀`
because every other term divided by xⁿ tends to 0.

**Example 9.4(ii): `lim_{x→π} sin x / (x − π)`**
Substitute z = x − π, so x = π + z; as x → π, z → 0.
`sin(π + z) = −sin z`. Then `lim_{z→0} −sin z / z = −1`.

**Example 9.4(iv): `lim_{n→∞} (1/n² + 2/n² + … + n/n²)`**
= `lim n(n+1) / (2n²) = (1/2) lim (1 + 1/n) = 1/2`.

**Example 9.4(v): `lim_{x→2−} √(x − 2)`** does not exist (square root undefined for x < 2 from the left).

> **Quick Recall:**
> - Quotient rule needs t₂ ≠ 0.
> - sin x / x → 1 only when x is in **radians**.
> - For polynomial-over-polynomial as x → ∞, ratio of leading coefficients wins.

### ⚠️ Common Mistakes
- ❌ Mistake: applying `lim f/g = lim f / lim g` when denominator limit is 0 → ✅ Correct: this is an indeterminate 0/0 (or ∞/∞) — needs algebraic simplification or L'Hôpital (Unit 10).
- ❌ Mistake: writing `lim sin x / x = 1` for x in degrees → ✅ Correct: only valid in radians.

---

## Section: Continuity (§9.6) 🔴

### Core Idea
A function is **continuous at x = a** if its graph has no "gap" at that point. Formally, `lim_{x→a} f(x)` exists, is finite, and equals f(a). Equivalently, both one-sided limits equal f(a). A function continuous at every point of its domain is **continuous on that domain**.

> **In Simple Terms:** Draw the function near x = a. If you can do it without lifting your pen, the function is continuous there. If you have to jump, leave a hole, or shoot off to infinity, it is discontinuous.

### Key Concepts

#### Three-part continuity test at x = a
1. f(a) exists.
2. `lim_{x→a} f(x)` exists (RHL = LHL).
3. The limit equals f(a).

#### Types of discontinuity
| Type | Characterisation | Example |
|---|---|---|
| **Ordinary** | RHL ≠ LHL | step function |
| **Removable** | RHL = LHL but ≠ f(a), or f(a) undefined | (x²−1)/(x−1) at x = 1 |
| **Infinite** | RHL or LHL is ±∞ | 1/x at x = 0 |
| **Oscillatory** | function oscillates without settling | (−1)^x at x → ∞ (finite or infinite oscillation) |

### Definitions
- **Continuous at x = a**: `lim_{x→a−} f(x) = lim_{x→a+} f(x) = f(a)`. ⭐ (exam-important)
- **Removable discontinuity**: a discontinuity that can be eliminated by redefining f(a) to equal the common one-sided limit. ⭐
- **Ordinary discontinuity**: f(a+0) ≠ f(a−0). ⭐

### Mechanisms / Processes
**Checking continuity at x = a:**
1. Compute f(a) — if undefined, it is at least a removable or essential discontinuity.
2. Compute LHL = `lim_{x→a−} f(x)`.
3. Compute RHL = `lim_{x→a+} f(x)`.
4. Compare: continuous ⟺ all three equal.

### Examples
**Example 9.5: `lim_{x→a} √(x − a)`** — for a removable case, f(a) may or may not exist.

**Example 9.6: f(x) = (x² − 1)/(x − 1).**
`lim_{x→1} f(x) = 2`, but f(1) is undefined (0/0). This is a *removable* discontinuity; defining f(1) = 2 makes f continuous.

**Example 9.7 (oscillatory):**
- (a) f(x) = (−1)^x oscillates finitely at infinity.
- (b) f(x) = (x²)^x oscillates infinitely.

### Properties of Continuous Functions (§9.6.1) — begins
- Sum, difference, and product of continuous functions are continuous (extends to any finite number of functions).
- Quotient is continuous wherever the denominator does not vanish.
- If f is continuous at a and f(a) ≠ 0, then f preserves sign in a neighbourhood of a.
<!-- Continues in chunk 002 -->

> **Quick Recall:**
> - Continuity at a needs three things: f(a) exists, the limit exists, the two are equal.
> - Removable: one redefinition fixes it. Ordinary: can't be fixed by redefining a single point.
> - Differentiability ⇒ continuity (proven in Unit 10), but continuous functions are not always differentiable.

### Connections
- Builds on: Limit (§9.2), One-sided limits (§9.3) — continuity is defined via limits.
- Is prerequisite for: Differentiability (Unit 10 §10.2) — you cannot have a derivative at a discontinuity (with rare infinite-derivative exceptions).

### Open Questions
1. Why does the |x| / x example fail to have a limit at 0 even though |x| and x are individually continuous?
2. Can a function be continuous at exactly one point? (yes — Dirichlet-type constructions, beyond syllabus.)


---


## Section: Properties of Continuous Functions — completion (§9.6.1) 🟡
<!-- See chunk 001 for start -->

### Core Idea
Continuity is preserved under arithmetic combinations and produces several global structural results — the foundation of the **Intermediate Value Theorem** (IVT) and the **Boundedness Theorem**, both used repeatedly later.

### Key Concepts

#### Intermediate Value Theorem (IVT)
If f is continuous on (a, b) and f(a), f(b) have **opposite signs**, then there exists at least one ξ ∈ (a, b) with f(ξ) = 0. More generally, f attains every value between f(a) and f(b) at least once on the interval.

#### Boundedness & extrema
- A function continuous on a *closed* interval is bounded there.
- Such a function actually **attains** its upper and lower bounds at least once each.

### Examples
**Example 9.8(i): xⁿ is continuous everywhere when n > 0 (rational); continuous everywhere except x = 0 when n < 0.**
**Example 9.8(ii): tan x = sin x / cos x is continuous except where cos x = 0, i.e., x = (2n+1)π/2.**
**Example 9.8(iii): f(x) = |x| (defined piecewise) is continuous at x = 0** even though it is not differentiable there.

> **Quick Recall:**
> - Sum, product, difference, composition of continuous → continuous.
> - Quotient continuous where denominator ≠ 0.
> - IVT (sign-change) gives existence of roots.

---

## Section: Unit 9 Sum-Up & Key Words (§9.7–§9.8) 🟢

### Core Idea
Unit 9 anchored two ideas: the *limit* (formal ε–δ definition; one-sided variants; algebra of limits and standard limits) and *continuity* (limit equals function value; classification of discontinuities; properties of continuous functions).

### Definitions
- **Limit** (Key Word, §9.8): the basic concept used to characterise the behaviour of a function around a point in its domain. Foundation of continuity and differentiability.
- **Continuity** (Key Word, §9.8): graphically, drawable in a neighbourhood without lifting the pen; formally, `lim_{x→a} f(x) = f(a)`.

---

## Section: Unit 9 Solved Problems (CYP & §9.10 Exercises) 🟡

### Worked Examples (selected)

**CYP1(i): `lim_{x→0} (√(a+x) − √(a−x))/x`**
Multiply numerator and denominator by the conjugate `√(a+x) + √(a−x)`:
`= lim 2x / [x(√(a+x) + √(a−x))] = 2 / (2√a) = 1/√a`.

**CYP1(iii): `lim_{x→θ} sin x = sin θ`** — uses the identity `sin x − sin θ = 2 sin((x−θ)/2) cos((x+θ)/2)` and squeeze.

**CYP2(ii): Discontinuity points of `f(x) = (x² − 2x + 4)/(x² − 5x + 6)`.**
Numerator and denominator are polynomials (continuous everywhere). The quotient is continuous where the denominator ≠ 0. `x² − 5x + 6 = (x−2)(x−3) = 0 ⇒ x = 2, 3` are the discontinuity points.

**CYP2(iii): Make `f(x) = (x² − 1)/(x² + x − 2)` continuous at x = 2.**
Wait — actually the form here simplifies via factorisation: `(x² − 1)/(x² + x − 2) = (x+1)(x−1)/[(x+2)(x−1)] = (x+1)/(x+2)` for x ≠ 1. To make continuous at x = 2 set f(2) = 4 (taking the limit value).

**§9.10 Q1: Show `lim_{x→a} (xⁿ − aⁿ)/(x − a) = n a^{n−1}` (a > 0).**
Factor: `xⁿ − aⁿ = (x − a)(x^{n−1} + x^{n−2} a + … + x a^{n−2} + a^{n−1})`. Cancel (x − a). Take x → a in the n-term sum to get `n · a^{n−1}`.

**§9.10 Q2: Show `lim_{x→0} ((1+x)ⁿ − 1)/x = n`.**
By binomial: (1+x)ⁿ = 1 + nx + n(n−1)/2 · x² + … + xⁿ. Subtract 1, divide by x, let x → 0: only the linear term survives, giving n.

**§9.10 Q3: `lim_{n→∞} xⁿ / n! = 0`.**
By Archimedean property pick natural k with x/k < 1; then for n > k, xⁿ/n! ≤ C · yⁿ where y < 1. Geometric series with ratio < 1 → 0.

> **Quick Recall:**
> - Conjugate trick handles `0/0` with square roots.
> - Polynomial in numerator/denominator: zeros of denominator = candidate discontinuities.
> - `xⁿ / n! → 0` is a fundamental "factorial beats power" fact.

---

## Section: Unit 10 Front Matter (§10.0–§10.1) 🟢

### Core Idea
Unit 10 introduces the derivative — a precise measure of *rate of change* — and applies it to economics (revenue, cost, elasticities), curve analysis (slope and curvature), and approximation (Taylor series, MVT, L'Hôpital).

### Key Concepts
- §10.0 Objectives: explain derivatives; geometric interpretation; economic applications; slope/curvature; MVT; L'Hôpital.
- §10.1 Introduction frames "change" as the central economic question.

---

## Section: §10.2 Derivative — Definition 🔴

### Core Idea
The derivative of f at x measures the limit of the average rate of change `Δy/Δx` as Δx → 0. When the limit exists, it is denoted `f'(x)`, `dy/dx`, `df/dx`, or `D f(x)`.

> **In Simple Terms:** Take two close points on the curve, draw the chord, measure the slope. Slide the second point closer and closer to the first. The limit of those chord-slopes is the **slope of the tangent** at the first point — that is the derivative.

### Key Concepts

#### Increment notation
- Δx (or h): an increment in the independent variable.
- Δy (or k): the corresponding increment in y = f(x), i.e., Δy = f(x + Δx) − f(x).

#### Definition
`f'(x) = dy/dx = lim_{Δx → 0} Δy/Δx = lim_{h→0} [f(x + h) − f(x)] / h`
provided this limit exists.

If `Δy/Δx → ±∞` as Δx → 0, the derivative is said to exist (as an "infinite" derivative).

#### Differentiability vs continuity (key relationship)
- **Differentiability ⇒ continuity** (a differentiable function must be continuous).
- **Continuity ⇏ differentiability** (continuous functions can lack derivatives).

### Examples
**Example 10.1: y = +√x, x increases from 4 to 4.1 (Δx = 0.1) ⇒ y goes from 2 to 2.025 (Δy = 0.025).**
Successive ratios Δy/Δx approach 0.25 — which is the derivative at x = 4 (i.e., 1/(2√4) = 0.25).

**Example 10.2: f(x) = |x| at x = 0 — continuous but not differentiable.**
- RHD: `lim_{h→0+} |h|/h = 1`.
- LHD: `lim_{h→0−} |h|/h = −1`.
- Right and left derivatives differ ⇒ f'(0) does not exist.

**Example 10.3: Discontinuous step but **infinite** derivative.**
The piecewise function with a jump at x = 1/2 fails continuity but has Δy/Δx → ∞ from both sides — derivative is "+∞" (a special degenerate case).

### Definitions
- **Right-hand derivative `R f'(x)`**: `lim_{h→0+} [f(x+h) − f(x)] / h`.
- **Left-hand derivative `L f'(x)`**: `lim_{h→0−} [f(x+h) − f(x)] / h`.
- **f'(x) exists** ⟺ R f'(x) and L f'(x) both exist and are equal. ⭐

### Mechanisms / Processes (first-principles derivative)
**Compute f'(x) for f(x) = 2x²:**
1. Write difference quotient: [f(x+h) − f(x)]/h = [2(x+h)² − 2x²]/h.
2. Expand: 2(x² + 2xh + h²) − 2x² = 4xh + 2h².
3. Divide by h: 4x + 2h.
4. Take h → 0: f'(x) = 4x.

> **Quick Recall:**
> - `f'(x) = lim_{h→0} [f(x+h) − f(x)]/h`.
> - For f' to exist at a, RHD = LHD.
> - Differentiable ⇒ continuous; converse fails (|x| at 0).

### ⚠️ Common Mistakes
- ❌ Mistake: assuming continuity guarantees differentiability → ✅ Correct: |x| is continuous everywhere but fails to be differentiable at 0.

---

## Section: Standard Derivatives & Rules of Differentiation 🔴

### Core Idea
Once the first-principles derivative is established for a few base functions, almost all calculus computations reduce to applying a small set of standard derivatives plus algebraic rules (constant, sum, product, quotient, chain, parametric).

### Key Concepts

#### Standard derivatives
| Function | Derivative |
|---|---|
| xⁿ (rational n) | n x^{n−1} |
| e^{mx} | m e^{mx} |
| aˣ | aˣ log_e a |
| log x (natural log) | 1/x |
| sin x | cos x |
| cos x | −sin x |
| tan x (x ≠ (2n+1)π/2) | sec² x |
| cot x (x ≠ nπ) | −cosec² x |
| sec x | sec x · tan x |
| cosec x | −cosec x · cot x |

x is in radians for trig functions.

#### Rules of differentiation
1. **Constant**: d(c)/dx = 0.
2. **Constant multiple**: d(c φ(x))/dx = c · dφ/dx.
3. **Sum**: d(φ + ψ)/dx = dφ/dx + dψ/dx (extends to finite sums).
4. **Product**: d(φψ)/dx = φ'ψ + φψ'.
5. **Quotient**: d(φ/ψ)/dx = (φ'ψ − φψ')/ψ².
6. **Chain rule (function-of-function)**: if y = f(v) and v = g(x), then `dy/dx = (dy/dv) · (dv/dx)`. Generalises: if y = f(v), v = φ(w), w = ψ(x), then `dy/dx = (dy/dv)(dv/dw)(dw/dx)`.
7. **Inverse function**: `dx/dy = 1 / (dy/dx)` provided both exist.
8. **Parametric**: if y = ψ(t), x = φ(t), then `dy/dx = (dy/dt)/(dx/dt)`, dx/dt ≠ 0.

> **Quick Recall:**
> - Memorise the standard table — it underpins every Unit 10 problem.
> - Chain rule is the workhorse: practise spotting "outside × inside".
> - Parametric form: keep a parameter t, differentiate each coordinate, take the ratio.

---

## Section: §10.3 Geometrical Interpretation of Derivatives — intro 🟡

### Core Idea
Geometrically, `f'(x₀)` is the slope of the tangent line to the curve y = f(x) at the point (x₀, f(x₀)). For a chord PQ between (x₀, y₀) and (x₀ + Δx, y₀ + Δy), the slope is Δy/Δx = QR/PR = tan φ (φ = angle with x-axis). As Q → P (Δx → 0), the chord rotates onto the tangent.

> **In Simple Terms:** Think of zooming in on a curve. The closer you zoom, the more the curve "looks like a straight line" — that line is the tangent, and its slope is f'.

<!-- Continues in chunk 003 (§10.4 Differentials, §10.5 Higher Order, §10.6 Economic Applications, §10.7 Slope and Curvature) -->

### Connections
- Builds on: Limit (Unit 9) — derivative is itself a limit.
- Is prerequisite for: Differentials (Chunk 003 §10.4); economic applications (Chunk 003 §10.6); Taylor series (Chunk 004 §10.8).

### Open Questions
1. Can a function have a derivative at a single isolated point? (related: differentiability vs continuity)
2. What is the geometrical meaning when f'(x) → ∞ at a point (vertical tangent)?


---


## Section: Differentiation Tricks (Logarithmic, Trig Simplification, Determinant) 🟡

### Core Idea
For complex compositions of products, powers, or ratios, transformations *before* differentiating often save labour. The three chief tricks: (i) logarithmic differentiation; (ii) trigonometric identity simplification; (iii) determinant differentiation column-by-column.

### Key Concepts

#### Logarithmic differentiation
For y = (cosec x)^{cot x}, take log first: `log y = cot x · log cosec x`. Differentiate both sides — the chain rule on the right yields a clean expression.

#### Trigonometric simplification
For `y = tan⁻¹[(√(1+sinx) − √(1−sinx)) / (√(1+sinx) + √(1−sinx))]`, multiply by conjugate / use half-angle: simplifies to `y = x/2`, hence `dy/dx = 1/2`.

#### Determinant differentiation
For Δ(x) = | row₁; row₂; row₃ | with each row a function of x:
Δ'(x) = | row₁'; row₂; row₃ | + | row₁; row₂'; row₃ | + | row₁; row₂; row₃' |
i.e., differentiate one row at a time and sum. The same rule holds column-wise.

### Examples
**Example 10.4(a): y = (cosec x)^{cot x}**
log y = cot x · log cosec x
(1/y) dy/dx = −cosec²x · log cosec x + cot x · (−cosec x cot x / cosec x)
= −(cosec²x · log cosec x + cot²x)
∴ dy/dx = −(cosec x)^{cot x} (cosec²x · log cosec x + cot²x).

**Example 10.5: 3×3 determinant with sin/cos rows.** Differentiating column-by-column and simplifying gives Δ'(x) = sin²x + cos²x = 1.

> **Quick Recall:**
> - log differentiation handles `f(x)^{g(x)}` cleanly.
> - For determinants of differentiable rows, differentiate one row/column per term and sum.

---

## Section: §10.4 Differentials 🔴

### Core Idea
Where a derivative `f'(x)` is a *rate*, the **differential** `df = f'(x) dx` is an *infinitesimal increment* — the linear approximation to the actual change Δf produced by an increment dx. Differentials behave like ordinary numbers in calculation and are central to integration.

> **In Simple Terms:** Imagine zooming in on a curve so it looks like a straight line. The differential dy is the change you'd predict using the tangent line; the actual change Δy is the change along the curve. They agree to first order in dx but differ for finite Δx.

### Key Concepts

#### Definition
For y = f(x), Δx an increment, the differential of f is:
`df(x) = f'(x) Δx` ... (10.1)
Taking f(x) = x ⇒ f'(x) = 1, so dx = Δx. Thus for the **independent** variable, dx = Δx.
Substituting back: `dy = f'(x) dx` ... (10.2).

#### Key relationship
`dy/dx = f'(x)` — so the derivative is also the *quotient* of differentials.

#### Rules for differentials
| Rule | Form |
|---|---|
| Constant | d(c) = 0 |
| Sum/diff | d(u + v − w) = du + dv − dw |
| Product | d(uv) = u dv + v du |
| Quotient | d(u/v) = (v du − u dv)/v² |

### Examples
**y = tan x ⇒ dy = sec² x · dx.**

> **Quick Recall:**
> - Δx = dx (independent var); Δy ≠ dy in general (Δy is exact, dy is linear approximation).
> - Differentials especially used for integration substitutions and total differential (Unit 11).

### ⚠️ Common Mistakes
- ❌ Mistake: writing Δy = dy as if always equal → ✅ Correct: only for the independent variable, or only "to first order in dx".

---

## Section: §10.5 Higher Order Derivatives 🟡

### Core Idea
The derivative of f(x) is itself a function, which can be differentiated again to give the **second derivative** f''(x), and so on for the n-th derivative f⁽ⁿ⁾(x).

### Notation
- f'(x), f''(x), …, f⁽ⁿ⁾(x).
- dy/dx, d²y/dx², d³y/dx³, …, dⁿy/dxⁿ.

### Examples
**Example 10.6: y = 4x⁵ + 7x⁴ + 3x + 9.**
- dy/dx = 20x⁴ + 28x³ + 3.
- d²y/dx² = 80x³ + 84x².
- d³y/dx³ = 240x² + 168x.

> **Quick Recall:**
> - Each successive differentiation typically reduces the degree of a polynomial by 1.
> - Some functions (sin x, cos x, eˣ) have predictable cyclic n-th derivatives.

---

## Section: §10.6 Application of Simple Derivatives in Economics 🔴

### Core Idea
Economics is full of functional relationships — and the *rate of change* of one variable due to another is exactly what derivatives compute. The chapter develops four canonical applications: AR/MR, AC/MC, point price elasticity, and the constant-elasticity demand curve.

### §10.6.1 Average Revenue (AR) and Marginal Revenue (MR)

#### Setup
- Inverse demand: `p = f(q)`. Total revenue: `R = p · q = f(q) · q`.
- **Average Revenue**: `AR = R/q = p = f(q)`.
- **Marginal Revenue**: `MR = dR/dq = f(q) + q · f'(q)`.

#### Key relationship
`MR = AR + q · f'(q)`

| Case | Sign of f'(q) | MR vs AR |
|---|---|---|
| Downward-sloping AR | f'(q) < 0 | MR < AR (MR below AR curve) |
| Upward-rising AR | f'(q) > 0 | MR > AR (MR above AR curve) |
| Horizontal AR (perfect competition) | f'(q) = 0 | MR = AR |

At q = 0: MR = AR = f(0) (curves intersect on the price axis).

### §10.6.2 Average Cost (AC) and Marginal Cost (MC)

- Total cost: `c = c(q)`. AC = c/q. MC = dc/dq.
- **Slope identity**: `d(AC)/dq = (1/q)(MC − AC)`.

| Case | AC | MC vs AC |
|---|---|---|
| AC falling | d(AC)/dq < 0 | MC < AC |
| AC rising | d(AC)/dq > 0 | MC > AC |
| AC at minimum | d(AC)/dq = 0 | MC = AC (curves cross at minimum AC) |

> **In Simple Terms:** Marginal pulls average up when above it, down when below it — like adding a higher-grade test pulls your average up.

### §10.6.3 Elasticity of Demand

#### Point price elasticity (e_p or ε_d)
For q = f(p):
`ε_p = (Δq/q × 100)/(Δp/p × 100) = (Δq/Δp)(p/q)`.
Taking Δp → 0:
`ε_p = (dq/dp)(p/q)` ... (10.3)

Demand curve typically slopes down (dq/dp < 0), so ε_p < 0; usually we report **|ε_p|**.

#### Classification
| |ε_p| | Demand category |
|---|---|
| 0 | perfectly inelastic |
| 0 < · < 1 | inelastic |
| = 1 | unitary elastic |
| 1 < · < ∞ | elastic |
| ∞ | perfectly elastic |

⚠️ Slope ≠ elasticity: two curves with the same slope can have different ε_p (depends on (p, q) point).

#### Income elasticity (η_d)
For q = f(y) (with price held fixed): `η_d = (dq/dy)(y/q)`.
- Luxury: η_d > 1 (demand rises more than proportionately with income).
- Necessity: 0 < η_d < 1.
- Inferior: η_d < 0.
- The graph q = q(y) is the **Engel curve**.

### §10.6.4 Constant Elasticity Demand Curve

For `q = A pᵅ` (A, α constants):
`ε_p = (p/q)(dq/dp) = (p/q)(A α p^{α−1}) = α (A pᵅ)/q = α`.

So ε_p = α everywhere on the curve — independent of (p, q). Special case α = −1: q = A/p, i.e., **pq = A**, a rectangular hyperbola.

### Definitions
- **Marginal Revenue**: derivative of total revenue w.r.t. quantity, MR = dR/dq. ⭐
- **Marginal Cost**: derivative of total cost w.r.t. quantity, MC = dc/dq. ⭐
- **Point price elasticity of demand**: ε_p = (dq/dp)(p/q). ⭐
- **Engel curve**: graph of demand against income, q = q(y). ⭐

### Examples
**Q: For p = aq² + bq + c, find ε_p and the q at which demand is unitary elastic.**
- dp/dq = 2aq + b ⇒ dq/dp = 1/(2aq + b).
- ε_p = (p/q)/(2aq + b) = (aq² + bq + c)/[q(2aq + b)] = (aq² + bq + c)/(2aq² + bq).
- Unitary: |ε_p| = 1 ⇒ aq² + bq + c = 2aq² + bq ⇒ aq² = c ⇒ q = √(c/a).

> **Quick Recall:**
> - MR = AR + q f'(q); for downward demand, MR < AR.
> - d(AC)/dq = (1/q)(MC − AC) ⇒ MC crosses AC at AC's minimum.
> - For q = A pᵅ, elasticity = α everywhere; α = −1 gives rectangular hyperbola.

### ⚠️ Common Mistakes
- ❌ Mistake: equating elasticity with slope → ✅ Correct: ε also depends on (p, q).
- ❌ Mistake: dropping the negative sign in elasticity sometimes loses information about good type → ✅ Correct: keep the sign or use absolute value consciously.

---

## Section: §10.7 Slope and Curvature 🔴

### Core Idea
The first derivative gives the *direction* of change (function rising or falling); the second derivative gives the *curvature* (convex, concave, or linear). Together they classify the local shape of a curve.

### Key Concepts

#### First derivative — slope / monotonicity
- f'(x) > 0 ⇒ f is increasing through x; tangent slopes upward.
- f'(x) < 0 ⇒ f is decreasing; tangent slopes downward.
- Monotonically increasing function: f'(x) > 0 ∀ x (in domain).
- Monotonically decreasing function: f'(x) < 0 ∀ x.

#### Second derivative — curvature
- f''(x) > 0 ⇒ **convex** (slope rising; curve bends upward; "cup-shaped").
- f''(x) < 0 ⇒ **concave** (slope falling; curve bends downward; "cap-shaped").
- f''(x) = 0 ⇒ linear (constant slope).

#### Cross-table of f' and f'' (six cases)
| f'(a) | f''(a) | Curve at a | Tangent rotation |
|---|---|---|---|
| > 0 | > 0 | upward, convex | turns anti-clockwise |
| > 0 | = 0 | upward, linear | does not turn |
| > 0 | < 0 | upward, concave | turns clockwise |
| < 0 | > 0 | downward, convex | turns anti-clockwise |
| < 0 | = 0 | downward, linear | does not turn |
| < 0 | < 0 | downward, concave | turns clockwise |

### Examples
**Example 10.8(i): y = 5x² + 6.** f''(x) = 10 > 0 — globally convex. (Note: source has f'' = 5 due to a typo; correct is 10. The qualitative conclusion stands: convex everywhere.)

**Example 10.8(ii): demand p = aq² + bq + c — find ε_p, conditions for unity elasticity.** (Worked above.)

**Example 10.8(iii): demand q = aq^b ... revenue R = a q^{b+1}.**
- MR = dR/dq = a(b+1) qᵇ > 0 for q > 0.
- d²R/dq² = a b (b+1) q^{b−1} > 0.
- ⇒ MR is upward-rising and convex.

### Definitions
- **Convex curve**: f''(x) > 0 — slope is increasing. ⭐
- **Concave curve**: f''(x) < 0 — slope is decreasing. ⭐
- **Monotonically increasing function**: f'(x) > 0 over its domain. ⭐

> **Quick Recall:**
> - f' sign = direction; f'' sign = bend.
> - Inflexion points: where f''(x) changes sign (≠ where f'' = 0 alone).

### Connections
- Builds on: Derivative (§10.2), Higher-order derivatives (§10.5).
- Is prerequisite for: Optimisation (Unit 11 §11.8 exercises) — second-order condition uses f''.
- Contrasts with: First-derivative test for extrema vs second-derivative test for curvature.

### Open Questions
1. Why does d(AC)/dq = (1/q)(MC − AC) imply MC and AC cross only at AC's minimum/maximum?
2. Can a curve be locally convex on the left of a point and concave on the right without f''(x) = 0 at the boundary? (No — continuity of f'' bridges the sign change at an inflexion point.)


---


## Section: §10.8 Taylor Series 🔴

### Core Idea
Many functions can be approximated near a point x = a by a polynomial whose coefficients are determined by f and its derivatives evaluated at a. This is the **Taylor expansion** — the central tool for local analysis, optimization conditions, and numerical evaluation.

> **In Simple Terms:** Imagine guessing a function near x = a. The constant term matches f(a). The linear term matches the slope (the tangent). The quadratic term curves the approximation correctly. Each higher-degree term refines the match. As you add more terms, the polynomial hugs the function more tightly.

### Key Concepts

#### Form of the polynomial
We seek `f_n(x) = a₀ + a₁(x − a) + a₂(x − a)² + … + aₙ(x − a)ⁿ` such that f_n agrees with f at x = a and its derivatives match up to order n.

Setting `x = a` and matching successive derivatives:
- a₀ = f(a)
- a₁ = f'(a)
- a₂ = f''(a)/2!
- ⋮
- aⱼ = f⁽ʲ⁾(a) / j!

#### Taylor series with Lagrange remainder
`f(x) = f(a) + f'(a)(x − a) + (f''(a)/2!)(x − a)² + … + (f⁽ⁿ⁾(a)/n!)(x − a)ⁿ + Rₙ`
where `Rₙ = f⁽ⁿ⁺¹⁾(x*)/(n+1)! · (x − a)^{n+1}` for some `x* = a + θ(x − a)`, 0 < θ < 1.

#### Maclaurin series
Special case **a = 0**:
`f(x) = f(0) + x f'(0) + (x²/2!) f''(0) + (x³/3!) f'''(0) + …`

### Definitions
- **Analytic function** (in this unit): one expressible as a power series of the above form. ⭐
- **Lagrange remainder**: the term `f⁽ⁿ⁺¹⁾(x*)(x − a)^{n+1}/(n+1)!` controlling truncation error.
- **Maclaurin series**: Taylor series centred at zero. ⭐

### Examples (from CYP2)
| f(x) | Maclaurin series |
|---|---|
| eˣ | `1 + x + x²/2! + x³/3! + … + xⁿ/n! + …` |
| sin x | `x − x³/3! + x⁵/5! − x⁷/7! + …` |
| cos x | `1 − x²/2! + x⁴/4! − x⁶/6! + …` |
| log(1 + x) | `x − x²/2 + x³/3 − x⁴/4 + …` (defined for −1 < x ≤ 1) |

> **Quick Recall:**
> - Taylor at a; Maclaurin at 0.
> - aⱼ = f⁽ʲ⁾(a)/j!.
> - Series for log(1+x) converges only for −1 < x ≤ 1.

### ⚠️ Common Mistakes
- ❌ Mistake: applying Maclaurin to functions like log x at x = 0 → ✅ Correct: log x is undefined at 0; use log(1 + x) instead.

---

## Section: §10.9 Mean Value Theorem (MVT) and L'Hôpital's Rule 🔴

### Core Idea
The **MVT** says that if a function is smooth enough on an interval, its average rate of change over the interval is realised at some interior point. **L'Hôpital's Rule** uses derivatives to evaluate indeterminate-form limits (0/0, ∞/∞).

### Key Concepts

#### Mean Value Theorem (MVT)
If (i) f is continuous on the closed interval [a, b], and (ii) f' exists on the open interval (a, b), then ∃ c ∈ (a, b) such that:
`f(b) − f(a) = (b − a) · f'(c)`

Equivalent (set b = a + h, c = a + θh, 0 < θ < 1):
`f(a + h) = f(a) + h · f'(a + θh)`

#### Derivation from Taylor (n = 1)
Putting n = 1 in the Taylor formula and writing R₀ = f'(a)(x − a) gives the **linearisation** of f.

#### L'Hôpital's Rule
If `f(x) = g(x)/h(x)` with both g, h → 0 (or both → ∞) as x → a, then:
`lim_{x→a} g(x)/h(x) = lim_{x→a} g'(x)/h'(x)` (if the latter limit exists).

### Examples
**Example 10.9(a): `lim_{x→0} (eˣ − 1)/x`** — both → 0/0.
g(x) = eˣ − 1, h(x) = x. g'(x) = eˣ, h'(x) = 1. Limit = e⁰/1 = **1**.

**Example 10.9(b): `lim_{x→0} ((1+x)ⁿ − 1)/x`** — 0/0.
g'(x) = n(1+x)^{n−1}, h'(x) = 1. Limit = n.

**CYP2(2)(i): `lim_{x→0} log(1+x)/x = 1`** by L'Hôpital (1/(1+x) over 1).

**CYP2(2)(ii): `lim_{x→1} (x³ + 3x − 4)/(2x² + x − 3)`**
0/0 ⇒ apply L'Hôpital: (3x² + 3)/(4x + 1). At x = 1: 6/5 — wait, source says 3/2; checking: (3·1+3)/(4·1+1) = 6/5. Source gives 3/2 but appears to drop the +3 term mid-step (OCR/typesetting confusion). The robust approach: factor `(x−1)` out of both numerator and denominator and evaluate cleanly.

### Definitions
- **Mean Value Theorem**: existence of c ∈ (a, b) where instantaneous rate equals average rate. ⭐
- **L'Hôpital's Rule**: the limit of a 0/0 (or ∞/∞) ratio equals the limit of the derivative ratio (if it exists). ⭐
- **Linearisation**: first-order Taylor approximation, f(x) ≈ f(a) + f'(a)(x − a).

> **Quick Recall:**
> - MVT requires continuity on [a,b] *and* differentiability on (a,b).
> - L'Hôpital applies only after confirming an indeterminate form (0/0 or ∞/∞).
> - MVT + Taylor at n=1 gives linearisation.

### ⚠️ Common Mistakes
- ❌ Mistake: applying L'Hôpital without checking indeterminate form → ✅ Correct: confirm 0/0 or ∞/∞ first; otherwise the rule gives a wrong answer.
- ❌ Mistake: differentiating numerator and denominator using the quotient rule → ✅ Correct: differentiate them **separately** (not as a quotient).

---

## Section: §10.10–§10.12 Sum-Up, Key Words, CYP Solutions 🟢

### Unit 10 Sum-Up (§10.10)
Unit 10 covered: differentiation rules; AR/MR, AC/MC, elasticity (price + income); slope and curvature; and three theorems — Taylor, MVT, L'Hôpital.

### Key Words (§10.11)
- **Derivative**: the limiting value of the ratio of change in a function to the corresponding change in its independent variable.
- **Differential coefficient (or derivative)**: a measure of the rate of change of a given function.
- **L'Hôpital's Rule**: used to evaluate indeterminate forms — limit equals limit of derivative ratio.
- **Mean Value Theorem**: ∃ point where derivative equals slope of secant joining endpoints.
- **Taylor Series**: infinite sum giving f(z) near a in terms of derivatives at a.

### Selected CYP1 derivative results
| f(x) | dy/dx |
|---|---|
| sin²x − eˣ + 4ˣ | sin 2x − eˣ + 4ˣ log_e 4 |
| 3x² cosec x | 3 cosec x (2x − cot x) |
| (log x − sin x)/(2x² − 1) | [(2x²−1)(1/x − cos x) − 4x(log x − sin x)] / (2x² − 1)² |
| 2 cos v + tan² v, v = e^{3x} | 6 e^{3x}[tan(e^{3x}) sec²(e^{3x}) − sin(e^{3x})] |
| x = b sin θ, y = a cos θ | −(a/b) tan θ |

### CYP1(3) — n-th derivatives
- d^n(eˣ)/dxⁿ = eˣ for all n.
- d^n(sin x)/dxⁿ cycles: sin x → cos x → −sin x → −cos x → sin x …
- d^n(log(1+x))/dxⁿ = (−1)^{n−1}(n−1)! · (1+x)^{−n}.

### Selected §10.13 Exercises (Solved)
**Q1: AC = q² − 2q + 5, max capacity 30 units.** d(AC)/dq = 2q − 2 ⇒ AC decreases for 0 < q < 1, increases for 1 < q < 30.

**Q2: c = a e^{bq}.** AC = (a e^{bq})/q; MC = ab e^{bq}. AC = MC ⇒ q = 1/b.

**Q3: Production q = −L³/3 + 2L² + 12L.** APL = q/L = −L²/3 + 2L + 12. d(APL)/dL = −2L/3 + 2 = 0 ⇒ L = 3. Beyond L = 3, average product diminishes.

**Q4: Demand p^k = a/q (i.e., q p^k = a, or q = a p^{−k}).** ε_p = −k. (Source's reasoning: −k log p = log a − log q; differentiate both sides; ε_p = q · (1/q) · (−k/p) · p / 1 = −k.)

**Q5: c = q³/3 − q² + q + 5.** MC = q² − 2q + 1 = (q − 1)²; d(MC)/dq = 2(q − 1). For q < 1, MC is decreasing; for q > 1, MC increasing — so for "continually right" q the behaviour switches at q = 1.

> **Quick Recall:**
> - Plug-and-chug exercises drill chain rule + quotient rule fluency.
> - For optimisation, set d/dq = 0 and check second derivative.

---

## Section: Unit 11 Front Matter (§11.0–§11.1) 🟢

### Core Idea
Unit 11 generalises differentiation to functions of *several* variables — central to all real-world economics where outputs depend on multiple inputs (utility on goods, output on labour and capital, demand on price *and* income).

### §11.0 Objectives
- Define partial derivatives.
- Compute higher-order and cross-partial derivatives (Young's theorem).
- Distinguish total derivative vs total differential.
- Identify homogeneous functions (Cobb–Douglas as a key example) and use Euler's theorem.

---

## Section: §11.2 Concept of Partial Differentiation 🔴

### Core Idea
When y depends on x₁, x₂, …, the **partial derivative** of y with respect to xᵢ measures how y changes if xᵢ alone varies — all other variables held constant. This is the natural multivariate generalisation of the single-variable derivative.

> **In Simple Terms:** In a recipe for cake quality y = f(flour, sugar, time), the partial derivative ∂y/∂flour answers: "if I change *only* the flour and keep sugar and time fixed, by how much does cake quality change per gram of flour?" Total change is something different (handled by total differential / total derivative).

### Key Concepts

#### Setting up bivariate case
For y = f(x₁, x₂):
- Change x₁ alone (x₂ fixed) ⇒ partial derivative w.r.t. x₁ — denoted `∂y/∂x₁`, `f₁`, `f_{x₁}`.
- Change x₂ alone ⇒ ∂y/∂x₂.
- If x₁ and x₂ are *related* (e.g., x₂ depends on x₁), the **total derivative** of y w.r.t. x₁ accounts for both direct and indirect effects.

#### Why this matters
Most economic problems are multivariate:
- Utility U = f(x₁, x₂, …) of multiple goods.
- Production Q = f(L, K, land, …).
- Demand q = f(p, y) of price and income.

<!-- Continues in chunk 005: §11.2.1 Partial derivative defined formally, examples, higher orders, cross-partials -->

### Connections
- Builds on: Derivative (§10.2) — partial derivative is the single-variable derivative applied along one axis.
- Is prerequisite for: Total differential, total derivative (§11.3); MRTS, elasticity of substitution (§11.4.3); homogeneous functions and Euler's theorem (§11.4.4).

### Open Questions
1. How does Young's theorem (cross-partials equal) interact with discontinuous second derivatives?
2. When two variables are related, why is the *total* derivative the relevant economic concept rather than the partial?


---


## Section: §11.2.1 Partial Derivative — Formal Definition 🔴
<!-- See chunk 004 for §11.2 intro -->

### Core Idea
The partial derivative of U = f(x₁, x₂) with respect to x₁ at a point is the limit of ΔU/Δx₁ as Δx₁ → 0 with x₂ held fixed. It is the slope of the "x₁-cross-section" of the surface.

### Key Concepts

#### Definition
Difference quotient:
`ΔU/Δx₁ = [f(x₁ + Δx₁, x₂*) − f(x₁*, x₂*)] / Δx₁`
Limiting value as Δx₁ → 0:
`f₁ = ∂U/∂x₁ = lim_{Δx₁→0} [f(x₁ + Δx₁, x₂) − f(x₁, x₂)] / Δx₁`

Symmetric definition for f₂ = ∂U/∂x₂.

#### Marginal interpretation in economics
If U = f(x₁, x₂) is a utility function, then `∂U/∂xᵢ` is the **marginal utility of good i** — the additional utility from one more unit of xᵢ, keeping the other goods fixed.

### Examples
**Example 11.1: f(x₁, x₂) = x₁³ + 2 x₁² x₂ + 3 x₁ x₂² + 4 x₂³.**
Treat x₂ as constant when differentiating w.r.t. x₁:
- f₁ = 3 x₁² + 4 x₁ x₂ + 3 x₂².
- f₂ = 2 x₁² + 6 x₁ x₂ + 12 x₂². (Source: 2 x₁² + 3x₁ + 8x₂ — appears truncated by OCR; the correct form is via differentiating each term w.r.t. x₂.)

### Definitions
- **Partial derivative ∂U/∂xᵢ**: derivative of U with respect to xᵢ holding all other variables constant. ⭐
- **Marginal utility (in economics)**: ∂U/∂xᵢ for a utility function U. ⭐

> **Quick Recall:**
> - To compute ∂f/∂xᵢ, treat all other xⱼ (j ≠ i) as constants and differentiate as in single-variable calculus.

---

## Section: §11.2.2 Higher Order Partial Derivatives 🟡

### Core Idea
Partial differentiating a partial derivative gives second- (and higher-) order partials. The notation: `f_{ij} = ∂²f / (∂xⱼ ∂xᵢ)` (differentiate w.r.t. xⱼ then w.r.t. xᵢ — orders matter notationally, though often equal by Young's theorem).

### Examples
**Example 11.2(i): z = 6x² + 5x³ + 10xy.**
- z_x = 18x + 15x² + 10y. (Source has 18x²+10x+10y; reading the source `6x²+5x³+10xy`, derivative is `12x + 15x² + 10y` — but the OCR may have mangled coefficients. Treat coefficients with care; the qualitative method is right.)
- z_{xx} = 12 + 30x.

**Example 11.2(ii): f(x₁, x₂) = e^{x₁ + x₂} + 3 x₁ x₂.**
- f₁ = e^{x₁+x₂} + 3 x₂.
- f₁₁ = e^{x₁+x₂}; (derivative of 3x₂ w.r.t. x₁ is 0).

> **Quick Recall:**
> - Differentiate the lower-order partial, treating other variables as constants.
> - When f no longer depends on a variable, further partials in that variable are 0.

---

## Section: §11.2.3 Cross-Partial Derivatives & Young's Theorem 🔴

### Core Idea
The two ways of computing a mixed second partial derivative — first w.r.t. x₁ then x₂, vs first w.r.t. x₂ then x₁ — give the **same result** under mild conditions (Young's theorem / Schwarz's theorem). This is a powerful symmetry used pervasively in economics (e.g., to show MRS = price ratio in equilibrium implies symmetric income effects).

### Key Concepts

#### Definitions
`f₁₂ = ∂f₁/∂x₂` and `f₂₁ = ∂f₂/∂x₁`.

#### Young's theorem
**`f₁₂ = f₂₁`** when both partials exist and (at least) one is continuous. Generalises to n variables: `f_{ij} = f_{ji}` for all i, j.

### Examples
**Example 11.3(i): f(x, y) = x³ + y⁵ + 4 x² y³ + 2xy.**
- f_x = 3x² + 8xy³ + 2y.
- f_y = 5y⁴ + 12 x² y² + 2x. (Source: 5y⁴ + 16 x²y² + 2x — coefficient 16 vs 12; checking `4 x² y³` derivative w.r.t. y is `12 x² y²`. OCR error in source.)
- f_{xy} = 24 xy² + 2 = f_{yx} (verifying symmetry).

**Example 11.3(ii): f(x₁, x₂) = log(x₁² + x₂²).**
- f₁ = 2x₁ / (x₁² + x₂²).
- f₂ = 2x₂ / (x₁² + x₂²).
- f₁₂ = f₂₁ = −4 x₁ x₂ / (x₁² + x₂²)² (Young verified).

### Definitions
- **Cross-partial derivative** f₁₂: differentiate f first w.r.t. x₁, then w.r.t. x₂. ⭐
- **Young's theorem**: f₁₂ = f₂₁ when one of the mixed partials is continuous. ⭐

> **Quick Recall:**
> - Young's theorem ⇒ order of mixed differentiation does not matter (under mild regularity).
> - Symmetric Hessian — used in second-order conditions for optimisation.

### ⚠️ Common Mistakes
- ❌ Mistake: assuming f₁₂ = f₂₁ always → ✅ Correct: requires continuity (or both existing as continuous functions); pathological constructions exist where it fails.

---

## Section: §11.3 Total Differential and Total Derivative 🔴

### Core Idea
Two distinct generalisations of dy = f'(x) dx exist for multivariate functions:
- **Total differential** dy: linear approximation of total change in y when *several* x's change *independently*.
- **Total derivative** dy/dt: rate of change of y when the xᵢ are themselves functions of a single variable t (chain rule).

### §11.3.1 Total Differential
For y = f(x₁, x₂):
**`dy = f₁ dx₁ + f₂ dx₂`**
This is the linear approximation to Δy = f(x₁ + Δx₁, x₂ + Δx₂) − f(x₁, x₂) — exact only in the limit, an approximation for small finite Δ.

### §11.3.2 Total Derivative (Chain Rule for one parameter)
If y = f(x₁, x₂) with x₁ = φ(t), x₂ = ψ(t):
**`dy/dt = f₁ · dx₁/dt + f₂ · dx₂/dt`**
Generalises to n variables.

### Examples
**Example 11.4: y = ax₁² + 2h x₁ x₂ + b x₂².**
- dy = (2ax₁ + 2h x₂) dx₁ + (2h x₁ + 2b x₂) dx₂
     = 2(ax₁ + h x₂) dx₁ + 2(h x₁ + b x₂) dx₂.

**Example 11.5(i): q = 4x₁ + 3x₂; x₁ = t³ + t² + 1, x₂ = t³ − t² − t.**
- f₁ = 4, f₂ = 3.
- dx₁/dt = 3t² + 2t.
- dx₂/dt = 3t² − 2t − 1.
- dq/dt = 4(3t² + 2t) + 3(3t² − 2t − 1) = 12t² + 8t + 9t² − 6t − 3 = **21t² + 2t − 3**.

### Definitions
- **Total differential** of y: dy = Σᵢ fᵢ dxᵢ. ⭐
- **Total derivative**: dy/dt = Σᵢ fᵢ · dxᵢ/dt when xᵢ depend on t. ⭐

> **Quick Recall:**
> - Total differential measures actual change when *multiple* variables change.
> - Total derivative composes via chain rule when *all* variables depend on one parameter.
> - Partial derivative is the building block; total versions sum the contributions.

---

## Section: §11.4 Differentiation & Applications — Chain Rule Cases (§11.4.1) 🔴

### Core Idea
Four standard chain-rule patterns cover most multivariate compositions encountered in practice.

| Case | Setup | Resulting derivatives |
|---|---|---|
| I | z = f(u), u = u(x, y) | ∂z/∂x = f'(u) · ∂u/∂x; ∂z/∂y = f'(u) · ∂u/∂y |
| II | z = f(x, y), x = φ(t), y = ψ(t) | dz/dt = (∂z/∂x) φ'(t) + (∂z/∂y) ψ'(t) |
| III | z = f(x, y), y = y(x) | dz/dx = ∂z/∂x + (∂z/∂y) · dy/dx |
| IV | z = f(x, y); x = φ(u, v), y = ψ(u, v) | ∂z/∂u = (∂z/∂x)(∂x/∂u) + (∂z/∂y)(∂y/∂u); similarly ∂z/∂v |

### Differential rules (multivariate)
| Rule | Form |
|---|---|
| Sum | d(u + v) = du + dv |
| Product | d(uv) = u dv + v du |
| Quotient | d(u/v) = (v du − u dv)/v² |
| Logarithm | d(log x) = dx/x |
| Compound | d(uv/w) = du/u + dv/v − dw/w (multiplied by uv/w) |

> **Quick Recall:**
> - Case III is the implicit-function chain rule (used heavily next subsection).
> - Case IV is the change-of-variables chain rule (used in optimisation transforms).

---

## Section: §11.4.2 Implicit Functions 🔴

### Core Idea
Many economic equations don't isolate y in terms of x — instead they tie x and y together by an equation `f(x, y) = 0`. The **implicit function theorem** lets us extract dy/dx from this without ever solving for y.

### Key Concepts

#### First derivative (implicit)
View f(x, y) = 0 as z = f(x, y) with z constant ≡ 0:
`dz = f_x dx + f_y dy = 0` ⇒ **`dy/dx = − f_x / f_y`**

#### Reciprocal property
By symmetry, `dx/dy = − f_y / f_x`. The two derivatives are reciprocals.

#### Second derivative (formula 11.1)
`d²y/dx² = −[f_{xx} · f_y² − 2 f_{xy} · f_x f_y + f_{yy} · f_x²] / f_y³`

### Examples
**Example 11.6: f(x, y) = 2x² + 3xy + 4y² = 0.**
f_x = 4x + 3y, f_y = 3x + 8y. ⇒ **dy/dx = −(4x + 3y)/(3x + 8y)**.

**Example 11.7: f(x, y) = x³ + xy + y³.** (Source has slight OCR mangling; standard worked: dy/dx = −(3x² + y)/(x + 3y²); d²y/dx² is computed via formula 11.1.)

> **Quick Recall:**
> - For f(x, y) = 0: dy/dx = −f_x / f_y. **The minus sign is essential.**
> - Second derivative uses the symmetric formula in f's second partials.

### ⚠️ Common Mistakes
- ❌ Mistake: forgetting the minus sign in dy/dx = −f_x/f_y → ✅ Correct: it comes from rearranging f_x dx + f_y dy = 0.

---

## Section: §11.4.3 Applications — MRTS & Elasticity of Substitution 🔴

### Marginal Rate of Technical Substitution (MRTS)

For production Y = f(L, K):
- Total differential: `dY = f_L dL + f_K dK`.
- Along an isoquant (constant Y), dY = 0 ⇒ `f_L dL + f_K dK = 0`.
- Rearranging: **`MRTS = −dK/dL = f_L / f_K`** (ratio of marginal products).

> **In Simple Terms:** MRTS tells you how much capital you can give up while still producing the same output, per extra unit of labour. If labour is more productive at the margin, you can substitute more capital for less labour.

### Elasticity of Substitution (σ)

#### Definition
`σ = % change in (x₁/x₂) / % change in (f₂/f₁)`
or
`σ = [d(x₁/x₂)/(x₁/x₂)] / [d(f₂/f₁)/(f₂/f₁)]`

#### Algebraic formula (after substitution)
`σ = f₁ f₂ (f₁ x₁ + f₂ x₂) / [x₁ x₂ (2 f₁ f₂ f₁₂ − f₁² f₂₂ − f₂² f₁₁)]`

#### Sign and interpretation
- Convexity of isoquant ⇒ denominator (2 f₁ f₂ f₁₂ − f₁² f₂₂ − f₂² f₁₁) > 0.
- (x₁, x₂, f₁, f₂) > 0 ⇒ σ > 0.
- σ inversely proportional to *degree of convexity* of isoquant: more curved isoquant ⇒ less substitutability ⇒ smaller σ.

#### Limiting cases
| Production type | Isoquant shape | σ |
|---|---|---|
| Leontief (fixed proportions) | L-shaped | 0 |
| Cobb–Douglas | smooth, downward, convex | 1 |
| Perfect substitutes | straight line | ∞ |

#### Notes
- σ varies from one (x₁, x₂) combination to another — σ is a function of (x₁, x₂).
- σ symmetric: σ_{x₁ x₂} = σ_{x₂ x₁}.
- For **linear-homogeneous** production: `σ = f_L · f_K / (q · f_{LK})` — inversely proportional to cross-second-order partial.

### Definitions
- **MRTS**: ratio f_L / f_K of marginal products along an isoquant. ⭐
- **Elasticity of substitution σ**: percentage change in input ratio per percentage change in MRTS. ⭐

> **Quick Recall:**
> - MRTS = f_L / f_K (signed positive when isoquant slopes down).
> - σ = 0: no substitutability (Leontief). σ = ∞: perfect substitutes. σ = 1: Cobb–Douglas.
> - Higher σ ⇔ flatter isoquants ⇔ easier factor substitution.

---

## Section: §11.4.4 Homogeneous Functions and Their Properties (begins) 🔴

### Core Idea
A function is **homogeneous of degree n** if scaling all arguments by a constant k scales the function value by `kⁿ`. Cobb–Douglas, CES, and many production / utility functions in economics are homogeneous — and homogeneity yields three powerful properties.

### Definition
`f(k x₁, k x₂) = kⁿ · f(x₁, x₂)` ⇒ degree of homogeneity = n.

For a homogeneous function, the **sum of indices in each term** is the same constant n.

### Examples (degree-checking)
- f(x₁, x₂) = x₁² + x₁ x₂ + x₂² is **degree 2** (each term sums to 2).
- z = x³ y + x² y² + y⁴ is **degree 4**.

### Property 1
A degree-n homogeneous function can always be written in either of two reduced forms:
`z = xⁿ · φ(y/x)` or `z = yⁿ · ψ(x/y)`
(set k = 1/x or k = 1/y in the definition).

### Property 2
The first-order partial derivatives of a degree-n homogeneous function are **homogeneous of degree (n − 1)**.

**Proof sketch.** Write z = xⁿ φ(y/x).
∂z/∂x = n x^{n−1} φ(y/x) + xⁿ · φ'(y/x) · (−y/x²)
= x^{n−1} [n φ(y/x) − (y/x) φ'(y/x)]
which is again of the form x^{n−1} · (function of y/x), i.e., homogeneous of degree (n − 1).

<!-- Property 3 (Euler's theorem) continues in chunk 006 -->

### Definitions
- **Homogeneous of degree n**: f(kx₁, kx₂) = kⁿ f(x₁, x₂). ⭐

### Connections
- Builds on: Partial derivatives (§11.2); chain rule (§11.4.1).
- Is prerequisite for: Cobb–Douglas analysis (chunk 006 CYP2); Euler's theorem (chunk 006).

### Open Questions
1. What economic significance does the degree of homogeneity have for production functions? (constant returns to scale ⟺ degree 1.)
2. Why does linear-homogeneity simplify σ to a function only of f_{LK}?


---


## Section: §11.4.4 Property 3 — Euler's Theorem 🔴
<!-- See chunk 005 for Properties 1–2 -->

### Core Idea
For a homogeneous function z = f(x, y) of degree n:
**`x · f_x + y · f_y = n · f(x, y)`**
This identity — Euler's homogeneous function theorem — is one of the most useful results in production theory.

> **In Simple Terms:** Multiply each input's marginal product by the input level, sum them up, and you get exactly n times the output. For n = 1 (constant returns to scale), this means total output = sum of (input × marginal product) — the "exhaustion of product" or marginal-productivity theory of distribution.

### Implications
- **Constant returns to scale (n = 1)**: x f_x + y f_y = f(x, y). Euler's theorem in this case underlies the marginal productivity theory of distribution: paying each factor its marginal product exactly exhausts total output.

> **Quick Recall:**
> - Euler's theorem: `Σᵢ xᵢ f_{xᵢ} = n · f` for degree-n homogeneous f.
> - For n = 1: total output = labour × MPL + capital × MPK.

---

## Section: Unit 11 Sum-Up & Key Words (§11.5–§11.6) 🟢

### Sum-Up
Unit 11 covered: partial derivatives; higher-order and cross-partials; Young's theorem; total differential vs total derivative; chain rule cases (I–IV); implicit functions; MRTS; elasticity of substitution; homogeneous functions and their three properties (including Euler).

### Key Words
- **Homogeneous function**: f(tx, ty) = tⁿ f(x, y).
- **Partial derivative**: derivative w.r.t. one variable, others held constant.
- **Total derivative**: rate of change of dependent variable when none of the variables is held constant.
- **Total differential**: linear approximation `dy = Σᵢ fᵢ dxᵢ`.

---

## Section: §11.7 Selected CYP Solutions 🟡

**CYP1 (1): Q = 5 L² K (note: source has L²K^? OCR'd; treating as L²K).**
- Q_L = 10 L K. (Source: Q_L = LK²; suggests degrees may differ — likely the textbook function is Q = 5 L² K with marginal products 10LK and 5L².) The standard mechanic remains: differentiate Q partially w.r.t. each input.

**CYP1 (3): f(x, y) = y sin x² + x³ cos y. Find f_x, f_y, f_{xx}, f_{yy}, and verify f_{xy} = f_{yx}.**
- f_x = 2xy cos x² + 3x² cos y.
- f_y = sin x² − x³ sin y.
- f_{xx} = 2y cos x² − 4x² y sin x² + 6x cos y.
- f_{yy} = −x³ cos y.
- f_{xy} = f_{yx} (by Young's theorem) = 2x cos x² − 3x² sin y.

**CYP2 (2): Cobb–Douglas q = A L^a K^{1−a}, A, a > 0.**

(a) **Homogeneous of degree 1:**
q(tL, tK) = A (tL)^a (tK)^{1−a} = A t^a L^a t^{1−a} K^{1−a} = t^{a + 1 − a} q = t · q. ✓

(b) **Marginal & average productivities depend only on K/L (or L/K):**
- MPL = A · a · L^{a−1} K^{1−a} = a · A · (K/L)^{1−a} → function of (K/L) alone.
- APL = q/L = A · L^{a−1} K^{1−a} = A · (K/L)^{1−a} → also a function of (K/L) only.

(c) **Elasticity of substitution σ = 1.** (Standard Cobb–Douglas property; can be derived from σ formula in §11.4.3 or directly: ln(L/K) is a linear function of ln(MRTS), with slope 1.)

(d) **Iso-quants downward sloping and convex.** Slope dK/dL < 0; second derivative d²K/dL² > 0 ⇒ convex to the origin.

> **Quick Recall:**
> - Cobb–Douglas q = A L^a K^{1−a}: degree 1, σ = 1, downward & convex isoquants.
> - Marginal products depend only on the input ratio K/L — homotheticity property.

---

## Section: §11.8 Unit 11 Exercises (Solved) 🟡

### Q1: Cubic cost C(x) = 10⁻⁶ x³ − 0.003 x² + 5x + 1000

(a) **Behaviour of marginal cost.**
- C'(x) = 3 × 10⁻⁶ · x² − 0.006 x + 5.
- C''(x) = 6 × 10⁻⁶ · x − 0.006.
- C''(x) = 0 at x = 1000. So MC is minimised at x = 1000.
- MC(1000) = 3·10⁻⁶ · 10⁶ − 0.006·1000 + 5 = 3 − 6 + 5 = 2.
- For x < 1000: MC decreasing. For x > 1000: MC increasing.

(b) **Sketch of C(x).**
- C'(x) > 0 always (no local extrema; cost continually rising).
- C'(x) decreases for x < 1000, increases beyond ⇒ C is **concave down for x < 1000**, **concave up for x > 1000**, with **inflexion at x = 1000**.
- The inflexion point of C(x) coincides with the minimum of MC.

### Q2: Demand p = 6 − x/2

- Revenue R(x) = x · p = 6x − x²/2.
- Marginal revenue R'(x) = 6 − x.
- R'(x) = 0 at x = 6.
- Maximum revenue R(6) = 36 − 18 = **18 rupees**.

> **Quick Recall:**
> - Inflexion point of total cost = minimum of marginal cost.
> - Revenue maximisation: dR/dx = 0 (set MR = 0).

---

## Section: Unit 12 Front Matter (§12.0–§12.1) 🟢

### Core Idea
Unit 12 is on **Integration** — the inverse of differentiation, and the language of accumulation (areas, total revenue from marginal revenue, present-value computations, etc.). It distinguishes **indefinite integrals** (a family of antiderivatives + constant) from **definite integrals** (a number = signed area).

### §12.0 Objectives
- Use integration as a problem-solving tool.
- Apply substitution, by-parts, trigonometric, partial-fraction, and rational-substitution methods.
- Evaluate improper integrals; classify convergent vs divergent.

> **Note on Unit 12 title**: the source's Unit 12 page header reads "DIFFERENTIAL CALCULUS: FUNCTIONS OF SEVERAL VARIABLES" — a typesetting/OCR carryover from Unit 11. The Block 3 cover page and Unit 12's actual content confirm the correct title is **"Integration: Introduction and Techniques"**.

---

## Section: §12.2 Indefinite Integrals 🔴

### Core Idea
Indefinite integration is **anti-differentiation**. Where differentiation finds the rate of change of a known function, indefinite integration finds an unknown function whose derivative is given.

### Notation
`∫ f(x) dx = F(x) + C`
where F'(x) = f(x), and C is the **constant of integration** (because antiderivatives are not unique — adding any constant gives another antiderivative).

- f(x) = the **integrand**.
- ∫ symbol is an elongated "S" denoting **sum** (anticipating the area-as-sum interpretation).
- ∫ f(x) dx reads "the integral of f(x) with respect to x".

### Examples
**Quick example.** If dy/dx = 3x², then y = x³ + C is an antiderivative because d(x³+C)/dx = 3x².

**Example 12.1: ∫(x² − 5) dx.**
We need a function whose derivative is x² − 5: that is x³/3 − 5x. So
`∫(x² − 5) dx = x³/3 − 5x + C`.

### Definitions
- **Indefinite integral** `∫ f(x) dx = F(x) + C`: any function F whose derivative is f, plus an arbitrary constant. ⭐
- **Constant of integration C**: the arbitrary additive constant; reflects non-uniqueness of antiderivatives. ⭐

> **Quick Recall:**
> - "Anti-derivative" is the most useful synonym.
> - **Always** include + C in indefinite integrals.

---

## Section: §12.3 Properties of the Indefinite Integral 🔴

### Property 1a — Linearity (constant factor)
`∫ k · f(x) dx = k · ∫ f(x) dx` for any constant k.

### Property 1b — Power rule
`∫ xⁿ dx = x^{n+1} / (n+1) + C`, valid for **n ≠ −1**. (For n = −1, the integral is ln|x| + C; see §12.6.)

### Property 2 — Linearity (sum)
`∫ [f(x) + g(x)] dx = ∫ f(x) dx + ∫ g(x) dx`.

(Subtraction works the same way: `∫ (f − g) dx = ∫ f dx − ∫ g dx`.)

### Examples
**Example 12.2: ∫ 5x² dx = 5 · x³/3 + C.**
**Example 12.3: ∫ x⁵ dx = x⁶/6 + C.**
**Example 12.4: ∫ 8 x⁶ dx = (8/7) x⁷ + C.**
**Example 12.5: ∫(4x² + 7x + 3) dx = (4x³)/3 + (7x²)/2 + 3x + C.**
**Example 12.6: dy = (5x² − 4x + 3) dx ⇒ y = (5x³)/3 − 2x² + 3x + C.**
**Example 12.7: ∫(2x + √x − 5/x³) dx**
Rewrite as ∫(2x + x^{1/2} − 5x^{−3}) dx = x² + (2/3) x^{3/2} + 5x^{−2}/2 + C.
(Source has a slight algebraic confusion; the right approach is term-by-term power rule.)

### Mechanisms / Processes (using initial condition to fix C)
**Example 12.8: dy/dx = 3x² − 2x; curve passes through (2, 5). Find y(x).**
1. Antidifferentiate: y = x³ − x² + C.
2. Plug in initial condition: 5 = 8 − 4 + C ⇒ C = 1.
3. Answer: y = x³ − x² + 1.

> **Quick Recall:**
> - Linearity: pull constants out, split sums.
> - Power rule: x^{n+1}/(n+1), but **only for n ≠ −1**.
> - Boundary/initial conditions uniquely determine C.

---

## Section: §12.3.2 Method of Substitution 🔴

### Core Idea
Substitution converts the integral of a composite function into a simpler integral by introducing a new variable u = g(x). The differential du = g'(x) dx must "match" something in the integrand for the trick to work.

### Statement
If x = g(y) (or u = g(x)), then `∫ f(x) dx = ∫ f(g(y)) g'(y) dy`. Most often used as: spot u = g(x) in the integrand whose derivative is also there (up to a constant).

### Mechanisms / Processes (substitution recipe)
1. Identify a composite expression: u = (something).
2. Compute du = (derivative of u) dx.
3. Rewrite the integral fully in u (no x left).
4. Integrate w.r.t. u using power/standard rules.
5. Substitute back u = g(x).
6. Add + C.

### Examples
**Example 12.9: ∫(2x⁴ − 5)⁵ x³ dx.**
Set u = 2x⁴ − 5 ⇒ du = 8 x³ dx ⇒ x³ dx = du/8.
`∫ u⁵ · du/8 = u⁶/48 + C = (2x⁴ − 5)⁶ / 48 + C`. (Source gives ⁷/56 in places — typo; the correct exponent is 6 because original power was 5.)

Wait — source says "(2x⁴ − 5)⁶ x³" with power 6 in places and 5 in others. Let me re-examine: the integrand was originally `(2x⁴ − 5)⁵ x³`, so the integral has u⁶/6 inside, and after dividing by 8 we get u⁶/48.

**Example 12.10: ∫(1 + 5x)^{1/2} dx.**
u = 1 + 5x ⇒ du = 5 dx ⇒ dx = du/5.
`(1/5) ∫ u^{1/2} du = (1/5) · (2/3) u^{3/2} + C = (2/15)(1 + 5x)^{3/2} + C`.

**Example 12.11: ∫ dx/(3x − 1)².**
u = 3x − 1 ⇒ du = 3 dx.
`(1/3) ∫ u^{−2} du = (1/3)(−u^{−1}) + C = −1/(3(3x − 1)) + C`.

**Example 12.12: ∫ e^{2x} dx.** u = 2x ⇒ du = 2 dx. (1/2) ∫ eᵘ du = (1/2) e^{2x} + C.

**Example 12.13: ∫ 2x √(x² + 1) dx.** u = x² + 1 ⇒ du = 2x dx. ∫ √u du = (2/3) u^{3/2} + C = (2/3)(x² + 1)^{3/2} + C.

> **Quick Recall:**
> - Substitution works when the integrand contains both g(x) and g'(x) (up to a constant).
> - Always express **everything** in terms of u — including dx.

### ⚠️ Common Mistakes
- ❌ Mistake: forgetting to convert dx into du → ✅ Correct: derive du = g'(x) dx and use it to replace dx.

---

## Section: §12.4 Integration of Trigonometric Functions (begins) 🟡

### Trigonometric identity refresh
- Ratio: `tan A = sin A / cos A`; `cot A = 1/tan A`.
- Reciprocal: `cosec A = 1/sin A`; `sec A = 1/cos A`.
- Pythagorean: `sin²A + cos²A = 1`; `1 + tan²A = sec²A`; `1 + cot²A = cosec²A`.

<!-- Continues in chunk 007: differentiation rules for trig, full integration table for trig functions, worked examples 12.14–12.18, integration by parts -->

### Connections
- Builds on: Substitution method (§12.3.2) — trig integrals often need substitution.
- Is prerequisite for: Integration by parts (§12.5) for products like x · sin x; partial fractions (§12.12) when simplifying after trig substitution.

### Open Questions
1. Why is the indefinite integral of 1/x not covered by the power rule? (The exponent +1 makes it 0/0; the answer is ln|x|.)
2. When should you choose substitution vs by-parts? (Substitution for products where one part is the derivative of another; by-parts for products with no such relation — see CYP2 in chunk 007.)


---


## Section: §12.4 Trigonometric Integration — completion 🟡
<!-- See chunk 006 for §12.4 intro -->

### Differentiation rules for trig (recap, used to derive integrals)
| Function | Derivative |
|---|---|
| sin A | cos A |
| cos A | −sin A |
| tan A | sec² A |
| cot A | −cosec² A |
| sec A | sec A · tan A |
| cosec A | −cosec A · cot A |

### Standard trig integration formulas
| Basic form | Generalised (linear arg ax + b) |
|---|---|
| ∫ cos x dx = sin x + C | ∫ cos(ax + b) dx = (1/a) sin(ax + b) + C |
| ∫ sin x dx = −cos x + C | ∫ sin(ax + b) dx = −(1/a) cos(ax + b) + C |
| ∫ tan x dx = −ln|cos x| + C | ∫ tan(ax + b) dx = −(1/a) ln|cos(ax + b)| + C |
| ∫ cot x dx = ln|sin x| + C | ∫ cot(ax + b) dx = (1/a) ln|sin(ax + b)| + C |
| ∫ sec x dx = ln|sec x + tan x| + C | (1/a) ln|sec(ax + b) + tan(ax + b)| + C |
| ∫ cosec x dx = ln|cosec x + cot x| + C (with a sign convention) | likewise (1/a) form |

### Examples
**Example 12.14: ∫ cos(15x) cos(4x) dx.** Use product-to-sum: cos A cos B = (1/2)[cos(A − B) + cos(A + B)].
`∫ cos(15x) cos(4x) dx = (1/2) ∫ [cos(11x) + cos(19x)] dx = (1/2) [(1/11) sin(11x) + (1/19) sin(19x)] + C`.

**Example 12.15: ∫ cos x sin⁵ x dx.**
u = sin x ⇒ du = cos x dx. ∫ u⁵ du = u⁶/6 + C = sin⁶ x / 6 + C.

**Example 12.16: ∫ sin⁵ x dx.**
sin⁵ x = (sin² x)² · sin x = (1 − cos² x)² · sin x. Set u = cos x ⇒ du = −sin x dx.
∫ sin⁵ x dx = −∫ (1 − u²)² du = −∫ (1 − 2u² + u⁴) du = −u + (2/3) u³ − u⁵/5 + C
= −cos x + (2/3) cos³ x − (1/5) cos⁵ x + C.

**Example 12.17: ∫ (3 sin x − 4 sec² x) dx = −3 cos x − 4 tan x + C.**

**Example 12.18: ∫ cos(2x − 6) dx.** u = 2x − 6 ⇒ du = 2 dx. ∫ cos u · du/2 = sin u / 2 + C = sin(2x − 6)/2 + C.

> **Quick Recall:**
> - Product-to-sum identities turn cos×cos, sin×cos, sin×sin into sums of single trig functions.
> - For odd powers of sin (or cos), peel off one factor to combine with du.
> - Linear-argument trick: ∫ f(ax + b) dx = (1/a) F(ax + b) where F is the antiderivative of f.

---

## Section: §12.5 Integration by Parts 🔴

### Core Idea
When the integrand is a **product** of two functions and substitution doesn't work, integration by parts is the technique of choice. It comes directly from the product rule for derivatives.

### Derivation
Product rule: `d(uv)/dx = u' v + u v'`. Integrating both sides:
`uv = ∫ u' v dx + ∫ u v' dx`.
Rearranging:
**`∫ u v' dx = uv − ∫ v u' dx`**

In differential form:
`∫ u dv = uv − ∫ v du`.

### Mechanisms / Processes (choosing u and dv)
1. Pick u: the part that **simplifies on differentiation** (e.g., x → 1, ln x → 1/x).
2. Pick dv: the part you **can integrate** (e.g., sin x dx, eˣ dx).
3. Compute du = u' dx and v = ∫ dv.
4. Apply the formula `∫ u dv = uv − ∫ v du`.
5. Evaluate the new integral; if needed, apply by-parts again.

**LIATE heuristic** (priority order for u): Logarithmic, Inverse trig, Algebraic, Trigonometric, Exponential.

### Examples
**Example 12.19: ∫ x e^{−x} dx.**
- u = x, dv = e^{−x} dx.
- du = dx, v = −e^{−x}.
- ∫ x e^{−x} dx = −x e^{−x} − ∫ (−e^{−x}) dx = −x e^{−x} − e^{−x} + C = −(1 + x) e^{−x} + C.

**Example 12.20: ∫ (3t + 5) cos(t/4) dt.**
- u = 3t + 5, dv = cos(t/4) dt.
- du = 3 dt, v = 4 sin(t/4).
- ∫ = 4(3t + 5) sin(t/4) − 12 ∫ sin(t/4) dt = 4(3t + 5) sin(t/4) + 48 cos(t/4) + C.

**Example 12.21: ∫ x ln x dx.**
- u = ln x, dv = x dx (LIATE: log first).
- du = dx/x, v = x²/2.
- ∫ x ln x dx = (x²/2) ln x − ∫ (x²/2) · (1/x) dx = (x²/2) ln x − x²/4 + C.

> **Quick Recall:**
> - `∫ u dv = uv − ∫ v du`.
> - LIATE: pick u from earlier in L-I-A-T-E.
> - Repeat by-parts when the new integral still has a product (e.g., for x² eˣ, two by-parts).

### ⚠️ Common Mistakes
- ❌ Mistake: forgetting the minus sign in `−∫ v du` → ✅ Correct: it comes straight from rearranging the product rule.

---

## Section: §12.6 Some Useful Formulae 🔴

| # | Formula | Notes |
|---|---|---|
| 1 | `∫ xⁿ dx = x^{n+1}/(n+1) + C` | n ≠ −1 |
| 2 | `∫ x^{−1} dx = ∫ dx/x = ln |x| + C` | for x ≠ 0 |
| 3 | `∫ e^{mx} dx = e^{mx}/m + C` | for any m ≠ 0 |
| 4 | `∫ a^{mx} dx = a^{mx}/(m ln a) + C` | a > 0, a ≠ 1 |
| 5 | `∫ cos(ax) dx = sin(ax)/a + C` | |
| 6 | `∫ sin(ax) dx = −cos(ax)/a + C` | |
| 7 | `∫ [k₁ f(x) + k₂ g(x)] dx = k₁ ∫ f(x) dx + k₂ ∫ g(x) dx + C` | linearity, k₁, k₂ constants |

> **Quick Recall:**
> - **Memorise these seven** — they cover most direct integrals encountered.

---

## Section: §12.7 Determining the Constant of Integration 🟡

### Core Idea
Indefinite integrals come with a **family** of solutions parameterised by C. A specific (initial or boundary) condition fixes C uniquely.

### Mechanisms / Processes
1. Find the general antiderivative F(x) + C.
2. Plug in the boundary point: y₀ = F(x₀) + C.
3. Solve for C: C = y₀ − F(x₀).
4. Write the unique solution: y = F(x) + C.

### Example
∫(x² + 3) dx = x³/3 + 3x + C. With y(0) = 20: 20 = 0 + 0 + C ⇒ C = 20. Unique answer: `y = x³/3 + 3x + 20`.

> **Quick Recall:**
> - One initial condition fixes one constant of integration.

---

## Section: §12.8 Definite Integrals 🔴

### Core Idea
The **definite integral** `∫ₐᵇ f(x) dx` is a *number* — geometrically, the signed area between the curve y = f(x) and the x-axis from x = a to x = b.

### §12.8.1 Finding Area — rectangles approximation

#### Setup
Divide [a, b] into n subintervals each of width `Δx = (b − a)/n`. End points: x₀ = a, x₁ = a + Δx, …, xₙ = b. From each subinterval pick a point xᵢ* and use f(xᵢ*) as the rectangle's height.

| Choice of height | Approx area |
|---|---|
| Right endpoint | Σᵢ f(xᵢ) Δx |
| Left endpoint | Σᵢ f(xᵢ₋₁) Δx |
| Midpoint | Σᵢ f((xᵢ₋₁ + xᵢ)/2) Δx |

For an increasing function on [a, b]:
- Right endpoints **overestimate**.
- Left endpoints **underestimate**.
- Midpoint typically gives the best approximation for fixed n.

#### Worked example: f(x) = x² + 1 on [0, 2] with n = 4
- Δx = 0.5; partition x₀=0, x₁=0.5, x₂=1, x₃=1.5, x₄=2.
- Right-endpoint sum A_R = 0.5[f(0.5) + f(1) + f(1.5) + f(2)] = 0.5[1.25 + 2 + 3.25 + 5] = 5.75.
- Left-endpoint sum A_L = 0.5[f(0) + f(0.5) + f(1) + f(1.5)] = 0.5[1 + 1.25 + 2 + 3.25] = 3.75.
- True value (from §12.8.2 below): ∫₀² (x² + 1) dx = 14/3 + 2 ≈ 4.67. (Right overestimates, left underestimates.)

> **In Simple Terms:** Slicing the area into vertical strips and summing strip-areas. The thinner the strip (larger n), the closer to the true area. The limit is the definite integral.

### §12.8.2 Definition via Riemann Sum

Given a continuous f on [a, b], partition into n equal subintervals of width Δx, choose any xᵢ* in each:
**`∫ₐᵇ f(x) dx = lim_{n→∞} Σᵢ₌₁ⁿ f(xᵢ*) Δx`**

This sum is the **Riemann sum**.

### Examples
**Example 12.22: ∫₀³ (x² + 1) dx.**
Source uses formula with right endpoints, computing as a sum:
`= lim_{n→∞} Σᵢ f(xᵢ) (b − a)/n` and arrives at value 12.
Alternatively, by the FTC (chunk 008): F(x) = x³/3 + x ⇒ F(3) − F(0) = 9 + 3 = **12**. ✓

### Definitions
- **Riemann sum**: Σᵢ f(xᵢ*) Δxᵢ for a partition of [a, b]. ⭐
- **Definite integral**: limit of Riemann sums as the partition gets infinitely fine. ⭐
- **Mesh size**: max width of subintervals in the partition.

> **Quick Recall:**
> - Riemann sum: pick a point in each strip, sum height × width.
> - Limit (mesh → 0) is the definite integral.

---

## Section: §12.8.3 Properties of Definite Integral 🔴

| # | Property |
|---|---|
| 1 | `∫ₐᵇ 1 dx = b − a` |
| 2 | `∫ₐᵇ c · f(x) dx = c · ∫ₐᵇ f(x) dx` (constant factors out) |
| 3 | `∫ₐᵇ [f + g] dx = ∫ₐᵇ f dx + ∫ₐᵇ g dx` (linearity) |
| 4 | `∫ₐᵇ f dx = ∫ₐᶜ f dx + ∫ᶜᵇ f dx` (additivity over intervals; a ≤ c ≤ b) |
| 5 | If 0 ≤ f(x) ≤ g(x) on [a, b], then `0 ≤ ∫ₐᵇ f dx ≤ ∫ₐᵇ g dx` (comparison) |
| 6 | `∫ₐᵃ f(x) dx = 0` (degenerate interval = 0 area) |
| 7 | `∫ₐᵇ f(x) dx = − ∫_b^a f(x) dx` (reversing bounds flips sign) |

### Examples
**Property 4 illustration:** ∫₁³(2x+3)dx = 14, ∫₃⁵(2x+3)dx = 22 ⇒ ∫₁⁵ = 14 + 22 = 36.
**Property 6: ∫₂² (3x + 4) dx = 0.**
**Property 7: If ∫₁⁴ x³ dx = 21, then ∫₄¹ x³ dx = −21.**

> **Quick Recall:**
> - Same bounds → 0.
> - Flipping bounds → flip sign.
> - Linearity (scalar + sum) extends to definite integrals just as for indefinite.

### Connections
- Builds on: Indefinite integral (§12.2); area-as-sum interpretation; FTC (§12.9 in chunk 008) ties indefinite and definite together.
- Is prerequisite for: Fundamental theorem (§12.9), area calculations (§12.10), improper integrals (§12.11).

### Open Questions
1. Why must f be continuous (or at least Riemann-integrable) for the limit definition to apply? (Pathological functions can have ill-defined Riemann sums.)
2. Can a definite integral be negative? (Yes — when f(x) < 0 on parts of [a, b]; the integral measures *signed* area.)


---


## Section: §12.9 Fundamental Theorem of Calculus (FTC) 🔴

### Core Idea
The FTC bridges differentiation and integration — two apparently independent operations — and is the engine that converts "find the area" into "find an antiderivative". The theorem has two parts: one says antidifferentiation can be reversed by differentiation; the other says the definite integral can be computed by evaluating an antiderivative at the endpoints.

> **In Simple Terms:** Integration and differentiation are inverse operations, like multiplication and division. Once you know any antiderivative F of f, the area under f from a to b is just F(b) − F(a). No more Riemann sums.

### Part 1 — Differentiation undoes integration
For continuous f on [a, b], define `F(x) = ∫ₐˣ f(t) dt`. Then:
**`F'(x) = f(x)`** and equivalently **`d/dx ∫ₐˣ f(t) dt = f(x)`**.

Every continuous f has an antiderivative; varying the lower limit gives the family of antiderivatives differing by constants.

### Part 2 — Evaluating definite integrals
For f continuous on [a, b] with **any** antiderivative F:
**`∫ₐᵇ f(x) dx = F(b) − F(a)`**

### Examples
**Example 12.25: d/dx ∫₃ˣ 4 t³ dt.**
The antiderivative inside is t⁴, so the integral equals x⁴ − 3⁴ = x⁴ − 81. d/dx of that is 4x³. (Equivalently: by Part 1 directly, derivative = integrand evaluated at x = 4x³.)

**Example 12.26: d/dx ∫₂^{sin x} e^{t²} dt.**
By Part 1 with chain rule (since the upper limit is sin x, not just x): the inner antiderivative G(u) = ∫₂ᵘ e^{t²} dt has G'(u) = e^{u²}. So d/dx [G(sin x)] = e^{sin² x} · cos x. Source's stated answer e^{x²} omits the chain factor — careful here.

**Example 12.27: ∫₂³ x² dx = [x³/3]₂³ = 27/3 − 8/3 = 19/3.**

**Example 12.28: ∫₀² (t² − 3t + 10) dt = [t³/3 − 3t²/2 + 10t]₀² = 8/3 − 6 + 20 = 8/3 + 14 = 50/3 ≈ 16.67.**

### Definitions
- **Antiderivative (or indefinite integral)**: any function F with F'(x) = f(x). ⭐
- **Fundamental Theorem of Calculus (Part 2)**: ∫ₐᵇ f(x) dx = F(b) − F(a). ⭐

> **Quick Recall:**
> - Part 1: derivative of "area function" = integrand.
> - Part 2: ∫ₐᵇ f = F(b) − F(a) for *any* antiderivative F.
> - Two antiderivatives differ by a constant — so the choice of F doesn't matter.

### ⚠️ Common Mistakes
- ❌ Mistake: applying Part 1 to ∫_{a}^{g(x)} f(t) dt as just f(x) → ✅ Correct: the chain rule gives f(g(x)) · g'(x).

---

## Section: §12.10 Integration & the Chain Rule (Net Area, Definite Substitution) 🟡

### Net area between graph and x-axis
The definite integral ∫ₐᵇ f(x) dx gives **signed (net) area**: positive contributions where f > 0, negative where f < 0. To get *actual* total area (always positive), split at zeros and integrate the absolute value.

### Examples
**Example 12.29: Area between y = 7 − x² and the x-axis on [−1, 2].**
∫_{−1}² (7 − x²) dx = [7x − x³/3]_{−1}² = (14 − 8/3) − (−7 + 1/3) = 14 − 8/3 + 7 − 1/3 = 21 − 9/3 = 21 − 3 = 18.

**Example 12.30: Net area of y = sin x on [0, 2π].**
∫₀^{2π} sin x dx = [−cos x]₀^{2π} = −1 − (−1) = **0** (net cancels: positive lobe on (0, π), negative on (π, 2π)).
Actual *total* area = ∫₀^π sin x dx + |∫_π^{2π} sin x dx| = 2 + 2 = 4.

### §12.10.1 u-substitution in definite integrals — two methods

#### Method 1 — convert and convert back
After substitution, integrate; revert to x and substitute the original bounds.

#### Method 2 — change the bounds
After substitution u = f(x), update bounds: a → f(a), b → f(b). Then evaluate purely in u.

For ∫ₐᵇ f(x) f'(x) dx with u = f(x):
`∫ₐᵇ f(x) f'(x) dx = ∫_{f(a)}^{f(b)} u du = [u²/2]_{f(a)}^{f(b)} = ((f(b))² − (f(a))²)/2`.

### Examples
**Example 12.31: ∫_{(stated bounds)} −2x (4 − x²) dx with u = 4 − x², du = −2x dx.**

**Example 12.32: ∫₀^{π/2} sin x cos x dx.**
- Method 1: u = sin x ⇒ du = cos x dx. ∫ u du = u²/2 + C; revert and evaluate at endpoints.
- Method 2: bounds u(0) = 0, u(π/2) = 1. ∫₀¹ u du = 1/2.

**Example 12.33: ∫₀^{π/2} sin² x cos x dx.**
u = sin x. ∫₀¹ u² du = 1/3.

> **Quick Recall:**
> - Net area ≠ total area when f changes sign — split at zeros for total.
> - For definite integrals with substitution: either revert to x then plug in original bounds, or update the bounds and stay in u.

---

## Section: §12.11 Improper Integrals 🔴

### Core Idea
A definite integral is **improper** when at least one bound is ±∞ or when the integrand has an unbounded singularity in [a, b]. Such integrals are evaluated as limits of proper definite integrals.

### Evaluation rules

| Form | Definition |
|---|---|
| ∫_b^∞ f(x) dx | lim_{a → ∞} ∫_b^a f(x) dx |
| ∫_{−∞}^a f(x) dx | lim_{b → −∞} ∫_b^a f(x) dx |

### §12.11.1 Convergent vs Divergent

The improper integral **converges** if the limit exists and is finite; otherwise it **diverges**.

For doubly-infinite integrals, split at any convenient c:
`∫_{−∞}^∞ f(x) dx = ∫_{−∞}^c f(x) dx + ∫_c^∞ f(x) dx`,
**convergent only if both pieces converge separately**. If either diverges, the whole integral diverges.

### Comparison Theorem
For continuous f, g on [a, ∞) with `f(x) ≥ g(x) ≥ 0`:
- If `∫_a^∞ f` converges, then `∫_a^∞ g` converges.
- If `∫_a^∞ g` diverges, then `∫_a^∞ f` diverges.

### Examples
**Example 12.34: ∫_1^∞ dx/x².**
∫_1^a dx/x² = [−1/x]_1^a = −1/a + 1.
lim_{a→∞} (1 − 1/a) = **1** ⇒ converges to 1. Geometrically, the area between 1/x², the x-axis, and x = 1 is finite (= 1) even though the region extends to infinity.

**Example 12.35: ∫_1^∞ dx/x.**
∫_1^a dx/x = ln a − ln 1 = ln a → ∞ as a → ∞ ⇒ **diverges**.
(So 1/x is the borderline case: 1/x^p converges for p > 1, diverges for p ≤ 1.)

**Example 12.36: ∫_{−∞}^0 dx/√(3 − x).**
−2√(3 − x) is the antiderivative. As b → −∞, √(3 − b) → ∞ ⇒ value → ∞ ⇒ **diverges**.

**Example 12.37: ∫_{−∞}^∞ x · e^{−x²} dx.**
Split at 0:
- ∫_{−∞}^0 x · e^{−x²} dx: u = −x², du = −2x dx. Antiderivative −(1/2) e^{−x²}. lim_{b → −∞} [−(1/2)(1 − e^{−b²})] = −1/2.
- ∫_0^∞ x · e^{−x²} dx = +1/2.
- Total = −1/2 + 1/2 = **0** ⇒ convergent to 0.

### Definitions
- **Improper integral**: definite integral with infinite bound or unbounded integrand. ⭐
- **Convergent integral**: limit exists and is finite. ⭐
- **Divergent integral**: limit is infinite or does not exist. ⭐

> **Quick Recall:**
> - Always rewrite `∫_b^∞` as `lim_{a→∞} ∫_b^a`.
> - For `∫_{−∞}^∞`, both halves must converge separately.
> - 1/x^p on [1, ∞): converges if p > 1, diverges if p ≤ 1.

### ⚠️ Common Mistakes
- ❌ Mistake: in ∫_{−∞}^∞ f, taking a single symmetric limit (a → ∞ with bounds [−a, a]) → ✅ Correct: each half must converge independently; the symmetric "principal value" can hide divergence.

---

## Section: §12.12 Integration with Partial Fractions 🔴

### Core Idea
Many rational integrands `p(x)/q(x)` are not directly integrable but can be **decomposed** into a sum of simpler fractions whose integrals are standard (logs, arctans, power rule). This is the partial fraction technique.

### Conditions for direct decomposition
1. p(x)/q(x) is a rational function (polynomials).
2. **deg(p) < deg(q)**. (If not, polynomial-divide first; integrate the polynomial part directly and decompose the remainder.)

### Decomposition templates
| Factor of denominator | Term in decomposition |
|---|---|
| (x − a) (distinct linear) | A/(x − a) |
| (x − a)² | A/(x − a) + B/(x − a)² |
| (x − a)ᵏ | A₁/(x − a) + A₂/(x − a)² + … + Aₖ/(x − a)ᵏ |
| irreducible quadratic (x² + bx + c) | (Bx + C)/(x² + bx + c) |
| (x² + bx + c)ᵏ | k similar quadratic terms with rising denominators |

### Mechanisms / Processes (decomposition recipe)
1. Check deg(p) < deg(q); if not, long-divide.
2. Factor q(x) completely (linear + irreducible quadratic factors).
3. Write the partial-fraction template with unknowns (A, B, C, …).
4. Multiply out to clear denominators ⇒ a polynomial identity.
5. Solve for unknowns by either (a) plugging in strategic values of x (often the zeros of q) or (b) equating coefficients of like powers.
6. Integrate each simple fraction.

### Examples

**Motivating example: ∫(3x + 11)/(x² − x − 6) dx.**
- Factor: x² − x − 6 = (x − 3)(x + 2).
- Decompose: (3x + 11)/[(x − 3)(x + 2)] = A/(x − 3) + B/(x + 2).
- Multiply out: 3x + 11 = A(x + 2) + B(x − 3).
- x = 3: 20 = 5A ⇒ A = 4.
- x = −2: 5 = −5B ⇒ B = −1.
- Integral = 4 ∫ dx/(x − 3) − ∫ dx/(x + 2) = 4 ln|x − 3| − ln|x + 2| + C.

**Example: 6/(x² − 1).**
6/[(x − 1)(x + 1)] = A/(x − 1) + B/(x + 1).
6 = A(x + 1) + B(x − 1).
x = 1: 6 = 2A ⇒ A = 3.
x = −1: 6 = −2B ⇒ B = −3.
Decomposition: **3/(x − 1) − 3/(x + 1)**.

**Example: (2x − 3)/(x³ + x).**
Factor x³ + x = x(x² + 1). Template: A/x + (Bx + C)/(x² + 1).
Multiply out: 2x − 3 = A(x² + 1) + (Bx + C) x.
x = 0: −3 = A.
Use x = i (imaginary): 2i − 3 = A(0) + (Bi + C) i = − B + C i.
Match real & imaginary: −B = −3 ⇒ B = 3; C = 2.
Decomposition: **−3/x + (3x + 2)/(x² + 1)**.

**Example 12.38 (repeated linear + irreducible quadratic):**
`(2x³ + 5x − 1) / [(x + 1)³ (x² + 4)²]` decomposes as
`A/(x+1) + B/(x+1)² + C/(x+1)³ + (Dx+E)/(x²+4) + (Fx+G)/(x²+4)²`.

**Example 12.39 (deg(p) ≥ deg(q)):** ∫(x⁴ + 3x³ − 5x² − 4x + 17)/(x² + x − 2) dx.
Long-divide first: (x⁴ + 3x³ − 5x² − 4x + 17)/(x² + x − 2) = (x² + 2x − 5) + (3x + 7)/[(x + 2)(x − 1)].
Then decompose (3x + 7)/[(x + 2)(x − 1)] using the standard recipe.

### Definitions
- **Partial fraction decomposition**: writing a rational function as a sum of simpler rational functions whose denominators are factors of the original denominator. ⭐

> **Quick Recall:**
> - Always check deg(p) < deg(q) first; long-divide if not.
> - Distinct linear factor → constant numerator. Repeated linear → ascending powers. Irreducible quadratic → linear numerator (Bx + C).
> - "Cover-up" (plug in x = root) is the fastest way to find the constant for a distinct linear factor.

### ⚠️ Common Mistakes
- ❌ Mistake: writing (Bx + C)/(x² + 1) as just B/(x² + 1) → ✅ Correct: irreducible quadratic factors get **linear** numerators.
- ❌ Mistake: forgetting to long-divide when deg(p) ≥ deg(q) → ✅ Correct: long-divide first; integrate the polynomial part separately.

### Connections
- Builds on: Linearity of integration (§12.3); standard logarithmic and inverse-tangent integrals.
- Continues into: Chunk 009 — more partial fraction examples (12.39–12.43), Unit 12 wrap-up, exercises.

### Open Questions
1. How do you handle ∫ dx/(x² + 1) without a partial fraction step? (It is arctan x + C — recognise it directly.)
2. What happens when q(x) has complex (non-real) roots? (Group conjugate pairs into irreducible quadratic factors.)


---


## Section: §12.12 Partial Fractions — Worked Examples (cont.) 🟡
<!-- See chunk 008 for the §12.12 method and earlier examples -->

### Example 12.39 (long-division then decomposition) — completion
`∫(x⁴ + 3x³ − 5x² − 4x + 17)/(x² + x − 2) dx`
- Long-divide: quotient x² + 2x − 5, remainder 3x + 7.
- Decompose (3x + 7)/[(x + 2)(x − 1)] = A/(x + 2) + B/(x − 1).
- 3x + 7 = A(x − 1) + B(x + 2).
- x = 1: 10 = 3B ⇒ B = 10/3.
- x = −2: 1 = −3A ⇒ A = −1/3.
- Integral = ∫ (x² + 2x − 5) dx − (1/3) ln|x + 2| + (10/3) ln|x − 1| + C
        = x³/3 + x² − 5x − (1/3) ln|x + 2| + (10/3) ln|x − 1| + C.
*(Source has slightly different numerators owing to OCR coefficients; the procedure is the canonical one.)*

### Example 12.40 (repeated linear factor) — ∫ (x + 7)/[x² (x + 2)] dx
- Decompose: (x + 7)/[x² (x + 2)] = A/x + B/x² + C/(x + 2).
- x + 7 = A x (x + 2) + B (x + 2) + C x².
- x = 0: 7 = 2B ⇒ B = 7/2.
- x = −2: 5 = 4C ⇒ C = 5/4.
- Equate coefficients of x²: 0 = A + C ⇒ A = −5/4.
- Integral = −(5/4) ln|x| − (7/2)/x + (5/4) ln|x + 2| + C.

### Example 12.41 (non-linear factor with x³ in denominator) — covers similar machinery, multiple unknowns

### Example 12.43: ∫ sin⁵ x dx via partial-fraction-style algebra
`sin⁵ x = sin x · (sin² x)² = sin x · (1 − cos² x)²`. Let u = cos x ⇒ du = −sin x dx.
`∫ sin⁵ x dx = − ∫ (1 − u²)² du = − ∫ (1 − 2u² + u⁴) du = − u + (2/3) u³ − u⁵/5 + C`
= −cos x + (2/3) cos³ x − (1/5) cos⁵ x + C.

> **Quick Recall:**
> - For repeated linear factors, you need ascending powers in the decomposition.
> - For "improper" rationals, long-divide before decomposing.
> - Trig integrals with odd powers reduce to substitution.

---

## Section: §12.13 Unit 12 Sum-Up 🟢

Unit 12 covered: indefinite integrals (anti-derivatives + C); definite integrals (numbers ≅ areas); methods — substitution, by parts, trig identities, partial fractions; convergence tests for improper integrals; numerous worked examples to drill technique.

---

## Section: §12.14 Key Words 🟡

| Term | Meaning |
|---|---|
| **Boundary condition** | A condition fixing C (e.g., y(x₀) = y₀) |
| **Closed interval** | [a, b] including endpoints |
| **Definite integral** | ∫ₐᵇ f(x) dx — a number; signed area |
| **Improper integral** | Definite integral with infinite bound or unbounded integrand; evaluated via limits |
| **Indefinite integral** | Anti-derivative — a function family F(x) + C |
| **Integration by parts** | ∫ u dv = uv − ∫ v du |
| **Partial fractions** | Decomposing p(x)/q(x) into simpler rational pieces |
| **Rational substitution** | Substituting to convert integrand into a rational function |
| **Riemann sum** | Σ f(xᵢ*) Δxᵢ — discrete approximation to ∫ |
| **Substitution rule** | ∫ f(g(x)) g'(x) dx = ∫ f(u) du, u = g(x) |

---

## Section: §12.15 CYP Solutions 🟡

### CYP1 (selected)
- Indefinite integral concept: anti-derivative — a function whose derivative is the given f.
- ∫ 4 dx = 4x + C.
- Power-rule integration: ∫ x² dx = x³/3 + C; ∫ (x² + 3) dx = x³/3 + 3x + C.
- ∫ −9 e^{3x} dx = −3 e^{3x} + C. (Source has -3e^{3x} which checks out: derivative is −9e^{3x}.)
- ∫ dx/(x + 2) = ln|x + 2| + C.

### CYP2 (selected)
- **CYP2(1):** ∫ cos(ax) dx = (1/a) sin(ax) + C, since d/dx[(1/a) sin(ax)] = cos(ax).
- **CYP2(2):** Always **try substitution first**; fall back to integration by parts if substitution fails.
- **CYP2(3):** ∫ x⁴ ln x dx — choose u = ln x (LIATE: log first); du = dx/x, dv = x⁴ dx, v = x⁵/5.

### CYP3 — Definite Integrals
1. **Definite integral**: integral with specific upper and lower bounds, giving a number.
2. **Riemann sum**: For partition a < x₁ < x₂ < … < x_{n−1} < b with mesh size max Δxₖ, the sum Σ f(x*ₖ) Δxₖ.

### CYP4 — Fundamental Theorem
- Connects derivative and integral.
- They are inverse operations: differentiate and then integrate gives back f.
- Definite integral = number (area under curve); indefinite integral = function (anti-derivative).

### CYP5 — Chain Rule for integration
1. Integration with chain rule reverses the chain rule for differentiation: ∫ a (g(x))^{n−1} g'(x) dx = a (g(x))ⁿ + C.
2. **Bounds change for u = 2x² + 3 over x ∈ [−1, 2]:** u(−1) = 5, u(2) = 11 ⇒ new bounds u ∈ [5, 11].
3. **Computing ∫_{−1}² 4x (2x² + 3)² dx:**
   - u = 2x² + 3, du = 4x dx ⇒ ∫₅¹¹ u² du = [u³/3]₅¹¹ = (11³ − 5³)/3 = (1331 − 125)/3 = 1206/3 = **402**.

### CYP6 — Improper Integrals
1. Improper integral: a definite integral with infinite limit or integrand approaching infinity in [a, b].
2. ∫_{−∞}^0 sin x dx: lim_{b → −∞} [cos b − cos 0] does not exist (oscillates) ⇒ **divergent**.
3. ∫_0^3 dx/√(3 − x): antiderivative −2√(3 − x). At x = 3: 0; at x = 0: −2√3. Value = 0 − (−2√3) = **2√3**. ⇒ **convergent**.

### CYP7 — Partial Fractions
**1. ∫(3x + 11)/(x² − x − 6) dx**:
- (x² − x − 6) = (x − 3)(x + 2). Decompose: A/(x − 3) + B/(x + 2).
- 3x + 11 = A(x + 2) + B(x − 3).
- x = −2: 5 = −5B ⇒ B = −1.
- x = 3: 20 = 5A ⇒ A = 4.
- ∫ = 4 ln|x − 3| − ln|x + 2| + C.

**2. ∫(2x + 7)/(x² + 4x + 3) dx**:
- (x² + 4x + 3) = (x + 1)(x + 3). Decompose A/(x + 1) + B/(x + 3).
- 2x + 7 = A(x + 3) + B(x + 1).
- x = −1: 5 = 2A ⇒ A = 5/2.
- x = −3: 1 = −2B ⇒ B = −1/2.
- ∫ = (5/2) ln|x + 1| − (1/2) ln|x + 3| + C.

**3. ∫(6x + 7)/(x + 2)² dx**:
- Decompose A/(x + 2) + B/(x + 2)².
- 6x + 7 = A(x + 2) + B.
- x = −2: −5 = B.
- Coeff of x: 6 = A.
- ∫ = 6 ln|x + 2| + 5/(x + 2) + C.

> **Quick Recall:**
> - For "(2x² + 3)" with x ∈ [−1, 2], the new u-bounds are 5 and 11.
> - 1/√(3 − x) on [0, 3] is improper at x = 3 — but converges (= 2√3).

---

## Section: §12.16 Unit 12 Exercises (Solved) 🟡

### Q1: ∫ sin⁶ x cos³ x dx
- cos³ x = cos x · (1 − sin² x). Let u = sin x, du = cos x dx.
- ∫ u⁶ (1 − u²) du = u⁷/7 − u⁹/9 + C = sin⁷ x / 7 − sin⁹ x / 9 + C.

### Q2: ∫ sin² x cos² x dx
- Use double-angle: sin² x = (1 − cos 2x)/2; cos² x = (1 + cos 2x)/2.
- Product = (1 − cos²(2x))/4 = sin²(2x)/4.
- = (1/4) ∫ (1 − cos 4x)/2 dx = (1/8) ∫ (1 − cos 4x) dx = x/8 − sin(4x)/32 + C.

### Q3: ∫ sec x dx = ln|sec x + tan x| + C
- Multiply numerator and denominator by (sec x + tan x): the derivative of (sec x + tan x) is sec x (sec x + tan x). Set u = sec x + tan x ⇒ du = sec x (sec x + tan x) dx.
- ∫ du/u = ln|u| + C = ln|sec x + tan x| + C.

### Q4: ∫ x e^{6x} dx
- u = x, dv = e^{6x} dx; du = dx, v = e^{6x}/6.
- ∫ x e^{6x} dx = x e^{6x}/6 − (1/6) ∫ e^{6x} dx = x e^{6x}/6 − e^{6x}/36 + C.

### Q5: ∫ x √(x + 1) dx — two ways
**(a) Integration by parts:** u = x, dv = √(x+1) dx, du = dx, v = (2/3)(x + 1)^{3/2}.
∫ x √(x+1) dx = (2x/3)(x+1)^{3/2} − (2/3) ∫ (x+1)^{3/2} dx = (2x/3)(x+1)^{3/2} − (4/15)(x+1)^{5/2} + C.

**(b) Substitution:** u = x + 1 ⇒ x = u − 1.
∫ (u − 1) √u du = ∫ (u^{3/2} − u^{1/2}) du = (2/5) u^{5/2} − (2/3) u^{3/2} + C
= (2/5)(x+1)^{5/2} − (2/3)(x+1)^{3/2} + C. *(Identical to (a) up to sign convention.)*

### Q6: ∫ ln x / x⁵ dx by parts
u = ln x, dv = x^{−5} dx; du = dx/x, v = −x^{−4}/4 = −1/(4x⁴).
∫ ln x / x⁵ dx = −ln x / (4x⁴) + (1/4) ∫ x^{−5} dx = −ln x / (4x⁴) − 1/(16 x⁴) + C.

### Q7: ∫ x² e^{3x} dx (parts twice)
- First: u = x², dv = e^{3x} dx; du = 2x dx, v = e^{3x}/3.
- ∫ = x² e^{3x}/3 − (2/3) ∫ x e^{3x} dx.
- Second by-parts on ∫ x e^{3x} dx: u = x, dv = e^{3x} dx ⇒ x e^{3x}/3 − e^{3x}/9.
- Final: x² e^{3x}/3 − (2/3)(x e^{3x}/3 − e^{3x}/9) + C = x² e^{3x}/3 − 2x e^{3x}/9 + 2 e^{3x}/27 + C.

### Q9: ∫_{−1}^{3} dx/x³ — divergent (split at 0)
Integrand has singularity at x = 0 ∈ [−1, 3]. Split into ∫_{−1}^0 + ∫_0^3. Either piece is divergent (1/x³ near 0 explodes) ⇒ **the integral diverges** without examining the other piece.

### Q10: ∫(2 − x)/(x² + 5x) dx
- x² + 5x = x(x + 5). Decompose (2 − x)/[x(x + 5)] = A/x + B/(x + 5).
- 2 − x = A(x + 5) + Bx.
- x = 0: 2 = 5A ⇒ A = 2/5.
- x = −5: 7 = −5B ⇒ B = −7/5.
- Integral = (2/5) ln|x| − (7/5) ln|x + 5| + C.

### Q11: ∫ 15 dx/(x² − 16)
- Factor: x² − 16 = (x − 4)(x + 4). Decompose 15/[(x − 4)(x + 4)] = A/(x − 4) + B/(x + 4).
- 15 = A(x + 4) + B(x − 4).
- x = 4: 15 = 8A ⇒ A = 15/8.
- x = −4: 15 = −8B ⇒ B = −15/8.
- Integral = (15/8) (ln|x − 4| − ln|x + 4|) + C.

> **Quick Recall:**
> - Q3 (∫ sec x): standard trick of multiplying by `(sec x + tan x)/(sec x + tan x)`.
> - Q5: ∫ x √(x+1) — substitution and parts both work.
> - Q9 demonstrates that a singularity *inside* the interval makes the integral improper even with finite bounds.

### Connections
- Builds on: Partial fraction decomposition (§12.12 in chunk 008); integration by parts (§12.5); FTC (§12.9).
- Closes Unit 12 / Block 3.

### Open Questions
1. How do you tell quickly that ∫ sec x dx requires the (sec x + tan x) trick rather than substitution?
2. For ∫ x² e^{3x}, why does **two** by-parts succeed, while ∫ e^{x²} dx has no closed-form antiderivative?


---


## Section: Publication Imprint 🟢

### Core Idea
Single-page back matter listing the publisher imprint and ISBN. No conceptual content.

### Key Concepts
- Publisher: MPDD/IGNOU.
- Print run: P.O. 5.3K, September 2023.
- ISBN: 978-93-5568-925-2.

### Connections
- Marks the end of Block 3 of MEC203 Quantitative Methods (Calculus).

### Open Questions
- (none — administrative page)


---

