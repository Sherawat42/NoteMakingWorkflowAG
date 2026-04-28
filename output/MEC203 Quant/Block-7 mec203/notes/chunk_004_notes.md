# Chunk 004 — Cake-Eating Solution, Unit 22 Wrap, Unit 23 Setup
<!-- Pages: 31-40 -->
<!-- Source: chunk_004.txt + page images -->

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
- Builds on: Bellman equation (Chunk 003), discounted utility (Chunk 003).
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
- Builds on: Euler–Lagrange (Chunk 002), transversality conditions (Chunk 003).
- Prerequisite for: Hamiltonian + Pontryagin's principle (Chunk 005), economic applications in Unit 24.
