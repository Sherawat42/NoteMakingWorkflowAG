# Chunk 005 — Unit 17 KT Examples Continued; Unit 18 Convexity & Concavity Begins
<!-- Pages: 41-50 -->
<!-- Source: chunk_005.txt -->
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
- Builds on: Linear utility KT (Chunk 004).
- Contrasts with: Cobb-Douglas (always interior) — see exercises in Chunk 005, 010.

---

## Section: Unit 17 Summary, Key Words, Answers 🟡

### Definitions
- **Necessary and Sufficient Conditions for Optimum** of `z = f(x₁,...,xₙ)`:
  - FOC max/min: `f₁ = f₂ = ... = fₙ = 0`.
  - SOC max: `(-1)^i |H_i| > 0` ∀ `i`.
  - SOC min: `|H_i| > 0` ∀ `i`.
- **Stationary point**: tangent to graph parallel to x-axis (derivative = 0).
- **Theorem of Lagrange**: necessary FOC for equality-constrained extremum (Chunk 004).
- **Theorem of Second Order Optimum**: bordered-Hessian definiteness on null space of constraint Jacobian (Chunk 004).
- **Kuhn-Tucker Theorem**: necessary FOC for inequality-constrained extremum (Chunk 004).

### Check Your Progress 1 (Chunk 003) — Answers
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
- Builds on: KT theorem (Chunk 004) — convexity gives sufficient conditions for KT necessary conditions to be sufficient.
- Is prerequisite for: Quasi-convex/concave generalisations (Chunk 006), homothetic functions (Chunk 009).

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
- Is prerequisite for: Hessian-based test (Chunk 006), quasi-convexity (Chunk 006).
