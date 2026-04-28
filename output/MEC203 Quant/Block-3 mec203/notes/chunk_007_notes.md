# Chunk 007 — Unit 12: Trig integration completion, Integration by Parts, Useful Formulae, Constant of Integration, Definite Integrals (Area, Riemann Sum), Properties
<!-- Pages: 61-70 -->
<!-- Source: chunk_007.txt -->

## Section: §12.4 Trigonometric Integration — completion 🟡
<!-- See chunk 006 for §12.4 intro -->

### Differentiation rules for trig (recap, used to derive integrals)
| Function | Derivative |
|---|---|
| sin A | cos A |
| cos A | −sin A |
| tan A | sec² A |
| cot A | −cosec² A |
| sec A | sec A · tan A |
| cosec A | −cosec A · cot A |

### Standard trig integration formulas
| Basic form | Generalised (linear arg ax + b) |
|---|---|
| ∫ cos x dx = sin x + C | ∫ cos(ax + b) dx = (1/a) sin(ax + b) + C |
| ∫ sin x dx = −cos x + C | ∫ sin(ax + b) dx = −(1/a) cos(ax + b) + C |
| ∫ tan x dx = −ln|cos x| + C | ∫ tan(ax + b) dx = −(1/a) ln|cos(ax + b)| + C |
| ∫ cot x dx = ln|sin x| + C | ∫ cot(ax + b) dx = (1/a) ln|sin(ax + b)| + C |
| ∫ sec x dx = ln|sec x + tan x| + C | (1/a) ln|sec(ax + b) + tan(ax + b)| + C |
| ∫ cosec x dx = ln|cosec x + cot x| + C (with a sign convention) | likewise (1/a) form |

### Examples
**Example 12.14: ∫ cos(15x) cos(4x) dx.** Use product-to-sum: cos A cos B = (1/2)[cos(A − B) + cos(A + B)].
`∫ cos(15x) cos(4x) dx = (1/2) ∫ [cos(11x) + cos(19x)] dx = (1/2) [(1/11) sin(11x) + (1/19) sin(19x)] + C`.

**Example 12.15: ∫ cos x sin⁵ x dx.**
u = sin x ⇒ du = cos x dx. ∫ u⁵ du = u⁶/6 + C = sin⁶ x / 6 + C.

**Example 12.16: ∫ sin⁵ x dx.**
sin⁵ x = (sin² x)² · sin x = (1 − cos² x)² · sin x. Set u = cos x ⇒ du = −sin x dx.
∫ sin⁵ x dx = −∫ (1 − u²)² du = −∫ (1 − 2u² + u⁴) du = −u + (2/3) u³ − u⁵/5 + C
= −cos x + (2/3) cos³ x − (1/5) cos⁵ x + C.

**Example 12.17: ∫ (3 sin x − 4 sec² x) dx = −3 cos x − 4 tan x + C.**

**Example 12.18: ∫ cos(2x − 6) dx.** u = 2x − 6 ⇒ du = 2 dx. ∫ cos u · du/2 = sin u / 2 + C = sin(2x − 6)/2 + C.

> **Quick Recall:**
> - Product-to-sum identities turn cos×cos, sin×cos, sin×sin into sums of single trig functions.
> - For odd powers of sin (or cos), peel off one factor to combine with du.
> - Linear-argument trick: ∫ f(ax + b) dx = (1/a) F(ax + b) where F is the antiderivative of f.

---

## Section: §12.5 Integration by Parts 🔴

### Core Idea
When the integrand is a **product** of two functions and substitution doesn't work, integration by parts is the technique of choice. It comes directly from the product rule for derivatives.

### Derivation
Product rule: `d(uv)/dx = u' v + u v'`. Integrating both sides:
`uv = ∫ u' v dx + ∫ u v' dx`.
Rearranging:
**`∫ u v' dx = uv − ∫ v u' dx`**

In differential form:
`∫ u dv = uv − ∫ v du`.

### Mechanisms / Processes (choosing u and dv)
1. Pick u: the part that **simplifies on differentiation** (e.g., x → 1, ln x → 1/x).
2. Pick dv: the part you **can integrate** (e.g., sin x dx, eˣ dx).
3. Compute du = u' dx and v = ∫ dv.
4. Apply the formula `∫ u dv = uv − ∫ v du`.
5. Evaluate the new integral; if needed, apply by-parts again.

