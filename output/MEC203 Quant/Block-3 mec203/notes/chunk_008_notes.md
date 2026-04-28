# Chunk 008 — Unit 12: Fundamental Theorem of Calculus, Integration with Chain Rule, Improper Integrals, Partial Fractions
<!-- Pages: 71-80 -->
<!-- Source: chunk_008.txt -->

## Section: §12.9 Fundamental Theorem of Calculus (FTC) 🔴

### Core Idea
The FTC bridges differentiation and integration — two apparently independent operations — and is the engine that converts "find the area" into "find an antiderivative". The theorem has two parts: one says antidifferentiation can be reversed by differentiation; the other says the definite integral can be computed by evaluating an antiderivative at the endpoints.

> **In Simple Terms:** Integration and differentiation are inverse operations, like multiplication and division. Once you know any antiderivative F of f, the area under f from a to b is just F(b) − F(a). No more Riemann sums.

### Part 1 — Differentiation undoes integration
For continuous f on [a, b], define `F(x) = ∫ₐˣ f(t) dt`. Then:
**`F'(x) = f(x)`** and equivalently **`d/dx ∫ₐˣ f(t) dt = f(x)`**.

Every continuous f has an antiderivative; varying the lower limit gives the family of antiderivatives differing by constants.

### Part 2 — Evaluating definite integrals
For f continuous on [a, b] with **any** antiderivative F:
**`∫ₐᵇ f(x) dx = F(b) − F(a)`**

### Examples
**Example 12.25: d/dx ∫₃ˣ 4 t³ dt.**
The antiderivative inside is t⁴, so the integral equals x⁴ − 3⁴ = x⁴ − 81. d/dx of that is 4x³. (Equivalently: by Part 1 directly, derivative = integrand evaluated at x = 4x³.)

**Example 12.26: d/dx ∫₂^{sin x} e^{t²} dt.**
By Part 1 with chain rule (since the upper limit is sin x, not just x): the inner antiderivative G(u) = ∫₂ᵘ e^{t²} dt has G'(u) = e^{u²}. So d/dx [G(sin x)] = e^{sin² x} · cos x. Source's stated answer e^{x²} omits the chain factor — careful here.

**Example 12.27: ∫₂³ x² dx = [x³/3]₂³ = 27/3 − 8/3 = 19/3.**

**Example 12.28: ∫₀² (t² − 3t + 10) dt = [t³/3 − 3t²/2 + 10t]₀² = 8/3 − 6 + 20 = 8/3 + 14 = 50/3 ≈ 16.67.**

### Definitions
- **Antiderivative (or indefinite integral)**: any function F with F'(x) = f(x). ⭐
- **Fundamental Theorem of Calculus (Part 2)**: ∫ₐᵇ f(x) dx = F(b) − F(a). ⭐

> **Quick Recall:**
> - Part 1: derivative of "area function" = integrand.
> - Part 2: ∫ₐᵇ f = F(b) − F(a) for *any* antiderivative F.
> - Two antiderivatives differ by a constant — so the choice of F doesn't matter.

### ⚠️ Common Mistakes
- ❌ Mistake: applying Part 1 to ∫_{a}^{g(x)} f(t) dt as just f(x) → ✅ Correct: the chain rule gives f(g(x)) · g'(x).

---

## Section: §12.10 Integration & the Chain Rule (Net Area, Definite Substitution) 🟡

### Net area between graph and x-axis
The definite integral ∫ₐᵇ f(x) dx gives **signed (net) area**: positive contributions where f > 0, negative where f < 0. To get *actual* total area (always positive), split at zeros and integrate the absolute value.

### Examples
**Example 12.29: Area between y = 7 − x² and the x-axis on [−1, 2].**
∫_{−1}² (7 − x²) dx = [7x − x³/3]_{−1}² = (14 − 8/3) − (−7 + 1/3) = 14 − 8/3 + 7 − 1/3 = 21 − 9/3 = 21 − 3 = 18.

**Example 12.30: Net area of y = sin x on [0, 2π].**
∫₀^{2π} sin x dx = [−cos x]₀^{2π} = −1 − (−1) = **0** (net cancels: positive lobe on (0, π), negative on (π, 2π)).
Actual *total* area = ∫₀^π sin x dx + |∫_π^{2π} sin x dx| = 2 + 2 = 4.

### §12.10.1 u-substitution in definite integrals — two methods

#### Method 1 — convert and convert back
After substitution, integrate; revert to x and substitute the original bounds.

#### Method 2 — change the bounds
After substitution u = f(x), update bounds: a → f(a), b → f(b). Then evaluate purely in u.

