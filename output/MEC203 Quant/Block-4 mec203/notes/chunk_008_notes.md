# Chunk 008 — Directional Derivatives, Jacobian, Hessian, Mean Value Theorem & Taylor's Theorem (Single Variable)
<!-- Pages: 71-80 -->
<!-- Source: chunk_008.txt -->

## Section: 14.5 Directional Derivatives (continued — three variables) [🔴]
<!-- Reason: extends gradient/dot-product formula to n variables; central exam fact -->

### Core Idea
For a differentiable `f(x, y, z)`, the directional derivative along a unit vector `û = ⟨cos α, cos β, cos γ⟩` is `D_û f = f_x cos α + f_y cos β + f_z cos γ = ⟨f_x, f_y, f_z⟩ · ⟨cos α, cos β, cos γ⟩`. The cosines are the direction cosines (one per coordinate axis). For a non-unit vector `V`, normalize to get `û = V/‖V‖`.

> **In Simple Terms:** Same gradient-dot-direction formula as 2D, just with more components. The direction is given by the cosines of the angles your arrow makes with each axis.

### Definitions
- **Direction cosines**: `(cos α, cos β, cos γ)` — the angles a unit vector makes with the `x`, `y`, `z` axes. ⭐
- **Directional derivative (3 variables)**: `D_û f = f_x cos α + f_y cos β + f_z cos γ`. ⭐

### Mechanisms / Processes
1. Compute `‖V‖`.
2. Form unit vector `û = V/‖V‖`.
3. Compute partials `f_x, f_y, f_z`.
4. Take dot product `∇f · û`.

### Examples
**Example 14.10** — `f(x, y, z) = 2xz² + 3y² z − x²yz` along `V = ⟨−1, 0, 3⟩`.
- `‖V‖ = √((−1)² + 0² + 3²) = √10`.
- `û = ⟨−1/√10, 0, 3/√10⟩`.
- `D_û f(x, y, z) = (−1/√10) f_x + 0 · f_y + (3/√10) f_z = (−1/√10){2z² − 2xyz} + (3/√10){4xz + 6yz − x²y}` *(per source)*.

### Connections
- Builds on: 14.5 (Chunk 007) — 2-variable directional derivative.
- Continues into: Jacobian (14.6) — generalizes the gradient row-vector to a matrix.

---

## Section: 14.6 Explicit Function from R^n to R^m, Jacobian Matrix, Hessian [🔴]
<!-- Reason: named matrices/definitions appearing in Key Words; central to optimization in MEC203 -->

### Core Idea
A function `f: R^n → R^m` can be written as `f(x) = (f_1(x), …, f_m(x))` with each `f_j: R^n → R`. The **Jacobian** `J_f` is the `m × n` matrix of all first-order partials `∂f_i/∂x_j`. When `n = m`, its determinant is the **Jacobian determinant** (used in multiple integrals). The **Hessian** of a scalar function `f: R^n → R` is the `n × n` matrix of all second-order partials `∂²f/(∂x_i ∂x_j)` and describes local curvature.

> **In Simple Terms:** Stack all gradients of all output components → Jacobian. Stack all second derivatives of one scalar output → Hessian.

### Key Concepts

#### 14.6.1 Function from R^n to R^m
For `f: R² → R⁴` defined by `f(x, y) = (x + y², 3x² − 5, x·y, 3y⁴)`, set `f_1(x, y) = x + y²`, `f_2(x, y) = 3x² − 5`, `f_3(x, y) = x·y`, `f_4(x, y) = 3y⁴`. In general, `f(x) = (f_1(x), …, f_m(x))`, each component a real-valued function on `R^n`.

#### 14.6.2 Jacobian / Jacobian matrix
The `nm` partial derivatives `∂f_i/∂x_j` for `i = 1,…,m`, `j = 1,…,n` are assumed to exist. The **Jacobian** is the `m × n` matrix `J_f(x) = (∂f_i/∂x_j)`. The `i`-th row of `J_f` is `∇f_i = [∂f_i/∂x_1, …, ∂f_i/∂x_n]`. Alternative notations: `D f`, `J_f`, `∇f`, `∂(f_1,…,f_m)/∂(x_1,…,x_n)`.

#### Jacobian determinant
If `n = m`, the Jacobian matrix is square, so its determinant is defined and called the **Jacobian determinant** (or just "Jacobian"). It is useful in evaluating multiple integrals. The text notes the ambiguity that "Jacobian matrix" is also sometimes called just "Jacobian".

#### 14.6.3 Hessian
For `f: R^n → R` mapping `x = (x_1, …, x_n)` to `f(x) ∈ R`, the Hessian `H_f` is the `n × n` matrix with `(i, j)` entry `∂²f/(∂x_i ∂x_j)`. **Hessian matrix describes the local curvature of a function of many variables.**

