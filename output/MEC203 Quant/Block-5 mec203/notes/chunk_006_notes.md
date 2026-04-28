# Chunk 006 — Unit 18 — Differentiable Convexity, Quasi-Convex/Concave, NDCQ, Slackness
<!-- Pages: 51-60 -->
<!-- Source: chunk_006.txt -->
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

### Check Your Progress 1 (Chunk 006)
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
- Builds on: Inequality KT theorem (Chunk 004).
- Is prerequisite for: Mixed equality/inequality formulation (Chunk 007).
