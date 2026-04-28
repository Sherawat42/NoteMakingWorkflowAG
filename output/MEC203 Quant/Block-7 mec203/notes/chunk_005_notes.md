# Chunk 005 — Unit 23: Optimal Control Setup, State Concept, Hamiltonian Derivation
<!-- Pages: 41-50 -->
<!-- Source: chunk_005.txt + page images -->

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
- Builds on: state-vs-control distinction (this section); discrete-time state x_t (Chunk 003).
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
- Builds on: Lagrange multipliers (Block 5), Euler–Lagrange equation (Chunk 002).
- Prerequisite for: full Pontryagin's principle (Chunk 006), discounted current-value Hamiltonian (Chunk 006), economic applications (Unit 24, Chunks 7–9).

### Open Questions
1. What if u is constrained to a non-open control set U? — Then ∂H/∂u = 0 is replaced by **maximisation of H over u ∈ U** (Pontryagin's Maximum Principle in its full form).
2. What if the state path can hit a constraint? — Constrained-state problems require additional KKT-style multipliers (out of MEC-203 scope).
