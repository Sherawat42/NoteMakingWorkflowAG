# Last Minute Revision Notes

> *This document contains ONLY ultra-high-yield definitions (⭐), Quick Recall facts, Common Mistakes, and core bullet points.*


## Topics

| Unit | Title | Key Tools |
|------|-------|-----------|
| 16 | Optimisation: An Introduction | FOC, SOC, point of inflexion, Hessian principal minors |
| 17 | Unconstrained & Constrained Optimisation | Lagrange multiplier, Kuhn-Tucker |
| 18 | Advanced Topics in Optimisation — I | Convexity/concavity, quasi-convexity, NDCQ |
| 19 | Advanced Topics in Optimisation — II | Envelope theorem, homogeneity, Euler's theorem |

### Concept of Maxima and Minima — Univariate Functions 🔴

**Local (Relative) Extremum**

**Global (Absolute) Extremum**
| Aspect | Local extremum | Global extremum |
|--------|----------------|-----------------|
| Scope | Some neighbourhood `(x-ε, x+ε)` | Entire domain |
| Uniqueness | Can be many | Unique (continuous f) |
| Location | Strictly interior | Interior or endpoint |
| Test | First/second derivative locally | Compare all candidates |
- **Stationary point**: a point where `f'(x) = 0` — the tangent is parallel to the x-axis. ⭐ (exam-important)
- **Extremum**: collective term for maximum and minimum, mathematical concept without optimality connotation. ⭐
- **Extreme values / extrema**: maximum and minimum values of a function. ⭐

### Identification of Maxima and Minima 🔴

**Necessary Condition (FOC)**

**Sufficient Condition (SOC)**
- For a **maximum** at `x₀`: `f'(x₀) = 0` AND `f''(x₀) < 0`.
- For a **minimum** at `x₀`: `f'(x₀) = 0` AND `f''(x₀) > 0`.
1. Compute `f'(x)`.
2. Solve `f'(x) = 0` → candidate stationary points.
3. Compute `f''(x)`.
4. Evaluate `f''` at each candidate:
   - `f''(x₀) > 0` → minimum at `x₀`.
   - `f''(x₀) < 0` → maximum at `x₀`.
   - `f''(x₀) = 0` → inconclusive (use higher-order test).
- FOC: `12x³ - 30x² + 12x = 0` → `3x(4x - 2)(x - 2) = 0` → `x = 0, 1/2, 2`.
- SOC: `f''(x) = 36x² - 60x + 12`.
  - At `x = 0`: `f''(0) = 12 > 0` → minimum.
  - At `x = 2`: `f''(2) = 144 - 120 + 12 = 36 > 0` → minimum.
  - At `x = 1/2`: `f''(1/2) = 9 - 30 + 12 = -9 < 0` → maximum.
- `f'(x) = 1 - 1/x²` ⟹ stationary at `x = 1, -1`.
- `f''(x) = 2/x³`.
- At `x = 1`: `f''(1) = 2 > 0` → minimum, `f(1) = 2`.
- At `x = -1`: `f''(-1) = -2 < 0` → maximum, `f(-1) = -2`.

### ⚠️ Common Mistakes
- ❌ Concluding a stationary point is a maximum just because `f'(x₀) = 0` → ✅ Always verify with `f''(x₀)`.
- ❌ Assuming the local max value > local min value → ✅ As Example 16.2 shows, this need not hold across separate regions.

**Quick Recall:**
- FOC for extremum: `f'(x₀) = 0` (same for max and min).
- Max ⟺ `f'(x₀) = 0` and `f''(x₀) < 0`.
- Min ⟺ `f'(x₀) = 0` and `f''(x₀) > 0`.
---

### Point of Inflexion 🔴
- **Point of inflexion**: a point at which a curve changes its curvature. Sufficient condition: `f''(x) = 0` and `f'''(x) ≠ 0`. ⭐ (exam-important)
- A point with `f'(x) = 0`, `f''(x) = 0`, `f'''(x) ≠ 0` is called **stationary and inflexional** — it's both a stationary point and an inflexion.

**Curvature Transition**
- If a monotonic function is first **convex** then **concave**, the inflexion point yields a maximum of `f'(x)`.
- If first **concave** then **convex**, the inflexion gives a minimum of `f'(x)`.
- `f'(x) = 3x²`, `f''(x) = 6x`, `f'''(x) = 6 ≠ 0`.
- `f''(x) = 6x = 0` ⟹ `x = 0`.
- Hence the function has a point of inflexion at the origin.

**Quick Recall:**
- Inflexion: `f''(x) = 0`, `f'''(x) ≠ 0`.
- Stationary + inflexional: `f'(x) = 0`, `f''(x) = 0`, `f'''(x) ≠ 0`.

### Conclusive Criterion (Taylor Series Test) 🔴
| Case | First non-zero derivative | Sign condition | Result at `x = a` |
|------|---------------------------|----------------|-------------------|
| I | `f'(a) ≠ 0` | — | Not an extremum (FOC fails) |
| II | `f'(a) = 0`, `f''(a) ≠ 0` | `f''(a) > 0` | Local minimum |
| | | `f''(a) < 0` | Local maximum |
| III | `f'(a) = f''(a) = 0`, `f'''(a) ≠ 0` | — | Point of inflexion |
| IV | `f'(a) = f''(a) = f'''(a) = 0`, `f⁽⁴⁾(a) ≠ 0` | `f⁽⁴⁾(a) > 0` | Local minimum |
| | | `f⁽⁴⁾(a) < 0` | Local maximum |

**Generalised rule**
- a **maximum** if `n` is **even** and `f⁽ⁿ⁾(a) < 0`,
- a **minimum** if `n` is **even** and `f⁽ⁿ⁾(a) > 0`,
- an **inflexion** if `n` is **odd**.

**Quick Recall:**
- Even `n` → extremum (sign of `f⁽ⁿ⁾` decides max/min).
- Odd `n` → inflexion.
- Use this when `f''(x₀) = 0` and the standard test is inconclusive.

### Extreme Values of Multivariate Functions — FOC for Bivariate 🔴
1. Compute partial derivatives: `f₁ = ∂f/∂x₁`, `f₂ = ∂f/∂x₂`.
2. Set both to zero: `f₁ = 0` and `f₂ = 0`.
3. Solve the system simultaneously to get candidate `(x₁*, x₂*)`.
4. Test SOC using the Hessian (Chunk 002 develops this).

**Quick Recall:**
- Bivariate FOC: `f₁ = f₂ = 0`.
- n-variable FOC: `fᵢ = 0 ∀ i = 1, ..., n`. <!-- Continues in chunk 002 -->
- Builds on: Univariate FOC `f'(x) = 0` (this section).
- Is prerequisite for: SOC via Hessian principal minors (Chunk 002).
1. How does the FOC for an extremum interact with constraints? (Answered in Unit 17.)