**LIATE heuristic** (priority order for u): Logarithmic, Inverse trig, Algebraic, Trigonometric, Exponential.

### Examples
**Example 12.19: ∫ x e^{−x} dx.**
- u = x, dv = e^{−x} dx.
- du = dx, v = −e^{−x}.
- ∫ x e^{−x} dx = −x e^{−x} − ∫ (−e^{−x}) dx = −x e^{−x} − e^{−x} + C = −(1 + x) e^{−x} + C.

**Example 12.20: ∫ (3t + 5) cos(t/4) dt.**
- u = 3t + 5, dv = cos(t/4) dt.
- du = 3 dt, v = 4 sin(t/4).
- ∫ = 4(3t + 5) sin(t/4) − 12 ∫ sin(t/4) dt = 4(3t + 5) sin(t/4) + 48 cos(t/4) + C.

**Example 12.21: ∫ x ln x dx.**
- u = ln x, dv = x dx (LIATE: log first).
- du = dx/x, v = x²/2.
- ∫ x ln x dx = (x²/2) ln x − ∫ (x²/2) · (1/x) dx = (x²/2) ln x − x²/4 + C.

> **Quick Recall:**
> - `∫ u dv = uv − ∫ v du`.
> - LIATE: pick u from earlier in L-I-A-T-E.
> - Repeat by-parts when the new integral still has a product (e.g., for x² eˣ, two by-parts).

### ⚠️ Common Mistakes
- ❌ Mistake: forgetting the minus sign in `−∫ v du` → ✅ Correct: it comes straight from rearranging the product rule.

---

## Section: §12.6 Some Useful Formulae 🔴

| # | Formula | Notes |
|---|---|---|
| 1 | `∫ xⁿ dx = x^{n+1}/(n+1) + C` | n ≠ −1 |
| 2 | `∫ x^{−1} dx = ∫ dx/x = ln |x| + C` | for x ≠ 0 |
| 3 | `∫ e^{mx} dx = e^{mx}/m + C` | for any m ≠ 0 |
| 4 | `∫ a^{mx} dx = a^{mx}/(m ln a) + C` | a > 0, a ≠ 1 |
| 5 | `∫ cos(ax) dx = sin(ax)/a + C` | |
| 6 | `∫ sin(ax) dx = −cos(ax)/a + C` | |
| 7 | `∫ [k₁ f(x) + k₂ g(x)] dx = k₁ ∫ f(x) dx + k₂ ∫ g(x) dx + C` | linearity, k₁, k₂ constants |

> **Quick Recall:**
> - **Memorise these seven** — they cover most direct integrals encountered.

---

## Section: §12.7 Determining the Constant of Integration 🟡

### Core Idea
Indefinite integrals come with a **family** of solutions parameterised by C. A specific (initial or boundary) condition fixes C uniquely.

### Mechanisms / Processes
1. Find the general antiderivative F(x) + C.
2. Plug in the boundary point: y₀ = F(x₀) + C.
3. Solve for C: C = y₀ − F(x₀).
4. Write the unique solution: y = F(x) + C.

### Example
∫(x² + 3) dx = x³/3 + 3x + C. With y(0) = 20: 20 = 0 + 0 + C ⇒ C = 20. Unique answer: `y = x³/3 + 3x + 20`.

> **Quick Recall:**
> - One initial condition fixes one constant of integration.

---

## Section: §12.8 Definite Integrals 🔴

### Core Idea
The **definite integral** `∫ₐᵇ f(x) dx` is a *number* — geometrically, the signed area between the curve y = f(x) and the x-axis from x = a to x = b.

### §12.8.1 Finding Area — rectangles approximation

#### Setup
Divide [a, b] into n subintervals each of width `Δx = (b − a)/n`. End points: x₀ = a, x₁ = a + Δx, …, xₙ = b. From each subinterval pick a point xᵢ* and use f(xᵢ*) as the rectangle's height.

| Choice of height | Approx area |
|---|---|
| Right endpoint | Σᵢ f(xᵢ) Δx |
| Left endpoint | Σᵢ f(xᵢ₋₁) Δx |
| Midpoint | Σᵢ f((xᵢ₋₁ + xᵢ)/2) Δx |

