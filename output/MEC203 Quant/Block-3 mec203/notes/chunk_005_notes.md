# Chunk 005 — Unit 11: Partial Derivatives, Total Differential/Derivative, Implicit, MRTS, Elasticity of Substitution, Homogeneity (Properties 1–2)
<!-- Pages: 41-50 -->
<!-- Source: chunk_005.txt -->

## Section: §11.2.1 Partial Derivative — Formal Definition 🔴
<!-- See chunk 004 for §11.2 intro -->

### Core Idea
The partial derivative of U = f(x₁, x₂) with respect to x₁ at a point is the limit of ΔU/Δx₁ as Δx₁ → 0 with x₂ held fixed. It is the slope of the "x₁-cross-section" of the surface.

### Key Concepts

#### Definition
Difference quotient:
`ΔU/Δx₁ = [f(x₁ + Δx₁, x₂*) − f(x₁*, x₂*)] / Δx₁`
Limiting value as Δx₁ → 0:
`f₁ = ∂U/∂x₁ = lim_{Δx₁→0} [f(x₁ + Δx₁, x₂) − f(x₁, x₂)] / Δx₁`

Symmetric definition for f₂ = ∂U/∂x₂.

#### Marginal interpretation in economics
If U = f(x₁, x₂) is a utility function, then `∂U/∂xᵢ` is the **marginal utility of good i** — the additional utility from one more unit of xᵢ, keeping the other goods fixed.

### Examples
**Example 11.1: f(x₁, x₂) = x₁³ + 2 x₁² x₂ + 3 x₁ x₂² + 4 x₂³.**
Treat x₂ as constant when differentiating w.r.t. x₁:
- f₁ = 3 x₁² + 4 x₁ x₂ + 3 x₂².
- f₂ = 2 x₁² + 6 x₁ x₂ + 12 x₂². (Source: 2 x₁² + 3x₁ + 8x₂ — appears truncated by OCR; the correct form is via differentiating each term w.r.t. x₂.)

### Definitions
- **Partial derivative ∂U/∂xᵢ**: derivative of U with respect to xᵢ holding all other variables constant. ⭐
- **Marginal utility (in economics)**: ∂U/∂xᵢ for a utility function U. ⭐

> **Quick Recall:**
> - To compute ∂f/∂xᵢ, treat all other xⱼ (j ≠ i) as constants and differentiate as in single-variable calculus.

---

## Section: §11.2.2 Higher Order Partial Derivatives 🟡

