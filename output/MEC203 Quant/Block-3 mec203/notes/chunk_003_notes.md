# Chunk 003 — Unit 10: Differentiation tricks, Differentials, Higher Order, Economic Applications, Slope & Curvature
<!-- Pages: 21-30 -->
<!-- Source: chunk_003.txt -->

## Section: Differentiation Tricks (Logarithmic, Trig Simplification, Determinant) 🟡

### Core Idea
For complex compositions of products, powers, or ratios, transformations *before* differentiating often save labour. The three chief tricks: (i) logarithmic differentiation; (ii) trigonometric identity simplification; (iii) determinant differentiation column-by-column.

### Key Concepts

#### Logarithmic differentiation
For y = (cosec x)^{cot x}, take log first: `log y = cot x · log cosec x`. Differentiate both sides — the chain rule on the right yields a clean expression.

#### Trigonometric simplification
For `y = tan⁻¹[(√(1+sinx) − √(1−sinx)) / (√(1+sinx) + √(1−sinx))]`, multiply by conjugate / use half-angle: simplifies to `y = x/2`, hence `dy/dx = 1/2`.

#### Determinant differentiation
For Δ(x) = | row₁; row₂; row₃ | with each row a function of x:
Δ'(x) = | row₁'; row₂; row₃ | + | row₁; row₂'; row₃ | + | row₁; row₂; row₃' |
i.e., differentiate one row at a time and sum. The same rule holds column-wise.

### Examples
**Example 10.4(a): y = (cosec x)^{cot x}**
log y = cot x · log cosec x
(1/y) dy/dx = −cosec²x · log cosec x + cot x · (−cosec x cot x / cosec x)
= −(cosec²x · log cosec x + cot²x)
∴ dy/dx = −(cosec x)^{cot x} (cosec²x · log cosec x + cot²x).

**Example 10.5: 3×3 determinant with sin/cos rows.** Differentiating column-by-column and simplifying gives Δ'(x) = sin²x + cos²x = 1.

> **Quick Recall:**
> - log differentiation handles `f(x)^{g(x)}` cleanly.
> - For determinants of differentiable rows, differentiate one row/column per term and sum.

---

## Section: §10.4 Differentials 🔴

### Core Idea
Where a derivative `f'(x)` is a *rate*, the **differential** `df = f'(x) dx` is an *infinitesimal increment* — the linear approximation to the actual change Δf produced by an increment dx. Differentials behave like ordinary numbers in calculation and are central to integration.

> **In Simple Terms:** Imagine zooming in on a curve so it looks like a straight line. The differential dy is the change you'd predict using the tangent line; the actual change Δy is the change along the curve. They agree to first order in dx but differ for finite Δx.

### Key Concepts

#### Definition
For y = f(x), Δx an increment, the differential of f is:
`df(x) = f'(x) Δx` ... (10.1)
Taking f(x) = x ⇒ f'(x) = 1, so dx = Δx. Thus for the **independent** variable, dx = Δx.
Substituting back: `dy = f'(x) dx` ... (10.2).

#### Key relationship
`dy/dx = f'(x)` — so the derivative is also the *quotient* of differentials.

#### Rules for differentials
| Rule | Form |
|---|---|
| Constant | d(c) = 0 |
| Sum/diff | d(u + v − w) = du + dv − dw |
| Product | d(uv) = u dv + v du |
| Quotient | d(u/v) = (v du − u dv)/v² |

### Examples
**y = tan x ⇒ dy = sec² x · dx.**

> **Quick Recall:**
> - Δx = dx (independent var); Δy ≠ dy in general (Δy is exact, dy is linear approximation).
> - Differentials especially used for integration substitutions and total differential (Unit 11).

### ⚠️ Common Mistakes
- ❌ Mistake: writing Δy = dy as if always equal → ✅ Correct: only for the independent variable, or only "to first order in dx".

---

## Section: §10.5 Higher Order Derivatives 🟡

### Core Idea
The derivative of f(x) is itself a function, which can be differentiated again to give the **second derivative** f''(x), and so on for the n-th derivative f⁽ⁿ⁾(x).

### Notation
- f'(x), f''(x), …, f⁽ⁿ⁾(x).
- dy/dx, d²y/dx², d³y/dx³, …, dⁿy/dxⁿ.

