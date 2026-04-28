# Chunk 006 — Unit 11 wrap (Euler) + Unit 12 begin (Indefinite integrals; Substitution; Trig integrals start)
<!-- Pages: 51-60 -->
<!-- Source: chunk_006.txt -->

## Section: §11.4.4 Property 3 — Euler's Theorem 🔴
<!-- See chunk 005 for Properties 1–2 -->

### Core Idea
For a homogeneous function z = f(x, y) of degree n:
**`x · f_x + y · f_y = n · f(x, y)`**
This identity — Euler's homogeneous function theorem — is one of the most useful results in production theory.

> **In Simple Terms:** Multiply each input's marginal product by the input level, sum them up, and you get exactly n times the output. For n = 1 (constant returns to scale), this means total output = sum of (input × marginal product) — the "exhaustion of product" or marginal-productivity theory of distribution.

### Implications
- **Constant returns to scale (n = 1)**: x f_x + y f_y = f(x, y). Euler's theorem in this case underlies the marginal productivity theory of distribution: paying each factor its marginal product exactly exhausts total output.

> **Quick Recall:**
> - Euler's theorem: `Σᵢ xᵢ f_{xᵢ} = n · f` for degree-n homogeneous f.
> - For n = 1: total output = labour × MPL + capital × MPK.

---

## Section: Unit 11 Sum-Up & Key Words (§11.5–§11.6) 🟢

### Sum-Up
Unit 11 covered: partial derivatives; higher-order and cross-partials; Young's theorem; total differential vs total derivative; chain rule cases (I–IV); implicit functions; MRTS; elasticity of substitution; homogeneous functions and their three properties (including Euler).

### Key Words
- **Homogeneous function**: f(tx, ty) = tⁿ f(x, y).
- **Partial derivative**: derivative w.r.t. one variable, others held constant.
- **Total derivative**: rate of change of dependent variable when none of the variables is held constant.
- **Total differential**: linear approximation `dy = Σᵢ fᵢ dxᵢ`.

---

## Section: §11.7 Selected CYP Solutions 🟡

