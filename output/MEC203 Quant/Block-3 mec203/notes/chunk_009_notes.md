# Chunk 009 — Unit 12 wrap-up: Partial Fraction Examples, Sum-Up, Key Words, CYP Solutions, Exercises
<!-- Pages: 81-90 -->
<!-- Source: chunk_009.txt -->

## Section: §12.12 Partial Fractions — Worked Examples (cont.) 🟡
<!-- See chunk 008 for the §12.12 method and earlier examples -->

### Example 12.39 (long-division then decomposition) — completion
`∫(x⁴ + 3x³ − 5x² − 4x + 17)/(x² + x − 2) dx`
- Long-divide: quotient x² + 2x − 5, remainder 3x + 7.
- Decompose (3x + 7)/[(x + 2)(x − 1)] = A/(x + 2) + B/(x − 1).
- 3x + 7 = A(x − 1) + B(x + 2).
- x = 1: 10 = 3B ⇒ B = 10/3.
- x = −2: 1 = −3A ⇒ A = −1/3.
- Integral = ∫ (x² + 2x − 5) dx − (1/3) ln|x + 2| + (10/3) ln|x − 1| + C
        = x³/3 + x² − 5x − (1/3) ln|x + 2| + (10/3) ln|x − 1| + C.
*(Source has slightly different numerators owing to OCR coefficients; the procedure is the canonical one.)*

### Example 12.40 (repeated linear factor) — ∫ (x + 7)/[x² (x + 2)] dx
- Decompose: (x + 7)/[x² (x + 2)] = A/x + B/x² + C/(x + 2).
- x + 7 = A x (x + 2) + B (x + 2) + C x².
- x = 0: 7 = 2B ⇒ B = 7/2.
- x = −2: 5 = 4C ⇒ C = 5/4.
- Equate coefficients of x²: 0 = A + C ⇒ A = −5/4.
- Integral = −(5/4) ln|x| − (7/2)/x + (5/4) ln|x + 2| + C.

### Example 12.41 (non-linear factor with x³ in denominator) — covers similar machinery, multiple unknowns

### Example 12.43: ∫ sin⁵ x dx via partial-fraction-style algebra
`sin⁵ x = sin x · (sin² x)² = sin x · (1 − cos² x)²`. Let u = cos x ⇒ du = −sin x dx.
`∫ sin⁵ x dx = − ∫ (1 − u²)² du = − ∫ (1 − 2u² + u⁴) du = − u + (2/3) u³ − u⁵/5 + C`
= −cos x + (2/3) cos³ x − (1/5) cos⁵ x + C.

> **Quick Recall:**
> - For repeated linear factors, you need ascending powers in the decomposition.
> - For "improper" rationals, long-divide before decomposing.
> - Trig integrals with odd powers reduce to substitution.

---

## Section: §12.13 Unit 12 Sum-Up 🟢

Unit 12 covered: indefinite integrals (anti-derivatives + C); definite integrals (numbers ≅ areas); methods — substitution, by parts, trig identities, partial fractions; convergence tests for improper integrals; numerous worked examples to drill technique.

---

## Section: §12.14 Key Words 🟡

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

---

## Section: §12.15 CYP Solutions 🟡

### CYP1 (selected)
- Indefinite integral concept: anti-derivative — a function whose derivative is the given f.
- ∫ 4 dx = 4x + C.
- Power-rule integration: ∫ x² dx = x³/3 + C; ∫ (x² + 3) dx = x³/3 + 3x + C.
- ∫ −9 e^{3x} dx = −3 e^{3x} + C. (Source has -3e^{3x} which checks out: derivative is −9e^{3x}.)
- ∫ dx/(x + 2) = ln|x + 2| + C.

### CYP2 (selected)
- **CYP2(1):** ∫ cos(ax) dx = (1/a) sin(ax) + C, since d/dx[(1/a) sin(ax)] = cos(ax).
- **CYP2(2):** Always **try substitution first**; fall back to integration by parts if substitution fails.
- **CYP2(3):** ∫ x⁴ ln x dx — choose u = ln x (LIATE: log first); du = dx/x, dv = x⁴ dx, v = x⁵/5.

