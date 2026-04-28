# Chunk 002 — Unit 16 (continued) — Multivariate SOC, Hessian, Examples
<!-- Pages: 11-20 -->
<!-- Source: chunk_002.txt -->
<!-- See chunk 001 for start of Unit 16 -->

## Section: Sufficient Condition for Bivariate Extreme Values 🔴

### Core Idea
For `y = f(x₁, x₂)` with FOC `f₁ = f₂ = 0` already satisfied, the sufficient condition asks whether `d²y` is everywhere negative (max), everywhere positive (min), or sign-indefinite (saddle/inflexion). After expanding `d²y` and using **Young's theorem** (`f₁₂ = f₂₁`), the test reduces to checking signs of three numbers: `f₁₁`, `f₂₂`, and the determinant `f₁₁f₂₂ - f₁₂²`.

> **In Simple Terms:** Past the flat spot, ask "what happens if I wiggle in any direction?" If you always go down → max. Always up → min. Sometimes up, sometimes down → saddle.

### Mechanisms / Processes

Starting from `dy = f₁ dx₁ + f₂ dx₂ = 0`, totally differentiate:
`d²y = f₁₁(dx₁)² + 2f₁₂ dx₁ dx₂ + f₂₂(dx₂)²`

Treat as quadratic form in `dx₁, dx₂`:
`q = au² + 2huv + bv²`
where `a = f₁₁, b = f₂₂, h = f₁₂, u = dx₁, v = dx₂`.

Complete the square:
`q = a[(u + (h/a)v)² + ((ab - h²)/a²)v²]`

Hence:
- `q < 0` ⟺ `a < 0` AND `ab - h² > 0` (which forces `b < 0` too).
- `q > 0` ⟺ `a > 0` AND `ab - h² > 0` (forces `b > 0` too).

### Key Concepts

| Condition on (f₁₁, f₂₂, f₁₁f₂₂ - f₁₂²) | Result |
|----------------------------------------|--------|
| `f₁₁ < 0`, `f₂₂ < 0`, `f₁₁f₂₂ - f₁₂² > 0` | **Maximum** |
| `f₁₁ > 0`, `f₂₂ > 0`, `f₁₁f₂₂ - f₁₂² > 0` | **Minimum** |
| `f₁₁f₂₂ < f₁₂²` and `f₁₁`, `f₂₂` have **different** signs | **Saddle point** |
| `f₁₁f₂₂ < f₁₂²` and `f₁₁`, `f₂₂` have **same** sign | **Inflexion point** |
| `f₁₁f₂₂ = f₁₂²` | Inconclusive |

### Definitions
- **Hessian determinant** (2×2): `|H| = | f₁₁ f₁₂ ; f₂₁ f₂₂ |`. ⭐ (exam-important)
- **Saddle point**: stationary point that is a max in one direction and a min in another. ⭐
- **Young's theorem**: For functions with continuous mixed partials, `f₁₂ = f₂₁`. ⭐
- **Principal minor**: a sub-determinant of the Hessian formed by the first `i` rows and columns. ⭐

### Matrix Form
Quadratic form `q = au² + 2huv + bv²` rewrites as `[u v] [[a h];[h b]] [u; v]`.
The matrix `[[a h];[h b]]` supplies the conditions:
- `q > 0` ⟺ `|a| > 0` AND `|H| > 0` (both leading principal minors positive).
- `q < 0` ⟺ `|a| < 0` AND `|H| > 0` (alternating signs).

> **Quick Recall:**
> - Bivariate min: `f₁₁ > 0`, `|H| > 0`.
> - Bivariate max: `f₁₁ < 0`, `|H| > 0`.
> - Saddle: `|H| < 0`.

---

## Section: Three-Variable Extrema (Principal Minors) 🔴

