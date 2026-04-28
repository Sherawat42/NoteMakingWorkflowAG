# Chunk 007 — Partial Derivatives, Chain Rule & Higher-Order Partials
<!-- Pages: 61-70 -->
<!-- Source: chunk_007.txt -->

## Section: 14.4 Overview of Partial Derivatives & Higher Order Partial Derivatives [🟢]
<!-- Reason: framing/recap section; orients the reader to the three forms of dependent-variable specification -->

### Core Idea
A dependent variable can be specified in three forms: (i) **explicitly** as a single function of the independent variables; (ii) **implicitly** in an equation where neither side is a single variable; (iii) as a **composition** (a non-circular chain of functional definitions). Partial derivatives arise only when a variable depends, directly or indirectly, on two or more variables.

> **In Simple Terms:** Same idea as a one-variable derivative, but only one input is allowed to wiggle while the others stay frozen. The form (explicit / implicit / chain) just changes the bookkeeping.

### Key Concepts

#### Three issues for multivariate derivatives
For functions of two or more variables we must address: (a) how the calculation procedure is modified, (b) how notation is modified, and (c) how the idea of "rate of change" evolves.

### Connections
- Builds on: Unit 11 (single-variable derivatives) and Unit 13 (limits, several real variables).
- Continues into: explicit partial derivatives (14.4.1) and the rest of section 14.4.

---

## Section: 14.4.1 Partial Derivative of Function with Explicit Representation [🔴]
<!-- Reason: defines partial derivative formally; sets all notation used through unit -->

### Core Idea
For `U = f(x, y)`, `f_x(x, y)` is the derivative of `f` w.r.t. `x` treating `y` as a constant; defined as the one-variable limit `lim_{h→0} [f(x+h, y) − f(x, y)]/h`. Similarly `f_y(x, y) = lim_{h→0} [f(x, y+h) − f(x, y)]/h`.

> **In Simple Terms:** Pretend the other variables are numbers (constants), and differentiate with the usual one-variable rules.

### Definitions
- **Partial derivative `f_x`**: `lim_{h→0} [f(x+h, y) − f(x, y)] / h`. ⭐
- **Partial derivative `f_y`**: `lim_{h→0} [f(x, y+h) − f(x, y)] / h`. ⭐
- **Alternative notations for `f_x`**: `∂f/∂x`, `∂U/∂x`, `D_x f`, `D_x f(x, y)`.

### Examples
**Example 14.4**

(i) `z = g(x, y) = 5x³ y⁴`
- `g_x(x, y) = ∂g/∂x = 5y⁴ · (3x²) = 15 y⁴ x²`
- `g_y(x, y) = (5x³)(4y³) = 20 x³ y³`

(ii) `v = h(x, y, w) = x² cos(y)/w`
- `∂v/∂x = 2x cos(y)/w`
- `∂v/∂y = (x²/w)(−sin(y)) = −(x² sin(y)/w)`
- `∂v/∂w = x² cos(y) · (−w⁻²) = −2 x² cos(y)/w³` *(source has minor OCR ambiguity but states "= −2 {x² cos(y)/w³}")*

### Connections
- Builds on: Section 14.2 limit concept.
- Continues into: implicit (14.4.2), composite (14.4.3), higher-order (14.4.4) cases.

---

## Section: 14.4.2 Partial Derivative of Function with Implicit Representation [🟡]
<!-- Reason: secondary mechanism — same idea, applied to implicit equations -->

### Core Idea
For an implicit relation among ≥ 3 variables, e.g. `2x⁴y³z² − 7x²y⁵z = x⁴ + y³`, you must (i) name the dependent variable and (ii) differentiate both sides treating other variables as constants, then collect terms in `∂z/∂x` and solve.

> **In Simple Terms:** Treat `z` as a hidden function of `x` (with `y` frozen). Differentiate both sides, gather all `∂z/∂x` terms on one side, and isolate.

### Mechanisms / Processes
1. State which variable is dependent.
2. Differentiate both sides w.r.t. the chosen independent variable, treating other independent variables as constants and using product/chain rule on terms involving the dependent variable.
3. Move all terms with the partial on LHS, others on RHS, factor and divide.

### Examples
**Implicit example (eq. 14.6 / 14.7):** `2x⁴y³z² − 7x²y⁵z = x⁴ + y³`.

For `∂z/∂x` (y constant):
- `2y³ · {(4x³)z² + x⁴(3z²)(∂z/∂x)} − 7y⁵ · {(2x)z + x²(∂z/∂x)} = 4x³`
- Collect `∂z/∂x` on LHS, the rest on RHS:
- `x · (6x³z² − 7y⁵) · (∂z/∂x) = x³(4 − 8z²) + 14 y³ z`  *(using OCR-cleaned form)*
- `∂z/∂x = {x³(4 − 8z²) + 14 y³ z} / [x(6x³z² − 7y⁵)]`

