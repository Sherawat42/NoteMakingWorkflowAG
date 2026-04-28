# Chunk 009 — Maclaurin Series, Linear/Quadratic Approximation & Multivariate Taylor's Theorem
<!-- Pages: 81-90 -->
<!-- Source: chunk_009.txt -->

## Section: 14.8.4 Maclaurin's Series [🔴]
<!-- Reason: named special case; classical formula appearing in standard exam questions -->

### Core Idea
The **Maclaurin series** is the special case of Taylor's series with `a = 0`. Under the conditions of Taylor's theorem,
`f(x) = f(0) + f'(0) x + (f''(0)/2!) x² + (f'''(0)/3!) x³ + … + (f^{(n)}(0)/n!) xⁿ + …`. ... (14.14)

> **In Simple Terms:** Taylor expansion centred at 0.

### Definitions
- **Maclaurin series**: Taylor's series with expansion point `a = 0`. ⭐

### Connections
- Special case of: Taylor's series (14.8.3, Chunk 008).

---

## Section: 14.8.5 Linear / Quadratic Approximation [🔴]
<!-- Reason: directly used in optimization, regression, error analysis; explicit polynomials worth memorizing -->

### Core Idea
Truncating the Taylor polynomial at order 1 gives the **linear approximation** (a tangent-line approximation); truncating at order 2 gives the **quadratic approximation** (a parabolic approximation). Higher order → smaller expected error.

> **In Simple Terms:** Pick how many derivatives to use. Use 1 → straight-line approximation. Use 2 → parabolic approximation. The remainder shrinks as the order grows.

### Definitions
- **Linear approximation `P_{1, a}`**: `f(a) + f'(a)(x − a)`. (14.15) ⭐
- **Quadratic approximation `P_{2, a}`**: `f(a) + f'(a)(x − a) + (f''(a)/2!)(x − a)²`. (14.17) ⭐
- **Taylor's formula (linear)**: `f(x) = P_{1,a} + R_1(x, a)`, with `lim_{x→a} R_1 = 0`. (14.16)
- **Taylor's formula (quadratic)**: `f(x) = P_{2,a} + R_2(x, a)`, with `lim_{x→a} R_2 = 0`. (14.18)

### Mechanisms / Processes
1. Compute `f(a)`.
2. Compute `f'(a)` (and `f''(a)` for quadratic).
3. Plug into the polynomial template.
4. Error of approximation is `R_k(x)`.

### Examples
**Example 14.14 — `f(x) = sin(x)`**
Values at `x = 0`: `sin(0) = 0`, `f'(0) = cos(0) = 1`, `f''(0) = −sin(0) = 0`, `f'''(0) = −cos(0) = −1`. (14.19)

**Part (i) Linear approximation**: `P_{1, 0} = sin(0) + x · cos(0) = 0 + x = x`.

**Part (i) Quadratic approximation**: `P_{2, 0} = 0 + x·1 + (x²/2!)·0 = x`.

**Part (ii) Maclaurin expansion** — derivative values cycle `0, 1, 0, −1, 0, 1, …`. Substituting:
`sin(x) = 0 + x·1 + (x²/2!)·0 + (x³/3!)·(−1) + (x⁴/4!)·0 + (x⁵/5!)·1 + … = x − x³/3! + x⁵/5! − x⁷/7! + …`.

### ⚠️ Common Mistakes
- ❌ Forgetting that the quadratic approximation includes the linear part → ✅ `P_{2,a} = P_{1,a} + (f''(a)/2!)(x − a)²`.

> **Quick Recall:**
> - `sin(x) = x − x³/3! + x⁵/5! − x⁷/7! + …`
> - `cos(x) = 1 − x²/2! + x⁴/4! − x⁶/6! + …` (derived in Chunk 010 CYP4 Q3)
> - `log(x)` around `x = 1`: `(x − 1) − (x − 1)²/2 + (x − 1)³/3 − …` (Chunk 010 CYP4 Q4)

### Connections
- Builds on: 14.8.1–14.8.3 (Chunk 008).
- Continues into: multivariate linear/quadratic approximation (14.9.1, 14.9.2).

---

## Section: 14.9 Multivariate Polynomial Approximation: Taylor's Theorem, Linear Approximation [🔴]
<!-- Reason: multivariate Taylor is heavily used in optimization, econometrics, comparative statics -->

### Core Idea
Multivariate polynomial approximation generalizes Taylor's theorem to functions of two or more variables. Build-up is staged: first linear approximation in 2 variables, then quadratic, then arbitrary order in `n` variables.