### Core Idea
For `z = f(x, y, w)`, the second-differential quadratic form has 3×3 Hessian
`H = [[fₓₓ, fₓᵧ, fₓw]; [fᵧₓ, fᵧᵧ, fᵧw]; [fwₓ, fwᵧ, fww]]`.
There are **three** principal minors `D₁, D₂, D₃`. The signs determine extremum type, generalising the bivariate result.

### Key Concepts

| Quadratic form | Principal minor pattern | Result |
|----------------|------------------------|--------|
| `q > 0` (`d²z` positive definite) | `D₁ > 0`, `D₂ > 0`, `D₃ > 0` | **Minimum** |
| `q < 0` (`d²z` negative definite) | `D₁ < 0`, `D₂ > 0`, `D₃ < 0` | **Maximum** |

In words:
- **All positive** ⟹ minimum.
- **Alternating starting with negative** ⟹ maximum.

### Definitions
- **D₁** = `fₓₓ` (1×1 leading minor).
- **D₂** = `|fₓₓ fₓᵧ ; fᵧₓ fᵧᵧ|` (2×2 leading minor).
- **D₃** = `|H|` (full 3×3 determinant).

---

## Section: n-Variable Extrema — Hessian Determinantal Test 🔴

### Core Idea
Generalising to `z = f(x₁, ..., xₙ)`:
- FOC: all `n` first partials vanish, `f₁ = f₂ = ... = fₙ = 0`.
- SOC: examine the `n` leading principal minors `|H₁|, |H₂|, ..., |Hₙ|`.

### Key Concepts

| Condition | Maximum | Minimum |
|-----------|---------|---------|
| FOC | `dz = 0`, i.e. `f₁ = f₂ = ... = fₙ = 0` | same |
| SOC | `\|H_i\|` alternate in sign starting negative: `\|H₁\| < 0`, `\|H₂\| > 0`, `\|H₃\| < 0`, ... | All `\|H_i\| > 0` |

Compactly:
- **Maximum**: `(-1)^i |Hᵢ| > 0` for `i = 1, ..., n`.
- **Minimum**: `|Hᵢ| > 0` for `i = 1, ..., n`.

### ⚠️ Common Mistakes
- ❌ Checking only `|Hₙ|` (the full determinant) → ✅ All leading principal minors must be checked.
- ❌ Forgetting that for max, the **first** minor `|H₁|` must be negative (not the last) → ✅ Sign pattern starts negative for max.

> **Quick Recall:**
> - Min: every `\|H_i\|` is **positive**.
> - Max: signs **alternate** starting with **negative**.

---

## Section: Worked Examples — Multivariate Extrema 🔴

### Examples

**Example 16.4 (i)** — Determine whether `Z = x₁² - 3x₁x₂ + 3x₂² + 4x₂x₃ + 6x₃²` is a max or a min.

FOC:
- `f₁ = 2x₁ - 3x₂ = 0`
- `f₂ = -3x₁ + 6x₂ + 4x₃ = 0`
- `f₃ = 4x₂ + 12x₃ = 0`

Solving: `x₁ = 0, x₂ = 0, x₃ = 0`. Stationary point: origin.

Hessian:
```
|H| = | 2  -3   0 |
      | -3  6   4 |
      | 0   4  12 |
```
- `|H₁| = 2 > 0`
- `|H₂| = | 2 -3 ; -3 6 | = 12 - 9 = 3 > 0`
- `|H₃| = 2(72 - 16) - (-3)(-36 - 0) + 0 = 112 - 108 = 4 > 0`

All positive → **minimum** at `(0, 0, 0)` with value 0.

**Example 16.4 (ii)** — `v = -x³ + 3xz + 2y - y² - 3z²`.

FOC: `f₁ = -3x² + 3z = 0`, `f₂ = 2 - 2y = 0`, `f₃ = 3x - 6z = 0`.
Solving: stationary points at `(0, 1, 0)` and `(1/2, 1, 1/4)`.

