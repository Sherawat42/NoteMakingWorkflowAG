# Chunk 004 — Unit 10 wrap-up (Taylor, MVT, L'Hôpital, Solved Exercises) + Unit 11 begin
<!-- Pages: 31-40 -->
<!-- Source: chunk_004.txt -->

## Section: §10.8 Taylor Series 🔴

### Core Idea
Many functions can be approximated near a point x = a by a polynomial whose coefficients are determined by f and its derivatives evaluated at a. This is the **Taylor expansion** — the central tool for local analysis, optimization conditions, and numerical evaluation.

> **In Simple Terms:** Imagine guessing a function near x = a. The constant term matches f(a). The linear term matches the slope (the tangent). The quadratic term curves the approximation correctly. Each higher-degree term refines the match. As you add more terms, the polynomial hugs the function more tightly.

### Key Concepts

#### Form of the polynomial
We seek `f_n(x) = a₀ + a₁(x − a) + a₂(x − a)² + … + aₙ(x − a)ⁿ` such that f_n agrees with f at x = a and its derivatives match up to order n.

Setting `x = a` and matching successive derivatives:
- a₀ = f(a)
- a₁ = f'(a)
- a₂ = f''(a)/2!
- ⋮
- aⱼ = f⁽ʲ⁾(a) / j!

#### Taylor series with Lagrange remainder
`f(x) = f(a) + f'(a)(x − a) + (f''(a)/2!)(x − a)² + … + (f⁽ⁿ⁾(a)/n!)(x − a)ⁿ + Rₙ`
where `Rₙ = f⁽ⁿ⁺¹⁾(x*)/(n+1)! · (x − a)^{n+1}` for some `x* = a + θ(x − a)`, 0 < θ < 1.

#### Maclaurin series
Special case **a = 0**:
`f(x) = f(0) + x f'(0) + (x²/2!) f''(0) + (x³/3!) f'''(0) + …`

### Definitions
- **Analytic function** (in this unit): one expressible as a power series of the above form. ⭐
- **Lagrange remainder**: the term `f⁽ⁿ⁺¹⁾(x*)(x − a)^{n+1}/(n+1)!` controlling truncation error.
- **Maclaurin series**: Taylor series centred at zero. ⭐

### Examples (from CYP2)
| f(x) | Maclaurin series |
|---|---|
| eˣ | `1 + x + x²/2! + x³/3! + … + xⁿ/n! + …` |
| sin x | `x − x³/3! + x⁵/5! − x⁷/7! + …` |
| cos x | `1 − x²/2! + x⁴/4! − x⁶/6! + …` |
| log(1 + x) | `x − x²/2 + x³/3 − x⁴/4 + …` (defined for −1 < x ≤ 1) |

> **Quick Recall:**
> - Taylor at a; Maclaurin at 0.
> - aⱼ = f⁽ʲ⁾(a)/j!.
> - Series for log(1+x) converges only for −1 < x ≤ 1.

### ⚠️ Common Mistakes
- ❌ Mistake: applying Maclaurin to functions like log x at x = 0 → ✅ Correct: log x is undefined at 0; use log(1 + x) instead.

---

## Section: §10.9 Mean Value Theorem (MVT) and L'Hôpital's Rule 🔴

### Core Idea
The **MVT** says that if a function is smooth enough on an interval, its average rate of change over the interval is realised at some interior point. **L'Hôpital's Rule** uses derivatives to evaluate indeterminate-form limits (0/0, ∞/∞).

### Key Concepts

#### Mean Value Theorem (MVT)
If (i) f is continuous on the closed interval [a, b], and (ii) f' exists on the open interval (a, b), then ∃ c ∈ (a, b) such that:
`f(b) − f(a) = (b − a) · f'(c)`

Equivalent (set b = a + h, c = a + θh, 0 < θ < 1):
`f(a + h) = f(a) + h · f'(a + θh)`

#### Derivation from Taylor (n = 1)
Putting n = 1 in the Taylor formula and writing R₀ = f'(a)(x − a) gives the **linearisation** of f.

