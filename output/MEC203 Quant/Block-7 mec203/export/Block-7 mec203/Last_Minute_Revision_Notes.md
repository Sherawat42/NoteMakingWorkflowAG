# Last Minute Revision Notes

> *This document contains ONLY ultra-high-yield definitions (⭐), Quick Recall facts, Common Mistakes, and core bullet points.*


## Topics

| Unit | Title | Page (Vol. 3) | Focus |
|------|-------|---------------|-------|
| 22 | Intertemporal Optimisation-I | 11 | Calculus of Variations + intro to dynamic programming |
| 23 | Intertemporal Optimisation-II | 39 | Optimal control / Pontryagin's maximum principle |
| 24 | Economic Applications of Dynamic Optimisation | 66 | Ramsey, optimal investment, Hotelling, etc. |
- **Dynamic Optimisation**: optimisation in which the decision variables are **time-variant** (change over time), in contrast to static optimisation where they are fixed at one instant. ⭐ (exam-important)

**Quick Recall:**
- Block 7 = Dynamic Optimisation = 3 units (22, 23, 24)
- Two main approaches: (i) Calculus of Variations / Pontryagin's Maximum Principle (continuous), (ii) Bellman's Dynamic Programming (recursive / discrete)
- **f : X → Y** — function with domain X and codomain Y. ⭐
- **∂f/∂xᵢ** — partial derivative; **∂²f/∂xᵢ ∂xⱼ** — second partial. ⭐
- **H(x₁, x₂)** — **Hessian** matrix (symmetric matrix of second partials). ⭐
- **t = 0, 1, 2, …** — time as discrete variable; **t ∈ [0, +∞)** — time as continuous variable. ⭐ (Block 7 will hinge on this distinction.)
- **∇f, grad f** — gradient of f, ∇f = (∂f/∂x₁, …, ∂f/∂xₙ). ⭐

