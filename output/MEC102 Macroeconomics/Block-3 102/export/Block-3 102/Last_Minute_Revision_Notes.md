# Last Minute Revision Notes

> *This document contains ONLY ultra-high-yield definitions (⭐), Quick Recall facts, Common Mistakes, and core bullet points.*


## Topics


**Quick Recall:**
- Keynes: $C_t = \bar{C} + cY_t$ → APC falls as $Y_t$ rises
- Cross-section data: APC falls with income (matches Keynes)
- Time-series data (Kuznets): APC constant over long run (contradicts Keynes)
- Puzzle drives the whole unit

### Fisher's Two-Period Intertemporal Choice Model 🔴

**Two-period setup**

**Intertemporal budget constraint (IBC)**
- Left side: present discounted value (PDV) of total lifetime consumption
- Right side: PDV of total lifetime income ($\hat{Y}$)
- Optimal $C_1$ is a function of $\hat{Y}$ and $r$

**Geometry of optimization (Fig. 8.1)**
- **Intertemporal budget constraint (IBC)**: $C_1 + \dfrac{C_2}{1+r} = Y_1 + \dfrac{Y_2}{1+r}$ — present discounted value of lifetime consumption equals present discounted value of lifetime income. ⭐ (exam-important)
- **Present discounted value (PDV)**: Today's value of future flows discounted at the interest rate.
- **Lifetime income** ($\hat{Y}$): The PDV of all current and future income.
1. $\hat{Y}$ rises → IBC shifts outward
2. If $C_1$ and $C_2$ are both normal goods → both $C_1$ and $C_2$ increase
3. Income effect → unambiguous: $C_1 \uparrow$
| Effect | Direction on $C_1$ | Reasoning |
|--------|--------------------|-----------|
| Income effect | $C_1 \uparrow$ | Higher $r$ means same savings buys more future consumption — feels richer, broader choice set |
| Substitution effect | $C_1 \downarrow$ | Future consumption is now relatively cheaper → substitute toward $C_2$ |
- Income effect dominates → $C_1 \uparrow$
- Substitution effect dominates → $C_1 \downarrow$
- Set $C_1 = 0$ in the IBC: $C_2/(1+r) = Y_1 + Y_2/(1+r)$ → $C_2 = (1+r)Y_1 + Y_2$
- Set $C_2 = 0$ in the IBC: $C_1 = Y_1 + Y_2/(1+r)$
- These give the x- and y-intercepts of the budget line.

### ⚠️ Common Mistakes
- ❌ Mistake: Assuming a higher $r$ always raises savings → ✅ Correct: Effect on savings is ambiguous; depends on relative strength of income vs. substitution effect.
- ❌ Mistake: Treating Fisher's model as just about current income → ✅ Correct: Current consumption depends on PDV of *lifetime* income $\hat{Y}$ and on $r$, not just $Y_1$.
- The interest rate $r$ here is strictly the *expected* future rate of interest expected to prevail in period 2. The simple model assumes the future is certain and known.

