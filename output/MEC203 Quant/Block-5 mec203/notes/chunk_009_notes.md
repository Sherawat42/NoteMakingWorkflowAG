# Chunk 009 — Unit 19 — Homothetic, Concave/Quasi-Concave, Bordered Hessian, Euler
<!-- Pages: 81-90 -->
<!-- Source: chunk_009.txt -->
<!-- See chunk 008 for start of homogeneous functions -->

## Section: Homothetic Functions — Definition & Properties 🔴

### Core Idea
**Homothetic** functions are **monotonic transformations of homogeneous functions**. They generalise homogeneity while preserving the key economic property: **MRS (slope of indifference curves) is constant along rays from the origin**. Homotheticity is an **ordinal** property — it depends only on the shape and location of level sets, not on actual function values.

> **In Simple Terms:** A homothetic function "looks like" a homogeneous function up to relabelling of contour values. Indifference curves expand radially as you move away from the origin.

### Definitions
- **Homothetic function**: `y: ℝⁿ → ℝ` is homothetic if `y = g ∘ x` where `x` is homogeneous and `g: ℝ → ℝ` is strictly increasing. ⭐ (exam-important)
- **Ordinal property**: depends only on shape/location of level sets, not on actual function values. ⭐
- **Cardinal property**: depends on the shape, location AND actual function values. ⭐
- **Monotonic transformation**: a strictly increasing function `g`. Composing with `g` preserves ranking.

### Examples (19.2)
Let `x(u, v) = uv` (homogeneous of degree 2). Then:
- `g₁(z) = z + 1` ⟹ `y₁(u, v) = uv + 1`. Homothetic (not homogeneous).
- `g₂(z) = z² + z` ⟹ `y₂(u, v) = u²v² + uv`. Homothetic (not homogeneous).
- `g₃(z) = ln z` ⟹ `y₃(u, v) = ln(uv) = ln u + ln v`. Homothetic.

### Theorem D — Level Sets are Radial Expansions
For homothetic `y`: `y(u) = y(v) ⟹ y(tu) = y(tv)` for any `t > 0`.

**Proof**: `y(tu) = g(x(tu)) = g(t^k x(u)) = g(t^k x(v)) = g(x(tv)) = y(tv)`. ✓

### Theorem E — MRS Constant Along Rays
For homothetic `y`, the **slope of level sets (MRS)** at any point on a ray from the origin is the same:
`(∂y/∂uᵢ)(tu) / (∂y/∂uⱼ)(tu) = (∂y/∂uᵢ)(u) / (∂y/∂uⱼ)(u)`

In other words, MRS for a homothetic function is **homogeneous of degree 0**.

**Proof sketch**: 
`(∂y/∂uᵢ)(tu) = (g'(x(tu))) · (∂x/∂uᵢ)(tu) = g'(t^k x(u)) · t^{k-1} · (∂x/∂uᵢ)(u)`.

The ratio `(∂y/∂uᵢ)/(∂y/∂uⱼ)` cancels `g'` and `t^{k-1}`, leaving `(∂x/∂uᵢ)/(∂x/∂uⱼ)` — independent of `t`.

### Theorem F — Ordinal Equivalence Preserves Homotheticity
If `x` is homothetic and `y` is ordinally equivalent to `x` (i.e. `y = h ∘ x` for monotone `h`), then `y` is homothetic.

> **Quick Recall:**
> - Homothetic = monotonic transform of homogeneous.
> - MRS along rays is constant for homothetic functions.
> - Property is ordinal, so survives any monotone relabelling.

### Check Your Progress 3 — Solutions
1. `f(u₁, u₂) = 3u₁²u₂⁴ + 2u₁²u₂⁴ - 3u₁³u₂³`. Compute `f(tu₁, tu₂)`:
   `= 3(tu₁)²(tu₂)⁴ + 2(tu₁)²(tu₂)⁴ - 3(tu₁)³(tu₂)³ = t⁶ f(u₁, u₂)`.
   **Homogeneous of degree 6**.
2. `f(u₁, u₂) = α ln(u₁) + β ln(u₂)`. We can write `f = ln(u₁^α u₂^β)`. Let `g(u₁, u₂) = u₁^α u₂^β` (homogeneous of degree `α + β`) and `h(z) = ln z` (strictly increasing). Then `f = h ∘ g`, so **homothetic**.