#### L'Hôpital's Rule
If `f(x) = g(x)/h(x)` with both g, h → 0 (or both → ∞) as x → a, then:
`lim_{x→a} g(x)/h(x) = lim_{x→a} g'(x)/h'(x)` (if the latter limit exists).

### Examples
**Example 10.9(a): `lim_{x→0} (eˣ − 1)/x`** — both → 0/0.
g(x) = eˣ − 1, h(x) = x. g'(x) = eˣ, h'(x) = 1. Limit = e⁰/1 = **1**.

**Example 10.9(b): `lim_{x→0} ((1+x)ⁿ − 1)/x`** — 0/0.
g'(x) = n(1+x)^{n−1}, h'(x) = 1. Limit = n.

**CYP2(2)(i): `lim_{x→0} log(1+x)/x = 1`** by L'Hôpital (1/(1+x) over 1).

**CYP2(2)(ii): `lim_{x→1} (x³ + 3x − 4)/(2x² + x − 3)`**
0/0 ⇒ apply L'Hôpital: (3x² + 3)/(4x + 1). At x = 1: 6/5 — wait, source says 3/2; checking: (3·1+3)/(4·1+1) = 6/5. Source gives 3/2 but appears to drop the +3 term mid-step (OCR/typesetting confusion). The robust approach: factor `(x−1)` out of both numerator and denominator and evaluate cleanly.

### Definitions
- **Mean Value Theorem**: existence of c ∈ (a, b) where instantaneous rate equals average rate. ⭐
- **L'Hôpital's Rule**: the limit of a 0/0 (or ∞/∞) ratio equals the limit of the derivative ratio (if it exists). ⭐
- **Linearisation**: first-order Taylor approximation, f(x) ≈ f(a) + f'(a)(x − a).

> **Quick Recall:**
> - MVT requires continuity on [a,b] *and* differentiability on (a,b).
> - L'Hôpital applies only after confirming an indeterminate form (0/0 or ∞/∞).
> - MVT + Taylor at n=1 gives linearisation.

### ⚠️ Common Mistakes
- ❌ Mistake: applying L'Hôpital without checking indeterminate form → ✅ Correct: confirm 0/0 or ∞/∞ first; otherwise the rule gives a wrong answer.
- ❌ Mistake: differentiating numerator and denominator using the quotient rule → ✅ Correct: differentiate them **separately** (not as a quotient).

---

## Section: §10.10–§10.12 Sum-Up, Key Words, CYP Solutions 🟢

### Unit 10 Sum-Up (§10.10)
Unit 10 covered: differentiation rules; AR/MR, AC/MC, elasticity (price + income); slope and curvature; and three theorems — Taylor, MVT, L'Hôpital.

### Key Words (§10.11)
- **Derivative**: the limiting value of the ratio of change in a function to the corresponding change in its independent variable.
- **Differential coefficient (or derivative)**: a measure of the rate of change of a given function.
- **L'Hôpital's Rule**: used to evaluate indeterminate forms — limit equals limit of derivative ratio.
- **Mean Value Theorem**: ∃ point where derivative equals slope of secant joining endpoints.
- **Taylor Series**: infinite sum giving f(z) near a in terms of derivatives at a.

### Selected CYP1 derivative results
| f(x) | dy/dx |
|---|---|
| sin²x − eˣ + 4ˣ | sin 2x − eˣ + 4ˣ log_e 4 |
| 3x² cosec x | 3 cosec x (2x − cot x) |
| (log x − sin x)/(2x² − 1) | [(2x²−1)(1/x − cos x) − 4x(log x − sin x)] / (2x² − 1)² |
| 2 cos v + tan² v, v = e^{3x} | 6 e^{3x}[tan(e^{3x}) sec²(e^{3x}) − sin(e^{3x})] |
| x = b sin θ, y = a cos θ | −(a/b) tan θ |

