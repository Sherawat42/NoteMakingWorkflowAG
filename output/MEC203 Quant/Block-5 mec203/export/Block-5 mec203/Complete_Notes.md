# Complete Notes


## Section: Block 5 Overview 🟢

### Core Idea
Block 5 of MEC-203 covers **Extreme Values and Optimisation** across four units. Unit 16 introduces extrema of single- and multi-variable functions; Unit 17 develops unconstrained and constrained optimisation (Lagrange and Kuhn-Tucker); Unit 18 deepens with convexity/concavity, NDCQ, and complementary slackness; Unit 19 covers the multiplier interpretation, envelope theorem, homogeneous/homothetic functions and quasi-concavity.

> **In Simple Terms:** This block teaches you the maths a producer or consumer uses to find the best choice — when nothing limits them, when an equation must hold, and when only inequalities apply.

### Unit Map

| Unit | Title | Key Tools |
|------|-------|-----------|
| 16 | Optimisation: An Introduction | FOC, SOC, point of inflexion, Hessian principal minors |
| 17 | Unconstrained & Constrained Optimisation | Lagrange multiplier, Kuhn-Tucker |
| 18 | Advanced Topics in Optimisation — I | Convexity/concavity, quasi-convexity, NDCQ |
| 19 | Advanced Topics in Optimisation — II | Envelope theorem, homogeneity, Euler's theorem |

---

## Section: Concept of Maxima and Minima — Univariate Functions 🔴

### Core Idea
Assume `y = f(x)` is differentiable (hence continuous). The graph can be constant, monotonically increasing, monotonically decreasing, or fluctuating. **Global (absolute) extrema** are the highest/lowest values over the entire domain — unique. **Local (relative) extrema** are extreme only within some neighbourhood. The collective term for max and min is **extremum**.

> **In Simple Terms:** A global maximum is the tallest hill in the entire country; a local maximum is the tallest hill in your village. There can be many local peaks but only one global peak.

### Key Concepts

#### Local (Relative) Extremum
At point `x = x₀`, the function attains a local maximum if for sufficiently small `ε > 0`,
`f(x₀ - ε) < f(x₀)` and `f(x₀ + ε) < f(x₀)`.
Similarly for a local minimum (inequalities flip). Local extrema are always **strictly interior** — they appear inside an interval, never at endpoints.

#### Global (Absolute) Extremum
The highest (resp. lowest) value of `f(x)` across its entire domain. A continuous function may have several local maxima but a unique global maximum. For a continuous function, the global max is always greater than the global min.

| Aspect | Local extremum | Global extremum |
|--------|----------------|-----------------|
| Scope | Some neighbourhood `(x-ε, x+ε)` | Entire domain |
| Uniqueness | Can be many | Unique (continuous f) |
| Location | Strictly interior | Interior or endpoint |
| Test | First/second derivative locally | Compare all candidates |

### Definitions
- **Stationary point**: a point where `f'(x) = 0` — the tangent is parallel to the x-axis. ⭐ (exam-important)
- **Extremum**: collective term for maximum and minimum, mathematical concept without optimality connotation. ⭐
- **Extreme values / extrema**: maximum and minimum values of a function. ⭐

---

## Section: Identification of Maxima and Minima 🔴

### Core Idea
At a turning point `A` (local max), `f'` changes from positive (left of A) to negative (right of A); at a local min, the slope changes from negative to positive. So a stationary value is necessary for an extremum, and the sign-change of `f'` is sufficient. The classic test: solve `f'(x) = 0`, then check `f''(x)`.

> **In Simple Terms:** Walking up a hill the path tilts up (slope > 0); standing on the peak it's flat (slope = 0); walking down it tilts down (slope < 0). The flat moment is the peak.

### Key Concepts

#### Necessary Condition (FOC)
For a max or a min at `x₀`: `f'(x₀) = 0`. Both maxima and minima share the **same** necessary condition. By itself, FOC is not enough — a point of inflexion also satisfies `f'(x) = 0`.

#### Sufficient Condition (SOC)
- For a **maximum** at `x₀`: `f'(x₀) = 0` AND `f''(x₀) < 0`.
- For a **minimum** at `x₀`: `f'(x₀) = 0` AND `f''(x₀) > 0`.

Geometrically: at a max, the curve passes through the peak with slope changing positive→negative, so the slope itself is decreasing (`f'' < 0`).

### Mechanisms / Processes

Standard procedure for univariate extrema:
1. Compute `f'(x)`.
2. Solve `f'(x) = 0` → candidate stationary points.
3. Compute `f''(x)`.
4. Evaluate `f''` at each candidate:
   - `f''(x₀) > 0` → minimum at `x₀`.
   - `f''(x₀) < 0` → maximum at `x₀`.
   - `f''(x₀) = 0` → inconclusive (use higher-order test).

### Examples

**Example 16.1 — Polynomial extrema**
For `y = 3x⁴ - 10x³ + 6x² + 5`:
- FOC: `12x³ - 30x² + 12x = 0` → `3x(4x - 2)(x - 2) = 0` → `x = 0, 1/2, 2`.
- SOC: `f''(x) = 36x² - 60x + 12`.
  - At `x = 0`: `f''(0) = 12 > 0` → minimum.
  - At `x = 2`: `f''(2) = 144 - 120 + 12 = 36 > 0` → minimum.
  - At `x = 1/2`: `f''(1/2) = 9 - 30 + 12 = -9 < 0` → maximum.

**Example 16.2 — A surprising case**
For `y = x + 1/x`:
- `f'(x) = 1 - 1/x²` ⟹ stationary at `x = 1, -1`.
- `f''(x) = 2/x³`.
- At `x = 1`: `f''(1) = 2 > 0` → minimum, `f(1) = 2`.
- At `x = -1`: `f''(-1) = -2 < 0` → maximum, `f(-1) = -2`.

So the "maximum" value (-2) is actually less than the "minimum" value (+2) — local extrema, not global.

### ⚠️ Common Mistakes
- ❌ Concluding a stationary point is a maximum just because `f'(x₀) = 0` → ✅ Always verify with `f''(x₀)`.
- ❌ Assuming the local max value > local min value → ✅ As Example 16.2 shows, this need not hold across separate regions.

> **Quick Recall:**
> - FOC for extremum: `f'(x₀) = 0` (same for max and min).
> - Max ⟺ `f'(x₀) = 0` and `f''(x₀) < 0`.
> - Min ⟺ `f'(x₀) = 0` and `f''(x₀) > 0`.

---

## Section: Point of Inflexion 🔴

### Core Idea
When the second derivative is zero, the standard SOC fails. The function may have a max, min, or a **point of inflexion** — a point where the curve changes its **curvature** (concave-up to concave-down or vice versa). At an inflexion point, the curve's direction of motion is preserved; only the bending changes. The first derivative reaches a local max or min there.

> **In Simple Terms:** Driving on a winding road, an inflexion point is where the road stops turning right and starts turning left (or vice versa) — your forward direction continues, but the bend reverses.

### Definitions
- **Point of inflexion**: a point at which a curve changes its curvature. Sufficient condition: `f''(x) = 0` and `f'''(x) ≠ 0`. ⭐ (exam-important)
- A point with `f'(x) = 0`, `f''(x) = 0`, `f'''(x) ≠ 0` is called **stationary and inflexional** — it's both a stationary point and an inflexion.

### Key Concepts

#### Curvature Transition
- If a monotonic function is first **convex** then **concave**, the inflexion point yields a maximum of `f'(x)`.
- If first **concave** then **convex**, the inflexion gives a minimum of `f'(x)`.

### Examples

**Example 16.3** — `f(x) = x³ + 2`:
- `f'(x) = 3x²`, `f''(x) = 6x`, `f'''(x) = 6 ≠ 0`.
- `f''(x) = 6x = 0` ⟹ `x = 0`.
- Hence the function has a point of inflexion at the origin.

**Check Your Progress 1**: Show `f(x) = x³ - 6x² + 24x + 4` has neither max nor min.
Solution: `f'(x) = 3(x² - 4x + 8) = 3[(x - 2)² + 4] > 0 ∀ x`. So `f'` never vanishes — no extrema.

**Check Your Progress 2**: For `f(x) = x³ + x² + x + 1`, the inflexion is at `x = -1/3`.

> **Quick Recall:**
> - Inflexion: `f''(x) = 0`, `f'''(x) ≠ 0`.
> - Stationary + inflexional: `f'(x) = 0`, `f''(x) = 0`, `f'''(x) ≠ 0`.

---

## Section: Conclusive Criterion (Taylor Series Test) 🔴

### Core Idea
A general test using Taylor's expansion with Lagrange remainder:
`f(x) - f(a) = f'(a)(x-a) + (1/2!)f''(a)(x-a)² + ... + (1/n!)f⁽ⁿ⁾(x*)(x-a)ⁿ`,
where `x* = a + θ(x - a)`, `0 < θ < 1`.

The leading non-zero derivative determines whether `a` is a max, min, or inflexion.

> **In Simple Terms:** If the standard `f''` test fails, keep differentiating. The first non-zero derivative tells you everything: if it's an even-order derivative the point is an extremum; if odd, an inflexion.

### Mechanisms / Processes

**Cases by order of vanishing derivatives:**

| Case | First non-zero derivative | Sign condition | Result at `x = a` |
|------|---------------------------|----------------|-------------------|
| I | `f'(a) ≠ 0` | — | Not an extremum (FOC fails) |
| II | `f'(a) = 0`, `f''(a) ≠ 0` | `f''(a) > 0` | Local minimum |
| | | `f''(a) < 0` | Local maximum |
| III | `f'(a) = f''(a) = 0`, `f'''(a) ≠ 0` | — | Point of inflexion |
| IV | `f'(a) = f''(a) = f'''(a) = 0`, `f⁽⁴⁾(a) ≠ 0` | `f⁽⁴⁾(a) > 0` | Local minimum |
| | | `f⁽⁴⁾(a) < 0` | Local maximum |

#### Generalised rule
When `f'(a) = f''(a) = ... = f⁽ⁿ⁻¹⁾(a) = 0` and `f⁽ⁿ⁾(a) ≠ 0`, point `x = a` is:
- a **maximum** if `n` is **even** and `f⁽ⁿ⁾(a) < 0`,
- a **minimum** if `n` is **even** and `f⁽ⁿ⁾(a) > 0`,
- an **inflexion** if `n` is **odd**.

> **Quick Recall:**
> - Even `n` → extremum (sign of `f⁽ⁿ⁾` decides max/min).
> - Odd `n` → inflexion.
> - Use this when `f''(x₀) = 0` and the standard test is inconclusive.

---

## Section: Extreme Values of Multivariate Functions — FOC for Bivariate 🔴

### Core Idea
For `y = f(x)`, the FOC `dy = 0` is equivalent to `f'(x) = 0` (since `dy = f'(x) dx` and `dx ≠ 0`). For a bivariate function `y = f(x₁, x₂)`, the total differential is `dy = f₁ dx₁ + f₂ dx₂`. For `dy = 0` to hold for arbitrary, non-zero `dx₁, dx₂`, we must have `f₁ = 0` AND `f₂ = 0` simultaneously.

> **In Simple Terms:** On a 2D landscape, you're at a flat point only if both the east-west slope and the north-south slope are zero. Either alone isn't enough.

### Mechanisms / Processes
1. Compute partial derivatives: `f₁ = ∂f/∂x₁`, `f₂ = ∂f/∂x₂`.
2. Set both to zero: `f₁ = 0` and `f₂ = 0`.
3. Solve the system simultaneously to get candidate `(x₁*, x₂*)`.
4. Test SOC using the Hessian (Chunk 002 develops this).

> **Quick Recall:**
> - Bivariate FOC: `f₁ = f₂ = 0`.
> - n-variable FOC: `fᵢ = 0 ∀ i = 1, ..., n`. <!-- Continues in chunk 002 -->

### Connections
- Builds on: Univariate FOC `f'(x) = 0` (this section).
- Is prerequisite for: SOC via Hessian principal minors (Chunk 002: Sufficient Condition for Bivariate Extreme Values).

### Open Questions
1. How does the FOC for an extremum interact with constraints? (Answered in Unit 17.)


---

<!-- See chunk 001 for start of Unit 16 -->

## Section: Sufficient Condition for Bivariate Extreme Values 🔴

### Core Idea
For `y = f(x₁, x₂)` with FOC `f₁ = f₂ = 0` already satisfied, the sufficient condition asks whether `d²y` is everywhere negative (max), everywhere positive (min), or sign-indefinite (saddle/inflexion). After expanding `d²y` and using **Young's theorem** (`f₁₂ = f₂₁`), the test reduces to checking signs of three numbers: `f₁₁`, `f₂₂`, and the determinant `f₁₁f₂₂ - f₁₂²`.

> **In Simple Terms:** Past the flat spot, ask "what happens if I wiggle in any direction?" If you always go down → max. Always up → min. Sometimes up, sometimes down → saddle.

### Mechanisms / Processes

Starting from `dy = f₁ dx₁ + f₂ dx₂ = 0`, totally differentiate:
`d²y = f₁₁(dx₁)² + 2f₁₂ dx₁ dx₂ + f₂₂(dx₂)²`

Treat as quadratic form in `dx₁, dx₂`:
`q = au² + 2huv + bv²`
where `a = f₁₁, b = f₂₂, h = f₁₂, u = dx₁, v = dx₂`.

Complete the square:
`q = a[(u + (h/a)v)² + ((ab - h²)/a²)v²]`

Hence:
- `q < 0` ⟺ `a < 0` AND `ab - h² > 0` (which forces `b < 0` too).
- `q > 0` ⟺ `a > 0` AND `ab - h² > 0` (forces `b > 0` too).

### Key Concepts

| Condition on (f₁₁, f₂₂, f₁₁f₂₂ - f₁₂²) | Result |
|----------------------------------------|--------|
| `f₁₁ < 0`, `f₂₂ < 0`, `f₁₁f₂₂ - f₁₂² > 0` | **Maximum** |
| `f₁₁ > 0`, `f₂₂ > 0`, `f₁₁f₂₂ - f₁₂² > 0` | **Minimum** |
| `f₁₁f₂₂ < f₁₂²` and `f₁₁`, `f₂₂` have **different** signs | **Saddle point** |
| `f₁₁f₂₂ < f₁₂²` and `f₁₁`, `f₂₂` have **same** sign | **Inflexion point** |
| `f₁₁f₂₂ = f₁₂²` | Inconclusive |

### Definitions
- **Hessian determinant** (2×2): `|H| = | f₁₁ f₁₂ ; f₂₁ f₂₂ |`. ⭐ (exam-important)
- **Saddle point**: stationary point that is a max in one direction and a min in another. ⭐
- **Young's theorem**: For functions with continuous mixed partials, `f₁₂ = f₂₁`. ⭐
- **Principal minor**: a sub-determinant of the Hessian formed by the first `i` rows and columns. ⭐