### Key Concepts

#### 14.9.1 Linear approximation in two variables (order 1)
At point `(a, b)`:
`P_{1, (a, b)}(x, y) = f(a, b) + (x − a) f_x(a, b) + (y − b) f_y(a, b)`. ... (14.20)

Taylor's formula: `f(x, y) = P_{1, (a, b)} + R_1(x, y)`, provided `lim_{(x,y) → (a,b)} R_1(x, y) = 0`. ... (14.21)

Required: values of `f, f_x, f_y` at `(a, b)`. Approximation called "linear" because `P_1` is degree one.

#### 14.9.2 Quadratic approximation in two variables (order 2)
At point `(a, b)`:
`P_{2, (a, b)}(x, y) = f(a, b) + {(x − a) f_x(a, b) + (y − b) f_y(a, b)} + {((x − a)²/2!) f_{xx}(a, b) + (x − a)(y − b) f_{xy}(a, b) + ((y − b)²/2!) f_{yy}(a, b)}`. ... (14.22)

Taylor's formula: `f(x, y) = P_{2, (a, b)} + R_2(x, y)`, with `lim_{(x,y)→(a,b)} R_2 = 0`. ... (14.23)

**Necessary condition for (14.23):** `f` has continuous first- and second-order partials at `(a, b)`.

In practice, "generally we use at most quadratic approximation."

#### 14.9.3 General Taylor's theorem (n variables, order k) — optional
For `F: R^n → R` and points `x = (x_1, …, x_n)`, `a = (a_1, …, a_n)`,
`P_k(x, a) = F(a) + Σ_{i} F_{x_i}(a)(x_i − a_i) + (1/2!) Σ_{i, j} F_{x_i x_j}(a)(x_i − a_i)(x_j − a_j) + … + (1/k!) Σ_{i_1, …, i_k} F_{x_{i_1} … x_{i_k}}(a)(x_{i_1} − a_{i_1}) … (x_{i_k} − a_{i_k})`. ... (14.24)

**Theorem:** there exists `R_k(x, a)` such that `F(x) = P_k(x, a) + R_k(x, a)` and `lim_{x → a} R_k(x, a) = 0`. ... (14.25) Error of approximation is `R_k(x, a)`.

The argument extends straightforwardly to `f: R^n → R^m` componentwise: `f = (f_1, …, f_m)`.

#### 14.9.3.1 Multivariate Taylor's series expansion
For functions infinitely differentiable at `a` (like `e^{x+y+z}`),
`F(x) = Σ_{k=0}^∞ (1/k!) Σ_{i_1, …, i_k} F_{x_{i_1} … x_{i_k}}(a) · (x_{i_1} − a_{i_1}) … (x_{i_k} − a_{i_k})`.

### Definitions
- **Linear (Taylor) approximation 2 variables**: `P_{1, (a,b)} = f(a,b) + (x−a) f_x(a,b) + (y−b) f_y(a,b)`. ⭐
- **Quadratic (Taylor) approximation 2 variables**: as in (14.22). ⭐
- **General Taylor polynomial of order `k` in `n` variables**: as in (14.24).

### Mechanisms / Processes
1. Compute `f(a)` and all required partials of order ≤ `k` at `a`.
2. Substitute into the order-`k` Taylor polynomial.
3. The remainder term provides the error.

### Examples
**Example 14.15 — Order-3 Taylor polynomial of `F(x_1, x_2, x_3) = e^{x_1 + x_2 + x_3}` near (0, 0, 0).**

All partials of `F` equal `e^{x_1 + x_2 + x_3}`, so at `(0, 0, 0)` every value is `1`:
`F(0,0,0) = 1`, `F_{x_i}(0,0,0) = 1`, `F_{x_i x_j}(0,0,0) = 1`, `F_{x_i x_j x_k}(0,0,0) = 1` for all `i, j, k`.

Substituting in (14.24) with `n = 3, k = 3, a = (0, 0, 0)`:
`F(x) = 1 + (x_1 + x_2 + x_3) + (1/2!)(x_1 + x_2 + x_3)² + (1/3!)(x_1 + x_2 + x_3)³`.

**Example 14.16 — Taylor series for `f(x, y, z) = xyz` around `(1, 1, 1)`.**
- `f(1, 1, 1) = 1`.
- First partials: `f_x = yz`, `f_y = xz`, `f_z = xy`; each `= 1` at `(1, 1, 1)`.
- Pure second partials all zero (`f_{xx} = f_{yy} = f_{zz} = 0`); mixed second partials: `f_{xy} = z`, `f_{xz} = y`, `f_{yz} = x`; each `= 1` at `(1, 1, 1)`.
- Third partial: only `f_{xyz} = 1` is non-zero; all others zero.
- Fourth and higher: all zero.

