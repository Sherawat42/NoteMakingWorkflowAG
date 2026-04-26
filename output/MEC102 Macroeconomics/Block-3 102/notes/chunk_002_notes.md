# Chunk 002 — Random Walk Hypothesis, Consumption-CAPM, Unit 9 Setup (Ramsey-Cass-Koopmans Central Planner)
<!-- Pages: 11-20 -->
<!-- Source: chunk_002.txt -->

## Section: Random Walk Hypothesis (Hall) — Full Derivation and Policy Implications 🔴
<!-- See chunk 001 for the setup of this section -->

### Core Idea
Building on the optimality condition derived in chunk 001 ($C_1 = E_1[C_2] = \ldots$ under quadratic utility), Hall (1978) showed that consumption follows a *random walk*: $C_{t+1} = C_t + e_{t+1}$, where $e_{t+1}$ is a mean-zero random surprise. The intuition: agents with rational expectations already incorporate all known future income changes into today's consumption, so the only thing that can move tomorrow's consumption is information they couldn't have had today. The major policy implication: anticipated government interventions (like a pre-announced tax cut) cannot affect consumption when they are implemented.

> **In Simple Terms:** If you know your salary will rise next year, you start enjoying that increase today by spending or borrowing a bit more — by the time the raise actually arrives, your consumption doesn't jump. Only true surprises move your spending. So a tax cut announced a year early is already "priced in" by the time it kicks in.

### Key Concepts

#### From optimality to random walk
From chunk 001's quadratic utility result: $C_1 = E_1[C_2] = E_1[C_3] = \cdots$. Generalizing to any period $t$:
$$E_t[C_{t+1}] = C_t$$
Under rational expectations, the actual realization differs from the expected value only by a random shock with zero mean:
$$C_{t+1} = E_t[C_{t+1}] + e_{t+1} = C_t + e_{t+1}$$
where $E[e_{t+1}] = 0$. This is the **random walk** equation: consumption from $t$ to $t+1$ stays the same except for an unpredictable random term.

#### Why consumption changes are unpredictable
- Any *expected* change in lifetime income is incorporated into consumption immediately, before the income change actually happens — through consumption smoothing.
- Therefore, consumption can only change because of *unexpected* events (surprises).
- Since surprises are by definition unpredictable, consumption changes are unpredictable.

#### Policy implication: announced policies don't work
If the government announces today a tax cut to be implemented next year, rational consumers immediately adjust today's consumption. By the time the tax cut actually takes effect, consumption has already adjusted — so it doesn't change at the time of implementation. Government policy can influence consumption only **to the extent it is unanticipated**.

### Definitions
- **Random Walk Hypothesis (RWH)**: Hall's (1978) result that under PIH plus rational expectations, changes in consumption over time are unpredictable: $C_{t+1} = C_t + e_{t+1}$ with $E[e_{t+1}] = 0$. ⭐ (exam-important)
- **Random walk**: A stochastic process in which the next value equals the current value plus a mean-zero unpredictable shock.