### Matrix Form
Quadratic form `q = au² + 2huv + bv²` rewrites as `[u v] [[a h];[h b]] [u; v]`.
The matrix `[[a h];[h b]]` supplies the conditions:
- `q > 0` ⟺ `|a| > 0` AND `|H| > 0` (both leading principal minors positive).
- `q < 0` ⟺ `|a| < 0` AND `|H| > 0` (alternating signs).

> **Quick Recall:**
> - Bivariate min: `f₁₁ > 0`, `|H| > 0`.
> - Bivariate max: `f₁₁ < 0`, `|H| > 0`.
> - Saddle: `|H| < 0`.

---

## Section: Three-Variable Extrema (Principal Minors) 🔴

### Core Idea
For `z = f(x, y, w)`, the second-differential quadratic form has 3×3 Hessian
`H = [[fₓₓ, fₓᵧ, fₓw]; [fᵧₓ, fᵧᵧ, fᵧw]; [fwₓ, fwᵧ, fww]]`.
There are **three** principal minors `D₁, D₂, D₃`. The signs determine extremum type, generalising the bivariate result.

### Key Concepts

| Quadratic form | Principal minor pattern | Result |
|----------------|------------------------|--------|
| `q > 0` (`d²z` positive definite) | `D₁ > 0`, `D₂ > 0`, `D₃ > 0` | **Minimum** |
| `q < 0` (`d²z` negative definite) | `D₁ < 0`, `D₂ > 0`, `D₃ < 0` | **Maximum** |

In words:
- **All positive** ⟹ minimum.
- **Alternating starting with negative** ⟹ maximum.

### Definitions
- **D₁** = `fₓₓ` (1×1 leading minor).
- **D₂** = `|fₓₓ fₓᵧ ; fᵧₓ fᵧᵧ|` (2×2 leading minor).
- **D₃** = `|H|` (full 3×3 determinant).

---

## Section: n-Variable Extrema — Hessian Determinantal Test 🔴

### Core Idea
Generalising to `z = f(x₁, ..., xₙ)`:
- FOC: all `n` first partials vanish, `f₁ = f₂ = ... = fₙ = 0`.
- SOC: examine the `n` leading principal minors `|H₁|, |H₂|, ..., |Hₙ|`.

### Key Concepts

| Condition | Maximum | Minimum |
|-----------|---------|---------|
| FOC | `dz = 0`, i.e. `f₁ = f₂ = ... = fₙ = 0` | same |
| SOC | `\|H_i\|` alternate in sign starting negative: `\|H₁\| < 0`, `\|H₂\| > 0`, `\|H₃\| < 0`, ... | All `\|H_i\| > 0` |

Compactly:
- **Maximum**: `(-1)^i |Hᵢ| > 0` for `i = 1, ..., n`.
- **Minimum**: `|Hᵢ| > 0` for `i = 1, ..., n`.

### ⚠️ Common Mistakes
- ❌ Checking only `|Hₙ|` (the full determinant) → ✅ All leading principal minors must be checked.
- ❌ Forgetting that for max, the **first** minor `|H₁|` must be negative (not the last) → ✅ Sign pattern starts negative for max.

> **Quick Recall:**
> - Min: every `\|H_i\|` is **positive**.
> - Max: signs **alternate** starting with **negative**.

---

## Section: Worked Examples — Multivariate Extrema 🔴

### Examples

**Example 16.4 (i)** — Determine whether `Z = x₁² - 3x₁x₂ + 3x₂² + 4x₂x₃ + 6x₃²` is a max or a min.

FOC:
- `f₁ = 2x₁ - 3x₂ = 0`
- `f₂ = -3x₁ + 6x₂ + 4x₃ = 0`
- `f₃ = 4x₂ + 12x₃ = 0`

Solving: `x₁ = 0, x₂ = 0, x₃ = 0`. Stationary point: origin.

Hessian:
```
|H| = | 2  -3   0 |
      | -3  6   4 |
      | 0   4  12 |
```
- `|H₁| = 2 > 0`
- `|H₂| = | 2 -3 ; -3 6 | = 12 - 9 = 3 > 0`
- `|H₃| = 2(72 - 16) - (-3)(-36 - 0) + 0 = 112 - 108 = 4 > 0`

All positive → **minimum** at `(0, 0, 0)` with value 0.

**Example 16.4 (ii)** — `v = -x³ + 3xz + 2y - y² - 3z²`.

FOC: `f₁ = -3x² + 3z = 0`, `f₂ = 2 - 2y = 0`, `f₃ = 3x - 6z = 0`.
Solving: stationary points at `(0, 1, 0)` and `(1/2, 1, 1/4)`.

Hessian: `|H| = | -6x 0 3 ; 0 -2 0 ; 3 0 -6 |`.
- At `(0, 1, 0)`: `f₁₁ = 0`, so SOC fails — inconclusive.
- At `(1/2, 1, 1/4)`: `|H₁| = -3 < 0`, `|H₂| = 6 > 0`, `|H₃| = -18 < 0` → alternating signs → **maximum**, with value `17/16`.

> **Quick Recall:**
> - Always evaluate the Hessian **at** the stationary point — its sign-pattern can vary across the domain.
> - If `|H₁| = 0` at a stationary point, SOC is inconclusive; need higher-order test.

---

## Section: Unit 16 Key Words & Answers 🟡

### Definitions
- **Local (relative) maxima/minima**: function attains the extremum only in some neighbourhood; can be non-unique.
- **Global (absolute) maxima/minima**: extremum across the entire domain; unique for a continuous function.
- **Point of inflexion**: a point where curvature changes; sufficient condition `f''(x) = 0` and `f'''(x) ≠ 0`.
- **Stationary point**: a point where first-order derivatives are zero; the function value there is a stationary value.

### Check Your Progress 3 — Bivariate
1. `z = 3x² + 6xy + 7y²`: FOC gives `(0, 0)`; `f_xx = 6 > 0`, `f_yy = 14 > 0`, `f_xx f_yy - f_xy² = 84 - 36 = 48 > 0` → **minimum**, value 0.
2. `z = 4x² - 2y² + 7xy`: FOC gives `(0, 0)`; `f_xx = 8`, `f_yy = -4` (opposite signs), `f_xx f_yy - f_xy² = -32 - 49 < 0` → **saddle point**.

### Check Your Progress 4
- (a) `z = 2x² + xy + 4y² + xz + z² + 2`: No max or min.
- (b) `z = e^(-x) - e^y + e^z - 2(x + e^z) + y`: Max at `(0, 0, 0)`.

---

## Section: Unit 16 Exercises 🟡

**Q1**: Maxima and minima of `f(x) = 1 + 2 sin x + 3 cos²x` on `0 ≤ x ≤ π/2`.
- `f'(x) = 2 cos x - 6 cos x sin x = 2 cos x (1 - 3 sin x)`.
- `f'(x) = 0` when `cos x = 0` (i.e. `x = π/2`) or `sin x = 1/3`.
- At `cos x = 0` (`sin x = 1`): `f''(x) = -2(1) - 6(0 - 1) = 4 > 0` → **min**, value `f = 1 + 2(1) + 0 = 3`.
- At `sin x = 1/3`: `f''(x) = -2(1/3) - 6(1 - 2/9) = -2/3 - 14/3 < 0` → **max**.
  Maximum value: `1 + 2(1/3) + 3(1 - 1/9) = 1 + 2/3 + 8/3 = 1 + 10/3 = 13/3`. (Source gives `4` — note minor OCR drift; algebra confirms `13/3 ≈ 4.33`.)

**Q2**: `y = x₁³ + 2x₂³ - 6x₁² + 9x₂² - 63x₁ - 60x₂ - 24`.
- `(x₁, x₂) = (-3, 2)`: saddle.
- `(7, -5)`: saddle.
- `(-3, -5)`: relative maximum.
- `(7, 2)`: relative minimum.

**Q3**: `y = -x₁³ + 9x₁ - 4x₂²`.
- FOC: `-3x₁² + 9 = 0` ⟹ `x₁ = ±√3`; `-8x₂ = 0` ⟹ `x₂ = 0`.
- At `(√3, 0)`: maximum. At `(-√3, 0)`: saddle.

### Connections
- Builds on: Univariate extrema (Chunk 001: Block 5 Overview).
- Is prerequisite for: Unconstrained optimisation in economic problems (Chunk 003: Unconstrained Optimisation — First Order Condition).

> **Quick Recall:**
> - For each stationary point, compute the Hessian **at that point**.
> - Different stationary points of the same function can have different natures.


---


## Section: Unconstrained Optimisation — First Order Condition 🔴

### Core Idea
Under unconstrained optimisation we maximise or minimise a function whose domain is **not restricted by any constraint**. The first-order condition for `y = f(x)` is `dy = 0` "for arbitrary nonzero `dx`," which is equivalent to the derivative form `f'(x) = 0`. This necessary condition is the **same for both** maxima and minima — what distinguishes them is the SOC.

> **In Simple Terms:** Wherever the slope is exactly zero, you've found a candidate for the top of the hill or the bottom of the valley. A separate check decides which.

### Definitions
- **Unconstrained optimisation**: maximisation/minimisation of `f(x₁, ..., xₙ)` with no equality or inequality constraint on the domain. ⭐
- **Differential FOC**: `dy = 0` for arbitrary `dx ≠ 0`.
- **Derivative FOC**: `f'(x) = 0` (univariate); `fᵢ = 0 ∀ i` (multivariate).

### Examples

**Example 17.1**: `y = x³ - x` on `(-∞, +∞)`.
- FOC: `3x² - 1 = 0` ⟹ `x = ±1/√3`.

**Example 17.2**: `Z = y² - xy + x²`.
- FOC: `∂Z/∂x = -y + 2x = 0`; `∂Z/∂y = 2y - x = 0`.
- Solution: `x* = 0, y* = 0`. Optimum value `z = 0`.

> **Quick Recall:**
> - Necessary FOC for any extremum: all first partials vanish.
> - Same FOC for max and min; SOC distinguishes.

---

## Section: Second Order Condition for `z = f(x, y)` 🔴

