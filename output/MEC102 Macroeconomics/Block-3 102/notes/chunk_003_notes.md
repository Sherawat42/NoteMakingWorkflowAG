# Chunk 003 — RCK Steady State, Decentralized Households, Ricardian Equivalence, Math Appendix; Unit 10 Intro
<!-- Pages: 21-30 -->
<!-- Source: chunk_003.txt -->

## Section: Central Planner's Problem — Steady State, Phase Diagram, Modified Golden Rule 🔴
<!-- See chunk 002 for the setup of this section -->

### Core Idea
With the planner's optimality conditions in hand (chunk 002), the dynamics reduce to two differential equations: one for $\dot{c}$ and one for $\dot{k}$. Their loci intersect at a unique non-zero **steady state** $E$. The steady-state capital-labor ratio satisfies $f'(k) = \rho + n$ — the **modified golden rule**. The steady state is a **saddle point**: only one trajectory (the saddle path) approaches $E$ from any initial $k_0$. The planner picks initial $c_0$ to land on the saddle path, ensuring convergence to long-run equilibrium.

> **In Simple Terms:** The two equations describe how consumption and capital each evolve. They balance out at exactly one long-run point $E$. From any starting capital, there's only one consumption choice that puts the economy on a path to $E$ — too high, and you eat your future; too low, and you over-save. The planner picks just right.

### Key Concepts