### Sufficient Condition for Bivariate Extreme Values 🔴
- `q < 0` ⟺ `a < 0` AND `ab - h² > 0` (which forces `b < 0` too).
- `q > 0` ⟺ `a > 0` AND `ab - h² > 0` (forces `b > 0` too).
| Condition on (f₁₁, f₂₂, f₁₁f₂₂ - f₁₂²) | Result |
|----------------------------------------|--------|
| `f₁₁ < 0`, `f₂₂ < 0`, `f₁₁f₂₂ - f₁₂² > 0` | **Maximum** |
| `f₁₁ > 0`, `f₂₂ > 0`, `f₁₁f₂₂ - f₁₂² > 0` | **Minimum** |
| `f₁₁f₂₂ < f₁₂²` and `f₁₁`, `f₂₂` have **different** signs | **Saddle point** |
| `f₁₁f₂₂ < f₁₂²` and `f₁₁`, `f₂₂` have **same** sign | **Inflexion point** |
| `f₁₁f₂₂ = f₁₂²` | Inconclusive |
- **Hessian determinant** (2×2): `|H| = | f₁₁ f₁₂ ; f₂₁ f₂₂ |`. ⭐ (exam-important)
- **Saddle point**: stationary point that is a max in one direction and a min in another. ⭐
- **Young's theorem**: For functions with continuous mixed partials, `f₁₂ = f₂₁`. ⭐
- **Principal minor**: a sub-determinant of the Hessian formed by the first `i` rows and columns. ⭐
- `q > 0` ⟺ `|a| > 0` AND `|H| > 0` (both leading principal minors positive).
- `q < 0` ⟺ `|a| < 0` AND `|H| > 0` (alternating signs).

**Quick Recall:**
- Bivariate min: `f₁₁ > 0`, `|H| > 0`.
- Bivariate max: `f₁₁ < 0`, `|H| > 0`.
- Saddle: `|H| < 0`.

### Three-Variable Extrema (Principal Minors) 🔴
| Quadratic form | Principal minor pattern | Result |
|----------------|------------------------|--------|
| `q > 0` (`d²z` positive definite) | `D₁ > 0`, `D₂ > 0`, `D₃ > 0` | **Minimum** |
| `q < 0` (`d²z` negative definite) | `D₁ < 0`, `D₂ > 0`, `D₃ < 0` | **Maximum** |
- **All positive** ⟹ minimum.
- **Alternating starting with negative** ⟹ maximum.
- **D₁** = `fₓₓ` (1×1 leading minor).
- **D₂** = `|fₓₓ fₓᵧ ; fᵧₓ fᵧᵧ|` (2×2 leading minor).
- **D₃** = `|H|` (full 3×3 determinant).

### n-Variable Extrema — Hessian Determinantal Test 🔴
- FOC: all `n` first partials vanish, `f₁ = f₂ = ... = fₙ = 0`.
- SOC: examine the `n` leading principal minors `|H₁|, |H₂|, ..., |Hₙ|`.
| Condition | Maximum | Minimum |
|-----------|---------|---------|
| FOC | `dz = 0`, i.e. `f₁ = f₂ = ... = fₙ = 0` | same |
| SOC | `\|H_i\|` alternate in sign starting negative: `\|H₁\| < 0`, `\|H₂\| > 0`, `\|H₃\| < 0`, ... | All `\|H_i\| > 0` |
- **Maximum**: `(-1)^i |Hᵢ| > 0` for `i = 1, ..., n`.
- **Minimum**: `|Hᵢ| > 0` for `i = 1, ..., n`.

### ⚠️ Common Mistakes
- ❌ Checking only `|Hₙ|` (the full determinant) → ✅ All leading principal minors must be checked.
- ❌ Forgetting that for max, the **first** minor `|H₁|` must be negative (not the last) → ✅ Sign pattern starts negative for max.

**Quick Recall:**
- Min: every `\|H_i\|` is **positive**.
- Max: signs **alternate** starting with **negative**.
---

### Worked Examples — Multivariate Extrema 🔴
- `f₁ = 2x₁ - 3x₂ = 0`
- `f₂ = -3x₁ + 6x₂ + 4x₃ = 0`
- `f₃ = 4x₂ + 12x₃ = 0`
- `|H₁| = 2 > 0`
- `|H₂| = | 2 -3 ; -3 6 | = 12 - 9 = 3 > 0`
- `|H₃| = 2(72 - 16) - (-3)(-36 - 0) + 0 = 112 - 108 = 4 > 0`
- At `(0, 1, 0)`: `f₁₁ = 0`, so SOC fails — inconclusive.
- At `(1/2, 1, 1/4)`: `|H₁| = -3 < 0`, `|H₂| = 6 > 0`, `|H₃| = -18 < 0` → alternating signs → **maximum**, with value `17/16`.

**Quick Recall:**
- Always evaluate the Hessian **at** the stationary point — its sign-pattern can vary across the domain.
- If `|H₁| = 0` at a stationary point, SOC is inconclusive; need higher-order test.

**Quick Recall:**
- For each stationary point, compute the Hessian **at that point**.
- Different stationary points of the same function can have different natures.

### Unconstrained Optimisation — First Order Condition 🔴
- **Unconstrained optimisation**: maximisation/minimisation of `f(x₁, ..., xₙ)` with no equality or inequality constraint on the domain. ⭐
- **Differential FOC**: `dy = 0` for arbitrary `dx ≠ 0`.
- **Derivative FOC**: `f'(x) = 0` (univariate); `fᵢ = 0 ∀ i` (multivariate).
- FOC: `3x² - 1 = 0` ⟹ `x = ±1/√3`.
- FOC: `∂Z/∂x = -y + 2x = 0`; `∂Z/∂y = 2y - x = 0`.
- Solution: `x* = 0, y* = 0`. Optimum value `z = 0`.

**Quick Recall:**
- Necessary FOC for any extremum: all first partials vanish.
- Same FOC for max and min; SOC distinguishes.

### Second Order Condition for `z = f(x, y)` 🔴

**Sufficient SOC for `z = f(x, y)`**
| Condition | Maximum | Minimum |
|-----------|---------|---------|
| FOC | `f_x = f_y = 0` | `f_x = f_y = 0` |
| SOC | `f_xx < 0`, `f_yy < 0`, `f_xx f_yy > f_xy²` | `f_xx > 0`, `f_yy > 0`, `f_xx f_yy > f_xy²` |

**Necessary vs Sufficient**