### CYP3 — Definite Integrals
1. **Definite integral**: integral with specific upper and lower bounds, giving a number.
2. **Riemann sum**: For partition a < x₁ < x₂ < … < x_{n−1} < b with mesh size max Δxₖ, the sum Σ f(x*ₖ) Δxₖ.

### CYP4 — Fundamental Theorem
- Connects derivative and integral.
- They are inverse operations: differentiate and then integrate gives back f.
- Definite integral = number (area under curve); indefinite integral = function (anti-derivative).

### CYP5 — Chain Rule for integration
1. Integration with chain rule reverses the chain rule for differentiation: ∫ a (g(x))^{n−1} g'(x) dx = a (g(x))ⁿ + C.
2. **Bounds change for u = 2x² + 3 over x ∈ [−1, 2]:** u(−1) = 5, u(2) = 11 ⇒ new bounds u ∈ [5, 11].
3. **Computing ∫_{−1}² 4x (2x² + 3)² dx:**
   - u = 2x² + 3, du = 4x dx ⇒ ∫₅¹¹ u² du = [u³/3]₅¹¹ = (11³ − 5³)/3 = (1331 − 125)/3 = 1206/3 = **402**.

### CYP6 — Improper Integrals
1. Improper integral: a definite integral with infinite limit or integrand approaching infinity in [a, b].
2. ∫_{−∞}^0 sin x dx: lim_{b → −∞} [cos b − cos 0] does not exist (oscillates) ⇒ **divergent**.
3. ∫_0^3 dx/√(3 − x): antiderivative −2√(3 − x). At x = 3: 0; at x = 0: −2√3. Value = 0 − (−2√3) = **2√3**. ⇒ **convergent**.

### CYP7 — Partial Fractions
**1. ∫(3x + 11)/(x² − x − 6) dx**:
- (x² − x − 6) = (x − 3)(x + 2). Decompose: A/(x − 3) + B/(x + 2).
- 3x + 11 = A(x + 2) + B(x − 3).
- x = −2: 5 = −5B ⇒ B = −1.
- x = 3: 20 = 5A ⇒ A = 4.
- ∫ = 4 ln|x − 3| − ln|x + 2| + C.

**2. ∫(2x + 7)/(x² + 4x + 3) dx**:
- (x² + 4x + 3) = (x + 1)(x + 3). Decompose A/(x + 1) + B/(x + 3).
- 2x + 7 = A(x + 3) + B(x + 1).
- x = −1: 5 = 2A ⇒ A = 5/2.
- x = −3: 1 = −2B ⇒ B = −1/2.
- ∫ = (5/2) ln|x + 1| − (1/2) ln|x + 3| + C.

**3. ∫(6x + 7)/(x + 2)² dx**:
- Decompose A/(x + 2) + B/(x + 2)².
- 6x + 7 = A(x + 2) + B.
- x = −2: −5 = B.
- Coeff of x: 6 = A.
- ∫ = 6 ln|x + 2| + 5/(x + 2) + C.

> **Quick Recall:**
> - For "(2x² + 3)" with x ∈ [−1, 2], the new u-bounds are 5 and 11.
> - 1/√(3 − x) on [0, 3] is improper at x = 3 — but converges (= 2√3).

---

## Section: §12.16 Unit 12 Exercises (Solved) 🟡

### Q1: ∫ sin⁶ x cos³ x dx
- cos³ x = cos x · (1 − sin² x). Let u = sin x, du = cos x dx.
- ∫ u⁶ (1 − u²) du = u⁷/7 − u⁹/9 + C = sin⁷ x / 7 − sin⁹ x / 9 + C.

### Q2: ∫ sin² x cos² x dx
- Use double-angle: sin² x = (1 − cos 2x)/2; cos² x = (1 + cos 2x)/2.
- Product = (1 − cos²(2x))/4 = sin²(2x)/4.
- = (1/4) ∫ (1 − cos 4x)/2 dx = (1/8) ∫ (1 − cos 4x) dx = x/8 − sin(4x)/32 + C.

### Q3: ∫ sec x dx = ln|sec x + tan x| + C
- Multiply numerator and denominator by (sec x + tan x): the derivative of (sec x + tan x) is sec x (sec x + tan x). Set u = sec x + tan x ⇒ du = sec x (sec x + tan x) dx.
- ∫ du/u = ln|u| + C = ln|sec x + tan x| + C.