### Mechanisms / Processes
**Derivation chain**:
1. Quadratic utility $u(C_t) = C_t - (a/2)C_t^2$ → linear marginal utility $u'(C_t) = 1 - aC_t$
2. Optimality: $E_1[u'(C_t)] = u'(C_1)$ → $1 - aC_1 = 1 - aE_1[C_t]$
3. Rearrange: $C_1 = E_1[C_2] = E_1[C_3] = \ldots$
4. Generalize to any $t$: $E_t[C_{t+1}] = C_t$
5. Rational expectations: $C_{t+1} = E_t[C_{t+1}] + e_{t+1}$
6. Substitute: $C_{t+1} = C_t + e_{t+1}$ — consumption is a random walk

### Examples
**Example: Pre-announced tax cut**
Government announces today (year 0) that taxes will be cut next year (year 1). Effect:
- Year 0: Rational consumers immediately adjust $C_0$ upward (and $C_1, C_2, \ldots$ as well) — lifetime income is now known to be higher.
- Year 1: When the tax cut actually takes effect, $C_1$ does not change — it was already at its new level.
- A surprise tax cut implemented without warning *would* move consumption when implemented.

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking RWH says consumption never changes → ✅ Correct: It says *changes* are unpredictable; consumption does change in response to surprises.
- ❌ Mistake: Concluding fiscal policy is useless → ✅ Correct: Only *anticipated* policies are neutralized; surprise policies still affect consumption.

### Edge Cases & Caveats
- The clean random-walk result $C_{t+1} = C_t + e_{t+1}$ depends on quadratic utility (linear marginal utility); with other utility functions, the result is approximate.
- Assumes rational expectations and no liquidity constraints — empirical tests find departures from pure random-walk behavior, attributable to these factors.

> **Quick Recall:**
> - $C_{t+1} = C_t + e_{t+1}$, with $E[e_{t+1}] = 0$
> - Changes in consumption are unpredictable
> - Anticipated policies have no effect at implementation
> - Only surprises move consumption

### Connections
- Builds on: Permanent Income Hypothesis under uncertainty (Chunk 001)
- Foundation for: Consumption-CAPM (next section, generalizes to uncertain returns)

---

## Section: Consumption Capital Asset Pricing Model (C-CAPM) 🔴

### Core Idea
The previous analysis assumed asset returns were certain (often $r = 0$). The Consumption-CAPM relaxes this by introducing risky assets with uncertain returns. The optimality condition for utility maximization yields a pricing rule: the **expected excess return on a risky asset over the risk-free rate** must equal the (negative) covariance between the asset's return and next period's marginal utility of consumption, scaled by expected marginal utility. Intuitively, assets that pay off well precisely when consumption is high (low marginal utility) provide poor consumption insurance, so they must offer a higher expected return — a **risk premium**.

> **In Simple Terms:** An asset that booms when you're already doing well (high consumption, low marginal utility of money) doesn't help you much when you really need it. So the market demands a higher expected return on it. An asset that pays off in bad times (when your consumption is low) is like insurance — investors accept a lower return on it.

### Key Concepts

#### Optimality condition with uncertain returns
With risky asset return $r_{t+1}$ uncertain, the Euler equation becomes:
$$u'(C_t) = E_t[(1 + r_{t+1}) u'(C_{t+1})]$$
where $t$ is the period when expectations are formed.

#### Decomposing using the covariance identity
Statistical identity: $E(AB) = E(A)E(B) + \text{Cov}(A, B)$.
Applied to the Euler equation:
$$u'(C_t) = E_t[(1 + r_{t+1})] \cdot E_t[u'(C_{t+1})] + \text{Cov}_t[(1 + r_{t+1}), u'(C_{t+1})]$$

#### Risk-free asset
Risk-free return $i_{t+1}$ is certain → uncorrelated with $C_{t+1}$ → $\text{Cov}_t[(1 + i_{t+1}), u'(C_{t+1})] = 0$. So:
$$1 + i_{t+1} = \frac{u'(C_t)}{E_t[u'(C_{t+1})]}$$

#### Risky asset
For a risky asset with expected return $E_t(r_{t+1})$:
$$1 + E_t(r_{t+1}) = \frac{u'(C_t)}{E_t[u'(C_{t+1})]} - \frac{\text{Cov}_t[(1 + r_{t+1}), u'(C_{t+1})]}{E_t[u'(C_{t+1})]}$$

#### The C-CAPM pricing equation
Subtracting the risk-free condition from the risky-asset condition:
$$E_t[r_{t+1}] - i_{t+1} = -\frac{\text{Cov}_t[(1 + r_{t+1}), u'(C_{t+1})]}{E_t[u'(C_{t+1})]}$$

Interpretation:
- A higher value of $C_{t+1}$ implies a lower $u'(C_{t+1})$ (diminishing marginal utility, $u'' < 0$)
- A *positive* covariance between $r_{t+1}$ and $C_{t+1}$ → *negative* covariance between $r_{t+1}$ and $u'(C_{t+1})$
- → The right-hand side is positive → required risk premium is positive
- The greater the covariance between $r_{t+1}$ and $C_{t+1}$, the higher the premium the asset must offer over the risk-free rate