**Saddle Point Detection**
- **Hessian** (2×2): `H = [[f_xx, f_xy]; [f_xy, f_yy]]`. ⭐ (exam-important)
- **Cross (mixed) partial**: `f_xy = ∂²f/∂x∂y`. Equals `f_yx` under continuity (Young's theorem).

### Determinantal Test (n-Variable) 🔴
|-----------|---------|---------|
| FOC | `f₁ = ... = fₙ = 0` | `f₁ = ... = fₙ = 0` |
| SOC | `(-1)^i \|H_i\| > 0` for all `i = 1,...,n` | `\|H_i\| > 0` for all `i = 1,...,n` |
- `n = 1`: SOC reduces to `f''(x*) < 0` (max) or `f''(x*) > 0` (min).
- `n = 2`: SOC reduces to `f_xx < 0` and `|H₂| = f_xx f_yy - f_xy² > 0` (max), with the dual for min.
- FOC: `f_x = 2x + y = 0`, `f_y = x + 4y = 0` ⟹ `x* = 0, y* = 0`.
- `f_xx = 2 > 0`, `f_yy = 4 > 0`, `f_xy = 1`. `f_xx f_yy = 8 > f_xy² = 1`. → **Minimum**.
- FOC: `-2x + y + 2 = 0`, `x - 2y + 1 = 0` ⟹ `x* = 5/3, y* = 4/3`.
- `f_xx = -2 < 0`, `f_yy = -2 < 0`, `f_xy = 1`. `f_xx f_yy = 4 > 1 = f_xy²`. → **Maximum**.

### ⚠️ Common Mistakes
- ❌ Confusing "SOC fails" with "no extremum" → ✅ SOC failure means inconclusive; it could still be an extremum (the sufficient condition is just sufficient).
- ❌ Forgetting `f_xy²` term — using only `f_xx f_yy > 0` → ✅ Must check `f_xx f_yy - f_xy² > 0` (the determinantal condition).

**Quick Recall:**
- `n` variables → `n` leading principal minors.
- **Min**: every minor positive.
- **Max**: signs alternate `(−, +, −, +, ...)` starting with negative.
---

### Economic Application — Multi-product Firm Under Pure Competition 🔴
- Revenue: `R = p₁q₁ + p₂q₂ = 5q₁ + 3q₂`.
- Cost: `C = 2q₁² + 2q₂² + q₁q₂`.
- Profit: `π = R - C = 5q₁ + 3q₂ - 2q₁² - 2q₂² - q₁q₂`.
1. `∂π/∂q₁ = 5 - 4q₁ - q₂ = 0`
2. `∂π/∂q₂ = 3 - 4q₂ - q₁ = 0`
- `|H₁| = -4 < 0` ✓
- `|H₂| = 16 - 1 = 15 > 0` ✓
- Alternating sign pattern → **negative definite** → maximum.

**Quick Recall:**
- Multi-product competitive firm: profit = (linear revenue) - (quadratic cost).
- Constant negative-definite Hessian ⟹ strict concavity ⟹ unique global max.

### Economic Application — Multi-product Monopoly 🔴
- `q₁ = 40 - 2p₁ + p₂`
- `q₂ = 15 + p₁ - p₂` (substitutes — see how a rise in `p₂` raises `q₁`).
- `p₁ = 55 - q₁ - q₂` (= AR₁)
- `p₂ = 70 - q₁ - 2q₂` (= AR₂)
- `π₁ = 55 - 3q₂ - 4q₁ = 0` ⟹ `4q₁ + 3q₂ = 55`
- `π₂ = 70 - 3q₁ - 6q₂ = 0` ⟹ `3q₁ + 6q₂ = 70`

### ⚠️ Common Mistakes
- ❌ Treating the demand cross-effect (between `p₁` and `q₂`) as zero in profit derivatives → ✅ The cost cross-term `q₁q₂` and the revenue cross-term both contribute.
- ❌ Concluding "local max" without checking signs of leading minors at the stationary point → ✅ Always test the Hessian.

**Quick Recall:**
- Substitute goods: cross-price coefficient in demand is **positive**.
- Inverse demand via Cramer's rule.
- If Hessian's principal-minor signs are independent of where evaluated, optimum is global.
---

### Constrained Optimisation — Setup 🔴
- **Objective function**: dependent variable to maximise/minimise.
- **Choice (decision/policy) variables**: independent variables we control.
- **Optimisation**: collective term for max and min ("the quest for the best").
- **Extremum** (in the math sense): max or min, no optimality connotation.
- **Constraint optimisation**: choosing values of decision variables that yield the desired extremum of the objective function while respecting constraints. ⭐
- **Choice / decision / policy variables**: the independent variables whose values the agent picks. ⭐ <!-- Continues in chunk 004 -->
- Builds on: Unconstrained SOC framework (this chunk).
- Is prerequisite for: Lagrange theorem and Kuhn-Tucker theory (Chunk 004).
1. How exactly does the budget constraint enter the FOC? (Lagrangian — Chunk 004.)
2. What if the constraint is an inequality? (Kuhn-Tucker — Chunk 004.)

### Equality Constrained Optimisation — No-Arbitrage Principle 🔴
- **Lagrangian function**: `L(x, λ) = f(x) + λ[c - g(x)]`. ⭐ (exam-important)
- **Lagrange multiplier λ***: shadow price of the constraint — the rate at which the optimum value of the objective changes when the constraint is relaxed by one unit. ⭐
- **Constraint qualification (CQ)**: the constraint gradient(s) are linearly independent at the optimum. ⭐

**Quick Recall:**
- Equal-MU-per-rupee rule: `∂f/∂xᵢ ÷ ∂g/∂xᵢ` is the same constant `λ*` across all `i`.
- λ* = derivative of optimal objective with respect to the constraint constant.

### Theorem of Lagrange 🔴
- **Theorem of Lagrange** (necessary condition): given continuous differentiability of `f` and `gⁱ`, at any local extremum of `f` on the constraint set there exist multipliers (not all zero) satisfying the gradient equation above. ⭐
- **Rank-`k` Jacobian condition** ⟺ CQ. If CQ holds, `μ ≠ 0`, so we can divide through and set `μ = 1`. ⭐
1. Write `L(x, λ) = f(x) + Σᵢ λᵢ gⁱ(x)`.
2. FOCs: `n + k` equations:
   - `∂L/∂xⱼ = ∂f/∂xⱼ + Σᵢ λᵢ ∂gⁱ/∂xⱼ = 0` for `j = 1, ..., n`.
   - `∂L/∂λᵢ = gⁱ(x) = 0` for `i = 1, ..., k`.
3. Solve simultaneously for `(x*, λ*)`.
4. Verify SOC via bordered Hessian on the tangent space.
- Lagrangian: `L = x²y + λ[200 - 2x - y]`.
- FOC: `2xy = 2λ`, `x² = λ`, `2x + y = 200`.
- Substitute `λ = x²` into `2xy = 2λ`: `xy = x²` ⟹ `y = x`. Then `2x + x = 3x = 200` (after error correction matches source). Source gives `x* = 200/3, y* = 200/3, λ* = (200/3)²`. (Source actually gets `x = y = 200/3` reflecting the calculation `2x + y = 200` paired with the FOC ratio).

**Quick Recall:**
- For each equality constraint, introduce one Lagrange multiplier.
- Stationary points of `L` correspond to candidate constrained extrema.
- Always check CQ (Jacobian of constraint gradients has full rank).

### Second Order Condition for Constrained Optimisation 🔴
- **Bordered Hessian**: matrix of second derivatives of `L` with respect to `x` and `λ` (constraint gradients form the "border"). ⭐
- **Null space `N(Dg(x*))`**: set of all `dx ∈ ℝⁿ` orthogonal to every constraint gradient.
| Outcome | Necessary | Sufficient |
|---------|-----------|------------|
| Local max | `x' D²L(x*, λ*) x ≤ 0` for all `x ∈ N(Dg(x*))` | `x' D²L(x*, λ*) x < 0` for all `x ∈ N(Dg(x*))`, `x ≠ 0` |
| Local min | `x' D²L(x*, λ*) x ≥ 0` for all `x ∈ N(Dg(x*))` | `x' D²L(x*, λ*) x > 0` for all `x ∈ N(Dg(x*))`, `x ≠ 0` |

**Quick Recall:**
- Constrained SOC = quadratic form on tangent space of constraints.
- Use bordered Hessian; sign pattern depends on whether maximisation or minimisation.

### Inequality Constrained Optimisation — Setup 🔴
- **Binding (tight, effective) constraint**: `gⁱ(x*) = 0`. ⭐
- **Slack (non-binding) constraint**: `gⁱ(x*) > 0`. ⭐

### Kuhn-Tucker Theorem 🔴
- If `gⁱ(x*) > 0` (slack), then `λᵢ = 0`.
- If `rank(Dg_β(x*)) = ℓ` (where `g_β` is the vector of binding constraints) — the **constraint qualification** — we may take `μ = 1`.
- `λᵢ ≥ 0` for all `i`, and `λᵢ > 0` for some `i` ⟹ `gⁱ(x*) = 0`.
- (FOC) `Df(x*) + Σᵢ λᵢ Dgⁱ(x*) = 0` ... (17.10)
- (Complementary slackness) `λᵢ gⁱ(x*) = 0`, `λᵢ ≥ 0`, `gⁱ(x*) ≥ 0` for all `i` ... (17.9)
- **Complementary slackness**: `λᵢ · gⁱ(x*) = 0` for each `i` — at most one of `λᵢ` and `gⁱ` is non-zero. ⭐ (exam-important)
- **Kuhn-Tucker conditions**: equations (17.9) + (17.10) (or 17.10a). ⭐

### ⚠️ Common Mistakes
- ❌ Forgetting that KT conditions are **necessary, not sufficient** → ✅ Points satisfying KT may not be local optima; checking via comparison or concavity is needed.
- ❌ Treating an inequality with `≤` as `≥` directly → ✅ Multiply by `-1` to convert: `h(x) ≤ c` ⟺ `c - h(x) ≥ 0`.
- ❌ Setting `λᵢ = 0` when `gⁱ` is binding → ✅ Slack constraint forces `λᵢ = 0`; binding constraint allows `λᵢ ≥ 0`.

**Quick Recall:**
- KT condition trio: stationarity, primal feasibility (`gⁱ ≥ 0`), dual feasibility (`λᵢ ≥ 0`), complementary slackness (`λᵢ gⁱ = 0`).
- Unlike Lagrange, KT does **not** require checking SOC (no second-order condition required by the theorem).
---

**Quick Recall:**
- Concave + convex domain ⟹ local max = global max.
- Convex set of maximisers ⟹ if there are multiple optima, every weighted average is also optimal.

### KT Application — Linear Utility Maximisation (Example 17.9) 🔴
1. **Case 1** (interior): `x₁, x₂ > 0`, budget binds.
2. **Case 2**: `x₁ = 0`, `x₂ > 0`, budget binds.
3. **Case 3**: `x₂ = 0`, `x₁ > 0`, budget binds.
- `λ₁ = λ₂ = 0` (slackness).
- FOCs: `1 + 0 - λ₃ p₁ = 0`, `1 + 0 - λ₃ p₂ = 0` ⟹ `λ₃ p₁ = λ₃ p₂ = 1`.
- Since `λ₃ > 0` (positive marginal utility of income), `p₁ = p₂`.
- Conclusion: interior solution exists **only when prices are equal**. Any `(x₁, x₂)` exhausting the budget is optimal. `U₁/p₁ = U₂/p₂ = 1/p`.
- `x₁ = 0` ⟹ from budget, `x₂ = I/p₂ > 0`. So `λ₂ = 0`.
- FOC for `x₂`: `λ₃ p₂ = 1`, so `λ₃* = 1/p₂`.
- FOC for `x₁`: `1 + λ₁ - λ₃ p₁ = 0` ⟹ `λ₁* = (p₁/p₂) - 1`.
- For `λ₁* > 0` we need `p₁ > p₂` — i.e. **good 1 is more expensive**, so consumer chooses only good 2.
| Price relation | Active case | Solution |
|----------------|-------------|----------|
| `p₁ = p₂` | Case 1 | Any budget-exhausting `(x₁, x₂)` |
| `p₁ > p₂` | Case 2 | `(0, I/p₂)` — buy only good 2 |
| `p₁ < p₂` | Case 3 | `(I/p₁, 0)` — buy only good 1 |

**Quick Recall:**
- With perfect-substitute utility, the consumer spends entire budget on the **cheaper** good.
- At an interior solution requires **equal** prices.
- Builds on: Lagrange theorem (this chunk).
- Contrasts with: Cobb-Douglas utility (interior solutions for any positive prices) — see later examples in chunks 005, 010.
- Is prerequisite for: Convexity-based sufficient conditions (Chunk 005-006).
1. What if utility is Cobb-Douglas? (Chunk 010 — Example "100 - 2x - 3y" KT.)
2. How does the multiplier λ* relate to comparative statics? (Envelope theorem, Chunk 008.)

### KT Application — Quasi-Linear Utility (Example 17.10) 🔴
- `1/(1+x₁)² + λ₁ - λ₃ p₁ = 0` (eq. 17.19)
- `1/(1+x₂)² + λ₂ - λ₃ p₂ = 0` (eq. 17.20)
- Slackness on each constraint: `λᵢ xᵢ = 0`, `λ₃(I - p₁x₁ - p₂x₂) = 0`.
- `λ₁ = λ₂ = 0` (slackness).
- `1/(1+x₁)² = λ₃ p₁`, `1/(1+x₂)² = λ₃ p₂`.
- Dividing: `(1+x₂)²/(1+x₁)² = p₁/p₂`.
- Combined with budget `p₁x₁ + p₂x₂ = I`:
  - `x₁* = [I + p₂ - (p₁p₂)^(1/2)] / [p₁ + (p₁p₂)^(1/2)]`
  - `x₂* = [I + p₁ - (p₁p₂)^(1/2)] / [p₂ + (p₁p₂)^(1/2)]`
- Required for Case 1: `I > (p₁p₂)^(1/2) - p₁` AND `I > (p₁p₂)^(1/2) - p₂`.
- `x₂ = I/p₂` (from budget). For positivity, `λ₂ = 0`.
- `λ₃ = 1/[p₂(1+x₂)²] = 1/[p₂(p₂+I)²/p₂²] = p₂/(p₂+I)²`.
- `λ₁ = λ₃ p₁ - 1`. For `λ₁ ≥ 0` need `λ₃ p₁ ≥ 1` ⟹ `I < (p₁p₂)^(1/2) - p₂`.
- `x₁ = I/p₁`. Similar conditions; this case applies if `I < (p₁p₂)^(1/2) - p₁`.
| Condition | Active case | Outcome |
|-----------|-------------|---------|
| `p₁ = p₂ = p` | Case 1 | `x₁* = x₂* = I/(2p)` |
| `p₁ < p₂` and `I > (p₁p₂)^(1/2) - p₁` | Case 1 | Both consumed (interior) |
| `p₁ < p₂` and `I < (p₁p₂)^(1/2) - p₁` | Case 3 | Only `x₁` consumed |
| `p₁ > p₂` | (symmetric) | Either Case 1 or Case 2 |

**Quick Recall:**
- With saturating (concave) utility, low income or extreme price ratio ⟹ corner solution.
- At interior, marginal utility ratio = price ratio: `(1+x₂)²/(1+x₁)² = p₁/p₂`.
- Builds on: Linear utility KT (Chunk 004).
- Contrasts with: Cobb-Douglas (always interior) — see exercises in Chunk 005, 010.

**Quick Recall:**
- Lagrange's central trick: introduce λ for each equality constraint and treat the augmented function as unconstrained.
- **Tangency condition** (geometric): MRS = price ratio at the optimum.

### Convex and Concave Functions — Definitions 🔴
- **Convex function**: For `S ⊂ ℝⁿ` convex and `f: S → ℝ`, `f` is convex if for all `u, v ∈ S` and `θ ∈ [0,1]`:
- `f(θu + (1-θ)v) ≤ θ f(u) + (1-θ) f(v)`. ⭐
- **Strictly convex**: strict inequality for `u ≠ v`, `θ ∈ (0,1)`. ⭐
- **Concave function**: same definition with inequality reversed:
- `f(θu + (1-θ)v) ≥ θ f(u) + (1-θ) f(v)`. ⭐
- **Strictly concave**: strict inequality version.
- **Affine**: a function that is both convex and concave (linear plus constant).

**Geometric Interpretation**
- For convex `f`: graph value at `θu + (1-θ)v` is **at most** the chord height `θf(u) + (1-θ)f(v)`.
- For concave `f`: graph value is **at least** the chord height.

**Chord & Tangent Inequalities (Differentiable Convex)**
- Slope of tangent at `u` ≤ slope of chord PR ≤ slope of chord PQ.
- Hence `f'(u) ≤ [f(v) - f(u)] / (v - u) ≤ f'(v)`.

**Sum and Scaling Properties**
- Sum of convex functions is convex.
- Positive scalar times convex function is convex.
- Concave is the mirror.
1. `f(u) = au + b` (affine, with any `a, b ∈ ℝ`).
2. `f(u) = u^p` for `p ≥ 1` (powers).
3. `f(u) = |u|^p` for `p ≥ 1` on ℝ.
4. `f(u) = e^(au)` for any `a ∈ ℝ`.
5. Every linear transformation `ℝⁿ → ℝ`.
6. `f(u₁, u₂) = 2u₁² + u₂² - 2u₁u₂`.
1. `f(u) = -u²`.
2. `f(u) = √u` (on ℝ₊).
3. Affine `f(u) = au + b`.
4. `f(u) = sin(u)` on `[0, π]`.
1. Conic combination: `f(u) = Σ cⱼ fⱼ(u)` with `cⱼ ≥ 0`, each `fⱼ` convex ⟹ `f` convex.
2. Pointwise max: `f(u) = max{f₁(u), ..., fₖ(u)}` with each `fⱼ` convex ⟹ `f` convex.
3. Quotient: if `g: ℝⁿ → ℝ` is concave, `g > 0`, then `f(x) = 1/g(x)` is convex on `{x : g(x) > 0}`.
4. Composition with non-decreasing convex `g: ℝ → ℝ` and convex `h: ℝⁿ → ℝ` ⟹ `f = g ∘ h` is convex.
5. Pre-composition with affine: convex `g`, affine `A(u) = Au + b` ⟹ `g ∘ A` is convex.

**Quick Recall:**
- Convex: chord above graph; `f(θu + (1-θ)v) ≤ θf(u) + (1-θ)f(v)`.
- Concave: chord below graph; reverse inequality.
- Affine = convex AND concave.

### ⚠️ Common Mistakes
- ❌ Confusing convex set with convex function — they're different concepts (a function's epigraph is a convex set iff the function is convex).
- ❌ Sum/max of concave is **not always** concave (max of concave is not concave; min is). The sum of concaves is concave.
- Builds on: Definition of convex set (assumed).
- Is prerequisite for: Hessian-based test (Chunk 006), quasi-convexity (Chunk 006).