**Quick Recall:**
- IBC: $C_1 + C_2/(1+r) = Y_1 + Y_2/(1+r) = \hat{Y}$
- $\Delta Y_1 \uparrow$ → $C_1 \uparrow$, $C_2 \uparrow$ (both normal)
- $\Delta r \uparrow$ → effect on $C_1$ ambiguous (income vs. substitution)
- Same ambiguity for savings
- Foundation for: Life Cycle Hypothesis, Permanent Income Hypothesis, Random Walk Hypothesis (all extend Fisher's intertemporal logic)

### Life Cycle Hypothesis (Modigliani–Brumberg) 🔴

**T-period model setup**

**Intertemporal budget constraint (T periods, $r = 0$)**

**Consumption smoothing result**

**Implication for current income**
- If $Y_t$ rises by $Z$ in one period only → $C_t$ rises by only $Z/T$
- If $Y_t$ rises by $Z$ now and falls by $Z$ later (so lifetime income unchanged) → $C_t$ does not change in any period

**Savings function (from LCH)**

**Income–consumption pattern over the lifetime (Fig. 8.2)**
- Income $Y_t$: low at young ages (low productivity), peaks in middle age, falls again in old age
- Consumption $C_t$: flat across the entire life
- Result: dissave when young (run down $A_0$ or borrow); save in middle years; dissave again in old age (run down accumulated wealth)
- **Consumption smoothing**: Spreading lifetime resources equally across all periods so consumption is constant even when income varies. ⭐ (exam-important)
- **Life Cycle Hypothesis (LCH)**: Modigliani–Brumberg's theory that households smooth consumption over the life cycle by saving during high-income middle years and dissaving in early and late years. ⭐ (exam-important)
- **Cross-sectional data**: At one point in time, the high-income category disproportionately contains middle-aged people (high income relative to their average lifetime income → high savings rate, low APC). The low-income category disproportionately contains young/old people (low income relative to lifetime average → high APC). So cross-section shows falling APC with income.
- **Time-series (long-run)**: As aggregate income rises over decades, the asset stock $A_0$ rises along with it (positively correlated). The short-run consumption line shifts upward over time (Fig. 8.3), so the long-run locus traced through points like A, B, C is steeper and exhibits a constant APC ($C_t$ proportional to $Y_t$).
- Result $C_1 = C_2 = \cdots = C_T$ depends on the assumption $r = 0$ and on time-additive utility with no discounting — qualitatively, smoothing logic survives generalization, but the exact equality does not.
- Initial asset stock $A_0$ matters — higher $A_0$ raises consumption in every period.

**Quick Recall:**
- Optimal: $C_t = (A_0 + \hat{Y})/T$ for all $t$ — flat consumption
- $S_t = Y_t - \hat{Y}/T - A_0/T$ — save when current income > lifetime average
- Income hump-shaped over life; consumption flat → dissave young + old, save middle
- Cross-section APC ↓ because middle-aged dominate high-income group
- Time-series APC constant because asset stock rises with income
- Builds on: Fisher's intertemporal choice (extends 2-period to T-period)
- Compare with: Permanent Income Hypothesis (alternative explanation, different income process)

### Permanent Income Hypothesis (Friedman) 🔴

**Decomposition of current income**
- $Y_t^P$ = **permanent income** = long-run average income, $\dfrac{1}{T}\sum_{t=1}^T Y_t$
- $Y_t^T$ = **transitory income** = random deviation, $Y_t - \dfrac{1}{T}\sum_{t=1}^T Y_t$
- Positive $Y_t^T$: current income exceeds permanent → windfall
- Negative $Y_t^T$: current income falls short of permanent → temporary dip

**Consumption depends only on permanent income**

**APC and the $Y^P/Y$ ratio**
- When current income temporarily rises above permanent ($Y_t^T > 0$, so $Y_t^P/Y_t < 1$) → APC falls
- When current income temporarily falls below permanent → APC rises
- **Permanent income** ($Y^P$): The long-run average income an individual expects to prevail. ⭐ (exam-important)
- **Transitory income** ($Y^T$): Random deviation of current income from permanent income; can be positive or negative. ⭐ (exam-important)
- **Permanent Income Hypothesis (PIH)**: Friedman's theory that current consumption depends only on permanent (long-run average) income, not on transitory deviations. ⭐ (exam-important)
- **Cross-sectional data**: The high-income group at any point in time disproportionately contains people with positive transitory income (lucky this year) → their APC is below average. The low-income group disproportionately contains people with negative transitory income → APC above average. So the cross-section shows falling APC with income.
- **Time-series (long-run)**: Random transitory shocks average out across many people and many years. Long-run income changes reflect changes in *permanent* income, so APC stays constant.

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing LCH and PIH because both resolve the same puzzle → ✅ Correct: LCH posits a *systematic* hump-shaped life-cycle income; PIH posits *random* temporary deviations from a long-run average.
- ❌ Mistake: Thinking a transitory income increase boosts current consumption → ✅ Correct: Under PIH, $C_t$ depends only on $Y_t^P$; transitory income changes do not move $C_t$.

**Quick Recall:**
- $Y_t = Y_t^P + Y_t^T$
- $C_t = A_0/T + Y_t^P$ — consumption depends only on permanent income
- APC = $C_t/Y_t$ depends on $Y_t^P/Y_t$
- Cross-section: high-income group has positive $Y^T$ → low APC
- Long run: transitory shocks average out → constant APC
- Builds on: Fisher's intertemporal choice (consumption depends on lifetime/long-run income)
- Compare with: Life Cycle Hypothesis (alternative explanation of the same puzzle)
- Foundation for: Random Walk Hypothesis (Hall extends PIH under uncertainty + rational expectations)

### Setup for Consumption under Uncertainty (Hall's Random Walk Hypothesis — Setup) 🔴

**Maximization problem under uncertainty**

**Optimality condition under rational expectations**

**Quadratic utility — closed-form result**
- **Rational expectations**: A theory in which agents' expectations do not differ systematically from realized outcomes — agents use all available information optimally. ⭐ (exam-important)
1. Permanent income is uncertain
2. Maximize expected utility subject to expected lifetime budget
3. Optimality: $u'(C_1) = E_1[u'(C_t)]$ for all $t$
4. Apply rational expectations: actual $C_t$ = expected $C_t$ + random surprise
5. → Changes in consumption are unpredictable (full random walk result derived in chunk 002)
- Quadratic utility is a strong assumption used to get the clean linear result; the qualitative random-walk result holds more generally but requires more careful approximation.
- The full random walk equation $C_{t+1} = C_t + e_{t+1}$ and its policy implications are derived in chunk 002.

**Quick Recall:**
- Under uncertainty: maximize $E[U] = \sum E[u(C_t)]$
- Optimality: $u'(C_1) = E_1[u'(C_t)]$ for all future $t$
- Quadratic utility ⇒ $C_1 = E_1[C_2] = E_1[C_3] = \cdots$
- Sets up Hall's random walk result (full derivation in chunk 002)
- Builds on: Permanent Income Hypothesis (Friedman) — extends PIH to uncertain environment
- Continues in: Random Walk Hypothesis derivation and policy implications (Chunk 002)

### Random Walk Hypothesis (Hall) — Full Derivation and Policy Implications 🔴

**From optimality to random walk**

**Why consumption changes are unpredictable**
- Any *expected* change in lifetime income is incorporated into consumption immediately, before the income change actually happens — through consumption smoothing.
- Therefore, consumption can only change because of *unexpected* events (surprises).
- Since surprises are by definition unpredictable, consumption changes are unpredictable.