### Definitions
- **Jacobian of `f: R^n → R^m`**: the `m × n` matrix `J_f(x) = (∂f_i/∂x_j)`, `i = 1,…,m`, `j = 1,…,n`. ⭐
- **Jacobian determinant**: when `n = m`, the determinant `det(J_f)`; useful in multiple integrals. ⭐
- **Hessian of `f: R^n → R`**: the `n × n` matrix of second partials, `H_f[i,j] = ∂²f/(∂x_i ∂x_j)`. ⭐

### Examples
**Example 14.11 — Jacobian**
`f: R² → R²`, `f(x, y) = (e^{xy²}, 2x² + 3y²)`.
- `f_1(x, y) = e^{xy²}`, `f_2(x, y) = 2x² + 3y²`.
- `J_f = [[ y² e^{xy²},  2xy e^{xy²} ], [ 4x, 6y ]]`. *(per source: ∂f₁/∂x = y²e^{xy²}; ∂f₁/∂y = 2xy e^{xy²}; ∂f₂/∂x = 4x; ∂f₂/∂y = 6y)*
- At `(2, 1)`: `J_f(2, 1) = [[ e², 4e² ], [ 8, 6 ]]`. *(per source: 2e⁴ in first row, but transcript shows `[2e^4 4e^4 / 8 6]` — keep per source)*

**Example 14.12 — Hessian**
`f: R² → R`, `f(x, y) = e^{xy²}`.
- First partials: `∂f/∂x = y² e^{xy²}`, `∂f/∂y = 2xy e^{xy²}`.
- Second partials:
  - `∂²f/∂x² = y⁴ e^{xy²}`
  - `∂²f/(∂x ∂y) = (2y + 4xy³) e^{xy²} = 2y(1 + 2xy²) e^{xy²}` (source written as `(2 + 4xy) e^{xy²}` after simplification of OCR: rendered as `(2 + 4xy)`)
  - `∂²f/∂y² = (2x + 4x²y²) e^{xy²} = 4x²·… e^{xy²}` (per source `4x²·e^{xy²}` plus mixed term)
- `H_f(2, 1)` per source `= [[ 4e², 10e² ], [ 10e², 16 e² ]]`.

### Connections
- Builds on: gradient (14.5).
- Continues into: Hessian's role in second-order Taylor expansion (Chunk 009) and in optimization (Unit 15).

---

## Section: 14.7 Mean Value Theorem [🔴]
<!-- Reason: classical named theorem in Key Words list; basis for Taylor's theorem -->

### Core Idea
The MVT relates the average rate of change of a function over an interval to the instantaneous rate of change at some interior point. Geometrically, the tangent at some interior point is parallel to the secant joining the endpoints.

> **In Simple Terms:** If you average 60 km/h on a road trip, at some moment your speedometer must have read exactly 60.

### Key Concepts

#### History
A special case for inverse interpolation of sine was first described by Parameshvara (1380–1460) of the Kerala School of Astronomy and Mathematics. Now also called **Lagrange's Mean Value Theorem**.

#### 14.7.1 MVT for single variable
**Statement:** For real `a < b`, if `f: [a, b] → R` is continuous on `[a, b]` and differentiable on `(a, b)`, then there exists `c ∈ (a, b)` such that
`f'(c) = (f(b) − f(a))/(b − a)`.

**Geometric interpretation:** A continuous and (interior-)differentiable curve has at least one interior point where the tangent is parallel to the chord joining `(a, f(a))` and `(b, f(b))`.

#### 14.7.2 MVT for several variables (optional reading)
For `f: G → R` differentiable on an open set `G ⊆ R^n`, and `x, y ∈ G`, there exists `c ∈ (0, 1)` such that
`f(y) − f(x) = ∇f((1 − c)x + c y) · (y − x)`.

The point `(1 − c)x + c y` lies on the line segment from `x` to `y`, and `∇f · (y − x)` is the directional derivative along the chord.

### Definitions
- **Mean Value Theorem (single variable)**: continuous on `[a, b]`, differentiable on `(a, b)` ⇒ `∃ c ∈ (a, b)`: `f'(c) = (f(b) − f(a))/(b − a)`. ⭐
- **MVT (several variables)**: differentiable on open `G ⊆ R^n`; for `x, y ∈ G`, `∃ c ∈ (0,1)`: `f(y) − f(x) = ∇f((1 − c)x + c y) · (y − x)`. ⭐

### Examples
**Example 14.13** — `f(y) = 2y² + 3y + 4` on `[1, 2]`.
- Polynomial → continuous and differentiable everywhere → MVT applies.
- `f'(y) = 4y + 3`; at the MVT point `c`: `4c + 3 = (f(2) − f(1))/(2 − 1) = (18 − 9)/1 = 9`.
- `4c = 6` ⇒ `c = 3/2 ∈ (1, 2)`. ✓