### Differentiable Convex/Concave — Second-Derivative Test (Two Variables) 🔴
| Property | Conditions throughout domain |
|----------|------------------------------|
| Concave | `f_uu ≤ 0`, `f_vv ≤ 0`, `f_uu f_vv - f_uv² ≥ 0` |
| Convex | `f_uu ≥ 0`, `f_vv ≥ 0`, `f_uu f_vv - f_uv² ≥ 0` |
| Strictly concave | `f_uu < 0`, `f_uu f_vv - f_uv² > 0` |
| Strictly convex | `f_uu > 0`, `f_uu f_vv - f_uv² > 0` |

**Quick Recall:**
- Concavity = SOC for max **everywhere**, not only at a stationary point.
- Convexity = SOC for min **everywhere**.

### Hessian Test for Convexity (n Variables) 🔴
- `f` convex on `S` ⟺ Hessian `H(u)` is PSD ∀ `u ∈ S` (`x' H(u) x ≥ 0` for all `x ∈ ℝⁿ`).
- `f` concave on `S` ⟺ Hessian `H(u)` is NSD ∀ `u ∈ S` (`x' H(u) x ≤ 0`).
- `f` concave ⟺ `(-1)^k D_k(u) ≥ 0` for `k = 1, ..., n`, ∀ `u ∈ S`.
- `f` convex ⟺ `D_k(u) ≥ 0` for `k = 1, ..., n`, ∀ `u ∈ S`.
- **Positive semidefinite (PSD)**: `x' H x ≥ 0` for all `x ∈ ℝⁿ`. ⭐
- **Negative semidefinite (NSD)**: `x' H x ≤ 0` for all `x ∈ ℝⁿ`. ⭐
- **Hessian matrix**: `H = [∂²f/∂uᵢ∂uⱼ]ᵢⱼ` (symmetric for C² functions). ⭐

