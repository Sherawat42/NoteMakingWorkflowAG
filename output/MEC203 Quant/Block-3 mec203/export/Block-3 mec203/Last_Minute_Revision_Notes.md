# Last Minute Revision Notes

> *This document contains ONLY ultra-high-yield definitions (⭐), Quick Recall facts, Common Mistakes, and core bullet points.*


## Topics


### Limit of a Function (§9.2) 🔴

**One-sided approach**
- Approach from the right: `x → a+` (also written `x → a + 0`), values strictly greater than a.
- Approach from the left: `x → a−` (also written `x → a − 0`), values strictly less than a.

**ε–δ definition (analytical form)**
- **Limit of f(x) as x → a**: the unique number t (when it exists) such that f(x) can be made arbitrarily close to t by taking x sufficiently close to a (but not equal to a). ⭐ (exam-important)

**Quick Recall:**
- Limit answers "where is f(x) heading?" — does not require f(a) to exist.
- ε–δ form: `∀ ε > 0, ∃ δ > 0 : 0 < |x − a| < δ ⇒ |f(x) − t| < ε`.

### Right-Hand and Left-Hand Limits (§9.3) 🔴

**Right-Hand Limit**

**Left-Hand Limit**

**Existence condition**
- RHL: for x > 0, |x|/x = +1, so `lim_{x→0+} = 1`.
- LHL: for x < 0, |x|/x = −1, so `lim_{x→0−} = −1`.
- Since 1 ≠ −1, the two-sided limit fails. Note also f(0) is undefined.

**Quick Recall:**
- Two-sided limit exists ⟺ RHL = LHL.
- One-sided limits use only one approach direction.

**Quick Recall:**
- "Limit is ∞" is a *behaviour* statement, not a value — the limit technically does not exist as a finite number.

### Fundamental Theorems on Limit (§9.5) 🔴

**Algebra of limits**
1. `lim {f + φ} = t₁ + t₂` (sum)
2. `lim {f · φ} = t₁ · t₂` (product)
3. `lim {f / φ} = t₁ / t₂`, provided t₂ ≠ 0 (quotient)
4. `lim F[f(x)] = F[lim f(x)]` (continuous outer)
5. **Sandwich (squeeze) theorem**: if φ(x) ≤ f(x) ≤ ψ(x) near a, and `lim φ = lim ψ = t`, then `lim f = t`.
6. Order: if φ ≤ ψ near a, then t₁ ≤ t₂.

**Standard limits to memorise**
| Limit | Value |
|---|---|
| `lim_{x→0} sin x / x` | 1 (x in radians) |
| `lim_{x→∞} (1 + 1/x)^x` | e |
| `lim_{x→0} (1 + x)^{1/x}` | e |
| `lim_{x→0} log(1+x) / x` | 1 |
| `lim_{x→0} (eˣ − 1) / x` | 1 |
| `lim_{x→a} (xⁿ − aⁿ) / (x − a)` | n a^{n−1} (a > 0) |
| `lim_{x→0} ((1+x)ⁿ − 1) / x` | n |
| `lim_{n→∞} xⁿ / n!` | 0 |

**Quick Recall:**
- Quotient rule needs t₂ ≠ 0.
- sin x / x → 1 only when x is in **radians**.
- For polynomial-over-polynomial as x → ∞, ratio of leading coefficients wins.

### ⚠️ Common Mistakes
- ❌ Mistake: applying `lim f/g = lim f / lim g` when denominator limit is 0 → ✅ Correct: this is an indeterminate 0/0 (or ∞/∞) — needs algebraic simplification or L'Hôpital (Unit 10).
- ❌ Mistake: writing `lim sin x / x = 1` for x in degrees → ✅ Correct: only valid in radians.
---

### Continuity (§9.6) 🔴

**Three-part continuity test at x = a**
1. f(a) exists.
2. `lim_{x→a} f(x)` exists (RHL = LHL).
3. The limit equals f(a).

**Types of discontinuity**
| Type | Characterisation | Example |
|---|---|---|
| **Ordinary** | RHL ≠ LHL | step function |
| **Removable** | RHL = LHL but ≠ f(a), or f(a) undefined | (x²−1)/(x−1) at x = 1 |
| **Infinite** | RHL or LHL is ±∞ | 1/x at x = 0 |
| **Oscillatory** | function oscillates without settling | (−1)^x at x → ∞ (finite or infinite oscillation) |
- **Continuous at x = a**: `lim_{x→a−} f(x) = lim_{x→a+} f(x) = f(a)`. ⭐ (exam-important)
- **Removable discontinuity**: a discontinuity that can be eliminated by redefining f(a) to equal the common one-sided limit. ⭐
- **Ordinary discontinuity**: f(a+0) ≠ f(a−0). ⭐
1. Compute f(a) — if undefined, it is at least a removable or essential discontinuity.
2. Compute LHL = `lim_{x→a−} f(x)`.
3. Compute RHL = `lim_{x→a+} f(x)`.
4. Compare: continuous ⟺ all three equal.
- (a) f(x) = (−1)^x oscillates finitely at infinity.
- (b) f(x) = (x²)^x oscillates infinitely.
- Sum, difference, and product of continuous functions are continuous (extends to any finite number of functions).
- Quotient is continuous wherever the denominator does not vanish.
- If f is continuous at a and f(a) ≠ 0, then f preserves sign in a neighbourhood of a.

**Quick Recall:**
- Continuity at a needs three things: f(a) exists, the limit exists, the two are equal.
- Removable: one redefinition fixes it. Ordinary: can't be fixed by redefining a single point.
- Differentiability ⇒ continuity (proven in Unit 10), but continuous functions are not always differentiable.
- Builds on: Limit (§9.2), One-sided limits (§9.3) — continuity is defined via limits.
- Is prerequisite for: Differentiability (Unit 10 §10.2) — you cannot have a derivative at a discontinuity (with rare infinite-derivative exceptions).
1. Why does the |x| / x example fail to have a limit at 0 even though |x| and x are individually continuous?
2. Can a function be continuous at exactly one point? (yes — Dirichlet-type constructions, beyond syllabus.)