### Definitions
- **Consumption Capital Asset Pricing Model (C-CAPM)**: Theory in which the expected excess return on a risky asset over the risk-free rate is determined by the covariance between the asset's return and the marginal utility of consumption. ⭐ (exam-important)
- **Risk premium**: The extra expected return required on a risky asset over and above the risk-free rate, to compensate investors for risk.
- **Covariance identity**: $E(AB) = E(A)E(B) + \text{Cov}(A, B)$.

### Mechanisms / Processes
**Derivation steps**:
1. Write the Euler equation under risky returns: $u'(C_t) = E_t[(1 + r_{t+1}) u'(C_{t+1})]$
2. Apply the covariance identity to expand $E_t[(1 + r_{t+1}) u'(C_{t+1})]$
3. Apply the Euler equation to the risk-free asset (covariance = 0)
4. Subtract risk-free from risky → C-CAPM equation
5. Use $u'' < 0$ to interpret the sign of the covariance term → risk premium

### Examples
**Example: Pro-cyclical asset (e.g., equity)**
A stock that pays off well in booms (when $C_{t+1}$ is high) and badly in recessions (when $C_{t+1}$ is low) has a *positive* $\text{Cov}_t(r_{t+1}, C_{t+1})$. By C-CAPM, this implies a positive required risk premium → expected return must exceed the risk-free rate.

**Example: Counter-cyclical asset (e.g., insurance-like asset)**
An asset that pays off when $C_{t+1}$ is low has *negative* $\text{Cov}_t(r_{t+1}, C_{t+1})$ → negative risk premium → can have an expected return *below* the risk-free rate (since it provides consumption insurance).

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing total variance of an asset's return with the relevant risk in C-CAPM → ✅ Correct: Only the covariance with consumption (not total variance) matters for the premium.
- ❌ Mistake: Reading the formula as $\text{Cov}(r, C)$ directly → ✅ Correct: It is $\text{Cov}(r, u'(C))$, which has the opposite sign because $u'' < 0$.

> **Quick Recall:**
> - Euler under risky return: $u'(C_t) = E_t[(1 + r_{t+1}) u'(C_{t+1})]$
> - Risk-free: $1 + i_{t+1} = u'(C_t)/E_t[u'(C_{t+1})]$
> - C-CAPM: $E_t[r_{t+1}] - i_{t+1} = -\text{Cov}_t[(1 + r_{t+1}), u'(C_{t+1})]/E_t[u'(C_{t+1})]$
> - Higher $\text{Cov}(r, C)$ → higher risk premium

### Connections
- Builds on: Random Walk Hypothesis framework (uncertainty + Euler equation)
- Generalizes: Standard CAPM by tying risk premia to marginal utility of consumption rather than market portfolio variance

---

## Section: Unit 8 Summary 🟢

### Core Idea
Unit 8 framed consumption in a dynamic, intertemporal setting and resolved Kuznets's puzzle through a sequence of theories. Fisher's two-period optimization is the foundation; LCH and PIH explain the cross-section/time-series APC discrepancy via consumption smoothing and permanent vs. transitory income; Hall's RWH adds rational expectations under uncertainty (changes in consumption are unpredictable; anticipated policies are neutralized); and the C-CAPM extends this to uncertain returns, deriving a consumption-based risk premium.

> **Quick Recall:**
> - Fisher → LCH → PIH → RWH → C-CAPM forms a logical progression
> - Each step adds realism: multi-period → systematic income variation → random income → uncertainty + rational expectations → uncertain returns
> - All resolve different aspects of the Kuznets puzzle and policy effectiveness

---

## Section: Unit 9 — Ramsey-Cass-Koopmans Model: Introduction 🟢

### Core Idea
Unit 8 considered finite-horizon households. Unit 9 introduces the Ramsey-Cass-Koopmans (RCK) optimal growth model, which models an *infinitely-lived* household (a dynasty: members die but are replaced by identical successors). The central question: what is the optimal consumption-saving path for such a household? Two versions: (i) a central planner allocating resources to maximize aggregate welfare, and (ii) a decentralized economy with price-taking households and competitive markets. Under perfect foresight, both yield the same solution path.