### Examples
**Example 10.6: y = 4x⁵ + 7x⁴ + 3x + 9.**
- dy/dx = 20x⁴ + 28x³ + 3.
- d²y/dx² = 80x³ + 84x².
- d³y/dx³ = 240x² + 168x.

> **Quick Recall:**
> - Each successive differentiation typically reduces the degree of a polynomial by 1.
> - Some functions (sin x, cos x, eˣ) have predictable cyclic n-th derivatives.

---

## Section: §10.6 Application of Simple Derivatives in Economics 🔴

### Core Idea
Economics is full of functional relationships — and the *rate of change* of one variable due to another is exactly what derivatives compute. The chapter develops four canonical applications: AR/MR, AC/MC, point price elasticity, and the constant-elasticity demand curve.

### §10.6.1 Average Revenue (AR) and Marginal Revenue (MR)

#### Setup
- Inverse demand: `p = f(q)`. Total revenue: `R = p · q = f(q) · q`.
- **Average Revenue**: `AR = R/q = p = f(q)`.
- **Marginal Revenue**: `MR = dR/dq = f(q) + q · f'(q)`.

#### Key relationship
`MR = AR + q · f'(q)`

| Case | Sign of f'(q) | MR vs AR |
|---|---|---|
| Downward-sloping AR | f'(q) < 0 | MR < AR (MR below AR curve) |
| Upward-rising AR | f'(q) > 0 | MR > AR (MR above AR curve) |
| Horizontal AR (perfect competition) | f'(q) = 0 | MR = AR |

At q = 0: MR = AR = f(0) (curves intersect on the price axis).

### §10.6.2 Average Cost (AC) and Marginal Cost (MC)

- Total cost: `c = c(q)`. AC = c/q. MC = dc/dq.
- **Slope identity**: `d(AC)/dq = (1/q)(MC − AC)`.

| Case | AC | MC vs AC |
|---|---|---|
| AC falling | d(AC)/dq < 0 | MC < AC |
| AC rising | d(AC)/dq > 0 | MC > AC |
| AC at minimum | d(AC)/dq = 0 | MC = AC (curves cross at minimum AC) |

> **In Simple Terms:** Marginal pulls average up when above it, down when below it — like adding a higher-grade test pulls your average up.

### §10.6.3 Elasticity of Demand

#### Point price elasticity (e_p or ε_d)
For q = f(p):
`ε_p = (Δq/q × 100)/(Δp/p × 100) = (Δq/Δp)(p/q)`.
Taking Δp → 0:
`ε_p = (dq/dp)(p/q)` ... (10.3)

Demand curve typically slopes down (dq/dp < 0), so ε_p < 0; usually we report **|ε_p|**.

#### Classification
| |ε_p| | Demand category |
|---|---|
| 0 | perfectly inelastic |
| 0 < · < 1 | inelastic |
| = 1 | unitary elastic |
| 1 < · < ∞ | elastic |
| ∞ | perfectly elastic |

⚠️ Slope ≠ elasticity: two curves with the same slope can have different ε_p (depends on (p, q) point).

#### Income elasticity (η_d)
For q = f(y) (with price held fixed): `η_d = (dq/dy)(y/q)`.
- Luxury: η_d > 1 (demand rises more than proportionately with income).
- Necessity: 0 < η_d < 1.
- Inferior: η_d < 0.
- The graph q = q(y) is the **Engel curve**.

### §10.6.4 Constant Elasticity Demand Curve

For `q = A pᵅ` (A, α constants):
`ε_p = (p/q)(dq/dp) = (p/q)(A α p^{α−1}) = α (A pᵅ)/q = α`.

So ε_p = α everywhere on the curve — independent of (p, q). Special case α = −1: q = A/p, i.e., **pq = A**, a rectangular hyperbola.

### Definitions
- **Marginal Revenue**: derivative of total revenue w.r.t. quantity, MR = dR/dq. ⭐
- **Marginal Cost**: derivative of total cost w.r.t. quantity, MC = dc/dq. ⭐
- **Point price elasticity of demand**: ε_p = (dq/dp)(p/q). ⭐
- **Engel curve**: graph of demand against income, q = q(y). ⭐