**Quick Recall:**
- Sum, product, difference, composition of continuous → continuous.
- Quotient continuous where denominator ≠ 0.
- IVT (sign-change) gives existence of roots.

**Quick Recall:**
- Conjugate trick handles `0/0` with square roots.
- Polynomial in numerator/denominator: zeros of denominator = candidate discontinuities.
- `xⁿ / n! → 0` is a fundamental "factorial beats power" fact.

### §10.2 Derivative — Definition 🔴

**Increment notation**
- Δx (or h): an increment in the independent variable.
- Δy (or k): the corresponding increment in y = f(x), i.e., Δy = f(x + Δx) − f(x).

**Definition**

**Differentiability vs continuity (key relationship)**
- **Differentiability ⇒ continuity** (a differentiable function must be continuous).
- **Continuity ⇏ differentiability** (continuous functions can lack derivatives).
- RHD: `lim_{h→0+} |h|/h = 1`.
- LHD: `lim_{h→0−} |h|/h = −1`.
- Right and left derivatives differ ⇒ f'(0) does not exist.
- **Right-hand derivative `R f'(x)`**: `lim_{h→0+} [f(x+h) − f(x)] / h`.
- **Left-hand derivative `L f'(x)`**: `lim_{h→0−} [f(x+h) − f(x)] / h`.
- **f'(x) exists** ⟺ R f'(x) and L f'(x) both exist and are equal. ⭐
1. Write difference quotient: [f(x+h) − f(x)]/h = [2(x+h)² − 2x²]/h.
2. Expand: 2(x² + 2xh + h²) − 2x² = 4xh + 2h².
3. Divide by h: 4x + 2h.
4. Take h → 0: f'(x) = 4x.

**Quick Recall:**
- `f'(x) = lim_{h→0} [f(x+h) − f(x)]/h`.
- For f' to exist at a, RHD = LHD.
- Differentiable ⇒ continuous; converse fails (|x| at 0).

### ⚠️ Common Mistakes
- ❌ Mistake: assuming continuity guarantees differentiability → ✅ Correct: |x| is continuous everywhere but fails to be differentiable at 0.
---

### Standard Derivatives & Rules of Differentiation 🔴

**Standard derivatives**
| Function | Derivative |
|---|---|
| xⁿ (rational n) | n x^{n−1} |
| e^{mx} | m e^{mx} |
| aˣ | aˣ log_e a |
| log x (natural log) | 1/x |
| sin x | cos x |
| cos x | −sin x |
| tan x (x ≠ (2n+1)π/2) | sec² x |
| cot x (x ≠ nπ) | −cosec² x |
| sec x | sec x · tan x |
| cosec x | −cosec x · cot x |

**Rules of differentiation**
1. **Constant**: d(c)/dx = 0.
2. **Constant multiple**: d(c φ(x))/dx = c · dφ/dx.
3. **Sum**: d(φ + ψ)/dx = dφ/dx + dψ/dx (extends to finite sums).
4. **Product**: d(φψ)/dx = φ'ψ + φψ'.
5. **Quotient**: d(φ/ψ)/dx = (φ'ψ − φψ')/ψ².
6. **Chain rule (function-of-function)**: if y = f(v) and v = g(x), then `dy/dx = (dy/dv) · (dv/dx)`. Generalises: if y = f(v), v = φ(w), w = ψ(x), then `dy/dx = (dy/dv)(dv/dw)(dw/dx)`.
7. **Inverse function**: `dx/dy = 1 / (dy/dx)` provided both exist.
8. **Parametric**: if y = ψ(t), x = φ(t), then `dy/dx = (dy/dt)/(dx/dt)`, dx/dt ≠ 0.

**Quick Recall:**
- Memorise the standard table — it underpins every Unit 10 problem.
- Chain rule is the workhorse: practise spotting "outside × inside".
- Parametric form: keep a parameter t, differentiate each coordinate, take the ratio.

**Quick Recall:**
- log differentiation handles `f(x)^{g(x)}` cleanly.
- For determinants of differentiable rows, differentiate one row/column per term and sum.

### §10.4 Differentials 🔴

**Definition**

**Key relationship**

**Rules for differentials**
| Rule | Form |
|---|---|
| Constant | d(c) = 0 |
| Sum/diff | d(u + v − w) = du + dv − dw |
| Product | d(uv) = u dv + v du |
| Quotient | d(u/v) = (v du − u dv)/v² |

**Quick Recall:**
- Δx = dx (independent var); Δy ≠ dy in general (Δy is exact, dy is linear approximation).
- Differentials especially used for integration substitutions and total differential (Unit 11).

### ⚠️ Common Mistakes
- ❌ Mistake: writing Δy = dy as if always equal → ✅ Correct: only for the independent variable, or only "to first order in dx".
---

**Quick Recall:**
- Each successive differentiation typically reduces the degree of a polynomial by 1.
- Some functions (sin x, cos x, eˣ) have predictable cyclic n-th derivatives.

### §10.6 Application of Simple Derivatives in Economics 🔴

**Setup**
- Inverse demand: `p = f(q)`. Total revenue: `R = p · q = f(q) · q`.
- **Average Revenue**: `AR = R/q = p = f(q)`.
- **Marginal Revenue**: `MR = dR/dq = f(q) + q · f'(q)`.

