# Chunk 004 — Unit 17 — Equality & Inequality Constraints; Lagrange & Kuhn-Tucker
<!-- Pages: 31-40 -->
<!-- Source: chunk_004.txt -->
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
