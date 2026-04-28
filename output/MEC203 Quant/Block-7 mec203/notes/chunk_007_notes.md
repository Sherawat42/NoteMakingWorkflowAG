# Chunk 007 — Unit 23 Exercises Wrap & Unit 24: Discounting, PV, Hotelling Monopoly Extraction
<!-- Pages: 61-70 -->
<!-- Source: chunk_007.txt + page images -->

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
- Builds on: current-value Hamiltonian (Chunk 006), perpetuity PV formulas (this chunk).
- Extended in: competitive Hotelling and Optimal Depletion (Chunk 008), Optimal Growth (Chunk 008).

### Open Questions
1. How does the rule change with **stock-dependent cost** C(q, x)? — Adds a term −∂C/∂x in the costate equation; price grows *slower* than r when extraction is cheaper at higher stocks.
2. What if the resource is renewable instead of exhaustible? — Treated next: state equation becomes x' = G(x) − q (natural growth net of harvest).