### CYP1(3) — n-th derivatives
- d^n(eˣ)/dxⁿ = eˣ for all n.
- d^n(sin x)/dxⁿ cycles: sin x → cos x → −sin x → −cos x → sin x …
- d^n(log(1+x))/dxⁿ = (−1)^{n−1}(n−1)! · (1+x)^{−n}.

### Selected §10.13 Exercises (Solved)
**Q1: AC = q² − 2q + 5, max capacity 30 units.** d(AC)/dq = 2q − 2 ⇒ AC decreases for 0 < q < 1, increases for 1 < q < 30.

**Q2: c = a e^{bq}.** AC = (a e^{bq})/q; MC = ab e^{bq}. AC = MC ⇒ q = 1/b.

**Q3: Production q = −L³/3 + 2L² + 12L.** APL = q/L = −L²/3 + 2L + 12. d(APL)/dL = −2L/3 + 2 = 0 ⇒ L = 3. Beyond L = 3, average product diminishes.

**Q4: Demand p^k = a/q (i.e., q p^k = a, or q = a p^{−k}).** ε_p = −k. (Source's reasoning: −k log p = log a − log q; differentiate both sides; ε_p = q · (1/q) · (−k/p) · p / 1 = −k.)

**Q5: c = q³/3 − q² + q + 5.** MC = q² − 2q + 1 = (q − 1)²; d(MC)/dq = 2(q − 1). For q < 1, MC is decreasing; for q > 1, MC increasing — so for "continually right" q the behaviour switches at q = 1.

> **Quick Recall:**
> - Plug-and-chug exercises drill chain rule + quotient rule fluency.
> - For optimisation, set d/dq = 0 and check second derivative.

---

## Section: Unit 11 Front Matter (§11.0–§11.1) 🟢

### Core Idea
Unit 11 generalises differentiation to functions of *several* variables — central to all real-world economics where outputs depend on multiple inputs (utility on goods, output on labour and capital, demand on price *and* income).

### §11.0 Objectives
- Define partial derivatives.
- Compute higher-order and cross-partial derivatives (Young's theorem).
- Distinguish total derivative vs total differential.
- Identify homogeneous functions (Cobb–Douglas as a key example) and use Euler's theorem.

---

## Section: §11.2 Concept of Partial Differentiation 🔴

### Core Idea
When y depends on x₁, x₂, …, the **partial derivative** of y with respect to xᵢ measures how y changes if xᵢ alone varies — all other variables held constant. This is the natural multivariate generalisation of the single-variable derivative.

> **In Simple Terms:** In a recipe for cake quality y = f(flour, sugar, time), the partial derivative ∂y/∂flour answers: "if I change *only* the flour and keep sugar and time fixed, by how much does cake quality change per gram of flour?" Total change is something different (handled by total differential / total derivative).

### Key Concepts

#### Setting up bivariate case
For y = f(x₁, x₂):
- Change x₁ alone (x₂ fixed) ⇒ partial derivative w.r.t. x₁ — denoted `∂y/∂x₁`, `f₁`, `f_{x₁}`.
- Change x₂ alone ⇒ ∂y/∂x₂.
- If x₁ and x₂ are *related* (e.g., x₂ depends on x₁), the **total derivative** of y w.r.t. x₁ accounts for both direct and indirect effects.

#### Why this matters
Most economic problems are multivariate:
- Utility U = f(x₁, x₂, …) of multiple goods.
- Production Q = f(L, K, land, …).
- Demand q = f(p, y) of price and income.

<!-- Continues in chunk 005: §11.2.1 Partial derivative defined formally, examples, higher orders, cross-partials -->

### Connections
- Builds on: Derivative (§10.2) — partial derivative is the single-variable derivative applied along one axis.
- Is prerequisite for: Total differential, total derivative (§11.3); MRTS, elasticity of substitution (§11.4.3); homogeneous functions and Euler's theorem (§11.4.4).

### Open Questions
1. How does Young's theorem (cross-partials equal) interact with discontinuous second derivatives?
2. When two variables are related, why is the *total* derivative the relevant economic concept rather than the partial?