For `∂z/∂y` (x constant):
- `(2x⁴)(3z²)(∂z/∂y) − (7x²){5y⁴ z + y⁵ (∂z/∂y)} = 3y²`
- `∂z/∂y = (y²/x²)·{3 + 35 x² y³ z} / [6x²z² − 7 y⁵]` (per source).

### ⚠️ Common Mistakes
- ❌ Forgetting product rule on terms like `x⁴ z²` when differentiating w.r.t. `x` (since `z` depends on `x`) → ✅ Use `(4x³)z² + x⁴(2z)(∂z/∂x)`.

### Connections
- Builds on: 14.4.1 (explicit case).

---

## Section: 14.4.3 Chain Rule & Composite Functions [🔴]
<!-- Reason: chain rule is universal; partial-derivative chain rule is exam-critical -->

### Core Idea
The chain rule lets you compute derivatives of nested compositions by multiplying derivatives along the chain. For one independent variable: `dy/dx = (dy/dz)(dz/dw)(dw/dx)`. For partials, contributions through every dependency path are summed.

> **In Simple Terms:** "Peel" the composition from outside in, multiplying derivatives at each layer. With several variables, sum the contributions from every path that connects the inputs to the output.

### Key Concepts

#### 14.4.3.1 Chain rule for single independent variable
For `y = log(sin(eˣ + 7x²))`, set `z = sin(eˣ + 7x²)`, `w = eˣ + 7x²`, so `y = log z`, `z = sin w`, `w = eˣ + 7x²`. Then:
`dy/dx = (dy/dz)(dz/dw)(dw/dx) = [1/sin w][cos w][eˣ + 14x] = (eˣ + 14x) cot(eˣ + 7x²)`.

**Caution:** `dy/dx` is a single symbol — the slash is *not* a fraction. It is a notational accident that the chain rule looks like cancellation. The chain rule has been **proved**; it is not just symbolic cancellation.

#### 14.4.3.2 Chain rule for partial derivatives
**Case I:** `w(x, y)` with `x = x(t)`, `y = y(t)` (single parameter).
`dw/dt = (∂w/∂x)(dx/dt) + (∂w/∂y)(dy/dt)`

**Case II:** `w(x, y)` with `x = x(r, s)`, `y = y(r, s)`.
`∂w/∂r = (∂w/∂x)(∂x/∂r) + (∂w/∂y)(∂y/∂r)`
`∂w/∂s = (∂w/∂x)(∂x/∂s) + (∂w/∂y)(∂y/∂s)`

### Examples
**Example 14.6 — Single parameter case**
`w(x, y) = (2x + 3y)²`, `x = (t+1)^{1/2}`, `y = t²`.
`dw/dt = [2(2x+3y)·2] · (½)(t+1)^{−1/2} + [2(2x+3y)·3] · (2t)`.

**Example 14.7 — Two-parameter case**
`w(x, y) = (2x + 3y)²`, `x = (2r + s)^{1/2}`, `y = (r − 2s)²`.
`∂w/∂r = [4(2x+3y)] · (½)(2r+s)^{−1/2}(2) + [6(2x+3y)] · [2(r−2s)·1]`
`∂w/∂s = [4(2x+3y)] · (½)(2r+s)^{−1/2}(1) + [6(2x+3y)] · [2(r−2s)·(−2)]`

### ⚠️ Common Mistakes
- ❌ Treating `dy/dx` as a fraction and "cancelling" `dz` with `dz` → ✅ The chain rule is a proved theorem; the notation is suggestive but not algebraic.

### Connections
- Builds on: 14.4.1 explicit derivatives.
- Continues into: total differentials (14.4.6) and Taylor multivariate (Chunk 009).

---

## Section: 14.4.4 Higher Order Partial Derivatives [🔴]
<!-- Reason: notation conventions are exam-critical; foundation for Hessian, Taylor, Young's theorem -->

### Core Idea
Partial derivatives are themselves functions; differentiating again gives second-order partials, and so on. Notation: in subscript form `f_xy` means "first `x`, then `y`"; in `∂` form `∂²f/(∂y ∂x)` means the same thing. **Suffix order rule:** later variables go on the **right** in `f_…` notation, on the **left** in `∂…` notation.

> **In Simple Terms:** Differentiate twice. The two notations read in opposite directions — be careful which one you use.

### Definitions
- **Second-order partial `f_{xx}`**: `∂²f/∂x² = ∂/∂x (∂f/∂x)`. ⭐
- **Mixed partial `f_{xy}`**: `∂/∂y(∂f/∂x) = ∂²f/(∂y ∂x)`. ⭐

### Mechanisms / Processes
1. Compute first-order partial `f_x`.
2. Treat it as a new function and partial-differentiate w.r.t. `x` or `y`.
3. Continue for third- and higher-order derivatives.

### Examples
For `z = f(x, y) = 5x³ y⁴`:
- `f_x = 15 y⁴ x²`, `f_y = 20 x³ y³`
- `z_{xx} = ∂²f/∂x² = 30 y⁴ x`
- `z_{xy} = ∂²f/(∂y ∂x) = 60 y³ x²`