**Policy implication: announced policies don't work**
- **Random Walk Hypothesis (RWH)**: Hall's (1978) result that under PIH plus rational expectations, changes in consumption over time are unpredictable: $C_{t+1} = C_t + e_{t+1}$ with $E[e_{t+1}] = 0$. ⭐ (exam-important)
- **Random walk**: A stochastic process in which the next value equals the current value plus a mean-zero unpredictable shock.
1. Quadratic utility $u(C_t) = C_t - (a/2)C_t^2$ → linear marginal utility $u'(C_t) = 1 - aC_t$
2. Optimality: $E_1[u'(C_t)] = u'(C_1)$ → $1 - aC_1 = 1 - aE_1[C_t]$
3. Rearrange: $C_1 = E_1[C_2] = E_1[C_3] = \ldots$
4. Generalize to any $t$: $E_t[C_{t+1}] = C_t$
5. Rational expectations: $C_{t+1} = E_t[C_{t+1}] + e_{t+1}$
6. Substitute: $C_{t+1} = C_t + e_{t+1}$ — consumption is a random walk
- Year 0: Rational consumers immediately adjust $C_0$ upward (and $C_1, C_2, \ldots$ as well) — lifetime income is now known to be higher.
- Year 1: When the tax cut actually takes effect, $C_1$ does not change — it was already at its new level.
- A surprise tax cut implemented without warning *would* move consumption when implemented.

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking RWH says consumption never changes → ✅ Correct: It says *changes* are unpredictable; consumption does change in response to surprises.
- ❌ Mistake: Concluding fiscal policy is useless → ✅ Correct: Only *anticipated* policies are neutralized; surprise policies still affect consumption.
- The clean random-walk result $C_{t+1} = C_t + e_{t+1}$ depends on quadratic utility (linear marginal utility); with other utility functions, the result is approximate.
- Assumes rational expectations and no liquidity constraints — empirical tests find departures from pure random-walk behavior, attributable to these factors.

**Quick Recall:**
- $C_{t+1} = C_t + e_{t+1}$, with $E[e_{t+1}] = 0$
- Changes in consumption are unpredictable
- Anticipated policies have no effect at implementation
- Only surprises move consumption
- Builds on: Permanent Income Hypothesis under uncertainty (Chunk 001)
- Foundation for: Consumption-CAPM (next section, generalizes to uncertain returns)

### Consumption Capital Asset Pricing Model (C-CAPM) 🔴

**Optimality condition with uncertain returns**

**Decomposing using the covariance identity**

**Risk-free asset**

**Risky asset**

**The C-CAPM pricing equation**
- A higher value of $C_{t+1}$ implies a lower $u'(C_{t+1})$ (diminishing marginal utility, $u'' < 0$)
- A *positive* covariance between $r_{t+1}$ and $C_{t+1}$ → *negative* covariance between $r_{t+1}$ and $u'(C_{t+1})$
- → The right-hand side is positive → required risk premium is positive
- The greater the covariance between $r_{t+1}$ and $C_{t+1}$, the higher the premium the asset must offer over the risk-free rate
- **Consumption Capital Asset Pricing Model (C-CAPM)**: Theory in which the expected excess return on a risky asset over the risk-free rate is determined by the covariance between the asset's return and the marginal utility of consumption. ⭐ (exam-important)
- **Risk premium**: The extra expected return required on a risky asset over and above the risk-free rate, to compensate investors for risk.
- **Covariance identity**: $E(AB) = E(A)E(B) + \text{Cov}(A, B)$.
1. Write the Euler equation under risky returns: $u'(C_t) = E_t[(1 + r_{t+1}) u'(C_{t+1})]$
2. Apply the covariance identity to expand $E_t[(1 + r_{t+1}) u'(C_{t+1})]$
3. Apply the Euler equation to the risk-free asset (covariance = 0)
4. Subtract risk-free from risky → C-CAPM equation
5. Use $u'' < 0$ to interpret the sign of the covariance term → risk premium

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing total variance of an asset's return with the relevant risk in C-CAPM → ✅ Correct: Only the covariance with consumption (not total variance) matters for the premium.
- ❌ Mistake: Reading the formula as $\text{Cov}(r, C)$ directly → ✅ Correct: It is $\text{Cov}(r, u'(C))$, which has the opposite sign because $u'' < 0$.

**Quick Recall:**
- Euler under risky return: $u'(C_t) = E_t[(1 + r_{t+1}) u'(C_{t+1})]$
- Risk-free: $1 + i_{t+1} = u'(C_t)/E_t[u'(C_{t+1})]$
- C-CAPM: $E_t[r_{t+1}] - i_{t+1} = -\text{Cov}_t[(1 + r_{t+1}), u'(C_{t+1})]/E_t[u'(C_{t+1})]$
- Higher $\text{Cov}(r, C)$ → higher risk premium
- Builds on: Random Walk Hypothesis framework (uncertainty + Euler equation)
- Generalizes: Standard CAPM by tying risk premia to marginal utility of consumption rather than market portfolio variance

**Quick Recall:**
- Fisher → LCH → PIH → RWH → C-CAPM forms a logical progression
- Each step adds realism: multi-period → systematic income variation → random income → uncertainty + rational expectations → uncertain returns
- All resolve different aspects of the Kuznets puzzle and policy effectiveness
| Version | Decision-maker | Year proposed |
|---------|----------------|---------------|
| Central planner's problem | Social planner allocates resources | Ramsey (1928) |
| Decentralized households' problem | Price-taking households + competitive firms | Cass (1965), Koopmans (1965) |
- **Ramsey-Cass-Koopmans (RCK) model**: An infinite-horizon optimal growth model where the consumption-accumulation path maximizes household utility. ⭐ (exam-important)