**Key relationship**
| Case | Sign of f'(q) | MR vs AR |
|---|---|---|
| Downward-sloping AR | f'(q) < 0 | MR < AR (MR below AR curve) |
| Upward-rising AR | f'(q) > 0 | MR > AR (MR above AR curve) |
| Horizontal AR (perfect competition) | f'(q) = 0 | MR = AR |
- Total cost: `c = c(q)`. AC = c/q. MC = dc/dq.
- **Slope identity**: `d(AC)/dq = (1/q)(MC − AC)`.
| Case | AC | MC vs AC |
|---|---|---|
| AC falling | d(AC)/dq < 0 | MC < AC |
| AC rising | d(AC)/dq > 0 | MC > AC |
| AC at minimum | d(AC)/dq = 0 | MC = AC (curves cross at minimum AC) |

**Point price elasticity (e_p or ε_d)**

**Classification**
| |ε_p| | Demand category |
|---|---|
| 0 | perfectly inelastic |
| 0 < · < 1 | inelastic |
| = 1 | unitary elastic |
| 1 < · < ∞ | elastic |
| ∞ | perfectly elastic |

**Income elasticity (η_d)**
- Luxury: η_d > 1 (demand rises more than proportionately with income).
- Necessity: 0 < η_d < 1.
- Inferior: η_d < 0.
- The graph q = q(y) is the **Engel curve**.
- **Marginal Revenue**: derivative of total revenue w.r.t. quantity, MR = dR/dq. ⭐
- **Marginal Cost**: derivative of total cost w.r.t. quantity, MC = dc/dq. ⭐
- **Point price elasticity of demand**: ε_p = (dq/dp)(p/q). ⭐
- **Engel curve**: graph of demand against income, q = q(y). ⭐
- dp/dq = 2aq + b ⇒ dq/dp = 1/(2aq + b).
- ε_p = (p/q)/(2aq + b) = (aq² + bq + c)/[q(2aq + b)] = (aq² + bq + c)/(2aq² + bq).
- Unitary: |ε_p| = 1 ⇒ aq² + bq + c = 2aq² + bq ⇒ aq² = c ⇒ q = √(c/a).

**Quick Recall:**
- MR = AR + q f'(q); for downward demand, MR < AR.
- d(AC)/dq = (1/q)(MC − AC) ⇒ MC crosses AC at AC's minimum.
- For q = A pᵅ, elasticity = α everywhere; α = −1 gives rectangular hyperbola.

### ⚠️ Common Mistakes
- ❌ Mistake: equating elasticity with slope → ✅ Correct: ε also depends on (p, q).
- ❌ Mistake: dropping the negative sign in elasticity sometimes loses information about good type → ✅ Correct: keep the sign or use absolute value consciously.
---

### §10.7 Slope and Curvature 🔴

**First derivative — slope / monotonicity**
- f'(x) > 0 ⇒ f is increasing through x; tangent slopes upward.
- f'(x) < 0 ⇒ f is decreasing; tangent slopes downward.
- Monotonically increasing function: f'(x) > 0 ∀ x (in domain).
- Monotonically decreasing function: f'(x) < 0 ∀ x.

**Second derivative — curvature**
- f''(x) > 0 ⇒ **convex** (slope rising; curve bends upward; "cup-shaped").
- f''(x) < 0 ⇒ **concave** (slope falling; curve bends downward; "cap-shaped").
- f''(x) = 0 ⇒ linear (constant slope).

**Cross-table of f' and f'' (six cases)**
| f'(a) | f''(a) | Curve at a | Tangent rotation |
|---|---|---|---|
| > 0 | > 0 | upward, convex | turns anti-clockwise |
| > 0 | = 0 | upward, linear | does not turn |
| > 0 | < 0 | upward, concave | turns clockwise |
| < 0 | > 0 | downward, convex | turns anti-clockwise |
| < 0 | = 0 | downward, linear | does not turn |
| < 0 | < 0 | downward, concave | turns clockwise |
- MR = dR/dq = a(b+1) qᵇ > 0 for q > 0.
- d²R/dq² = a b (b+1) q^{b−1} > 0.
- ⇒ MR is upward-rising and convex.
- **Convex curve**: f''(x) > 0 — slope is increasing. ⭐
- **Concave curve**: f''(x) < 0 — slope is decreasing. ⭐
- **Monotonically increasing function**: f'(x) > 0 over its domain. ⭐

**Quick Recall:**
- f' sign = direction; f'' sign = bend.
- Inflexion points: where f''(x) changes sign (≠ where f'' = 0 alone).
- Builds on: Derivative (§10.2), Higher-order derivatives (§10.5).
- Is prerequisite for: Optimisation (Unit 11 §11.8 exercises) — second-order condition uses f''.
- Contrasts with: First-derivative test for extrema vs second-derivative test for curvature.
1. Why does d(AC)/dq = (1/q)(MC − AC) imply MC and AC cross only at AC's minimum/maximum?
2. Can a curve be locally convex on the left of a point and concave on the right without f''(x) = 0 at the boundary? (No — continuity of f'' bridges the sign change at an inflexion point.)

### §10.8 Taylor Series 🔴

**Form of the polynomial**
- a₀ = f(a)
- a₁ = f'(a)
- a₂ = f''(a)/2!
- ⋮
- aⱼ = f⁽ʲ⁾(a) / j!

**Taylor series with Lagrange remainder**

**Maclaurin series**
- **Analytic function** (in this unit): one expressible as a power series of the above form. ⭐
- **Lagrange remainder**: the term `f⁽ⁿ⁺¹⁾(x*)(x − a)^{n+1}/(n+1)!` controlling truncation error.
- **Maclaurin series**: Taylor series centred at zero. ⭐
| f(x) | Maclaurin series |
|---|---|
| eˣ | `1 + x + x²/2! + x³/3! + … + xⁿ/n! + …` |
| sin x | `x − x³/3! + x⁵/5! − x⁷/7! + …` |
| cos x | `1 − x²/2! + x⁴/4! − x⁶/6! + …` |
| log(1 + x) | `x − x²/2 + x³/3 − x⁴/4 + …` (defined for −1 < x ≤ 1) |