> **In Simple Terms:** Imagine a family that lives forever (each generation passes wealth to the next). How should it choose between consuming now and investing for its descendants? Ramsey first asked this from a benevolent planner's viewpoint; Cass and Koopmans showed that competitive markets reach the same answer.

### Key Concepts

#### Why infinite horizon?
- An individual is finite, but the household (as a dynasty) lives forever — new identical members born each period.
- For an economy of identical infinitely-lived households, what is the optimal accumulation path?

#### Two versions of the model
| Version | Decision-maker | Year proposed |
|---------|----------------|---------------|
| Central planner's problem | Social planner allocates resources | Ramsey (1928) |
| Decentralized households' problem | Price-taking households + competitive firms | Cass (1965), Koopmans (1965) |

Both versions handle the same dynamic optimization but from different vantage points.

### Definitions
- **Ramsey-Cass-Koopmans (RCK) model**: An infinite-horizon optimal growth model where the consumption-accumulation path maximizes household utility. ⭐ (exam-important)
- **Dynastic household**: A household whose members live finitely but are replaced each period by identical new members, so the household effectively lives forever.

### Connections
- Extends: Unit 8's intertemporal choice models to infinite horizon
- Compared with: Solow growth model (1957) — RCK has optimal saving from utility maximization, Solow has exogenous saving rate

---

## Section: Central Planner's Problem (Setup) 🔴
<!-- Continues in chunk 003 (steady-state characterization, modified golden rule) -->

### Core Idea
The social planner maximizes a discounted-integral welfare function for a representative household, subject to the economy's per-capita resource constraint. Output is produced by a neoclassical CRS production function with capital and labor; population grows at exogenous rate $n$. Setting up a Hamiltonian gives four optimality conditions in continuous time, which reduce to a system of two differential equations in per-capita consumption $c$ and per-capita capital $k$.

> **In Simple Terms:** The planner is solving "how much should the economy save versus consume each year, forever?" The answer: balance the joy of consuming today against the future returns from investing. The math gives a system of equations describing how consumption and capital evolve along the optimal path.

### Key Concepts

#### Welfare function
$$W = \int_0^{\infty} u(c_t) \exp(-\rho t)\, dt$$
- $c_t$ = per capita consumption in period $t$
- $u(c_t)$ = instantaneous utility
- $\rho > 0$ = subjective discount rate (rate of time preference)

#### Why the discount factor $\exp(-\rho t)$?
Reflects household preference for present over future:
- At $t = 0$: $\exp(-\rho \cdot 0) = 1$ → current utility weighted at unity
- At $t = 1$: $\exp(-\rho)$ < 1
- At $t = 2$: $\exp(-2\rho) < \exp(-\rho)$
- Each subsequent period gets exponentially smaller weight: $1 > \exp(-\rho) > \exp(-2\rho) > \cdots$

#### Resource constraint (aggregate)
$$C_t + \frac{dK}{dt} = Y_t$$
- $C_t$ = aggregate consumption
- $dK/dt$ = investment (augments capital stock)
- $Y_t$ = total output

#### Production technology
Neoclassical production function $Y_t = F(K_t, L_t)$ with:
- Continuity, concavity, constant returns to scale (CRS)
- CRS implies per-capita output: $y = F(K/L, 1) = f(k)$
- Marginal products: $\partial F/\partial K = f'(k)$, $\partial F/\partial L = f(k) - kf'(k)$

#### Inada conditions
Assumed properties of $f(k)$:
- $f(0) = 0$ — no production with zero capital
- $\lim_{k \to 0} f'(k) = \infty$ — marginal product of capital infinite at zero capital
- $\lim_{k \to \infty} f'(k) = 0$ — marginal product of capital approaches zero as capital becomes abundant

#### Population growth
$$\frac{1}{L}\frac{dL}{dt} = n$$
Population grows at constant exogenous rate $n$.

