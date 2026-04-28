# Chunk 002 — Unit 9 wrap-up + Unit 10 begin (§9.6.1–§9.10; §10.0–§10.3)
<!-- Pages: 11-20 -->
<!-- Source: chunk_002.txt -->

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