### ⚠️ Common Mistakes
- ❌ Assuming homothetic ⟹ homogeneous → ✅ One-way only. `uv + 1` is homothetic but not homogeneous.
- ❌ Trying cardinal-style argument on homothetic functions → ✅ Only ordinal properties (level set shapes) are preserved.

---

## Section: Concave Functions — Differentiable & Geometric Definitions 🔴

### Core Idea
A function is **concave** on an interval if either:
- (Geometric) the chord joining any two points on its graph lies on or below the curve, or equivalently
- (Differentiable) `f''(u) ≤ 0` for all `u` (univariate), or Hessian NSD (multivariate).

> **In Simple Terms:** Concave = "frown shape." Mixing two arguments gives at least the average of the values — diversification is preferred.

### Univariate Concavity
For `f` continuous on `X` and twice-differentiable on its interior `X°`:
`f` concave on `X°` ⟺ `f''(u) ≤ 0` for all `u ∈ X°`.

### Examples
**Example 19.3**: Is `f(u) = au² + bu` concave?
- `f'(u) = 2au + b`, `f''(u) = 2a`.
- If `a < 0`, `f''(u) < 0` ⟹ concave. If `a > 0`, convex.

### Geometric Definition (Continuous, possibly non-differentiable)
A function `f` defined on a convex set `X ⊂ ℝⁿ` is **concave** if for all `u₁, u₂ ∈ X` and `α ∈ [0, 1]`:
`(1 - α) f(a) + α f(b) ≤ f((1 - α) a + α b)`

i.e. the chord lies on or below the function.

### Construction
Let `u = (1 - α) a + α b` for `α ∈ [0, 1]`, so `u ∈ [a, b]`. Conversely, given `u ∈ [a, b]`, set `α = (u - a)/(b - a) ∈ [0, 1]`. The chord height at `u` is:
`h(u) = (1 - α) f(a) + α f(b)`

Concavity ⟺ `h(u) ≤ f(u)` for all `α ∈ [0, 1]`.

### Connections
- Builds on: Convex set definition.
- Equivalent to: Hessian-based test (Chunk 006).

---

## Section: Maximum/Minimum Conditions for Concave Functions 🔴

### Core Idea
For concave functions, **any stationary point is a maximum**. This is the powerful property that makes concavity central to economic optimisation.

> **In Simple Terms:** On a concave hill, every flat point is at the top. There's no need to check second-order conditions — concavity guarantees it.

### Theorems

**Theorem (Stationary point of concave function = max)**:
If `f` is concave on `X`, and `a ∈ X°` (interior) is a stationary point (`f'(a) = 0`), then `a` is a global maximum of `f` on `X`.

**Conditions explicit**:
- `f''(u) ≤ 0` for all `u ∈ X` AND
- `f'(a) = 0`
⟹ `u = a` is the maximum point of `f` on `X`.

The dual: convex `f` with `f'(a) = 0` ⟹ `a` is the minimum.

> **Quick Recall:**
> - Concave + stationary = global maximum.
> - Convex + stationary = global minimum.
> - **Don't need SOC** when concavity/convexity is established.

---

## Section: Concave Functions — Theorems G, H, I 🔴

### Theorem G — Tangent Inequality (Univariate)
Let `f` be differentiable on the open convex set `X ⊂ ℝ`. Then `f` is concave ⟺ for every `u₁, u ∈ X`:
`f(u) ≤ f(u₁) + f'(u₁)(u - u₁)`

**Geometric meaning**: the curve lies **below** any tangent line. (For convex, curve lies above.)

### Theorem H — Non-Increasing Derivative
Let `f` be differentiable on the open convex set `X ⊂ ℝ`. Then `f` is concave ⟺ `f'` is non-increasing.

(Equivalently: `f''(u) ≤ 0` ⟺ slope is non-increasing.)

### Theorem I — Multivariable Tangent Inequality
For `f` differentiable on the open convex set `X ⊂ ℝⁿ`. Then `f` is concave ⟺ for every `u₁, u ∈ X`:
`f(u) - f(u₁) ≤ ∇f(u₁) · (u - u₁)`

**Proof (forward)**: Concavity gives `f(u₁ + α(u - u₁)) ≥ f(u₁) + α[f(u) - f(u₁)]` for all `α ∈ [0, 1]`. Rearranging:
`[f(u₁ + α(u - u₁)) - f(u₁)] / α ≥ f(u) - f(u₁)`
Taking `α → 0⁺`: `∇f(u₁) · (u - u₁) ≥ f(u) - f(u₁)`. ✓