**Quick Recall:**
- Continuous time: t ∈ [0, ∞); discrete time: t = 0, 1, 2, …
- Hessian = symmetric matrix of second partials → used for second-order conditions
- ‖x‖ Euclidean = √Σxᵢ² ; sup-norm = max|xᵢ|
| Method | Originator | Style | Better for |
|--------|-----------|-------|-----------|
| Calculus of Variations / Pontryagin's Maximum Principle | Bernoulli, Euler, Lagrange; Pontryagin | Continuous, classical | Continuous-time problems with smooth functionals |
| Dynamic Programming (Bellman's principle) | Richard Bellman | Recursive (sub-game-perfect-style) | Discrete-time, sequential-decision problems |
- **Dynamic optimisation problem**: an optimisation problem in which variables of the model are time-variant. ⭐
- **Static vs. dynamic**: in static, variables are fixed at one instant; in dynamic, time is itself an independent variable (often *the* independent variable). ⭐

**Quick Recall:**
- Block 7 only covers *deterministic* dynamic optimisation.
- Two main toolkits: Calculus of Variations / Optimal Control (continuous), Dynamic Programming (discrete).

### Function vs. Functional 🔴

**Worked illustration — set of functions on [0, b]**
- g(x) = x  (a straight line)
- h(x) = +√(b² − x²)  (upper half of a circle of radius b)
- k(x) = x²  (a parabola)
1. F_length, b (g) = ∫₀ᵇ √(1² + 1) dx = √2 · b
2. F_length, b (h) = (1/4) × circumference of circle of radius b = (πb)/2
3. F_length, b (k) = ∫₀ᵇ √(1 + (2x)²) dx  (closed-form using a hyperbolic substitution)
1. F_area, b (g) = (1/2) b²
2. F_area, b (h) = (1/4) π b²
3. F_area, b (k) = ∫₀ᵇ x² dx = b³/3
- **Functional**: a function whose **input** is itself a function and whose output is a real number. ⭐ (exam-important)
- **Function f : X → Y**: a rule associating to each x ∈ X a unique y ∈ Y.

**Quick Recall:**
- Function: number → number
- Functional: whole function → number
- Calculus of Variations = "calculus on functionals"
- **C^k (differentiability class k)**: f is of class C^k on open U ⊂ ℝ if f, f', f'', …, f^(k) all exist and are continuous on U. ⭐

**Quick Recall:**

**Quick Recall:**
- Continuous: Max ∫ V(x, x', t) dt, with end-point conditions on x.
- Discrete: Max Σ βᵗ u(C_t), with state-equation W_{t+1} = W_t − C_t.

### Theorem for Optimality — The Euler–Lagrange Equation 🔴
- ∂V/∂x(t)  −  d/dt (∂V/∂x'(t))  =  0       …(22.4)   ⭐⭐
1. Suppose x*(t) is the extremal path; let x_a(t) = x*(t) + δx(t) be a nearby admissible "varied" path with ‖δx‖ → 0. Because endpoints are fixed:  δx(t₀) = 0, δx(t_f) = 0.
2. Expand J(x_a) by Taylor series about x*: J(x_a) = J(x*) + ΔJ, where ΔJ ≈ δJ + δ²J (first and second variations).
3. **First variation** (necessary condition δJ = 0):
4. Apply **integration by parts** to the second term (using d(UV) = U dV + V dU):
5. Substitute back:
6. Apply the **Fundamental Lemma** (below): since this must hold for every admissible δx(t), the bracket must vanish identically:
- **Extremal path / extremal**: a function x*(t) that satisfies the Euler–Lagrange equation. ⭐
- **First variation δJ**: the linear-in-δx part of ΔJ; necessary condition is δJ = 0.
- **Second variation δ²J**: quadratic-in-δx part; sufficient sign-conditions: δ²J > 0 ⇒ minimum, δ²J < 0 ⇒ maximum.

### ⚠️ Common Mistakes
- ❌ Treating the Euler–Lagrange equation as a partial differential equation. → ✅ It is an **ordinary** differential equation in t (generally **second-order, nonlinear**).
- ❌ Assuming the boundary term automatically vanishes. → ✅ It vanishes only because endpoints are fixed; with free endpoints you instead get a **transversality condition** (see §22.9).
- ❌ Reading the equation as ∂V/∂x − ∂V/∂x' = 0. → ✅ The second term has a *total time derivative* d/dt outside the partial: d/dt (∂V/∂x'), **not** just ∂V/∂x'.
- For x(t) scalar: one second-order ODE (so two integration constants C₁, C₂, pinned down by the two boundary conditions).
- For x(t) an n×1 vector: the equation becomes a system of **n** second-order ODEs (2n integration constants ⇒ 2n boundary conditions).
- The equation in general is **nonlinear and time-varying**.

**Quick Recall:**
- Necessary 1st-order condition: ∂V/∂x − d/dt (∂V/∂x') = 0.
- It's an ODE; order = 2 per state variable.
- Boundary conditions: x(t₀) = x₀, x(t_f) = x_f (fixed-endpoint problem).
- Sufficient: 2nd variation δ²J > 0 (min) or δ²J < 0 (max).
- Builds on: **integration by parts** (Block 3 calculus), **Taylor expansion** (Block 3), Fundamental Lemma (this section).
- Prerequisite for: special cases of Euler–Lagrange (§22.4), Legendre condition (§22.6), free-end problems & transversality (§22.9), all of Unit 23 (Optimal Control), Unit 24 (Economic Applications).
1. What if V is non-smooth (only C¹)? — The classical Euler–Lagrange derivation breaks down; weak/distributional formulations are needed (out of MEC-203 scope).
2. How does the equation change when endpoints are free? — Resolved by **transversality conditions** in §22.9.

### ⚠️ Common Mistakes
- ❌ Skipping the E–L check and jumping to second-order conditions. → ✅ E–L must be satisfied first; second-order conditions only classify between max/min once an extremal is found.
---

**Quick Recall:**

### Euler Equation in Special Cases 🔴

**Quick Recall:**
- No x: ∂V/∂x' = const (first-order ODE)
- No t: H = x'·(∂V/∂x') − V = const (first-order ODE)
- Both special cases give **first integrals** that lower the order of the E–L equation by one.
- Builds on: Euler–Lagrange theorem (Chunk 002).

### Second-Order Condition for Optimality 🔴
- A is **positive definite at x*** ⇒ J is **minimised** at x*.
- A is **negative definite at x*** ⇒ J is **maximised** at x*.
- **Positive definite** matrix M: xᵀ M x > 0 for every non-zero column vector x.
- **Negative definite** matrix M: xᵀ M x < 0 for every non-zero column vector x.

**Quick Recall:**
- Necessary: E–L (∂V/∂x − d/dt(∂V/∂x') = 0).
- Sufficient (min): A is positive definite at x*.
- Sufficient (max): A is negative definite at x*.

### Legendre Condition 🔴
- If V is **concave** in (x, x'), then any path satisfying the E–L equation **maximises** J.
- If V is **convex** in (x, x'), then any path satisfying the E–L equation **minimises** J.

**Quick Recall:**
- Legendre necessary: max needs ∂²V/∂(x')² ≤ 0; min needs ≥ 0.
- Legendre sufficient: V concave (convex) in (x, x') ⇒ E–L gives max (min).

### Necessary & Sufficient Conditions Together 🔴
- A positive definite at x* ⇒ x* is the **minimiser**.
- A negative definite at x* ⇒ x* is the **maximiser**.

**Quick Recall:**

### Isoperimetric Problem 🔴
1. Integral constraint  ∫ F(x*, x*', t) dt = B
2. x(t₀) = x₀
3. x(t_f) = x_f
1. Form S = V − λF.
2. Solve E–L for S to obtain x*(t; λ, C₁, C₂).
3. Plug into the integral constraint and the two boundary conditions.
4. Solve the three simultaneous equations for λ, C₁, C₂.

**Quick Recall:**

### Free-End-Value Problems & Transversality Condition 🔴
| Case | What is free | Conditions to solve |
|------|--------------|---------------------|
| I  | Both t_f and x(t_f) free | E–L (22.25), [V − x'·∂V/∂x']_{t_f} = 0 (22.26), [∂V/∂x']_{t_f} = 0 (22.27) |
| II  | t_f fixed, x(t_f) free  | E–L (22.25) and [∂V/∂x']_{t_f} = 0 (22.27) |
| III | t_f free, x(t_f) fixed  | E–L (22.25) and [V − x'·∂V/∂x']_{t_f} = 0 (22.26) |
| IV  | Endpoint B lies on curve x = g(t) | E–L (22.25) and [V + (∂V/∂x')(g'(t) − x'(t))]_{t_f} = 0 (22.28) |

**Quick Recall:**
- Fixed both ends: just E–L.
- x_f free: add ∂V/∂x' |_{t_f} = 0.
- t_f free: add V − x'·∂V/∂x' |_{t_f} = 0.
- Endpoint on a curve g(t): add the curve-tangency transversality (22.28).
- Builds on: integration-by-parts step in the E–L derivation (Chunk 002).
- Prerequisite for: optimal-control transversality conditions in Unit 23, infinite-horizon transversality in Unit 24.

### Discrete-Time Dynamic Optimisation — Setup 🔴
- **Timing**: state x_t is a *stock* measured at the **start** of period t; control U_t is a *flow* measured at the **end** of period t.
- **Horizon**: T can be finite or infinite (T = ∞ is the more common case).
- **Objective**: intertemporal utility is **additively separable, stationary, time-discounted**:
- **State equation** (autonomous): x_{t+1} = g(x_t, U_t), with g continuous, differentiable, concave (so a unique solution exists).
- **No-Ponzi-game condition**: lim_{t→∞} βᵗ x_t = 0, with 0 < β < 1.
- **Side conditions** like x_t ≥ 0, U_t > 0 may exist; the unit treats only **interior** solutions (or open domains).
- **State variable x_t** ⭐: *stock* describing the system at the start of period t (e.g., capital).
- **Control variable U_t** ⭐: *flow* chosen by the decision maker at period t (e.g., consumption).
- **Discount factor β** ⭐: 0 < β < 1; models impatience. Subjective discount rate ρ satisfies β = 1/(1+ρ).
- **No-Ponzi-game condition**: lim_{t→∞} βᵗ x_t = 0; rules out exploding state paths bankrolled by ever-growing borrowing.

**Quick Recall:**
- State = stock (start of period); Control = flow (end of period).
- Objective: Σ βᵗ f(x_t, U_t); state law x_{t+1} = g(x_t, U_t).
- 0 < β < 1; no-Ponzi: lim βᵗ x_t = 0.

### Dynamic Programming & the Bellman Equation 🔴
- **Value function V_T−t (x_t)** ⭐: the maximised intertemporal utility starting at period t with state x_t and remaining horizon T − t periods:

**Derivation (heuristic)**

### ⚠️ Common Mistakes
- ❌ Treating the value function as differentiable. → ✅ Continuity is generally guaranteed; differentiability is **not** (Stokey & Lucas 1989). Differentiability requires extra regularity.
- ❌ Confusing dynamic programming with dynamic optimisation. → ✅ DP is *one* method; calculus of variations and optimal control are others.

**Quick Recall:**
- Bellman: V_T(x) = max_U {f(x, U) + β V_{T−1}(g(x, U))}.
- Infinite horizon: V(x) = max_U {f(x, U) + β V(g(x, U))}.
- Policy function: U* = h(x). Solved numerically by value-function iteration.
- Builds on: state/control distinction (this chunk), discount factor concept (this chunk).
- Equivalent first-order condition in continuous time = Pontryagin's maximum principle (Unit 23).
- Application: Cake-Eating Problem solved via Bellman equation in next chunk.
1. When is the value function differentiable? — see Stokey & Lucas (1989), Benveniste–Scheinkman theorem (out of MEC-203 scope).
2. How fast does value-function iteration converge? — geometric, with ratio β.

### The Cake-Eating Problem — Worked Solution via the Bellman Equation 🔴
1. **Set up the Bellman equation** (above).
2. **Guess** the form of the value function:  V(W_t) = C₁ + C₂ ln(W_t).
3. **Take the FOC** of the RHS w.r.t. W_{t+1} and solve for the optimal W_{t+1}*.
4. **Match the guess** to the Bellman equation evaluated at W_{t+1}*.
5. **Identify the unknown coefficients** C₁ and C₂ by equating constant terms and the coefficient of ln(W_t).
6. **Recover the policy function** for W_{t+1} (and hence the optimal consumption C_t*).
- **Policy function**: a feedback rule mapping the current state to the optimal current control (here, U* = (1 − β) W_t).
- **Guess-and-verify**: a standard method for closed-form solutions of Bellman equations — guess the functional form of V, verify that the FOCs are consistent with the guess.

### ⚠️ Common Mistakes
- ❌ Forgetting that the constant term C₁ is also pinned down by matching; ignoring it leaves the value function ill-defined.
- ❌ Treating C_0 as well-defined: the muncher only starts eating at t = 1 (so C₀ = 0 in the timing convention adopted in the unit).

**Quick Recall:**
- Cake-eating with log utility ⇒ policy g(W) = β W.
- Optimal consumption ⇒ C_t* = (1 − β) W_t.
- V(W) = C₁ + C₂ ln W with C₂ = 1/(1 − β).
- Standard method: guess-and-verify on the Bellman equation.
- Builds on: Bellman equation (Chunk 003), discounted utility (Chunk 003).
- Generalises to: Ramsey/CASS–KOOPMANS optimal-growth model (Unit 24, with concave production replacing the cake constraint).
1. What if utility is CRRA u(C) = C^(1−σ)/(1−σ) instead of log? — The policy is still linear in W (W_{t+1}* = (β R)^(1/σ) W_t / [1 + (β R)^(1/σ)] for return R), but the algebra is messier.
- **Bellman equation** ⭐: V(x) = max_u { f(x, u) + β V(g(x, u)) }.

### Worked Exercises — Selected Solutions (§22.13–22.14) 🔴
- *Particular integral:* try y_p = B t eᵗ. Differentiating twice gives y_p'' = B(t eᵗ + 2eᵗ). Substituting: B t eᵗ + 2B eᵗ − B t eᵗ = 2eᵗ ⇒ 2B = 2 ⇒ B = 1, so y_p = t eᵗ.
- *Complementary function:* try y_c = A e^{rt}. The auxiliary equation r² − 1 = 0 ⇒ r = ±1, so y_c = A₁ eᵗ + A₂ e^{−t}.
- *Boundary conditions:* y(0) = A₁ + A₂ = 0 ⇒ A₂ = −A₁. y(1) = A₁ e + A₂ e^{−1} + e = 1 (with the y_p contribution at t = 1 being e). Solve for A₁ = (1 − e)/(e − e^{−1}). The final answer (textbook):  **y(t) = [(1 − e)/(1 − e²)]·(eᵗ − e^{−t}) + t·eᵗ**.
- ∂V/∂x = −2 x' + 10t.
- ∂V/∂x' = 2 x' − 2 x ⇒ d/dt(∂V/∂x') = 2 x'' − 2 x'.
- E–L: −2 x' + 10t − 2 x'' + 2 x' = 0 ⇒ **2 x'' = 10t** ⇒ x'' = 5t.
- Integrating: x'(t) = (5/2) t² + C₁; x(t) = (5/6) t³ + C₁ t + C₂.
- BCs: x(0) = 0 ⇒ C₂ = 0. x(1) = 2 ⇒ 5/6 + C₁ = 2 ⇒ C₁ = 7/6.
- **x*(t) = (5/6) t³ + (7/6) t**. (The unit's published answer: x*(t) = (5/6) t³ + (1/6) t — note the discrepancy; the OCR'd source shows "5/6 t³ + 1/6 t". When in doubt re-derive.)
- BC x(0) = 1 ⇒ C₂ = 1.
- BC x(1) = 2 ⇒ −λ/4 + C₁ + 1 = 2 ⇒ C₁ = 1 + λ/4.
- Integral constraint ∫₀¹ x(t) dt = K:
- z₁ = 2 + √3 ≈ 3.732 ⇒ t_{f,1} ≈ 1.932; corresponding C₁ ≈ −1.117 ⇒ **x*(t) = t³ − 1.117 t**.
- z₂ = 2 − √3 ≈ 0.2679 ⇒ t_{f,2} ≈ 0.6446; corresponding C₁ ≈ 2.6871 ⇒ **x*(t) = t³ + 2.6871 t**.

**Quick Recall:**
- Step 1: write E–L (or augmented E–L for isoperimetric).
- Step 2: integrate twice (or solve ODE).
- Step 3: use BCs (and integral constraint / transversality) to pin down constants.
- Step 4: verify with Legendre / second-order condition.

**Quick Recall:**
- Unit 22 = unconstrained calculus of variations + intro to DP.
- Unit 23 = constrained dynamic optimisation via Hamiltonians (continuous-time optimal control).

### ⚠️ Common Mistakes
- ❌ Confusing "value of choice variable that maximises objective" with "maximum value of the choice variable".
---

### The Concept of STATE — and State-Space Representation 🔴
1. SV is a **minimal independent** subset (no redundancy: e.g., if z = 3y₁ + 4y₂ then z is not in SV).
2. The output map: SV × IP → OP is **well-defined** (a function): output(s_i, j) ∈ OP is unique for each (s_i, j).
3. The next-state map: SV × IP → SV is **well-defined**: next-state(s_i, j) is unique.
4. **Persistence**: the state remains unchanged unless an external input is received (internal variables may evolve, but state values change only at input instants).
- **State variable** ⭐: minimal independent internal variable summarising progress; uniquely determines (with input) the next state and output.
- **Internal variable**: appears neither in the input nor the output of the system.
- **State-space representation**: model of a dynamic system as a set of (input, output, state) variables related by **first-order** differential or difference equations.

**Quick Recall:**
- State = minimal sufficient summary of history.
- Always involves *first-order* (no second-derivative) ODEs.
- State variable + input → uniquely determines next state and output.
- Builds on: state-vs-control distinction (this section); discrete-time state x_t (Chunk 003).
- Prerequisite for: optimal control formulation in §23.2 (this chunk).

**Quick Recall:**

### Optimal Control Theory — Setup & Differences from CoV 🔴
| Aspect | Calculus of Variations | Optimal Control |
|--------|------------------------|-----------------|
| Rate of change y'(t) | Determined endogenously by E–L from y(t) | Driven by external control: y'(t) = f(t, y, u) |
| Choice variable | Path y(·) of the state | Path u(·) of the control |
| Functional argument | V(y) — emphasis on internal state | V(u) — emphasis on external control |
| Constraint type | Boundary conditions only | Boundary + state equation (dynamic constraint) |
- **Control variable u(t)** ⭐: external variable chosen by the decision-maker that influences the rate of change of the state.
- **State equation / equation of motion**: y'(t) = f(t, y, u) — the constraint linking state to control.
- **Bolza problem** ⭐: an optimal-control problem with both an *integral* (running) cost and a *terminal* cost (cost at the final time).
- Objective: V(u) → **J(u)**
- State variable: y(t) → **x(t)**
- Time derivative: y'(t) → **ẋ(t)**
- Initial / final times: 0, T → **t₀, t_f**

**Quick Recall:**
- CoV: optimise V[y]; E–L equation only.
- Optimal Control: optimise J[u]; state equation + Hamiltonian conditions.

### Necessary Conditions — Derivation of the Hamiltonian 🔴
- **H(x, u, λ, t) = V(x, u, t) + λ(t) f(x, u, t)**   …(23.9)   ⭐⭐
- **Costate variable λ(t)**: the time-varying Lagrange multiplier on the state equation. Economic interpretation: **marginal valuation of the state at time t** (shadow price of the state) ⭐.
- **Hamiltonian H = V + λ f**: bundles the running cost and the constraint shadow-price.
- The optimality conditions (Pontryagin's Maximum Principle) follow from setting δJ̃ = 0 — this gives:
  - State equation: ẋ = ∂H/∂λ.
  - Costate equation: λ̇ = −∂H/∂x.
  - Optimality of u: ∂H/∂u = 0   (interior; otherwise H is maximised over u).
- These are derived in detail in the next chunk.
- **Hamiltonian H(x, u, λ, t) = V(x, u, t) + λ(t) f(x, u, t)** ⭐⭐. Sums running cost and shadow value of the state's evolution.
- **Costate / adjoint variable λ(t)** ⭐: Lagrange multiplier on the state equation; equals the marginal value of the state at time t.
- **Bolza problem**: problem with both integral and terminal cost.

### ⚠️ Common Mistakes
- ❌ Treating λ as a constant. → ✅ λ = λ(t) is *time-varying*; it has its own ODE (the costate equation).
- ❌ Confusing H with the Lagrangian Λ. → ✅ H groups only V + λ f; Λ adds the terminal-cost gradient and a −λẋ term.
- ❌ Setting up H without state-equation adjoining. → ✅ The whole point of H is that it bakes the constraint ẋ = f into the optimality conditions.

**Quick Recall:**
- **H = V + λ f**.
- λ(t) = shadow price / marginal valuation of state x at time t.
- Pontryagin's conditions: ẋ = ∂H/∂λ;  λ̇ = −∂H/∂x;  ∂H/∂u = 0 (or H maximised in u).
- Bolza = integral cost + terminal cost.
- Builds on: Lagrange multipliers (Block 5), Euler–Lagrange equation (Chunk 002).
- Prerequisite for: full Pontryagin's principle (Chunk 006), discounted current-value Hamiltonian (Chunk 006), economic applications (Unit 24, Chunks 7–9).
1. What if u is constrained to a non-open control set U? — Then ∂H/∂u = 0 is replaced by **maximisation of H over u ∈ U** (Pontryagin's Maximum Principle in its full form).
2. What if the state path can hit a constraint? — Constrained-state problems require additional KKT-style multipliers (out of MEC-203 scope).

### Pontryagin's Necessary Conditions in Hamiltonian Form 🔴
| Condition | Equation | Source eq # |
|-----------|----------|-------------|
| **Optimality of control** (interior) | ∂H/∂u = 0 | 23.21 |
| **State equation** | ∂H/∂λ = ẋ(t) | 23.25 |
| **Costate equation** | ∂H/∂x = −λ̇(t) | 23.23 |
|-----------|----------|-------------|
| Optimality | (∂H/∂u)ᵀ = 0_m | 23.22 |
| State | (∂H/∂λ)ᵀ = ẋ(t) | 23.26 |
| Costate | (∂H/∂x)ᵀ = −λ̇(t) | 23.24 |
1. From the Lagrangian-form expansion of δJ̃ (eq. 23.13), three integrals must vanish for every admissible variation.
2. Apply the **fundamental lemma**: each integrand bracket must be identically zero on (t₀, t_f).
3. The bracket multiplying δu gives ∂H/∂u = 0 (or ∂Λ/∂u = 0, but ∂Λ/∂u reduces to ∂H/∂u because Λ − H is independent of u).
4. The bracket multiplying δx gives ∂H/∂x − dλ/dt = 0, i.e., **λ̇ = −∂H/∂x**.
5. The state equation ẋ = f = ∂H/∂λ holds by construction (it is the original constraint).
- **State equation** ⭐: ẋ(t) = ∂H/∂λ. Restates the dynamic constraint inside the Hamiltonian framework.
- **Costate equation** ⭐: λ̇(t) = −∂H/∂x. The "shadow price" of the state evolves as the negative of the Hamiltonian's sensitivity to x.

### ⚠️ Common Mistakes
- ❌ Writing the costate equation with a *positive* sign. → ✅ It is **λ̇ = −∂H/∂x**; the minus sign is essential.
- ❌ Treating ∂H/∂u = 0 as sufficient. → ✅ It is *necessary* (interior); for sufficiency, also check second-order conditions on H.
- ❌ Using ∂H/∂λ to derive the state equation in *minimisation* problems and forgetting the sign convention. → ✅ State equation is always ẋ = ∂H/∂λ regardless of max/min.

**Quick Recall:**
- **∂H/∂u = 0** (control)
- **ẋ = ∂H/∂λ** (state)
- **λ̇ = −∂H/∂x** (costate)
- Builds on: derivation of Hamiltonian (Chunk 005); Lagrange multipliers (static).
- Equivalent in continuous time to: HJB / Bellman recursion (Chunk 003).

### General Boundary Condition (Free t_f and Free x_f) 🔴

**Quick Recall:**

### Hamiltonian Optimality — Four Boundary-Condition Cases 🔴
| Case | t_f | x_f | Required boundary conditions (in addition to ∂H/∂u, ẋ, λ̇) |
|------|-----|-----|-----------------------------------------------------------|
| **A** | Fixed | Fixed | **None** — only solve eqs. 23.21 / 22, 23.23 / 24, 23.25 / 26 |
| **B** | **Free** | Fixed | Add: **H(t_f) + ∂S/∂t |_{t_f} = 0**   …(23.29) |
| **C** | Fixed | **Free** | Add: **[∂S/∂x − λ]_{t_f} = 0**   …(23.30) (vector form: …(23.31)) |
| **D** | Free | Free | Add **both** (23.32) and (23.33) (or 23.34 for vector x) |
- **Transversality condition (general)**: a boundary condition on the costate λ(t_f) (or on H(t_f) + S_t) imposed by the freedom of the corresponding endpoint.

**Quick Recall:**
- Fixed-fixed: just the 3 PMP equations.
- Free t_f → H + S_t = 0 at t_f.
- Free x_f → λ(t_f) = ∂S/∂x|_{t_f}  (so λ(t_f) = 0 if S ≡ 0).

### Transversality Condition — Sign-Restricted State 🔴
- **Complementary-slackness transversality**: either the terminal state is at its lower bound, or its shadow price is zero (or both).
- **Infinite-horizon transversality**: lim_{t→∞} λ(t) · x(t) = 0 (with sign restrictions adjusted as above).

**Quick Recall:**
- x ≥ 0 case: x(t_f) · λ(t_f) = 0 (and ≥ 0).
- x unrestricted: λ(t_f) = 0.
- Infinite horizon: lim_{t→∞} x(t) · λ(t) = 0.
- Builds on: free-end transversality from CoV (Chunk 003).
- Crucial for: Ramsey/optimal-growth models in Unit 24, exhaustible-resource problems (Hotelling).

### The Discounted Problem & Current-Value Hamiltonian 🔴
- If x_T sign-restricted:  lim_{T→∞} x_T ≥ 0,  lim_{T→∞} e^{−ρT} μ_T x_T = 0   …(23.42)
- If x_T unrestricted:    lim_{T→∞} e^{−ρT} μ_T = 0.
- **Discount rate ρ**: ρ > 0; subjective time-preference rate for the planner.
- **Current-value multiplier μ_t = λ_t e^{ρt}** ⭐: shadow price of state x_t expressed in time-t consumption units (rather than time-0 units).
- **Current-value Hamiltonian H̃ = g + μ h** ⭐⭐.
- **Modified costate equation**: μ̇ = ρμ − ∂H̃/∂x.

### ⚠️ Common Mistakes
- ❌ Forgetting the +ρμ drift term in the current-value costate equation. → ✅ μ̇ = ρμ − ∂H̃/∂x; the standard λ̇ = −∂H/∂x has no ρ-drift.
- ❌ Using e^{−ρt} terminal conditions on μ. → ✅ Transversality on μ is e^{−ρt} μ_T x_T → 0 (you must reinsert the discount factor for the limit to make sense).

**Quick Recall:**
- **H̃ = g + μ h**.
- **μ̇ = ρμ − ∂H̃/∂x**.
- ẋ = ∂H̃/∂μ = h.
- ∂H̃/∂u = 0 (control).
- Transversality: lim e^{−ρT} μ_T x_T = 0.
- Generalises: standard Hamiltonian (this section).
- Prerequisite for: Ramsey/Cass–Koopmans, optimal investment, optimal extraction in Unit 24.

### Second-Order Condition for Optimal Control 🔴
- **A* positive definite ⇒ J* is a minimum.**
- **A* negative definite ⇒ J* is a maximum.**
1. Solve the Hamiltonian (PMP) equations for u*(t), x*(t).
2. Form the symmetric Hessian matrix A of H in (x, u).
3. Evaluate A at (x*, u*) to obtain A*.
4. Sign-test: positive definite ⇒ min; negative definite ⇒ max.

**Quick Recall:**
- Builds on: 2nd-order condition from CoV (Chunk 003); positive/negative definiteness criteria.

### Worked Exercise — Linear-Quadratic Optimal Control 🔴
- ∂H/∂u = −2u + λ = 0  ⇒  **u(t) = (1/2) λ(t)**.   …(1)
- Costate: λ̇ = −∂H/∂y = −λ.  General solution: **λ(t) = k e^{−t}**, k a constant.   …(2)
- State: ẏ = y + u = y + (1/2) k e^{−t}.
  - 1 = c − k/4
  - 0 = c e − k e^{−1}/4
- ∂H/∂u = 2u + λ = 0  ⇒  **u* = −(1/2) λ(t)**.
- Costate: λ̇ = −∂H/∂x = −2x.
- State: ẋ = u = −λ/2.
- x(0) = 1 ⇒ A + B = 1.
- x(1) free ⇒ transversality (case C, eq. 23.30): [∂S/∂x − λ]_{t_f} = 0; with no terminal cost S, this gives **λ(1) = 0**, i.e. **2 ẋ(1) = 0**, so ẋ(1) = 0:

**Quick Recall:**
1. Write H = (running cost) + λ · (state equation RHS).
2. ∂H/∂u = 0 → solve for u in terms of λ.
3. λ̇ = −∂H/∂x → costate ODE.
4. ẋ = ∂H/∂λ → state ODE.
5. Reduce to a single ODE in x (or x and λ).
6. Apply BCs (initial state + transversality on free end).
7. Verify 2nd-order via Hessian of H.
- Builds on: PMP conditions, transversality (this chunk).
- Pattern reused throughout Unit 24 (Ramsey, optimal investment, etc.).
- **Hamiltonian function** ⭐: H = V + λf, formed from objective + costate × constraint.
- **Transversality condition** ⭐: boundary condition on the costate λ(t_f) when the corresponding endpoint is free; especially relevant in infinite-horizon problems without an end-point state constraint.

**Quick Recall:**

### Discounting & Present Value 🔴

**Compounding formula (discrete)**
- P = principal (today)
- r = annual interest rate (%)
- T = time horizon (years)
- Y = future value

**Present value of a future amount x_T**
- **Present value (PV)** ⭐: today-equivalent value of a future cash flow, found by dividing by (1 + r)ᵀ.
- **Discount rate r**: rate at which future cash is shrunk; usually equals the market interest rate or the planner's time-preference rate.
- **Reference year**: the year against which all cash flows are normalised; could be t = 0, t = 5, etc., as long as it is consistent.

**Quick Recall:**

### Present Value of an Investment Stream 🔴
- **Perpetuity**: a stream of equal payments continuing forever.
- **Geometric series sum**: Σ_{k=0}^{∞} y^k = 1/(1 − y) for |y| < 1.

**Quick Recall:**
- Stream: PV = Σ x_t / (1 + r)^t.
- Perpetuity starting at t=0: **(1 + r) · x / r**.
- Perpetuity starting at t=1: **x / r** (the famous "x over r" formula).
- Builds on: discrete geometric series (Block 1).
- Continuous-time analogue: PV = ∫₀^∞ e^{−ρt} x dt = x/ρ. Used throughout Hamiltonian formulations.

### Optimal Rate of Extraction of Exhaustible Resources by a Monopoly 🔴
- p_t = market price at time t,
- q_t = quantity extracted (= sold; **no inventory** — assumes zero storage),
- C(q_t) = extraction cost,
- x(t) = remaining stock,
- r = discount rate.
- **Hotelling rule** ⭐: the in-situ shadow price (or, with zero cost, the price) of an exhaustible resource grows at the discount rate r along the optimal extraction path.
- **In-situ value**: the value of the resource still in the ground.

### ⚠️ Common Mistakes
- ❌ Stating that *price* grows at r in general. → ✅ Only with **zero MC** and **constant ε** does p ∝ e^{rt}; in general, *net MR (MR − MC)* grows at r.
- ❌ Forgetting the −μ_t term in H̃. → ✅ The state equation is ẋ = −q_t, so the costate enters with a *minus* sign.

**Quick Recall:**
- Stiglitz monopoly: H̃ = p q − C(q) − μ q.
- FOC: MR − MC = μ.
- Hotelling: d(MR − MC)/dt = r · (MR − MC).
- Special case (zero MC, const ε): p_t = p_0 e^{rt}.
- Builds on: current-value Hamiltonian (Chunk 006), perpetuity PV formulas (this chunk).
- Extended in: competitive Hotelling and Optimal Depletion (Chunk 008), Optimal Growth (Chunk 008).
1. How does the rule change with **stock-dependent cost** C(q, x)? — Adds a term −∂C/∂x in the costate equation; price grows *slower* than r when extraction is cheaper at higher stocks.
2. What if the resource is renewable instead of exhaustible? — Treated next: state equation becomes x' = G(x) − q (natural growth net of harvest).
| | Competitive | Monopoly |
|---|---|---|
| FOC for q | p − C' = μ | MR(q) − C' = μ (with MR < p) |
| Hotelling rule | d(p − C')/dt = r(p − C') | d(MR − C')/dt = r(MR − C') |
| Price path (zero MC, const ε) | p ∝ e^{rt} (steeper) | p ∝ e^{rt}, but starts at *higher* level (flatter trajectory in q) |
| Extraction path q_t | Steeper (more today, less later) | Flatter (smoothed across time) |

**Quick Recall:**

### Optimal Control of a Generic Renewable Resource 🔴
- γ = intrinsic growth rate
- k = environmental carrying capacity
- For x small: g(x) ≈ γx (exponential growth); for x → k: g(x) → 0 (saturation).
- **MSY** maximises g(x): set g'(x) = 0. For logistic, g'(x) = γ(1 − 2x/k) = 0 ⇒ **x_MSY = k/2**.
- With r > 0, the optimal stock satisfies g'(x*) = r > 0, so x* < x_MSY (you sit on the *upward-sloping* portion of g).
- Only when r = 0 does x* = x_MSY (MSY = bio-economic optimum).
- **Logistic growth**: g(x) = γ x (1 − x/k).
- **Maximum Sustainable Yield (MSY)** ⭐: the harvest rate that maximises long-run yield; for logistic, occurs at x = k/2 with g(k/2) = γk/4.
- **Intrinsic growth rate γ**: the per-capita growth at low population.
- **Carrying capacity k**: the equilibrium stock at zero harvest.

### ⚠️ Common Mistakes
- ❌ Equating "optimal" with MSY. → ✅ Only when r = 0 they coincide; with r > 0 the optimal stock is **smaller** than MSY.

**Quick Recall:**
- Logistic g(x) = γx(1 − x/k); MSY at x = k/2.
- Steady state: r = g'(x*).
- r > 0 ⇒ x* < x_MSY (over-harvest relative to biologist's recommendation).
- Builds on: discounted Hamiltonian (Chunk 006), Hotelling rule (Chunk 007).
- Application named in source: **forestry / fisheries** (Fisher 2020 cited in source).
1. What if C depends on x (cost rises as stock falls)? — Adds C_x term to costate equation; pushes optimal x* upward.
2. Stochastic extensions (Reed 1979) — out of MEC-203 scope.

### Optimal Depletion of Non-Renewable Resource 🔴
- Production: **Y = F(k, R)** (two essential inputs).
- Capital evolution: **k̇ = F(k, R) − c**   …(24.11)
- Resource stock evolution: **Ṡ = −R**   …(24.12)
- Welfare: **W = ∫₀ᵀ e^{−δt} u(c) dt**   …(24.13)
- Initial conditions: k(0) = k₀, S(0) = S₀.
- **(d/dt)(∂F/∂R) = (∂F/∂k)·(∂F/∂R)**   …(24.19)   ⭐
- **ċ/c = (∂F/∂k − δ) / η**   …(24.20)   ⭐
- **Relative risk aversion η = −u''(c) c / u'(c)** ⭐: elasticity of marginal utility; assumed constant in CRRA utility.
- **Elasticity of intertemporal substitution (EIS) = 1/η**: how willingly the agent substitutes consumption between periods.
- **Modified Hotelling rule** (with capital): (d/dt)(∂F/∂R) = (∂F/∂k)(∂F/∂R).
- **Keynes–Ramsey rule** ⭐⭐: ċ/c = (∂F/∂k − δ) / η — fundamental optimal-growth condition.

**Quick Recall:**
- Two states ⇒ two costates ⇒ two coupled FOCs.
- Modified Hotelling: d/dt(F_R) = F_k · F_R.
- Keynes-Ramsey: ċ/c = (F_k − δ)/η.
- Cobb-Douglas closed form: x(t) = [(1−a)t + x_0^{1−a}]^{1/(1−a)}.
- Builds on: discounted Hamiltonian (Chunk 006), Hotelling (Chunk 007).
- Citations in source: Dasgupta & Heal (1974); Pearce (1975); Davison (1978).

**Quick Recall:**

### Neoclassical Investment Theory 🔴
- Production function F(k, L): F(k, 0) = F(0, L) = 0 (essentiality), F_k > 0, F_L > 0, F_kk < 0, F_LL < 0, F_kL ≥ 0 (concavity).
- Often: constant returns to scale F(λk, λL) = λF(k, L).
- Profit: **R(t) = p(t) F(k(t), L(t)) − w(t) L(t) − q(t) I(t)**   …(24.26).
- Firm is a price-taker: p, w, q exogenous.
- Present value: **W = ∫₀^∞ e^{−rt} R(t) dt**   …(24.27)
- Capital evolution: **k̇ = I − δ k**   …(24.28).
- **Implicit rental value of capital C** ⭐: C = q(r + δ) − q̇ — "user cost" of capital, also called Jorgenson's user cost.
- **Tobin's q-interpretation**: μ_{1t} = q is the marginal value of an additional unit of capital, equal to its unit purchase price.

### ⚠️ Common Mistakes
- ❌ Forgetting the q̇ term in user cost. → ✅ Must subtract q̇ — capital gains lower the user cost.
- ❌ Using r alone as the discount rate. → ✅ The relevant return is **r + δ**, since capital also depreciates.

**Quick Recall:**
- p ∂F/∂L = w (wage = VMPL).
- p ∂F/∂k = q (r + δ) − q̇ (Jorgenson user cost).
- μ_{1} = q (shadow price of capital = unit price of investment).
- Builds on: current-value Hamiltonian (Chunk 006); Cobb-Douglas marginal products (Chunk 008).
- Extended in: investment with adjustment costs / Tobin's q-theory (Chunk 009).
1. What if q itself depends on I (adjustment costs)? — Treated in §24.9 (Chunk 009). Tobin's q-theory.
2. What if labour and capital are non-separable (e.g., putty-clay)? — Out of MEC-203 scope.

### Optimal Growth (Ramsey) Model — Setup 🔴
- Output **y(t) = F(k_t, L_t)**.
- Wage **w(t)** = unit cost of labour. Capital cost **r(t)** = unit cost of borrowing.
- Capital depreciates at rate **δ ∈ (0, 1)**.
- Household has two income sources: wage from firm + interest on capital.
- Household consumes whatever is produced; the balance is invested back.
- Household buys output at price p_t.
- Builds on: Keynes–Ramsey rule (Chunk 008 — derived implicitly in §24.6); current-value Hamiltonian (Chunk 006).
- Continued in: Chunk 009 (full Ramsey solution + Tobin's q with adjustment costs).

### Ramsey (Cass–Koopmans) Optimal-Growth Model 🔴
- ∂π/∂L = ∂F/∂L − w(t) = 0  ⇒  **w(t) = ∂F/∂L**   …(24.35)
- ∂π/∂k = ∂F/∂k − [r(t) + δ] = 0  ⇒  **r(t) + δ = ∂F/∂k**   …(24.36)
- ∂F/∂L = (1 − a) A k^a = w   …(24.39)
- ∂F/∂k = a A k^{a−1} = r + δ   …(24.40)
- u' > 0, u'' < 0 (positive, diminishing marginal utility — Gossen's first law).
- **θ = relative risk aversion = −c · u''(c)/u'(c)** ⭐.
- **1/θ = elasticity of intertemporal substitution (EIS)** ⭐.
- **θ = 1 special case** (by L'Hôpital): **u(c) = ln c**   …(24.44).
- **CEIS / CRRA utility** ⭐: u(c) = (c^{1−θ} − 1)/(1 − θ); equivalently u(c) = ln c when θ = 1.
- **Coefficient of relative risk aversion (θ)** ⭐: −c·u''/u'; tells how the household ranks lotteries.
- **EIS = 1/θ** ⭐: how willingly the household shifts consumption between periods.
- **∂H̃/∂c = 0** ⇒ u'(c) − λ_t = 0  ⇒  **c_t^{−θ} = λ_t**   …(24.43)*
- **Costate**: λ̇_t = ρ λ_t − ∂H̃/∂k = λ_t (ρ + δ − a A k^{a−1})   …(24.44)*
- This is the **Keynes–Ramsey rule** ⭐⭐: consumption grows when the marginal product of capital exceeds (ρ + δ); EIS = 1/θ scales the response.
- **Higher A** (productivity) ⇒ k* and c* increase proportionally.
- **Higher ρ** (impatience) ⇒ k* and c* decrease (less saving).
- **Higher δ** (depreciation) ⇒ k* decreases; effect on c* depends on parameters.

### ⚠️ Common Mistakes
- ❌ Confusing ρ (rate of time preference) with r (interest rate). → ✅ At steady state, r = aAk^{a−1} − δ = ρ; otherwise they differ.
- ❌ Treating saving rate as exogenous (Solow). → ✅ In Ramsey, saving rate is **derived** optimally; only the steady-state s* is constant.
- ❌ Forgetting transversality. → ✅ Without it, you can find spurious paths that diverge.
- **Rate of time preference ρ** ⭐: subjective impatience; ρ > 0.
- **Keynes–Ramsey rule** ⭐⭐: ċ/c = (1/θ)·[F'(k) − (ρ + δ)].
- **Modified golden rule**: at the steady state of the Ramsey model, F'(k*) = ρ + δ (vs. golden rule F'(k_g) = δ).
- **Optimal saving rate s**: at steady state, s* y* = δ k*; saving exactly replaces depreciation.

**Quick Recall:**
- Cobb-Douglas Ramsey: k̇ = A k^a − c − δ k.
- Keynes-Ramsey: ċ/c = (1/θ)·[a A k^{a−1} − (ρ + δ)].
- Steady state: k* = [aA/(ρ+δ)]^{1/(1−a)}, F'(k*) = ρ + δ.
- Saving rate at SS: covers depreciation only (s* y* = δ k*).
- Welfare theorem: Ramsey saving rate is optimal — anything else lowers utility.
- Builds on: current-value Hamiltonian (Chunk 006), discounting (Chunk 007), Cobb-Douglas marginal products (Chunk 008).
- Welfare implication: dynamic inefficiency (over-saving) of the Solow model is ruled out.
- Used in: MEC-102 macroeconomics (the source explicitly notes this preview).
1. With non-constant population growth n: replace ρ with ρ + n in the FOCs (Cass–Koopmans extension).
2. With endogenous labour supply: control vector (c, L) — bigger system but same logic.

### Neoclassical Investment with Adjustment Costs (Tobin's q-theory) 🔴
- p^k = relative price of capital,
- G(I, k) = convex adjustment-cost function: ∂G/∂I > 0, ∂²G/∂I² > 0, ∂G/∂k < 0, G(0, k) = 0.
- I_max < ∞, I_min ≥ 0, δ > 0, r > 0.
- **μ_t = q(t) · p^k**: μ is the marginal value of installed capital — the present value of the additional net revenue from one extra unit of capital.
- **Tobin's marginal q ≡ μ_t / p^k**: ratio of shadow price of capital to its purchase price.
- q > 1 ⇒ install more capital; q < 1 ⇒ disinvest; q = 1 in steady state.
- k̇ = 0 ⇒ **I = δ k**   …(24.57)
- μ̇ = 0 ⇒ **μ* = ((r + δ) p^k + ∂G/∂k − ∂G/∂I·(r+δ)) / [F'(k) terms]**, but more simply: μ* = [p · ∂F/∂k − ∂G/∂k] / (r + δ).   …(24.58)
1. **μ_t > 0 always** (since p^k, δ > 0).
2. **μ̇ vs k**: With CRS, ∂F/∂k is constant in k, so the μ̇ = 0 locus is downward-sloping in (k, μ) space.
3. **k̇ = 0 locus**: I = δk; with adjustment costs, this gives an upward-sloping locus.
4. **Saddle-path stable**: the (k*, μ*) intersection is a saddle point; the optimal trajectory is the stable manifold (descends if k > k*, ascends if k < k*).
5. **Negative interest-rate elasticity of investment**: ∂I/∂r < 0 — a standard neoclassical property. Lower r raises μ_t, raising I and accelerating convergence to k*.

### ⚠️ Common Mistakes
- ❌ Equating Tobin's q with the **average** q (V/k). → ✅ The model speaks of **marginal q** = μ/p^k. They coincide only under linear-homogeneous F and G (Hayashi 1982).
- ❌ Treating G as concave. → ✅ G must be **convex** for smooth gradual adjustment; a concave G gives lumpy investment (different model, "non-convex adjustment costs").

**Quick Recall:**
- State: k̇ = I − δk.
- FOC for I: μ = p^k + G_I (purchase price + marginal adjustment cost).
- Tobin's marginal q = μ/p^k; q > 1 ⇒ invest; q < 1 ⇒ divest.
- Costate: μ̇ = (r + δ) μ − p F_k + G_k.
- Steady state: I = δk, F_k = (r + δ)·μ*/p − G_k/p.
- Builds on: neoclassical investment without adjustment (Chunk 008, §24.7).
- Generalises to: real-options / irreversible investment (out of MEC-203 scope).
- Empirical link: Tobin's q regressions in macro / asset-pricing.

**Quick Recall:**
- **Transversality condition** ⭐: lim_{t→∞} λ_t · x_t = 0 (or current-value form lim e^{−ρt} μ_t x_t = 0); necessary for infinite-horizon problems.