### ⚠️ Common Mistakes
- ❌ Applying MVT to a function with a discontinuity in `[a, b]` → ✅ Continuity on closed interval is required.

### Connections
- Continues into: Taylor's theorem (14.8) — Lagrange-form remainder uses MVT.
- Used in Exercises 7 & 8 (Chunk 010): `f' ≡ 0 ⇒ f` constant; `f' > 0 ⇒ f` strictly increasing.

---

## Section: 14.8 Polynomial Approximation: Taylor's Theorem, Linear & Quadratic Approximations [🔴]
<!-- Reason: named theorem; fundamental tool; explicit Taylor formula in Key Words list -->

### Core Idea
Many "elementary" functions (`√x`, `x^{2/3}`, `eˣ`, `log x`, `sin x`) cannot be evaluated as rational numbers exactly even at simple inputs. They can however be **approximated** by polynomials, which are easy to evaluate (since `xⁿ` is rational when `x` is rational, but `eˣ` and `log x` typically aren't). Taylor's approach builds the approximating polynomial out of values of `f` and its derivatives at a known point `a`.

> **In Simple Terms:** If you know the function and its slopes at one point, you can build a polynomial that closely matches the function nearby — that's a Taylor polynomial. Adding higher-order terms makes the match better.

### Key Concepts

#### Why polynomials?
Polynomial values are rational when inputs are rational, regardless of degree, so they are computable. Other elementary functions (`eˣ`, `log x`) generally produce irrational outputs even from rational inputs.

#### 14.8.1 Taylor's polynomial of order `k`
Given `f(a), f'(a), f''(a), …, f^{(k)}(a)`,
`P_{k,a}(x) = f(a) + f'(a)(x − a) + (f''(a)/2!)(x − a)² + … + (f^{(k)}(a)/k!)(x − a)^k`. ... (14.11)

Then **Taylor's formula** is `f(x) = P_{k,a}(x) + R_{k,a}(x)`, where `R_{k,a}(x)` is the **remainder term** representing the error of approximation. ... (14.12)

For "well-behaved" `f`, `lim_{x → a} R_{k,a}(x) = 0`.

#### Forms of the remainder (mentioned, may be skipped)
- **Peano's form**: `R_{k,a}(x) = h_{k,a}(x)·(x − a)^k`, with `lim_{x → a} h_{k,a}(x) = 0`.
- **Lagrange mean-value form**: `R_k(x) = (f^{(k+1)}(c)/(k+1)!)·(x − a)^{k+1}` for some `c` between `a` and `x`.
- **Cauchy's form**: `R_k(x) = (f^{(k+1)}(c)/k!)·(x − c)^k(x − a)`.

#### 14.8.2 Taylor's theorem (statement, no proof)
For integer `k ≥ 1`, if `f: R → R` is `k`-times differentiable at `a`, then there exists a function `R_k(x, a)` such that
`f(x) = f(a) + f'(a)(x − a) + (f''(a)/2!)(x − a)² + … + (f^{(k)}(a)/k!)(x − a)^k + R_k(x, a)`,
and `lim_{x → a} R_k(x, a) = 0`. The function `R_k(x, a)` depends on `x`, `a`, and `f`.

#### 14.8.3 Taylor's series / expansion
For functions infinitely differentiable at `a` (like `eˣ`, `sin x`),
`f(x) = Σ_{n=0}^∞ (f^{(n)}(a)/n!)(x − a)^n`,
where `0! = 1` and `(x − a)⁰ = 1`. ... (14.13)

### Definitions
- **Taylor polynomial `P_{k, a}`**: `Σ_{j=0}^k (f^{(j)}(a)/j!)(x − a)^j`. ⭐
- **Taylor's formula**: `f(x) = P_{k,a}(x) + R_{k,a}(x)`. ⭐
- **Remainder term `R_{k,a}(x)`**: error of polynomial approximation; depends on `k`, `a`, `f`. ⭐
- **Taylor's series**: infinite version of Taylor's polynomial when `f` has all derivatives at `a` and `R_k → 0`. ⭐

> **Quick Recall:**
> - `P_{k,a}(x) = Σ_{j=0}^k f^{(j)}(a)·(x − a)^j / j!`
> - `f(x) = P_{k,a}(x) + R_{k,a}(x)`
> - For nice `f`, `R_{k,a}(x) → 0` as `x → a`.

### Connections
- Builds on: MVT (14.7) — supplies the Lagrange remainder.
- Continues into: Maclaurin series (14.8.4), linear/quadratic approximation (14.8.5), and multivariate Taylor (14.9) — all in Chunk 009.

### Open Questions
1. The remainder forms (Peano, Lagrange, Cauchy) are stated but not used; under what conditions is each preferred? (Beyond scope of the unit.)