**Proof (reverse)**: Use the inequality at `u' = αu + (1-α)u''` with both directions; multiply and add to get concavity.

> **Quick Recall:**
> - Concave: `f(u) ≤ f(u₀) + ∇f(u₀) · (u - u₀)` (tangent above curve).
> - Convex: reverse inequality (tangent below).

---

## Section: Quasi-Concave Functions — Theorems J, K, L 🔴

### Definitions
- **Upper level set `U(f, α)`**: `{u ∈ X : f(u) ≥ α}`. ⭐
- **Lower level set `L(f, α)`**: `{u ∈ X : f(u) ≤ α}`.
- **Quasi-concave** (level-set form): all upper level sets `U(f, α)` are convex. ⭐

### Theorem J — Equivalence of Convex Upper Level Sets and Mixing Inequality
Let `f` be defined on convex `X ⊂ ℝⁿ`. Then `f` is quasi-concave ⟺
`f(αu₁ + (1 - α)u₂) ≥ min{f(u₁), f(u₂)}` for every `u₁, u₂ ∈ X`, `α ∈ [0, 1]`.

**Proof (forward, U(f, α) convex ⟹ inequality)**: Without loss `f(u₁) ≥ f(u₂) = α`. Both `u₁, u₂ ∈ U(f, α)`; convexity ⟹ `αu₁ + (1-α)u₂ ∈ U(f, α)` ⟹ `f(αu₁ + (1-α)u₂) ≥ α = min{f(u₁), f(u₂)}`.

**Proof (reverse)**: For any `α`, take `u₁, u₂ ∈ U(f, α)` (so `f ≥ α`). Inequality gives `f(convex combo) ≥ min ≥ α`, so the combo is in `U(f, α)`. Hence `U(f, α)` convex.

### Theorem K — Differentiable Quasi-Concavity (Gradient Form)
Let `f` be differentiable on open convex `X ⊂ ℝⁿ`. Then `f` is quasi-concave ⟺ for every `u₁, u₂ ∈ X`:
`f(u₂) ≥ f(u₁) ⟹ ∇f(u₁) · (u₂ - u₁) ≥ 0`

### Theorem L — Hessian Restricted to Tangent Vectors
Let `f` be twice-differentiable quasi-concave on open convex `X`. If `u₁ ∈ X`, `y ∈ ℝⁿ`, and `y' ∇f(u₁) = 0`, then `y' ∇²f(u₁) y ≤ 0`.