#### Two driving equations
From chunk 002:
- **Capital dynamics (iiia)**: $\dot{k}_t = f(k_t) - nk_t - c_t$
- **Consumption dynamics (va)** (Keynes-Ramsey): $\dfrac{\dot{c}_t}{c_t} = \dfrac{1}{\sigma}[f'(k_t) - n - \rho]$ where $\sigma = -cu''(c)/u'(c)$

#### Phase diagram loci

**$\dot{c} = 0$ locus**: From (va), either $c_t = 0$ OR $f'(k_t) = \rho + n$. Equilibrium lies on a **vertical line** in $(k, c)$ space at $k^*$ where $f'(k^*) = \rho + n$.
- Left of vertical: $\dot{c} > 0$ → $c$ rising over time
- Right of vertical: $\dot{c} < 0$ → $c$ falling

**$\dot{k} = 0$ locus**: From (iiia), $c = f(k) - nk$. This is an **inverted-U-shaped curve** in $(k, c)$ space — $c$ first rises with $k$, then falls.
- Below the curve: $\dot{k} > 0$ → $k$ rising
- Above the curve: $\dot{k} < 0$ → $k$ falling

#### Steady state
The intersection of the vertical $\dot{c} = 0$ line and the $\dot{k} = 0$ inverted-U is the unique **steady state** $E$ (Fig. 9.3). At $E$:
- $f'(k) = \rho + n$ → defines the **modified golden rule** capital-labor ratio
- $c = f(k) - nk$ → corresponding steady-state per-capita consumption
- Both $c$ and $k$ remain constant over time

#### Saddle path
$E$ is a **saddle point**: only one unique trajectory (the saddle path) approaches it; all other trajectories diverge. Given any $k_0$, the planner chooses the initial $c_0$ that lies on the saddle path — this is the only path satisfying all four FOCs including the transversality condition.

#### Modified golden rule vs. golden rule
| Concept | Condition | Interpretation |
|---------|-----------|----------------|
| Golden rule | $f'(k_g) = n$ | Maximizes steady-state per-capita consumption |
| Modified golden rule | $f'(k^*) = \rho + n$ | RCK steady state with positive time preference |

When $\rho = 0$, the modified golden rule coincides with the golden rule. When $\rho > 0$, $f'(k^*) > f'(k_g)$ → $k^* < k_g$ → households accumulate less and reach a *lower* steady-state consumption than at the golden rule. People with positive time preference are unwilling to sacrifice current consumption for future consumption beyond a point.

### Definitions
- **Steady state**: A long-run equilibrium where the values of the variables remain constant over time. ⭐ (exam-important)
- **Modified golden rule**: The steady-state capital-labor ratio in the RCK model where $f'(k) = \rho + n$ (marginal product of capital equals population growth rate plus rate of time preference). ⭐ (exam-important)
- **Golden rule** capital-labor ratio: The steady-state $k_g$ that maximizes steady-state per-capita consumption, defined by $f'(k_g) = n$. ⭐ (exam-important)
- **Saddle path**: The unique trajectory in the phase diagram that converges to a saddle-point steady state.
- **Saddle point**: A type of steady state with one stable manifold (the saddle path) and one unstable manifold; almost all paths diverge.

### Mechanisms / Processes
**Reading the phase diagram (Fig. 9.3)**:
1. Plot vertical $\dot{c} = 0$ line at $k^*$
2. Plot inverted-U $\dot{k} = 0$ curve $c = f(k) - nk$
3. Intersection at $E$ — the steady state
4. Direction arrows in each quadrant (NE, NW, SE, SW) show motion of $(c, k)$
5. Saddle path: the unique trajectory that enters $E$
6. Given $k_0$: planner chooses $c_0$ on the saddle path

### Examples
**Example: Effect of higher discount rate $\rho$**
A higher $\rho$ (more impatient households) → higher $\rho + n$ → smaller $k^*$ (modified golden rule shifts left) → vertical $\dot{c} = 0$ line shifts left → new steady state has lower $k$ and lower $c$ than before.

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing golden rule with modified golden rule → ✅ Correct: Golden rule maximizes steady-state consumption ($f'(k_g) = n$); modified golden rule is the actual RCK steady state with $f'(k^*) = \rho + n > n$.
- ❌ Mistake: Thinking the planner chooses $k_0$ → ✅ Correct: $k_0$ is given; the planner chooses initial $c_0$ to land on the saddle path.

### Edge Cases & Caveats
- The saddle-path property is asserted, not proven, in this text.
- A higher rate of time preference $\rho$ leads to *lower* steady-state $c$ and $k$ — impatience comes at the cost of long-run consumption.

> **Quick Recall:**
> - $\dot{c} = 0$ locus: vertical at $k^*$ where $f'(k^*) = \rho + n$
> - $\dot{k} = 0$ locus: inverted-U $c = f(k) - nk$
> - Steady state $E$ at intersection — saddle point
> - Modified golden rule: $f'(k) = \rho + n$
> - Golden rule: $f'(k_g) = n$
> - When $\rho > 0$: $k^* < k_g$, $c^* < c_g$

### Connections
- Builds on: Central planner's setup (Chunk 002)
- Continues into: Decentralized households' problem (next section)

---

## Section: Decentralized Households' Problem 🔴

### Core Idea
Cass and Koopmans recast the planner's problem into a market economy of identical price-taking households + competitive firms. Households own assets (capital + bonds) and earn wage and interest income; firms hire labor and capital, paying their marginal products. Each household maximizes the same lifetime welfare function as before, subject to a budget constraint, plus a **No-Ponzi-Game (NPG) condition** ruling out infinite borrowing. Under perfect foresight, the resulting optimal trajectories are *identical* to the central planner's solution — a strong equivalence result.

> **In Simple Terms:** Take the planner's economy and replace him with millions of households trading in competitive markets. Each household chooses how much to save, paying for consumption from wages plus interest on assets. The no-borrow-forever rule prevents cheating. Remarkably, when households perfectly foresee future prices, the market outcome matches what a benevolent planner would have chosen — the "invisible hand" works.

### Key Concepts

#### Market structure
- Two competitive factor markets determine wage rate $w_t$ and rate of return on capital $r_t$
- Many identical competitive firms produce final output using same neoclassical technology as the planner
- Competition: $r_t = f'(k_t)$ and $w_t = f(k_t) - k_t f'(k_t)$ (factors paid marginal products)

#### Household assets and budget constraint
Each household holds per-capita asset stock $a_t = k_t + b_t$ where $k_t$ is per-capita capital owned and $b_t$ is per-capita debt (negative if net lender). Arbitrage in the asset market: physical capital and lending earn the same rate $r_t$.

Per-capita household income: $w_t + r_t a_t$. Budget constraint:
$$\frac{da_t}{dt} = w_t + (r_t - n) a_t - c_t$$

#### Optimization problem
Maximize $W = \int_0^\infty u(c_t) e^{-\rho t} dt$ subject to the above budget constraint, with $a_0$ given.

Hamiltonian:
$$H = u(c_t)\exp(-\rho t) + \mu_t [w_t + (r_t - n)a_t - c_t]$$

#### First-order conditions
**(ib)** $u'(c_t)\exp(-\rho t) = \mu_t$
**(iib)** $\dot{\mu}_t = -\mu_t (r_t - n)$
**(iiib)** $\dot{a}_t = w_t + (r_t - n)a_t - c_t$
**(ivb)** $\lim_{t \to \infty} \mu_t a_t = 0$ (transversality)

These mirror the planner's (ia)–(iva) but with $r_t$ in place of $f'(k_t)$ and $a_t$ in place of $k_t$.

#### No-Ponzi-Game (NPG) condition (additional)
**(vb)** $\lim_{t \to \infty} a_t \cdot \exp\left(-\int_0^t (r_\tau - n)\, d\tau\right) \geq 0$

This rules out infinite-debt financing of consumption. Without NPG, an optimal household would borrow to fund infinitely high consumption forever (since net debt would grow at rate $r - n$ but never need to be repaid). NPG forces the present discounted value of long-run assets to be non-negative.

#### Consumption growth equation (decentralized)
**(vib)** $\dfrac{\dot{c}_t}{c_t} = \dfrac{1}{\sigma}[r_t - n - \rho]$

Same form as the planner's Keynes-Ramsey rule, with $r_t$ replacing $f'(k_t)$.

#### Equivalence under perfect foresight
- **Perfect foresight** assumption: households cannot derive $w$ and $r$ as functions of $k$, but they exactly guess their values at every point in time.
- In equilibrium, net borrowing across households is zero (identical agents): $a_t = k_t$.
- Substituting $r_t = f'(k_t)$, $w_t = f(k_t) - k_t f'(k_t)$, and $a_t = k_t$ into the household's (iiib) and (vib) yields the **same** system as the planner's.
- Conclusion: optimal consumption-accumulation paths in the decentralized economy coincide with the planner's. Market and planner solutions are identical.

### Definitions
- **No-Ponzi-Game (NPG) condition**: A constraint preventing infinite debt accumulation by requiring the present discounted value of the household's per-capita asset stock to be non-negative as $t \to \infty$. ⭐ (exam-important)
- **Ponzi-game financing**: A scheme of consuming above income forever by perpetually borrowing more, including to repay interest — ruled out by NPG.
- **Perfect foresight**: Assumption that households exactly anticipate future values of prices ($w$, $r$) without errors. ⭐ (exam-important)
- **Arbitrage condition** (in the asset market): physical capital and bonds must earn the same rate of return.

### Mechanisms / Processes
**Why NPG matters**:
1. Without NPG: household maintains infinite consumption stream by borrowing.
2. Net per-capita borrowing grows exponentially at rate $r - n$ (must borrow for both consumption and interest payments).
3. PDV of net debt → $\infty$. Lenders would never offer such loans.
4. NPG enforces eventual repayment (or non-negative long-run assets in PDV terms).

**Equivalence proof sketch**:
1. Household FOCs: (ib), (iib), (iiib), (ivb), (vb) → consumption growth (vib).
2. Equilibrium: $a_t = k_t$, $r_t = f'(k_t)$, $w_t = f(k_t) - k_t f'(k_t)$.
3. Substitute into (iiib): $\dot{k}_t = (f(k_t) - k_t f'(k_t)) + (f'(k_t) - n) k_t - c_t = f(k_t) - nk_t - c_t$ — matches planner's (iiia).
4. Substitute into (vib): $\dot{c}_t/c_t = (1/\sigma)[f'(k_t) - n - \rho]$ — matches planner's (va).
5. Same system → same solution.

### Examples
**Example: Why net borrowing is zero in equilibrium**
All households are identical → if one wants to be a net borrower, so do all others. But with no net lender, no borrowing is possible. So in equilibrium, $b_t = 0$ for every household → $a_t = k_t$.

### ⚠️ Common Mistakes
- ❌ Mistake: Forgetting the NPG condition is *additional* to the standard FOCs → ✅ Correct: For decentralized households (with borrowing), NPG (vb) is required *on top of* (ib)–(ivb).
- ❌ Mistake: Thinking the equivalence holds without perfect foresight → ✅ Correct: Equivalence depends crucially on perfect foresight; with imperfect anticipation, market and planner solutions can diverge.

> **Quick Recall:**
> - Budget: $\dot{a}_t = w_t + (r_t - n)a_t - c_t$
> - FOCs: (ib)–(ivb) + NPG (vb)
> - Consumption growth: $\dot{c}/c = (1/\sigma)[r_t - n - \rho]$
> - Equilibrium: $a_t = k_t$, $r_t = f'(k_t)$, $w_t = f(k_t) - k_t f'(k_t)$
> - Under perfect foresight: market path = planner path
> - NPG rules out infinite-debt financing

### Connections
- Builds on: Central planner's problem (same structure, different setup)
- Foundation for: Government in RCK & Ricardian Equivalence (next section)

---

## Section: Government in RCK and Ricardian Equivalence 🔴

### Core Idea
Adding a government with lump-sum taxation lowers steady-state consumption by exactly the tax amount, leaving the steady-state capital stock unchanged (the $\dot{k} = 0$ locus shifts down by $\tau$). The deeper result: whether the government finances spending by taxation **or** by borrowing makes no difference to households' optimal decisions. Forward-looking households with perfect foresight know that any debt today must be repaid by future taxes, and they save accordingly. This is **Ricardian Equivalence**.

> **In Simple Terms:** If the government taxes you ₹100 today, you adjust. If instead the government borrows ₹100 today (issuing a bond), you know you'll be taxed later to repay it — so you save the windfall to cover that future tax. Either way, your real situation is identical. Tax now or borrow now: same outcome for the household.

### Key Concepts

#### Tax-financed government (lump-sum tax $\tau$ per period)
- Disposable household income: $w_t + r_t a_t - \tau$
- Modified budget constraint: $\dot{a}_t = w_t + (r_t - n)a_t - c_t - \tau$
- Other FOCs unchanged
- Phase diagram: $\dot{k} = 0$ curve shifts *downward* by $\tau$
- New steady state $E'$ (Fig. 9.4): $k$ unchanged, but $c$ lower by $\tau$

#### Debt-financed government
At first glance: government bonds = household asset → no reduction in disposable income → composition of portfolio changes but not optimum.

But a careful analysis: if government must maintain a balanced budget in the long run (cannot borrow indefinitely), at some future date taxes must rise to repay debt. With perfect foresight, households anticipate this future tax burden → adjust current consumption and capital accumulation accordingly → end up at the same optimum as under tax financing.

#### Ricardian Equivalence
For households with perfect foresight (or rational expectations), the **mode of financing** (tax vs. debt) of government expenditure does not matter. Tax financing and debt financing are equivalent for household optima.

### Definitions
- **Lump-sum tax**: A tax of fixed amount $\tau$ that does not depend on income or behavior, hence does not distort decisions at the margin.
- **Ricardian Equivalence**: The proposition that, for forward-looking households with perfect foresight, the choice between tax and debt financing of government expenditure has no effect on household consumption or capital accumulation. ⭐ (exam-important)

### Mechanisms / Processes
**Effect of lump-sum tax in phase diagram**:
1. Budget constraint adds $-\tau$ → $\dot{k} = 0$ locus shifts down by $\tau$ (new $c = f(k) - nk - \tau$).
2. The $\dot{c} = 0$ vertical line is unchanged ($f'(k) = \rho + n$ still defines $k^*$).
3. New intersection $E'$: same $k^*$, lower $c^* - \tau$.

**Why debt financing is equivalent**:
1. Government issues bonds today instead of taxing → households' apparent income unchanged today.
2. Government must eventually balance budget → future taxes will rise.
3. Households with perfect foresight know future tax burden → save the windfall to cover it.
4. Net effect: identical to immediate taxation.

### Examples
**Example: Tax cut financed by debt (Ricardian)**
Government cuts taxes today by $\tau$ and borrows $\tau$ to fund the deficit. Households receive an apparent windfall of $\tau$. But they know that $\tau$ (plus interest) of future taxes is coming, so they save $\tau$ today (plus enough to cover the future interest). Current consumption is unchanged.

### ⚠️ Common Mistakes
- ❌ Mistake: Believing debt financing stimulates consumption (vs. tax financing) → ✅ Correct: Under Ricardian Equivalence with perfect foresight, the two are identical.
- ❌ Mistake: Assuming Ricardian Equivalence holds in all real-world settings → ✅ Correct: Requires perfect foresight; can fail with myopic agents, liquidity constraints, or finite horizons (relevant for OLG model — Unit 10).

### Edge Cases & Caveats
- The result depends on lump-sum (non-distorting) taxes. Distortionary taxes break the equivalence.
- Requires that government's lifetime budget constraint binds (eventually).

> **Quick Recall:**
> - Lump-sum tax: $k$ unchanged at steady state, $c$ falls by $\tau$
> - Phase diagram: $\dot{k} = 0$ shifts down by $\tau$
> - Ricardian Equivalence: tax = debt financing under perfect foresight
> - Households save windfall from debt financing to cover future taxes
> - Requires perfect foresight (fails in OLG and other settings)

### Connections
- Builds on: Decentralized households' problem (Chunk 003)
- Compare with: OLG model (Chunk 004) — Ricardian Equivalence breaks down with finite-life selfish generations

---

## Section: Unit 9 Summary 🟢

### Core Idea
The RCK model derives the optimal consumption-accumulation path for an infinitely-lived economy as the saddle path leading to a steady state defined by the modified golden rule. The same path arises whether the economy is run by a benevolent central planner or by competitive decentralized households (under perfect foresight). Adding a government financed by lump-sum taxation lowers steady-state consumption but not capital; further, the choice of tax vs. debt financing is irrelevant under perfect foresight (Ricardian Equivalence).

> **Quick Recall:**
> - Optimal path = saddle path → steady state $E$
> - Steady state: modified golden rule $f'(k) = \rho + n$
> - Centralized = decentralized under perfect foresight
> - Lump-sum tax → lower $c^*$, same $k^*$
> - Ricardian Equivalence: tax = debt financing

---

## Section: Mathematical Appendix — Dynamic Optimization in Continuous Time (Optimal Control) 🟡

### Core Idea
This appendix provides the mathematical foundation for the dynamic optimization techniques used throughout Unit 9. **Pontryagin's Maximum Principle** gives the necessary first-order conditions for optimization problems where one chooses a control variable over time, subject to a differential equation governing a state variable. The Hamiltonian function packages the problem's payoff and constraint together; partial derivatives yield the optimality conditions and the law of motion of the **co-state variable** (the shadow price of the state).

> **In Simple Terms:** This is the toolbox behind the Hamiltonians used earlier. You're choosing a path through time, your choice today affects tomorrow's state, and you want to maximize a total reward. The Hamiltonian rolls everything into one expression; its derivatives spit out the rules for optimal motion.

### Key Concepts

#### A.1 Finite horizon problem
Maximize $W = \int_0^T F(u_t, x_t, t)\, dt$, subject to $\dfrac{dx_t}{dt} = f(u_t, x_t, t)$, with $x_0 = \bar{x}_0$ and $u \in U$.

- **Control variable** $u_t$: variable directly chosen
- **State variable** $x_t$: variable changing as a function of $u_t$ via the differential equation
- **State transition function** $f$: defines how $x$ evolves
- **Instantaneous objective function** $F$: per-period payoff (depends on both $u$ and $x$)

#### Pontryagin's Maximum Principle
There exists a co-state variable $\mu_t$ (continuous, piecewise differentiable) and a Hamiltonian:
$$H(u_t, x_t, \mu_t, t) = F(u_t, x_t, t) + \mu_t \cdot f(u_t, x_t, t)$$
such that, along the optimal path $(u_t^*, x_t^*)$:

**(i)** $H$ is maximized w.r.t. $u$ at $u^*$ for all $t \in [0, T]$
**(ii)** $\dfrac{\partial H}{\partial x}\bigg|_{u^*, x^*} = -\dfrac{d\mu_t}{dt}$
**(iii)** $\dfrac{\partial H}{\partial \mu}\bigg|_{u^*, x^*} = \dfrac{dx_t}{dt}$
**(iv)** $\mu_T x_T = 0$ (Transversality condition for finite horizon)

If $H$ is non-linear in $u$, condition (i) can be replaced by $\partial H/\partial u = 0$ (provided second-order condition $\partial^2 H/\partial u^2 < 0$ holds).

#### Co-state interpretation
$\mu_t$ measures the change in objective value $W$ from a tiny exogenous increment to $x$ at time $t$ (with re-optimization thereafter). It is the **shadow price** of the state variable at time $t$.

#### A.2 Infinite horizon problem
Same setup but $T = \infty$. Two complications:
1. The integral $W$ may not converge — so additional restrictions needed.
2. Transversality condition is more controversial; usually a limiting form: $\lim_{t \to \infty} \mu_t x_t = 0$.

The FOCs (i)–(iii) are unchanged; (iv) becomes the limiting transversality condition.

### Definitions
- **Hamiltonian function**: $H = F(u, x, t) + \mu \cdot f(u, x, t)$ — packages payoff and constraint for dynamic optimization. ⭐ (exam-important)
- **Control variable**: The variable directly chosen by the optimizer at each instant.
- **State variable**: The variable whose evolution is determined by the choice of control through a differential equation.
- **Co-state variable** ($\mu$): Continuous-time analog of a Lagrange multiplier; measures the marginal value of the state variable. ⭐ (exam-important)
- **Transversality condition**: A terminal condition on the co-state and state variable; $\mu_T x_T = 0$ (finite horizon) or $\lim_{t \to \infty} \mu_t x_t = 0$ (infinite horizon). ⭐ (exam-important)
- **Pontryagin's Maximum Principle**: The set of necessary conditions for optimal control problems, characterizing optimal paths via the Hamiltonian. ⭐ (exam-important)

### Mechanisms / Processes
**Steps to solve a dynamic optimization problem**:
1. Identify control $u$, state $x$, instantaneous objective $F$, transition $f$.
2. Write Hamiltonian $H = F + \mu f$.
3. Apply Pontryagin's conditions: maximize $H$ w.r.t. $u$; derive laws of motion for $\mu$ and $x$.
4. Apply transversality.
5. Solve the resulting system of differential equations.

### Edge Cases & Caveats
- For infinite-horizon problems, must verify the integral converges.
- When $H$ is linear in $u$, the maximization in (i) might give corner solutions (bang-bang control); the partial derivative shortcut doesn't apply.

> **Quick Recall:**
> - Hamiltonian: $H = F(u, x, t) + \mu \cdot f(u, x, t)$
> - FOCs: max $H$ w.r.t. $u$; $-\dot{\mu} = \partial H/\partial x$; $\dot{x} = \partial H/\partial \mu$
> - Transversality: $\mu_T x_T = 0$ (finite); $\lim \mu_t x_t = 0$ (infinite)
> - Co-state $\mu$ = shadow price of state

### Connections
- Provides the mathematical engine for: Central planner's problem and decentralized households' problem (RCK, Chunks 002–003)

---

## Section: Unit 10 — Overlapping Generations Model: Introduction 🟢

### Core Idea
Unit 9's RCK assumed infinitely-lived dynastic households. Unit 10 introduces an alternative framework — the **Overlapping Generations (OLG) model** developed by Samuelson (1954) — where individuals live for finite (typically two) periods but the society lives forever. At each point in time, two generations are simultaneously alive: the current young (born this period) and the current old (born last period). Their lives overlap by exactly one period.

> **In Simple Terms:** Imagine an economy that runs forever, but each person only lives for two periods (young then old). At any moment, you have one batch of working-age young people and one batch of retired old people overlapping. New babies replace the dying old each period. This is a different way to model long-run dynamics — and it produces results (notably possible inefficiency) that the RCK model rules out.

### Key Concepts

#### Two-period generations setup
Each generation lives exactly 2 periods:
- The cohort born at the beginning of period $t$ ("generation $t$"): alive in period $t$ (young) and period $t+1$ (old).
- The cohort born at the beginning of period $t+1$: alive in periods $t+1$ (young) and $t+2$ (old).
- Two successive generations overlap for exactly one period.

#### Why use OLG?
- Generations are *finitely* lived (more realistic than dynastic infinitely-lived agents)
- Each generation is selfish — no bequest to next generation
- Society as a whole lives forever
- Yields qualitatively different results from RCK (e.g., possible dynamic inefficiency, role for social security)

### Definitions
- **Overlapping Generations (OLG) framework**: A model where individuals have finite (typically two-period) lives and at each point in time the lifetimes of two successive generations overlap. ⭐ (exam-important)
- **Generation $t$**: The cohort of people born at the beginning of period $t$.

### Connections
- Compare with: RCK model (infinite-life dynasty vs. finite-life selfish individuals)
- Continues into: Structure of the model + Dynamic Inefficiency + Social Security (Chunk 004)