**Quick Recall:**
- Taylor at a; Maclaurin at 0.
- aⱼ = f⁽ʲ⁾(a)/j!.
- Series for log(1+x) converges only for −1 < x ≤ 1.

### ⚠️ Common Mistakes
- ❌ Mistake: applying Maclaurin to functions like log x at x = 0 → ✅ Correct: log x is undefined at 0; use log(1 + x) instead.
---

### §10.9 Mean Value Theorem (MVT) and L'Hôpital's Rule 🔴

**Mean Value Theorem (MVT)**

**Derivation from Taylor (n = 1)**

**L'Hôpital's Rule**
- **Mean Value Theorem**: existence of c ∈ (a, b) where instantaneous rate equals average rate. ⭐
- **L'Hôpital's Rule**: the limit of a 0/0 (or ∞/∞) ratio equals the limit of the derivative ratio (if it exists). ⭐
- **Linearisation**: first-order Taylor approximation, f(x) ≈ f(a) + f'(a)(x − a).

**Quick Recall:**
- MVT requires continuity on [a,b] *and* differentiability on (a,b).
- L'Hôpital applies only after confirming an indeterminate form (0/0 or ∞/∞).
- MVT + Taylor at n=1 gives linearisation.

### ⚠️ Common Mistakes
- ❌ Mistake: applying L'Hôpital without checking indeterminate form → ✅ Correct: confirm 0/0 or ∞/∞ first; otherwise the rule gives a wrong answer.
- ❌ Mistake: differentiating numerator and denominator using the quotient rule → ✅ Correct: differentiate them **separately** (not as a quotient).
---
| f(x) | dy/dx |
|---|---|
| sin²x − eˣ + 4ˣ | sin 2x − eˣ + 4ˣ log_e 4 |
| 3x² cosec x | 3 cosec x (2x − cot x) |
| (log x − sin x)/(2x² − 1) | [(2x²−1)(1/x − cos x) − 4x(log x − sin x)] / (2x² − 1)² |
| 2 cos v + tan² v, v = e^{3x} | 6 e^{3x}[tan(e^{3x}) sec²(e^{3x}) − sin(e^{3x})] |
| x = b sin θ, y = a cos θ | −(a/b) tan θ |

**Quick Recall:**
- Plug-and-chug exercises drill chain rule + quotient rule fluency.
- For optimisation, set d/dq = 0 and check second derivative.

### §11.2 Concept of Partial Differentiation 🔴

**Setting up bivariate case**
- Change x₁ alone (x₂ fixed) ⇒ partial derivative w.r.t. x₁ — denoted `∂y/∂x₁`, `f₁`, `f_{x₁}`.
- Change x₂ alone ⇒ ∂y/∂x₂.
- If x₁ and x₂ are *related* (e.g., x₂ depends on x₁), the **total derivative** of y w.r.t. x₁ accounts for both direct and indirect effects.

**Why this matters**
- Utility U = f(x₁, x₂, …) of multiple goods.
- Production Q = f(L, K, land, …).
- Demand q = f(p, y) of price and income.
- Builds on: Derivative (§10.2) — partial derivative is the single-variable derivative applied along one axis.
- Is prerequisite for: Total differential, total derivative (§11.3); MRTS, elasticity of substitution (§11.4.3); homogeneous functions and Euler's theorem (§11.4.4).
1. How does Young's theorem (cross-partials equal) interact with discontinuous second derivatives?
2. When two variables are related, why is the *total* derivative the relevant economic concept rather than the partial?

### §11.2.1 Partial Derivative — Formal Definition 🔴

**Definition**

**Marginal interpretation in economics**
- f₁ = 3 x₁² + 4 x₁ x₂ + 3 x₂².
- f₂ = 2 x₁² + 6 x₁ x₂ + 12 x₂². (Source: 2 x₁² + 3x₁ + 8x₂ — appears truncated by OCR; the correct form is via differentiating each term w.r.t. x₂.)
- **Partial derivative ∂U/∂xᵢ**: derivative of U with respect to xᵢ holding all other variables constant. ⭐
- **Marginal utility (in economics)**: ∂U/∂xᵢ for a utility function U. ⭐

**Quick Recall:**
- To compute ∂f/∂xᵢ, treat all other xⱼ (j ≠ i) as constants and differentiate as in single-variable calculus.

**Quick Recall:**
- Differentiate the lower-order partial, treating other variables as constants.
- When f no longer depends on a variable, further partials in that variable are 0.

### §11.2.3 Cross-Partial Derivatives & Young's Theorem 🔴

**Definitions**

**Young's theorem**
- f_x = 3x² + 8xy³ + 2y.
- f_y = 5y⁴ + 12 x² y² + 2x. (Source: 5y⁴ + 16 x²y² + 2x — coefficient 16 vs 12; checking `4 x² y³` derivative w.r.t. y is `12 x² y²`. OCR error in source.)
- f_{xy} = 24 xy² + 2 = f_{yx} (verifying symmetry).
- f₁ = 2x₁ / (x₁² + x₂²).
- f₂ = 2x₂ / (x₁² + x₂²).
- f₁₂ = f₂₁ = −4 x₁ x₂ / (x₁² + x₂²)² (Young verified).
- **Cross-partial derivative** f₁₂: differentiate f first w.r.t. x₁, then w.r.t. x₂. ⭐
- **Young's theorem**: f₁₂ = f₂₁ when one of the mixed partials is continuous. ⭐

**Quick Recall:**
- Young's theorem ⇒ order of mixed differentiation does not matter (under mild regularity).
- Symmetric Hessian — used in second-order conditions for optimisation.