(Quasi-concavity restricts the Hessian's quadratic form on the tangent space `{y : ∇f · y = 0}`.)

> **Quick Recall:**
> - Quasi-concave: upper level sets convex.
> - Differentiable QC: gradient inequality (level-equal points yield non-negative directional derivative).

---

## Section: Bordered Hessian — Determinant Criterion for Quasi-Concavity 🔴

### Core Idea
Test for **quasi-concavity** of `z = f(u₁, u₂)` (and generalisations) using the **bordered Hessian determinant**:

```
       | 0      f₁(u)  f₂(u) |
D₂(u) =| f₁(u)  f₁₁    f₁₂   |
       | f₂(u)  f₂₁    f₂₂   |
```

The function `z = f(u₁, ..., uₙ)` is strictly quasi-concave at `u` if appropriate sign conditions on the bordered Hessian hold.

> **In Simple Terms:** Adding the gradient as a "border" lets us check the Hessian only on the tangent space — the relevant directions for level-set convexity.

### Conditions
- **Necessary** (for quasi-concavity): `(-1)^b D_b(u) ≥ 0` for `b = 1, ..., n`, all `u ∈ X`.
- **Sufficient** (for strict quasi-concavity): `(-1)^b D_b(u) > 0` for `b = 1, ..., n`, all `u ∈ X`.

### Definitions
- **Bordered Hessian (bth order)**: `(b+1) × (b+1)` matrix with first row `(0, f₁, ..., f_b)`, first column transposed of same, rest the `b × b` Hessian. ⭐

### Check Your Progress 4 — Worked

**Problem 1**: Test `f(u₁, u₂) = u₁ e^{-u₂}` for quasi-concavity on `u₁ ≥ 0, u₂ ≥ 0`.

Compute partials:
- `f₁ = e^{-u₂}`, `f₂ = -u₁ e^{-u₂}`.
- `f₁₁ = 0`, `f₁₂ = -e^{-u₂}`, `f₂₂ = u₁ e^{-u₂}`.

Bordered Hessian:
```
| 0           e^{-u₂}      -u₁ e^{-u₂} |
| e^{-u₂}     0            -e^{-u₂}    |
| -u₁ e^{-u₂} -e^{-u₂}     u₁ e^{-u₂}  |
```

`D₁(u₁, u₂) = -e^{-2u₂} ≤ 0` (with equality only at limits).

`D₂(u₁, u₂) = u₁ e^{-3u₂} ≥ 0`.

Both determinants vanish only when `u₁ = 0`. The test does not establish quasi-concavity at `u₁ = 0` (boundary), but **on `u₁ > 0`**: `(-1)^1 D₁ = e^{-2u₂} > 0` ✓ and `(-1)^2 D₂ = u₁ e^{-3u₂} > 0` ✓ — so `f` is **quasi-concave on `u₁ > 0, u₂ ≥ 0`**.

**Problem 2** (concavity check via Hessian): `f(u₁, u₂) = 2u₁³ - 6u₂²`.
- `f_u₁ = 6u₁²`, `f_u₂ = -12u₂`.
- `f_u₁u₁ = 12u₁`, `f_u₂u₂ = -12`, `f_u₁u₂ = 0`.
- Hessian `H(u) = [[12u₁, 0], [0, -12]]`.
- For `u₁ ≤ 0`: `12u₁ ≤ 0`, `-12 < 0`, `det = -144u₁ ≥ 0`. NSD → **concave on `u₁ ≤ 0`**.

> **Quick Recall:**
> - Bordered Hessian sign-pattern: alternating starting positive (after `(-1)^b` weighting).
> - For utility functions over goods (`u_i ≥ 0`), check signs throughout the orthant.

---

## Section: Economic Applications of Euler's Theorem 🔴

### Core Idea
**Euler's theorem**: If `f(u₁, ..., uₙ)` is homogeneous of degree `k`, then:
`u₁ · ∂f/∂u₁ + u₂ · ∂f/∂u₂ + ... + uₙ · ∂f/∂uₙ = k · f(u)`
Or in gradient form: `u · ∇f(u) = k f(u)`.

Economic implication: for a production function `q = f(u₁, ..., uₙ)` homogeneous of degree `k`, total payments to factors (each at marginal product) relate to total revenue via:

`p · q = (1/k) · Σᵢ uᵢ · pᵢ · ∂f/∂uᵢ` (when `k = 1`, total factor payments = revenue ⟹ zero profit).

> **In Simple Terms:** Euler's theorem links a homogeneous function to its first-order partials in a beautiful identity. Economically, if production is CRS, paying every factor its marginal product exactly exhausts revenue — no "residual" profit.

### Mechanisms / Processes — Returns to Scale and Profit

For production `q = f(u₁, ..., uₙ)` homogeneous of degree `k`, output price `p`:
- `pq = total revenue`.
- `uᵢ p (∂f/∂uᵢ) = total payment to factor i` (under marginal-product pricing).
- Total factor cost: `Σᵢ uᵢ p (∂f/∂uᵢ) = p · k · f(u) = k · pq`.

Cases:
- `k = 1` (CRS): total factor cost = `p q` ⟹ **zero profit**. Firm spends entire revenue on inputs.
- `k > 1` (IRS): total factor payment exceeds revenue ⟹ negative profit, "exhausts more than the product."
- `0 < k < 1` (DRS): factor payment < revenue ⟹ **positive profit** for the firm.

### Definitions
- **Euler's theorem**: `Σᵢ uᵢ (∂f/∂uᵢ) = k f(u)` for homogeneous `f` of degree `k`. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Assuming Euler's theorem holds for any function → ✅ Only homogeneous functions. Degree `k` matters.
- ❌ Concluding that CRS always means zero accounting profit → ✅ "Zero profit" here = economic profit; it assumes inputs paid at marginal product.

> **Quick Recall:**
> - Euler: `u · ∇f = k f` (homogeneous degree `k`).
> - CRS ⟹ exhaust revenue on factor payments (zero economic profit).
> - DRS ⟹ residual surplus to firm (positive profit).

### Connections
- Builds on: Homogeneous function definition (Chunk 008).
- Is prerequisite for: Cost-minimisation duality, factor demand functions (graduate microeconomics).

### Open Questions
1. How does this connect to perfect competition's zero-profit result? (CRS + competitive markets ⟹ zero economic profit.)
2. What if production is not homogeneous? (Euler's theorem doesn't apply; use envelope theorem instead.)