### Central Planner's Problem (Setup) 🔴

**Welfare function**
- $c_t$ = per capita consumption in period $t$
- $u(c_t)$ = instantaneous utility
- $\rho > 0$ = subjective discount rate (rate of time preference)

**Why the discount factor $\exp(-\rho t)$?**
- At $t = 0$: $\exp(-\rho \cdot 0) = 1$ → current utility weighted at unity
- At $t = 1$: $\exp(-\rho)$ < 1
- At $t = 2$: $\exp(-2\rho) < \exp(-\rho)$
- Each subsequent period gets exponentially smaller weight: $1 > \exp(-\rho) > \exp(-2\rho) > \cdots$

**Resource constraint (aggregate)**
- $C_t$ = aggregate consumption
- $dK/dt$ = investment (augments capital stock)
- $Y_t$ = total output

**Production technology**
- Continuity, concavity, constant returns to scale (CRS)
- CRS implies per-capita output: $y = F(K/L, 1) = f(k)$
- Marginal products: $\partial F/\partial K = f'(k)$, $\partial F/\partial L = f(k) - kf'(k)$

**Inada conditions**
- $f(0) = 0$ — no production with zero capital
- $\lim_{k \to 0} f'(k) = \infty$ — marginal product of capital infinite at zero capital
- $\lim_{k \to \infty} f'(k) = 0$ — marginal product of capital approaches zero as capital becomes abundant

**Population growth**

**Per capita resource constraint**
- **Subjective discount rate / rate of time preference** ($\rho$): The constant factor representing how much weight the household puts on present vs. future utility. ⭐ (exam-important)
- **Inada conditions**: $f(0) = 0$, $\lim_{k \to 0} f'(k) = \infty$, $\lim_{k \to \infty} f'(k) = 0$ — limiting behavior of the marginal product of capital. ⭐ (exam-important)
- **Per capita capital stock** ($k$): Capital-labor ratio $K/L$.
- Control: $c_t$
- State: $k_t$
- Co-state: $\mu_t$ (shadow price of capital)

**Economic meaning of (ia)**

**Transversality condition (iva)**
- The shadow price of capital $\mu_t \to 0$ (capital has no remaining value), OR
- The capital stock $k_t \to 0$ (no capital left)

**Deriving the consumption growth equation**
- The full steady-state characterization (modified golden rule, phase diagram, saddle path) appears in chunk 003.
- The condition $\mu_t k_t \to 0$ is the infinite-horizon analog of standard transversality conditions.

