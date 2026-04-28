# Chunk 001 — Block 5 Intro & Unit 16 (Optimisation: An Introduction)
<!-- Pages: 1-10 -->
<!-- Source: chunk_001.txt -->

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
- Is prerequisite for: SOC via Hessian principal minors (Chunk 002).

### Open Questions
1. How does the FOC for an extremum interact with constraints? (Answered in Unit 17.)