### ⚠️ Common Mistakes
- ❌ Mistake: assuming f₁₂ = f₂₁ always → ✅ Correct: requires continuity (or both existing as continuous functions); pathological constructions exist where it fails.
---

### §11.3 Total Differential and Total Derivative 🔴
- **Total differential** dy: linear approximation of total change in y when *several* x's change *independently*.
- **Total derivative** dy/dt: rate of change of y when the xᵢ are themselves functions of a single variable t (chain rule).
- dy = (2ax₁ + 2h x₂) dx₁ + (2h x₁ + 2b x₂) dx₂
- f₁ = 4, f₂ = 3.
- dx₁/dt = 3t² + 2t.
- dx₂/dt = 3t² − 2t − 1.
- dq/dt = 4(3t² + 2t) + 3(3t² − 2t − 1) = 12t² + 8t + 9t² − 6t − 3 = **21t² + 2t − 3**.
- **Total differential** of y: dy = Σᵢ fᵢ dxᵢ. ⭐
- **Total derivative**: dy/dt = Σᵢ fᵢ · dxᵢ/dt when xᵢ depend on t. ⭐

**Quick Recall:**
- Total differential measures actual change when *multiple* variables change.
- Total derivative composes via chain rule when *all* variables depend on one parameter.
- Partial derivative is the building block; total versions sum the contributions.

### §11.4 Differentiation & Applications — Chain Rule Cases (§11.4.1) 🔴
| Case | Setup | Resulting derivatives |
|---|---|---|
| I | z = f(u), u = u(x, y) | ∂z/∂x = f'(u) · ∂u/∂x; ∂z/∂y = f'(u) · ∂u/∂y |
| II | z = f(x, y), x = φ(t), y = ψ(t) | dz/dt = (∂z/∂x) φ'(t) + (∂z/∂y) ψ'(t) |
| III | z = f(x, y), y = y(x) | dz/dx = ∂z/∂x + (∂z/∂y) · dy/dx |
| IV | z = f(x, y); x = φ(u, v), y = ψ(u, v) | ∂z/∂u = (∂z/∂x)(∂x/∂u) + (∂z/∂y)(∂y/∂u); similarly ∂z/∂v |
| Rule | Form |
|---|---|
| Sum | d(u + v) = du + dv |
| Product | d(uv) = u dv + v du |
| Quotient | d(u/v) = (v du − u dv)/v² |
| Logarithm | d(log x) = dx/x |
| Compound | d(uv/w) = du/u + dv/v − dw/w (multiplied by uv/w) |

**Quick Recall:**
- Case III is the implicit-function chain rule (used heavily next subsection).
- Case IV is the change-of-variables chain rule (used in optimisation transforms).

### §11.4.2 Implicit Functions 🔴

**First derivative (implicit)**

**Reciprocal property**

**Second derivative (formula 11.1)**

**Quick Recall:**
- For f(x, y) = 0: dy/dx = −f_x / f_y. **The minus sign is essential.**
- Second derivative uses the symmetric formula in f's second partials.

### ⚠️ Common Mistakes
- ❌ Mistake: forgetting the minus sign in dy/dx = −f_x/f_y → ✅ Correct: it comes from rearranging f_x dx + f_y dy = 0.
---

### §11.4.3 Applications — MRTS & Elasticity of Substitution 🔴
- Total differential: `dY = f_L dL + f_K dK`.
- Along an isoquant (constant Y), dY = 0 ⇒ `f_L dL + f_K dK = 0`.
- Rearranging: **`MRTS = −dK/dL = f_L / f_K`** (ratio of marginal products).

**Definition**

**Algebraic formula (after substitution)**

**Sign and interpretation**
- Convexity of isoquant ⇒ denominator (2 f₁ f₂ f₁₂ − f₁² f₂₂ − f₂² f₁₁) > 0.
- (x₁, x₂, f₁, f₂) > 0 ⇒ σ > 0.
- σ inversely proportional to *degree of convexity* of isoquant: more curved isoquant ⇒ less substitutability ⇒ smaller σ.

**Limiting cases**
| Production type | Isoquant shape | σ |
|---|---|---|
| Leontief (fixed proportions) | L-shaped | 0 |
| Cobb–Douglas | smooth, downward, convex | 1 |
| Perfect substitutes | straight line | ∞ |

**Notes**
- σ varies from one (x₁, x₂) combination to another — σ is a function of (x₁, x₂).
- σ symmetric: σ_{x₁ x₂} = σ_{x₂ x₁}.
- For **linear-homogeneous** production: `σ = f_L · f_K / (q · f_{LK})` — inversely proportional to cross-second-order partial.
- **MRTS**: ratio f_L / f_K of marginal products along an isoquant. ⭐
- **Elasticity of substitution σ**: percentage change in input ratio per percentage change in MRTS. ⭐

**Quick Recall:**
- MRTS = f_L / f_K (signed positive when isoquant slopes down).
- σ = 0: no substitutability (Leontief). σ = ∞: perfect substitutes. σ = 1: Cobb–Douglas.
- Higher σ ⇔ flatter isoquants ⇔ easier factor substitution.

### §11.4.4 Homogeneous Functions and Their Properties (begins) 🔴
- f(x₁, x₂) = x₁² + x₁ x₂ + x₂² is **degree 2** (each term sums to 2).
- z = x³ y + x² y² + y⁴ is **degree 4**.
- **Homogeneous of degree n**: f(kx₁, kx₂) = kⁿ f(x₁, x₂). ⭐
- Builds on: Partial derivatives (§11.2); chain rule (§11.4.1).
- Is prerequisite for: Cobb–Douglas analysis (chunk 006 CYP2); Euler's theorem (chunk 006).
1. What economic significance does the degree of homogeneity have for production functions? (constant returns to scale ⟺ degree 1.)
2. Why does linear-homogeneity simplify σ to a function only of f_{LK}?