**CYP1 (1): Q = 5 L² K (note: source has L²K^? OCR'd; treating as L²K).**
- Q_L = 10 L K. (Source: Q_L = LK²; suggests degrees may differ — likely the textbook function is Q = 5 L² K with marginal products 10LK and 5L².) The standard mechanic remains: differentiate Q partially w.r.t. each input.

**CYP1 (3): f(x, y) = y sin x² + x³ cos y. Find f_x, f_y, f_{xx}, f_{yy}, and verify f_{xy} = f_{yx}.**
- f_x = 2xy cos x² + 3x² cos y.
- f_y = sin x² − x³ sin y.
- f_{xx} = 2y cos x² − 4x² y sin x² + 6x cos y.
- f_{yy} = −x³ cos y.
- f_{xy} = f_{yx} (by Young's theorem) = 2x cos x² − 3x² sin y.

**CYP2 (2): Cobb–Douglas q = A L^a K^{1−a}, A, a > 0.**

(a) **Homogeneous of degree 1:**
q(tL, tK) = A (tL)^a (tK)^{1−a} = A t^a L^a t^{1−a} K^{1−a} = t^{a + 1 − a} q = t · q. ✓

(b) **Marginal & average productivities depend only on K/L (or L/K):**
- MPL = A · a · L^{a−1} K^{1−a} = a · A · (K/L)^{1−a} → function of (K/L) alone.
- APL = q/L = A · L^{a−1} K^{1−a} = A · (K/L)^{1−a} → also a function of (K/L) only.

(c) **Elasticity of substitution σ = 1.** (Standard Cobb–Douglas property; can be derived from σ formula in §11.4.3 or directly: ln(L/K) is a linear function of ln(MRTS), with slope 1.)

(d) **Iso-quants downward sloping and convex.** Slope dK/dL < 0; second derivative d²K/dL² > 0 ⇒ convex to the origin.

> **Quick Recall:**
> - Cobb–Douglas q = A L^a K^{1−a}: degree 1, σ = 1, downward & convex isoquants.
> - Marginal products depend only on the input ratio K/L — homotheticity property.

---

## Section: §11.8 Unit 11 Exercises (Solved) 🟡

### Q1: Cubic cost C(x) = 10⁻⁶ x³ − 0.003 x² + 5x + 1000

(a) **Behaviour of marginal cost.**
- C'(x) = 3 × 10⁻⁶ · x² − 0.006 x + 5.
- C''(x) = 6 × 10⁻⁶ · x − 0.006.
- C''(x) = 0 at x = 1000. So MC is minimised at x = 1000.
- MC(1000) = 3·10⁻⁶ · 10⁶ − 0.006·1000 + 5 = 3 − 6 + 5 = 2.
- For x < 1000: MC decreasing. For x > 1000: MC increasing.

(b) **Sketch of C(x).**
- C'(x) > 0 always (no local extrema; cost continually rising).
- C'(x) decreases for x < 1000, increases beyond ⇒ C is **concave down for x < 1000**, **concave up for x > 1000**, with **inflexion at x = 1000**.
- The inflexion point of C(x) coincides with the minimum of MC.

### Q2: Demand p = 6 − x/2

- Revenue R(x) = x · p = 6x − x²/2.
- Marginal revenue R'(x) = 6 − x.
- R'(x) = 0 at x = 6.
- Maximum revenue R(6) = 36 − 18 = **18 rupees**.

> **Quick Recall:**
> - Inflexion point of total cost = minimum of marginal cost.
> - Revenue maximisation: dR/dx = 0 (set MR = 0).

---

## Section: Unit 12 Front Matter (§12.0–§12.1) 🟢

### Core Idea
Unit 12 is on **Integration** — the inverse of differentiation, and the language of accumulation (areas, total revenue from marginal revenue, present-value computations, etc.). It distinguishes **indefinite integrals** (a family of antiderivatives + constant) from **definite integrals** (a number = signed area).

### §12.0 Objectives
- Use integration as a problem-solving tool.
- Apply substitution, by-parts, trigonometric, partial-fraction, and rational-substitution methods.
- Evaluate improper integrals; classify convergent vs divergent.

> **Note on Unit 12 title**: the source's Unit 12 page header reads "DIFFERENTIAL CALCULUS: FUNCTIONS OF SEVERAL VARIABLES" — a typesetting/OCR carryover from Unit 11. The Block 3 cover page and Unit 12's actual content confirm the correct title is **"Integration: Introduction and Techniques"**.

---

## Section: §12.2 Indefinite Integrals 🔴

### Core Idea
Indefinite integration is **anti-differentiation**. Where differentiation finds the rate of change of a known function, indefinite integration finds an unknown function whose derivative is given.

### Notation
`∫ f(x) dx = F(x) + C`
where F'(x) = f(x), and C is the **constant of integration** (because antiderivatives are not unique — adding any constant gives another antiderivative).

- f(x) = the **integrand**.
- ∫ symbol is an elongated "S" denoting **sum** (anticipating the area-as-sum interpretation).
- ∫ f(x) dx reads "the integral of f(x) with respect to x".

### Examples
**Quick example.** If dy/dx = 3x², then y = x³ + C is an antiderivative because d(x³+C)/dx = 3x².

**Example 12.1: ∫(x² − 5) dx.**
We need a function whose derivative is x² − 5: that is x³/3 − 5x. So
`∫(x² − 5) dx = x³/3 − 5x + C`.

### Definitions
- **Indefinite integral** `∫ f(x) dx = F(x) + C`: any function F whose derivative is f, plus an arbitrary constant. ⭐
- **Constant of integration C**: the arbitrary additive constant; reflects non-uniqueness of antiderivatives. ⭐

> **Quick Recall:**
> - "Anti-derivative" is the most useful synonym.
> - **Always** include + C in indefinite integrals.

---

## Section: §12.3 Properties of the Indefinite Integral 🔴

### Property 1a — Linearity (constant factor)
`∫ k · f(x) dx = k · ∫ f(x) dx` for any constant k.

### Property 1b — Power rule
`∫ xⁿ dx = x^{n+1} / (n+1) + C`, valid for **n ≠ −1**. (For n = −1, the integral is ln|x| + C; see §12.6.)

### Property 2 — Linearity (sum)
`∫ [f(x) + g(x)] dx = ∫ f(x) dx + ∫ g(x) dx`.

(Subtraction works the same way: `∫ (f − g) dx = ∫ f dx − ∫ g dx`.)

### Examples
**Example 12.2: ∫ 5x² dx = 5 · x³/3 + C.**
**Example 12.3: ∫ x⁵ dx = x⁶/6 + C.**
**Example 12.4: ∫ 8 x⁶ dx = (8/7) x⁷ + C.**
**Example 12.5: ∫(4x² + 7x + 3) dx = (4x³)/3 + (7x²)/2 + 3x + C.**
**Example 12.6: dy = (5x² − 4x + 3) dx ⇒ y = (5x³)/3 − 2x² + 3x + C.**
**Example 12.7: ∫(2x + √x − 5/x³) dx**
Rewrite as ∫(2x + x^{1/2} − 5x^{−3}) dx = x² + (2/3) x^{3/2} + 5x^{−2}/2 + C.
(Source has a slight algebraic confusion; the right approach is term-by-term power rule.)

### Mechanisms / Processes (using initial condition to fix C)
**Example 12.8: dy/dx = 3x² − 2x; curve passes through (2, 5). Find y(x).**
1. Antidifferentiate: y = x³ − x² + C.
2. Plug in initial condition: 5 = 8 − 4 + C ⇒ C = 1.
3. Answer: y = x³ − x² + 1.

> **Quick Recall:**
> - Linearity: pull constants out, split sums.
> - Power rule: x^{n+1}/(n+1), but **only for n ≠ −1**.
> - Boundary/initial conditions uniquely determine C.

---

## Section: §12.3.2 Method of Substitution 🔴

### Core Idea
Substitution converts the integral of a composite function into a simpler integral by introducing a new variable u = g(x). The differential du = g'(x) dx must "match" something in the integrand for the trick to work.

### Statement
If x = g(y) (or u = g(x)), then `∫ f(x) dx = ∫ f(g(y)) g'(y) dy`. Most often used as: spot u = g(x) in the integrand whose derivative is also there (up to a constant).

### Mechanisms / Processes (substitution recipe)
1. Identify a composite expression: u = (something).
2. Compute du = (derivative of u) dx.
3. Rewrite the integral fully in u (no x left).
4. Integrate w.r.t. u using power/standard rules.
5. Substitute back u = g(x).
6. Add + C.

### Examples
**Example 12.9: ∫(2x⁴ − 5)⁵ x³ dx.**
Set u = 2x⁴ − 5 ⇒ du = 8 x³ dx ⇒ x³ dx = du/8.
`∫ u⁵ · du/8 = u⁶/48 + C = (2x⁴ − 5)⁶ / 48 + C`. (Source gives ⁷/56 in places — typo; the correct exponent is 6 because original power was 5.)

Wait — source says "(2x⁴ − 5)⁶ x³" with power 6 in places and 5 in others. Let me re-examine: the integrand was originally `(2x⁴ − 5)⁵ x³`, so the integral has u⁶/6 inside, and after dividing by 8 we get u⁶/48.

**Example 12.10: ∫(1 + 5x)^{1/2} dx.**
u = 1 + 5x ⇒ du = 5 dx ⇒ dx = du/5.
`(1/5) ∫ u^{1/2} du = (1/5) · (2/3) u^{3/2} + C = (2/15)(1 + 5x)^{3/2} + C`.

**Example 12.11: ∫ dx/(3x − 1)².**
u = 3x − 1 ⇒ du = 3 dx.
`(1/3) ∫ u^{−2} du = (1/3)(−u^{−1}) + C = −1/(3(3x − 1)) + C`.

**Example 12.12: ∫ e^{2x} dx.** u = 2x ⇒ du = 2 dx. (1/2) ∫ eᵘ du = (1/2) e^{2x} + C.

**Example 12.13: ∫ 2x √(x² + 1) dx.** u = x² + 1 ⇒ du = 2x dx. ∫ √u du = (2/3) u^{3/2} + C = (2/3)(x² + 1)^{3/2} + C.

> **Quick Recall:**
> - Substitution works when the integrand contains both g(x) and g'(x) (up to a constant).
> - Always express **everything** in terms of u — including dx.

### ⚠️ Common Mistakes
- ❌ Mistake: forgetting to convert dx into du → ✅ Correct: derive du = g'(x) dx and use it to replace dx.

---

## Section: §12.4 Integration of Trigonometric Functions (begins) 🟡

### Trigonometric identity refresh
- Ratio: `tan A = sin A / cos A`; `cot A = 1/tan A`.
- Reciprocal: `cosec A = 1/sin A`; `sec A = 1/cos A`.
- Pythagorean: `sin²A + cos²A = 1`; `1 + tan²A = sec²A`; `1 + cot²A = cosec²A`.

<!-- Continues in chunk 007: differentiation rules for trig, full integration table for trig functions, worked examples 12.14–12.18, integration by parts -->

### Connections
- Builds on: Substitution method (§12.3.2) — trig integrals often need substitution.
- Is prerequisite for: Integration by parts (§12.5) for products like x · sin x; partial fractions (§12.12) when simplifying after trig substitution.

### Open Questions
1. Why is the indefinite integral of 1/x not covered by the power rule? (The exponent +1 makes it 0/0; the answer is ln|x|.)
2. When should you choose substitution vs by-parts? (Substitution for products where one part is the derivative of another; by-parts for products with no such relation — see CYP2 in chunk 007.)
