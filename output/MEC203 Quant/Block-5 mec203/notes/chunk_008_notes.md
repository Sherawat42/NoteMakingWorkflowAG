# Chunk 008 — Unit 19 — Multiplier, Envelope Theorem, Homogeneous Functions
<!-- Pages: 71-80 -->
<!-- Source: chunk_008.txt -->

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
- Builds on: Lagrangian theorem (Chunk 004), value function concept (this section).
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
- Is prerequisite for: Homothetic functions (Chunk 009), Euler's theorem (Chunk 009).

### Open Questions
1. What's the relationship between homogeneity and concavity? (Independent — neither implies the other.)
2. How does homogeneity of degree 1 relate to the cost-minimising firm? (CRS ⟺ marginal cost = average cost.)
