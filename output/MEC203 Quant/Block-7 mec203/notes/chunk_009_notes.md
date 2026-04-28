# Chunk 009 — Unit 24: Ramsey Model in Detail, Investment with Adjustment Costs (Tobin's q), Wrap-up
<!-- Pages: 81-90 -->
<!-- Source: chunk_009.txt + page images -->

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
- Builds on: current-value Hamiltonian (Chunk 006), discounting (Chunk 007), Cobb-Douglas marginal products (Chunk 008).
- Welfare implication: dynamic inefficiency (over-saving) of the Solow model is ruled out.
- Used in: MEC-102 macroeconomics (the source explicitly notes this preview).

### Open Questions
1. With non-constant population growth n: replace ρ with ρ + n in the FOCs (Cass–Koopmans extension).
2. With endogenous labour supply: control vector (c, L) — bigger system but same logic.

---

## Section: Neoclassical Investment with Adjustment Costs (Tobin's q-theory) 🔴
<!-- Reason: macro / corporate finance link; Tobin's q is named theorem -->

### Core Idea
The basic neoclassical model (Chunk 008) has investment respond instantaneously to differences between marginal product and user cost — unrealistic. **Adjustment costs** (Eisner–Strotz 1963) introduce a convex cost G(I, k) to investment, so capital adjusts only **gradually**. The shadow price of capital μ(t) becomes **Tobin's marginal q**, and the optimal investment function depends on q.

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