### Edge Cases & Caveats
- The text remarks that first-order partials always have explicit form regardless of how the original function was given (explicit/implicit/composite). So the method for higher-order derivatives is the **explicit-case method** of 14.4.1.

### Connections
- Continues into: Hessian (14.6.3, Chunk 008), Taylor's theorem (14.8, Chunks 008–009).

---

## Section: 14.4.5 Interpretation of Partial Derivatives [🟡]
<!-- Reason: connects calculation to economic intuition (rate of change) -->

### Core Idea
`f_x(x, y)` is the rate of change of `f` as `x` changes with `y` held fixed; `f_y(x, y)` similarly with `y` varying. Sign indicates direction: positive → increasing in that variable, negative → decreasing. A function may simultaneously be increasing in one variable and decreasing in another at a point.

### Examples
**Example 14.8** — Is `f(x, y) = 2x³/(3y²)` increasing or decreasing at `(1, 3)`?
- `f_x = 4x²/(3y²)` ⇒ `f_x(1, 3) = (4/3)(1/9) > 0` → increasing in `x` (with `y` fixed).
- `f_y = −2 · (2x³/3) · y⁻³ = −2x³/y³` *(per source: `f_y = 6(2x³/3y²)/dy = [(2/3)·(−3)]/y³ = −2x³/y³`)*. Wait — but source uses `2x³/3 y²`. Let me re-state per source: `f_y(x, y) = −2x³/y³`. Then `f_y(1, 3) = −2/81 < 0` → decreasing in `y` (with `x` fixed).

### Connections
- Builds on: 14.4.1.
- Continues into: directional derivatives (14.5).

---

## Section: 14.4.6 Differential / Total Differential [🔴]
<!-- Reason: key formula appearing in Key Words list and used through optimization, integration, ODEs -->

### Core Idea
For one variable, `dy = f'(x) dx` (or `df = f'(x) dx`). For a function of several variables, the **total differential** sums each partial derivative times the corresponding variable's differential.

> **In Simple Terms:** Total change = sum of (rate of change in each direction) × (small step in that direction).

### Definitions
- **Total differential of `z = f(x, y)`**: `dz = f_x dx + f_y dy` (equivalently `df = f_x dx + f_y dy`). ⭐
- **Total differential of `w = h(x, y, z)`**: `dw = h_x dx + h_y dy + h_z dz`. ⭐

> **Quick Recall:**
> - 1 variable: `dy = f'(x) dx`
> - 2 variables: `dz = f_x dx + f_y dy`
> - 3 variables: `dw = h_x dx + h_y dy + h_z dz`

### Connections
- Plays significant role in Integral Calculus and Differential Equations (per text).
- Builds on: 14.4.1.

---

## Section: 14.5 Directional Derivatives (start) [🔴]
<!-- Reason: named formula, central to gradient and continued throughout unit -->

### Core Idea
Partial derivatives only measure change in axis-aligned directions. The **directional derivative** measures the rate of change of `f(x, y)` along an arbitrary unit direction `Â` making angle `θ` with the positive `x`-axis. By a stated (unproved) result, for a differentiable `f`, `D_Â f(x, y) = f_x cos θ + f_y sin θ`, which equals the dot product of the gradient `∇f = ⟨f_x, f_y⟩` with the unit vector `⟨cos θ, cos(π/2 − θ)⟩`.

> **In Simple Terms:** Pick a direction. The directional derivative is how fast the function changes if you walk one unit step in that direction. It's just the gradient dotted with the unit direction vector.

### Definitions
- **Directional derivative (formal)**: `D_A f(x, y) = lim_{|A|→0} [f(x + |A| cos θ, y + |A| sin θ) − f(x, y)] / |A|`. ⭐
- **Gradient `∇f`**: the vector `⟨f_x, f_y⟩`. ⭐
- **Formula (differentiable f)**: `D_Â f(x, y) = f_x cos θ + f_y sin θ = ⟨f_x, f_y⟩ · ⟨cos θ, cos(π/2 − θ)⟩ = ∇f · Â`. ⭐

### Examples
**Example 14.9 (start)** — `f(x, y) = x² e^{xy} + 3y²` at `(0, 2)` along unit vector `Û` in direction `θ = 2π/3`.
- `Û = ⟨cos(2π/3), sin(2π/3)⟩ = ⟨−½, (√3)/2⟩`.
- `D_Û f(x, y) = −½ f_x + (√3/2) f_y`
  `= −½ {2x e^{xy} + x²y e^{xy}} + (√3/2){x³ e^{xy} + 6y}` *(per source)*
- At `(0, 2)`: `D_Û f(0, 2) = −½ · 0 + (√3/2)(0 + 12) = 6√3`.

### Connections
- Builds on: partial derivatives (14.4) and inner product (Section 6.4 of Unit 6).
- Continues into: 3-variable directional derivatives, Jacobian, Hessian (Chunk 008).

### Open Questions
1. Why `cos(π/2 − θ)` for the second component of the unit vector — i.e. how is the same formula generalized to `n` axes via direction cosines? (Addressed in Chunk 008.)