Hessian: `|H| = | -6x 0 3 ; 0 -2 0 ; 3 0 -6 |`.
- At `(0, 1, 0)`: `f₁₁ = 0`, so SOC fails — inconclusive.
- At `(1/2, 1, 1/4)`: `|H₁| = -3 < 0`, `|H₂| = 6 > 0`, `|H₃| = -18 < 0` → alternating signs → **maximum**, with value `17/16`.

> **Quick Recall:**
> - Always evaluate the Hessian **at** the stationary point — its sign-pattern can vary across the domain.
> - If `|H₁| = 0` at a stationary point, SOC is inconclusive; need higher-order test.

---

## Section: Unit 16 Key Words & Answers 🟡

### Definitions
- **Local (relative) maxima/minima**: function attains the extremum only in some neighbourhood; can be non-unique.
- **Global (absolute) maxima/minima**: extremum across the entire domain; unique for a continuous function.
- **Point of inflexion**: a point where curvature changes; sufficient condition `f''(x) = 0` and `f'''(x) ≠ 0`.
- **Stationary point**: a point where first-order derivatives are zero; the function value there is a stationary value.

### Check Your Progress 3 — Bivariate
1. `z = 3x² + 6xy + 7y²`: FOC gives `(0, 0)`; `f_xx = 6 > 0`, `f_yy = 14 > 0`, `f_xx f_yy - f_xy² = 84 - 36 = 48 > 0` → **minimum**, value 0.
2. `z = 4x² - 2y² + 7xy`: FOC gives `(0, 0)`; `f_xx = 8`, `f_yy = -4` (opposite signs), `f_xx f_yy - f_xy² = -32 - 49 < 0` → **saddle point**.

### Check Your Progress 4
- (a) `z = 2x² + xy + 4y² + xz + z² + 2`: No max or min.
- (b) `z = e^(-x) - e^y + e^z - 2(x + e^z) + y`: Max at `(0, 0, 0)`.

---

## Section: Unit 16 Exercises 🟡

**Q1**: Maxima and minima of `f(x) = 1 + 2 sin x + 3 cos²x` on `0 ≤ x ≤ π/2`.
- `f'(x) = 2 cos x - 6 cos x sin x = 2 cos x (1 - 3 sin x)`.
- `f'(x) = 0` when `cos x = 0` (i.e. `x = π/2`) or `sin x = 1/3`.
- At `cos x = 0` (`sin x = 1`): `f''(x) = -2(1) - 6(0 - 1) = 4 > 0` → **min**, value `f = 1 + 2(1) + 0 = 3`.
- At `sin x = 1/3`: `f''(x) = -2(1/3) - 6(1 - 2/9) = -2/3 - 14/3 < 0` → **max**.
  Maximum value: `1 + 2(1/3) + 3(1 - 1/9) = 1 + 2/3 + 8/3 = 1 + 10/3 = 13/3`. (Source gives `4` — note minor OCR drift; algebra confirms `13/3 ≈ 4.33`.)

**Q2**: `y = x₁³ + 2x₂³ - 6x₁² + 9x₂² - 63x₁ - 60x₂ - 24`.
- `(x₁, x₂) = (-3, 2)`: saddle.
- `(7, -5)`: saddle.
- `(-3, -5)`: relative maximum.
- `(7, 2)`: relative minimum.

**Q3**: `y = -x₁³ + 9x₁ - 4x₂²`.
- FOC: `-3x₁² + 9 = 0` ⟹ `x₁ = ±√3`; `-8x₂ = 0` ⟹ `x₂ = 0`.
- At `(√3, 0)`: maximum. At `(-√3, 0)`: saddle.

### Connections
- Builds on: Univariate extrema (Chunk 001).
- Is prerequisite for: Unconstrained optimisation in economic problems (Chunk 003).

> **Quick Recall:**
> - For each stationary point, compute the Hessian **at that point**.
> - Different stationary points of the same function can have different natures.