For an increasing function on [a, b]:
- Right endpoints **overestimate**.
- Left endpoints **underestimate**.
- Midpoint typically gives the best approximation for fixed n.

#### Worked example: f(x) = x² + 1 on [0, 2] with n = 4
- Δx = 0.5; partition x₀=0, x₁=0.5, x₂=1, x₃=1.5, x₄=2.
- Right-endpoint sum A_R = 0.5[f(0.5) + f(1) + f(1.5) + f(2)] = 0.5[1.25 + 2 + 3.25 + 5] = 5.75.
- Left-endpoint sum A_L = 0.5[f(0) + f(0.5) + f(1) + f(1.5)] = 0.5[1 + 1.25 + 2 + 3.25] = 3.75.
- True value (from §12.8.2 below): ∫₀² (x² + 1) dx = 14/3 + 2 ≈ 4.67. (Right overestimates, left underestimates.)

> **In Simple Terms:** Slicing the area into vertical strips and summing strip-areas. The thinner the strip (larger n), the closer to the true area. The limit is the definite integral.

### §12.8.2 Definition via Riemann Sum

Given a continuous f on [a, b], partition into n equal subintervals of width Δx, choose any xᵢ* in each:
**`∫ₐᵇ f(x) dx = lim_{n→∞} Σᵢ₌₁ⁿ f(xᵢ*) Δx`**

This sum is the **Riemann sum**.

### Examples
**Example 12.22: ∫₀³ (x² + 1) dx.**
Source uses formula with right endpoints, computing as a sum:
`= lim_{n→∞} Σᵢ f(xᵢ) (b − a)/n` and arrives at value 12.
Alternatively, by the FTC (chunk 008): F(x) = x³/3 + x ⇒ F(3) − F(0) = 9 + 3 = **12**. ✓

### Definitions
- **Riemann sum**: Σᵢ f(xᵢ*) Δxᵢ for a partition of [a, b]. ⭐
- **Definite integral**: limit of Riemann sums as the partition gets infinitely fine. ⭐
- **Mesh size**: max width of subintervals in the partition.

> **Quick Recall:**
> - Riemann sum: pick a point in each strip, sum height × width.
> - Limit (mesh → 0) is the definite integral.

---

## Section: §12.8.3 Properties of Definite Integral 🔴

| # | Property |
|---|---|
| 1 | `∫ₐᵇ 1 dx = b − a` |
| 2 | `∫ₐᵇ c · f(x) dx = c · ∫ₐᵇ f(x) dx` (constant factors out) |
| 3 | `∫ₐᵇ [f + g] dx = ∫ₐᵇ f dx + ∫ₐᵇ g dx` (linearity) |
| 4 | `∫ₐᵇ f dx = ∫ₐᶜ f dx + ∫ᶜᵇ f dx` (additivity over intervals; a ≤ c ≤ b) |
| 5 | If 0 ≤ f(x) ≤ g(x) on [a, b], then `0 ≤ ∫ₐᵇ f dx ≤ ∫ₐᵇ g dx` (comparison) |
| 6 | `∫ₐᵃ f(x) dx = 0` (degenerate interval = 0 area) |
| 7 | `∫ₐᵇ f(x) dx = − ∫_b^a f(x) dx` (reversing bounds flips sign) |

### Examples
**Property 4 illustration:** ∫₁³(2x+3)dx = 14, ∫₃⁵(2x+3)dx = 22 ⇒ ∫₁⁵ = 14 + 22 = 36.
**Property 6: ∫₂² (3x + 4) dx = 0.**
**Property 7: If ∫₁⁴ x³ dx = 21, then ∫₄¹ x³ dx = −21.**

> **Quick Recall:**
> - Same bounds → 0.
> - Flipping bounds → flip sign.
> - Linearity (scalar + sum) extends to definite integrals just as for indefinite.

### Connections
- Builds on: Indefinite integral (§12.2); area-as-sum interpretation; FTC (§12.9 in chunk 008) ties indefinite and definite together.
- Is prerequisite for: Fundamental theorem (§12.9), area calculations (§12.10), improper integrals (§12.11).

### Open Questions
1. Why must f be continuous (or at least Riemann-integrable) for the limit definition to apply? (Pathological functions can have ill-defined Riemann sums.)
2. Can a definite integral be negative? (Yes — when f(x) < 0 on parts of [a, b]; the integral measures *signed* area.)