For ∫ₐᵇ f(x) f'(x) dx with u = f(x):
`∫ₐᵇ f(x) f'(x) dx = ∫_{f(a)}^{f(b)} u du = [u²/2]_{f(a)}^{f(b)} = ((f(b))² − (f(a))²)/2`.

### Examples
**Example 12.31: ∫_{(stated bounds)} −2x (4 − x²) dx with u = 4 − x², du = −2x dx.**

**Example 12.32: ∫₀^{π/2} sin x cos x dx.**
- Method 1: u = sin x ⇒ du = cos x dx. ∫ u du = u²/2 + C; revert and evaluate at endpoints.
- Method 2: bounds u(0) = 0, u(π/2) = 1. ∫₀¹ u du = 1/2.

**Example 12.33: ∫₀^{π/2} sin² x cos x dx.**
u = sin x. ∫₀¹ u² du = 1/3.

> **Quick Recall:**
> - Net area ≠ total area when f changes sign — split at zeros for total.
> - For definite integrals with substitution: either revert to x then plug in original bounds, or update the bounds and stay in u.

---

## Section: §12.11 Improper Integrals 🔴

### Core Idea
A definite integral is **improper** when at least one bound is ±∞ or when the integrand has an unbounded singularity in [a, b]. Such integrals are evaluated as limits of proper definite integrals.

### Evaluation rules

| Form | Definition |
|---|---|
| ∫_b^∞ f(x) dx | lim_{a → ∞} ∫_b^a f(x) dx |
| ∫_{−∞}^a f(x) dx | lim_{b → −∞} ∫_b^a f(x) dx |

### §12.11.1 Convergent vs Divergent

The improper integral **converges** if the limit exists and is finite; otherwise it **diverges**.

For doubly-infinite integrals, split at any convenient c:
`∫_{−∞}^∞ f(x) dx = ∫_{−∞}^c f(x) dx + ∫_c^∞ f(x) dx`,
**convergent only if both pieces converge separately**. If either diverges, the whole integral diverges.

### Comparison Theorem
For continuous f, g on [a, ∞) with `f(x) ≥ g(x) ≥ 0`:
- If `∫_a^∞ f` converges, then `∫_a^∞ g` converges.
- If `∫_a^∞ g` diverges, then `∫_a^∞ f` diverges.

### Examples
**Example 12.34: ∫_1^∞ dx/x².**
∫_1^a dx/x² = [−1/x]_1^a = −1/a + 1.
lim_{a→∞} (1 − 1/a) = **1** ⇒ converges to 1. Geometrically, the area between 1/x², the x-axis, and x = 1 is finite (= 1) even though the region extends to infinity.

**Example 12.35: ∫_1^∞ dx/x.**
∫_1^a dx/x = ln a − ln 1 = ln a → ∞ as a → ∞ ⇒ **diverges**.
(So 1/x is the borderline case: 1/x^p converges for p > 1, diverges for p ≤ 1.)

**Example 12.36: ∫_{−∞}^0 dx/√(3 − x).**
−2√(3 − x) is the antiderivative. As b → −∞, √(3 − b) → ∞ ⇒ value → ∞ ⇒ **diverges**.

**Example 12.37: ∫_{−∞}^∞ x · e^{−x²} dx.**
Split at 0:
- ∫_{−∞}^0 x · e^{−x²} dx: u = −x², du = −2x dx. Antiderivative −(1/2) e^{−x²}. lim_{b → −∞} [−(1/2)(1 − e^{−b²})] = −1/2.
- ∫_0^∞ x · e^{−x²} dx = +1/2.
- Total = −1/2 + 1/2 = **0** ⇒ convergent to 0.

### Definitions
- **Improper integral**: definite integral with infinite bound or unbounded integrand. ⭐
- **Convergent integral**: limit exists and is finite. ⭐
- **Divergent integral**: limit is infinite or does not exist. ⭐

> **Quick Recall:**
> - Always rewrite `∫_b^∞` as `lim_{a→∞} ∫_b^a`.
> - For `∫_{−∞}^∞`, both halves must converge separately.
> - 1/x^p on [1, ∞): converges if p > 1, diverges if p ≤ 1.

### ⚠️ Common Mistakes
- ❌ Mistake: in ∫_{−∞}^∞ f, taking a single symmetric limit (a → ∞ with bounds [−a, a]) → ✅ Correct: each half must converge independently; the symmetric "principal value" can hide divergence.

---

## Section: §12.12 Integration with Partial Fractions 🔴

### Core Idea
Many rational integrands `p(x)/q(x)` are not directly integrable but can be **decomposed** into a sum of simpler fractions whose integrals are standard (logs, arctans, power rule). This is the partial fraction technique.

### Conditions for direct decomposition
1. p(x)/q(x) is a rational function (polynomials).
2. **deg(p) < deg(q)**. (If not, polynomial-divide first; integrate the polynomial part directly and decompose the remainder.)