**Quick Recall:**
- Welfare: $W = \int_0^\infty u(c_t) e^{-\rho t} dt$
- Resource constraint (per cap): $\dot{k}_t = f(k_t) - nk_t - c_t$
- Production: CRS neoclassical, $y = f(k)$
- Inada: $f(0) = 0$, $f'(0) = \infty$, $f'(\infty) = 0$
- Hamiltonian → 4 FOCs (ia–iva)
- Transversality: $\lim \mu_t k_t = 0$
- Co-state $\mu_t$ = shadow price of capital
- Keynes-Ramsey: $\dot{c}/c = (1/\sigma)[f'(k) - n - \rho]$
- Builds on: Solow growth model (same production technology, but optimal saving rate)
- Continues in: Steady-state and saddle-path analysis (Chunk 003)

### Central Planner's Problem — Steady State, Phase Diagram, Modified Golden Rule 🔴

**Two driving equations**
- **Capital dynamics (iiia)**: $\dot{k}_t = f(k_t) - nk_t - c_t$
- **Consumption dynamics (va)** (Keynes-Ramsey): $\dfrac{\dot{c}_t}{c_t} = \dfrac{1}{\sigma}[f'(k_t) - n - \rho]$ where $\sigma = -cu''(c)/u'(c)$

**Phase diagram loci**
- Left of vertical: $\dot{c} > 0$ → $c$ rising over time
- Right of vertical: $\dot{c} < 0$ → $c$ falling
- Below the curve: $\dot{k} > 0$ → $k$ rising
- Above the curve: $\dot{k} < 0$ → $k$ falling

**Steady state**
- $f'(k) = \rho + n$ → defines the **modified golden rule** capital-labor ratio
- $c = f(k) - nk$ → corresponding steady-state per-capita consumption
- Both $c$ and $k$ remain constant over time

**Saddle path**

**Modified golden rule vs. golden rule**
| Concept | Condition | Interpretation |
|---------|-----------|----------------|
| Golden rule | $f'(k_g) = n$ | Maximizes steady-state per-capita consumption |
| Modified golden rule | $f'(k^*) = \rho + n$ | RCK steady state with positive time preference |
- **Steady state**: A long-run equilibrium where the values of the variables remain constant over time. ⭐ (exam-important)
- **Modified golden rule**: The steady-state capital-labor ratio in the RCK model where $f'(k) = \rho + n$ (marginal product of capital equals population growth rate plus rate of time preference). ⭐ (exam-important)
- **Golden rule** capital-labor ratio: The steady-state $k_g$ that maximizes steady-state per-capita consumption, defined by $f'(k_g) = n$. ⭐ (exam-important)
- **Saddle path**: The unique trajectory in the phase diagram that converges to a saddle-point steady state.
- **Saddle point**: A type of steady state with one stable manifold (the saddle path) and one unstable manifold; almost all paths diverge.
1. Plot vertical $\dot{c} = 0$ line at $k^*$
2. Plot inverted-U $\dot{k} = 0$ curve $c = f(k) - nk$
3. Intersection at $E$ — the steady state
4. Direction arrows in each quadrant (NE, NW, SE, SW) show motion of $(c, k)$
5. Saddle path: the unique trajectory that enters $E$
6. Given $k_0$: planner chooses $c_0$ on the saddle path

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing golden rule with modified golden rule → ✅ Correct: Golden rule maximizes steady-state consumption ($f'(k_g) = n$); modified golden rule is the actual RCK steady state with $f'(k^*) = \rho + n > n$.
- ❌ Mistake: Thinking the planner chooses $k_0$ → ✅ Correct: $k_0$ is given; the planner chooses initial $c_0$ to land on the saddle path.
- The saddle-path property is asserted, not proven, in this text.
- A higher rate of time preference $\rho$ leads to *lower* steady-state $c$ and $k$ — impatience comes at the cost of long-run consumption.

**Quick Recall:**
- $\dot{c} = 0$ locus: vertical at $k^*$ where $f'(k^*) = \rho + n$
- $\dot{k} = 0$ locus: inverted-U $c = f(k) - nk$
- Steady state $E$ at intersection — saddle point
- Modified golden rule: $f'(k) = \rho + n$
- Golden rule: $f'(k_g) = n$
- When $\rho > 0$: $k^* < k_g$, $c^* < c_g$
- Builds on: Central planner's setup (Chunk 002)
- Continues into: Decentralized households' problem (next section)

### Decentralized Households' Problem 🔴

**Market structure**
- Two competitive factor markets determine wage rate $w_t$ and rate of return on capital $r_t$
- Many identical competitive firms produce final output using same neoclassical technology as the planner
- Competition: $r_t = f'(k_t)$ and $w_t = f(k_t) - k_t f'(k_t)$ (factors paid marginal products)

**Household assets and budget constraint**

**Optimization problem**

**First-order conditions**

**No-Ponzi-Game (NPG) condition (additional)**

**Consumption growth equation (decentralized)**

**Equivalence under perfect foresight**
- **Perfect foresight** assumption: households cannot derive $w$ and $r$ as functions of $k$, but they exactly guess their values at every point in time.
- In equilibrium, net borrowing across households is zero (identical agents): $a_t = k_t$.
- Substituting $r_t = f'(k_t)$, $w_t = f(k_t) - k_t f'(k_t)$, and $a_t = k_t$ into the household's (iiib) and (vib) yields the **same** system as the planner's.
- Conclusion: optimal consumption-accumulation paths in the decentralized economy coincide with the planner's. Market and planner solutions are identical.
- **No-Ponzi-Game (NPG) condition**: A constraint preventing infinite debt accumulation by requiring the present discounted value of the household's per-capita asset stock to be non-negative as $t \to \infty$. ⭐ (exam-important)
- **Ponzi-game financing**: A scheme of consuming above income forever by perpetually borrowing more, including to repay interest — ruled out by NPG.
- **Perfect foresight**: Assumption that households exactly anticipate future values of prices ($w$, $r$) without errors. ⭐ (exam-important)
- **Arbitrage condition** (in the asset market): physical capital and bonds must earn the same rate of return.
1. Without NPG: household maintains infinite consumption stream by borrowing.
2. Net per-capita borrowing grows exponentially at rate $r - n$ (must borrow for both consumption and interest payments).
3. PDV of net debt → $\infty$. Lenders would never offer such loans.
4. NPG enforces eventual repayment (or non-negative long-run assets in PDV terms).
1. Household FOCs: (ib), (iib), (iiib), (ivb), (vb) → consumption growth (vib).
2. Equilibrium: $a_t = k_t$, $r_t = f'(k_t)$, $w_t = f(k_t) - k_t f'(k_t)$.
3. Substitute into (iiib): $\dot{k}_t = (f(k_t) - k_t f'(k_t)) + (f'(k_t) - n) k_t - c_t = f(k_t) - nk_t - c_t$ — matches planner's (iiia).
4. Substitute into (vib): $\dot{c}_t/c_t = (1/\sigma)[f'(k_t) - n - \rho]$ — matches planner's (va).
5. Same system → same solution.

### ⚠️ Common Mistakes
- ❌ Mistake: Forgetting the NPG condition is *additional* to the standard FOCs → ✅ Correct: For decentralized households (with borrowing), NPG (vb) is required *on top of* (ib)–(ivb).
- ❌ Mistake: Thinking the equivalence holds without perfect foresight → ✅ Correct: Equivalence depends crucially on perfect foresight; with imperfect anticipation, market and planner solutions can diverge.

**Quick Recall:**
- Budget: $\dot{a}_t = w_t + (r_t - n)a_t - c_t$
- FOCs: (ib)–(ivb) + NPG (vb)
- Consumption growth: $\dot{c}/c = (1/\sigma)[r_t - n - \rho]$
- Equilibrium: $a_t = k_t$, $r_t = f'(k_t)$, $w_t = f(k_t) - k_t f'(k_t)$
- Under perfect foresight: market path = planner path
- NPG rules out infinite-debt financing
- Builds on: Central planner's problem (same structure, different setup)
- Foundation for: Government in RCK & Ricardian Equivalence (next section)

### Government in RCK and Ricardian Equivalence 🔴

**Tax-financed government (lump-sum tax $\tau$ per period)**
- Disposable household income: $w_t + r_t a_t - \tau$
- Modified budget constraint: $\dot{a}_t = w_t + (r_t - n)a_t - c_t - \tau$
- Other FOCs unchanged
- Phase diagram: $\dot{k} = 0$ curve shifts *downward* by $\tau$
- New steady state $E'$ (Fig. 9.4): $k$ unchanged, but $c$ lower by $\tau$

**Debt-financed government**

**Ricardian Equivalence**
- **Lump-sum tax**: A tax of fixed amount $\tau$ that does not depend on income or behavior, hence does not distort decisions at the margin.
- **Ricardian Equivalence**: The proposition that, for forward-looking households with perfect foresight, the choice between tax and debt financing of government expenditure has no effect on household consumption or capital accumulation. ⭐ (exam-important)
1. Budget constraint adds $-\tau$ → $\dot{k} = 0$ locus shifts down by $\tau$ (new $c = f(k) - nk - \tau$).
2. The $\dot{c} = 0$ vertical line is unchanged ($f'(k) = \rho + n$ still defines $k^*$).
3. New intersection $E'$: same $k^*$, lower $c^* - \tau$.
1. Government issues bonds today instead of taxing → households' apparent income unchanged today.
2. Government must eventually balance budget → future taxes will rise.
3. Households with perfect foresight know future tax burden → save the windfall to cover it.
4. Net effect: identical to immediate taxation.

### ⚠️ Common Mistakes
- ❌ Mistake: Believing debt financing stimulates consumption (vs. tax financing) → ✅ Correct: Under Ricardian Equivalence with perfect foresight, the two are identical.
- ❌ Mistake: Assuming Ricardian Equivalence holds in all real-world settings → ✅ Correct: Requires perfect foresight; can fail with myopic agents, liquidity constraints, or finite horizons (relevant for OLG model — Unit 10).
- The result depends on lump-sum (non-distorting) taxes. Distortionary taxes break the equivalence.
- Requires that government's lifetime budget constraint binds (eventually).

**Quick Recall:**
- Lump-sum tax: $k$ unchanged at steady state, $c$ falls by $\tau$
- Phase diagram: $\dot{k} = 0$ shifts down by $\tau$
- Ricardian Equivalence: tax = debt financing under perfect foresight
- Households save windfall from debt financing to cover future taxes
- Requires perfect foresight (fails in OLG and other settings)
- Builds on: Decentralized households' problem (Chunk 003)
- Compare with: OLG model (Chunk 004) — Ricardian Equivalence breaks down with finite-life selfish generations

**Quick Recall:**
- Optimal path = saddle path → steady state $E$
- Steady state: modified golden rule $f'(k) = \rho + n$
- Centralized = decentralized under perfect foresight
- Lump-sum tax → lower $c^*$, same $k^*$
- Ricardian Equivalence: tax = debt financing
- **Hamiltonian function**: $H = F(u, x, t) + \mu \cdot f(u, x, t)$ — packages payoff and constraint for dynamic optimization. ⭐ (exam-important)
- **Co-state variable** ($\mu$): Continuous-time analog of a Lagrange multiplier; measures the marginal value of the state variable. ⭐ (exam-important)
- **Transversality condition**: A terminal condition on the co-state and state variable; $\mu_T x_T = 0$ (finite horizon) or $\lim_{t \to \infty} \mu_t x_t = 0$ (infinite horizon). ⭐ (exam-important)
- **Pontryagin's Maximum Principle**: The set of necessary conditions for optimal control problems, characterizing optimal paths via the Hamiltonian. ⭐ (exam-important)

**Quick Recall:**
- Hamiltonian: $H = F(u, x, t) + \mu \cdot f(u, x, t)$
- FOCs: max $H$ w.r.t. $u$; $-\dot{\mu} = \partial H/\partial x$; $\dot{x} = \partial H/\partial \mu$
- Transversality: $\mu_T x_T = 0$ (finite); $\lim \mu_t x_t = 0$ (infinite)
- Co-state $\mu$ = shadow price of state
- **Overlapping Generations (OLG) framework**: A model where individuals have finite (typically two-period) lives and at each point in time the lifetimes of two successive generations overlap. ⭐ (exam-important)

### Structure of the OLG Model 🔴

**Individual budget constraints**
- **Period 1 (young)**: $c_{1t} + s_t = w_t$ — wage is split between consumption and savings
- **Period 2 (old)**: $c_{2t+1} = (1 + r_{t+1}) s_t$ — savings plus interest funds retirement consumption
- $c_{1t}$ = first-period (young) consumption of generation $t$
- $c_{2t+1}$ = second-period (old) consumption of generation $t$ (occurring in period $t+1$)
- $w_t$ = wage rate when young
- $r_{t+1}$ = interest rate on savings when old

**Lifetime budget constraint**

**Two-period utility maximization**
1. $\dfrac{U_1}{U_2} = (1 + r_{t+1})$ — MRS equals price ratio
2. $c_{1t} + \dfrac{c_{2t+1}}{1 + r_{t+1}} = w_t$ — budget binds

**Population growth**

**Production side**

**Aggregating consumption across generations**
- $L_{t-1}$ old people each consume $c_{2t}$ → $L_{t-1} c_{2t} = (1 + r_t) K_t$ (old fully consume their interest plus capital — they die at end of period, no bequest)
- $L_t$ young people each consume $c_{1t}$ → $L_t c_{1t} = L_t w_t - L_t s_t$
- Aggregate consumption: $C_t = L_t c_{1t} + L_{t-1} c_{2t}$

**Goods market equilibrium → basic dynamic equation**
- **Bequest**: A transfer of wealth from one generation to the next. In the standard OLG model, there is no bequest — the old fully consume their wealth.
- **Basic dynamic equation (OLG)**: $k_{t+1} = s(w(k_t), r(k_{t+1}))/(1+n)$ — links tomorrow's capital-labor ratio to today's. ⭐ (exam-important)
- **Savings function**: $s_t = s(w_t, r_{t+1})$, derived from individual two-period utility maximization.
1. The young earn $w_t L_t$ in total wages, consume $L_t c_{1t}$, save $L_t s_t$.
2. The old fully consume capital + interest: $L_{t-1} c_{2t} = (1 + r_t) K_t$.
3. Goods market: $C_t + (K_{t+1} - K_t) = Y_t = w_t L_t + r_t K_t$.
4. Substitute: $L_t c_{1t} + L_{t-1} c_{2t} + K_{t+1} - K_t = w_t L_t + r_t K_t$
5. Simplify using $L_{t-1} c_{2t} = (1 + r_t) K_t$ and $L_t c_{1t} = L_t w_t - L_t s_t$:
6. → $K_{t+1} = L_t s_t$. ✓

**Slope of the dynamic equation**
- Under "consumption is normal in both periods" assumption: $0 < s_w < 1$ ✓
- $s_r$ has ambiguous sign: substitution effect of higher $r$ raises savings, income effect lowers savings
  - If income effect dominates: $s_r < 0$
  - If substitution effect dominates: $s_r > 0$
- The text assumes substitution effect dominates → $s_r > 0$ → $k_{t+1}$ line is positively sloped

**Multiple steady states (Fig. 10.1)**
- $k_{t+1}$ line crosses 45° from *above* → locally stable equilibrium
- $k_{t+1}$ line crosses 45° from *below* → locally unstable equilibrium

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking the new capital comes from the old's savings → ✅ Correct: The old fully consume; only the young's savings become next period's capital.
- ❌ Mistake: Believing $s_w > 1$ is possible → ✅ Correct: With both consumptions normal goods, $0 < s_w < 1$.
- ❌ Mistake: Assuming $s_r > 0$ always → ✅ Correct: $s_r$ depends on which of income/substitution effect dominates.
- The slope analysis depends on the assumption that the substitution effect dominates the income effect for savings ($s_r > 0$).
- Multiple equilibria possible depending on the curvature of $k_{t+1}(k_t)$.
- The "no bequest" assumption is what makes generations effectively selfish — central to dynamic inefficiency.

**Quick Recall:**
- Young: $c_{1t} + s_t = w_t$
- Old: $c_{2t+1} = (1 + r_{t+1}) s_t$
- Lifetime BC: $c_{1t} + c_{2t+1}/(1 + r_{t+1}) = w_t$
- FOC: $U_1/U_2 = (1 + r_{t+1})$
- Capital evolves: $K_{t+1} = L_t s_t$ → $k_{t+1} = s(w(k_t), r(k_{t+1}))/(1+n)$
- Multiple steady states possible
- Cross-from-above → stable; cross-from-below → unstable
- Builds on: Two-period utility maximization (similar to Fisher, Chunk 001) but with explicit production
- Compare with: Ramsey-Cass-Koopmans (infinite-life dynasty vs. two-period selfish individuals)
- Foundation for: Dynamic inefficiency analysis (next section)

### Dynamic Inefficiency in OLG 🔴

**Pareto efficiency in steady-state comparison**

**Golden rule**

**Two regions:**
- **Right of $k_g$ (i.e., $k > k_g$): dynamically inefficient region**
  - Capital is over-accumulated
  - If people consumed part of their savings in period 1, $k$ would fall toward $k_g$ AND lifetime utility would rise
  - Pareto improvement: can raise current consumption *without* sacrificing future consumption
  - These are **dynamically inefficient** points
- **Left of $k_g$ (i.e., $k < k_g$): dynamically efficient region**
  - To move toward $k_g$, must save more (forgo current consumption) — a real cost
  - Cannot say definitively whether moving is welfare-improving (current loss vs. future gain)
  - All points are **Pareto efficient** / dynamically efficient

**RCK steady state is always dynamically efficient**

**OLG steady state can be dynamically inefficient**
- **Dynamic efficiency**: A property of an equilibrium where current consumption cannot be increased without reducing future consumption. ⭐ (exam-important)
- **Dynamic inefficiency**: A situation (possible in OLG but not RCK) where the economy has over-accumulated capital — current consumption can be raised *without* sacrificing future consumption, yielding a Pareto improvement. ⭐ (exam-important)
- **Golden rule capital-labor ratio** ($k_g$): The steady-state $k$ that maximizes per-capita steady-state utility, satisfying $f'(k_g) = n$.
1. Individuals in OLG are selfish — no bequest to next generation.
2. They do not share the benefits of investment with future generations (who grow at rate $n$).
3. When valuing return on investment, the relevant return for each individual is just $f'(k)$ — *not net of $n$*.
4. They will invest as long as $f'(k) > 0$, even when $f'(k) < n$.
5. → Over-saving relative to the social optimum.
- Utility: $U(c_{1t}, c_{2t+1}) = \ln c_{1t} + \beta \ln c_{2t+1}$, $0 < \beta < 1$
- Production: $f(k_t) = A k_t^\alpha$, $0 < \alpha < 1$ (Cobb-Douglas)
1. $\dfrac{c_{2t+1}}{c_{1t}} = \beta(1 + r_{t+1})$
2. $c_{1t} + \dfrac{c_{2t+1}}{1 + r_{t+1}} = w_t$

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing dynamic inefficiency with simple welfare loss → ✅ Correct: Specifically means a Pareto improvement is possible by *reducing* savings.
- ❌ Mistake: Thinking dynamic inefficiency means too *little* savings → ✅ Correct: It means too *much* savings — over-accumulation.
- ❌ Mistake: Assuming RCK can be dynamically inefficient too → ✅ Correct: RCK steady state is always to the *left* of $k_g$ (since $\rho > 0$), so always dynamically efficient.
- Dynamic inefficiency in OLG is parameter-dependent — not guaranteed. Depends on utility, production technology, and growth rate.
- Even if the steady state is unique and stable, it can still be inefficient.

**Quick Recall:**
- Golden rule: $f'(k_g) = n$
- $k > k_g$: dynamically inefficient (over-saving)
- $k < k_g$: dynamically efficient
- RCK steady state: $f'(k^*) = \rho + n > n$ → always efficient
- OLG steady state: can be either; condition $\frac{\beta(1-\alpha)}{1+\beta} > \frac{\alpha(1+n)}{n}$ in CD example
- Cause: selfish OLG individuals don't account for population growth
- Builds on: Structure of OLG model (previous section); golden rule (Chunk 003)
- Contrasts with: RCK steady state (always efficient, Chunk 003)
- Foundation for: Social security analysis (next section)

### Social Security 🔴

**Fully funded social security**

**Pay-as-you-go (PAYG) social security**
| System | Rate of return on contribution |
|--------|--------------------------------|
| Fully funded | $r$ (capital return) |
| Pay-as-you-go | $n$ (population growth rate) |
- If $r > n$: private savings have higher return → people prefer to save privately → PAYG less attractive
- If $r < n$ (the dynamically inefficient case): PAYG offers a *higher* return than private savings → people save less privately and contribute more to PAYG → reduces capital accumulation → economy moves toward dynamic efficiency
- **Social security programme**: A government scheme that provides income to individuals after retirement.
- **Fully funded social security**: A system where contributions made by individuals when young are invested and returned with interest to the same individuals when old. ⭐ (exam-important)
- **Pay-as-you-go (PAYG) social security**: A system where contributions from current workers are immediately transferred to current retirees; effective rate of return is the population growth rate $n$. ⭐ (exam-important)
1. Young pay $d_t$, government invests it, returns $(1 + r_{t+1}) d_t$ when they're old.
2. Individual's effective savings: $s_t + d_t$; effective consumption when old: $(1 + r_{t+1})(s_t + d_t)$.
3. Individual chooses optimal total: $s_t^{old} = s_t + d_t$ → cuts private $s_t$ by exactly $d_t$.
4. Net effect on aggregate: 0.
1. Young pay $d_t$ → immediately given to old → $b_t = (1 + n) d_t$.
2. Effective return on contribution = $n$ (vs. $r$ for private capital).
3. If $r < n$ (dynamic inefficiency): individuals prefer higher-return PAYG, save less privately.
4. Lower $s_t$ → lower $K_{t+1}$ → $k$ falls toward $k_g$ → dynamic efficiency restored.

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking both social security systems are equivalent → ✅ Correct: Fully funded is neutral; PAYG affects behavior because effective return differs from $r$.
- ❌ Mistake: Believing PAYG always reduces capital → ✅ Correct: It does so only in dynamically inefficient regions where $r < n$. In dynamically efficient regions, effects can differ.
- ❌ Mistake: Calling the result a violation of Ricardian Equivalence → ✅ Correct: It is — Ricardian Equivalence breaks down in OLG because each generation is finite-lived and selfish, so debt/transfers across generations have real effects.
- Fully funded results assume government earns same return as private investment.
- PAYG's efficiency gain depends on $r < n$ holding — not always true.
- Real-world systems are mixed and have many complications (myopia, liquidity constraints).

**Quick Recall:**
- Fully funded: $b_{t+1} = (1 + r_{t+1}) d_t$ — same return as private capital
- PAYG: $b_t = (1 + n) d_t$ — effective return = $n$
- Fully funded: neutral (offset by reduced private saving)
- PAYG: reduces private savings if $r < n$ → fixes dynamic inefficiency
- PAYG works precisely because Ricardian Equivalence fails in OLG
- Builds on: Dynamic inefficiency analysis (previous section)
- Contrasts with: Ricardian Equivalence in RCK (Chunk 003) — debt-financed government is neutral there but transfers can have real effects in OLG

**Quick Recall:**
- Basic dynamic equation: $K_{t+1} = L_t s_t$
- Per-capita: $k_{t+1} = s/(1+n)$
- Steady state: possibly dynamically inefficient
- Fully funded SS: no effect on capital
- PAYG SS: reduces capital if $r < n$ → eliminates inefficiency