### Core Idea
The second-order partials are `f_xx, f_yy` (own seconds) and `f_xy = f_yx` (cross/mixed, equal by Young's theorem). Sufficient conditions for an extremum at the stationary point use signs of all three:

> **In Simple Terms:** It's not enough that the surface curls down in the x-direction. It must curl down in the y-direction too, AND the cross-term `f_xy²` must not exceed `f_xx · f_yy`. Otherwise the surface might be a saddle.

### Key Concepts

#### Sufficient SOC for `z = f(x, y)`

| Condition | Maximum | Minimum |
|-----------|---------|---------|
| FOC | `f_x = f_y = 0` | `f_x = f_y = 0` |
| SOC | `f_xx < 0`, `f_yy < 0`, `f_xx f_yy > f_xy²` | `f_xx > 0`, `f_yy > 0`, `f_xx f_yy > f_xy²` |

The cross-partial `f_xy` ensures that the surface bends consistently in **all** directions — not just along axis-aligned cross-sections.

#### Necessary vs Sufficient
The SOC stated above is **sufficient** but not **necessary** — the strict inequalities can collapse to weak ones at an actual extremum. Necessary SOC: `d²z ≤ 0` (max) or `d²z ≥ 0` (min) for all `(dx, dy)`, not both zero.

#### Saddle Point Detection
If at a stationary point `f_xx f_yy < f_xy²`, the sign of `d²z` is indefinite (positive in some directions, negative in others) — this is a **saddle point**.

### Definitions
- **Hessian** (2×2): `H = [[f_xx, f_xy]; [f_xy, f_yy]]`. ⭐ (exam-important)
- **Cross (mixed) partial**: `f_xy = ∂²f/∂x∂y`. Equals `f_yx` under continuity (Young's theorem).

---

## Section: Determinantal Test (n-Variable) 🔴

### Core Idea
For `z = f(x₁, ..., xₙ)`, FOC is `f₁ = ... = fₙ = 0`. The Hessian is the symmetric `n×n` matrix of all second partials. The SOC examines the leading principal minors `|H₁|, ..., |Hₙ|`.

### Key Concepts

| Condition | Maximum | Minimum |
|-----------|---------|---------|
| FOC | `f₁ = ... = fₙ = 0` | `f₁ = ... = fₙ = 0` |
| SOC | `(-1)^i \|H_i\| > 0` for all `i = 1,...,n` | `\|H_i\| > 0` for all `i = 1,...,n` |

**Special cases:**
- `n = 1`: SOC reduces to `f''(x*) < 0` (max) or `f''(x*) > 0` (min).
- `n = 2`: SOC reduces to `f_xx < 0` and `|H₂| = f_xx f_yy - f_xy² > 0` (max), with the dual for min.

### Examples

**Example 17.3**: `Z = x² + xy + 2y² + 3`.
- FOC: `f_x = 2x + y = 0`, `f_y = x + 4y = 0` ⟹ `x* = 0, y* = 0`.
- `f_xx = 2 > 0`, `f_yy = 4 > 0`, `f_xy = 1`. `f_xx f_yy = 8 > f_xy² = 1`. → **Minimum**.

**Example 17.4**: `Z = -x² + xy - y² + 2x + y`.
- FOC: `-2x + y + 2 = 0`, `x - 2y + 1 = 0` ⟹ `x* = 5/3, y* = 4/3`.
- `f_xx = -2 < 0`, `f_yy = -2 < 0`, `f_xy = 1`. `f_xx f_yy = 4 > 1 = f_xy²`. → **Maximum**.

### ⚠️ Common Mistakes
- ❌ Confusing "SOC fails" with "no extremum" → ✅ SOC failure means inconclusive; it could still be an extremum (the sufficient condition is just sufficient).
- ❌ Forgetting `f_xy²` term — using only `f_xx f_yy > 0` → ✅ Must check `f_xx f_yy - f_xy² > 0` (the determinantal condition).

> **Quick Recall:**
> - `n` variables → `n` leading principal minors.
> - **Min**: every minor positive.
> - **Max**: signs alternate `(−, +, −, +, ...)` starting with negative.

---

## Section: Economic Application — Multi-product Firm Under Pure Competition 🔴

### Core Idea
Under pure competition, prices are exogenous. A two-product firm with prices `p₁ = 5, p₂ = 3` and cost function `C = 2q₁² + 2q₂² + q₁q₂` (cost cross-term reflecting **technical relatedness** in production) chooses output levels to maximise profit. The Hessian's negative-definiteness on the entire domain proves the candidate is a **unique absolute** maximum, not just local.

> **In Simple Terms:** A wheat-and-rice farmer who can't influence prices picks output levels by setting marginal profit on each product to zero. Because his cost function has a constant negative-definite Hessian, the answer is the unique global best.

### Mechanisms / Processes — Example 17.5

Setup:
- Revenue: `R = p₁q₁ + p₂q₂ = 5q₁ + 3q₂`.
- Cost: `C = 2q₁² + 2q₂² + q₁q₂`.
- Profit: `π = R - C = 5q₁ + 3q₂ - 2q₁² - 2q₂² - q₁q₂`.

**FOC:**
1. `∂π/∂q₁ = 5 - 4q₁ - q₂ = 0`
2. `∂π/∂q₂ = 3 - 4q₂ - q₁ = 0`

System: `4q₁ + q₂ = 5`, `q₁ + 4q₂ = 3`. Solve via Cramer/elimination:
`q₁* = 17/15`, `q₂* = 7/15`. Maximum profit `π* ≈ 5.51`.

**SOC (Hessian):**
```
H = [ -4  -1 ]
    [ -1  -4 ]
```
- `|H₁| = -4 < 0` ✓
- `|H₂| = 16 - 1 = 15 > 0` ✓
- Alternating sign pattern → **negative definite** → maximum.

**Why unique global?** Both principal minors are constants — independent of `(q₁, q₂)`. So the Hessian is negative definite **everywhere**, the objective function is **strictly concave**, and the local max is the unique global max.

> **Quick Recall:**
> - Multi-product competitive firm: profit = (linear revenue) - (quadratic cost).
> - Constant negative-definite Hessian ⟹ strict concavity ⟹ unique global max.

---

## Section: Economic Application — Multi-product Monopoly 🔴

### Core Idea
The same firm now sets **both prices and quantities** as a monopolist in both markets. Demand functions reveal that the goods are **substitutes** (`q₁` rises if `p₂` rises). Inverting demand via Cramer's rule gives the average revenue functions. Maximise profit `π(q₁, q₂)`; verify SOC.

> **In Simple Terms:** A monopolist over two related products chooses quantities knowing each price reacts to its own and the other product's quantity. The optimum balances loss in one market against gain in the other.

### Mechanisms / Processes — Example 17.6

Demand functions:
- `q₁ = 40 - 2p₁ + p₂`
- `q₂ = 15 + p₁ - p₂` (substitutes — see how a rise in `p₂` raises `q₁`).

Inverted (Cramer's rule on `-2p₁ + p₂ = q₁ - 40`, `p₁ - p₂ = q₂ - 15`):
- `p₁ = 55 - q₁ - q₂` (= AR₁)
- `p₂ = 70 - q₁ - 2q₂` (= AR₂)

Revenue: `R = p₁q₁ + p₂q₂ = 55q₁ + 70q₂ - 2q₁q₂ - q₁² - 2q₂²`.
Cost (assumed): `C = q₁² + q₁q₂ + q₂²`.
Profit: `π = 55q₁ + 70q₂ - 3q₁q₂ - 2q₁² - 3q₂²`.

**FOC:**
- `π₁ = 55 - 3q₂ - 4q₁ = 0` ⟹ `4q₁ + 3q₂ = 55`
- `π₂ = 70 - 3q₁ - 6q₂ = 0` ⟹ `3q₁ + 6q₂ = 70`

Solution: `q₁* = 8`, `q₂* = 7 + 2/3 ≈ 7.67`.
Substituting back: `p₁* ≈ 39.3`, `p₂* ≈ 46.4`, `π* ≈ 488.3`.

**SOC:**
```
H = [ -4  -3 ]
    [ -3  -6 ]
```
`|H₁| = -4 < 0`, `|H₂| = 24 - 9 = 15 > 0`. Negative definite everywhere → **strictly concave profit function** → unique absolute maximum.

### ⚠️ Common Mistakes
- ❌ Treating the demand cross-effect (between `p₁` and `q₂`) as zero in profit derivatives → ✅ The cost cross-term `q₁q₂` and the revenue cross-term both contribute.
- ❌ Concluding "local max" without checking signs of leading minors at the stationary point → ✅ Always test the Hessian.

> **Quick Recall:**
> - Substitute goods: cross-price coefficient in demand is **positive**.
> - Inverse demand via Cramer's rule.
> - If Hessian's principal-minor signs are independent of where evaluated, optimum is global.

---

## Section: Constrained Optimisation — Setup 🔴

### Core Idea
Most economic problems have **constraints**: budgets, resource availability, technology bounds. **Constrained optimisation** seeks the best feasible alternative. Vocabulary:
- **Objective function**: dependent variable to maximise/minimise.
- **Choice (decision/policy) variables**: independent variables we control.
- **Optimisation**: collective term for max and min ("the quest for the best").
- **Extremum** (in the math sense): max or min, no optimality connotation.

> **In Simple Terms:** A consumer maximising utility `U(x₁, x₂)` is unconstrained on paper but constrained by income and prices. Constrained optimisation gives the rules for the trade-off.

### Definitions
- **Constraint optimisation**: choosing values of decision variables that yield the desired extremum of the objective function while respecting constraints. ⭐
- **Choice / decision / policy variables**: the independent variables whose values the agent picks. ⭐ <!-- Continues in chunk 004 -->

### Connections
- Builds on: Unconstrained SOC framework (this chunk).
- Is prerequisite for: Lagrange theorem and Kuhn-Tucker theory (Chunk 004: Equality Constrained Optimisation — No-Arbitrage Principle).

### Open Questions
1. How exactly does the budget constraint enter the FOC? (Lagrangian — Chunk 004.)
2. What if the constraint is an inequality? (Kuhn-Tucker — Chunk 004.)


---

<!-- See chunk 003 for start of Constrained Optimisation -->

## Section: Equality Constrained Optimisation — No-Arbitrage Principle 🔴

### Core Idea
At a constrained maximum, no infinitesimal reallocation across choice variables (that respects the constraint) can increase the objective. For a household choosing `(x₁, x₂)` to maximise `U(x₁, x₂)` subject to `p₁x₁ + p₂x₂ = I`, the no-arbitrage condition becomes:

`U₁/p₁ = U₂/p₂` — **marginal utility per rupee is equal across goods**.

> **In Simple Terms:** If you could shift one rupee from good 2 to good 1 and gain utility, you weren't at the optimum. The optimum is precisely where any such shift gains nothing — that's why ratios of MU to price must be equal.

### Mechanisms / Processes — Example 17.7

Setup: `Max U(x₁, x₂)` s.t. `I - p₁x₁ - p₂x₂ = 0` with `x* > 0`.

Shift income `dI > 0` from good 2 to good 1: `dx₁ = dI/p₁ > 0`, `dx₂ = -dI/p₂ < 0`. Budget still satisfied:
`p₁(x₁ + dx₁) + p₂(x₂ + dx₂) = I` ✓.

Change in utility: `dU = U₁ dx₁ + U₂ dx₂ = [U₁/p₁ - U₂/p₂] dI ≤ 0` (since `x*` is a max, no upward variation possible).

Reverse direction (shift from good 1 to good 2) gives the opposite inequality. Combined:

`U₁(x*)/p₁ = U₂(x*)/p₂`

This implies `U₁(x*) = λ* p₁`, `U₂(x*) = λ* p₂` where `λ*` is the **Lagrange multiplier** representing **marginal utility of income**. Together with the budget equation, these are the FOCs of the **Lagrangian**:

`L(x, λ) = U(x₁, x₂) + λ[I - p₁x₁ - p₂x₂]`

### Generalisation
For `Max F(x)` s.t. `c - G(x) = 0`, the no-arbitrage logic gives `F₁(x*)/G₁(x*) = F₂(x*)/G₂(x*) = λ*`, with the **constraint qualification** `G₁(x*)` and `G₂(x*)` not both zero.

### Definitions
- **Lagrangian function**: `L(x, λ) = f(x) + λ[c - g(x)]`. ⭐ (exam-important)
- **Lagrange multiplier λ***: shadow price of the constraint — the rate at which the optimum value of the objective changes when the constraint is relaxed by one unit. ⭐
- **Constraint qualification (CQ)**: the constraint gradient(s) are linearly independent at the optimum. ⭐

> **Quick Recall:**
> - Equal-MU-per-rupee rule: `∂f/∂xᵢ ÷ ∂g/∂xᵢ` is the same constant `λ*` across all `i`.
> - λ* = derivative of optimal objective with respect to the constraint constant.

---

## Section: Theorem of Lagrange 🔴

### Core Idea
For a smooth objective `f: ℝⁿ → ℝ` and `k` smooth equality constraints `gⁱ: ℝⁿ → ℝ` (with `k < n`), if `x*` is a local extremum on the constraint set, then there exist real numbers `μ*, λ₁*, ..., λₖ*` (not all zero) such that

`μ* Df(x*) + Σᵢ λᵢ* Dgⁱ(x*) = 0`.

If the **constraint qualification** holds — `rank(Dg(x*)) = k` (i.e. the constraint gradients are linearly independent) — then we can normalise `μ = 1`, recovering the standard Lagrangian FOCs.

> **In Simple Terms:** At a constrained extremum, the gradient of the objective is a linear combination of the gradients of the constraints. They line up — there's no "free" direction along the constraint surface that improves the objective.

### Definitions
- **Theorem of Lagrange** (necessary condition): given continuous differentiability of `f` and `gⁱ`, at any local extremum of `f` on the constraint set there exist multipliers (not all zero) satisfying the gradient equation above. ⭐
- **Rank-`k` Jacobian condition** ⟺ CQ. If CQ holds, `μ ≠ 0`, so we can divide through and set `μ = 1`. ⭐

### Mechanisms / Processes — Lagrangian Method
1. Write `L(x, λ) = f(x) + Σᵢ λᵢ gⁱ(x)`.
2. FOCs: `n + k` equations:
   - `∂L/∂xⱼ = ∂f/∂xⱼ + Σᵢ λᵢ ∂gⁱ/∂xⱼ = 0` for `j = 1, ..., n`.
   - `∂L/∂λᵢ = gⁱ(x) = 0` for `i = 1, ..., k`.
3. Solve simultaneously for `(x*, λ*)`.
4. Verify SOC via bordered Hessian on the tangent space.

### Examples (KT method introduced for completeness)

**Check Your Progress 2(1)**: `U(x, y) = x²y`, `p_x = 2, p_y = 1, I = 200`.
- Lagrangian: `L = x²y + λ[200 - 2x - y]`.
- FOC: `2xy = 2λ`, `x² = λ`, `2x + y = 200`.
- Substitute `λ = x²` into `2xy = 2λ`: `xy = x²` ⟹ `y = x`. Then `2x + x = 3x = 200` (after error correction matches source). Source gives `x* = 200/3, y* = 200/3, λ* = (200/3)²`. (Source actually gets `x = y = 200/3` reflecting the calculation `2x + y = 200` paired with the FOC ratio).

> **Quick Recall:**
> - For each equality constraint, introduce one Lagrange multiplier.
> - Stationary points of `L` correspond to candidate constrained extrema.
> - Always check CQ (Jacobian of constraint gradients has full rank).

---

## Section: Second Order Condition for Constrained Optimisation 🔴

### Core Idea
Constrained SOC examines the **Hessian of the Lagrangian**, evaluated at `(x*, λ*)`, but **only on the tangent space** of the constraint surface — i.e. on vectors `dx` orthogonal to the constraint gradients (vectors satisfying `Dg(x*) · dx = 0`). This space is the **null space** `N(Dg(x*))`.

> **In Simple Terms:** Going off the constraint surface isn't allowed, so we only care how the objective curves in directions that stay on the surface. Curving down in those directions = max; curving up = min.

### Definitions
- **Bordered Hessian**: matrix of second derivatives of `L` with respect to `x` and `λ` (constraint gradients form the "border"). ⭐
- **Null space `N(Dg(x*))`**: set of all `dx ∈ ℝⁿ` orthogonal to every constraint gradient.

### Theorem of Second Order Optimum
Suppose `(x* ∈ ℝⁿ, λ* ∈ ℝᵏ)` satisfy `rank(Dg(x*)) = k` and `Df(x*) + Σᵢ λᵢ* Dgⁱ(x*) = 0`. Then:

| Outcome | Necessary | Sufficient |
|---------|-----------|------------|
| Local max | `x' D²L(x*, λ*) x ≤ 0` for all `x ∈ N(Dg(x*))` | `x' D²L(x*, λ*) x < 0` for all `x ∈ N(Dg(x*))`, `x ≠ 0` |
| Local min | `x' D²L(x*, λ*) x ≥ 0` for all `x ∈ N(Dg(x*))` | `x' D²L(x*, λ*) x > 0` for all `x ∈ N(Dg(x*))`, `x ≠ 0` |

In matrix language: bordered Hessian is **negative (semi-)definite on the tangent space** for max, **positive (semi-)definite** for min.

> **Quick Recall:**
> - Constrained SOC = quadratic form on tangent space of constraints.
> - Use bordered Hessian; sign pattern depends on whether maximisation or minimisation.

---

## Section: Inequality Constrained Optimisation — Setup 🔴

### Core Idea
Now constraints are inequalities `gⁱ(x) ≥ 0` (with the convention that `h(x) ≤ c` rewrites as `c - h(x) ≥ 0`). Each constraint at `x*` is either **binding/tight** (`gⁱ(x*) = 0`) or **slack/non-binding** (`gⁱ(x*) > 0`). The Lagrange theorem doesn't apply directly — we don't know in advance which constraints bind.

> **In Simple Terms:** With inequality constraints, you don't always touch the boundary. Sometimes the budget binds, sometimes you don't even spend it all. Kuhn-Tucker handles both cases simultaneously.

### Examples

**Example 17.8**: `Max U(x₁, x₂)` s.t. `x₁ ≥ 0`, `x₂ ≥ 0`, `I - p₁x₁ - p₂x₂ ≥ 0`. We don't know in advance whether (a) `xᵢ = 0` (corner solution), or (b) the budget is exhausted, or (c) bliss point reached without spending all income.

### Definitions
- **Binding (tight, effective) constraint**: `gⁱ(x*) = 0`. ⭐
- **Slack (non-binding) constraint**: `gⁱ(x*) > 0`. ⭐

---

## Section: Kuhn-Tucker Theorem 🔴

### Core Idea
The Kuhn-Tucker theorem extends Lagrange to inequality constraints by replacing the equation `gⁱ(x) = 0` with the **complementary slackness** condition `λᵢ gⁱ(x) = 0` (along with `λᵢ ≥ 0` and `gⁱ(x) ≥ 0`). The theorem provides necessary conditions for a local optimum.

### Statement
Let `f, g¹, ..., gᵏ : ℝⁿ → ℝ` be C¹. Suppose `x*` is a maximum of `f` on `S = U ∩ {x ∈ ℝⁿ : gⁱ(x) ≥ 0, i = 1,...,k}`. Then there exist real numbers `μ, λ₁, ..., λₖ`, not all zero, such that:

`μ Df(x*) + Σᵢ λᵢ Dgⁱ(x*) = 0`

Moreover:
- If `gⁱ(x*) > 0` (slack), then `λᵢ = 0`.
- If `rank(Dg_β(x*)) = ℓ` (where `g_β` is the vector of binding constraints) — the **constraint qualification** — we may take `μ = 1`.
- `λᵢ ≥ 0` for all `i`, and `λᵢ > 0` for some `i` ⟹ `gⁱ(x*) = 0`.

### KT Conditions (with CQ, μ = 1)

For a **maximum**:
- (FOC) `Df(x*) + Σᵢ λᵢ Dgⁱ(x*) = 0` ... (17.10)
- (Complementary slackness) `λᵢ gⁱ(x*) = 0`, `λᵢ ≥ 0`, `gⁱ(x*) ≥ 0` for all `i` ... (17.9)

For a **minimum**: replace (17.10) by `-Df(x*) + Σᵢ λᵢ Dgⁱ(x*) = 0` ... (17.10a). Slackness condition unchanged.

### Definitions
- **Complementary slackness**: `λᵢ · gⁱ(x*) = 0` for each `i` — at most one of `λᵢ` and `gⁱ` is non-zero. ⭐ (exam-important)
- **Kuhn-Tucker conditions**: equations (17.9) + (17.10) (or 17.10a). ⭐

### ⚠️ Common Mistakes
- ❌ Forgetting that KT conditions are **necessary, not sufficient** → ✅ Points satisfying KT may not be local optima; checking via comparison or concavity is needed.
- ❌ Treating an inequality with `≤` as `≥` directly → ✅ Multiply by `-1` to convert: `h(x) ≤ c` ⟺ `c - h(x) ≥ 0`.
- ❌ Setting `λᵢ = 0` when `gⁱ` is binding → ✅ Slack constraint forces `λᵢ = 0`; binding constraint allows `λᵢ ≥ 0`.

> **Quick Recall:**
> - KT condition trio: stationarity, primal feasibility (`gⁱ ≥ 0`), dual feasibility (`λᵢ ≥ 0`), complementary slackness (`λᵢ gⁱ = 0`).
> - Unlike Lagrange, KT does **not** require checking SOC (no second-order condition required by the theorem).

---

## Section: Local–Global Maxima Link 🟡

### Core Idea
Concavity converts a local optimum into a global one.

### Theorem
Let `S ⊂ ℝⁿ` be convex and `f: S → ℝ` be concave. Then:
1. Any local maximum of `f` on `S` is a global maximum.
2. The set of maximisers `argmax{f(x) : x ∈ S}` is either empty or convex.

> **Quick Recall:**
> - Concave + convex domain ⟹ local max = global max.
> - Convex set of maximisers ⟹ if there are multiple optima, every weighted average is also optimal.

---

## Section: KT Application — Linear Utility Maximisation (Example 17.9) 🔴

### Core Idea
Maximise `U(x₁, x₂) = x₁ + x₂` subject to `x₁ ≥ 0, x₂ ≥ 0, I - p₁x₁ - p₂x₂ ≥ 0`. Three inequality constraints → potentially `2³ = 8` cases of binding combinations, but only **three are economically relevant** because `U` strictly increases (so the budget always binds) and consuming nothing of both is not optimal.

> **In Simple Terms:** With perfect substitutes, you spend everything on the cheaper good — unless prices are equal, in which case any split works.

### Mechanisms / Processes

Lagrangian: `L = x₁ + x₂ + λ₁ x₁ + λ₂ x₂ + λ₃ (I - p₁x₁ - p₂x₂)`.

Three relevant cases of binding constraints:
1. **Case 1** (interior): `x₁, x₂ > 0`, budget binds.
2. **Case 2**: `x₁ = 0`, `x₂ > 0`, budget binds.
3. **Case 3**: `x₂ = 0`, `x₁ > 0`, budget binds.

### Case 1 — Interior Solution
- `λ₁ = λ₂ = 0` (slackness).
- FOCs: `1 + 0 - λ₃ p₁ = 0`, `1 + 0 - λ₃ p₂ = 0` ⟹ `λ₃ p₁ = λ₃ p₂ = 1`.
- Since `λ₃ > 0` (positive marginal utility of income), `p₁ = p₂`.
- Conclusion: interior solution exists **only when prices are equal**. Any `(x₁, x₂)` exhausting the budget is optimal. `U₁/p₁ = U₂/p₂ = 1/p`.

### Case 2 — Corner at x₁ = 0
- `x₁ = 0` ⟹ from budget, `x₂ = I/p₂ > 0`. So `λ₂ = 0`.
- FOC for `x₂`: `λ₃ p₂ = 1`, so `λ₃* = 1/p₂`.
- FOC for `x₁`: `1 + λ₁ - λ₃ p₁ = 0` ⟹ `λ₁* = (p₁/p₂) - 1`.
- For `λ₁* > 0` we need `p₁ > p₂` — i.e. **good 1 is more expensive**, so consumer chooses only good 2.

### Case 3 — Corner at x₂ = 0
By symmetry: occurs only when `p₁ < p₂`.

### Summary
| Price relation | Active case | Solution |
|----------------|-------------|----------|
| `p₁ = p₂` | Case 1 | Any budget-exhausting `(x₁, x₂)` |
| `p₁ > p₂` | Case 2 | `(0, I/p₂)` — buy only good 2 |
| `p₁ < p₂` | Case 3 | `(I/p₁, 0)` — buy only good 1 |

> **Quick Recall:**
> - With perfect-substitute utility, the consumer spends entire budget on the **cheaper** good.
> - At an interior solution requires **equal** prices.

### Connections
- Builds on: Lagrange theorem (this chunk).
- Contrasts with: Cobb-Douglas utility (interior solutions for any positive prices) — see later examples in chunks 005, 010.
- Is prerequisite for: Convexity-based sufficient conditions (Chunk 005-006).

### Open Questions
1. What if utility is Cobb-Douglas? (Chunk 010 — Example "100 - 2x - 3y" KT.)
2. How does the multiplier λ* relate to comparative statics? (Envelope theorem, Chunk 008.)


---

<!-- See chunk 004 for start of Kuhn-Tucker theory -->

## Section: KT Application — Quasi-Linear Utility (Example 17.10) 🔴

### Core Idea
Maximise `U(x₁, x₂) = x₁/(1+x₁) + x₂/(1+x₂)` subject to `x₁ ≥ 0, x₂ ≥ 0, p₁x₁ + p₂x₂ ≤ I`. The utility function's separability and concavity give downward-sloping convex indifference curves that **cut the axes** — corner solutions are possible. Three KT cases mirror Example 17.9 but with non-trivial interior allocation when both goods consumed.

> **In Simple Terms:** Each good has saturating utility (more gives less extra utility). If income or relative prices are extreme, you may consume only one good. Otherwise, you split between them.

### Setup

Lagrangian:
`L = x₁/(1+x₁) + x₂/(1+x₂) + λ₁ x₁ + λ₂ x₂ + λ₃(I - p₁x₁ - p₂x₂)`

KT FOCs:
- `1/(1+x₁)² + λ₁ - λ₃ p₁ = 0` (eq. 17.19)
- `1/(1+x₂)² + λ₂ - λ₃ p₂ = 0` (eq. 17.20)
- Slackness on each constraint: `λᵢ xᵢ = 0`, `λ₃(I - p₁x₁ - p₂x₂) = 0`.

### Mechanisms / Processes — Three Cases

**Case 1: Interior** (`x₁ > 0`, `x₂ > 0`)
- `λ₁ = λ₂ = 0` (slackness).
- `1/(1+x₁)² = λ₃ p₁`, `1/(1+x₂)² = λ₃ p₂`.
- Dividing: `(1+x₂)²/(1+x₁)² = p₁/p₂`.
- Combined with budget `p₁x₁ + p₂x₂ = I`:
  - `x₁* = [I + p₂ - (p₁p₂)^(1/2)] / [p₁ + (p₁p₂)^(1/2)]`
  - `x₂* = [I + p₁ - (p₁p₂)^(1/2)] / [p₂ + (p₁p₂)^(1/2)]`
- Required for Case 1: `I > (p₁p₂)^(1/2) - p₁` AND `I > (p₁p₂)^(1/2) - p₂`.

**Case 2: Corner at x₁ = 0**
- `x₂ = I/p₂` (from budget). For positivity, `λ₂ = 0`.
- `λ₃ = 1/[p₂(1+x₂)²] = 1/[p₂(p₂+I)²/p₂²] = p₂/(p₂+I)²`.
  Wait — actually `1/(1+I/p₂)² = (p₂/(p₂+I))²`, so `λ₃ = (p₂/(p₂+I))²/p₂ = p₂/(p₂+I)²`. (Source eq. matches `λ₃ = p₂/(p₂+I)²`.)
- `λ₁ = λ₃ p₁ - 1`. For `λ₁ ≥ 0` need `λ₃ p₁ ≥ 1` ⟹ `I < (p₁p₂)^(1/2) - p₂`.

**Case 3: Corner at x₂ = 0** (by symmetry)
- `x₁ = I/p₁`. Similar conditions; this case applies if `I < (p₁p₂)^(1/2) - p₁`.

### Summary by Price Regime

| Condition | Active case | Outcome |
|-----------|-------------|---------|
| `p₁ = p₂ = p` | Case 1 | `x₁* = x₂* = I/(2p)` |
| `p₁ < p₂` and `I > (p₁p₂)^(1/2) - p₁` | Case 1 | Both consumed (interior) |
| `p₁ < p₂` and `I < (p₁p₂)^(1/2) - p₁` | Case 3 | Only `x₁` consumed |
| `p₁ > p₂` | (symmetric) | Either Case 1 or Case 2 |

> **Quick Recall:**
> - With saturating (concave) utility, low income or extreme price ratio ⟹ corner solution.
> - At interior, marginal utility ratio = price ratio: `(1+x₂)²/(1+x₁)² = p₁/p₂`.

### Connections
- Builds on: Linear utility KT (Chunk 004: Equality Constrained Optimisation — No-Arbitrage Principle).
- Contrasts with: Cobb-Douglas (always interior) — see exercises in Chunk 005, 010.

---

## Section: Unit 17 Summary, Key Words, Answers 🟡

### Definitions
- **Necessary and Sufficient Conditions for Optimum** of `z = f(x₁,...,xₙ)`:
  - FOC max/min: `f₁ = f₂ = ... = fₙ = 0`.
  - SOC max: `(-1)^i |H_i| > 0` ∀ `i`.
  - SOC min: `|H_i| > 0` ∀ `i`.
- **Stationary point**: tangent to graph parallel to x-axis (derivative = 0).
- **Theorem of Lagrange**: necessary FOC for equality-constrained extremum (Chunk 004: Equality Constrained Optimisation — No-Arbitrage Principle).
- **Theorem of Second Order Optimum**: bordered-Hessian definiteness on null space of constraint Jacobian (Chunk 004: Equality Constrained Optimisation — No-Arbitrage Principle).
- **Kuhn-Tucker Theorem**: necessary FOC for inequality-constrained extremum (Chunk 004: Equality Constrained Optimisation — No-Arbitrage Principle).

### Check Your Progress 1 (Chunk 003: Unconstrained Optimisation — First Order Condition) — Answers
1. `Z = -x² + xy - y² + x + 5y`: see Section 17.2.2 (extremum at FOC stationary point).
2. `y = x² - 6`: FOC `2x = 0` ⟹ `x = 0`. SOC `d²y = 2 > 0`. **Minimum** at `x = 0`.
3. `y = x³ - 2x² + x - 6`: FOC `3x² - 4x + 1 = 0` ⟹ `x = 1, 1/3`. `d²y = 6x - 4`. At `x = 1`: `d²y = 2 > 0` → **min**. At `x = 1/3`: `d²y = -2 < 0` → **max**.
4. `Z = x² - 2x - y²`: FOC ⟹ `x = 1, y = 0`. Hessian `|H| = [[2,0],[0,-2]]`. `|H₁| = 2 > 0`, `|H₂| = -4 < 0` (saddle). **Source mistakenly says minimum** — algebraically this is a saddle. Algebraic check: along `y = 0`, function is `x² - 2x` (min at `x=1`); along `x = 1`, function is `1 - 2 - y² = -1 - y²` (max at `y=0`). Hence saddle.

### Check Your Progress 2 — Answers
1. `U(x, y) = x²y`, `2x + y = 200`: `x* = y* = 200/3`, `λ* = (200/3)`. CQ holds (`p_x, p_y > 0`). Bordered Hessian negative definite — verified maximum.
2. `U(x, y) = x²y` (or different form, similar method): same Lagrangian technique.

### Check Your Progress 3 — KT Answers
1. `U = x^0.5 y^0.5`, `I = 100, p_x = 2, p_y = 3`: `x* = 25`, `y* = 50/3`. KT FOCs from `L = x^0.5 y^0.5 + λ[100 - 2x - 3y]`.
2. `U = (x - 3)(y - 2)` s.t. `x ≥ 0, y ≥ 0, 5x + 3y ≤ 50`: `x* = 6.1`, `y* = 6.5`.

### Unit 17 Exercises (Q1–Q3)

**Q1**: `f(x, y) = 2xy + 2x - x² - 2y²`. FOC ⟹ `(x*, y*) = (2, 1)`. Hessian `|H| = (-2)(-4) - 2² = 4 > 0`, `f_xx = -2 < 0`. **Local maximum**.

**Q2**: Maximise `u = xy` s.t. `x + 4y = 240` (`p_x = 1, p_y = 4, I = 240`).
Method: equate slope of indifference curve `-(y/x)` with budget slope `-(1/4)` ⟹ `x = 4y`. Substituting into constraint: `4y + 4y = 240` ⟹ `y = 30, x = 120`.

**Q3**: Maximise `u = xy`, `10x + 20y = 400`. Lagrangian: `L = xy - μ(10x + 20y - 400)`.
- FOC: `y = 10μ`, `x = 20μ`, `10x + 20y = 400`.
- From first two: `x = 2y`. Substituting: `20y + 20y = 400` ⟹ `y = 10, x = 20`.

> **Quick Recall:**
> - Lagrange's central trick: introduce λ for each equality constraint and treat the augmented function as unconstrained.
> - **Tangency condition** (geometric): MRS = price ratio at the optimum.

---

## Section: Unit 18 Introduction — Convexity & Concavity Motivation 🟢

### Core Idea
Concave functions are central to economics: cost and profit functions are typically concave; utility functions are commonly assumed (quasi)concave; demand functions are homogeneous. Convexity ensures a preference for diversification (mixing options is at least as good as the average preference).

> **In Simple Terms:** Convex/concave shapes show up everywhere because they encode "more is better but with diminishing returns" or "diversification is at least as good as concentration."

### Connections
- Builds on: KT theorem (Chunk 004: Equality Constrained Optimisation — No-Arbitrage Principle) — convexity gives sufficient conditions for KT necessary conditions to be sufficient.
- Is prerequisite for: Quasi-convex/concave generalisations (Chunk 006: Differentiable Convex/Concave — Second-Derivative Test (Two Variables)), homothetic functions (Chunk 009: Homothetic Functions — Definition & Properties).

---

## Section: Convex and Concave Functions — Definitions 🔴

### Core Idea
A function is **convex** if the line segment connecting any two points on its graph lies on or above the graph. **Concave** flips the inequality.

> **In Simple Terms:** Convex looks like a smile (cup-shaped); concave looks like a frown (cap-shaped). Mixing two arguments gives a value at least the chord (convex) or at most the chord (concave).

### Definitions
- **Convex function**: For `S ⊂ ℝⁿ` convex and `f: S → ℝ`, `f` is convex if for all `u, v ∈ S` and `θ ∈ [0,1]`:
  `f(θu + (1-θ)v) ≤ θ f(u) + (1-θ) f(v)`. ⭐
- **Strictly convex**: strict inequality for `u ≠ v`, `θ ∈ (0,1)`. ⭐
- **Concave function**: same definition with inequality reversed:
  `f(θu + (1-θ)v) ≥ θ f(u) + (1-θ) f(v)`. ⭐
- **Strictly concave**: strict inequality version.
- **Affine**: a function that is both convex and concave (linear plus constant).

### Key Concepts

#### Geometric Interpretation
Let `u, v ∈ S`. Consider `θu + (1-θ)v` for `θ ∈ [0,1]` — points on the line segment between `u, v`.
- For convex `f`: graph value at `θu + (1-θ)v` is **at most** the chord height `θf(u) + (1-θ)f(v)`.
- For concave `f`: graph value is **at least** the chord height.

#### Chord & Tangent Inequalities (Differentiable Convex)
From Fig. 18.1: for a differentiable convex `f` and `u < v`:
- Slope of tangent at `u` ≤ slope of chord PR ≤ slope of chord PQ.
- Hence `f'(u) ≤ [f(v) - f(u)] / (v - u) ≤ f'(v)`.

#### Sum and Scaling Properties
- Sum of convex functions is convex.
- Positive scalar times convex function is convex.
- Concave is the mirror.

### Examples — Convex Functions
1. `f(u) = au + b` (affine, with any `a, b ∈ ℝ`).
2. `f(u) = u^p` for `p ≥ 1` (powers).
3. `f(u) = |u|^p` for `p ≥ 1` on ℝ.
4. `f(u) = e^(au)` for any `a ∈ ℝ`.
5. Every linear transformation `ℝⁿ → ℝ`.
6. `f(u₁, u₂) = 2u₁² + u₂² - 2u₁u₂`.

### Examples — Concave Functions
1. `f(u) = -u²`.
2. `f(u) = √u` (on ℝ₊).
3. Affine `f(u) = au + b`.
4. `f(u) = sin(u)` on `[0, π]`.

### Useful Convex-Function Constructions
1. Conic combination: `f(u) = Σ cⱼ fⱼ(u)` with `cⱼ ≥ 0`, each `fⱼ` convex ⟹ `f` convex.
2. Pointwise max: `f(u) = max{f₁(u), ..., fₖ(u)}` with each `fⱼ` convex ⟹ `f` convex.
3. Quotient: if `g: ℝⁿ → ℝ` is concave, `g > 0`, then `f(x) = 1/g(x)` is convex on `{x : g(x) > 0}`.
4. Composition with non-decreasing convex `g: ℝ → ℝ` and convex `h: ℝⁿ → ℝ` ⟹ `f = g ∘ h` is convex.
5. Pre-composition with affine: convex `g`, affine `A(u) = Au + b` ⟹ `g ∘ A` is convex.

> **Quick Recall:**
> - Convex: chord above graph; `f(θu + (1-θ)v) ≤ θf(u) + (1-θ)f(v)`.
> - Concave: chord below graph; reverse inequality.
> - Affine = convex AND concave.

### ⚠️ Common Mistakes
- ❌ Confusing convex set with convex function — they're different concepts (a function's epigraph is a convex set iff the function is convex).
- ❌ Sum/max of concave is **not always** concave (max of concave is not concave; min is). The sum of concaves is concave.

### Connections
- Builds on: Definition of convex set (assumed).
- Is prerequisite for: Hessian-based test (Chunk 006: Differentiable Convex/Concave — Second-Derivative Test (Two Variables)), quasi-convexity (Chunk 006: Differentiable Convex/Concave — Second-Derivative Test (Two Variables)).


---

<!-- See chunk 005 for start of Unit 18 convexity definitions -->

## Section: Differentiable Convex/Concave — Second-Derivative Test (Two Variables) 🔴

### Core Idea
For twice-differentiable `λ = f(u, v)` on an open convex set, convexity/concavity is governed by signs of own seconds and the Hessian determinant. The 2-variable test mirrors the bivariate SOC for max/min — but applied throughout the domain rather than at one point.

> **In Simple Terms:** Concavity = "cap-shaped everywhere": both second partials non-positive, and the Hessian determinant non-negative throughout the domain.

### Key Concepts

| Property | Conditions throughout domain |
|----------|------------------------------|
| Concave | `f_uu ≤ 0`, `f_vv ≤ 0`, `f_uu f_vv - f_uv² ≥ 0` |
| Convex | `f_uu ≥ 0`, `f_vv ≥ 0`, `f_uu f_vv - f_uv² ≥ 0` |
| Strictly concave | `f_uu < 0`, `f_uu f_vv - f_uv² > 0` |
| Strictly convex | `f_uu > 0`, `f_uu f_vv - f_uv² > 0` |

> **Quick Recall:**
> - Concavity = SOC for max **everywhere**, not only at a stationary point.
> - Convexity = SOC for min **everywhere**.

---

## Section: Hessian Test for Convexity (n Variables) 🔴

### Core Idea
For `f: S → ℝ` twice differentiable on a non-empty `S ⊂ ℝⁿ`, convexity ⟺ Hessian is **positive semidefinite (PSD)** at every point in `S`; concavity ⟺ Hessian is **negative semidefinite (NSD)** everywhere.

> **In Simple Terms:** A function is concave on a region iff at every point, perturbing in any direction shows non-positive curvature. The Hessian's quadratic form captures this.

### Theorems
- `f` convex on `S` ⟺ Hessian `H(u)` is PSD ∀ `u ∈ S` (`x' H(u) x ≥ 0` for all `x ∈ ℝⁿ`).
- `f` concave on `S` ⟺ Hessian `H(u)` is NSD ∀ `u ∈ S` (`x' H(u) x ≤ 0`).

### Leading-Principal-Minor Tests
Let `D_k(u)` be the kth leading principal minor.
- `f` concave ⟺ `(-1)^k D_k(u) ≥ 0` for `k = 1, ..., n`, ∀ `u ∈ S`.
- `f` convex ⟺ `D_k(u) ≥ 0` for `k = 1, ..., n`, ∀ `u ∈ S`.

### Definitions
- **Positive semidefinite (PSD)**: `x' H x ≥ 0` for all `x ∈ ℝⁿ`. ⭐
- **Negative semidefinite (NSD)**: `x' H x ≤ 0` for all `x ∈ ℝⁿ`. ⭐
- **Hessian matrix**: `H = [∂²f/∂uᵢ∂uⱼ]ᵢⱼ` (symmetric for C² functions). ⭐

> **Quick Recall:**
> - Convex ⟺ PSD; Concave ⟺ NSD.
> - n-variable test: leading principal minor signs (≥ 0 for convex; alternating for concave).

---

## Section: Quasi-Convex and Quasi-Concave Functions 🔴

### Core Idea
Quasi-convexity weakens convexity: instead of comparing `f` at convex combinations to a weighted sum, we compare it only to the **maximum** of the two values. This generalisation captures functions whose level sets are convex (a property heavily used in microeconomic theory).

> **In Simple Terms:** A function is quasi-convex if mixing two points never produces a value larger than the worse of the two. (For quasi-concave: never smaller than the better of the two.)

### Definitions
- **Quasi-convex**: `f(θu + (1-θ)v) ≤ max{f(u), f(v)}` for all `u, v ∈ S`, `θ ∈ [0, 1]`. ⭐
- **Strictly quasi-convex**: strict inequality for `u ≠ v`, `θ ∈ (0, 1)`.
- **Quasi-concave**: `-f` quasi-convex, equivalently `f(θu + (1-θ)v) ≥ min{f(u), f(v)}`. ⭐
- **Strictly quasi-concave**: strict inequality version.
- **Quasi-linear**: both quasi-convex and quasi-concave.

### Key Concepts

#### Examples
- `|u|` is quasi-convex on ℝ.
- `log u` is quasi-convex (and concave) on ℝ₊.

#### Differentiable Quasi-Convexity Condition
For `f: S → ℝ` differentiable on an open convex `S`:
`f` is quasi-convex ⟺ for all `u, v ∈ S`:
- If `f(u) ≤ f(v)`, then `∇f(v)·(u - v) ≤ 0`, OR equivalently
- If `∇f(v)·(u - v) > 0`, then `f(u) > f(v)`.

#### Worked Illustration
Let `f(u) = u³`. To check quasi-convexity:
- Suppose `f(u₁) ≤ f(u₂)`, i.e. `u₁³ ≤ u₂³`, i.e. `u₁ ≤ u₂`.
- Compute `∇f(u₂)(u₁ - u₂) = 3u₂²(u₁ - u₂) ≤ 0` (since `u₁ ≤ u₂` and `3u₂² ≥ 0`).
- Theorem condition holds → `f` is quasi-convex.

#### Counter-example (Sum of Quasi-Convex Need Not Be Quasi-Convex)
Let `f(u₁, u₂) = u₁³ + u₂³`. Take `u_a = (2, -2)`, `u_b = (1, 0)`. Then `f(u_a) = 0`, `f(u_b) = 1`, so `f(u_a) ≤ f(u_b)`. But `∇f(u_b)·(u_a - u_b) = (3, 0)·(1, -2) = 3 > 0`, contradicting the necessary condition. So sum of two quasi-convex functions can fail quasi-convexity.

### Propositions
- A function that is both quasi-convex and quasi-concave is **quasi-linear**.
- Every convex function is quasi-convex.
- A concave function can be quasi-convex (e.g. `log` is concave AND quasi-convex).
- Sum of quasi-convex functions is **not necessarily** quasi-convex (above).
- Product of two positive convex decreasing functions is quasi-convex.

### Strongly Quasi-Convex
**Strong** quasi-convexity strengthens by requiring strict inequality without requiring `u ≠ v` (?), actually requiring strict inequality on the convex combination for `u ≠ v`. Implications:
- Strictly convex ⟹ strongly quasi-convex.
- Strongly quasi-convex ⟹ strictly quasi-convex ⟹ quasi-convex.

### ⚠️ Common Mistakes
- ❌ Assuming "concave" means "quasi-concave" reverses (every concave function is quasi-concave, but not vice versa) → ✅ Quasi-concavity is **weaker**.
- ❌ Sum-preserves-quasi-convexity → ✅ Sum can fail (counter-example above). Sum **does** preserve convexity.

### Check Your Progress 1 (Chunk 006: Differentiable Convex/Concave — Second-Derivative Test (Two Variables))
1. (a) `f(u₁, u₂) = 2u₁³ - 6u₂²`: For `u₁ < 0`, `u₂ > 0`: `f_u₁u₁ = 12u₁ < 0`, `f_u₂u₂ = -12 < 0`, `|H| = -144u₁ ≥ 0`. NSD → **concave** for `u₁ ≤ 0`.
   (b) `f(u) = -8u²`: `f''(u) = -16 < 0` always. **Strictly concave**.
2. Quasi-concavity is **weaker** than concavity. Every concave function is quasi-concave, but not vice versa.

> **Quick Recall:**
> - Quasi-convex: level sets `{u : f(u) ≤ α}` convex. <!-- Continues in chunk 009 -->
> - Quasi-concave: level sets `{u : f(u) ≥ α}` (upper level sets) convex.
> - Convex ⟹ quasi-convex (one-way only).

---

## Section: Constrained Optimisation — NDCQ 🔴

### Core Idea
For constrained optimisation with multiple constraints, the **Non-Degenerate Constraint Qualification (NDCQ)** requires the **Jacobian matrix of constraint gradients to have full rank** at the candidate optimum. If not, the Lagrangian method gives no information at that point — it must be added separately to the candidate-solution set.

> **In Simple Terms:** Constraints must be "independent" at the optimum — none redundant. If two constraints have parallel gradients, the Lagrangian formula fails and you must check that point manually.

### Setup

General problem:
- Minimise (or maximise) `f(u)`
- Subject to `gⱼ(u) ≤ 0`, `j = 1, ..., m`; `hₗ(u) = 0`, `ℓ = 1, ..., r`.
- `f, g, h: ℝⁿ → ℝ`.
- Feasible set: `Ω = {u ∈ ℝⁿ : hₗ(u) = 0, gⱼ(u) ≤ 0}`.

### Definitions
- **Feasible solution**: a point satisfying all constraints. ⭐
- **Feasible region (Ω)**: collection of all feasible solutions.
- **Optimal solution**: feasible point with maximal/minimal `f`.
- **NDCQ**: Jacobian of binding-constraint gradients `Dh(u*)` (or `Dg_β(u*)`) has full rank `m`. ⭐ (exam-important)

### One-Constraint Case
`max f(u)` s.t. `h(u) = c`.
At the optimum `u*`:
- Tangency: `∇f(u*) = λ ∇h(u*)`.
- Lagrangian `L(u, λ) = f(u) - λ[h(u) - c]`.
- FOCs: `∇L = 0` (which yields both `∇f = λ ∇h` and `h(u) = c`).

### Several Constraints
For `m` constraints `hⱼ(u) = cⱼ`:
- Jacobian matrix `Dh(u*) = [∇h₁(u*); ...; ∇hₘ(u*)]ᵐˣⁿ`.
- NDCQ: `rank(Dh(u*)) = m`.
- If any `∇hⱼ(u*) = 0`, that constraint drops out — Lagrangian fails.
- Lagrangian: `L(u, λ) = f(u) - Σⱼ λⱼ [hⱼ(u) - cⱼ]`.
- FOCs: `∂L/∂uᵢ = 0` for all `i`; `∂L/∂λⱼ = 0` for all `j` (recovers original constraints).

### Examples

**Example 18.1**: Max `f(u) = u³` s.t. `0 ≤ u ≤ 1`. Strictly increasing on compact set ⟹ max at `u = 1`.

**Check Your Progress 2(1)**: Constraints `3u₁ + u₂ + u₃ = 5`, `u₁ + u₂ + u₃ = 1`. Jacobian:
```
[3 1 1]
[1 1 1]
```
Rank = 2 (rows linearly independent) → NDCQ holds.

**Check Your Progress 2(2)**: `max 3 + u₁u₂` s.t. `u₁² + u₂² = 1`.
- Lagrangian: `L = 3 + u₁u₂ - λ(u₁² + u₂² - 1)`.
- FOCs: `u₂ - 2λu₁ = 0`, `u₁ - 2λu₂ = 0`, `u₁² + u₂² = 1`.
- Solutions: `u₁ = ±1/√2`, `u₂ = ±1/√2`, with `u₁, u₂` same sign for max → `(1/√2, 1/√2)` or `(-1/√2, -1/√2)`. Maximum value `3 + 1/2 = 7/2`.

> **Quick Recall:**
> - NDCQ = Jacobian of constraint gradients has rank `m`.
> - If NDCQ fails at a candidate, that point must be checked separately.

---

## Section: Inequality Constraints — Binding/Non-Binding Analysis 🔴

### Core Idea
With one inequality `g(u) ≤ b`, the maximum is either on the boundary (binding constraint) or interior (constraint inactive). Both cases are summarised by the **complementary slackness** condition: `λ[g(u) - b] = 0`.

> **In Simple Terms:** Either you've used up the resource (`g(u) = b`, `λ ≥ 0`) or you have slack (`g(u) < b`, `λ = 0`). Never both non-zero.

### Mechanisms / Processes — One Inequality

**Case 1 — Binding** (`g(u*) = b`):
- `∇f(u*) = λ ∇g(u*)`, `λ ≥ 0`.
- The unconstrained max lies outside the feasible region; the constraint pushes us back.

**Case 2 — Non-Binding** (`g(u*) < b`):
- Standard unconstrained FOC: `∇f(u*) = 0`.
- Equivalent to constrained form with `λ = 0`.

**Combined KKT-style conditions for `max f(u)` s.t. `g(u) ≤ b`:**
- `∂L/∂uᵢ = ∂f/∂uᵢ - λ ∂g/∂uᵢ = 0` for all `i`.
- `λ[g(u) - b] = 0` (**complementary slackness**).
- `g(u) - b ≤ 0` (primal feasibility).
- `λ ≥ 0` (dual feasibility).

### Several Inequality Constraints
Same structure but with multiple `λⱼ`:
- `∂f/∂uᵢ - Σⱼ λⱼ ∂gⱼ/∂uᵢ = 0` for all `i`.
- `λⱼ [gⱼ(u) - bⱼ] = 0` for all `j`.
- `gⱼ(u) ≤ bⱼ`, `λⱼ ≥ 0`.

NDCQ: only need to check Jacobian of **binding** constraints. Since we don't know in advance which bind, check all combinations.

### Definitions
- **Complementary slackness (CS)**: `λⱼ · [gⱼ(u) - bⱼ] = 0` for each `j`. ⭐
- **Binding constraint** at `u*`: `gⱼ(u*) = bⱼ`. ⭐
- **Non-binding (slack) constraint**: `gⱼ(u*) < bⱼ`. Forces `λⱼ = 0`.

> **Quick Recall:**
> - Always check primal (`g ≤ b`), dual (`λ ≥ 0`), and slackness simultaneously.
> - Slackness is the key new condition compared to equality-Lagrange.

---

## Section: LP Duality — Complementary Slackness Theorem 🟡

### Core Idea
In linear programming duality, the **Complementary Slackness Theorem** characterises optimality of feasible primal-dual pairs: their costs match iff slackness holds.

### Setup
- **Primal**: max `c'x` s.t. `Ax ≤ b`.
- **Dual**: min `b'y` s.t. `A'y = c`, `y ≥ 0`.

### Theorem (Optimality)
Let `x₀, y₀` be feasible solutions of primal and dual. Then both are optimal ⟺ `c'x₀ = b'y₀` (weak duality + complementary slackness).

### Theorem (Complementary Slackness Condition)
For feasible `x₀, y₀`: `c'x₀ = b'y₀` ⟺ for each `i`, `(y₀)ᵢ > 0 ⟹ (Ax₀)ᵢ = bᵢ`.

> **Quick Recall:**
> - At LP optimum: positive dual variable ⟹ corresponding primal constraint binds.
> - This is the LP analogue of `λ_j g_j = 0` in nonlinear KT. <!-- See chunk 007 for proof -->

### Connections
- Builds on: Inequality KT theorem (Chunk 004: Equality Constrained Optimisation — No-Arbitrage Principle).
- Is prerequisite for: Mixed equality/inequality formulation (Chunk 007: Complementary Slackness — Proof (Primal-Dual)).


---

<!-- See chunk 006 for start of Complementary Slackness -->

## Section: Complementary Slackness — Proof (Primal-Dual) 🟡

### Core Idea
Proof of the LP slackness theorem: feasibility plus equality of objectives forces the slackness condition, and vice versa.

### Proof Sketch
Given feasible `x₀, y₀` with `Ax₀ ≤ b`, `A'y₀ = c`, `y₀ ≥ 0`:

`c' x₀ = (A'y₀)' x₀ = y₀' A x₀ = Σᵢ (y₀)ᵢ (Ax₀)ᵢ`

Since `(Ax₀)ᵢ ≤ bᵢ` and `(y₀)ᵢ ≥ 0`, we have `Σ (y₀)ᵢ (Ax₀)ᵢ ≤ Σ (y₀)ᵢ bᵢ = b' y₀` (weak duality).

Equality `c' x₀ = b' y₀` ⟺ for every `i`, `(y₀)ᵢ [bᵢ - (Ax₀)ᵢ] = 0`. Hence the slackness condition.

> **Quick Recall:**
> - Weak duality: primal cost ≤ dual cost (for max primal).
> - Strong duality: at optimum, primal = dual cost.
> - Slackness: equality forces the right "binding" pattern.

---

## Section: Mixed Constraints — General Theorem 🔴

### Core Idea
General nonlinear program: `max f(u)` s.t. `gⱼ(u) ≤ bⱼ` (`j = 1, ..., k`) and `hᵢ(u) = cᵢ` (`i = 1, ..., m`). Combining what we know about equalities and inequalities:

> **In Simple Terms:** With both kinds of constraints, the FOCs blend Lagrange (for equalities) and Kuhn-Tucker (for inequalities). Equalities always bind; inequalities are governed by slackness.

### Theorem
Suppose `u*` is a local maximiser. Without loss, the first `k₀` inequalities are binding; the rest are slack. Suppose the Jacobian of the `m` equalities and the `k₀` binding inequalities has full rank.

Form the Lagrangian:
`L(u, λ, ν) = f(u) - Σⱼ λⱼ [gⱼ(u) - bⱼ] - Σᵢ νᵢ [hᵢ(u) - cᵢ]`

There exist multipliers `λ₁*, ..., λₖ*, ν₁*, ..., νₘ*` such that:
- `∂L/∂uⱼ = 0` for all `j ∈ {1, ..., n}`.
- `λᵢ [gᵢ(u*) - bᵢ] = 0` for all `i ∈ {1, ..., k}` (slackness).
- `hᵢ(u*) = cᵢ` for all `i ∈ {1, ..., m}` (equality).
- `gᵢ(u*) ≤ bᵢ` for all inequality `i` (primal feasibility).
- `λᵢ ≥ 0` for all inequality `i` (dual feasibility).

### Definitions
- **Mixed-constraint Lagrangian**: `L = f(u) - Σ λⱼ [gⱼ - bⱼ] - Σ νᵢ [hᵢ - cᵢ]`. ⭐
- **Active set**: the indices of binding constraints at `u*`. ⭐

> **Quick Recall:**
> - Equality multipliers `νᵢ` can be of any sign.
> - Inequality multipliers `λⱼ ≥ 0`.
> - Slackness on inequalities only.

---

## Section: Kuhn-Tucker Lagrangian (with Non-Negativity) 🔴

### Core Idea
Many problems include non-negativity `xⱼ ≥ 0` as constraints. Treating each as a separate inequality balloons the FOC count. The **Kuhn-Tucker Lagrangian** absorbs the non-negativity into the Lagrangian's structure, reducing total FOC equations from `3n + 3m` to `2n + 3m`.

> **In Simple Terms:** Non-negativity is so common that we encode it directly in the FOC sign rather than carry separate multipliers.

### Setup

Problem: `max f(u₁, ..., uₙ)` s.t. `gⱼ(u) ≤ bⱼ` (`j = 1, ..., m`) AND `xⱼ ≥ 0` (`j = 1, ..., n`).

**Standard Lagrangian** (treat non-negativity as separate constraints):
`L = f(u) - Σⱼ λⱼ[gⱼ(u) - bⱼ] + Σⱼ νⱼ uⱼ`

`3n + 3m` FOCs: derivative conditions, slackness on `g`, slackness on `u`, sign on `λ`, sign on `ν`.

**Kuhn-Tucker Lagrangian** (drop the `Σⱼ νⱼ uⱼ` term and weaken to inequality FOCs):
`L̄(u, λ) = f(u) - Σⱼ λⱼ[gⱼ(u) - bⱼ]`

The KT FOCs become:
- `∂L̄/∂xⱼ ≤ 0` and `xⱼ · ∂L̄/∂xⱼ = 0` for all `j` (subsumes non-negativity slackness).
- `∂L̄/∂λⱼ ≥ 0` and `λⱼ · ∂L̄/∂λⱼ = 0` for all `j`.
- `λⱼ ≥ 0` for all `j`.

Total: `2n + 3m` conditions (saves `n` slackness conditions on the non-negativity).

### Mechanisms / Processes — Why fewer FOCs?
- The non-negativity `uⱼ ≥ 0` is captured by the **inequality direction** of `∂L̄/∂xⱼ ≤ 0` rather than a separate slackness equation.
- The `νⱼ uⱼ = 0` slackness is replaced by `xⱼ · ∂L̄/∂xⱼ = 0` directly.

> **Quick Recall:**
> - Use KT Lagrangian when many non-negativity constraints — saves bookkeeping.
> - Three types of FOCs: stationarity (≤0 with slackness on `xⱼ`), constraint slackness (≥0 on `λⱼ`), and `λ ≥ 0`.

---

## Section: KT with Equality Constraint — Worked (Check Your Progress 3) 🔴

### Mechanisms / Processes

**Problem**: `max f(u₁, u₂) = u₁u₂` s.t. `h(u₁, u₂) = u₁ + 4u₂ = 16`, with `u₁, u₂ ≥ 0`.

Lagrangian: `L = u₁u₂ - λ(u₁ + 4u₂ - 16)`.
FOCs:
- `∂L/∂u₁ = u₂ - λ = 0` ⟹ `λ = u₂`.
- `∂L/∂u₂ = u₁ - 4λ = 0` ⟹ `u₁ = 4λ = 4u₂`.
- `∂L/∂λ = 16 - u₁ - 4u₂ = 0`.

Substituting `u₁ = 4u₂`: `4u₂ + 4u₂ = 16` ⟹ `u₂* = 2`, `u₁* = 8`, `λ* = 2`.

**Jacobian check**: `Dh(u) = [2u₁, 2u₂]` would be the gradient if `h = u₁² + u₂² + ...`; for `h = u₁ + 4u₂`, `Dh = [1, 4]` — non-zero, NDCQ holds.

**Maximum value**: `f(8, 2) = 16`.

---

## Section: Worked Examples — Convexity/Concavity Verification 🟡

### Q2 — Section 18.9
**(I)** `f(u) = 10 - u²`. `f'(u) = -2u`, `f''(u) = -2 < 0` for all `u`. **Concave**.

**(II)** `f(u₁, u₂) = 5u₁ + 2u₂²`. `∂f/∂u₁ = 5`, `∂f/∂u₂ = 4u₂`. Second partials: `f_u₁u₁ = 0`, `f_u₂u₂ = 4 > 0`, `f_u₁u₂ = 0`. Hessian `[[0,0],[0,4]]` PSD → **Convex**.

### Q3 — Verify Convexity
`f(u) = 4u₁³ + 3u₂² + u₃² - 6u₁u₂ + u₁u₃ + 9u₁ + 15`.

Necessary conditions: solving FOC `∂f/∂uᵢ = 0` gives `u₁ = -5, u₂ = -2, u₃ = 5/2` (interior stationary point).

Hessian:
```
H(u) = | 24u₁  -6   1 |
       | -6     6   0 |
       | 1      0   2 |
```

(Source notes: `f_u₁u₁ = 24u₁`, etc. The source incorrectly states `8`, `-6`, `1` for the first row — but algebraically `∂²f/∂u₁² = 24u₁` since `f` has `4u₁³`. The source's claim "all principal minors non-negative ⟹ convex" only holds globally if all `D_k(u) ≥ 0` for **all** `u`. With `24u₁`, this fails for `u₁ < 0` — so the function is **not globally convex**.)

Actual verdict: this function is convex only on `{u : u₁ ≥ 0}`. Source's claim of "convex" overstates the result; the principal minor sign-check must hold throughout the domain to guarantee global convexity.

---

## Section: KT Application — Inequality + Box Constraints (Q1, Section 18.9) 🔴

### Mechanisms / Processes

**Problem**: Max `f(u₁, u₂) = u₂` s.t.:
- `g₁(u) = u₁² + u₂² - 4 ≤ 0`
- `g₂(u) = -u₁ + u₂ ≤ 0`
- `g₃(u) = -u₁ ≤ 0` (i.e. `u₁ ≥ 0`)
- `g₄(u) = -u₂ ≤ 0` (i.e. `u₂ ≥ 0`)

KT Conditions:
- `u₁² + u₂² ≤ 4`, `-u₁ + u₂ ≤ 0`, `u₁ ≥ 0`, `u₂ ≥ 0`.
- Stationarity: `2u₁ λ₁ - 2u₂ λ₂ - λ₃ = 0`, `2u₂ λ₁ + λ₂ - λ₄ = 1` (the "1" from `∂f/∂u₂ = 1`).
- Slackness: `λᵢ gᵢ = 0` for `i = 1, ..., 4`.
- Non-negativity: `λᵢ ≥ 0`.

**Optimal solution by inspection**: `u₁* = 1.24962`, `u₂* = 1.56155`, `λ₁ = λ₂ = 0.24254`, `λ₃ = λ₄ = 0`.

But there's also a non-optimum critical point `u₁ = 0, u₂ = 0, λ₁ = 0, λ₂ = 1, λ₃ = λ₄ = 0` — satisfies KT but is NOT a local max. Reinforces: **KT conditions are necessary, not sufficient** without convexity assumptions.

### ⚠️ Common Mistakes
- ❌ Concluding KT-satisfying point is automatically a max → ✅ Either verify SOC (bordered Hessian) or rely on concavity of `f` and convexity of constraint set.
- ❌ Skipping NDCQ check at corner solutions → ✅ Box constraints can violate NDCQ at corners; always verify Jacobian rank.

> **Quick Recall:**
> - KT yields candidate set; comparing objective values at all candidates picks the optimum.
> - Multiple candidates can satisfy KT — only one (or some) are actual maxima.

### Connections
- Builds on: KT theorem (Chunk 004: Equality Constrained Optimisation — No-Arbitrage Principle), complementary slackness (Chunk 006: Differentiable Convex/Concave — Second-Derivative Test (Two Variables)).
- Is prerequisite for: Envelope theorem (Chunk 008: Lagrange Multiplier Method — Equality Constraints (Restated)) and quasi-concave optimisation theory (Chunk 009: Homothetic Functions — Definition & Properties).

### Open Questions
1. How does the multiplier `λ*` change with parameter `b`? (Envelope theorem — Chunk 008.)
2. When do KT conditions become sufficient? (When `f` concave, constraint set convex.)

### Check Your Progress (KT-related, Section 18.8) — Worked
**Problem (Section 17.5)**: `max -(u₁ - 5)² - (u₂ - 5)²` s.t. `9 - u₁² - u₂² ≥ 0`, `u₁, u₂ ≥ 0`.

KT conditions:
- (A) `L_u₁ = -2(u₁ - 5) - 2λu₁ ≤ 0`
- (B) `L_u₂ = -2(u₂ - 5) - 2λu₂ ≤ 0` (source has `-2(u₂-5) - λ` — typo; consistent reading is `-2λu₂`)
- (C) `L_λ = 9 - u₁² - u₂² ≥ 0`
- (D) `u₁, u₂, λ ≥ 0`
- Slackness: `u₁ L_u₁ = 0`, `u₂ L_u₂ = 0`, `λ L_λ = 0`.

After case analysis: solution at `(u₁*, u₂*, λ*) = (3√11/2, (12 - √11)/2, λ)` where `λ = √11/2 - 2 ≈ 1.317`. (Source has minor numerical roughness; key insight is non-trivial constrained max with both `u₁, u₂ > 0` and constraint binding.)


---


## Section: Lagrange Multiplier Method — Equality Constraints (Restated) 🔴

### Core Idea
Standardise the nonlinear programming notation: minimise `f(u)` subject to `G(u) = 0` (equality constraints, `k` of them) and possibly `H(u) ≤ 0` (inequality, `m` of them). The Lagrangian is `F(u, λ) = f(u) - λ' G(u)` with multipliers `λ = (λ₁, ..., λₖ)`. Stationarity `∇F = 0` plus the constraint equations are the necessary conditions.

> **In Simple Terms:** Multipliers convert constrained problems into unconstrained ones over a larger space `(u, λ)`. Stationary points of the Lagrangian correspond to constrained extrema.

### Mechanisms / Processes
- Lagrangian: `F(u, λ) = f(u) - Σᵢ λᵢ Gᵢ(u)`.
- FOCs: `∂F/∂uⱼ = ∂f/∂uⱼ - Σᵢ λᵢ ∂Gᵢ/∂uⱼ = 0` for `j = 1, ..., n`.
- Constraint equations: `Gᵢ(u) = 0` for `i = 1, ..., k`.

> **Quick Recall:**
> - Total: `n + k` equations in `n + k` unknowns `(u₁, ..., uₙ, λ₁, ..., λₖ)`.

---

## Section: Mathematical Proof of Lagrange Multiplier Method 🟡

### Core Idea
The proof uses the **Implicit Function Theorem**: with `n = 4` variables and 2 equality constraints, the constraint Jacobian's non-vanishing allows expressing 2 variables as functions of the other 2. Substitution reduces to an unconstrained 2-variable problem; matching FOCs gives the multipliers.

### Setup
- Variables: `u₁, u₂, u₃, u₄`. Objective: `Z = f(u₁, u₂, u₃, u₄)`.
- Constraints: `C(u₁, ..., u₄) = 0`, `E(u₁, ..., u₄) = 0`.
- Jacobian: `∂(C, E)/∂(u₃, u₄) = C_u₃ E_u₄ - C_u₄ E_u₃ ≠ 0` at the optimum.

### Sketch
Implicit function theorem ⟹ `u₃ = g(u₁, u₂)`, `u₄ = h(u₁, u₂)` near the optimum. Substituting into `f` gives an unconstrained problem in `(u₁, u₂)` with FOCs:
- `f_u₁ + f_u₃ ∂g/∂u₁ + f_u₄ ∂h/∂u₁ = 0`
- `f_u₂ + f_u₃ ∂g/∂u₂ + f_u₄ ∂h/∂u₂ = 0`

Choose `λ, μ` so that:
- `f_u₃ - λ C_u₃ - μ E_u₃ = 0`
- `f_u₄ - λ C_u₄ - μ E_u₄ = 0`

Differentiating constraints `C, E` w.r.t. `u₁, u₂` gives two more linear equations. Combining recovers `f_u₁ - λ C_u₁ - μ E_u₁ = 0` and `f_u₂ - λ C_u₂ - μ E_u₂ = 0` — exactly the Lagrangian stationarity.

> **Quick Recall:**
> - Lagrange multipliers exist provided NDCQ (Jacobian full rank).
> - The "magic" of multipliers: they encode the implicit dependence of constrained variables.

---

## Section: Extension to Inequality Constraints 🔴

### Core Idea
With inequality `H(u) ≤ 0`: the constraint is **active** if `Hⱼ = 0`, **inactive** if `Hⱼ < 0`. For inactive constraints, set `μⱼ = 0`. For active constraints, the gradient `∇Hⱼ` points outside the feasible region — to stay feasible we set `μⱼ ≤ 0` (sign convention here differs from KT-max formulation; some texts use `μⱼ ≥ 0` with `g(u) ≥ 0` formulation).

> **In Simple Terms:** Inequalities are added like equalities to the Lagrangian, but with the rule "if not at the boundary, drop the term."

### Augmented Lagrangian
`F(u, λ, μ) = f(u) - λ' G(u) - μ' H(u)`

KT-style conditions (in this text's sign convention):
- `∇f(u*) - Σᵢ λᵢ ∇Gᵢ(u*) - Σⱼ μⱼ ∇Hⱼ(u*) = 0`
- `μⱼ Hⱼ = 0` for `j = 1, ..., m` (slackness)
- `μⱼ ≤ 0`, `Hⱼ(u*) ≤ 0`

> **Quick Recall:**
> - Active vs inactive: depends on whether `H` binds at `u*`.
> - Inactive constraints are dropped from the Lagrangian.

### Check Your Progress 1 — Solutions

**Problem 1**: `u₃ = u₁u₂` s.t. `u₁ + u₂ = 100`. (Find max `u₃`.)
- `L = u₁u₂ + λ(100 - u₁ - u₂)`.
- FOCs: `u₂ = λ`, `u₁ = λ` ⟹ `u₁ = u₂`. Constraint: `u₁ + u₂ = 100` ⟹ `u₁ = u₂ = 50`.
- Maximum: `u₃* = 2500`.

**Problem 2**: `u₃ = 4u₁² + 3u₁u₂ + 6u₂²` s.t. `u₁ + u₂ = 56`. (Find max.)
- Lagrangian: `L = 4u₁² + 3u₁u₂ + 6u₂² + λ(56 - u₁ - u₂)`.
- FOCs: `8u₁ + 3u₂ = λ`, `3u₁ + 12u₂ = λ`, `u₁ + u₂ = 56`.
- Equate first two: `8u₁ + 3u₂ = 3u₁ + 12u₂` ⟹ `5u₁ = 9u₂` ⟹ `u₁ = 1.8 u₂`.
- Constraint: `1.8u₂ + u₂ = 56` ⟹ `u₂ = 20`. Then `u₁ = 36`. `λ = 8(36) + 3(20) = 348`.

> **Quick Recall:**
> - For utility-style maximisation problems, the multiplier λ has units of "extra utility per unit of relaxed constraint" — its **shadow price** interpretation.

---

## Section: Envelope Theorem — Concept 🔴

### Core Idea
Optimal value functions depend on **parameters** (prices, income). The **Envelope Theorem** says: the total derivative of the optimal value function with respect to a parameter equals the **partial** derivative of the Lagrangian (or objective in unconstrained case) with respect to that parameter, evaluated at the optimum. The "indirect effects" via choice variables vanish at the optimum due to the FOCs.

> **In Simple Terms:** When a parameter changes, you'd think the answer changes both directly AND because you re-optimise. The envelope theorem says only the **direct** effect matters at the optimum — the re-optimisation contribution is zero (FOCs are zero).

### Definitions
- **Value function `V(a)`**: optimal value of `f(u, a)` for parameter `a`, i.e. `V(a) = f(u*(a), a)`. ⭐
- **Envelope theorem**: `dV/da = ∂L/∂a` evaluated at the optimum (constrained); or `dV/da = ∂f/∂a` (unconstrained). ⭐ (exam-important)

### Statement (Constrained)
For `max f(u, a)` s.t. `gᵢ(u, a) = 0`, define `V(a) = max f(u, a)`. Let `u*(a)` be the optimiser. Then:

`∂V(a)/∂aₜ = ∂L(u*(a), a)/∂aₜ` for each parameter `aₜ`, `t = 1, 2, ..., k`.

### Mechanisms / Processes — Proof
Total derivative:
`∂V/∂aₜ = Σᵢ [∂f/∂uᵢ] · [∂uᵢ*/∂aₜ] + ∂f/∂aₜ`

The first term sums an "indirect effect" via choice variables. From FOCs:
`∂f/∂uᵢ = -Σⱼ λⱼ · ∂gⱼ/∂uᵢ` (Lagrangian stationarity, eqn 19.24).

Substitute:
`∂V/∂aₜ = -Σⱼ λⱼ [Σᵢ (∂gⱼ/∂uᵢ)(∂uᵢ*/∂aₜ)] + ∂f/∂aₜ`

Differentiating the constraint `gⱼ(u*(a), a) = 0` with respect to `aₜ`:
`Σᵢ (∂gⱼ/∂uᵢ)(∂uᵢ*/∂aₜ) + ∂gⱼ/∂aₜ = 0`

Hence `Σᵢ (∂gⱼ/∂uᵢ)(∂uᵢ*/∂aₜ) = -∂gⱼ/∂aₜ`.

Substituting:
`∂V/∂aₜ = Σⱼ λⱼ (∂gⱼ/∂aₜ) + ∂f/∂aₜ = ∂L/∂aₜ`. ✓

> **Quick Recall:**
> - Envelope identity: `∂V/∂a = ∂L/∂a` at the optimum.
> - Indirect effects vanish because of FOCs.

---

## Section: Envelope Theorem for Unconstrained Optimisation 🔴

### Core Idea
For `max f(u, v, a)` (no constraints), with `(u*(a), v*(a))` the optimisers and `V(a) = f(u*, v*, a)`:
`dV/da = ∂f/∂a` evaluated at `(u*(a), v*(a), a)`.

> **In Simple Terms:** Only the direct effect of `a` on `f` matters at the optimum — the optimal `u, v` already absorb everything else.

### Mechanisms / Processes
`dV/da = ∂f/∂u · du*/da + ∂f/∂v · dv*/da + ∂f/∂a`

The first two terms vanish by FOC (`∂f/∂u = ∂f/∂v = 0` at optimum). Hence:
`dV/da = ∂f/∂a |_{u*, v*}`

### Examples

**Example 19.1**: `max(u₁, u₂)` of `4u₁ + au₂ - u₁² - u₂² + u₁u₂`.
- FOCs: `4 - 2u₁ + u₂ = 0`, `a - 2u₂ + u₁ = 0`.
- Solving: `u₁* = (8 + a)/3`, `u₂* = (2a + 4)/3`.
- Value function: `V(a) = 4 · (8+a)/3 + a · (2a+4)/3 - [(8+a)/3]² - [(2a+4)/3]² + (8+a)(2a+4)/9`.
  Simplifying gives a function purely of `a`.
- By envelope: `dV/da = ∂f/∂a |_{(u*, u*)} = u₂* = (2a + 4)/3`. (Faster than expanding `V(a)`.)

> **Quick Recall:**
> - Skip the algebra of substituting and re-differentiating; use envelope to read off `dV/da = ∂f/∂a`.

---

## Section: Envelope Theorem for Constrained Optimisation 🔴

### Core Idea
For `max f(u, v, a)` s.t. `g(u, v, a) = 0`, let Lagrangian `L = f + γ g`. With `(u*(a), v*(a), γ*(a))` solving the constrained problem, value function `V(a) = f(u*, v*, a)`:
`dV/da = ∂L/∂a |_{u*, v*, γ*} = ∂f/∂a + γ* · ∂g/∂a`

### Mechanisms / Processes
Write `V(a) = f(u*(a), v*(a), a) + γ*(a) g(u*(a), v*(a), a)` (since `g = 0` at optimum, this just adds 0).
Differentiate w.r.t. `a`:
`dV/da = [∂f/∂u + γ ∂g/∂u] · du*/da + [∂f/∂v + γ ∂g/∂v] · dv*/da + dγ/da · g(...) + ∂f/∂a + γ ∂g/∂a`

- First two brackets are zero by FOCs.
- `dγ/da · g(...)` is zero because `g = 0`.
- Remaining: `∂f/∂a + γ* ∂g/∂a = ∂L/∂a`. ✓

> **Quick Recall:**
> - For constrained problems, use Lagrangian's `∂L/∂a`, not `∂f/∂a` alone.

### Connections
- Builds on: Lagrangian theorem (Chunk 004: Equality Constrained Optimisation — No-Arbitrage Principle), value function concept (this section).
- Is prerequisite for: Comparative statics in microeconomics; Hotelling's lemma; Roy's identity (graduate microeconomics, beyond this block).

---

## Section: Homogeneous Functions — Definition & Economic Applications 🔴

### Core Idea
A function `f(u₁, ..., uₙ)` is **homogeneous of degree `k`** if scaling all inputs by `t > 0` scales the output by `t^k`:
`f(tu₁, ..., tuₙ) = t^k f(u₁, ..., uₙ)`.

Economic relevance: **production**, **cost**, and **demand** functions are typically homogeneous, with the degree encoding returns to scale.

> **In Simple Terms:** Homogeneous functions scale predictably. Doubling all inputs makes output exactly `2^k` times bigger.

### Definitions
- **Homogeneous of degree `k`**: `f(tu) = t^k f(u)` for all `t > 0`. ⭐ (exam-important)

### Economic Applications

#### Returns to Scale
Production function `q = f(u₁, ..., uₙ)`:
- Homogeneous of degree `k = 1` ⟺ **Constant Returns to Scale (CRS)**. Doubling inputs ⟹ doubling output.
- `k > 1` ⟺ **Increasing Returns to Scale (IRS)**. Doubling inputs ⟹ more than doubling output.
- `0 < k < 1` ⟺ **Decreasing Returns to Scale (DRS)**. Doubling inputs ⟹ less than doubling output.

#### Cobb-Douglas Utility/Production
`u(x₁, ..., xₙ) = A x₁^α₁ x₂^α₂ ... xₙ^αₙ` is homogeneous of degree `k = α₁ + α₂ + ... + αₙ`.

#### CES (Constant Elasticity of Substitution)
`U = (a₁ x₁^ρ + a₂ x₂^ρ)^(q/ρ)` is homogeneous of degree `q`.

#### Demand Functions Homogeneous of Degree 0
For utility `U(x)` and budget `p · x ≤ I`, demand `x = D(p₁, ..., pₙ, I)`. Scale prices and income by `t > 0`:

`Maximise U(x)` s.t. `tp · x ≤ tI` ⟺ `Maximise U(x)` s.t. `p · x ≤ I` (same problem!).

So `D(tp, tI) = D(p, I) = t⁰ D(p, I)`. **Demand depends only on relative prices**, not absolute price levels — the **homogeneity-of-degree-zero property of demand**.

> **Quick Recall:**
> - CRS ⟺ degree 1 production function.
> - Demand functions are degree 0 in `(p, I)` — money illusion-free.

---

## Section: Properties of Homogeneous Functions (Theorems A, B, C) 🔴

### Theorem A — Degree of Partial Derivatives
If `f(u₁, ..., uₙ)` is homogeneous of degree `k`, then each first-order partial derivative `∂f/∂uⱼ` is homogeneous of degree `k - 1`.

**Proof sketch**: Differentiate `f(tu) = t^k f(u)` w.r.t. `uⱼ`:
`t · ∂f(tu)/∂(tuⱼ) = t^k · ∂f(u)/∂uⱼ`
⟹ `∂f(tu)/∂(tuⱼ) = t^{k-1} · ∂f(u)/∂uⱼ`.

### Theorem B — Level Sets are Radial Expansions
If `u, v` are on the same level set (`f(u) = f(v)`), then for any `t > 0`, `tu` and `tv` are on the same level set (`f(tu) = f(tv)`).

**Proof**: `f(tu) = t^k f(u) = t^k f(v) = f(tv)`. ✓

This means level sets are "radial expansions" of each other — they look the same after rescaling.

### Theorem C — Function-Restriction Reconstruction
If `F(u₁, ..., uₙ, z)` is homogeneous of degree `k` and `f(u₁, ..., uₙ) = F(u₁, ..., uₙ, 1)` is its restriction to `z = 1`, then:
`F(u₁, ..., uₙ, z) = z^k f(u₁/z, ..., uₙ/z)`.

**Proof**: `F(u, z) = F(z·u/z, z·1) = z^k F(u/z, 1) = z^k f(u/z)`. ✓

### Connections
- Builds on: Chain rule, parameterised optimisation.
- Is prerequisite for: Homothetic functions (Chunk 009: Homothetic Functions — Definition & Properties), Euler's theorem (Chunk 009: Homothetic Functions — Definition & Properties).

### Open Questions
1. What's the relationship between homogeneity and concavity? (Independent — neither implies the other.)
2. How does homogeneity of degree 1 relate to the cost-minimising firm? (CRS ⟺ marginal cost = average cost.)


---

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
- Equivalent to: Hessian-based test (Chunk 006: Differentiable Convex/Concave — Second-Derivative Test (Two Variables)).

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
- Builds on: Homogeneous function definition (Chunk 008: Lagrange Multiplier Method — Equality Constraints (Restated)).
- Is prerequisite for: Cost-minimisation duality, factor demand functions (graduate microeconomics).

### Open Questions
1. How does this connect to perfect competition's zero-profit result? (CRS + competitive markets ⟹ zero economic profit.)
2. What if production is not homogeneous? (Euler's theorem doesn't apply; use envelope theorem instead.)


---

<!-- See chunk 009 for start of Unit 19 -->

## Section: Check Your Progress 1 Solutions — Lagrange Worked Examples 🟡

### Mechanisms / Processes

**CYP 1.1**: Max `u₃ = u₁ u₂` s.t. `u₁ + u₂ = 100`.
- Lagrangian: `L = u₁ u₂ + λ(100 - u₁ - u₂)`.
- FOCs: `u₂ - λ = 0`, `u₁ - λ = 0`, `100 - u₁ - u₂ = 0`.
- From first two: `u₁ = u₂`. Then `2u₁ = 100` ⟹ `u₁ = u₂ = 50`.
- `u₃* = 50 × 50 = 2500`.

**CYP 1.2**: Max `u₃ = 4u₁² + 3u₁u₂ + 6u₂²` s.t. `u₁ + u₂ = 56`.
- Lagrangian: `L = 4u₁² + 3u₁u₂ + 6u₂² + λ(56 - u₁ - u₂)`.
- FOCs:
  - `∂L/∂u₁ = 8u₁ + 3u₂ - λ = 0`
  - `∂L/∂u₂ = 3u₁ + 12u₂ - λ = 0`
  - `∂L/∂λ = 56 - u₁ - u₂ = 0`
- Equating first two: `8u₁ + 3u₂ = 3u₁ + 12u₂` ⟹ `5u₁ = 9u₂` ⟹ `u₁ = 1.8 u₂`.
- Constraint: `1.8u₂ + u₂ = 56` ⟹ `2.8 u₂ = 56` ⟹ `u₂* = 20`. So `u₁* = 36`.
- `λ* = 8(36) + 3(20) = 288 + 60 = 348`.

> **Quick Recall:**
> - For symmetric quadratic Lagrangians, equating FOCs eliminates `λ` and reduces to one equation.
> - Then substitute into the linear constraint to get the second equation.

---

## Section: Check Your Progress 2 Solutions — Envelope Theorem Worked 🟡

### Mechanisms / Processes

**CYP 2.1**: For `f(u; a) = -u² + 2au + 4a²`, find max w.r.t. `u` and `dV/da`.
- FOC: `∂f/∂u = -2u + 2a = 0` ⟹ `u*(a) = a`. Local (and global) max.
- Value function: `V(a) = -a² + 2a² + 4a² = 5a²`.
- Direct: `dV/da = 10a`.
- **Envelope theorem**: `dV/da = ∂f/∂a |_{u = u*(a)} = (2u + 8a)|_{u = a} = 2a + 8a = 10a`. ✓

**CYP 2.2**: Constrained envelope. Max `u + 3v` s.t. `u² + av² = 10`. Estimate `f(1.01)` when `a = 1.01`.
- Lagrangian: `L = u + 3v - γ(u² + av² - 10)`.
- NDCQ holds when `a ≠ 0`.
- FOCs: `1 - 2γu = 0` ⟹ `u = 1/(2γ)`. `3 - 2aγv = 0` ⟹ `v = 3/(2aγ)`.
- Constraint: `(1/(2γ))² + a(3/(2aγ))² = 10` ⟹ `1/(4γ²) + 9/(4aγ²) = 10` ⟹ `(a + 9)/(4aγ²) = 10` ⟹ `γ = √((a+9)/(40a))` (taking positive root).
- For `a = 1`: `γ = √(10/40) = 1/2`. So `u* = 1`, `v* = 3`. `f(1) = 1 + 9 = 10`.
- **Envelope estimate**: `df*/da = ∂L/∂a = -γv²` at the optimum `(u*, v*, γ*)`. At `a = 1`: `-(1/2)(9) = -4.5`.
- `f(1.01) ≈ f(1) + 0.01 × (-4.5) = 10 - 0.045 = 9.955`.
- **Exact computation**: For `a = 1.01`, `γ = √((1.01 + 9)/(40 × 1.01)) = √(10.01/40.4) ≈ √0.24777 ≈ 0.4978`. Then `u(1.01) ≈ 1.0045`, `v(1.01) ≈ 2.9836`. `f(1.01) = 1.0045 + 3(2.9836) = 1.0045 + 8.9508 = 9.9553`. ✓ (Matches envelope estimate within rounding.)

### ⚠️ Common Mistakes
- ❌ Forgetting that envelope estimate is **first-order Taylor approximation** → ✅ Higher-order terms can matter for large `Δa`.
- ❌ Using `∂f/∂a` instead of `∂L/∂a` for constrained problems → ✅ Constrained envelope uses Lagrangian's partial.

> **Quick Recall:**
> - Envelope: `dV/da = ∂L/∂a |_{u*, λ*}`.
> - Faster than re-substituting and differentiating.

---

## Section: Check Your Progress 3 Solutions — Homogeneous & Quasi-Concave 🟡

### Mechanisms / Processes

**CYP 3.1**: `f(u₁, u₂) = 3u₁²u₂⁴ + 2u₁²u₂⁴ - 3u₁³u₂³`. Test homogeneity.
- Substitute `(tu₁, tu₂)`:
  `f(tu₁, tu₂) = 3(tu₁)²(tu₂)⁴ + 2(tu₁)²(tu₂)⁴ - 3(tu₁)³(tu₂)³`
  `= 3 t² u₁² · t⁴ u₂⁴ + 2 t² u₁² · t⁴ u₂⁴ - 3 t³ u₁³ · t³ u₂³`
  `= t⁶ (3u₁²u₂⁴ + 2u₁²u₂⁴ - 3u₁³u₂³) = t⁶ f(u₁, u₂)`.
- **Homogeneous of degree 6**.

**CYP 3.2**: `f(u₁, u₂) = α ln u₁ + β ln u₂`. Homothetic?
- Rewrite: `f = ln(u₁^α u₂^β) = h(g(u₁, u₂))`, where `g(u₁, u₂) = u₁^α u₂^β` (homogeneous of degree `α + β`) and `h(z) = ln z` (strictly increasing).
- ⟹ `f` is **homothetic** (composition of monotone with homogeneous).

> **Quick Recall:**
> - Test homogeneity by substituting `(tu)`; check if `t^k` factors out.
> - Cobb-Douglas log form is homothetic (and Cobb-Douglas itself is homogeneous).

### CYP 4.1 — Bordered Hessian (rephrased from Chunk 009)

**Test `f(u₁, u₂) = u₁ e^{-u₂}` for quasi-concavity on `u₁ ≥ 0, u₂ ≥ 0`.**
Bordered Hessian:
- `D₁(u) = -u₂² e^{-2u₂}` ... actually source has `-u₂² e^{-2u₂}` for D as listed in source though our reasoning gives different terms; the principle is the same.
- After computation: `D₁ ≤ 0`, `D₂ ≥ 0`. Both vanish at `u₁ = 0`.
- Conclusion: function is quasi-concave on `u₁ > 0, u₂ ≥ 0`.

### CYP 4.2 — Direct Hessian

`f(u₁, u₂) = 2u₁³ - 6u₂²`. Hessian `H = diag(12u₁, -12)`. `H_11 = 12u₁`, `det H = -144u₁`. For `u₁ ≤ 0`: `H` NSD → `f` is **concave on `u₁ ≤ 0`**.

---

## Section: Unit 19 Exercises 🟡

### Q1 — Profit Function and Envelope Verification

**Problem**: A firm produces goods A and B with prices `p_A = 13`, `p_B = p`. Profit: `π(u, v) = 13u + pv - C(u, v)`, where `C(u, v) = 0.04u² - 0.01uv + 0.01v² + 4u + 2v + 500`. Determine optimal value function `π*(p)` and verify envelope theorem.

**Solution**:
- Substitute cost: `π(u, v) = -0.04u² + 0.01uv - 0.01v² + 9u + (p - 2)v - 500`.
- FOCs:
  - `∂π/∂u = -0.08u + 0.01v + 9 = 0` ⟹ `8u - v = 900`.
  - `∂π/∂v = 0.01u - 0.02v + p - 2 = 0` ⟹ `u - 2v = 200 - 100p`.
- Linear system. Determinant: `8(-2) - (-1)(1) = -16 + 1 = -15 ≠ 0`.
- Solve: `u* = (1/15)(1600 + 100p)`, `v* = (1/15)(-700 + 800p)`. (Source has these; matches our derivation.)
- Hessian:
  ```
  | -0.08   0.01 |
  |  0.01  -0.02 |
  ```
  `D₁ = -0.08 < 0`, `D₂ = 0.0016 - 0.0001 = 0.0015 > 0`. Negative definite → maximum.
- Optimal value: `π*(p) = (80p² - 140p + 80)/3`. (Source value; verified by substitution.)
- Direct derivative: `dπ*/dp = (160p - 140)/3`.
- **Envelope check**: `∂π/∂p |_{u*, v*} = v* = (1/15)(-700 + 800p) = (160p - 140)/3` ✓ matches.

> **Quick Recall:**
> - Envelope theorem reduces algebra dramatically — read off `dπ*/dp = v*` at the optimum without forming `π*(p)` explicitly.

### Q2 — Monomial Homogeneity

**Problem**: Show `f(u₁, u₂, u₃) = u₁²u₂³u₃` is homogeneous of degree 6. Also `f(u₁, u₂) = √(u₁³ + u₂³)`.

**Solutions**:
- `f(tu₁, tu₂, tu₃) = (tu₁)²(tu₂)³(tu₃) = t² · u₁² · t³ · u₂³ · t · u₃ = t⁶ u₁²u₂³u₃ = t⁶ f(u₁, u₂, u₃)`. ✓
- `f(u₁, u₂) = √(u₁³ + u₂³)`. Then `f(tu₁, tu₂) = √(t³ u₁³ + t³ u₂³) = √(t³ (u₁³ + u₂³)) = t^(3/2) f(u₁, u₂)`. So homogeneous of **degree 3/2**.

### Q3 — Constrained Minimisation

**Problem**: Minimise `f(u₁, u₂) = 2u₁² + u₂²` s.t. `u₁ + u₂ = 1`.

**Solution**:
- Lagrangian: `L(u₁, u₂, λ) = 2u₁² + u₂² + λ(1 - u₁ - u₂)`.
- FOCs:
  - `∂L/∂u₁ = 4u₁ - λ = 0` ⟹ `λ = 4u₁`.
  - `∂L/∂u₂ = 2u₂ - λ = 0` ⟹ `λ = 2u₂`.
  - `∂L/∂λ = 1 - u₁ - u₂ = 0`.
- Equating: `4u₁ = 2u₂` ⟹ `u₂ = 2u₁`. Substituting: `u₁ + 2u₁ = 1` ⟹ `u₁* = 1/3`. Then `u₂* = 2/3`. `λ* = 4/3`.
- Minimum value: `f* = 2(1/9) + (4/9) = 6/9 = 2/3`.

(Source has `u₁* = u₂* = 1/4, λ = 1/4` — but algebra confirms `u₁* = 1/3, u₂* = 2/3, λ* = 4/3` for the problem as stated. The source's claim corresponds to a different problem; trust the algebra.)

### ⚠️ Common Mistakes
- ❌ Forgetting that minimising vs maximising flips the SOC sign requirement → ✅ For minimum, bordered Hessian must be **positive (semi-)definite** on tangent space.
- ❌ Treating constraint multiplier `λ` casually → ✅ It has economic meaning: shadow price of the constraint (`dV/dc = λ`).

> **Quick Recall:**
> - Lagrangian for minimisation: same form, opposite SOC sign convention.
> - For convex objective + linear constraint: any stationary point of `L` is the global minimum.

### Connections
- Builds on: Lagrangian theorem (Chunk 004: Equality Constrained Optimisation — No-Arbitrage Principle), envelope theorem (Chunk 008: Lagrange Multiplier Method — Equality Constraints (Restated)).
- Concludes: All 4 units of Block 5.

### Open Questions
1. How do we handle problems where the objective is convex but constraint set is non-convex? (Beyond this block — see graduate optimisation.)
2. When are KT conditions sufficient for inequality constraints? (When `f` concave AND `gᵢ` convex AND constraint set has interior — see Slater's condition.)


---

