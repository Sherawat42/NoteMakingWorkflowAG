# Chunk 006 — Unit 23: Pontryagin's Conditions, 4 Boundary Cases, Transversality, Discounted Hamiltonian, 2nd-Order
<!-- Pages: 51-60 -->
<!-- Source: chunk_006.txt + page images -->

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
- Builds on: derivation of Hamiltonian (Chunk 005); Lagrange multipliers (static).
- Equivalent in continuous time to: HJB / Bellman recursion (Chunk 003).

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
- Builds on: free-end transversality from CoV (Chunk 003).
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
- Builds on: 2nd-order condition from CoV (Chunk 003); positive/negative definiteness criteria.

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
