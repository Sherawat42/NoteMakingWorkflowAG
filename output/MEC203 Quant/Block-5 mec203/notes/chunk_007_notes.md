# Chunk 007 — Unit 18 — Mixed Constraints, KT Lagrangian, Worked Problems
<!-- Pages: 61-70 -->
<!-- Source: chunk_007.txt -->
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
- Builds on: KT theorem (Chunk 004), complementary slackness (Chunk 006).
- Is prerequisite for: Envelope theorem (Chunk 008) and quasi-concave optimisation theory (Chunk 009).

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