### Examples
**Q: For p = aq² + bq + c, find ε_p and the q at which demand is unitary elastic.**
- dp/dq = 2aq + b ⇒ dq/dp = 1/(2aq + b).
- ε_p = (p/q)/(2aq + b) = (aq² + bq + c)/[q(2aq + b)] = (aq² + bq + c)/(2aq² + bq).
- Unitary: |ε_p| = 1 ⇒ aq² + bq + c = 2aq² + bq ⇒ aq² = c ⇒ q = √(c/a).

> **Quick Recall:**
> - MR = AR + q f'(q); for downward demand, MR < AR.
> - d(AC)/dq = (1/q)(MC − AC) ⇒ MC crosses AC at AC's minimum.
> - For q = A pᵅ, elasticity = α everywhere; α = −1 gives rectangular hyperbola.

### ⚠️ Common Mistakes
- ❌ Mistake: equating elasticity with slope → ✅ Correct: ε also depends on (p, q).
- ❌ Mistake: dropping the negative sign in elasticity sometimes loses information about good type → ✅ Correct: keep the sign or use absolute value consciously.

---

## Section: §10.7 Slope and Curvature 🔴

### Core Idea
The first derivative gives the *direction* of change (function rising or falling); the second derivative gives the *curvature* (convex, concave, or linear). Together they classify the local shape of a curve.

### Key Concepts

#### First derivative — slope / monotonicity
- f'(x) > 0 ⇒ f is increasing through x; tangent slopes upward.
- f'(x) < 0 ⇒ f is decreasing; tangent slopes downward.
- Monotonically increasing function: f'(x) > 0 ∀ x (in domain).
- Monotonically decreasing function: f'(x) < 0 ∀ x.

#### Second derivative — curvature
- f''(x) > 0 ⇒ **convex** (slope rising; curve bends upward; "cup-shaped").
- f''(x) < 0 ⇒ **concave** (slope falling; curve bends downward; "cap-shaped").
- f''(x) = 0 ⇒ linear (constant slope).

#### Cross-table of f' and f'' (six cases)
| f'(a) | f''(a) | Curve at a | Tangent rotation |
|---|---|---|---|
| > 0 | > 0 | upward, convex | turns anti-clockwise |
| > 0 | = 0 | upward, linear | does not turn |
| > 0 | < 0 | upward, concave | turns clockwise |
| < 0 | > 0 | downward, convex | turns anti-clockwise |
| < 0 | = 0 | downward, linear | does not turn |
| < 0 | < 0 | downward, concave | turns clockwise |

### Examples
**Example 10.8(i): y = 5x² + 6.** f''(x) = 10 > 0 — globally convex. (Note: source has f'' = 5 due to a typo; correct is 10. The qualitative conclusion stands: convex everywhere.)

**Example 10.8(ii): demand p = aq² + bq + c — find ε_p, conditions for unity elasticity.** (Worked above.)

**Example 10.8(iii): demand q = aq^b ... revenue R = a q^{b+1}.**
- MR = dR/dq = a(b+1) qᵇ > 0 for q > 0.
- d²R/dq² = a b (b+1) q^{b−1} > 0.
- ⇒ MR is upward-rising and convex.

### Definitions
- **Convex curve**: f''(x) > 0 — slope is increasing. ⭐
- **Concave curve**: f''(x) < 0 — slope is decreasing. ⭐
- **Monotonically increasing function**: f'(x) > 0 over its domain. ⭐

> **Quick Recall:**
> - f' sign = direction; f'' sign = bend.
> - Inflexion points: where f''(x) changes sign (≠ where f'' = 0 alone).

### Connections
- Builds on: Derivative (§10.2), Higher-order derivatives (§10.5).
- Is prerequisite for: Optimisation (Unit 11 §11.8 exercises) — second-order condition uses f''.
- Contrasts with: First-derivative test for extrema vs second-derivative test for curvature.

### Open Questions
1. Why does d(AC)/dq = (1/q)(MC − AC) imply MC and AC cross only at AC's minimum/maximum?
2. Can a curve be locally convex on the left of a point and concave on the right without f''(x) = 0 at the boundary? (No — continuity of f'' bridges the sign change at an inflexion point.)
