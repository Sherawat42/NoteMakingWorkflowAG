# Chunk 008 — Unit 24: Competitive vs. Monopoly, Renewable Resources, Non-Renewable Depletion, Neoclassical Investment, Ramsey Setup
<!-- Pages: 71-80 -->
<!-- Source: chunk_008.txt + page images -->

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
- Builds on: monopolist Hotelling (Chunk 007).
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
- Builds on: discounted Hamiltonian (Chunk 006), Hotelling rule (Chunk 007).
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
- Builds on: discounted Hamiltonian (Chunk 006), Hotelling (Chunk 007).
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
- Builds on: current-value Hamiltonian (Chunk 006); Cobb-Douglas marginal products (Chunk 008).
- Extended in: investment with adjustment costs / Tobin's q-theory (Chunk 009).

### Open Questions
1. What if q itself depends on I (adjustment costs)? — Treated in §24.9 (Chunk 009). Tobin's q-theory.
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
- Builds on: Keynes–Ramsey rule (Chunk 008 — derived implicitly in §24.6); current-value Hamiltonian (Chunk 006).
- Continued in: Chunk 009 (full Ramsey solution + Tobin's q with adjustment costs).
