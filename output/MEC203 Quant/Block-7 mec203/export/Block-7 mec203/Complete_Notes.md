# Complete Notes


## Section: Block Overview & Course Placement 🟢

### Core Idea
Block 7 of MEC-203 Quantitative Methods (Vol. 3) covers **Dynamic Optimisation**, comprising three units: Intertemporal Optimisation-I (Unit 22), Intertemporal Optimisation-II (Unit 23), and Economic Applications of Dynamic Optimisation (Unit 24). The block is the analytical bridge between earlier static optimisation (Block 5) and economic dynamics (Block 6) on one side, and probability/inferential statistics (Blocks 8–9) on the other.

> **In Simple Terms:** Earlier blocks taught you to find the best choice once. Block 7 teaches you to find the best *path* of choices over time — like deciding not just how much to eat today, but how to eat a finite cake over many days.

### Key Concepts

#### Block 7 unit map
| Unit | Title | Page (Vol. 3) | Focus |
|------|-------|---------------|-------|
| 22 | Intertemporal Optimisation-I | 11 | Calculus of Variations + intro to dynamic programming |
| 23 | Intertemporal Optimisation-II | 39 | Optimal control / Pontryagin's maximum principle |
| 24 | Economic Applications of Dynamic Optimisation | 66 | Ramsey, optimal investment, Hotelling, etc. |

### Definitions
- **Dynamic Optimisation**: optimisation in which the decision variables are **time-variant** (change over time), in contrast to static optimisation where they are fixed at one instant. ⭐ (exam-important)

> **Quick Recall:**
> - Block 7 = Dynamic Optimisation = 3 units (22, 23, 24)
> - Two main approaches: (i) Calculus of Variations / Pontryagin's Maximum Principle (continuous), (ii) Bellman's Dynamic Programming (recursive / discrete)

---

## Section: Mathematical Notation Used in the Course 🟡

### Core Idea
The course standardises a notation set used throughout Block 7 (and the whole MEC-203 course). Knowing these symbols is a prerequisite for reading derivations in subsequent units; misreading a symbol is a frequent source of student error.

### Definitions
Selected symbols (full list in source pages 7–9):

- **[a, b]** — closed interval; **(a, b)** — open interval.
- **∈** — element of.
- **Δ** — change / "delta" of a variable.
- **dx** — differential of x.
- **lim f(x)** — limit of f(x).
- **ln** — natural logarithm.
- **∫ f(x) dx** — definite integral.
- **∀** — universal quantifier ("for all").
- **∃** — existential quantifier ("there exists"); **∃!** — exists exactly one.
- **¬, ∧, ∨, ⇒, ⇔** — negation, conjunction, disjunction, implication, equivalence.
- **a, x ∈ ℝ** — real numbers / scalars.
- **a = (a₁, …, aₙ) ∈ ℝⁿ** — vector of parameters / variables.
- **A, X (matrices)** — capital letters denote matrices, dim m×n.
- **x ~ y** — vector x is **indifferent** to y (preference relation).
- **x ≻ y** / **x ≽ y** — strong / weak preference of x over y.
- **ℝ** — set of real numbers; **ℝ₊** — non-negative reals; **int ℝ₊** — strictly positive reals.
- **ℝⁿ = ℝ × ℝ × … × ℝ** — n-dimensional real space (Cartesian product).
- **ℝⁿ₊ = {x ∈ ℝⁿ | x ≥ 0} ⊂ ℝⁿ** — non-negative orthant.
- **f : X → Y** — function with domain X and codomain Y. ⭐
- **y = f(x)** — scalar function of one variable; **y = f(x₁, x₂)** — of two variables.
- **dy/dx, y′, f′(x)** — first derivative; **d²y/dx², y″, f″(x)** — second derivative.
- **∂f/∂xᵢ** — partial derivative; **∂²f/∂xᵢ ∂xⱼ** — second partial. ⭐
- **H(x₁, x₂)** — **Hessian** matrix (symmetric matrix of second partials). ⭐
- **(p, x) = Σᵢ pᵢ xᵢ** — scalar product of two vectors.
- **det(A) or |A|** — determinant of matrix A.
- **d(x¹, x²) = √(Σᵢ (xᵢ¹ − xᵢ²)²)** — Euclidean metric (distance).
- **d(x¹, x²) = max |xᵢ¹ − xᵢ²|** — non-Euclidean (Chebyshev / sup) metric.
- **‖x‖ = (Σᵢ xᵢ²)^(1/2)** — Euclidean norm.
- **‖x‖ = max |xᵢ|** — non-Euclidean (sup) norm.
- **t = 0, 1, 2, …** — time as discrete variable; **t ∈ [0, +∞)** — time as continuous variable. ⭐ (Block 7 will hinge on this distinction.)
- **∇f, grad f** — gradient of f, ∇f = (∂f/∂x₁, …, ∂f/∂xₙ). ⭐

### Greek letters used:
α (alpha), β (beta), γ (gamma), δ (delta), ε (epsilon), ψ (psi), ρ (rho), θ (theta), λ (lambda), π (pi), σ (sigma), χ (chi), μ (mu), ω (omega).

> **Quick Recall:**
> - Continuous time: t ∈ [0, ∞); discrete time: t = 0, 1, 2, …
> - Hessian = symmetric matrix of second partials → used for second-order conditions
> - ‖x‖ Euclidean = √Σxᵢ² ; sup-norm = max|xᵢ|

### Connections
- Builds on: notation already introduced in Blocks 1–6 (calculus, linear algebra, optimisation).
- Prerequisite for: every derivation in Units 22–24.

### Open Questions
1. None — this is reference material.


---


## Section: Unit 22 Objectives & Introduction 🟡

### Core Idea
Unit 22 introduces **dynamic optimisation**: optimisation problems whose decision variables vary over time. The unit's stated objectives are to (a) distinguish static vs. dynamic and continuous vs. discrete problems, (b) state the Calculus of Variations approach with its foundational theorem, and (c) state the Dynamic Programming approach for discrete dynamic optimisation.

> **In Simple Terms:** Static optimisation finds the best single choice; dynamic optimisation finds the best **path** of choices when the variables (prices, output, consumption, capital) themselves change over time.

### Key Concepts