### Decomposition templates
| Factor of denominator | Term in decomposition |
|---|---|
| (x − a) (distinct linear) | A/(x − a) |
| (x − a)² | A/(x − a) + B/(x − a)² |
| (x − a)ᵏ | A₁/(x − a) + A₂/(x − a)² + … + Aₖ/(x − a)ᵏ |
| irreducible quadratic (x² + bx + c) | (Bx + C)/(x² + bx + c) |
| (x² + bx + c)ᵏ | k similar quadratic terms with rising denominators |

### Mechanisms / Processes (decomposition recipe)
1. Check deg(p) < deg(q); if not, long-divide.
2. Factor q(x) completely (linear + irreducible quadratic factors).
3. Write the partial-fraction template with unknowns (A, B, C, …).
4. Multiply out to clear denominators ⇒ a polynomial identity.
5. Solve for unknowns by either (a) plugging in strategic values of x (often the zeros of q) or (b) equating coefficients of like powers.
6. Integrate each simple fraction.

### Examples

**Motivating example: ∫(3x + 11)/(x² − x − 6) dx.**
- Factor: x² − x − 6 = (x − 3)(x + 2).
- Decompose: (3x + 11)/[(x − 3)(x + 2)] = A/(x − 3) + B/(x + 2).
- Multiply out: 3x + 11 = A(x + 2) + B(x − 3).
- x = 3: 20 = 5A ⇒ A = 4.
- x = −2: 5 = −5B ⇒ B = −1.
- Integral = 4 ∫ dx/(x − 3) − ∫ dx/(x + 2) = 4 ln|x − 3| − ln|x + 2| + C.

**Example: 6/(x² − 1).**
6/[(x − 1)(x + 1)] = A/(x − 1) + B/(x + 1).
6 = A(x + 1) + B(x − 1).
x = 1: 6 = 2A ⇒ A = 3.
x = −1: 6 = −2B ⇒ B = −3.
Decomposition: **3/(x − 1) − 3/(x + 1)**.

**Example: (2x − 3)/(x³ + x).**
Factor x³ + x = x(x² + 1). Template: A/x + (Bx + C)/(x² + 1).
Multiply out: 2x − 3 = A(x² + 1) + (Bx + C) x.
x = 0: −3 = A.
Use x = i (imaginary): 2i − 3 = A(0) + (Bi + C) i = − B + C i.
Match real & imaginary: −B = −3 ⇒ B = 3; C = 2.
Decomposition: **−3/x + (3x + 2)/(x² + 1)**.

**Example 12.38 (repeated linear + irreducible quadratic):**
`(2x³ + 5x − 1) / [(x + 1)³ (x² + 4)²]` decomposes as
`A/(x+1) + B/(x+1)² + C/(x+1)³ + (Dx+E)/(x²+4) + (Fx+G)/(x²+4)²`.

**Example 12.39 (deg(p) ≥ deg(q)):** ∫(x⁴ + 3x³ − 5x² − 4x + 17)/(x² + x − 2) dx.
Long-divide first: (x⁴ + 3x³ − 5x² − 4x + 17)/(x² + x − 2) = (x² + 2x − 5) + (3x + 7)/[(x + 2)(x − 1)].
Then decompose (3x + 7)/[(x + 2)(x − 1)] using the standard recipe.

### Definitions
- **Partial fraction decomposition**: writing a rational function as a sum of simpler rational functions whose denominators are factors of the original denominator. ⭐

> **Quick Recall:**
> - Always check deg(p) < deg(q) first; long-divide if not.
> - Distinct linear factor → constant numerator. Repeated linear → ascending powers. Irreducible quadratic → linear numerator (Bx + C).
> - "Cover-up" (plug in x = root) is the fastest way to find the constant for a distinct linear factor.

### ⚠️ Common Mistakes
- ❌ Mistake: writing (Bx + C)/(x² + 1) as just B/(x² + 1) → ✅ Correct: irreducible quadratic factors get **linear** numerators.
- ❌ Mistake: forgetting to long-divide when deg(p) ≥ deg(q) → ✅ Correct: long-divide first; integrate the polynomial part separately.

### Connections
- Builds on: Linearity of integration (§12.3); standard logarithmic and inverse-tangent integrals.
- Continues into: Chunk 009 — more partial fraction examples (12.39–12.43), Unit 12 wrap-up, exercises.

### Open Questions
1. How do you handle ∫ dx/(x² + 1) without a partial fraction step? (It is arctan x + C — recognise it directly.)
2. What happens when q(x) has complex (non-real) roots? (Group conjugate pairs into irreducible quadratic factors.)
