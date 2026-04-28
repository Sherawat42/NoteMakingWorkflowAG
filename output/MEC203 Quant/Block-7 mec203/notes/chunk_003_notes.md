# Chunk 003 — Unit 22: Special cases of E–L, Legendre, Isoperimetric, Free-end, Discrete DP
<!-- Pages: 21-30 -->
<!-- Source: chunk_003.txt + page images -->

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
- Builds on: Euler–Lagrange theorem (Chunk 002).

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
- Builds on: integration-by-parts step in the E–L derivation (Chunk 002).
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
