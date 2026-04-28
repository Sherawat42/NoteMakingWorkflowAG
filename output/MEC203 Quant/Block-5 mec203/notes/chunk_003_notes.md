# Chunk 003 — Unit 17 — Unconstrained Optimisation; Multi-product Firm
<!-- Pages: 21-30 -->
<!-- Source: chunk_003.txt -->

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
- Is prerequisite for: Lagrange theorem and Kuhn-Tucker theory (Chunk 004).

### Open Questions
1. How exactly does the budget constraint enter the FOC? (Lagrangian — Chunk 004.)
2. What if the constraint is an inequality? (Kuhn-Tucker — Chunk 004.)