### §11.4.4 Property 3 — Euler's Theorem 🔴
- **Constant returns to scale (n = 1)**: x f_x + y f_y = f(x, y). Euler's theorem in this case underlies the marginal productivity theory of distribution: paying each factor its marginal product exactly exhausts total output.

**Quick Recall:**
- Euler's theorem: `Σᵢ xᵢ f_{xᵢ} = n · f` for degree-n homogeneous f.
- For n = 1: total output = labour × MPL + capital × MPK.

**Quick Recall:**
- Cobb–Douglas q = A L^a K^{1−a}: degree 1, σ = 1, downward & convex isoquants.
- Marginal products depend only on the input ratio K/L — homotheticity property.

**Quick Recall:**
- Inflexion point of total cost = minimum of marginal cost.
- Revenue maximisation: dR/dx = 0 (set MR = 0).

### §12.2 Indefinite Integrals 🔴
- f(x) = the **integrand**.
- ∫ symbol is an elongated "S" denoting **sum** (anticipating the area-as-sum interpretation).
- ∫ f(x) dx reads "the integral of f(x) with respect to x".
- **Indefinite integral** `∫ f(x) dx = F(x) + C`: any function F whose derivative is f, plus an arbitrary constant. ⭐
- **Constant of integration C**: the arbitrary additive constant; reflects non-uniqueness of antiderivatives. ⭐

**Quick Recall:**
- "Anti-derivative" is the most useful synonym.
- **Always** include + C in indefinite integrals.

### §12.3 Properties of the Indefinite Integral 🔴
1. Antidifferentiate: y = x³ − x² + C.
2. Plug in initial condition: 5 = 8 − 4 + C ⇒ C = 1.
3. Answer: y = x³ − x² + 1.

**Quick Recall:**
- Linearity: pull constants out, split sums.
- Power rule: x^{n+1}/(n+1), but **only for n ≠ −1**.
- Boundary/initial conditions uniquely determine C.

### §12.3.2 Method of Substitution 🔴
1. Identify a composite expression: u = (something).
2. Compute du = (derivative of u) dx.
3. Rewrite the integral fully in u (no x left).
4. Integrate w.r.t. u using power/standard rules.
5. Substitute back u = g(x).
6. Add + C.

**Quick Recall:**
- Substitution works when the integrand contains both g(x) and g'(x) (up to a constant).
- Always express **everything** in terms of u — including dx.

### ⚠️ Common Mistakes
- ❌ Mistake: forgetting to convert dx into du → ✅ Correct: derive du = g'(x) dx and use it to replace dx.
---
| Function | Derivative |
|---|---|
| sin A | cos A |
| cos A | −sin A |
| tan A | sec² A |
| cot A | −cosec² A |
| sec A | sec A · tan A |
| cosec A | −cosec A · cot A |
| Basic form | Generalised (linear arg ax + b) |
|---|---|
| ∫ cos x dx = sin x + C | ∫ cos(ax + b) dx = (1/a) sin(ax + b) + C |
| ∫ sin x dx = −cos x + C | ∫ sin(ax + b) dx = −(1/a) cos(ax + b) + C |
| ∫ tan x dx = −ln|cos x| + C | ∫ tan(ax + b) dx = −(1/a) ln|cos(ax + b)| + C |
| ∫ cot x dx = ln|sin x| + C | ∫ cot(ax + b) dx = (1/a) ln|sin(ax + b)| + C |
| ∫ sec x dx = ln|sec x + tan x| + C | (1/a) ln|sec(ax + b) + tan(ax + b)| + C |
| ∫ cosec x dx = ln|cosec x + cot x| + C (with a sign convention) | likewise (1/a) form |

**Quick Recall:**
- Product-to-sum identities turn cos×cos, sin×cos, sin×sin into sums of single trig functions.
- For odd powers of sin (or cos), peel off one factor to combine with du.
- Linear-argument trick: ∫ f(ax + b) dx = (1/a) F(ax + b) where F is the antiderivative of f.

### §12.5 Integration by Parts 🔴
1. Pick u: the part that **simplifies on differentiation** (e.g., x → 1, ln x → 1/x).
2. Pick dv: the part you **can integrate** (e.g., sin x dx, eˣ dx).
3. Compute du = u' dx and v = ∫ dv.
4. Apply the formula `∫ u dv = uv − ∫ v du`.
5. Evaluate the new integral; if needed, apply by-parts again.
- u = x, dv = e^{−x} dx.
- du = dx, v = −e^{−x}.
- ∫ x e^{−x} dx = −x e^{−x} − ∫ (−e^{−x}) dx = −x e^{−x} − e^{−x} + C = −(1 + x) e^{−x} + C.
- u = 3t + 5, dv = cos(t/4) dt.
- du = 3 dt, v = 4 sin(t/4).
- ∫ = 4(3t + 5) sin(t/4) − 12 ∫ sin(t/4) dt = 4(3t + 5) sin(t/4) + 48 cos(t/4) + C.
- u = ln x, dv = x dx (LIATE: log first).
- du = dx/x, v = x²/2.
- ∫ x ln x dx = (x²/2) ln x − ∫ (x²/2) · (1/x) dx = (x²/2) ln x − x²/4 + C.

**Quick Recall:**
- `∫ u dv = uv − ∫ v du`.
- LIATE: pick u from earlier in L-I-A-T-E.
- Repeat by-parts when the new integral still has a product (e.g., for x² eˣ, two by-parts).

### ⚠️ Common Mistakes
- ❌ Mistake: forgetting the minus sign in `−∫ v du` → ✅ Correct: it comes straight from rearranging the product rule.
---