**Quick Recall:**
- Convex ⟺ PSD; Concave ⟺ NSD.
- n-variable test: leading principal minor signs (≥ 0 for convex; alternating for concave).

### Quasi-Convex and Quasi-Concave Functions 🔴
- **Quasi-convex**: `f(θu + (1-θ)v) ≤ max{f(u), f(v)}` for all `u, v ∈ S`, `θ ∈ [0, 1]`. ⭐
- **Strictly quasi-convex**: strict inequality for `u ≠ v`, `θ ∈ (0, 1)`.
- **Quasi-concave**: `-f` quasi-convex, equivalently `f(θu + (1-θ)v) ≥ min{f(u), f(v)}`. ⭐
- **Strictly quasi-concave**: strict inequality version.
- **Quasi-linear**: both quasi-convex and quasi-concave.

**Examples**
- `|u|` is quasi-convex on ℝ.
- `log u` is quasi-convex (and concave) on ℝ₊.

**Differentiable Quasi-Convexity Condition**
- If `f(u) ≤ f(v)`, then `∇f(v)·(u - v) ≤ 0`, OR equivalently
- If `∇f(v)·(u - v) > 0`, then `f(u) > f(v)`.

**Worked Illustration**
- Suppose `f(u₁) ≤ f(u₂)`, i.e. `u₁³ ≤ u₂³`, i.e. `u₁ ≤ u₂`.
- Compute `∇f(u₂)(u₁ - u₂) = 3u₂²(u₁ - u₂) ≤ 0` (since `u₁ ≤ u₂` and `3u₂² ≥ 0`).
- Theorem condition holds → `f` is quasi-convex.

**Counter-example (Sum of Quasi-Convex Need Not Be Quasi-Convex)**
- A function that is both quasi-convex and quasi-concave is **quasi-linear**.
- Every convex function is quasi-convex.
- A concave function can be quasi-convex (e.g. `log` is concave AND quasi-convex).
- Sum of quasi-convex functions is **not necessarily** quasi-convex (above).
- Product of two positive convex decreasing functions is quasi-convex.
- Strictly convex ⟹ strongly quasi-convex.
- Strongly quasi-convex ⟹ strictly quasi-convex ⟹ quasi-convex.

### ⚠️ Common Mistakes
- ❌ Assuming "concave" means "quasi-concave" reverses (every concave function is quasi-concave, but not vice versa) → ✅ Quasi-concavity is **weaker**.
- ❌ Sum-preserves-quasi-convexity → ✅ Sum can fail (counter-example above). Sum **does** preserve convexity.
1. (a) `f(u₁, u₂) = 2u₁³ - 6u₂²`: For `u₁ < 0`, `u₂ > 0`: `f_u₁u₁ = 12u₁ < 0`, `f_u₂u₂ = -12 < 0`, `|H| = -144u₁ ≥ 0`. NSD → **concave** for `u₁ ≤ 0`.
2. Quasi-concavity is **weaker** than concavity. Every concave function is quasi-concave, but not vice versa.

**Quick Recall:**
- Quasi-convex: level sets `{u : f(u) ≤ α}` convex. <!-- Continues in chunk 009 -->
- Quasi-concave: level sets `{u : f(u) ≥ α}` (upper level sets) convex.
- Convex ⟹ quasi-convex (one-way only).