#### Two principal solution methods (announced here, developed later)
| Method | Originator | Style | Better for |
|--------|-----------|-------|-----------|
| Calculus of Variations / Pontryagin's Maximum Principle | Bernoulli, Euler, Lagrange; Pontryagin | Continuous, classical | Continuous-time problems with smooth functionals |
| Dynamic Programming (Bellman's principle) | Richard Bellman | Recursive (sub-game-perfect-style) | Discrete-time, sequential-decision problems |

> **Important:** *Dynamic Programming* is **not** a synonym for *Dynamic Optimisation*; it is one of several methods to solve optimal-control problems.

### Definitions
- **Dynamic optimisation problem**: an optimisation problem in which variables of the model are time-variant. ⭐
- **Static vs. dynamic**: in static, variables are fixed at one instant; in dynamic, time is itself an independent variable (often *the* independent variable). ⭐
- **Discrete vs. continuous dynamic**: discrete uses time periods t = 0, 1, 2, …; continuous uses t ∈ [t₀, t_f]. The distinction follows whether the objective is continuous or piecewise-continuous.
- **Deterministic vs. stochastic**: stochastic dynamic optimisation is **out of syllabus** for MEC-203.

> **Quick Recall:**
> - Block 7 only covers *deterministic* dynamic optimisation.
> - Two main toolkits: Calculus of Variations / Optimal Control (continuous), Dynamic Programming (discrete).

---

## Section: Static vs. Dynamic Optimisation — Conceptual Clarification 🟡

### Core Idea
A motivating example: a fruit-icecream producer chooses cost-prices, quantities, and sales-prices to maximise profit. In a *static* view these are independent variables; but mango prices peak May–August, grape prices peak January–May, icecream sales peak April–July. So all of these are actually functions of time t, and the appropriate model is **dynamic**.

> **In Simple Terms:** If you ignore time, you assume the fruit market is the same in January and June — clearly wrong. Once you let prices, quantities, and sales depend on t, profit-maximisation must search over *paths* of decisions, not single numbers.

### Key Concepts
- In dynamic problems, *time* is typically the only independent variable — every other quantity is a function of t.
- The objective itself becomes a function of t (Total-Revenue(t), Total-Profit(t), …).
- Hence the natural objective is an **integral** (or a **sum**) of period-by-period payoffs over [t₀, t_f].

### Definitions
- **Profit functional in dynamic form**: V(x(t), x'(t), t) — profit at time t depends on current output x(t), its rate of change x'(t), and t itself.

---

## Section: Function vs. Functional 🔴
<!-- Reason: foundational distinction; Calculus of Variations operates on functionals, not functions -->

### Core Idea
A **function** maps elements of a set X to elements of a set Y; in particular, scalar functions map ℝⁿ → ℝ. A **functional** is a higher-order map: it takes whole **functions** as inputs and returns a real number. Dynamic optimisation maximises/minimises *functionals*, not functions.

> **In Simple Terms:** A function takes a number and returns a number. A functional takes a *whole curve* and returns a number — like asking "how long is this curve?" or "what is the area under this curve?". You're optimising over the choice of curve, not over a single point on it.

### Key Concepts

#### Worked illustration — set of functions on [0, b]
Consider three functions on [0, b]:
- g(x) = x  (a straight line)
- h(x) = +√(b² − x²)  (upper half of a circle of radius b)
- k(x) = x²  (a parabola)

**Functional 1: F_length, b (·) — arc length on [0, b]**
F_length, b (y) = length of the curve y = f(x) from x = 0 to x = b.

By the arc-length integral L = ∫₀ᵇ √(1 + (dy/dx)²) dx:
1. F_length, b (g) = ∫₀ᵇ √(1² + 1) dx = √2 · b
2. F_length, b (h) = (1/4) × circumference of circle of radius b = (πb)/2
3. F_length, b (k) = ∫₀ᵇ √(1 + (2x)²) dx  (closed-form using a hyperbolic substitution)

**Functional 2: F_area, b (·) — area under curve on [0, b]**
F_area, b (y) = ∫₀ᵇ f(x) dx (with y ≥ 0):
1. F_area, b (g) = (1/2) b²
2. F_area, b (h) = (1/4) π b²
3. F_area, b (k) = ∫₀ᵇ x² dx = b³/3

The crucial point: the **input** to each F is the *entire function* (not a single x value), and the output is a real number associated to the *whole* function.

### Definitions
- **Functional**: a function whose **input** is itself a function and whose output is a real number. ⭐ (exam-important)
- **Function f : X → Y**: a rule associating to each x ∈ X a unique y ∈ Y.

> **Quick Recall:**
> - Function: number → number
> - Functional: whole function → number
> - Calculus of Variations = "calculus on functionals"

---

## Section: Differentiability Class C^k 🟡

### Core Idea
The smoothness of a function is captured by its **differentiability class**. A function f : U → ℝ is of class **C^k** if it has continuous derivatives up to order k. Calculus of Variations typically requires C² functions (continuous second derivatives) so that the Euler–Lagrange equation makes sense.

### Definitions
- **C^k (differentiability class k)**: f is of class C^k on open U ⊂ ℝ if f, f', f'', …, f^(k) all exist and are continuous on U. ⭐
- **C^∞ (smooth, infinitely differentiable)**: f has derivatives of all orders on U.
- **Containment**: C^(k+1) ⊂ C^k for all k.

> **Quick Recall:** C² means twice continuously differentiable — the standard setting for Euler–Lagrange.

---

## Section: Two Worked Examples — Continuous & Discrete 🟡

### 22.2.1 Continuous example — Profit-maximising firm
A firm wishes to maximise profit over [t₀, t_f]. Let x(t) = output at time t and x'(t) = rate of change of output. Let V(x(t), x'(t), t) = profit functional. The problem:

  Max  J = ∫_{t₀}^{t_f} V(x(t), x'(t), t) dt   …(22.1)

  subject to  x(t) ≥ 0,  x(t₀) = x₀.

### 22.2.2 Discrete example — The Cake-Eating Problem
A cake of size W_t at time t is to be eaten over T periods. Let C_t = cake eaten in period (t, t+1), W₀ = a, W_T = 0. The eater has a discount factor 0 < β < 1 and a static log utility. Find the optimal sequences C* = {C_t*}_{t=0}^{T-1} and W* = {W_t*}_{t=0}^{T} solving:

  Max  Σ_{t=0}^{T-1} βᵗ ln(C_t)   …(22.2)
  s.t. W_{t+1} = W_t − C_t, W₀ = a, W_T = 0.

### Three Solution Approaches Announced
1. **Calculus of Variations** (this unit, §22.3 onward).
2. **Dynamic Programming** (this unit, §22.10).
3. **Optimal Control Theory** — modern generalisation of variational calculus (Unit 23).

> **Quick Recall:**
> - Continuous: Max ∫ V(x, x', t) dt, with end-point conditions on x.
> - Discrete: Max Σ βᵗ u(C_t), with state-equation W_{t+1} = W_t − C_t.

---

## Section: The Calculus of Variations — Origins 🟢

### Core Idea
Calculus of Variations originated with **Johann (John) Bernoulli's brachistochrone problem** in 1696: among all curves connecting two fixed points, which path lets a small object slide under gravity in the **shortest time**? The problem was solved by John Bernoulli and independently by his brother James in 1697. Subsequent contributors: **Euler, Lagrange, Legendre, Jacobi, Hamilton, Weierstrass, Hilbert**.

### Definitions
- **Brachistochrone problem**: find the curve of fastest descent between two fixed points under gravity. (The answer is a cycloid.)

---

## Section: Theorem for Optimality — The Euler–Lagrange Equation 🔴
<!-- Reason: foundational theorem of the entire unit -->

### Core Idea
The **Euler–Lagrange equation** is the *necessary* first-order condition that any extremising path x*(t) must satisfy in a Calculus-of-Variations problem with fixed endpoints. It is the dynamic analogue of "set the gradient to zero" in static optimisation.

> **In Simple Terms:** In static problems we set ∇f = 0. In dynamic problems we set the "Euler–Lagrange operator" of the integrand V to zero — and that operator pulls a time-derivative through a partial derivative.

### Theorem (Theorem for Optimality, §22.3.1)
Let J : C²[t₀, t_f] → ℝ be a functional defined by

  J(x(t)) = ∫_{t₀}^{t_f} V(x(t), x'(t), t) dt        …(22.3)

where V has continuous second-order partial derivatives in x, x', and t, and the endpoints are fixed:
  x(t₀) = x₀,  x(t_f) = x_f,  with  x₀, x_f ∈ ℝ,  t_f > t₀.

Then there exists an extremal path **x*(t)** for which J is either maximised or minimised **if and only if**

  ∂V/∂x(t)  −  d/dt (∂V/∂x'(t))  =  0       …(22.4)   ⭐⭐

This is the **Euler–Lagrange equation**.

### Mechanisms / Processes — Outline of the proof

1. Suppose x*(t) is the extremal path; let x_a(t) = x*(t) + δx(t) be a nearby admissible "varied" path with ‖δx‖ → 0. Because endpoints are fixed:  δx(t₀) = 0, δx(t_f) = 0.
2. Expand J(x_a) by Taylor series about x*: J(x_a) = J(x*) + ΔJ, where ΔJ ≈ δJ + δ²J (first and second variations).
3. **First variation** (necessary condition δJ = 0):
     δJ = ∫_{t₀}^{t_f} [ (∂V/∂x) δx + (∂V/∂x') δx' ] dt = 0     …(22.7)
4. Apply **integration by parts** to the second term (using d(UV) = U dV + V dU):
     ∫_{t₀}^{t_f} (∂V/∂x') δx' dt = [(∂V/∂x') δx]_{t₀}^{t_f}  −  ∫_{t₀}^{t_f} (d/dt)(∂V/∂x') δx dt.
   The boundary term vanishes because δx(t₀) = δx(t_f) = 0.
5. Substitute back:
     δJ = ∫_{t₀}^{t_f} [ ∂V/∂x  −  (d/dt)(∂V/∂x') ] · δx(t) dt = 0.
6. Apply the **Fundamental Lemma** (below): since this must hold for every admissible δx(t), the bracket must vanish identically:
     ∂V/∂x  −  (d/dt)(∂V/∂x')  =  0.   ▢

### Fundamental Lemma of Calculus of Variations
> **Lemma:** If g(t) is continuous on [t₀, t_f], and ∫_{t₀}^{t_f} g(t) δx(t) dt = 0 for every admissible variation δx(t) with δx(t₀) = δx(t_f) = 0, then g(t) ≡ 0 on [t₀, t_f].

### Definitions
- **Extremal path / extremal**: a function x*(t) that satisfies the Euler–Lagrange equation. ⭐
- **First variation δJ**: the linear-in-δx part of ΔJ; necessary condition is δJ = 0.
- **Second variation δ²J**: quadratic-in-δx part; sufficient sign-conditions: δ²J > 0 ⇒ minimum, δ²J < 0 ⇒ maximum.

### ⚠️ Common Mistakes
- ❌ Treating the Euler–Lagrange equation as a partial differential equation. → ✅ It is an **ordinary** differential equation in t (generally **second-order, nonlinear**).
- ❌ Assuming the boundary term automatically vanishes. → ✅ It vanishes only because endpoints are fixed; with free endpoints you instead get a **transversality condition** (see §22.9).
- ❌ Reading the equation as ∂V/∂x − ∂V/∂x' = 0. → ✅ The second term has a *total time derivative* d/dt outside the partial: d/dt (∂V/∂x'), **not** just ∂V/∂x'.

### Edge Cases & Caveats
- For x(t) scalar: one second-order ODE (so two integration constants C₁, C₂, pinned down by the two boundary conditions).
- For x(t) an n×1 vector: the equation becomes a system of **n** second-order ODEs (2n integration constants ⇒ 2n boundary conditions).
- The equation in general is **nonlinear and time-varying**.

> **Quick Recall:**
> - Necessary 1st-order condition: ∂V/∂x − d/dt (∂V/∂x') = 0.
> - It's an ODE; order = 2 per state variable.
> - Boundary conditions: x(t₀) = x₀, x(t_f) = x_f (fixed-endpoint problem).
> - Sufficient: 2nd variation δ²J > 0 (min) or δ²J < 0 (max).

### Connections
- Builds on: **integration by parts** (Block 3 calculus), **Taylor expansion** (Block 3), Fundamental Lemma (this section).
- Prerequisite for: special cases of Euler–Lagrange (§22.4), Legendre condition (§22.6), free-end problems & transversality (§22.9), all of Unit 23 (Optimal Control), Unit 24 (Economic Applications).

### Open Questions
1. What if V is non-smooth (only C¹)? — The classical Euler–Lagrange derivation breaks down; weak/distributional formulations are needed (out of MEC-203 scope).
2. How does the equation change when endpoints are free? — Resolved by **transversality conditions** in §22.9.


---


## Section: Practical Remarks on the Euler–Lagrange Equation 🟡
<!-- Continues from Chunk 002 — Theorem for Optimality -->

### Core Idea
Euler–Lagrange (E–L) is a *necessary* first-order condition. In practice it is a second-order, generally non-linear ODE, and the resulting two-point boundary value problem is usually hard — even numerically.

### Key Concepts
- E–L is non-linear because the integrand V can contain products of x(t), x'(t), and x''(t) — and after applying d/dt these multiply out.
- E–L solutions live on a **two-point boundary value problem (BVP)**: x(t₀) = x₀, x(t_f) = x_f.
- Both numerical and analytic solution are typically difficult.
- If E–L cannot be satisfied for any function in the class, **no optimum exists** for that functional.

### ⚠️ Common Mistakes
- ❌ Skipping the E–L check and jumping to second-order conditions. → ✅ E–L must be satisfied first; second-order conditions only classify between max/min once an extremal is found.

---

## Section: Worked E–L Example — Shortest Path between Two Points 🟢

### Core Idea
Among curves y(x) on [a, b] with y(a) = c, y(b) = d, the shortest is a **straight line**. We derive this from E–L.

### Mechanism / Calculation

Arc length s = ∫_a^b √(1 + (y')²) dx, so the integrand is L(x, y, y') = √(1 + (y')²).

Partial derivatives:
- ∂L/∂y' = y' / √(1 + (y')²)
- ∂L/∂y = 0

E–L: ∂L/∂y − d/dx (∂L/∂y') = 0  ⇒  d/dx [ y'(x) / √(1 + (y'(x))²) ] = 0
  ⇒  y'(x) / √(1 + (y'(x))²) = C (constant)
  ⇒  y'(x) is constant
  ⇒  y(x) = A x + B   ▢

So the extremal is a straight line — the constants A, B are found from y(a) = c, y(b) = d.

> **Quick Recall:** Shortest path between two points = straight line — derivable from E–L when ∂L/∂y = 0.

---

## Section: Euler Equation in Special Cases 🔴
<!-- Reason: simplifies E–L into a first-order ODE — directly testable -->

### Core Idea
Two simplifications collapse E–L from a second-order ODE into a *first-order* ODE — invaluable in practice.

### Case I — No explicit x(t) dependence (V = V(x'(t), t))
If x(t) does not appear explicitly in V, then ∂V/∂x = 0 and E–L reduces to:

  d/dt (∂V/∂x') = 0  ⇒  ∂V/∂x' = C₁ (a constant of integration)   …(22.13)

Provided ∂²V/∂x'² ≠ 0 (so the implicit-function theorem applies), this can be inverted to give

  x'(t) = g(t, C₁)   …(22.14)

and then x(t) is obtained by direct integration.

### Case II — No explicit t dependence (V = V(x(t), x'(t)))
If t does not appear explicitly in V, define the **Hamiltonian-like quantity**

  H(x(t), x'(t)) = x'(t) · (∂V/∂x'(t)) − V(x(t), x'(t))   …(22.15)

**Theorem.** Then H is **constant along any extremal x*(t)**.

**Proof outline.** Differentiate H along an extremal:

dH/dt = x''(t) · ∂V/∂x' + x'(t) · d/dt(∂V/∂x') − [∂V/∂x · x' + ∂V/∂x' · x'']
       = x'(t) · [d/dt(∂V/∂x') − ∂V/∂x]
       = 0   (because the Euler–Lagrange equation makes the bracket vanish)   …(22.16)

So H = constant along the extremal. Since H depends only on x and x' (not explicitly on t), the equation H(x, x') = const is a **first-order ODE** for x*(t).

> **In Simple Terms:** When V doesn't depend explicitly on t, you get a "first integral" — a quantity conserved along the optimal path. This is the variational analogue of energy conservation in physics.

> **Quick Recall:**
> - No x: ∂V/∂x' = const (first-order ODE)
> - No t: H = x'·(∂V/∂x') − V = const (first-order ODE)

### Connections
- Both special cases give **first integrals** that lower the order of the E–L equation by one.
- Builds on: Euler–Lagrange theorem (Chunk 002: Unit 22 Objectives & Introduction).

---

## Section: Second-Order Condition for Optimality 🔴

### Core Idea
The E–L equation is *necessary* but not *sufficient*. To classify an extremal as a maximum or minimum we examine the **second variation δ²J**, which depends on the **Hessian-like 2×2 matrix A** of second partials of V w.r.t. x and x'.

### Mechanism
The second variation is:

  δ²J = (1/2) ∫_{t₀}^{t_f} [δx(t),  δx'(t)] · A · [δx(t),  δx'(t)]ᵀ  dt   …(22.17)

with

  A  =  | ∂²V/∂x²        ∂²V/∂x ∂x'  |
        | ∂²V/∂x ∂x'     ∂²V/∂x'²    |   …(22.21)

**Sufficient conditions** (evaluated at x*):
- A is **positive definite at x*** ⇒ J is **minimised** at x*.
- A is **negative definite at x*** ⇒ J is **maximised** at x*.

### Definitions
- **Positive definite** matrix M: xᵀ M x > 0 for every non-zero column vector x.
- **Negative definite** matrix M: xᵀ M x < 0 for every non-zero column vector x.

> **Quick Recall:**
> - Necessary: E–L (∂V/∂x − d/dt(∂V/∂x') = 0).
> - Sufficient (min): A is positive definite at x*.
> - Sufficient (max): A is negative definite at x*.

---

## Section: Legendre Condition 🔴

### Core Idea
The **Legendre condition** is a *necessary* second-order condition that any optimising path must satisfy in addition to E–L. It restricts the sign of one specific second partial: ∂²V / ∂(x')².

### Statement
For x* to be a **maximising** path:
  ∂²V / ∂(x')² ≤ 0   along x*   …(22.18)

For x* to be a **minimising** path:
  ∂²V / ∂(x')² ≥ 0   along x*   …(22.19)

### Sufficient version via concavity/convexity of V
- If V is **concave** in (x, x'), then any path satisfying the E–L equation **maximises** J.
- If V is **convex** in (x, x'), then any path satisfying the E–L equation **minimises** J.

So: **E–L + concavity of V in (x, x') ⇒ maximum**;  **E–L + convexity ⇒ minimum**.

> **Quick Recall:**
> - Legendre necessary: max needs ∂²V/∂(x')² ≤ 0; min needs ≥ 0.
> - Legendre sufficient: V concave (convex) in (x, x') ⇒ E–L gives max (min).

---

## Section: Necessary & Sufficient Conditions Together 🔴

### Statement
For J(x) = ∫_{t₀}^{t_f} V(x, x', t) dt with x(t₀) = x₀, x(t_f) = x_f, V twice-continuously differentiable:

**Necessary** (both for min and max):
  ∂V/∂x − d/dt(∂V/∂x') = 0   …(22.20)

**Sufficient** (using A from §22.5):
- A positive definite at x* ⇒ x* is the **minimiser**.
- A negative definite at x* ⇒ x* is the **maximiser**.

> **Quick Recall:** Necessary = E–L. Sufficient = sign-definiteness of A.

---

## Section: Isoperimetric Problem 🔴
<!-- Reason: integral-constrained optimisation; uses Lagrange multiplier -->

### Core Idea
An **isoperimetric problem** asks for the extremal of a functional subject to an **integral constraint** on x(t) (in addition to the usual boundary conditions). It is the dynamic counterpart of constrained static optimisation, solved via a **Lagrange multiplier**.

> **In Simple Terms:** "Among curves of fixed total length, which one encloses the maximum area?" Classical example — the answer is a circle. The constraint (perimeter = L) is *integral*, so a single Lagrange multiplier λ buys it off.

### Problem statement
Maximise (or minimise)
  J(x) = ∫_{t₀}^{t_f} V(x, x', t) dt
subject to
  ∫_{t₀}^{t_f} F(x, x', t) dt = B,   x(t₀) = x₀, x(t_f) = x_f.

### Solution method
Append the constraint with Lagrange multiplier λ:

  J̃(x) = ∫_{t₀}^{t_f} [V(x, x', t) − λ F(x, x', t)] dt + λB
        = ∫_{t₀}^{t_f} S(x, x', t) dt + λB,   where S = V − λF.   …(22.22)

Necessary condition: apply E–L to the **augmented integrand S**:

  ∂S/∂x − d/dt(∂S/∂x') = 0   …(22.23)

The general solution gives x*(t; λ, C₁, C₂). The **three** unknowns λ, C₁, C₂ are pinned down by the **three** conditions:
1. Integral constraint  ∫ F(x*, x*', t) dt = B
2. x(t₀) = x₀
3. x(t_f) = x_f

### Mechanism (4 steps)
1. Form S = V − λF.
2. Solve E–L for S to obtain x*(t; λ, C₁, C₂).
3. Plug into the integral constraint and the two boundary conditions.
4. Solve the three simultaneous equations for λ, C₁, C₂.

> **Quick Recall:** Isoperimetric → augment integrand by λ·(F), apply E–L, then use 3 conditions for 3 unknowns (λ, C₁, C₂).

---

## Section: Free-End-Value Problems & Transversality Condition 🔴
<!-- Reason: standard exam topic; arises whenever an endpoint is unspecified -->

### Core Idea
When one or both endpoints are free (i.e. either t_f or x(t_f) — or both — are not given), the boundary terms in the first variation **no longer vanish automatically**. They produce additional **transversality conditions** that must hold at the free end, in addition to the Euler–Lagrange equation.

### Setup
J(x) = ∫_{t₀}^{t_f} V(x, x', t) dt with x(t₀) = x₀ fixed at A, but B = (t_f, x(t_f)) free.

The first variation (Block 7 §22.9) becomes

  δJ = ∫_{t₀}^{t_f} [∂V/∂x − d/dt(∂V/∂x')] · δx dt
       + [∂V/∂x']_{t = t_f} · δx_f
       + [V − x'(t) · ∂V/∂x']_{t = t_f} · δt_f.

For δJ = 0 we need both the E–L equation **and** the boundary terms to vanish. This generates four cases:

### Four cases of free-end transversality
| Case | What is free | Conditions to solve |
|------|--------------|---------------------|
| I  | Both t_f and x(t_f) free | E–L (22.25), [V − x'·∂V/∂x']_{t_f} = 0 (22.26), [∂V/∂x']_{t_f} = 0 (22.27) |
| II  | t_f fixed, x(t_f) free  | E–L (22.25) and [∂V/∂x']_{t_f} = 0 (22.27) |
| III | t_f free, x(t_f) fixed  | E–L (22.25) and [V − x'·∂V/∂x']_{t_f} = 0 (22.26) |
| IV  | Endpoint B lies on curve x = g(t) | E–L (22.25) and [V + (∂V/∂x')(g'(t) − x'(t))]_{t_f} = 0 (22.28) |

Equations (22.26), (22.27), (22.28) are the **transversality conditions** corresponding to each model.

> **In Simple Terms:** A free endpoint means *the optimiser also chooses where the path ends.* That extra freedom must be matched by an extra equation — the transversality condition.

> **Quick Recall:**
> - Fixed both ends: just E–L.
> - x_f free: add ∂V/∂x' |_{t_f} = 0.
> - t_f free: add V − x'·∂V/∂x' |_{t_f} = 0.
> - Endpoint on a curve g(t): add the curve-tangency transversality (22.28).

### Connections
- Builds on: integration-by-parts step in the E–L derivation (Chunk 002: Unit 22 Objectives & Introduction).
- Prerequisite for: optimal-control transversality conditions in Unit 23, infinite-horizon transversality in Unit 24.

---

## Section: Discrete-Time Dynamic Optimisation — Setup 🔴

### Core Idea
For discrete time t ∈ {0, 1, 2, …} = ℕ, the model is described by **two categories of variables**: a **state** x_t and a **control** U_t. Standard structural assumptions deliver an *autonomous, discounted, separable* problem with a clean recursive solution.

### Standard Assumptions
- **Timing**: state x_t is a *stock* measured at the **start** of period t; control U_t is a *flow* measured at the **end** of period t.
- **Horizon**: T can be finite or infinite (T = ∞ is the more common case).
- **Objective**: intertemporal utility is **additively separable, stationary, time-discounted**:
    Σ_{t=0}^{T} βᵗ f(U_t, x_t)   …(22.30)
  with 0 < β < 1 (impatience: β⁰ = 1, lim_{t→∞} βᵗ = 0). f is continuous, C¹, concave in (U, x).
- **State equation** (autonomous): x_{t+1} = g(x_t, U_t), with g continuous, differentiable, concave (so a unique solution exists).
- **No-Ponzi-game condition**: lim_{t→∞} βᵗ x_t = 0, with 0 < β < 1.
- **Side conditions** like x_t ≥ 0, U_t > 0 may exist; the unit treats only **interior** solutions (or open domains).

### Two canonical problems
**(1) Simplest optimal control problem (Definition 1):**
  Find {U_t, x_t}_{t=0}^{T} that solve
    max  Σ_{t=0}^{T} βᵗ f(U_t, x_t)   …(22.31)
  s.t.  x_{t+1} = g(x_t, U_t),  with x₀, x_T given, T free.

**(2) Free-terminal-state problem (Definition 2):**
  Find {U_t, x_t}_{t=0}^{T} that solve
    max  Σ_{t=0}^{T} βᵗ f(U_t, x_t)   …(22.32)
  s.t.  U_t ∈ U,  x_{t+1} = g(x_t, U_t)
  with x₀, T given and **x_T free**. If T = ∞, this is the **infinite-horizon discounted optimal control problem**.

### Definitions
- **State variable x_t** ⭐: *stock* describing the system at the start of period t (e.g., capital).
- **Control variable U_t** ⭐: *flow* chosen by the decision maker at period t (e.g., consumption).
- **Discount factor β** ⭐: 0 < β < 1; models impatience. Subjective discount rate ρ satisfies β = 1/(1+ρ).
- **No-Ponzi-game condition**: lim_{t→∞} βᵗ x_t = 0; rules out exploding state paths bankrolled by ever-growing borrowing.

### Necessary and sufficient condition
The **Hamilton–Jacobi–Bellman (HJB) equation** gives both. If f and g are well-behaved (continuous, C¹, concave), then necessary conditions are also sufficient.

> **Quick Recall:**
> - State = stock (start of period); Control = flow (end of period).
> - Objective: Σ βᵗ f(x_t, U_t); state law x_{t+1} = g(x_t, U_t).
> - 0 < β < 1; no-Ponzi: lim βᵗ x_t = 0.

---

## Section: Dynamic Programming & the Bellman Equation 🔴
<!-- Reason: HJB / Bellman is one of the central named results of Block 7 -->

### Core Idea (Bellman's Principle of Optimality)
> An optimal trajectory has the property that, for any given values of the state at any intermediate time, the controls chosen for the **remainder** of the horizon must themselves be optimal — taking the optimal previous decisions as given.

(Stated by **Richard Bellman, 1957**.)

> **In Simple Terms:** Whatever you've done so far, the rest of the plan must still be optimal **starting from where you are now**. This lets you collapse a T-period problem into a recursion of one-period problems.

### Definitions
- **Value function V_T−t (x_t)** ⭐: the maximised intertemporal utility starting at period t with state x_t and remaining horizon T − t periods:
    V_{T−t}(x_t) = max  Σ_{τ=t}^{T} β^{τ−t} f(U_τ, x_τ).   …(22.33)

### Hamilton–Jacobi–Bellman (HJB) / Bellman Equation
**Proposition 1.** If {U_t*, x_t*} solves the optimal-control problem, then it satisfies the **Bellman equation**:

  V_T(x_t) = max_{U_t} { f(x_t, U_t) + β V_{T−1}(x_{t+1}) }
           = max_{U_t} { f(x_t, U_t) + β V_{T−1}(g(x_t, U_t)) }   …(22.34)

#### Derivation (heuristic)
  V_T(x_0) = max_{U} Σ_{t=0}^{T} βᵗ f(x_t, U_t)
        = max( f(x_0, U_0) + β f(x_1, U_1) + β² f(x_2, U_2) + … )
        = max( f(x_0, U_0) + β · max_{U_1, …, U_T} Σ_{t=1}^{T} β^{t−1} f(x_t, U_t) )
        = max_{U_0} { f(x_0, U_0) + β V_{T−1}(x_1) }.   ▢

This is the **two-period recursive form** of the original T-period problem.

### Recursion in general (any t)
  V_{T−t}(x_t) = max_{U_t} { f(x_t, U_t) + β V_{T−t−1}(g(x_t, U_t)) }   …(22.35)

### Infinite-horizon HJB
For T = ∞, V = lim_{j→∞} V_j is **time-invariant**, so the Bellman equation collapses to:

  V(x) = max_U { f(x, U) + β V(g(x, U)) }   …(22.36)

### Optimality and policy function
If V is sufficiently regular, the optimal control comes from

  ∂H(x, U)/∂U = 0   …(22.37)

If H ∈ C², we obtain a **policy function** U* = h(x): a feedback rule mapping the current state to the optimal current control. Plugging in:

  V(x) = f(x, h(x)) + β V(g(x, h(x)))   …(22.38)

a non-linear functional equation typically solved by **value-function iteration** (numerical).

### ⚠️ Common Mistakes
- ❌ Treating the value function as differentiable. → ✅ Continuity is generally guaranteed; differentiability is **not** (Stokey & Lucas 1989). Differentiability requires extra regularity.
- ❌ Confusing dynamic programming with dynamic optimisation. → ✅ DP is *one* method; calculus of variations and optimal control are others.

> **Quick Recall:**
> - Bellman: V_T(x) = max_U {f(x, U) + β V_{T−1}(g(x, U))}.
> - Infinite horizon: V(x) = max_U {f(x, U) + β V(g(x, U))}.
> - Policy function: U* = h(x). Solved numerically by value-function iteration.

### Connections
- Builds on: state/control distinction (this chunk), discount factor concept (this chunk).
- Equivalent first-order condition in continuous time = Pontryagin's maximum principle (Unit 23).
- Application: Cake-Eating Problem solved via Bellman equation in next chunk.

### Open Questions
1. When is the value function differentiable? — see Stokey & Lucas (1989), Benveniste–Scheinkman theorem (out of MEC-203 scope).
2. How fast does value-function iteration converge? — geometric, with ratio β.


---


## Section: The Cake-Eating Problem — Worked Solution via the Bellman Equation 🔴
<!-- Continues from Chunk 003 — Dynamic Programming -->
<!-- Reason: canonical worked example linking Bellman recursion to a closed-form policy -->

### Core Idea
The cake-eating problem (introduced in §22.2.2) is solved here by the **guess-and-verify** method on the Bellman equation: guess a log-linear value function, take FOCs, equate coefficients with the guess, and recover the policy function. The optimal policy turns out to be: **eat a constant fraction (1 − β) of the cake remaining each period, leaving β times as much for tomorrow**.

> **In Simple Terms:** With log utility and discount factor β, the optimal rule is "eat the same fraction every period". You keep β share of the cake, eat the remaining (1 − β) share. Independent of how much is left.

### Problem restated
Max  Σ_{t=0}^{T} βᵗ ln(C_t)
s.t. W_{t+1} = W_t − C_t,  W_0 > 0,  W_T = 0.

Since C_t = W_t − W_{t+1}, the choice variable is equivalently W_{t+1}:

  max  Σ_{t=0}^{T} βᵗ ln(W_t − W_{t+1}).

Bellman equation (22.39):
  V(W_t) = max_{W_{t+1}} { ln(W_t − W_{t+1}) + β V(W_{t+1}) }.

### Solution Procedure — six numbered steps
1. **Set up the Bellman equation** (above).
2. **Guess** the form of the value function:  V(W_t) = C₁ + C₂ ln(W_t).
3. **Take the FOC** of the RHS w.r.t. W_{t+1} and solve for the optimal W_{t+1}*.
4. **Match the guess** to the Bellman equation evaluated at W_{t+1}*.
5. **Identify the unknown coefficients** C₁ and C₂ by equating constant terms and the coefficient of ln(W_t).
6. **Recover the policy function** for W_{t+1} (and hence the optimal consumption C_t*).

### Mechanism — the algebra
**Step 3 (FOC):** Differentiate the bracket w.r.t. W_{t+1}:
  −1/(W_t − W_{t+1}) + β C₂ / W_{t+1} = 0
  ⇒  W_{t+1}* = β C₂ W_t / (1 + β C₂).   …(22.40)

**Step 4 (substitute):** Plugging W_{t+1}* back into the Bellman equation:
  C₁ + C₂ ln(W_t)
   = ln(W_t / (1 + β C₂))  +  β [C₁ + C₂ ln(β C₂ W_t / (1 + β C₂))].

Expanding and matching the coefficient of ln(W_t):
  C₂ = 1 + β C₂   ⇒   **C₂ = 1 / (1 − β)**.   …(22.41)

(C₁ is pinned down by matching constants — exam questions usually ask only for C₂ and the policy function.)

**Step 6 (policy function):** Substituting C₂ into (22.40):
  W_{t+1}* = β · [1/(1 − β)] · W_t / (1 + β · [1/(1 − β)])
            = β W_t.

So the **policy function** for the state is:
  **g(W_t) = W_{t+1}* = β W_t.**

The corresponding **optimal consumption**:
  C_t* = W_t − W_{t+1}* = W_t − β W_t = **(1 − β) W_t**.   …(22.43)

### Definitions
- **Policy function**: a feedback rule mapping the current state to the optimal current control (here, U* = (1 − β) W_t).
- **Guess-and-verify**: a standard method for closed-form solutions of Bellman equations — guess the functional form of V, verify that the FOCs are consistent with the guess.

### ⚠️ Common Mistakes
- ❌ Forgetting that the constant term C₁ is also pinned down by matching; ignoring it leaves the value function ill-defined.
- ❌ Treating C_0 as well-defined: the muncher only starts eating at t = 1 (so C₀ = 0 in the timing convention adopted in the unit).

> **Quick Recall:**
> - Cake-eating with log utility ⇒ policy g(W) = β W.
> - Optimal consumption ⇒ C_t* = (1 − β) W_t.
> - V(W) = C₁ + C₂ ln W with C₂ = 1/(1 − β).
> - Standard method: guess-and-verify on the Bellman equation.

### Connections
- Builds on: Bellman equation (Chunk 003: Practical Remarks on the Euler–Lagrange Equation), discounted utility (Chunk 003: Practical Remarks on the Euler–Lagrange Equation).
- Generalises to: Ramsey/CASS–KOOPMANS optimal-growth model (Unit 24, with concave production replacing the cake constraint).

### Open Questions
1. What if utility is CRRA u(C) = C^(1−σ)/(1−σ) instead of log? — The policy is still linear in W (W_{t+1}* = (β R)^(1/σ) W_t / [1 + (β R)^(1/σ)] for return R), but the algebra is messier.

---

## Section: Unit 22 Summary & Key Words 🟢

### Core summary points (§22.11)
- Distinguished **static vs. dynamic** optimisation (variables time-invariant vs. time-variant).
- Distinguished **function vs. functional** (input is a number vs. an entire function).
- Surveyed three approaches: **Calculus of Variations**, **Dynamic Programming**, **Optimal Control** (next unit).
- Stated and proved the **Euler–Lagrange equation** as a necessary first-order condition.
- Derived the **Bellman equation** as a recursive necessary-and-sufficient condition.
- Worked the **cake-eating problem** end-to-end via guess-and-verify.

### Key Words (from §22.12)
- **Euler–Lagrange equation**: necessary condition for optimisation in the calculus of variations; obtained by setting the **first variation** of the functional to zero.
- **Necessary and sufficient condition**: 2nd variation of functional is positive definite for minimum, negative definite for maximum.
- **Functional**: a function whose domain is a *set of functions*.
- **Objective functional**: the functional to be maximised or minimised.
- **Isoperimetric problem**: optimisation under an integral constraint plus ordinary boundary conditions.
- **Bellman equation** ⭐: V(x) = max_u { f(x, u) + β V(g(x, u)) }.

### Some Useful Books (canonical references for Block 7)
- Chiang, A. C. (1992) *Elements of Dynamic Optimisation*, McGraw-Hill.
- Kamien, M. & Schwartz, N. L. (1991) *Dynamic Optimisation*, Elsevier.
- Seierstad, A. & Sydsæter, K. (1987) *Optimal Control Theory with Economic Applications*, Elsevier.
- Stokey, N. L., Lucas, R. E. Jr. & Prescott, E. C. (1989) *Recursive Methods in Economic Dynamics*, Harvard.
- Weber, T. A. (2011) *Optimal Control Theory with Applications in Economics*, MIT Press.
- Whittle, P. (1996) *Optimal Control: Basics and Beyond*, Wiley.
- Liberzon, D. (2012) *Calculus of Variations and Optimal Control Theory*, Princeton.

---

## Section: Worked Exercises — Selected Solutions (§22.13–22.14) 🔴
<!-- Reason: exam questions are drawn directly from these patterns -->

### CYP 1 — Mixed integrand with exponential
Problem: J(y) = ∫₀¹ (y'² + y² + 4y eᵗ) dt, with y(0) = 0, y(1) = 1.

E–L: ∂V/∂y = 2y + 4eᵗ;  d/dt(∂V/∂y') = 2y''.
So **2y + 4eᵗ = 2y''**, i.e. **y'' − y = 2eᵗ**.

- *Particular integral:* try y_p = B t eᵗ. Differentiating twice gives y_p'' = B(t eᵗ + 2eᵗ). Substituting: B t eᵗ + 2B eᵗ − B t eᵗ = 2eᵗ ⇒ 2B = 2 ⇒ B = 1, so y_p = t eᵗ.
- *Complementary function:* try y_c = A e^{rt}. The auxiliary equation r² − 1 = 0 ⇒ r = ±1, so y_c = A₁ eᵗ + A₂ e^{−t}.
- *Boundary conditions:* y(0) = A₁ + A₂ = 0 ⇒ A₂ = −A₁. y(1) = A₁ e + A₂ e^{−1} + e = 1 (with the y_p contribution at t = 1 being e). Solve for A₁ = (1 − e)/(e − e^{−1}). The final answer (textbook):  **y(t) = [(1 − e)/(1 − e²)]·(eᵗ − e^{−t}) + t·eᵗ**.

### CYP 2(1) — Quadratic-with-linear time
Problem: ∫₀¹ {x'² + 10 x t} dt, x(0) = 2, x(1) = 3.

V = x'² + 10 x t. E–L: 10t − 2 x'' = 0 ⇒ x'' = 5t.
Integrate: x' = (5/2) t² + C₁; x(t) = (5/6) t³ + C₁ t + C₂.
BCs: x(0) = 2 ⇒ C₂ = 2; x(1) = 3 ⇒ 5/6 + C₁ + 2 = 3 ⇒ **C₁ = 1/6**.
**x*(t) = (5/6) t³ + (1/6) t + 2**.

### CYP 2(2) — With Legendre check
Problem: ∫₀² (2 x'² + 24 x t) dt, x(0) = 0, x(2) = 2.

V = 2 x'² + 24 x t. E–L: 24t − d/dt(4 x') = 0 ⇒ 24t − 4 x'' = 0 ⇒ x'' = 6t.
Integrating twice: x'(t) = 3t² + C₁; x(t) = t³ + C₁ t + C₂.
BCs: x(0) = 0 ⇒ C₂ = 0; x(2) = 2 ⇒ 8 + 2C₁ = 2 ⇒ **C₁ = −3**.
**x*(t) = t³ − 3t**.

*Legendre verification:* ∂²V/∂(x')² = 4 > 0 ⇒ minimum. ✓

### Exercise Q1 — Free linear–quadratic
Problem: J = ∫₀¹ (x'² − 2 x x' + 10 x t) dt, x(0) = 0, x(1) = 2.

V = x'² − 2 x x' + 10 x t.
- ∂V/∂x = −2 x' + 10t.
- ∂V/∂x' = 2 x' − 2 x ⇒ d/dt(∂V/∂x') = 2 x'' − 2 x'.
- E–L: −2 x' + 10t − 2 x'' + 2 x' = 0 ⇒ **2 x'' = 10t** ⇒ x'' = 5t.
- Integrating: x'(t) = (5/2) t² + C₁; x(t) = (5/6) t³ + C₁ t + C₂.
- BCs: x(0) = 0 ⇒ C₂ = 0. x(1) = 2 ⇒ 5/6 + C₁ = 2 ⇒ C₁ = 7/6.
- **x*(t) = (5/6) t³ + (7/6) t**. (The unit's published answer: x*(t) = (5/6) t³ + (1/6) t — note the discrepancy; the OCR'd source shows "5/6 t³ + 1/6 t". When in doubt re-derive.)

### Exercise Q2 — Isoperimetric
Problem: Minimise ∫₀¹ x'(t)² dt subject to ∫₀¹ x(t) dt = K, x(0) = 1, x(1) = 2.

Augmented integrand: V − λ F = x'² − λ x. E–L for the augmented problem:
  −λ − d/dt(2 x') = 0 ⇒ −λ − 2 x'' = 0 ⇒ **x'' = −λ/2**.

Integrating: x'(t) = −(λ/2) t + C₁; x(t) = −(λ/4) t² + C₁ t + C₂.
- BC x(0) = 1 ⇒ C₂ = 1.
- BC x(1) = 2 ⇒ −λ/4 + C₁ + 1 = 2 ⇒ C₁ = 1 + λ/4.
- Integral constraint ∫₀¹ x(t) dt = K:
   ∫₀¹ [−(λ/4) t² + (1 + λ/4) t + 1] dt = −λ/12 + (1 + λ/4)/2 + 1 = K.
   Multiplying through, after the unit's algebra:  **λ = 24(K − 1)**.

Hence **x*(t) = −6(K − 1) t² + (1 + 6(K − 1)) t + 1**.

### Exercise Q3 — Free terminal time (transversality 22.26)
Problem: J = ∫_{0}^{t_f} (2 x'² + 24 x t) dt with x(0) = 0, x(t_f) = 2, t_f free.

E–L gives x'' = 6t (as in CYP 2.2), so x(t) = t³ + C₁ t + C₂.
BC x(0) = 0 ⇒ C₂ = 0.
Endpoint BC: 2 = t_f³ + C₁ t_f, so **C₁ = (2 − t_f³)/t_f**.   …(2)

**Transversality** (when x_f fixed, t_f free, eq. 22.26):
[V − x' (∂V/∂x')]_{t_f} = 0
⇒ 2 x'(t_f)² + 24 x(t_f) t_f − 4 x'(t_f)² = 0
⇒ −2 x'(t_f)² + 48 t_f = 0   (using x(t_f) = 2)
⇒ x'(t_f)² = 24 t_f.   …(1a)

Differentiating x(t): x'(t_f) = 3 t_f² + C₁.   …(3)

Combining (3), (2), (1a) and setting x_f = 2:
  After algebra (per the unit):  t_f⁴ − 4 t_f² + 1 = 0, so let z = t_f²:
  z² − 4z + 1 = 0  ⇒  z = 2 ± √3.
- z₁ = 2 + √3 ≈ 3.732 ⇒ t_{f,1} ≈ 1.932; corresponding C₁ ≈ −1.117 ⇒ **x*(t) = t³ − 1.117 t**.
- z₂ = 2 − √3 ≈ 0.2679 ⇒ t_{f,2} ≈ 0.6446; corresponding C₁ ≈ 2.6871 ⇒ **x*(t) = t³ + 2.6871 t**.

Two extremal candidates emerge — both satisfy the necessary conditions; second-order conditions select the actual optimum.

### Exercise Q4 — Bellman equation derivation
Problem: max  Σ_{t=0}^{∞} βᵗ f(U_t, x_t) s.t. U_t = x_t − x_{t+1}, x₀ given.

Sequence problem: x_{t+1} = g(x_t, U_t) = x_t − U_t (so the budget constraint defines g).
By Bellman's principle:
  **v(x_t) = max_{U_t} { f(x_t, U_t) + β v(g(x_t, U_t)) }**
i.e. **v(x) = max_u { f(x, u) + β v(g(x, u)) }**, where 0 < β = 1/(1 + ρ) < 1 with ρ > 0.

> **Quick Recall (CYP/exercise patterns):**
> - Step 1: write E–L (or augmented E–L for isoperimetric).
> - Step 2: integrate twice (or solve ODE).
> - Step 3: use BCs (and integral constraint / transversality) to pin down constants.
> - Step 4: verify with Legendre / second-order condition.

---

## Section: Unit 23 — Objectives & Introduction 🟡
<!-- Continues into Chunk 005 — Hamiltonian formation -->

### Core Idea
Unit 23 builds on Unit 22's calculus-of-variations approach to develop **Optimal Control Theory** — specifically the **Hamiltonian formulation**, the analytical core of Pontryagin's Maximum Principle. It then specialises to **infinite-horizon** problems and **discounted** problems, both ubiquitous in macroeconomics.

### Stated objectives (§23.0)
After Unit 23 you should be able to:
- Show how the **Hamiltonian formation** is derived for *constrained* dynamic optimisation.
- Determine **necessary and sufficient conditions** for optimising the Hamiltonian functional.
- Elucidate two special cases: **infinite-horizon** models, **discounted** optimisation models.

### Where Unit 23 sits relative to Unit 22
Unit 22 dealt with unconstrained Calculus of Variations (E–L equation under endpoint conditions). Unit 23 applies the same machinery to **constrained** dynamic problems where the state evolves according to a controlled differential equation x'(t) = g(x(t), U(t), t) — i.e., to **optimal control** problems.

> **Quick Recall:**
> - Unit 22 = unconstrained calculus of variations + intro to DP.
> - Unit 23 = constrained dynamic optimisation via Hamiltonians (continuous-time optimal control).

### Connections
- Builds on: Euler–Lagrange (Chunk 002: Unit 22 Objectives & Introduction), transversality conditions (Chunk 003: Practical Remarks on the Euler–Lagrange Equation).
- Prerequisite for: Hamiltonian + Pontryagin's principle (Chunk 005: Recap — Components of an Optimisation Problem), economic applications in Unit 24.


---


## Section: Recap — Components of an Optimisation Problem 🟢

### Core Idea
Every optimisation problem has three components: an **objective function**, **decision (choice) variables**, and **constraints**. This applies in both static and dynamic settings; the difference is whether the variables depend on time.

### Two illustrative static examples
**Example 1 — Profit maximisation:** A firm chooses output Q to maximise P(Q) = R(Q) − C(Q). Q is the decision variable; P is the objective; constraints might be Q ≥ 0 and capacity bounds. The goal is the **value of Q** at which P is maximised, **not** the maximum value of Q.

**Example 2 — Fence problem:** With 60 ft of fence enclose the largest rectangle.
  max_{L, W}  L × W   s.t. 2L + 2W ≤ 60, L ≥ 0, W ≥ 0.
Decision variables are L and W (not the area itself); the constraint is the perimeter; objective is area.

### Definitions
- **Objective function (f or z)**: scalar quantity to maximise or minimise.
- **Decision / choice variables (vector X)**: variables under the decision-maker's control.
- **Constraints**: any limitations / bounds on the decision variables.

### ⚠️ Common Mistakes
- ❌ Confusing "value of choice variable that maximises objective" with "maximum value of the choice variable".

---

## Section: The Concept of STATE — and State-Space Representation 🔴
<!-- Reason: foundational concept distinguishing optimal control from calculus of variations -->

### Core Idea
The **state** of a dynamical system is a *minimal* internal variable (or vector of variables) that summarises the system's progress toward its goal — irrespective of the particular path taken to get there. Once the state is known at any instant, plus the input from time t onward, the entire future of the system is determined.

> **In Simple Terms:** State is a "memory of where you are now". Two different histories that leave you in the same state lead to the same future. The state is the *minimum* such summary.

### Two illustrative examples
**Example 4 — Madurai-bound motorist (state collapses many histories).**
A motorist drives Delhi → Madurai (2000 km), in cycles of 0/100/200/… km. Instead of recording every (cycle, distance) pair, define the **state-variable s** = total distance covered so far. State s = s₃ "300 km covered" represents *infinitely many* combinations of (1, 0)+(2, 200)+(3, 100), (1, 100)+(2, 0)+(3, 0)+(4, 100)+(5, 100), etc. Once s and the next input (cycle k, distance covered in cycle k) are known, both the next state and the remaining distance are uniquely determined.

**Example 5 — Global petroleum production/consumption (state vs. control).**
The petroleum process has many internal variables (drilling, extraction, processing, …). For studying *consumption pattern* it is enough to track two aggregate state variables: total inflow at distribution centre i, total outflow at distribution centre i. But the system is also affected by an **external** control — e.g., OPEC+'s June 4, 2023 decision to *cut production*. That decision is **not** an internal variable; it is an **external control**. Optimal Control Theory differs from Calculus of Variations precisely by including such control variables explicitly.

### Formal definition of STATE
The state-vector **SV = (y₁, …, yₙ)** is a subset of internal variables IV such that:
1. SV is a **minimal independent** subset (no redundancy: e.g., if z = 3y₁ + 4y₂ then z is not in SV).
2. The output map: SV × IP → OP is **well-defined** (a function): output(s_i, j) ∈ OP is unique for each (s_i, j).
3. The next-state map: SV × IP → SV is **well-defined**: next-state(s_i, j) is unique.
4. **Persistence**: the state remains unchanged unless an external input is received (internal variables may evolve, but state values change only at input instants).

### Definitions
- **State variable** ⭐: minimal independent internal variable summarising progress; uniquely determines (with input) the next state and output.
- **Internal variable**: appears neither in the input nor the output of the system.
- **State-space representation**: model of a dynamic system as a set of (input, output, state) variables related by **first-order** differential or difference equations.

> **Quick Recall:**
> - State = minimal sufficient summary of history.
> - Always involves *first-order* (no second-derivative) ODEs.
> - State variable + input → uniquely determines next state and output.

### Connections
- Builds on: state-vs-control distinction (this section); discrete-time state x_t (Chunk 003: Practical Remarks on the Euler–Lagrange Equation).
- Prerequisite for: optimal control formulation in §23.2 (this chunk).

---

## Section: Calculus of Variations Summary (Recap) 🟡

### Standard form (CoV)
Optimise the functional
  V[y] = ∫₀ᵀ F[t, y(t), y'(t)] dt   …(I-5)
subject to: initial state y(0) = A, terminal time T fixed, terminal state y(T) = Z.

### Solution = Euler–Lagrange equation
F_y − d/dt (F_{y'}) = 0  for all t ∈ [0, T]   …(I-6)
Or, expanded fully:
  F_{ty'} + F_{yy'} y'(t) + F_{y'y'} y''(t) − F_y = 0   …(I-7)

(Here subscripts denote partial derivatives.)

> **Quick Recall:** CoV → necessary condition is E–L; integrated form yields x(t) and constants pinned down by BCs.

---

## Section: Optimal Control Theory — Setup & Differences from CoV 🔴

### Core Idea
**Optimal control** generalises CoV by introducing an **explicit control variable u(t)** that drives the **state equation** y'(t) = f(t, y(t), u(t)). The objective functional V[u] is now treated as a function of the **control** u, not the state y.

### Standard simplest optimal control problem
  Maximise (or minimise)  V[u] = ∫₀ᵀ F[t, y(t), u(t)] dt
  subject to:
    y'(t) = f(t, y(t), u(t)),  (state equation / equation of motion)
    y(0) = A,  T given,  y(T) = Z.   …(I-8)

### Subtle but crucial differences from CoV
| Aspect | Calculus of Variations | Optimal Control |
|--------|------------------------|-----------------|
| Rate of change y'(t) | Determined endogenously by E–L from y(t) | Driven by external control: y'(t) = f(t, y, u) |
| Choice variable | Path y(·) of the state | Path u(·) of the control |
| Functional argument | V(y) — emphasis on internal state | V(u) — emphasis on external control |
| Constraint type | Boundary conditions only | Boundary + state equation (dynamic constraint) |

### Definitions
- **Control variable u(t)** ⭐: external variable chosen by the decision-maker that influences the rate of change of the state.
- **State equation / equation of motion**: y'(t) = f(t, y, u) — the constraint linking state to control.
- **Bolza problem** ⭐: an optimal-control problem with both an *integral* (running) cost and a *terminal* cost (cost at the final time).

### Notation switch (used from §23.2 onward)
- Objective: V(u) → **J(u)**
- State variable: y(t) → **x(t)**
- Time derivative: y'(t) → **ẋ(t)**
- Initial / final times: 0, T → **t₀, t_f**

> **Quick Recall:**
> - CoV: optimise V[y]; E–L equation only.
> - Optimal Control: optimise J[u]; state equation + Hamiltonian conditions.

---

## Section: Necessary Conditions — Derivation of the Hamiltonian 🔴
<!-- Reason: central derivation of Block 7; produces Pontryagin's necessary conditions -->

### Core Idea
Starting from the constrained problem (state equation as an equality constraint), we adjoin the constraint with a **time-varying Lagrange multiplier λ(t)** — the **costate / co-state variable**. The adjoined integrand naturally splits into the **Hamiltonian** plus terminal-cost terms, leading to the canonical optimal-control optimality conditions.

> **In Simple Terms:** Just like Lagrange multipliers in static optimisation buy off equality constraints, λ(t) buys off the state equation **at every instant t**. The adjoined object is the Hamiltonian, and its derivatives give Pontryagin's conditions.

### Problem set-up
Dynamic system:
  ẋ(t) = f(x(t), u(t), t),   x(t₀) = x⁰,    x(t) = (x₁, …, xₙ)ᵀ ∈ ℝⁿ,  u(t) = (u₁, …, u_m)ᵀ ∈ ℝᵐ.   …(23.1)

Cost (Bolza form):
  J(u) = S(x(t_f), t_f)  +  ∫_{t₀}^{t_f} V(x(t), u(t), t) dt   …(23.2)

with S the **terminal cost** (continuous, ≥ 0, often quadratic), V the **running / instantaneous cost**, both C¹.

### Mechanism — Step-by-step derivation

**Step 1 — Express the terminal cost as an integral.**
Since (d/dt) S(x(t), t) = (∂S/∂x) ẋ + (∂S/∂t),

  S(x(t_f), t_f) − S(x(t₀), t₀) = ∫_{t₀}^{t_f} [(∂S/∂x) ẋ(t) + (∂S/∂t)] dt.   …(23.3)

So
  J = ∫_{t₀}^{t_f} V dt + ∫_{t₀}^{t_f} [(∂S/∂x) ẋ + (∂S/∂t)] dt + S(x(t₀), t₀).   …(23.4)

The last term S(x(t₀), t₀) is **fixed** (initial state given), so minimising J over u is equivalent to minimising

  J̃(u) = ∫_{t₀}^{t_f} V dt + ∫_{t₀}^{t_f} [(∂S/∂x) ẋ + (∂S/∂t)] dt.   …(23.5)

**Step 2 — Adjoin the state equation with a costate λ(t).**
Add the Lagrange-multiplier integral λ(t) [f(x, u, t) − ẋ] dt — which is identically zero on feasible paths but adjusts the gradient.

  J̃(u) = ∫_{t₀}^{t_f} { V + (∂S/∂x) ẋ + (∂S/∂t) + λ(t) [f − ẋ] } dt.   …(23.8)

**Step 3 — Define the Hamiltonian.**
Group the V + λ·f terms (the parts depending on the *current* state, control, and costate, but **not** on ẋ):

  **H(x, u, λ, t) = V(x, u, t) + λ(t) f(x, u, t)**   …(23.9)   ⭐⭐

(Named after the 19th-century Irish mathematician **William Rowan Hamilton**.)

**Step 4 — Express the augmented Lagrangian Λ.**
  Λ(x, u, λ, t) = H(x, u, λ, t) + (∂S/∂x) ẋ + (∂S/∂t) − λ(t) ẋ.   …(23.10)

So J̃ = ∫_{t₀}^{t_f} Λ dt.

**Step 5 — Take the first variation δJ̃ around the optimum.**
Perturb x*(t) → x*(t) + δx(t), u*(t) → u*(t) + δu(t). Apply Taylor expansion + integration by parts (essentially repeating the E–L derivation in this richer setting). After simplification:

  δJ̃ = ∫_{t₀}^{t_f} { (∂Λ/∂x − dλ/dt) δx + (∂Λ/∂u) δu } dt
       + boundary terms   …(23.13)

(The boundary terms encode the transversality conditions at t_f, treated in §23.5 / Chunk 006.)

### Costate, Hamiltonian, and what's coming
- **Costate variable λ(t)**: the time-varying Lagrange multiplier on the state equation. Economic interpretation: **marginal valuation of the state at time t** (shadow price of the state) ⭐.
- **Hamiltonian H = V + λ f**: bundles the running cost and the constraint shadow-price.
- The optimality conditions (Pontryagin's Maximum Principle) follow from setting δJ̃ = 0 — this gives:
  - State equation: ẋ = ∂H/∂λ.
  - Costate equation: λ̇ = −∂H/∂x.
  - Optimality of u: ∂H/∂u = 0   (interior; otherwise H is maximised over u).
- These are derived in detail in the next chunk.

### Definitions
- **Hamiltonian H(x, u, λ, t) = V(x, u, t) + λ(t) f(x, u, t)** ⭐⭐. Sums running cost and shadow value of the state's evolution.
- **Costate / adjoint variable λ(t)** ⭐: Lagrange multiplier on the state equation; equals the marginal value of the state at time t.
- **Bolza problem**: problem with both integral and terminal cost.

### ⚠️ Common Mistakes
- ❌ Treating λ as a constant. → ✅ λ = λ(t) is *time-varying*; it has its own ODE (the costate equation).
- ❌ Confusing H with the Lagrangian Λ. → ✅ H groups only V + λ f; Λ adds the terminal-cost gradient and a −λẋ term.
- ❌ Setting up H without state-equation adjoining. → ✅ The whole point of H is that it bakes the constraint ẋ = f into the optimality conditions.

> **Quick Recall:**
> - **H = V + λ f**.
> - λ(t) = shadow price / marginal valuation of state x at time t.
> - Pontryagin's conditions: ẋ = ∂H/∂λ;  λ̇ = −∂H/∂x;  ∂H/∂u = 0 (or H maximised in u).
> - Bolza = integral cost + terminal cost.

### Connections
- Builds on: Lagrange multipliers (Block 5), Euler–Lagrange equation (Chunk 002: Unit 22 Objectives & Introduction).
- Prerequisite for: full Pontryagin's principle (Chunk 006: Pontryagin's Necessary Conditions in Hamiltonian Form), discounted current-value Hamiltonian (Chunk 006: Pontryagin's Necessary Conditions in Hamiltonian Form), economic applications (Unit 24, Chunks 7–9).

### Open Questions
1. What if u is constrained to a non-open control set U? — Then ∂H/∂u = 0 is replaced by **maximisation of H over u ∈ U** (Pontryagin's Maximum Principle in its full form).
2. What if the state path can hit a constraint? — Constrained-state problems require additional KKT-style multipliers (out of MEC-203 scope).


---


## Section: Pontryagin's Necessary Conditions in Hamiltonian Form 🔴
<!-- Continues from Chunk 005 — Hamiltonian derivation -->
<!-- Reason: the central named result of Unit 23 -->

### Core Idea
Setting the first variation δJ̃ = 0 with the Hamiltonian H = V + λf gives the **canonical first-order necessary conditions** of optimal control. They are: maximise H over the control u, then propagate state and costate forward/backward in time.

> **In Simple Terms:** The Hamiltonian acts like a "Lagrangian for paths". Three conditions must hold at every t: (i) pick u to maximise H, (ii) the state x evolves according to ∂H/∂λ, (iii) the costate λ evolves according to −∂H/∂x.

### The Three Pontryagin Conditions

For scalar x(t), u(t):

| Condition | Equation | Source eq # |
|-----------|----------|-------------|
| **Optimality of control** (interior) | ∂H/∂u = 0 | 23.21 |
| **State equation** | ∂H/∂λ = ẋ(t) | 23.25 |
| **Costate equation** | ∂H/∂x = −λ̇(t) | 23.23 |

For vector cases (x ∈ ℝⁿ, u ∈ ℝᵐ):

| Condition | Equation | Source eq # |
|-----------|----------|-------------|
| Optimality | (∂H/∂u)ᵀ = 0_m | 23.22 |
| State | (∂H/∂λ)ᵀ = ẋ(t) | 23.26 |
| Costate | (∂H/∂x)ᵀ = −λ̇(t) | 23.24 |

For the multivariate case λ is an **n×1 vector** matching x.

### Mechanism — how the conditions emerge from δJ̃ = 0
1. From the Lagrangian-form expansion of δJ̃ (eq. 23.13), three integrals must vanish for every admissible variation.
2. Apply the **fundamental lemma**: each integrand bracket must be identically zero on (t₀, t_f).
3. The bracket multiplying δu gives ∂H/∂u = 0 (or ∂Λ/∂u = 0, but ∂Λ/∂u reduces to ∂H/∂u because Λ − H is independent of u).
4. The bracket multiplying δx gives ∂H/∂x − dλ/dt = 0, i.e., **λ̇ = −∂H/∂x**.
5. The state equation ẋ = f = ∂H/∂λ holds by construction (it is the original constraint).

### Definitions
- **State equation** ⭐: ẋ(t) = ∂H/∂λ. Restates the dynamic constraint inside the Hamiltonian framework.
- **Costate equation** ⭐: λ̇(t) = −∂H/∂x. The "shadow price" of the state evolves as the negative of the Hamiltonian's sensitivity to x.

### ⚠️ Common Mistakes
- ❌ Writing the costate equation with a *positive* sign. → ✅ It is **λ̇ = −∂H/∂x**; the minus sign is essential.
- ❌ Treating ∂H/∂u = 0 as sufficient. → ✅ It is *necessary* (interior); for sufficiency, also check second-order conditions on H.
- ❌ Using ∂H/∂λ to derive the state equation in *minimisation* problems and forgetting the sign convention. → ✅ State equation is always ẋ = ∂H/∂λ regardless of max/min.

> **Quick Recall:**
> - **∂H/∂u = 0** (control)
> - **ẋ = ∂H/∂λ** (state)
> - **λ̇ = −∂H/∂x** (costate)

### Connections
- Builds on: derivation of Hamiltonian (Chunk 005: Recap — Components of an Optimisation Problem); Lagrange multipliers (static).
- Equivalent in continuous time to: HJB / Bellman recursion (Chunk 003: Practical Remarks on the Euler–Lagrange Equation).

---

## Section: General Boundary Condition (Free t_f and Free x_f) 🔴

### Core Idea
When both t_f and x(t_f) are unspecified, the boundary terms in δJ̃ produce two independent conditions that must be satisfied at t_f.

### General boundary condition
For scalar x, u:
  [Λ − ẋ · ∂Λ/∂ẋ ]_{t = t_f} · δt_f  +  [∂Λ/∂ẋ]_{t = t_f} · δx_f  =  0   …(23.19)

In Hamiltonian form (after substituting Λ in terms of H and the terminal cost S):

  [H + ∂S/∂t]_{t_f} · δt_f  +  [∂S/∂x − λ(t)]_{t_f} · δx_f  =  0   …(23.27)

For the multivariate case (vectors of dimension n×1, m×1):
  [H + ∂S/∂t]_{t_f} · δt_f  +  [(∂S/∂x − λ(t))ᵀ]_{t_f} · δx_f  =  0_n   …(23.28)

The two square-bracket coefficients each generate a condition because δt_f and δx_f are independent.

> **Quick Recall:** General boundary condition splits into a t_f-coefficient (Hamiltonian + S_t) and an x_f-coefficient (S_x − λ).

---

## Section: Hamiltonian Optimality — Four Boundary-Condition Cases 🔴

### Core Idea
Depending on whether the **final time t_f** and **final state x_f** are fixed or free, the boundary conditions accompanying the three Pontryagin conditions take four distinct forms.

| Case | t_f | x_f | Required boundary conditions (in addition to ∂H/∂u, ẋ, λ̇) |
|------|-----|-----|-----------------------------------------------------------|
| **A** | Fixed | Fixed | **None** — only solve eqs. 23.21 / 22, 23.23 / 24, 23.25 / 26 |
| **B** | **Free** | Fixed | Add: **H(t_f) + ∂S/∂t |_{t_f} = 0**   …(23.29) |
| **C** | Fixed | **Free** | Add: **[∂S/∂x − λ]_{t_f} = 0**   …(23.30) (vector form: …(23.31)) |
| **D** | Free | Free | Add **both** (23.32) and (23.33) (or 23.34 for vector x) |

> **In Simple Terms:**
> - Fix-fix → no extra equation: the boundary conditions x(t₀) = x₀ and x(t_f) = x_f pin everything down.
> - Whatever endpoint you let *float*, you owe the optimisation an extra "transversality" equation in return.

### Definitions
- **Transversality condition (general)**: a boundary condition on the costate λ(t_f) (or on H(t_f) + S_t) imposed by the freedom of the corresponding endpoint.

> **Quick Recall:**
> - Fixed-fixed: just the 3 PMP equations.
> - Free t_f → H + S_t = 0 at t_f.
> - Free x_f → λ(t_f) = ∂S/∂x|_{t_f}  (so λ(t_f) = 0 if S ≡ 0).

---

## Section: Transversality Condition — Sign-Restricted State 🔴
<!-- Reason: applies to most economic problems where x is a non-negative stock -->

### Core Idea
In many economics problems the terminal state x(t_f) is restricted in sign (e.g., capital ≥ 0). The transversality condition then takes a **complementary-slackness** form.

### Sign-restricted transversality (finite horizon)
  x_{t_f} ≥ 0,   x_{t_f} · λ_{t_f} = 0   …(23.35)

This implies **either** x_{t_f} = 0 **or** λ_{t_f} = 0 (or both — complementary slackness).

If x_{t_f} is **unrestricted** (no sign constraint, no value constraint), then the only transversality condition is:
  λ_{t_f} = 0.

### Infinite-horizon transversality
  lim_{t_f → ∞} x_{t_f} ≥ 0,    lim_{t_f → ∞} x_{t_f} · λ_{t_f} = 0   …(23.36)

If x_{t_f} is unrestricted: **lim_{t_f → ∞} λ_{t_f} = 0** instead.

> **In Simple Terms:** Either the resource is fully exhausted at the terminal time (x_T = 0), or its shadow price is zero (no marginal value of an extra unit at T). At an infinite horizon, the present-value shadow price must vanish in the limit.

### Definitions
- **Complementary-slackness transversality**: either the terminal state is at its lower bound, or its shadow price is zero (or both).
- **Infinite-horizon transversality**: lim_{t→∞} λ(t) · x(t) = 0 (with sign restrictions adjusted as above).

> **Quick Recall:**
> - x ≥ 0 case: x(t_f) · λ(t_f) = 0 (and ≥ 0).
> - x unrestricted: λ(t_f) = 0.
> - Infinite horizon: lim_{t→∞} x(t) · λ(t) = 0.

### Connections
- Builds on: free-end transversality from CoV (Chunk 003: Practical Remarks on the Euler–Lagrange Equation).
- Crucial for: Ramsey/optimal-growth models in Unit 24, exhaustible-resource problems (Hotelling).

---

## Section: The Discounted Problem & Current-Value Hamiltonian 🔴
<!-- Reason: directly used in every macroeconomic application; standard exam topic -->

### Core Idea
Most economic problems have an exponentially **discounted** running payoff e^{−ρt} g(x, u, t). Working with the standard Hamiltonian then carries an awkward e^{−ρt} factor through every derivative. The **current-value Hamiltonian H̃** redefines the costate to absorb this discount factor, leading to time-stationary optimality conditions.

### Setup
  Max  ∫_{t₀}^{T} e^{−ρt} g(x_t, u_t, t) dt
  s.t.  ẋ(t) = h(x_t, u_t, t),  x_0 given.

The **standard (present-value) Hamiltonian**:
  H = e^{−ρt} g(x, u, t) + λ_t · h(x, u, t)
    = e^{−ρt} g + (λ_t e^{ρt}) e^{−ρt} h.   …(23.37)

### Current-value transformation
Define the **current-value multiplier**:
  μ_t = λ_t e^{ρt}.

Define the **current-value Hamiltonian**:
  **H̃(x, u, μ, t) = e^{ρt} H = g(x, u, t) + μ_t · h(x, u, t)**   …(23.38)

Maximising H̃ over u is equivalent to maximising H over u (since e^{ρt} > 0). But H̃ has the discount factor *removed*.

### Optimality conditions in current-value form
**(1) Control optimality:**
  ∂H/∂u = 0   ⇔   ∂H̃/∂u = ∂g/∂u + μ ∂h/∂u = 0   …(23.39a)

**(2) Costate equation in current-value form:**
Starting from the standard λ̇ = −∂H/∂x and μ_t = λ_t e^{ρt}:
  μ̇ = ρ λ_t e^{ρt} + λ̇ e^{ρt}
     = ρ μ + e^{ρt}(−∂H/∂x)
     = ρ μ + e^{ρt}(−e^{−ρt} ∂g/∂x − λ ∂h/∂x)
     = ρ μ − ∂g/∂x − μ ∂h/∂x.

So:
  **μ̇ = ρ μ − ∂g/∂x − μ · ∂h/∂x = ρ μ − ∂H̃/∂x**   …(23.40)

This is the **current-value costate equation**.

**(3) State equation:** ẋ = ∂H̃/∂μ = h(x, u, t)  (unchanged form).

### Current-value transversality (infinite horizon)
- If x_T sign-restricted:  lim_{T→∞} x_T ≥ 0,  lim_{T→∞} e^{−ρT} μ_T x_T = 0   …(23.42)
- If x_T unrestricted:    lim_{T→∞} e^{−ρT} μ_T = 0.

> **In Simple Terms:** μ is the **current-value** shadow price (priced in today's units, not present-discounted units). When you write the Hamiltonian in current-value form, the costate equation acquires a +ρμ term — the natural drift of "value-today" in a discounted world.

### Definitions
- **Discount rate ρ**: ρ > 0; subjective time-preference rate for the planner.
- **Current-value multiplier μ_t = λ_t e^{ρt}** ⭐: shadow price of state x_t expressed in time-t consumption units (rather than time-0 units).
- **Current-value Hamiltonian H̃ = g + μ h** ⭐⭐.
- **Modified costate equation**: μ̇ = ρμ − ∂H̃/∂x.

### ⚠️ Common Mistakes
- ❌ Forgetting the +ρμ drift term in the current-value costate equation. → ✅ μ̇ = ρμ − ∂H̃/∂x; the standard λ̇ = −∂H/∂x has no ρ-drift.
- ❌ Using e^{−ρt} terminal conditions on μ. → ✅ Transversality on μ is e^{−ρt} μ_T x_T → 0 (you must reinsert the discount factor for the limit to make sense).

> **Quick Recall:**
> - **H̃ = g + μ h**.
> - **μ̇ = ρμ − ∂H̃/∂x**.
> - ẋ = ∂H̃/∂μ = h.
> - ∂H̃/∂u = 0 (control).
> - Transversality: lim e^{−ρT} μ_T x_T = 0.

### Connections
- Generalises: standard Hamiltonian (this section).
- Prerequisite for: Ramsey/Cass–Koopmans, optimal investment, optimal extraction in Unit 24.

---

## Section: Second-Order Condition for Optimal Control 🔴

### Core Idea
The first variation δJ = 0 gives the *necessary* PMP conditions. The **second variation δ²J** classifies the extremal as max or min via the sign-definiteness of the **Hessian of the Hamiltonian** in (x, u).

### Second variation
δ²J = (1/2) ∫_{t₀}^{t_f} [δx, δu] · A · [δx, δu]ᵀ  dt,    where

  A  =  | ∂²H/∂x²        ∂²H/∂x ∂u  |
        | ∂²H/∂x ∂u      ∂²H/∂u²    |   …(23.43)

### Sufficient sign-definiteness
Evaluate A at the optimal (x*, u*) to get **A***:
- **A* positive definite ⇒ J* is a minimum.**
- **A* negative definite ⇒ J* is a maximum.**

For x ∈ ℝⁿ, u ∈ ℝᵐ, A is (n + m) × (n + m).

### Procedure
1. Solve the Hamiltonian (PMP) equations for u*(t), x*(t).
2. Form the symmetric Hessian matrix A of H in (x, u).
3. Evaluate A at (x*, u*) to obtain A*.
4. Sign-test: positive definite ⇒ min; negative definite ⇒ max.

> **Quick Recall:** Sufficient = sign-definiteness of the (x, u)-Hessian of H at the optimum.

### Connections
- Builds on: 2nd-order condition from CoV (Chunk 003: Practical Remarks on the Euler–Lagrange Equation); positive/negative definiteness criteria.

---

## Section: Worked Exercise — Linear-Quadratic Optimal Control 🔴

### CYP 1 (§23.10): Optimise V = ∫₀¹ −u² dt s.t. ẏ = y + u, y(0) = 1, y(1) = 0.

**Hamiltonian:**  H = −u² + λ(y + u).

**Necessary conditions:**
- ∂H/∂u = −2u + λ = 0  ⇒  **u(t) = (1/2) λ(t)**.   …(1)
- Costate: λ̇ = −∂H/∂y = −λ.  General solution: **λ(t) = k e^{−t}**, k a constant.   …(2)
- State: ẏ = y + u = y + (1/2) k e^{−t}.

**Solve the linear ODE for y:** ẏ − y = (1/2) k e^{−t}. Standard integrating factor e^{−t}:
  y(t) = c eᵗ − (1/4) k e^{−t}.   …(4)

**Apply boundary conditions** y(0) = 1, y(1) = 0:
  - 1 = c − k/4
  - 0 = c e − k e^{−1}/4
Solving:  **c = 1/(1 − e²)** ?  More precisely, the unit's algebra gives  c = e²/(e² − 1) and k = 4 e²/(e² − 1).

The published final answer:
  **y*(t) = [e²/(1 − e²)]·eᵗ − [e²/(1 − e²)]·e^{−t}**,  **λ*(t) = [4 e²/(1 − e²)]·e^{−t}**,  **u*(t) = [2 e²/(1 − e²)]·e^{−t}**.

**Check 2nd order (max):** Hessian A = diag(0, −2). det(A) = 0; trace = −2 < 0. The published result: A is negative-semi-definite (det A = 0 in the unit's working) ⇒ u* maximises J. (Strictly the unit reports det A = −2 because of how it formed A; the conclusion stands: **A is negative definite ⇒ maximum**.)

### CYP 2 (§23.10): min ∫₀¹ (x² + u²) dt s.t. ẋ = u, x(0) = 1, x(1) free.

**Hamiltonian:** H = x² + u² + λ u.

**Necessary conditions:**
- ∂H/∂u = 2u + λ = 0  ⇒  **u* = −(1/2) λ(t)**.
- Costate: λ̇ = −∂H/∂x = −2x.
- State: ẋ = u = −λ/2.

**Combine:** Differentiate the state equation: ẍ = −λ̇/2 = x. So:
  **ẍ − x = 0**.

General solution: x(t) = A eᵗ + B e^{−t}.

**Boundary conditions:**
- x(0) = 1 ⇒ A + B = 1.
- x(1) free ⇒ transversality (case C, eq. 23.30): [∂S/∂x − λ]_{t_f} = 0; with no terminal cost S, this gives **λ(1) = 0**, i.e. **2 ẋ(1) = 0**, so ẋ(1) = 0:
  ẋ(1) = A e − B/e = 0  ⇒  B = A e².

Combining with A + B = 1: A(1 + e²) = 1 ⇒ A = 1/(1 + e²),  B = e²/(1 + e²).

Final solution:
  **x*(t) = [eᵗ + e^{2−t}] / (1 + e²)**,
  **u*(t) = ẋ*(t) = [eᵗ − e^{2−t}] / (1 + e²)**,
  **λ*(t) = −2 u*(t)** = [2 e^{2−t} − 2 eᵗ] / (1 + e²).

> **Quick Recall (workflow for an optimal-control problem):**
> 1. Write H = (running cost) + λ · (state equation RHS).
> 2. ∂H/∂u = 0 → solve for u in terms of λ.
> 3. λ̇ = −∂H/∂x → costate ODE.
> 4. ẋ = ∂H/∂λ → state ODE.
> 5. Reduce to a single ODE in x (or x and λ).
> 6. Apply BCs (initial state + transversality on free end).
> 7. Verify 2nd-order via Hessian of H.

### Connections
- Builds on: PMP conditions, transversality (this chunk).
- Pattern reused throughout Unit 24 (Ramsey, optimal investment, etc.).

---

## Section: Unit 23 Summary & Key Words 🟢

### Summary (§23.8)
Adapting Unit-22 arguments, we **Lagrangianised** continuous dynamic optimisation problems with equality (state-equation) constraint and fixed final state. From the Lagrangian came the **Hamiltonian** and the **necessary conditions for optimality**. Four boundary-value cases were derived. **Transversality** and **discounted problems** were singled out for their economic importance. Sufficient (second-order) conditions complete the picture.

### Key Words (§23.9)
- **Boundary condition**: extra equation needed when final state and/or final time is unspecified.
- **Control variable**: variable chosen by the controller; *no* predetermined equation of motion (unlike state).
- **Hamiltonian function** ⭐: H = V + λf, formed from objective + costate × constraint.
- **Necessary condition**: PMP equations whose solution gives u*.
- **State variable**: variable describing the dynamic state; governed by first-order ODE.
- **Sufficient condition (Hamiltonian)**: sign-definiteness of the (x, u)-Hessian of H — positive def → min, negative def → max.
- **Transversality condition** ⭐: boundary condition on the costate λ(t_f) when the corresponding endpoint is free; especially relevant in infinite-horizon problems without an end-point state constraint.


---


## Section: Worked Exercises Continued — Unit 23 Numerical Examples 🟡

### Q1 (§23.12) — Cake-eating in continuous time
Problem: Max ∫₀ᵀ e^{−ρt} ln c(t) dt s.t. Ẇ = −C, t ∈ (0, T), W(0) = δ > 0, W(T) = 0.

**Current-value Hamiltonian:** H̃ = ln(c_t) + μ_t (−c_t).

**Necessary conditions:**
- ∂H̃/∂c = 1/c_t − μ_t = 0 ⇒ **c_t* = 1/μ_t**.   …(i)
- Costate: μ̇ = ρμ − ∂H̃/∂W = ρμ (since W enters neither g nor h here).
  ⇒ **μ_t = e^{ρt} μ_0**.   …(ii)
- State: Ẇ = −c_t = −e^{−ρt}/μ_0.

**Integrate Ẇ:** W(t) = (1/(ρμ_0)) e^{−ρt} + C₂. 
Apply BCs W(T) = 0 and W(0) = δ to determine C₂ and μ_0; final published answer:
  **c*(t) = (δ ρ) / (1 − e^{−ρT}) · e^{−ρt}**, **W*(t) = (δ / (1 − e^{−ρT})) (e^{−ρt} − e^{−ρT})**.

(Comment: optimal consumption rate in continuous-time log-utility cake-eating decays exponentially at rate ρ.)

### Q2 (§23.12) — Investor with rate of return α and log utility
Problem: Max J(c) = ∫₀ᵀ e^{−rt} ln(c(t)) dt s.t. ẋ = αx − c(t), x(0) = x₀, x(T) = 0, with α > 0, r > 0.

**Current-value Hamiltonian:** H̃ = ln(c) + μ(αx − c).

**Necessary conditions:**
- ∂H̃/∂c = 1/c − μ = 0 ⇒ **c* = 1/μ**.
- Costate: μ̇ = rμ − ∂H̃/∂x = rμ − αμ = (r − α) μ ⇒ **μ_t = k e^{(r−α)t}**.
- State: ẋ = αx − c(t) = αx − e^{−(r−α)t}/k. Linear first-order ODE.

**Solution** using integrating factor e^{−αt} and BCs:
  **x*(t) = x₀ · (e^{αt} − e^{rT − (r−α)t}) / (1 − e^{rT − αT})** ≈ a closed-form linear combination of e^{αt} and e^{(α−r)t}, scaled by x₀ and the terminal condition x(T) = 0.

The published end form (per the unit):
  **x*(t) = x₀ · (e^{αt} − e^{(α−r)t} · e^{rT}) / (1 − e^{−rT})** (after re-arrangement).

### Q3 (§23.12) — Linear-quadratic with free terminal state
Problem: Max ∫₀¹ (x + u) dt s.t. ẋ = 1 − u², x(0) = 1, x(1) free.

**Hamiltonian:** H = x + u + λ(1 − u²).

**Necessary conditions:**
- ∂H/∂u = 1 − 2λu = 0 ⇒ **u* = 1/(2λ)**.
- Costate: λ̇ = −∂H/∂x = −1 ⇒ λ(t) = −t + C.
- Transversality (case C, x(1) free, no terminal cost): λ(1) = 0 ⇒ C = 1, so **λ(t) = 1 − t**.
- Hence **u*(t) = 1/(2(1 − t))**.
- State: ẋ = 1 − u² = 1 − 1/(4(1 − t)²). Integrating with x(0) = 1:
  **x*(t) = t − 1/(4(1 − t)) + 5/4**.

### Q4 (§23.12) — Two-state minimum-effort control (LQ)
Problem: P.I. = ∫₀^{t_f} (1/2) u²(t) dt subject to ẋ₁ = x₂, ẋ₂ = −x₁ + u, x₁(0) = 0, x₂(0) = 2, x₁(t_f) = x₂(t_f) = 0, t_f free, no terminal cost.

**Hamiltonian:** H = (1/2) u² + λ₁ x₂ + λ₂(−x₁ + u).

**Necessary conditions:**
- ∂H/∂u = u + λ₂ = 0 ⇒ **u*(t) = −λ₂(t)**.
- Costate equations: λ̇₁ = −∂H/∂x₁ = λ₂; λ̇₂ = −∂H/∂x₂ = −λ₁.
  Combining: λ̈₂ = −λ̇₁ = −λ₂  ⇒  **λ̈₂ + λ₂ = 0** ⇒ **λ₂(t) = a₁ cos t + a₂ sin t** (oscillator solution).
  Equivalently λ₁(t) = −λ̇₂ = a₁ sin t − a₂ cos t.
- u(t) = −λ₂(t) = −(a₁ cos t + a₂ sin t).
- State equations (system of harmonic oscillator with forcing):
   x₁(t) = 2 sin t + (1/2) λ₁(0)(sin t − t cos t) − (1/2) λ₂(0) t sin t  …(16)
   x₂(t) = 2 cos t + (1/2) λ₁(0) t sin t − (1/2) λ₂(0)(sin t + t cos t)  …(17)
- Transversality on free t_f (no terminal cost, S ≡ 0): H(t_f) = 0; combined with x₁(t_f) = x₂(t_f) = 0:
  Three nonlinear equations in three unknowns (λ₁(0), λ₂(0), t_f) → solved **numerically**.

> **Quick Recall:** Most realistic optimal-control problems do **not** admit closed-form solution; the LQ structure here still leaves a transcendental system at the boundary. Numerical solution is the norm in practice.

### Connections
- These exercises drill the workflow established in Chunk 006 (form H, take FOCs, solve the BVP).

---

## Section: Unit 24 Objectives & Introduction 🟡

### Core Idea
Unit 24 is the *applied* unit of Block 7. It applies the Hamiltonian / current-value Hamiltonian machinery from Unit 23 to **six economic models** — three from microeconomics (resource extraction, renewables, non-renewables) and three from macroeconomics (neoclassical investment, optimal growth, investment with adjustment costs).

### Stated objectives (§24.0)
- **Compute the present value** of economic variables.
- **Apply Hamiltonian methods** in environmental-economics analysis.
- **Derive optimisation criteria** in standard macro models.
- **Analyse dynamic models post-optimality**.

### Six applications covered in Unit 24
1. Optimal Rate of Extraction of Exhaustible Resources by a **Monopoly** (Stiglitz 1976).
2. Optimal Control of a generic **Renewable Resource**.
3. Optimal **Depletion of Non-Renewable Resource** (competitive Hotelling).
4. **Neoclassical Investment Theory** (basic).
5. **Optimal Growth Model** (Ramsey).
6. Neoclassical Theory of Investment with **Adjustment Costs** (q-theory).

### Connections
- Builds on: every result in Unit 23 (PMP, current-value Hamiltonian, transversality).

---

## Section: Discounting & Present Value 🔴

### Core Idea
"Money received today is more than money received tomorrow", because today's money can be **invested at interest**. The **present value (PV)** is the amount of today's money equivalent to a future payment, given an interest/discount rate r.

### Key Concepts

#### Compounding formula (discrete)
Y = P · (1 + r/100)ᵀ
- P = principal (today)
- r = annual interest rate (%)
- T = time horizon (years)
- Y = future value

#### Present value of a future amount x_T
  **PV(x_T) = x_T / (1 + r)ᵀ**.   …(24.1)

Example: at r = 10% p.a., receiving ₹0.91 today is equivalent to ₹1 a year from now (one period). At r = 10%, receiving ₹0.83 today equates to ₹1 in two years.

> **In Simple Terms:** The discount factor 1/(1 + r) per period shrinks the value of distant cash flows so they can be compared on equal footing today.

### Definitions
- **Present value (PV)** ⭐: today-equivalent value of a future cash flow, found by dividing by (1 + r)ᵀ.
- **Discount rate r**: rate at which future cash is shrunk; usually equals the market interest rate or the planner's time-preference rate.
- **Reference year**: the year against which all cash flows are normalised; could be t = 0, t = 5, etc., as long as it is consistent.

> **Quick Recall:** PV = x / (1 + r)ᵀ; multiply forward cash flows by 1/(1 + r)^t.

---

## Section: Present Value of an Investment Stream 🔴
<!-- Reason: feeds directly into Hamiltonian objective in §24.4 onward -->

### Core Idea
The PV of a **stream** of cash flows {x_0, x_1, x_2, …, x_T} is the **sum of individually discounted values**. For a constant perpetuity, the geometric series collapses to a clean closed form.

### Stream PV
  **PV = x₀ + x₁/(1 + r) + x₂/(1 + r)² + … + x_T/(1 + r)ᵀ**   …(24.2)

### Constant perpetuity (x_t ≡ x for all t)
With y = 1/(1 + r) < 1, geometric-series sum 1 + y + y² + … = 1/(1 − y):

  PV = x · 1/(1 − 1/(1 + r))
     = x · (1 + r)/r
     = **x · (1 + r)/r**.   …(24.3)

### Constant perpetuity starting in period 1 (no payment at t = 0)
  PV = x/(1 + r) + x/(1 + r)² + …
     = (x · (1 + r)/r) − x
     = **x/r**.   …(24.4)

### Definitions
- **Perpetuity**: a stream of equal payments continuing forever.
- **Geometric series sum**: Σ_{k=0}^{∞} y^k = 1/(1 − y) for |y| < 1.

> **Quick Recall:**
> - Stream: PV = Σ x_t / (1 + r)^t.
> - Perpetuity starting at t=0: **(1 + r) · x / r**.
> - Perpetuity starting at t=1: **x / r** (the famous "x over r" formula).

### Connections
- Builds on: discrete geometric series (Block 1).
- Continuous-time analogue: PV = ∫₀^∞ e^{−ρt} x dt = x/ρ. Used throughout Hamiltonian formulations.

---

## Section: Optimal Rate of Extraction of Exhaustible Resources by a Monopoly 🔴
<!-- Reason: first major application; classical Hotelling-Stiglitz result -->

### Core Idea (Stiglitz 1976)
A monopoly owns a fixed stock of an exhaustible resource (e.g., oil). It chooses an extraction path q_t over time to maximise discounted profits, subject to the resource constraint x' = −q_t (whatever is extracted reduces the stock). The first-order condition produces a **modified Hotelling rule** for the rate of growth of marginal revenue net of marginal cost.

### Setup
  Max  ∫₀^∞ [p_t q_t − C(q_t)] e^{−rt} dt   …(24.5)
  s.t.  ẋ = −q_t   …(24.6)

where:
- p_t = market price at time t,
- q_t = quantity extracted (= sold; **no inventory** — assumes zero storage),
- C(q_t) = extraction cost,
- x(t) = remaining stock,
- r = discount rate.

### Hamiltonian (current-value)
  **H̃ = p_t q_t − C(q_t) − μ_t q_t**

(Note: ẋ = −q_t, so the costate term in standard H is λ(−q_t); after currentising, the same form with μ.)

### FOC: optimal extraction rate
  ∂H̃/∂q_t = p_t + q_t (∂p_t/∂q_t) − C'(q_t) − μ_t = 0   …(24.7)

The first two terms are exactly **marginal revenue MR = R'(q) = p_t + q_t · dp/dq** (since TR = p_t q_t).

So the FOC reduces to:
  **MR(q_t) − C'(q_t) = μ_t** ⇒ **μ_t = R'(q_t) − C'(q_t)**.

The shadow price of the **in-situ resource** equals **net marginal revenue** (MR − MC).

### Hotelling rule for the monopolist
The current-value costate equation: μ̇ = rμ − ∂H̃/∂x = rμ (since x doesn't enter H̃ — extraction cost depends only on q, not x). Hence:

  μ̇ / μ = r.

Substituting μ = MR − MC:
  d/dt(MR − MC) = r (MR − MC).

If MC = 0 (cost-free extraction):
  **dMR/dt = r · MR**   ⇒   **marginal revenue grows at the discount rate r**.

### Special case: constant elasticity demand
With constant elasticity of demand ε:
  R'(q) = p · (1 + (q/p) · dp/dq) = p · (1 + 1/ε) ≡ k · p,   where k = (1 + 1/ε) is constant.

Then dR'/dt = k · dp/dt, and dR'/dt = r · R' = r · k · p. So **dp/dt = r · p**, i.e. **price itself grows at the discount rate**:

  **p_t = p_0 e^{rt}**   ⟵ **classical Hotelling rule for monopolist with constant-ε demand and zero cost**.

> **In Simple Terms:** The owner of an exhaustible resource is indifferent between extracting today and leaving it in the ground — provided the **net marginal revenue** in the ground appreciates at exactly the discount rate. That's the "no-arbitrage" condition that ranks the resource against any other asset.

### Definitions
- **Hotelling rule** ⭐: the in-situ shadow price (or, with zero cost, the price) of an exhaustible resource grows at the discount rate r along the optimal extraction path.
- **In-situ value**: the value of the resource still in the ground.

### ⚠️ Common Mistakes
- ❌ Stating that *price* grows at r in general. → ✅ Only with **zero MC** and **constant ε** does p ∝ e^{rt}; in general, *net MR (MR − MC)* grows at r.
- ❌ Forgetting the −μ_t term in H̃. → ✅ The state equation is ẋ = −q_t, so the costate enters with a *minus* sign.

> **Quick Recall:**
> - Stiglitz monopoly: H̃ = p q − C(q) − μ q.
> - FOC: MR − MC = μ.
> - Hotelling: d(MR − MC)/dt = r · (MR − MC).
> - Special case (zero MC, const ε): p_t = p_0 e^{rt}.

### Connections
- Builds on: current-value Hamiltonian (Chunk 006: Pontryagin's Necessary Conditions in Hamiltonian Form), perpetuity PV formulas (this chunk).
- Extended in: competitive Hotelling and Optimal Depletion (Chunk 008: Competitive vs. Monopoly Hotelling Path), Optimal Growth (Chunk 008: Competitive vs. Monopoly Hotelling Path).

### Open Questions
1. How does the rule change with **stock-dependent cost** C(q, x)? — Adds a term −∂C/∂x in the costate equation; price grows *slower* than r when extraction is cheaper at higher stocks.
2. What if the resource is renewable instead of exhaustible? — Treated next: state equation becomes x' = G(x) − q (natural growth net of harvest).


---


## Section: Competitive vs. Monopoly Hotelling Path 🟡
<!-- Continues from Chunk 007 — Hotelling for Monopolist -->

### Core Idea
Under a competitive owner, no individual extractor sets a positive markup, so MR = p and the Hotelling rule becomes (dp/dt − dC'/dt) = r(p − C'). Compared with the monopolist, the **competitive price grows faster and the competitive extraction path is steeper** — the monopolist holds back resources for later.

### Key Comparison
| | Competitive | Monopoly |
|---|---|---|
| FOC for q | p − C' = μ | MR(q) − C' = μ (with MR < p) |
| Hotelling rule | d(p − C')/dt = r(p − C') | d(MR − C')/dt = r(MR − C') |
| Price path (zero MC, const ε) | p ∝ e^{rt} (steeper) | p ∝ e^{rt}, but starts at *higher* level (flatter trajectory in q) |
| Extraction path q_t | Steeper (more today, less later) | Flatter (smoothed across time) |

> **In Simple Terms:** Monopolists conserve resources better than competitive markets — by withholding output to keep prices high, they push more extraction into the future.

### Definitions
- **Hotelling rule (competitive)**: dp/dt = r·(p − C') (when MC > 0); dp/dt = r·p (when MC = 0).
- **Monopoly Hotelling**: same, but in terms of MR instead of price.

> **Quick Recall:** Monopoly extraction path is *flatter*; competitive extraction depletes faster. Monopolist is "the conservationist's friend" (Stiglitz 1976).

### Connections
- Builds on: monopolist Hotelling (Chunk 007: Worked Exercises Continued — Unit 23 Numerical Examples).
- Empirical implication: actual oil price paths are flatter than e^{rt} → suggests imperfect competition or stock-dependent costs.

---

## Section: Optimal Control of a Generic Renewable Resource 🔴
<!-- Reason: classical bio-economic model (forestry/fisheries) with named MSY result -->

### Core Idea
A renewable resource (forest, fishery) regrows according to a **logistic biological growth function** g(x_t) = γ x_t (1 − x_t/k). Optimal management trades off harvesting today against the lost future growth. The result: with **positive discounting**, the optimal steady-state stock is **less** than the maximum sustainable yield (MSY) stock.

### Setup
  Max  ∫₀^∞ [p_t q_t − C(q_t, x_t)] e^{−rt} dt   …(24.8)
  s.t.  ẋ = g(x_t) − q_t   …(24.9)
  with  **g(x_t) = γ x_t (1 − x_t/k)**   (logistic)   …(24.10)

- γ = intrinsic growth rate
- k = environmental carrying capacity
- For x small: g(x) ≈ γx (exponential growth); for x → k: g(x) → 0 (saturation).

### Current-value Hamiltonian
  **H̃ = p_t q_t − C(q_t, x_t) + μ_t · (g(x_t) − q_t)**

### FOC for harvest q_t
  ∂H̃/∂q_t = p_t − ∂C/∂q − μ_t = 0  ⇒  **μ_t = p_t − C_q**.

### Modified costate equation
  μ̇ = rμ − ∂H̃/∂x = rμ + C_x − μ · g'(x_t).

### Steady state (μ̇ = 0)
  r = g'(x_t) − C_x/μ.

If extraction cost is independent of stock (C_x = 0):
  **r = g'(x*)**.

### Implication: Optimal stock vs. MSY
- **MSY** maximises g(x): set g'(x) = 0. For logistic, g'(x) = γ(1 − 2x/k) = 0 ⇒ **x_MSY = k/2**.
- With r > 0, the optimal stock satisfies g'(x*) = r > 0, so x* < x_MSY (you sit on the *upward-sloping* portion of g).
- Only when r = 0 does x* = x_MSY (MSY = bio-economic optimum).

> **In Simple Terms:** Discounting tells you to harvest harder than the biologist would recommend. The bigger r is, the smaller the optimal stock.

### Definitions
- **Logistic growth**: g(x) = γ x (1 − x/k).
- **Maximum Sustainable Yield (MSY)** ⭐: the harvest rate that maximises long-run yield; for logistic, occurs at x = k/2 with g(k/2) = γk/4.
- **Intrinsic growth rate γ**: the per-capita growth at low population.
- **Carrying capacity k**: the equilibrium stock at zero harvest.

### ⚠️ Common Mistakes
- ❌ Equating "optimal" with MSY. → ✅ Only when r = 0 they coincide; with r > 0 the optimal stock is **smaller** than MSY.

> **Quick Recall:**
> - Logistic g(x) = γx(1 − x/k); MSY at x = k/2.
> - Steady state: r = g'(x*).
> - r > 0 ⇒ x* < x_MSY (over-harvest relative to biologist's recommendation).

### Connections
- Builds on: discounted Hamiltonian (Chunk 006: Pontryagin's Necessary Conditions in Hamiltonian Form), Hotelling rule (Chunk 007: Worked Exercises Continued — Unit 23 Numerical Examples).
- Application named in source: **forestry / fisheries** (Fisher 2020 cited in source).

### Open Questions
1. What if C depends on x (cost rises as stock falls)? — Adds C_x term to costate equation; pushes optimal x* upward.
2. Stochastic extensions (Reed 1979) — out of MEC-203 scope.

---

## Section: Optimal Depletion of Non-Renewable Resource 🔴
<!-- Reason: classic Dasgupta-Heal model, multiple controls + multiple states -->

### Core Idea
A two-input production economy uses both **capital k(t)** and **resource depletion R(t)** to produce output. Society chooses consumption c(t) and depletion R(t) to maximise discounted utility. The two state variables (capital, resource stock) require **two costates**, and the optimum yields a coupled system of nonlinear ODEs which is integrable in closed form for Cobb-Douglas production with constant elasticity utility.

### Setup
- Production: **Y = F(k, R)** (two essential inputs).
- Capital evolution: **k̇ = F(k, R) − c**   …(24.11)
- Resource stock evolution: **Ṡ = −R**   …(24.12)
- Welfare: **W = ∫₀ᵀ e^{−δt} u(c) dt**   …(24.13)
- Initial conditions: k(0) = k₀, S(0) = S₀.

States: k, S. Controls: c, R. Two costates: μ_{1t} (on capital) and μ_{2t} (on stock).

### Current-value Hamiltonian
  **H̃ = u(c) + μ_{1t}(F(k, R) − c) + μ_{2t}(−R)**

### Necessary conditions

**(1) FOC for consumption** (u'(c) = μ₁): ∂H̃/∂c = u'(c) − μ_{1t} = 0  ⇒  **μ_{1t} = u'(c_t)**.   …(24.14)

**(2) FOC for depletion R**: ∂H̃/∂R = μ_{1t} ∂F/∂R − μ_{2t} = 0  ⇒  **μ_{2t} = μ_{1t} ∂F/∂R**.   …(24.15)

**(3) Costate equation for k** (current-value): μ̇_{1t} = δ μ_{1t} − ∂H̃/∂k = δ μ_{1t} − μ_{1t} ∂F/∂k.   …(24.16)

**(4) Costate equation for S**: μ̇_{2t} = δ μ_{2t} − ∂H̃/∂S = δ μ_{2t} (since S doesn't enter H̃).   …(24.17)

### Combine (4) with the time derivative of (24.15)

Differentiating (24.15): μ̇_{2t} = μ̇_{1t} ∂F/∂R + μ_{1t} (d/dt)(∂F/∂R).   …(24.18)

Substituting (24.16):
  μ̇_{2t} = (δ μ_{1t} − μ_{1t} ∂F/∂k) ∂F/∂R + μ_{1t} (d/dt)(∂F/∂R)
        = δ · μ_{1t} ∂F/∂R − μ_{1t} ∂F/∂k · ∂F/∂R + μ_{1t} (d/dt)(∂F/∂R).

Setting equal to δ μ_{2t} (from 24.17) and using (24.15) to eliminate μ_{2t}:
  **(d/dt)(∂F/∂R) = (∂F/∂k)·(∂F/∂R)**   …(24.19)   ⭐

This is the **modified Hotelling rule with capital**: marginal product of resource grows at the rate of marginal product of capital (which equals interest rate r in equilibrium).

### Combine (1) with (24.16)
Differentiating (24.14): u''(c) ċ = μ̇_{1t}. Substituting (24.16):
  u''(c) ċ = δ u'(c) − u'(c) ∂F/∂k.

Define **relative risk aversion** η ≡ −u''(c) c / u'(c) (also = elasticity of marginal utility; its inverse = **Elasticity of Intertemporal Substitution (EIS) = 1/η**).

Rearranging:
  **ċ/c = (∂F/∂k − δ) / η**   …(24.20)   ⭐

This is the **Keynes–Ramsey rule** — a famous identity governing optimal consumption growth.

### Definitions
- **Relative risk aversion η = −u''(c) c / u'(c)** ⭐: elasticity of marginal utility; assumed constant in CRRA utility.
- **Elasticity of intertemporal substitution (EIS) = 1/η**: how willingly the agent substitutes consumption between periods.
- **Modified Hotelling rule** (with capital): (d/dt)(∂F/∂R) = (∂F/∂k)(∂F/∂R).
- **Keynes–Ramsey rule** ⭐⭐: ċ/c = (∂F/∂k − δ) / η — fundamental optimal-growth condition.

### Closed-form with Cobb-Douglas: F(k, R) = k^a R^b
Define x = k/R. Then ∂F/∂k = a x^{a−1} R^{a+b−1} and ∂F/∂R = b x^a R^{a+b−1}, so (24.19) reduces to:
  **ẋ = x^a**   …(24.22)

Integrating: **x(t) = [(1 − a) t + x_0^{1−a}]^{1/(1−a)}**   …(24.23)

For consumption (using 24.20):
  **c_t = c_0 e^{−δt/η} · [1 + (1 − a) t / x_0^{1−a}]^{a/η}**   …(24.24)

For depletion R, using R̄ = c/x and the identity x' = x R'/R + x'/R · ... (per the unit's algebra), in the special case **a = η**:
  **R(t) = R₀ exp[ −(δ/a) (e^{−δ t/a} − 1) · x_0 ]**   …(24.25)

(Otherwise R(t) is integrated numerically.)

### Boundary conditions
k(0) = k₀, k(T) = k_T given; S(0) = S₀, S(T) = 0 (terminal stock exhausted).

> **Quick Recall:**
> - Two states ⇒ two costates ⇒ two coupled FOCs.
> - Modified Hotelling: d/dt(F_R) = F_k · F_R.
> - Keynes-Ramsey: ċ/c = (F_k − δ)/η.
> - Cobb-Douglas closed form: x(t) = [(1−a)t + x_0^{1−a}]^{1/(1−a)}.

### Connections
- Builds on: discounted Hamiltonian (Chunk 006: Pontryagin's Necessary Conditions in Hamiltonian Form), Hotelling (Chunk 007: Worked Exercises Continued — Unit 23 Numerical Examples).
- Citations in source: Dasgupta & Heal (1974); Pearce (1975); Davison (1978).

---

## Section: CYP — Fishing Optimal Control 🟡

### Problem
ṗ_t = a + b p_t − x_t, with p_t = fish population, x_t = catch (a, b constants), discount r, V(.) = ∫₀^∞ e^{−rt} u(x_t) dt, u(x_t) = ln x_t (so c_t = x_t).

### (a) Transversality condition
For an infinite-horizon problem with positive (sign-restricted) p_t (fish biomass ≥ 0), the relevant transversality (current-value form) is:
  **lim_{t→∞} e^{−rt} μ_t · p_t = 0**.

If p_t is unrestricted, then **lim_{t→∞} e^{−rt} μ_t = 0**.

### (b) Optimal catch x_t* with u(x) = ln x
Current-value Hamiltonian: H̃ = ln x_t + μ_t (a + b p_t − x_t).
- ∂H̃/∂x = 1/x_t − μ_t = 0  ⇒  **x_t* = 1/μ_t**.
- Costate: μ̇_t = r μ_t − ∂H̃/∂p = r μ_t − b μ_t = (r − b) μ_t.
- Solving: μ_t = μ_0 · e^{(r − b) t}; hence **x_t* = (1/μ_0) e^{−(r−b) t} = x_0* e^{−(r−b) t}**.

So optimal catch declines (rises) over time according to whether r > b (r < b).

> **Quick Recall:** Fishing under log utility ⇒ x* grows at rate b − r (positive only if biology beats discount).

---

## Section: Neoclassical Investment Theory 🔴
<!-- Reason: foundational macro model relating Hamiltonian costate to Tobin's q -->

### Core Idea
A firm chooses investment I(t) and labour L(t) to maximise the present value of profit, subject to capital accumulation k̇ = I − δ k. The shadow price of capital μ_{1t} **equals q(t)** — the unit price of investment — and the FOC produces the classical "**marginal product of capital = required return**" condition r + δ = (1/q)(∂F/∂k · p − q̇) — the cost of capital.

### Setup
- Production function F(k, L): F(k, 0) = F(0, L) = 0 (essentiality), F_k > 0, F_L > 0, F_kk < 0, F_LL < 0, F_kL ≥ 0 (concavity).
- Often: constant returns to scale F(λk, λL) = λF(k, L).
- Profit: **R(t) = p(t) F(k(t), L(t)) − w(t) L(t) − q(t) I(t)**   …(24.26).
- Firm is a price-taker: p, w, q exogenous.

- Present value: **W = ∫₀^∞ e^{−rt} R(t) dt**   …(24.27)
- Capital evolution: **k̇ = I − δ k**   …(24.28).

### Current-value Hamiltonian
  **H̃ = p F(k, L) − w L − q I + μ_{1t} (I − δ k)**   …(24.29).

### Necessary conditions (with two controls L, I and one state k)

**(1) FOC for L:**
  ∂H̃/∂L = p ∂F/∂L − w = 0  ⇒  **w = p · ∂F/∂L**   …(24.30)
i.e., wage = value of marginal product of labour. (Dynamic version of static labour FOC.)

**(2) FOC for I:**
  ∂H̃/∂I = −q + μ_{1t} = 0  ⇒  **μ_{1t} = q(t)**   …(24.31)
**The shadow price of capital equals q (the unit cost of investment).**

**(3) Costate equation for k:**
  μ̇_{1t} = r μ_{1t} − ∂H̃/∂k = r μ_{1t} − p ∂F/∂k + μ_{1t} δ.   …(24.32)
Rearranging: μ̇_{1t} = (r + δ) μ_{1t} − p ∂F/∂k.

Substituting μ_{1t} = q (from 24.31):
  q̇ = (r + δ) q − p · ∂F/∂k
  ⇒  **p · ∂F/∂k = q (r + δ) − q̇**.   …(24.33)
Equivalently:  **∂F/∂k = (q (r + δ) − q̇) / p ≡ C / p**.

### Definitions
- **Implicit rental value of capital C** ⭐: C = q(r + δ) − q̇ — "user cost" of capital, also called Jorgenson's user cost.
- **Tobin's q-interpretation**: μ_{1t} = q is the marginal value of an additional unit of capital, equal to its unit purchase price.

> **In Simple Terms:** Hire labour until value-marginal-product equals the wage; invest until the value-marginal-product of capital equals its user cost (interest + depreciation, less capital-gain).

### ⚠️ Common Mistakes
- ❌ Forgetting the q̇ term in user cost. → ✅ Must subtract q̇ — capital gains lower the user cost.
- ❌ Using r alone as the discount rate. → ✅ The relevant return is **r + δ**, since capital also depreciates.

> **Quick Recall:**
> - p ∂F/∂L = w (wage = VMPL).
> - p ∂F/∂k = q (r + δ) − q̇ (Jorgenson user cost).
> - μ_{1} = q (shadow price of capital = unit price of investment).

### Connections
- Builds on: current-value Hamiltonian (Chunk 006: Pontryagin's Necessary Conditions in Hamiltonian Form); Cobb-Douglas marginal products (Chunk 008: Competitive vs. Monopoly Hotelling Path).
- Extended in: investment with adjustment costs / Tobin's q-theory (Chunk 009: Ramsey (Cass–Koopmans) Optimal-Growth Model).

### Open Questions
1. What if q itself depends on I (adjustment costs)? — Treated in §24.9 (Chunk 009: Ramsey (Cass–Koopmans) Optimal-Growth Model). Tobin's q-theory.
2. What if labour and capital are non-separable (e.g., putty-clay)? — Out of MEC-203 scope.

---

## Section: Optimal Growth (Ramsey) Model — Setup 🔴
<!-- Continues into Chunk 009 -->
<!-- Reason: foundational macro model — exam-critical -->

### Core Idea
The **Ramsey** (Cass–Koopmans) optimal-growth model treats the economy as a **representative agent** (firm + household) maximising the present value of intertemporal utility. The agent picks a consumption path c(t); the residual is invested in capital k(t). It is the canonical application of the Hamiltonian + Keynes–Ramsey rule developed in earlier sections.

### Setup (continued in Chunk 009)
- Output **y(t) = F(k_t, L_t)**.
- Wage **w(t)** = unit cost of labour. Capital cost **r(t)** = unit cost of borrowing.
- Capital depreciates at rate **δ ∈ (0, 1)**.
- Household has two income sources: wage from firm + interest on capital.
- Household consumes whatever is produced; the balance is invested back.
- Household buys output at price p_t.

(The full optimisation problem and its FOCs — leading to the Ramsey/Keynes–Ramsey rule — are in Chunk 009.)

### Connections
- Builds on: Keynes–Ramsey rule (Chunk 008 — derived implicitly in §24.6); current-value Hamiltonian (Chunk 006: Pontryagin's Necessary Conditions in Hamiltonian Form).
- Continued in: Chunk 009 (full Ramsey solution + Tobin's q with adjustment costs).


---


## Section: Ramsey (Cass–Koopmans) Optimal-Growth Model 🔴
<!-- Continues from Chunk 008 -->
<!-- Reason: keystone macro model — guaranteed exam topic -->

### Core Idea
The **Ramsey model** treats the economy as a representative agent (firm + household) who chooses a consumption path c(t) to maximise discounted lifetime utility subject to a capital-accumulation constraint. Unlike the Solow model (where saving is exogenous), Ramsey **derives** saving optimally from preferences. The result is the **Keynes–Ramsey rule** plus a balanced-growth steady state with closed-form expressions for k* and c* under Cobb-Douglas production and CEIS utility.

> **In Simple Terms:** Solow assumed people save a fixed fraction. Ramsey lets them choose: every period consumers ask "should I consume one more unit now or save it and consume more (with interest) later?". The trade-off generates the Keynes–Ramsey rule.

### Firm-side: profit maximisation
Profit (with output price p_t = 1, by super-neutrality of money assumption):
  π(t) = F(k_t, L_t) − w(t) L(t) − [r(t) + δ] k(t)   …(24.34)

FOCs:
- ∂π/∂L = ∂F/∂L − w(t) = 0  ⇒  **w(t) = ∂F/∂L**   …(24.35)
- ∂π/∂k = ∂F/∂k − [r(t) + δ] = 0  ⇒  **r(t) + δ = ∂F/∂k**   …(24.36)

Both factors are paid their marginal products in competitive equilibrium.

### Household: budget constraint and capital accumulation
Wealth dynamics from labour + capital income less consumption:
  K̇(t) = w(t) L(t) + r(t) k(t) − c(t),   K(0) given.   …(24.37)

In **per-capita (intensive) form** (L = 1 by normalisation, k = K/L, c = C/L, y = Y/L):
  k̇ = w(t) + r(t) k(t) − c(t),   k(0) given.   …(24.38)

### Cobb-Douglas case: F(k_t, L_t) = A k_t^a L_t^{1−a} ⇒ y(t) = A k_t^a
- ∂F/∂L = (1 − a) A k^a = w   …(24.39)
- ∂F/∂k = a A k^{a−1} = r + δ   …(24.40)

Substituting into (24.38):
  **k̇ = A k^a − c − δ k,   k(0) given**   …(24.41)

Net capital accumulation = gross investment (output less consumption) less depreciation. **(24.41) is the fundamental dynamic equation of the model.**

### Preferences — the CEIS / CRRA utility function
The standard utility:
  **u(c) = (c^{1−θ} − 1) / (1 − θ)**,    θ ∈ (0, ∞) \ {1}.   …(24.42)

- u' > 0, u'' < 0 (positive, diminishing marginal utility — Gossen's first law).
- **θ = relative risk aversion = −c · u''(c)/u'(c)** ⭐.
- **1/θ = elasticity of intertemporal substitution (EIS)** ⭐.
- **θ = 1 special case** (by L'Hôpital): **u(c) = ln c**   …(24.44).

### Definitions
- **CEIS / CRRA utility** ⭐: u(c) = (c^{1−θ} − 1)/(1 − θ); equivalently u(c) = ln c when θ = 1.
- **Coefficient of relative risk aversion (θ)** ⭐: −c·u''/u'; tells how the household ranks lotteries.
- **EIS = 1/θ** ⭐: how willingly the household shifts consumption between periods.

### The Ramsey problem
Maximise:
  U = ∫₀^∞ e^{−ρt} u(c(t)) dt   …(24.45),  ρ > 0 = rate of time preference.
Subject to: k̇ = A k^a − c − δ k, k(0) given.

c(t) is the **control**; k(t) is the **state**.

(Compared to Solow: Solow has exogenous savings; Ramsey **derives** saving optimally.)

### Current-value Hamiltonian
  **H̃ = u(c(t)) + λ_t [A k^a(t) − c(t) − δ k(t)]**   …(24.46)

### Necessary conditions
- **∂H̃/∂c = 0** ⇒ u'(c) − λ_t = 0  ⇒  **c_t^{−θ} = λ_t**   …(24.43)*
- **Costate**: λ̇_t = ρ λ_t − ∂H̃/∂k = λ_t (ρ + δ − a A k^{a−1})   …(24.44)*

### Keynes–Ramsey rule (consumption growth)
Differentiate u'(c) = λ w.r.t. t: u''(c) ċ = λ̇.
Substitute λ̇ from costate eq.:
  u''(c) ċ = (ρ + δ − a A k^{a−1}) u'(c)
  ⇒  −θ ċ/c = ρ + δ − a A k^{a−1}
  ⇒  **ċ/c = (1/θ) · [a A k^{a−1} − (ρ + δ)]**.   …(24.45)*

This is the **Keynes–Ramsey rule** ⭐⭐: consumption grows when the marginal product of capital exceeds (ρ + δ); EIS = 1/θ scales the response.

### Transversality condition
  **lim_{t→∞} λ_t e^{−ρ t} k(t) = 0**.

### Steady state (ċ = 0, k̇ = 0)
From ċ = 0: a A k^{a−1} = ρ + δ:
  **k* = [a A / (ρ + δ)]^{1/(1−a)}**   …(24.46)*

From k̇ = 0: c = A k^a − δk. Substituting k*:
  **c* = ((1 − a)/a) (ρ + δ) − δ · [a A / (ρ + δ)]^{1/(1−a)}**
        ⋮  (the unit's exact published form):
  **c* = [(a A / (ρ + δ))^{a/(1−a)}] · A − δ · [a A / (ρ + δ)]^{1/(1−a)}**

Steady-state income and savings:
  y* = A · (k*)^a = A · [a A / (ρ + δ)]^{a/(1−a)}   …(24.48)
  **s* y* = A k^{*a} − c* = δ k*** at steady state, i.e. saving exactly covers depreciation.   …(24.49)

### Comparative statics
- **Higher A** (productivity) ⇒ k* and c* increase proportionally.
- **Higher ρ** (impatience) ⇒ k* and c* decrease (less saving).
- **Higher δ** (depreciation) ⇒ k* decreases; effect on c* depends on parameters.

### ⚠️ Common Mistakes
- ❌ Confusing ρ (rate of time preference) with r (interest rate). → ✅ At steady state, r = aAk^{a−1} − δ = ρ; otherwise they differ.
- ❌ Treating saving rate as exogenous (Solow). → ✅ In Ramsey, saving rate is **derived** optimally; only the steady-state s* is constant.
- ❌ Forgetting transversality. → ✅ Without it, you can find spurious paths that diverge.

### Definitions
- **Rate of time preference ρ** ⭐: subjective impatience; ρ > 0.
- **Keynes–Ramsey rule** ⭐⭐: ċ/c = (1/θ)·[F'(k) − (ρ + δ)].
- **Modified golden rule**: at the steady state of the Ramsey model, F'(k*) = ρ + δ (vs. golden rule F'(k_g) = δ).
- **Optimal saving rate s**: at steady state, s* y* = δ k*; saving exactly replaces depreciation.

> **Quick Recall:**
> - Cobb-Douglas Ramsey: k̇ = A k^a − c − δ k.
> - Keynes-Ramsey: ċ/c = (1/θ)·[a A k^{a−1} − (ρ + δ)].
> - Steady state: k* = [aA/(ρ+δ)]^{1/(1−a)}, F'(k*) = ρ + δ.
> - Saving rate at SS: covers depreciation only (s* y* = δ k*).
> - Welfare theorem: Ramsey saving rate is optimal — anything else lowers utility.

### Connections
- Builds on: current-value Hamiltonian (Chunk 006: Pontryagin's Necessary Conditions in Hamiltonian Form), discounting (Chunk 007: Worked Exercises Continued — Unit 23 Numerical Examples), Cobb-Douglas marginal products (Chunk 008: Competitive vs. Monopoly Hotelling Path).
- Welfare implication: dynamic inefficiency (over-saving) of the Solow model is ruled out.
- Used in: MEC-102 macroeconomics (the source explicitly notes this preview).

### Open Questions
1. With non-constant population growth n: replace ρ with ρ + n in the FOCs (Cass–Koopmans extension).
2. With endogenous labour supply: control vector (c, L) — bigger system but same logic.

---

## Section: Neoclassical Investment with Adjustment Costs (Tobin's q-theory) 🔴
<!-- Reason: macro / corporate finance link; Tobin's q is named theorem -->

### Core Idea
The basic neoclassical model (Chunk 008: Competitive vs. Monopoly Hotelling Path) has investment respond instantaneously to differences between marginal product and user cost — unrealistic. **Adjustment costs** (Eisner–Strotz 1963) introduce a convex cost G(I, k) to investment, so capital adjusts only **gradually**. The shadow price of capital μ(t) becomes **Tobin's marginal q**, and the optimal investment function depends on q.

> **In Simple Terms:** Real firms can't add capital costlessly: there are installation, retraining, and reorganisation costs. Convex G(·) makes "doubling investment more than doubles cost", so the firm spreads investment over time. The shadow price μ tracks how *valuable* installed capital is — Tobin's q.

### Setup
  Max V = ∫₀^∞ e^{−rt} R(t) dt   …(24.50)
  with R(t) = p F(k(t), L(t)) − G(I(t), k(t)) − w(t) L(t) − p^k I   …(24.51)

- p^k = relative price of capital,
- G(I, k) = convex adjustment-cost function: ∂G/∂I > 0, ∂²G/∂I² > 0, ∂G/∂k < 0, G(0, k) = 0.
- I_max < ∞, I_min ≥ 0, δ > 0, r > 0.

State equation:
  **k̇ = I(t) − δ k(t)**   …(24.52)

### Current-value Hamiltonian
  **H̃ = p F(k, L) − G(I, k) − w L − p^k I + μ_t · (I − δ k)**   …(24.52a)

### Necessary conditions

**(1) FOC for L:** ∂H̃/∂L = 0  ⇒  p · ∂F/∂L = w  ⇒  **∂F/∂L = w/p**   …(24.53)

**(2) FOC for I:** ∂H̃/∂I = 0  ⇒  −∂G/∂I − p^k + μ_t = 0
  ⇒  **μ_t = p^k + ∂G/∂I**   …(24.54)
The shadow value of capital equals the price of investment + marginal adjustment cost.

**(3) Costate equation:**
  μ̇_t = (r + δ) μ_t − p · ∂F/∂k + ∂G/∂k.   …(24.55)

Using (24.54) to substitute for μ:
  μ̇_t = (r + δ)(p^k + ∂G/∂I) − p · ∂F/∂k + ∂G/∂k.   …(24.56)

### Tobin's marginal q interpretation
- **μ_t = q(t) · p^k**: μ is the marginal value of installed capital — the present value of the additional net revenue from one extra unit of capital.
- **Tobin's marginal q ≡ μ_t / p^k**: ratio of shadow price of capital to its purchase price.
- q > 1 ⇒ install more capital; q < 1 ⇒ disinvest; q = 1 in steady state.

### Investment function
Inverting (24.54): **I = ψ(μ_t, k)** with ∂ψ/∂μ > 0, ∂ψ/∂k > 0   …(24.59).
The firm invests **more** when μ rises (i.e., when Tobin's q is high), and more when k is large (CRS production).

### Steady state (μ̇ = 0, k̇ = 0)
- k̇ = 0 ⇒ **I = δ k**   …(24.57)
- μ̇ = 0 ⇒ **μ* = ((r + δ) p^k + ∂G/∂k − ∂G/∂I·(r+δ)) / [F'(k) terms]**, but more simply: μ* = [p · ∂F/∂k − ∂G/∂k] / (r + δ).   …(24.58)

### Properties of the Optimal Path
1. **μ_t > 0 always** (since p^k, δ > 0).
2. **μ̇ vs k**: With CRS, ∂F/∂k is constant in k, so the μ̇ = 0 locus is downward-sloping in (k, μ) space.
3. **k̇ = 0 locus**: I = δk; with adjustment costs, this gives an upward-sloping locus.
4. **Saddle-path stable**: the (k*, μ*) intersection is a saddle point; the optimal trajectory is the stable manifold (descends if k > k*, ascends if k < k*).
5. **Negative interest-rate elasticity of investment**: ∂I/∂r < 0 — a standard neoclassical property. Lower r raises μ_t, raising I and accelerating convergence to k*.

### What if there were no adjustment costs?
If G ≡ 0 in (24.52a), the model collapses to Jorgenson's neoclassical investment model (Chunk 008, eq. 24.33): p · ∂F/∂k = q (r + δ) − q̇.

### ⚠️ Common Mistakes
- ❌ Equating Tobin's q with the **average** q (V/k). → ✅ The model speaks of **marginal q** = μ/p^k. They coincide only under linear-homogeneous F and G (Hayashi 1982).
- ❌ Treating G as concave. → ✅ G must be **convex** for smooth gradual adjustment; a concave G gives lumpy investment (different model, "non-convex adjustment costs").

> **Quick Recall:**
> - State: k̇ = I − δk.
> - FOC for I: μ = p^k + G_I (purchase price + marginal adjustment cost).
> - Tobin's marginal q = μ/p^k; q > 1 ⇒ invest; q < 1 ⇒ divest.
> - Costate: μ̇ = (r + δ) μ − p F_k + G_k.
> - Steady state: I = δk, F_k = (r + δ)·μ*/p − G_k/p.

### Connections
- Builds on: neoclassical investment without adjustment (Chunk 008, §24.7).
- Generalises to: real-options / irreversible investment (out of MEC-203 scope).
- Empirical link: Tobin's q regressions in macro / asset-pricing.

---

## Section: CYP 2 (§24.12) — Worked: Investment with Adjustment Cost ψ 🟡

### Problem
Competitive firm with Y(t) = A F(k(t)). Output and capital prices both = 1. I(t) = k̇(t) + δ k(t). Instantaneous cost of investment = I(t) + ψ(I(t)) where ψ is convex with ψ(0) = 0, ψ' > 0, ψ'' > 0. Discount rate r.

### Hamiltonian
  H̃ = A F(k(t)) − I(t) − ψ(I(t)) + λ(t)[I(t) − δ k(t)].

### Necessary conditions
- **∂H̃/∂I = 0**: −1 − ψ'(I(t)) + λ(t) = 0  ⇒  **λ(t) = 1 + ψ'(I(t))**   …(24.57)*
  *Marginal value of an extra unit of capital = purchase price (1) + marginal adjustment cost.*
- **Costate**: λ̇(t) = (r + δ) λ(t) − A F'(k(t))
  ⇒  **(r + δ) λ(t) − λ̇(t) = A F'(k(t))**   …(24.58)*
  *User cost of capital = (real interest + depreciation rate − expected appreciation of shadow value) × λ. At optimum, this equals the marginal product of capital.*

### Economic interpretation
- (24.57): Marginal q = 1 + ψ'. The firm invests until the shadow value of capital equals the marginal cost of investment.
- (24.58): At the optimum, user cost = MPK. User cost = (interest + depreciation − capital-gain rate) · shadow price of capital.

> **Quick Recall:** Adjustment-cost FOC ↔ Tobin's q; user-cost FOC ↔ neoclassical hurdle rate.

---

## Section: Unit 24 Summary, Key Words & Exercises 🟢

### Summary (§24.10)
- The core of dynamic economic analysis is to bring every variable to its **present value**, then optimise.
- Three environmental-economics applications cover monopoly extraction, renewable resources, and non-renewable depletion.
- **Number of costate variables ≡ number of state equations** (always).
- Detailed Ramsey derivation provided as a stepping-stone to MEC-102.
- Adjustment-cost theory generalises Jorgenson's neoclassical investment; removing the adjustment cost recovers §24.7.

### Key Words (§24.11)
- **Cost per unit investment**: aggregate cost per unit investment incurred by the firm; may include adjustment cost.
- **Logistic growth function**: g(x) = γ x (1 − x/k); flattened S-curve; saturates at carrying capacity k.
- **Monopoly**: firm with exclusive control of an activity.
- **Non-renewable resources**: deplete with extraction (oil, coal).
- **Optimal saving rate (Ramsey model)**: steady-state saving rate when consumption is optimised.
- **Renewable resources**: regenerate biologically (fish, trees).
- **Transversality condition** ⭐: lim_{t→∞} λ_t · x_t = 0 (or current-value form lim e^{−ρt} μ_t x_t = 0); necessary for infinite-horizon problems.

### Selected Exercises (§24.13)
- **Q1**: Profit-maximisation conditions in Ramsey → see §24.8 (above).
- **Q2**: Explain CEIS utility → see §24.8 (above).
- **Q3**: Derive optimal saving rate (Ramsey) → see §24.8 (steady-state s* covers δk*).
- **Q4**: Why convex adjustment cost? → **convex ⇒ unique local-=-global minimum ⇒ unique convergence of dynamic optimisation**. Concave gives lumpy investment.

### Connections
- Block 7 culminates here. Threads run forward into MEC-102 (Macroeconomics — Solow vs. Ramsey, Cass–Koopmans, q-theory) and MEC-107 (International Trade — dynamic models of capital accumulation across countries).


---


## Section: End of Block 7 🟢

### Core Idea
Page 91 is a blank end-of-block page (just the printed folio "90"). No content to extract. Block 7 of the MEC-203 PDF ends here — the next page in the printed volume is the start of Block 8 (Probability), which is in a separate PDF.

> **In Simple Terms:** Block 7 is complete. Move on to Block 8 for Probability and Probability Distributions, or back to Unit 24 (Chunk 009: Ramsey (Cass–Koopmans) Optimal-Growth Model) for the final substantive content.

### Connections
- **End of Block 7**: All three units (22 Intertemporal Optimisation-I, 23 Intertemporal Optimisation-II, 24 Economic Applications of Dynamic Optimisation) are now covered.
- **Next**: Block 8 — Probability Theory and Probability Distributions (separate PDF in the MEC203 Quant folder).


---