### §12.6 Some Useful Formulae 🔴
| # | Formula | Notes |
|---|---|---|
| 1 | `∫ xⁿ dx = x^{n+1}/(n+1) + C` | n ≠ −1 |
| 2 | `∫ x^{−1} dx = ∫ dx/x = ln |x| + C` | for x ≠ 0 |
| 3 | `∫ e^{mx} dx = e^{mx}/m + C` | for any m ≠ 0 |
| 4 | `∫ a^{mx} dx = a^{mx}/(m ln a) + C` | a > 0, a ≠ 1 |
| 5 | `∫ cos(ax) dx = sin(ax)/a + C` | |
| 6 | `∫ sin(ax) dx = −cos(ax)/a + C` | |
| 7 | `∫ [k₁ f(x) + k₂ g(x)] dx = k₁ ∫ f(x) dx + k₂ ∫ g(x) dx + C` | linearity, k₁, k₂ constants |

**Quick Recall:**
- **Memorise these seven** — they cover most direct integrals encountered.

**Quick Recall:**
- One initial condition fixes one constant of integration.

### §12.8 Definite Integrals 🔴

**Setup**
| Choice of height | Approx area |
|---|---|
| Right endpoint | Σᵢ f(xᵢ) Δx |
| Left endpoint | Σᵢ f(xᵢ₋₁) Δx |
| Midpoint | Σᵢ f((xᵢ₋₁ + xᵢ)/2) Δx |
- Right endpoints **overestimate**.
- Left endpoints **underestimate**.
- Midpoint typically gives the best approximation for fixed n.

**Worked example: f(x) = x² + 1 on [0, 2] with n = 4**
- Δx = 0.5; partition x₀=0, x₁=0.5, x₂=1, x₃=1.5, x₄=2.
- Right-endpoint sum A_R = 0.5[f(0.5) + f(1) + f(1.5) + f(2)] = 0.5[1.25 + 2 + 3.25 + 5] = 5.75.
- Left-endpoint sum A_L = 0.5[f(0) + f(0.5) + f(1) + f(1.5)] = 0.5[1 + 1.25 + 2 + 3.25] = 3.75.
- True value (from §12.8.2 below): ∫₀² (x² + 1) dx = 14/3 + 2 ≈ 4.67. (Right overestimates, left underestimates.)
- **Riemann sum**: Σᵢ f(xᵢ*) Δxᵢ for a partition of [a, b]. ⭐
- **Definite integral**: limit of Riemann sums as the partition gets infinitely fine. ⭐
- **Mesh size**: max width of subintervals in the partition.

**Quick Recall:**
- Riemann sum: pick a point in each strip, sum height × width.
- Limit (mesh → 0) is the definite integral.

### §12.8.3 Properties of Definite Integral 🔴
| # | Property |
|---|---|
| 1 | `∫ₐᵇ 1 dx = b − a` |
| 2 | `∫ₐᵇ c · f(x) dx = c · ∫ₐᵇ f(x) dx` (constant factors out) |
| 3 | `∫ₐᵇ [f + g] dx = ∫ₐᵇ f dx + ∫ₐᵇ g dx` (linearity) |
| 4 | `∫ₐᵇ f dx = ∫ₐᶜ f dx + ∫ᶜᵇ f dx` (additivity over intervals; a ≤ c ≤ b) |
| 5 | If 0 ≤ f(x) ≤ g(x) on [a, b], then `0 ≤ ∫ₐᵇ f dx ≤ ∫ₐᵇ g dx` (comparison) |
| 6 | `∫ₐᵃ f(x) dx = 0` (degenerate interval = 0 area) |
| 7 | `∫ₐᵇ f(x) dx = − ∫_b^a f(x) dx` (reversing bounds flips sign) |

**Quick Recall:**
- Same bounds → 0.
- Flipping bounds → flip sign.
- Linearity (scalar + sum) extends to definite integrals just as for indefinite.
- Builds on: Indefinite integral (§12.2); area-as-sum interpretation; FTC (§12.9 in chunk 008) ties indefinite and definite together.
- Is prerequisite for: Fundamental theorem (§12.9), area calculations (§12.10), improper integrals (§12.11).
1. Why must f be continuous (or at least Riemann-integrable) for the limit definition to apply? (Pathological functions can have ill-defined Riemann sums.)
2. Can a definite integral be negative? (Yes — when f(x) < 0 on parts of [a, b]; the integral measures *signed* area.)

### §12.9 Fundamental Theorem of Calculus (FTC) 🔴
- **Antiderivative (or indefinite integral)**: any function F with F'(x) = f(x). ⭐
- **Fundamental Theorem of Calculus (Part 2)**: ∫ₐᵇ f(x) dx = F(b) − F(a). ⭐

**Quick Recall:**
- Part 1: derivative of "area function" = integrand.
- Part 2: ∫ₐᵇ f = F(b) − F(a) for *any* antiderivative F.
- Two antiderivatives differ by a constant — so the choice of F doesn't matter.

### ⚠️ Common Mistakes
- ❌ Mistake: applying Part 1 to ∫_{a}^{g(x)} f(t) dt as just f(x) → ✅ Correct: the chain rule gives f(g(x)) · g'(x).
---

**Quick Recall:**
- Net area ≠ total area when f changes sign — split at zeros for total.
- For definite integrals with substitution: either revert to x then plug in original bounds, or update the bounds and stay in u.