### Constrained Optimisation — NDCQ 🔴
- Minimise (or maximise) `f(u)`
- Subject to `gⱼ(u) ≤ 0`, `j = 1, ..., m`; `hₗ(u) = 0`, `ℓ = 1, ..., r`.
- `f, g, h: ℝⁿ → ℝ`.
- Feasible set: `Ω = {u ∈ ℝⁿ : hₗ(u) = 0, gⱼ(u) ≤ 0}`.
- **Feasible solution**: a point satisfying all constraints. ⭐
- **Feasible region (Ω)**: collection of all feasible solutions.
- **Optimal solution**: feasible point with maximal/minimal `f`.
- **NDCQ**: Jacobian of binding-constraint gradients `Dh(u*)` (or `Dg_β(u*)`) has full rank `m`. ⭐ (exam-important)
- Tangency: `∇f(u*) = λ ∇h(u*)`.
- Lagrangian `L(u, λ) = f(u) - λ[h(u) - c]`.
- FOCs: `∇L = 0` (which yields both `∇f = λ ∇h` and `h(u) = c`).
- Jacobian matrix `Dh(u*) = [∇h₁(u*); ...; ∇hₘ(u*)]ᵐˣⁿ`.
- NDCQ: `rank(Dh(u*)) = m`.
- If any `∇hⱼ(u*) = 0`, that constraint drops out — Lagrangian fails.
- Lagrangian: `L(u, λ) = f(u) - Σⱼ λⱼ [hⱼ(u) - cⱼ]`.
- FOCs: `∂L/∂uᵢ = 0` for all `i`; `∂L/∂λⱼ = 0` for all `j` (recovers original constraints).
- Lagrangian: `L = 3 + u₁u₂ - λ(u₁² + u₂² - 1)`.
- FOCs: `u₂ - 2λu₁ = 0`, `u₁ - 2λu₂ = 0`, `u₁² + u₂² = 1`.
- Solutions: `u₁ = ±1/√2`, `u₂ = ±1/√2`, with `u₁, u₂` same sign for max → `(1/√2, 1/√2)` or `(-1/√2, -1/√2)`. Maximum value `3 + 1/2 = 7/2`.

**Quick Recall:**
- NDCQ = Jacobian of constraint gradients has rank `m`.
- If NDCQ fails at a candidate, that point must be checked separately.

### Inequality Constraints — Binding/Non-Binding Analysis 🔴
- `∇f(u*) = λ ∇g(u*)`, `λ ≥ 0`.
- The unconstrained max lies outside the feasible region; the constraint pushes us back.
- Standard unconstrained FOC: `∇f(u*) = 0`.
- Equivalent to constrained form with `λ = 0`.
- `∂L/∂uᵢ = ∂f/∂uᵢ - λ ∂g/∂uᵢ = 0` for all `i`.
- `λ[g(u) - b] = 0` (**complementary slackness**).
- `g(u) - b ≤ 0` (primal feasibility).
- `λ ≥ 0` (dual feasibility).
- `∂f/∂uᵢ - Σⱼ λⱼ ∂gⱼ/∂uᵢ = 0` for all `i`.
- `λⱼ [gⱼ(u) - bⱼ] = 0` for all `j`.
- `gⱼ(u) ≤ bⱼ`, `λⱼ ≥ 0`.
- **Complementary slackness (CS)**: `λⱼ · [gⱼ(u) - bⱼ] = 0` for each `j`. ⭐
- **Binding constraint** at `u*`: `gⱼ(u*) = bⱼ`. ⭐
- **Non-binding (slack) constraint**: `gⱼ(u*) < bⱼ`. Forces `λⱼ = 0`.

**Quick Recall:**
- Always check primal (`g ≤ b`), dual (`λ ≥ 0`), and slackness simultaneously.
- Slackness is the key new condition compared to equality-Lagrange.

**Quick Recall:**
- At LP optimum: positive dual variable ⟹ corresponding primal constraint binds.
- This is the LP analogue of `λ_j g_j = 0` in nonlinear KT. <!-- See chunk 007 for proof -->

**Quick Recall:**
- Weak duality: primal cost ≤ dual cost (for max primal).
- Strong duality: at optimum, primal = dual cost.
- Slackness: equality forces the right "binding" pattern.

### Mixed Constraints — General Theorem 🔴
- `∂L/∂uⱼ = 0` for all `j ∈ {1, ..., n}`.
- `λᵢ [gᵢ(u*) - bᵢ] = 0` for all `i ∈ {1, ..., k}` (slackness).
- `hᵢ(u*) = cᵢ` for all `i ∈ {1, ..., m}` (equality).
- `gᵢ(u*) ≤ bᵢ` for all inequality `i` (primal feasibility).
- `λᵢ ≥ 0` for all inequality `i` (dual feasibility).
- **Mixed-constraint Lagrangian**: `L = f(u) - Σ λⱼ [gⱼ - bⱼ] - Σ νᵢ [hᵢ - cᵢ]`. ⭐
- **Active set**: the indices of binding constraints at `u*`. ⭐

**Quick Recall:**
- Equality multipliers `νᵢ` can be of any sign.
- Inequality multipliers `λⱼ ≥ 0`.
- Slackness on inequalities only.

### Kuhn-Tucker Lagrangian (with Non-Negativity) 🔴
- `∂L̄/∂xⱼ ≤ 0` and `xⱼ · ∂L̄/∂xⱼ = 0` for all `j` (subsumes non-negativity slackness).
- `∂L̄/∂λⱼ ≥ 0` and `λⱼ · ∂L̄/∂λⱼ = 0` for all `j`.
- `λⱼ ≥ 0` for all `j`.
- The non-negativity `uⱼ ≥ 0` is captured by the **inequality direction** of `∂L̄/∂xⱼ ≤ 0` rather than a separate slackness equation.
- The `νⱼ uⱼ = 0` slackness is replaced by `xⱼ · ∂L̄/∂xⱼ = 0` directly.

**Quick Recall:**
- Use KT Lagrangian when many non-negativity constraints — saves bookkeeping.
- Three types of FOCs: stationarity (≤0 with slackness on `xⱼ`), constraint slackness (≥0 on `λⱼ`), and `λ ≥ 0`.

### KT with Equality Constraint — Worked (Check Your Progress 3) 🔴
- `∂L/∂u₁ = u₂ - λ = 0` ⟹ `λ = u₂`.
- `∂L/∂u₂ = u₁ - 4λ = 0` ⟹ `u₁ = 4λ = 4u₂`.
- `∂L/∂λ = 16 - u₁ - 4u₂ = 0`.

### KT Application — Inequality + Box Constraints (Q1, Section 18.9) 🔴
- `g₁(u) = u₁² + u₂² - 4 ≤ 0`
- `g₂(u) = -u₁ + u₂ ≤ 0`
- `g₃(u) = -u₁ ≤ 0` (i.e. `u₁ ≥ 0`)
- `g₄(u) = -u₂ ≤ 0` (i.e. `u₂ ≥ 0`)
- `u₁² + u₂² ≤ 4`, `-u₁ + u₂ ≤ 0`, `u₁ ≥ 0`, `u₂ ≥ 0`.
- Stationarity: `2u₁ λ₁ - 2u₂ λ₂ - λ₃ = 0`, `2u₂ λ₁ + λ₂ - λ₄ = 1` (the "1" from `∂f/∂u₂ = 1`).
- Slackness: `λᵢ gᵢ = 0` for `i = 1, ..., 4`.
- Non-negativity: `λᵢ ≥ 0`.