#### Per capita resource constraint
Dividing the aggregate constraint by $L$:
$$c_t + \frac{dk}{dt} + nk_t = f(k_t)$$
or equivalently $\dfrac{dk}{dt} = f(k_t) - nk_t - c_t$.

### Definitions
- **Subjective discount rate / rate of time preference** ($\rho$): The constant factor representing how much weight the household puts on present vs. future utility. ⭐ (exam-important)
- **Inada conditions**: $f(0) = 0$, $\lim_{k \to 0} f'(k) = \infty$, $\lim_{k \to \infty} f'(k) = 0$ — limiting behavior of the marginal product of capital. ⭐ (exam-important)
- **Per capita capital stock** ($k$): Capital-labor ratio $K/L$.

### Mechanisms / Processes
**Setting up the Hamiltonian**:

Maximize $W = \int_0^{\infty} u(c_t) \exp(-\rho t)\, dt$ subject to $\dot{k}_t = f(k_t) - nk_t - c_t$, with $k_0$ given.

Hamiltonian:
$$H = u(c_t)\exp(-\rho t) + \mu_t [f(k_t) - nk_t - c_t]$$

Variables:
- Control: $c_t$
- State: $k_t$
- Co-state: $\mu_t$ (shadow price of capital)

First-order conditions (taking partial derivatives and setting to zero):

**(ia)** $u'(c_t) \exp(-\rho t) = \mu_t$ → present-discounted marginal utility of consumption equals shadow price of capital

**(iia)** $\dfrac{d\mu_t}{dt} = -\mu_t (f'(k_t) - n)$ → law of motion of co-state

**(iiia)** $\dfrac{dk_t}{dt} = f(k_t) - nk_t - c_t$ → resource constraint

**(iva)** $\lim_{t \to \infty} \mu_t k_t = 0$ → transversality condition

#### Economic meaning of (ia)
At any moment, one unit of output can be either consumed (gain: marginal utility) or invested (gain: future utility through capital accumulation, valued by shadow price). Optimality requires these returns to be equal — that's exactly what (ia) says.

#### Transversality condition (iva)
As the economy approaches infinity, either:
- The shadow price of capital $\mu_t \to 0$ (capital has no remaining value), OR
- The capital stock $k_t \to 0$ (no capital left)

#### Deriving the consumption growth equation
Differentiate (ia) with respect to $t$, use (iia) to eliminate $\dot{\mu}_t$, and let $\sigma(c) \equiv -\dfrac{cu''(c)}{u'(c)}$ denote the elasticity of marginal utility w.r.t. consumption. Result:
$$\frac{1}{c_t}\frac{dc_t}{dt} = \frac{1}{\sigma(c_t)}[f'(k_t) - n - \rho]$$

This is the **Keynes-Ramsey rule** form. Together with $\dot{k}_t = f(k_t) - nk_t - c_t$ (iiia), it forms a system of differential equations describing optimal trajectories.

### Edge Cases & Caveats
- The full steady-state characterization (modified golden rule, phase diagram, saddle path) appears in chunk 003.
- The condition $\mu_t k_t \to 0$ is the infinite-horizon analog of standard transversality conditions.

> **Quick Recall:**
> - Welfare: $W = \int_0^\infty u(c_t) e^{-\rho t} dt$
> - Resource constraint (per cap): $\dot{k}_t = f(k_t) - nk_t - c_t$
> - Production: CRS neoclassical, $y = f(k)$
> - Inada: $f(0) = 0$, $f'(0) = \infty$, $f'(\infty) = 0$
> - Hamiltonian → 4 FOCs (ia–iva)
> - Transversality: $\lim \mu_t k_t = 0$
> - Co-state $\mu_t$ = shadow price of capital
> - Keynes-Ramsey: $\dot{c}/c = (1/\sigma)[f'(k) - n - \rho]$

### Connections
- Builds on: Solow growth model (same production technology, but optimal saving rate)
- Continues in: Steady-state and saddle-path analysis (Chunk 003)