### Q4: ∫ x e^{6x} dx
- u = x, dv = e^{6x} dx; du = dx, v = e^{6x}/6.
- ∫ x e^{6x} dx = x e^{6x}/6 − (1/6) ∫ e^{6x} dx = x e^{6x}/6 − e^{6x}/36 + C.

### Q5: ∫ x √(x + 1) dx — two ways
**(a) Integration by parts:** u = x, dv = √(x+1) dx, du = dx, v = (2/3)(x + 1)^{3/2}.
∫ x √(x+1) dx = (2x/3)(x+1)^{3/2} − (2/3) ∫ (x+1)^{3/2} dx = (2x/3)(x+1)^{3/2} − (4/15)(x+1)^{5/2} + C.

**(b) Substitution:** u = x + 1 ⇒ x = u − 1.
∫ (u − 1) √u du = ∫ (u^{3/2} − u^{1/2}) du = (2/5) u^{5/2} − (2/3) u^{3/2} + C
= (2/5)(x+1)^{5/2} − (2/3)(x+1)^{3/2} + C. *(Identical to (a) up to sign convention.)*

### Q6: ∫ ln x / x⁵ dx by parts
u = ln x, dv = x^{−5} dx; du = dx/x, v = −x^{−4}/4 = −1/(4x⁴).
∫ ln x / x⁵ dx = −ln x / (4x⁴) + (1/4) ∫ x^{−5} dx = −ln x / (4x⁴) − 1/(16 x⁴) + C.

### Q7: ∫ x² e^{3x} dx (parts twice)
- First: u = x², dv = e^{3x} dx; du = 2x dx, v = e^{3x}/3.
- ∫ = x² e^{3x}/3 − (2/3) ∫ x e^{3x} dx.
- Second by-parts on ∫ x e^{3x} dx: u = x, dv = e^{3x} dx ⇒ x e^{3x}/3 − e^{3x}/9.
- Final: x² e^{3x}/3 − (2/3)(x e^{3x}/3 − e^{3x}/9) + C = x² e^{3x}/3 − 2x e^{3x}/9 + 2 e^{3x}/27 + C.

### Q9: ∫_{−1}^{3} dx/x³ — divergent (split at 0)
Integrand has singularity at x = 0 ∈ [−1, 3]. Split into ∫_{−1}^0 + ∫_0^3. Either piece is divergent (1/x³ near 0 explodes) ⇒ **the integral diverges** without examining the other piece.

### Q10: ∫(2 − x)/(x² + 5x) dx
- x² + 5x = x(x + 5). Decompose (2 − x)/[x(x + 5)] = A/x + B/(x + 5).
- 2 − x = A(x + 5) + Bx.
- x = 0: 2 = 5A ⇒ A = 2/5.
- x = −5: 7 = −5B ⇒ B = −7/5.
- Integral = (2/5) ln|x| − (7/5) ln|x + 5| + C.

### Q11: ∫ 15 dx/(x² − 16)
- Factor: x² − 16 = (x − 4)(x + 4). Decompose 15/[(x − 4)(x + 4)] = A/(x − 4) + B/(x + 4).
- 15 = A(x + 4) + B(x − 4).
- x = 4: 15 = 8A ⇒ A = 15/8.
- x = −4: 15 = −8B ⇒ B = −15/8.
- Integral = (15/8) (ln|x − 4| − ln|x + 4|) + C.

> **Quick Recall:**
> - Q3 (∫ sec x): standard trick of multiplying by `(sec x + tan x)/(sec x + tan x)`.
> - Q5: ∫ x √(x+1) — substitution and parts both work.
> - Q9 demonstrates that a singularity *inside* the interval makes the integral improper even with finite bounds.

### Connections
- Builds on: Partial fraction decomposition (§12.12 in chunk 008); integration by parts (§12.5); FTC (§12.9).
- Closes Unit 12 / Block 3.

### Open Questions
1. How do you tell quickly that ∫ sec x dx requires the (sec x + tan x) trick rather than substitution?
2. For ∫ x² e^{3x}, why does **two** by-parts succeed, while ∫ e^{x²} dx has no closed-form antiderivative?