### ⚠️ Common Mistakes
- ❌ Concluding KT-satisfying point is automatically a max → ✅ Either verify SOC (bordered Hessian) or rely on concavity of `f` and convexity of constraint set.
- ❌ Skipping NDCQ check at corner solutions → ✅ Box constraints can violate NDCQ at corners; always verify Jacobian rank.

**Quick Recall:**
- KT yields candidate set; comparing objective values at all candidates picks the optimum.
- Multiple candidates can satisfy KT — only one (or some) are actual maxima.
- Builds on: KT theorem (Chunk 004), complementary slackness (Chunk 006).
- Is prerequisite for: Envelope theorem (Chunk 008) and quasi-concave optimisation theory (Chunk 009).
1. How does the multiplier `λ*` change with parameter `b`? (Envelope theorem — Chunk 008.)
2. When do KT conditions become sufficient? (When `f` concave, constraint set convex.)
- (A) `L_u₁ = -2(u₁ - 5) - 2λu₁ ≤ 0`
- (B) `L_u₂ = -2(u₂ - 5) - 2λu₂ ≤ 0` (source has `-2(u₂-5) - λ` — typo; consistent reading is `-2λu₂`)
- (C) `L_λ = 9 - u₁² - u₂² ≥ 0`
- (D) `u₁, u₂, λ ≥ 0`
- Slackness: `u₁ L_u₁ = 0`, `u₂ L_u₂ = 0`, `λ L_λ = 0`.

### Lagrange Multiplier Method — Equality Constraints (Restated) 🔴
- Lagrangian: `F(u, λ) = f(u) - Σᵢ λᵢ Gᵢ(u)`.
- FOCs: `∂F/∂uⱼ = ∂f/∂uⱼ - Σᵢ λᵢ ∂Gᵢ/∂uⱼ = 0` for `j = 1, ..., n`.
- Constraint equations: `Gᵢ(u) = 0` for `i = 1, ..., k`.

**Quick Recall:**
- Total: `n + k` equations in `n + k` unknowns `(u₁, ..., uₙ, λ₁, ..., λₖ)`.

**Quick Recall:**
- Lagrange multipliers exist provided NDCQ (Jacobian full rank).
- The "magic" of multipliers: they encode the implicit dependence of constrained variables.

### Extension to Inequality Constraints 🔴
- `∇f(u*) - Σᵢ λᵢ ∇Gᵢ(u*) - Σⱼ μⱼ ∇Hⱼ(u*) = 0`
- `μⱼ Hⱼ = 0` for `j = 1, ..., m` (slackness)
- `μⱼ ≤ 0`, `Hⱼ(u*) ≤ 0`

**Quick Recall:**
- Active vs inactive: depends on whether `H` binds at `u*`.
- Inactive constraints are dropped from the Lagrangian.
- `L = u₁u₂ + λ(100 - u₁ - u₂)`.
- FOCs: `u₂ = λ`, `u₁ = λ` ⟹ `u₁ = u₂`. Constraint: `u₁ + u₂ = 100` ⟹ `u₁ = u₂ = 50`.
- Maximum: `u₃* = 2500`.
- Lagrangian: `L = 4u₁² + 3u₁u₂ + 6u₂² + λ(56 - u₁ - u₂)`.
- FOCs: `8u₁ + 3u₂ = λ`, `3u₁ + 12u₂ = λ`, `u₁ + u₂ = 56`.
- Equate first two: `8u₁ + 3u₂ = 3u₁ + 12u₂` ⟹ `5u₁ = 9u₂` ⟹ `u₁ = 1.8 u₂`.
- Constraint: `1.8u₂ + u₂ = 56` ⟹ `u₂ = 20`. Then `u₁ = 36`. `λ = 8(36) + 3(20) = 348`.

**Quick Recall:**
- For utility-style maximisation problems, the multiplier λ has units of "extra utility per unit of relaxed constraint" — its **shadow price** interpretation.

### Envelope Theorem — Concept 🔴
- **Value function `V(a)`**: optimal value of `f(u, a)` for parameter `a`, i.e. `V(a) = f(u*(a), a)`. ⭐
- **Envelope theorem**: `dV/da = ∂L/∂a` evaluated at the optimum (constrained); or `dV/da = ∂f/∂a` (unconstrained). ⭐ (exam-important)

**Quick Recall:**
- Envelope identity: `∂V/∂a = ∂L/∂a` at the optimum.
- Indirect effects vanish because of FOCs.

### Envelope Theorem for Unconstrained Optimisation 🔴
- FOCs: `4 - 2u₁ + u₂ = 0`, `a - 2u₂ + u₁ = 0`.
- Solving: `u₁* = (8 + a)/3`, `u₂* = (2a + 4)/3`.
- Value function: `V(a) = 4 · (8+a)/3 + a · (2a+4)/3 - [(8+a)/3]² - [(2a+4)/3]² + (8+a)(2a+4)/9`.
- By envelope: `dV/da = ∂f/∂a |_{(u*, u*)} = u₂* = (2a + 4)/3`. (Faster than expanding `V(a)`.)

**Quick Recall:**
- Skip the algebra of substituting and re-differentiating; use envelope to read off `dV/da = ∂f/∂a`.

### Envelope Theorem for Constrained Optimisation 🔴
- First two brackets are zero by FOCs.
- `dγ/da · g(...)` is zero because `g = 0`.
- Remaining: `∂f/∂a + γ* ∂g/∂a = ∂L/∂a`. ✓

**Quick Recall:**
- For constrained problems, use Lagrangian's `∂L/∂a`, not `∂f/∂a` alone.
- Builds on: Lagrangian theorem (Chunk 004), value function concept (this section).
- Is prerequisite for: Comparative statics in microeconomics; Hotelling's lemma; Roy's identity (graduate microeconomics, beyond this block).

### Homogeneous Functions — Definition & Economic Applications 🔴
- **Homogeneous of degree `k`**: `f(tu) = t^k f(u)` for all `t > 0`. ⭐ (exam-important)

**Returns to Scale**
- Homogeneous of degree `k = 1` ⟺ **Constant Returns to Scale (CRS)**. Doubling inputs ⟹ doubling output.
- `k > 1` ⟺ **Increasing Returns to Scale (IRS)**. Doubling inputs ⟹ more than doubling output.
- `0 < k < 1` ⟺ **Decreasing Returns to Scale (DRS)**. Doubling inputs ⟹ less than doubling output.

**Cobb-Douglas Utility/Production**

**CES (Constant Elasticity of Substitution)**

**Demand Functions Homogeneous of Degree 0**

**Quick Recall:**
- CRS ⟺ degree 1 production function.
- Demand functions are degree 0 in `(p, I)` — money illusion-free.

### Properties of Homogeneous Functions (Theorems A, B, C) 🔴
- Builds on: Chain rule, parameterised optimisation.
- Is prerequisite for: Homothetic functions (Chunk 009), Euler's theorem (Chunk 009).
1. What's the relationship between homogeneity and concavity? (Independent — neither implies the other.)
2. How does homogeneity of degree 1 relate to the cost-minimising firm? (CRS ⟺ marginal cost = average cost.)

### Homothetic Functions — Definition & Properties 🔴
- **Homothetic function**: `y: ℝⁿ → ℝ` is homothetic if `y = g ∘ x` where `x` is homogeneous and `g: ℝ → ℝ` is strictly increasing. ⭐ (exam-important)
- **Ordinal property**: depends only on shape/location of level sets, not on actual function values. ⭐
- **Cardinal property**: depends on the shape, location AND actual function values. ⭐
- **Monotonic transformation**: a strictly increasing function `g`. Composing with `g` preserves ranking.
- `g₁(z) = z + 1` ⟹ `y₁(u, v) = uv + 1`. Homothetic (not homogeneous).
- `g₂(z) = z² + z` ⟹ `y₂(u, v) = u²v² + uv`. Homothetic (not homogeneous).
- `g₃(z) = ln z` ⟹ `y₃(u, v) = ln(uv) = ln u + ln v`. Homothetic.

