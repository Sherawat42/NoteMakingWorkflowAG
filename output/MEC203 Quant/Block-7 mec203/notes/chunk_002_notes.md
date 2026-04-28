# Chunk 002 — Unit 22: Intertemporal Optimisation-I (Setup, Calculus of Variations, Euler–Lagrange)
<!-- Pages: 11-20 -->
<!-- Source: chunk_002.txt + page images -->

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