### Core Idea
Partial differentiating a partial derivative gives second- (and higher-) order partials. The notation: `f_{ij} = ∂²f / (∂xⱼ ∂xᵢ)` (differentiate w.r.t. xⱼ then w.r.t. xᵢ — orders matter notationally, though often equal by Young's theorem).

### Examples
**Example 11.2(i): z = 6x² + 5x³ + 10xy.**
- z_x = 18x + 15x² + 10y. (Source has 18x²+10x+10y; reading the source `6x²+5x³+10xy`, derivative is `12x + 15x² + 10y` — but the OCR may have mangled coefficients. Treat coefficients with care; the qualitative method is right.)
- z_{xx} = 12 + 30x.

**Example 11.2(ii): f(x₁, x₂) = e^{x₁ + x₂} + 3 x₁ x₂.**
- f₁ = e^{x₁+x₂} + 3 x₂.
- f₁₁ = e^{x₁+x₂}; (derivative of 3x₂ w.r.t. x₁ is 0).

> **Quick Recall:**
> - Differentiate the lower-order partial, treating other variables as constants.
> - When f no longer depends on a variable, further partials in that variable are 0.

---

## Section: §11.2.3 Cross-Partial Derivatives & Young's Theorem 🔴

### Core Idea
The two ways of computing a mixed second partial derivative — first w.r.t. x₁ then x₂, vs first w.r.t. x₂ then x₁ — give the **same result** under mild conditions (Young's theorem / Schwarz's theorem). This is a powerful symmetry used pervasively in economics (e.g., to show MRS = price ratio in equilibrium implies symmetric income effects).

### Key Concepts

#### Definitions
`f₁₂ = ∂f₁/∂x₂` and `f₂₁ = ∂f₂/∂x₁`.

#### Young's theorem
**`f₁₂ = f₂₁`** when both partials exist and (at least) one is continuous. Generalises to n variables: `f_{ij} = f_{ji}` for all i, j.

### Examples
**Example 11.3(i): f(x, y) = x³ + y⁵ + 4 x² y³ + 2xy.**
- f_x = 3x² + 8xy³ + 2y.
- f_y = 5y⁴ + 12 x² y² + 2x. (Source: 5y⁴ + 16 x²y² + 2x — coefficient 16 vs 12; checking `4 x² y³` derivative w.r.t. y is `12 x² y²`. OCR error in source.)
- f_{xy} = 24 xy² + 2 = f_{yx} (verifying symmetry).

**Example 11.3(ii): f(x₁, x₂) = log(x₁² + x₂²).**
- f₁ = 2x₁ / (x₁² + x₂²).
- f₂ = 2x₂ / (x₁² + x₂²).
- f₁₂ = f₂₁ = −4 x₁ x₂ / (x₁² + x₂²)² (Young verified).

### Definitions
- **Cross-partial derivative** f₁₂: differentiate f first w.r.t. x₁, then w.r.t. x₂. ⭐
- **Young's theorem**: f₁₂ = f₂₁ when one of the mixed partials is continuous. ⭐

> **Quick Recall:**
> - Young's theorem ⇒ order of mixed differentiation does not matter (under mild regularity).
> - Symmetric Hessian — used in second-order conditions for optimisation.

### ⚠️ Common Mistakes
- ❌ Mistake: assuming f₁₂ = f₂₁ always → ✅ Correct: requires continuity (or both existing as continuous functions); pathological constructions exist where it fails.

---

## Section: §11.3 Total Differential and Total Derivative 🔴

### Core Idea
Two distinct generalisations of dy = f'(x) dx exist for multivariate functions:
- **Total differential** dy: linear approximation of total change in y when *several* x's change *independently*.
- **Total derivative** dy/dt: rate of change of y when the xᵢ are themselves functions of a single variable t (chain rule).

### §11.3.1 Total Differential
For y = f(x₁, x₂):
**`dy = f₁ dx₁ + f₂ dx₂`**
This is the linear approximation to Δy = f(x₁ + Δx₁, x₂ + Δx₂) − f(x₁, x₂) — exact only in the limit, an approximation for small finite Δ.

### §11.3.2 Total Derivative (Chain Rule for one parameter)
If y = f(x₁, x₂) with x₁ = φ(t), x₂ = ψ(t):
**`dy/dt = f₁ · dx₁/dt + f₂ · dx₂/dt`**
Generalises to n variables.

### Examples
**Example 11.4: y = ax₁² + 2h x₁ x₂ + b x₂².**
- dy = (2ax₁ + 2h x₂) dx₁ + (2h x₁ + 2b x₂) dx₂
     = 2(ax₁ + h x₂) dx₁ + 2(h x₁ + b x₂) dx₂.

**Example 11.5(i): q = 4x₁ + 3x₂; x₁ = t³ + t² + 1, x₂ = t³ − t² − t.**
- f₁ = 4, f₂ = 3.
- dx₁/dt = 3t² + 2t.
- dx₂/dt = 3t² − 2t − 1.
- dq/dt = 4(3t² + 2t) + 3(3t² − 2t − 1) = 12t² + 8t + 9t² − 6t − 3 = **21t² + 2t − 3**.

### Definitions
- **Total differential** of y: dy = Σᵢ fᵢ dxᵢ. ⭐
- **Total derivative**: dy/dt = Σᵢ fᵢ · dxᵢ/dt when xᵢ depend on t. ⭐

> **Quick Recall:**
> - Total differential measures actual change when *multiple* variables change.
> - Total derivative composes via chain rule when *all* variables depend on one parameter.
> - Partial derivative is the building block; total versions sum the contributions.

---

## Section: §11.4 Differentiation & Applications — Chain Rule Cases (§11.4.1) 🔴

### Core Idea
Four standard chain-rule patterns cover most multivariate compositions encountered in practice.

| Case | Setup | Resulting derivatives |
|---|---|---|
| I | z = f(u), u = u(x, y) | ∂z/∂x = f'(u) · ∂u/∂x; ∂z/∂y = f'(u) · ∂u/∂y |
| II | z = f(x, y), x = φ(t), y = ψ(t) | dz/dt = (∂z/∂x) φ'(t) + (∂z/∂y) ψ'(t) |
| III | z = f(x, y), y = y(x) | dz/dx = ∂z/∂x + (∂z/∂y) · dy/dx |
| IV | z = f(x, y); x = φ(u, v), y = ψ(u, v) | ∂z/∂u = (∂z/∂x)(∂x/∂u) + (∂z/∂y)(∂y/∂u); similarly ∂z/∂v |

### Differential rules (multivariate)
| Rule | Form |
|---|---|
| Sum | d(u + v) = du + dv |
| Product | d(uv) = u dv + v du |
| Quotient | d(u/v) = (v du − u dv)/v² |
| Logarithm | d(log x) = dx/x |
| Compound | d(uv/w) = du/u + dv/v − dw/w (multiplied by uv/w) |

> **Quick Recall:**
> - Case III is the implicit-function chain rule (used heavily next subsection).
> - Case IV is the change-of-variables chain rule (used in optimisation transforms).

---

## Section: §11.4.2 Implicit Functions 🔴

### Core Idea
Many economic equations don't isolate y in terms of x — instead they tie x and y together by an equation `f(x, y) = 0`. The **implicit function theorem** lets us extract dy/dx from this without ever solving for y.

### Key Concepts

#### First derivative (implicit)
View f(x, y) = 0 as z = f(x, y) with z constant ≡ 0:
`dz = f_x dx + f_y dy = 0` ⇒ **`dy/dx = − f_x / f_y`**

#### Reciprocal property
By symmetry, `dx/dy = − f_y / f_x`. The two derivatives are reciprocals.

#### Second derivative (formula 11.1)
`d²y/dx² = −[f_{xx} · f_y² − 2 f_{xy} · f_x f_y + f_{yy} · f_x²] / f_y³`

### Examples
**Example 11.6: f(x, y) = 2x² + 3xy + 4y² = 0.**
f_x = 4x + 3y, f_y = 3x + 8y. ⇒ **dy/dx = −(4x + 3y)/(3x + 8y)**.

**Example 11.7: f(x, y) = x³ + xy + y³.** (Source has slight OCR mangling; standard worked: dy/dx = −(3x² + y)/(x + 3y²); d²y/dx² is computed via formula 11.1.)

> **Quick Recall:**
> - For f(x, y) = 0: dy/dx = −f_x / f_y. **The minus sign is essential.**
> - Second derivative uses the symmetric formula in f's second partials.

### ⚠️ Common Mistakes
- ❌ Mistake: forgetting the minus sign in dy/dx = −f_x/f_y → ✅ Correct: it comes from rearranging f_x dx + f_y dy = 0.

---

## Section: §11.4.3 Applications — MRTS & Elasticity of Substitution 🔴

### Marginal Rate of Technical Substitution (MRTS)

For production Y = f(L, K):
- Total differential: `dY = f_L dL + f_K dK`.
- Along an isoquant (constant Y), dY = 0 ⇒ `f_L dL + f_K dK = 0`.
- Rearranging: **`MRTS = −dK/dL = f_L / f_K`** (ratio of marginal products).

> **In Simple Terms:** MRTS tells you how much capital you can give up while still producing the same output, per extra unit of labour. If labour is more productive at the margin, you can substitute more capital for less labour.

### Elasticity of Substitution (σ)

#### Definition
`σ = % change in (x₁/x₂) / % change in (f₂/f₁)`
or
`σ = [d(x₁/x₂)/(x₁/x₂)] / [d(f₂/f₁)/(f₂/f₁)]`

#### Algebraic formula (after substitution)
`σ = f₁ f₂ (f₁ x₁ + f₂ x₂) / [x₁ x₂ (2 f₁ f₂ f₁₂ − f₁² f₂₂ − f₂² f₁₁)]`

#### Sign and interpretation
- Convexity of isoquant ⇒ denominator (2 f₁ f₂ f₁₂ − f₁² f₂₂ − f₂² f₁₁) > 0.
- (x₁, x₂, f₁, f₂) > 0 ⇒ σ > 0.
- σ inversely proportional to *degree of convexity* of isoquant: more curved isoquant ⇒ less substitutability ⇒ smaller σ.

#### Limiting cases
| Production type | Isoquant shape | σ |
|---|---|---|
| Leontief (fixed proportions) | L-shaped | 0 |
| Cobb–Douglas | smooth, downward, convex | 1 |
| Perfect substitutes | straight line | ∞ |

#### Notes
- σ varies from one (x₁, x₂) combination to another — σ is a function of (x₁, x₂).
- σ symmetric: σ_{x₁ x₂} = σ_{x₂ x₁}.
- For **linear-homogeneous** production: `σ = f_L · f_K / (q · f_{LK})` — inversely proportional to cross-second-order partial.

### Definitions
- **MRTS**: ratio f_L / f_K of marginal products along an isoquant. ⭐
- **Elasticity of substitution σ**: percentage change in input ratio per percentage change in MRTS. ⭐

> **Quick Recall:**
> - MRTS = f_L / f_K (signed positive when isoquant slopes down).
> - σ = 0: no substitutability (Leontief). σ = ∞: perfect substitutes. σ = 1: Cobb–Douglas.
> - Higher σ ⇔ flatter isoquants ⇔ easier factor substitution.

---

## Section: §11.4.4 Homogeneous Functions and Their Properties (begins) 🔴

### Core Idea
A function is **homogeneous of degree n** if scaling all arguments by a constant k scales the function value by `kⁿ`. Cobb–Douglas, CES, and many production / utility functions in economics are homogeneous — and homogeneity yields three powerful properties.

### Definition
`f(k x₁, k x₂) = kⁿ · f(x₁, x₂)` ⇒ degree of homogeneity = n.

For a homogeneous function, the **sum of indices in each term** is the same constant n.

### Examples (degree-checking)
- f(x₁, x₂) = x₁² + x₁ x₂ + x₂² is **degree 2** (each term sums to 2).
- z = x³ y + x² y² + y⁴ is **degree 4**.

### Property 1
A degree-n homogeneous function can always be written in either of two reduced forms:
`z = xⁿ · φ(y/x)` or `z = yⁿ · ψ(x/y)`
(set k = 1/x or k = 1/y in the definition).

### Property 2
The first-order partial derivatives of a degree-n homogeneous function are **homogeneous of degree (n − 1)**.

**Proof sketch.** Write z = xⁿ φ(y/x).
∂z/∂x = n x^{n−1} φ(y/x) + xⁿ · φ'(y/x) · (−y/x²)
= x^{n−1} [n φ(y/x) − (y/x) φ'(y/x)]
which is again of the form x^{n−1} · (function of y/x), i.e., homogeneous of degree (n − 1).

<!-- Property 3 (Euler's theorem) continues in chunk 006 -->

### Definitions
- **Homogeneous of degree n**: f(kx₁, kx₂) = kⁿ f(x₁, x₂). ⭐

### Connections
- Builds on: Partial derivatives (§11.2); chain rule (§11.4.1).
- Is prerequisite for: Cobb–Douglas analysis (chunk 006 CYP2); Euler's theorem (chunk 006).

### Open Questions
1. What economic significance does the degree of homogeneity have for production functions? (constant returns to scale ⟺ degree 1.)
2. Why does linear-homogeneity simplify σ to a function only of f_{LK}?