**Quick Recall:**
- Homothetic = monotonic transform of homogeneous.
- MRS along rays is constant for homothetic functions.
- Property is ordinal, so survives any monotone relabelling.
1. `f(u₁, u₂) = 3u₁²u₂⁴ + 2u₁²u₂⁴ - 3u₁³u₂³`. Compute `f(tu₁, tu₂)`:
2. `f(u₁, u₂) = α ln(u₁) + β ln(u₂)`. We can write `f = ln(u₁^α u₂^β)`. Let `g(u₁, u₂) = u₁^α u₂^β` (homogeneous of degree `α + β`) and `h(z) = ln z` (strictly increasing). Then `f = h ∘ g`, so **homothetic**.

### ⚠️ Common Mistakes
- ❌ Assuming homothetic ⟹ homogeneous → ✅ One-way only. `uv + 1` is homothetic but not homogeneous.
- ❌ Trying cardinal-style argument on homothetic functions → ✅ Only ordinal properties (level set shapes) are preserved.
---

### Concave Functions — Differentiable & Geometric Definitions 🔴
- (Geometric) the chord joining any two points on its graph lies on or below the curve, or equivalently
- (Differentiable) `f''(u) ≤ 0` for all `u` (univariate), or Hessian NSD (multivariate).
- `f'(u) = 2au + b`, `f''(u) = 2a`.
- If `a < 0`, `f''(u) < 0` ⟹ concave. If `a > 0`, convex.
- Builds on: Convex set definition.
- Equivalent to: Hessian-based test (Chunk 006).

### Maximum/Minimum Conditions for Concave Functions 🔴
- `f''(u) ≤ 0` for all `u ∈ X` AND
- `f'(a) = 0`

**Quick Recall:**
- Concave + stationary = global maximum.
- Convex + stationary = global minimum.
- **Don't need SOC** when concavity/convexity is established.

### Concave Functions — Theorems G, H, I 🔴

**Quick Recall:**
- Concave: `f(u) ≤ f(u₀) + ∇f(u₀) · (u - u₀)` (tangent above curve).
- Convex: reverse inequality (tangent below).

### Quasi-Concave Functions — Theorems J, K, L 🔴
- **Upper level set `U(f, α)`**: `{u ∈ X : f(u) ≥ α}`. ⭐
- **Lower level set `L(f, α)`**: `{u ∈ X : f(u) ≤ α}`.
- **Quasi-concave** (level-set form): all upper level sets `U(f, α)` are convex. ⭐

**Quick Recall:**
- Quasi-concave: upper level sets convex.
- Differentiable QC: gradient inequality (level-equal points yield non-negative directional derivative).

### Bordered Hessian — Determinant Criterion for Quasi-Concavity 🔴
- **Necessary** (for quasi-concavity): `(-1)^b D_b(u) ≥ 0` for `b = 1, ..., n`, all `u ∈ X`.
- **Sufficient** (for strict quasi-concavity): `(-1)^b D_b(u) > 0` for `b = 1, ..., n`, all `u ∈ X`.
- **Bordered Hessian (bth order)**: `(b+1) × (b+1)` matrix with first row `(0, f₁, ..., f_b)`, first column transposed of same, rest the `b × b` Hessian. ⭐
- `f₁ = e^{-u₂}`, `f₂ = -u₁ e^{-u₂}`.
- `f₁₁ = 0`, `f₁₂ = -e^{-u₂}`, `f₂₂ = u₁ e^{-u₂}`.
- `f_u₁ = 6u₁²`, `f_u₂ = -12u₂`.
- `f_u₁u₁ = 12u₁`, `f_u₂u₂ = -12`, `f_u₁u₂ = 0`.
- Hessian `H(u) = [[12u₁, 0], [0, -12]]`.
- For `u₁ ≤ 0`: `12u₁ ≤ 0`, `-12 < 0`, `det = -144u₁ ≥ 0`. NSD → **concave on `u₁ ≤ 0`**.

**Quick Recall:**
- Bordered Hessian sign-pattern: alternating starting positive (after `(-1)^b` weighting).
- For utility functions over goods (`u_i ≥ 0`), check signs throughout the orthant.

### Economic Applications of Euler's Theorem 🔴
- `pq = total revenue`.
- `uᵢ p (∂f/∂uᵢ) = total payment to factor i` (under marginal-product pricing).
- Total factor cost: `Σᵢ uᵢ p (∂f/∂uᵢ) = p · k · f(u) = k · pq`.
- `k = 1` (CRS): total factor cost = `p q` ⟹ **zero profit**. Firm spends entire revenue on inputs.
- `k > 1` (IRS): total factor payment exceeds revenue ⟹ negative profit, "exhausts more than the product."
- `0 < k < 1` (DRS): factor payment < revenue ⟹ **positive profit** for the firm.
- **Euler's theorem**: `Σᵢ uᵢ (∂f/∂uᵢ) = k f(u)` for homogeneous `f` of degree `k`. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Assuming Euler's theorem holds for any function → ✅ Only homogeneous functions. Degree `k` matters.
- ❌ Concluding that CRS always means zero accounting profit → ✅ "Zero profit" here = economic profit; it assumes inputs paid at marginal product.

**Quick Recall:**
- Euler: `u · ∇f = k f` (homogeneous degree `k`).
- CRS ⟹ exhaust revenue on factor payments (zero economic profit).
- DRS ⟹ residual surplus to firm (positive profit).
- Builds on: Homogeneous function definition (Chunk 008).
- Is prerequisite for: Cost-minimisation duality, factor demand functions (graduate microeconomics).
1. How does this connect to perfect competition's zero-profit result? (CRS + competitive markets ⟹ zero economic profit.)
2. What if production is not homogeneous? (Euler's theorem doesn't apply; use envelope theorem instead.)

**Quick Recall:**
- For symmetric quadratic Lagrangians, equating FOCs eliminates `λ` and reduces to one equation.
- Then substitute into the linear constraint to get the second equation.

### ⚠️ Common Mistakes
- ❌ Forgetting that envelope estimate is **first-order Taylor approximation** → ✅ Higher-order terms can matter for large `Δa`.
- ❌ Using `∂f/∂a` instead of `∂L/∂a` for constrained problems → ✅ Constrained envelope uses Lagrangian's partial.

**Quick Recall:**
- Envelope: `dV/da = ∂L/∂a |_{u*, λ*}`.
- Faster than re-substituting and differentiating.
---

**Quick Recall:**
- Test homogeneity by substituting `(tu)`; check if `t^k` factors out.
- Cobb-Douglas log form is homothetic (and Cobb-Douglas itself is homogeneous).

**Quick Recall:**
- Envelope theorem reduces algebra dramatically — read off `dπ*/dp = v*` at the optimum without forming `π*(p)` explicitly.

### ⚠️ Common Mistakes
- ❌ Forgetting that minimising vs maximising flips the SOC sign requirement → ✅ For minimum, bordered Hessian must be **positive (semi-)definite** on tangent space.
- ❌ Treating constraint multiplier `λ` casually → ✅ It has economic meaning: shadow price of the constraint (`dV/dc = λ`).

**Quick Recall:**
- Lagrangian for minimisation: same form, opposite SOC sign convention.
- For convex objective + linear constraint: any stationary point of `L` is the global minimum.