### §12.11 Improper Integrals 🔴
| Form | Definition |
|---|---|
| ∫_b^∞ f(x) dx | lim_{a → ∞} ∫_b^a f(x) dx |
| ∫_{−∞}^a f(x) dx | lim_{b → −∞} ∫_b^a f(x) dx |
- If `∫_a^∞ f` converges, then `∫_a^∞ g` converges.
- If `∫_a^∞ g` diverges, then `∫_a^∞ f` diverges.
- ∫_{−∞}^0 x · e^{−x²} dx: u = −x², du = −2x dx. Antiderivative −(1/2) e^{−x²}. lim_{b → −∞} [−(1/2)(1 − e^{−b²})] = −1/2.
- ∫_0^∞ x · e^{−x²} dx = +1/2.
- Total = −1/2 + 1/2 = **0** ⇒ convergent to 0.
- **Improper integral**: definite integral with infinite bound or unbounded integrand. ⭐
- **Convergent integral**: limit exists and is finite. ⭐
- **Divergent integral**: limit is infinite or does not exist. ⭐

**Quick Recall:**
- Always rewrite `∫_b^∞` as `lim_{a→∞} ∫_b^a`.
- For `∫_{−∞}^∞`, both halves must converge separately.
- 1/x^p on [1, ∞): converges if p > 1, diverges if p ≤ 1.

### ⚠️ Common Mistakes
- ❌ Mistake: in ∫_{−∞}^∞ f, taking a single symmetric limit (a → ∞ with bounds [−a, a]) → ✅ Correct: each half must converge independently; the symmetric "principal value" can hide divergence.
---

### §12.12 Integration with Partial Fractions 🔴
1. p(x)/q(x) is a rational function (polynomials).
2. **deg(p) < deg(q)**. (If not, polynomial-divide first; integrate the polynomial part directly and decompose the remainder.)
| Factor of denominator | Term in decomposition |
|---|---|
| (x − a) (distinct linear) | A/(x − a) |
| (x − a)² | A/(x − a) + B/(x − a)² |
| (x − a)ᵏ | A₁/(x − a) + A₂/(x − a)² + … + Aₖ/(x − a)ᵏ |
| irreducible quadratic (x² + bx + c) | (Bx + C)/(x² + bx + c) |
| (x² + bx + c)ᵏ | k similar quadratic terms with rising denominators |
1. Check deg(p) < deg(q); if not, long-divide.
2. Factor q(x) completely (linear + irreducible quadratic factors).
3. Write the partial-fraction template with unknowns (A, B, C, …).
4. Multiply out to clear denominators ⇒ a polynomial identity.
5. Solve for unknowns by either (a) plugging in strategic values of x (often the zeros of q) or (b) equating coefficients of like powers.
6. Integrate each simple fraction.
- Factor: x² − x − 6 = (x − 3)(x + 2).
- Decompose: (3x + 11)/[(x − 3)(x + 2)] = A/(x − 3) + B/(x + 2).
- Multiply out: 3x + 11 = A(x + 2) + B(x − 3).
- x = 3: 20 = 5A ⇒ A = 4.
- x = −2: 5 = −5B ⇒ B = −1.
- Integral = 4 ∫ dx/(x − 3) − ∫ dx/(x + 2) = 4 ln|x − 3| − ln|x + 2| + C.
- **Partial fraction decomposition**: writing a rational function as a sum of simpler rational functions whose denominators are factors of the original denominator. ⭐

**Quick Recall:**
- Always check deg(p) < deg(q) first; long-divide if not.
- Distinct linear factor → constant numerator. Repeated linear → ascending powers. Irreducible quadratic → linear numerator (Bx + C).
- "Cover-up" (plug in x = root) is the fastest way to find the constant for a distinct linear factor.

### ⚠️ Common Mistakes
- ❌ Mistake: writing (Bx + C)/(x² + 1) as just B/(x² + 1) → ✅ Correct: irreducible quadratic factors get **linear** numerators.
- ❌ Mistake: forgetting to long-divide when deg(p) ≥ deg(q) → ✅ Correct: long-divide first; integrate the polynomial part separately.
- Builds on: Linearity of integration (§12.3); standard logarithmic and inverse-tangent integrals.
- Continues into: Chunk 009 — more partial fraction examples (12.39–12.43), Unit 12 wrap-up, exercises.
1. How do you handle ∫ dx/(x² + 1) without a partial fraction step? (It is arctan x + C — recognise it directly.)
2. What happens when q(x) has complex (non-real) roots? (Group conjugate pairs into irreducible quadratic factors.)

**Quick Recall:**
- For repeated linear factors, you need ascending powers in the decomposition.
- For "improper" rationals, long-divide before decomposing.
- Trig integrals with odd powers reduce to substitution.
| Term | Meaning |
|---|---|
| **Boundary condition** | A condition fixing C (e.g., y(x₀) = y₀) |
| **Closed interval** | [a, b] including endpoints |
| **Definite integral** | ∫ₐᵇ f(x) dx — a number; signed area |
| **Improper integral** | Definite integral with infinite bound or unbounded integrand; evaluated via limits |
| **Indefinite integral** | Anti-derivative — a function family F(x) + C |
| **Integration by parts** | ∫ u dv = uv − ∫ v du |
| **Partial fractions** | Decomposing p(x)/q(x) into simpler rational pieces |
| **Rational substitution** | Substituting to convert integrand into a rational function |
| **Riemann sum** | Σ f(xᵢ*) Δxᵢ — discrete approximation to ∫ |
| **Substitution rule** | ∫ f(g(x)) g'(x) dx = ∫ f(u) du, u = g(x) |

**Quick Recall:**
- For "(2x² + 3)" with x ∈ [−1, 2], the new u-bounds are 5 and 11.
- 1/√(3 − x) on [0, 3] is improper at x = 3 — but converges (= 2√3).

**Quick Recall:**
- Q3 (∫ sec x): standard trick of multiplying by `(sec x + tan x)/(sec x + tan x)`.
- Q5: ∫ x √(x+1) — substitution and parts both work.
- Q9 demonstrates that a singularity *inside* the interval makes the integral improper even with finite bounds.