Substituting:
`f(x, y, z) = 1 + {(x − 1) + (y − 1) + (z − 1)} + (1/2)·2·{(x − 1)(y − 1) + (y − 1)(z − 1) + (x − 1)(z − 1)} + (1/3!)·6·{(x − 1)(y − 1)(z − 1)} + 0 + …`
`= 1 + (x − 1) + (y − 1) + (z − 1) + {(x − 1)(y − 1) + (y − 1)(z − 1) + (x − 1)(z − 1)} + (x − 1)(y − 1)(z − 1)`.

### ⚠️ Common Mistakes
- ❌ Forgetting the cross term `(x − a)(y − b) f_{xy}(a, b)` in the quadratic 2-variable Taylor → ✅ Always include it.
- ❌ Using the wrong factor `1/2!` for cross-terms — note the source formula uses `(x − a)(y − b) f_{xy}` with no `1/2!` because both off-diagonal entries `f_{xy}` and `f_{yx}` are summed.

> **Quick Recall (2-variable):**
> - Linear: `f(a,b) + f_x(a,b)(x − a) + f_y(a,b)(y − b)`
> - Quadratic adds: `½ f_{xx}(a,b)(x − a)² + f_{xy}(a,b)(x − a)(y − b) + ½ f_{yy}(a,b)(y − b)²`

### Connections
- Builds on: 14.4 partials, 14.4.4 higher-order partials, 14.8.5 single-variable approximations.
- Continues into: optimization (Unit 15) — second-order conditions use Hessian and quadratic Taylor.

---

## Section: 14.10 Let Us Sum Up [🟢]
<!-- Reason: recap material -->

### Core Idea
The unit covered: limits of multivariate functions, partial derivatives (explicit, implicit, composite via chain rule), higher-order partials, directional derivatives, Jacobian, Hessian, Mean Value Theorem (one and several variables), Taylor's theorem and series for one and several variables, with applications to polynomial approximation.

### Connections
- Recap of all sections in Unit 14.

---

## Section: 14.11 Key Words [🔴]
<!-- Reason: official examination terminology -->

### Definitions
- **Partial derivative**: derivative of a dependent variable `z` w.r.t. one or more of the variables `x, y, w, …` while treating at least one of them as a constant. ⭐
- **Unit vector specification (in `n`-D)**: `(cos θ_1, cos θ_2, …, cos θ_n)`, where `θ_i` is the angle the vector makes with the `i`-th axis. For `n = 2`, with `θ` the angle with `x`-axis, the unit vector is `(cos θ, cos(π/2 − θ))`. ⭐
- **Gradient `∇f`**: for `f` of `n` variables `x_1, …, x_n`, `∇f = ⟨f_{x_1}, …, f_{x_n}⟩`. ⭐
- **Directional derivative**: in multivariate calculus, the derivative along a chosen direction at a point. If `û = (cos θ_1, …, cos θ_n)` and `∇f = ⟨f_{x_1}, …, f_{x_n}⟩`, then `D_û f = ∇f · û`. ⭐
- **Jacobian**: for `f: R^n → R^m`, the `m × n` matrix `J_f(x) = (∂f_i/∂x_j)`. ⭐
- **Hessian**: for `f: R^n → R`, the `n × n` matrix of second partials. ⭐
- **Mean Value Theorem**: continuous on `[a, b]`, differentiable on `(a, b)` ⇒ `∃ c ∈ (a, b)`: `f'(c) = (f(b) − f(a))/(b − a)`. ⭐
- **Taylor's formula**: `f(x) = P_{k, a}(x) + R_{k, a}(x)`, where `P_{k, a} = f(a) + f'(a)(x − a) + (f''(a)/2!)(x − a)² + … + (f^{(k)}(a)/k!)(x − a)^k`. ⭐

---

## Section: 14.12 Answers — Check Your Progress 1, Q1 [🟡]
<!-- Reason: worked exercise solution -->

### Examples
**CYP1 Q1** — `lim_{(x, y) → (4, 1)} 3 x y² / (x + y)`.

The function fails continuity along `x + y = 0`, but `(4, 1)` does not lie on that line. On the rest of the domain (including `(4, 1)`) the function is continuous, so the limit equals the value:
`lim = 3·(4)·(1)² / (4 + 1) = 12/5`.

### Connections
- Builds on: 14.3 continuity-based limit shortcut.
