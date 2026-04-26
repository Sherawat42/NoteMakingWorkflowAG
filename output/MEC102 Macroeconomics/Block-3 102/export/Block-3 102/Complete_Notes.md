# Complete Notes


## Section: Introduction — The Consumption Puzzle 🟢

### Core Idea
Economic decisions about consumption and savings are inherently inter-temporal — they depend on past, current, and expected future variables. Keynes treated current income as the prime determinant of current consumption, giving a falling average propensity to consume (APC) as income rises. Cross-sectional data initially supported this, but Kuznets (1940s) found that long-run aggregate APC stayed roughly constant despite huge income growth — a puzzle that motivated all the modern intertemporal theories of consumption that this unit covers.

> **In Simple Terms:** Imagine snapshotting many households today — rich families look like they save more of every rupee than poor families, supporting Keynes. But zoom out across decades for the whole country, and the saving rate barely moves. That contradiction is the puzzle every theory in this unit tries to resolve.

### Key Concepts

#### Keynesian consumption function
A simple linear relationship: $C_t = \bar{C} + cY_t$, with $\bar{C} > 0$ and $0 < c < 1$. The average propensity to consume $C_t/Y_t$ falls as income rises because the autonomous component $\bar{C}$ becomes a smaller share of income.

#### The cross-section vs. time-series discrepancy
Cross-sectional household data shows richer households consume a smaller fraction of income. Long-run time series data (Kuznets) shows aggregate APC is essentially constant. This empirical puzzle is what the Life-Cycle Hypothesis, Permanent Income Hypothesis, and Random Walk Hypothesis all attempt to explain.

### Definitions
- **Inter-temporal decision making**: Decisions of an economic agent that involve different periods of time, where current actions depend on past states and future expectations.
- **Average propensity to consume (APC)**: The ratio $C_t/Y_t$ — share of current income that is consumed.

> **Quick Recall:**
> - Keynes: $C_t = \bar{C} + cY_t$ → APC falls as $Y_t$ rises
> - Cross-section data: APC falls with income (matches Keynes)
> - Time-series data (Kuznets): APC constant over long run (contradicts Keynes)
> - Puzzle drives the whole unit

---

## Section: Fisher's Two-Period Intertemporal Choice Model 🔴

### Core Idea
Irving Fisher (1930) recast consumption as the outcome of a two-period utility-maximization exercise. Each individual lives for two periods, gets income in each, can save period-1 income at interest rate $r$, and chooses $C_1$ and $C_2$ to maximize lifetime utility subject to a single intertemporal budget constraint. The optimal current consumption depends on the present discounted value of lifetime income and on the interest rate — not just current income.

> **In Simple Terms:** You earn money this year and next year. You decide today how much to spend now versus save for later, knowing savings grow with interest. Fisher's insight: today's consumption is shaped by your *whole* lifetime income picture, not just this year's paycheck.

### Key Concepts

#### Two-period setup
Person lives 2 periods (period 1 = youth, period 2 = old age, broadly defined). Utility function $U(C_1, C_2)$. Income $Y_1$ in period 1, $Y_2$ in period 2. Period-1 saving $S_1 = Y_1 - C_1$ earns interest, so $C_2 = Y_2 + (1+r)S_1$.

#### Intertemporal budget constraint (IBC)
By rearranging $C_2 = Y_2 + (1+r)(Y_1 - C_1)$:
$$C_1 + \frac{C_2}{1+r} = Y_1 + \frac{Y_2}{1+r} \equiv \hat{Y}$$
- Left side: present discounted value (PDV) of total lifetime consumption
- Right side: PDV of total lifetime income ($\hat{Y}$)
- Optimal $C_1$ is a function of $\hat{Y}$ and $r$

#### Geometry of optimization (Fig. 8.1)
Plotting $C_1$ on y-axis, $C_2$ on x-axis: the budget line crosses the x-axis at $(1+r)Y_1 + Y_2$ (when $C_1 = 0$) and the y-axis at $Y_1 + Y_2/(1+r)$ (when $C_2 = 0$). The optimum E is the tangency between the IBC and the highest indifference curve $U(C_1, C_2)$.

### Definitions
- **Intertemporal budget constraint (IBC)**: $C_1 + \dfrac{C_2}{1+r} = Y_1 + \dfrac{Y_2}{1+r}$ — present discounted value of lifetime consumption equals present discounted value of lifetime income. ⭐ (exam-important)
- **Present discounted value (PDV)**: Today's value of future flows discounted at the interest rate.
- **Lifetime income** ($\hat{Y}$): The PDV of all current and future income.

### Mechanisms / Processes
**Effect of an increase in current income $Y_1$**, ceteris paribus:
1. $\hat{Y}$ rises → IBC shifts outward
2. If $C_1$ and $C_2$ are both normal goods → both $C_1$ and $C_2$ increase
3. Income effect → unambiguous: $C_1 \uparrow$

**Effect of an increase in interest rate $r$** on $C_1$ — ambiguous, two opposing effects:
| Effect | Direction on $C_1$ | Reasoning |
|--------|--------------------|-----------|
| Income effect | $C_1 \uparrow$ | Higher $r$ means same savings buys more future consumption — feels richer, broader choice set |
| Substitution effect | $C_1 \downarrow$ | Future consumption is now relatively cheaper → substitute toward $C_2$ |

Net effect on $C_1$:
- Income effect dominates → $C_1 \uparrow$
- Substitution effect dominates → $C_1 \downarrow$

Same logic applies to savings $S_1 = Y_1 - C_1$: ambiguous, depends on which effect dominates.

### Examples
**Example: Reading the IBC intercepts (Fig. 8.1)**
- Set $C_1 = 0$ in the IBC: $C_2/(1+r) = Y_1 + Y_2/(1+r)$ → $C_2 = (1+r)Y_1 + Y_2$
- Set $C_2 = 0$ in the IBC: $C_1 = Y_1 + Y_2/(1+r)$
- These give the x- and y-intercepts of the budget line.

### ⚠️ Common Mistakes
- ❌ Mistake: Assuming a higher $r$ always raises savings → ✅ Correct: Effect on savings is ambiguous; depends on relative strength of income vs. substitution effect.
- ❌ Mistake: Treating Fisher's model as just about current income → ✅ Correct: Current consumption depends on PDV of *lifetime* income $\hat{Y}$ and on $r$, not just $Y_1$.

### Edge Cases & Caveats
- The interest rate $r$ here is strictly the *expected* future rate of interest expected to prevail in period 2. The simple model assumes the future is certain and known.

> **Quick Recall:**
> - IBC: $C_1 + C_2/(1+r) = Y_1 + Y_2/(1+r) = \hat{Y}$
> - $\Delta Y_1 \uparrow$ → $C_1 \uparrow$, $C_2 \uparrow$ (both normal)
> - $\Delta r \uparrow$ → effect on $C_1$ ambiguous (income vs. substitution)
> - Same ambiguity for savings

### Connections
- Foundation for: Life Cycle Hypothesis, Permanent Income Hypothesis, Random Walk Hypothesis (all extend Fisher's intertemporal logic)

---

## Section: Life Cycle Hypothesis (Modigliani–Brumberg) 🔴

### Core Idea
Modigliani and Brumberg (1954) extended Fisher's two-period model to a T-period horizon. With diminishing marginal utility and a zero interest rate (for simplicity), the optimal consumption is **constant across all periods** — the individual smooths consumption equally over the entire life. Income, however, varies systematically over the life cycle (low when young, high in middle age, low when old). Households save during high-income middle years and dissave at the start and end of life.

> **In Simple Terms:** Even though you earn very little as a student, lots in your prime working years, and nothing in retirement, you don't want your consumption to swing along with that. So you borrow when young, save in middle age, and run down savings when old — keeping consumption smooth.

### Key Concepts

#### T-period model setup
Each person lives T periods ($T \geq 2$). Additive utility:
$$U(C_1, C_2, \ldots, C_T) = u(C_1) + u(C_2) + \cdots + u(C_T) = \sum_{t=1}^{T} u(C_t)$$
Utility is well-behaved: $u' > 0$, $u'' < 0$ (positive but diminishing marginal utility). Assume $r = 0$ for simplicity (positive $r$ doesn't change the qualitative result).

#### Intertemporal budget constraint (T periods, $r = 0$)
$$\sum_{t=1}^{T} C_t = A_0 + \sum_{t=1}^{T} Y_t$$
where $A_0$ is the initial wealth stock.

#### Consumption smoothing result
The Lagrangian first-order conditions give $u'(C_1) = u'(C_2) = \cdots = u'(C_T) = \lambda$, which (since $u$ is strictly concave) implies:
$$C_1 = C_2 = \cdots = C_T$$
Combined with the IBC:
$$C_t = \frac{1}{T}\left(A_0 + \sum_{t=1}^{T} Y_t\right) = \frac{A_0 + \hat{Y}}{T} \quad \text{for all } t$$
This is **consumption smoothing**: lifetime resources spread equally across all periods.

#### Implication for current income
A change in current income $Y_t$ affects $C_t$ only through its effect on average lifetime income $\hat{Y}/T$:
- If $Y_t$ rises by $Z$ in one period only → $C_t$ rises by only $Z/T$
- If $Y_t$ rises by $Z$ now and falls by $Z$ later (so lifetime income unchanged) → $C_t$ does not change in any period

#### Savings function (from LCH)
$$S_t = Y_t - \frac{1}{T}\sum_{t=1}^T Y_t - \frac{A_0}{T}$$
Savings are high when current income is high relative to *average* lifetime income.

#### Income–consumption pattern over the lifetime (Fig. 8.2)
- Income $Y_t$: low at young ages (low productivity), peaks in middle age, falls again in old age
- Consumption $C_t$: flat across the entire life
- Result: dissave when young (run down $A_0$ or borrow); save in middle years; dissave again in old age (run down accumulated wealth)

### Definitions
- **Consumption smoothing**: Spreading lifetime resources equally across all periods so consumption is constant even when income varies. ⭐ (exam-important)
- **Life Cycle Hypothesis (LCH)**: Modigliani–Brumberg's theory that households smooth consumption over the life cycle by saving during high-income middle years and dissaving in early and late years. ⭐ (exam-important)

### Mechanisms / Processes
**Solving the Lagrangian** (T-period, $r = 0$):
$$\mathcal{L} = \sum_{t=1}^T u(C_t) + \lambda\left[A_0 + \sum_{t=1}^T Y_t - \sum_{t=1}^T C_t\right]$$
F.O.C: $u'(C_t) = \lambda$ for all $t$ → $u'(C_1) = u'(C_2) = \cdots$ → $C_1 = C_2 = \cdots = C_T$ → equal-share rule for $C_t$.

### Examples
**Example: One-period income shock**
A worker receives a one-time bonus $Z$ in period $\hat{t}$, with no change to other periods' incomes. By LCH, their consumption rises by only $Z/T$ in that period (and by $Z/T$ in every other period too — since the bonus raises lifetime income). Most of the bonus goes into savings.

**Example: Compensated income shift**
$Y_t$ rises by $Z$ today, $Y_{t+5}$ falls by $Z$ five periods later. Lifetime income $\hat{Y}$ is unchanged → $C_t$ does not change in any period.

### How LCH solves the Kuznets puzzle
- **Cross-sectional data**: At one point in time, the high-income category disproportionately contains middle-aged people (high income relative to their average lifetime income → high savings rate, low APC). The low-income category disproportionately contains young/old people (low income relative to lifetime average → high APC). So cross-section shows falling APC with income.
- **Time-series (long-run)**: As aggregate income rises over decades, the asset stock $A_0$ rises along with it (positively correlated). The short-run consumption line shifts upward over time (Fig. 8.3), so the long-run locus traced through points like A, B, C is steeper and exhibits a constant APC ($C_t$ proportional to $Y_t$).

### Edge Cases & Caveats
- Result $C_1 = C_2 = \cdots = C_T$ depends on the assumption $r = 0$ and on time-additive utility with no discounting — qualitatively, smoothing logic survives generalization, but the exact equality does not.
- Initial asset stock $A_0$ matters — higher $A_0$ raises consumption in every period.

> **Quick Recall:**
> - Optimal: $C_t = (A_0 + \hat{Y})/T$ for all $t$ — flat consumption
> - $S_t = Y_t - \hat{Y}/T - A_0/T$ — save when current income > lifetime average
> - Income hump-shaped over life; consumption flat → dissave young + old, save middle
> - Cross-section APC ↓ because middle-aged dominate high-income group
> - Time-series APC constant because asset stock rises with income

### Connections
- Builds on: Fisher's intertemporal choice (extends 2-period to T-period)
- Compare with: Permanent Income Hypothesis (alternative explanation, different income process)

---

## Section: Permanent Income Hypothesis (Friedman) 🔴

### Core Idea
Friedman (1957) also resolves the Kuznets puzzle through Fisher's intertemporal framework, but rejects LCH's regular life-cycle income pattern. Instead, individuals face *random and temporary* income fluctuations. He splits current income into a **permanent** component (long-run average) and a **transitory** component (random deviation). Current consumption depends only on permanent income — transitory shocks don't move consumption.

> **In Simple Terms:** If you got a one-time bonus this month, you wouldn't suddenly multiply your monthly spending. You'd treat that bonus as a windfall and largely save it. Friedman says people consume based on what they think their "normal" income is, not what happens to land in their account this period.

### Key Concepts

#### Decomposition of current income
$$Y_t = Y_t^P + Y_t^T$$
- $Y_t^P$ = **permanent income** = long-run average income, $\dfrac{1}{T}\sum_{t=1}^T Y_t$
- $Y_t^T$ = **transitory income** = random deviation, $Y_t - \dfrac{1}{T}\sum_{t=1}^T Y_t$
- Positive $Y_t^T$: current income exceeds permanent → windfall
- Negative $Y_t^T$: current income falls short of permanent → temporary dip

#### Consumption depends only on permanent income
$$C_t = \frac{A_0}{T} + \frac{1}{T}\sum_{t=1}^T Y_t = \frac{A_0}{T} + Y_t^P$$
Any change in transitory income $Y_t^T$ that leaves $Y_t^P$ unchanged has **no impact** on $C_t$.

#### APC and the $Y^P/Y$ ratio
APC depends on the ratio $Y_t^P / Y_t$:
- When current income temporarily rises above permanent ($Y_t^T > 0$, so $Y_t^P/Y_t < 1$) → APC falls
- When current income temporarily falls below permanent → APC rises

### Definitions
- **Permanent income** ($Y^P$): The long-run average income an individual expects to prevail. ⭐ (exam-important)
- **Transitory income** ($Y^T$): Random deviation of current income from permanent income; can be positive or negative. ⭐ (exam-important)
- **Permanent Income Hypothesis (PIH)**: Friedman's theory that current consumption depends only on permanent (long-run average) income, not on transitory deviations. ⭐ (exam-important)

### How PIH solves the Kuznets puzzle
- **Cross-sectional data**: The high-income group at any point in time disproportionately contains people with positive transitory income (lucky this year) → their APC is below average. The low-income group disproportionately contains people with negative transitory income → APC above average. So the cross-section shows falling APC with income.
- **Time-series (long-run)**: Random transitory shocks average out across many people and many years. Long-run income changes reflect changes in *permanent* income, so APC stays constant.

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing LCH and PIH because both resolve the same puzzle → ✅ Correct: LCH posits a *systematic* hump-shaped life-cycle income; PIH posits *random* temporary deviations from a long-run average.
- ❌ Mistake: Thinking a transitory income increase boosts current consumption → ✅ Correct: Under PIH, $C_t$ depends only on $Y_t^P$; transitory income changes do not move $C_t$.

> **Quick Recall:**
> - $Y_t = Y_t^P + Y_t^T$
> - $C_t = A_0/T + Y_t^P$ — consumption depends only on permanent income
> - APC = $C_t/Y_t$ depends on $Y_t^P/Y_t$
> - Cross-section: high-income group has positive $Y^T$ → low APC
> - Long run: transitory shocks average out → constant APC

### Connections
- Builds on: Fisher's intertemporal choice (consumption depends on lifetime/long-run income)
- Compare with: Life Cycle Hypothesis (alternative explanation of the same puzzle)
- Foundation for: Random Walk Hypothesis (Hall extends PIH under uncertainty + rational expectations)

---

## Section: Setup for Consumption under Uncertainty (Hall's Random Walk Hypothesis — Setup) 🔴
<!-- Continues in chunk 002 -->

### Core Idea
PIH so far assumed permanent income is known with certainty. In reality there is uncertainty. The natural extension is for individuals to maximize *expected* utility subject to the constraint that *expected* total consumption equals *expected* total lifetime income. Combining this with rational expectations leads to Hall's (1978) Random Walk Hypothesis: changes in consumption over time are unpredictable.

> **In Simple Terms:** If your income next year is uncertain, you make consumption plans based on your best guess about lifetime income. Whenever you get *new* information, you update. Hall's insight: if your initial plan was already optimal, the only thing that can change your consumption tomorrow is news you couldn't have predicted today — pure surprise.

### Key Concepts

#### Maximization problem under uncertainty
Objective:
$$E[U] = E[u(C_1)] + E[u(C_2)] + \cdots + E[u(C_T)] = \sum_{t=1}^T E[u(C_t)]$$
Constraint:
$$\sum_{t=1}^T E(C_t) = A_0 + \sum_{t=1}^T E(Y_t)$$

#### Optimality condition under rational expectations
Decisions made at $t = 1$ use information available at $t = 1$. The agent equates expected marginal utilities across periods:
$$u'(C_1) = E_1[u'(C_2)] = E_1[u'(C_3)] = \cdots = E_1[u'(C_T)]$$
(Consumption in period 1 is a certain event from the perspective of period 1, so $E_1[u'(C_1)] = u'(C_1)$.)

#### Quadratic utility — closed-form result
With quadratic utility $u(C_t) = C_t - \dfrac{a}{2}C_t^2$, marginal utility is linear: $u'(C_t) = 1 - aC_t$. Then:
$$E_1[u'(C_t)] = 1 - aE_1[C_t]$$
Substituting into the optimality condition:
$$1 - aC_1 = 1 - aE_1[C_2] = 1 - aE_1[C_3] = \cdots$$
Simplifying:
$$C_1 = E_1[C_2] = E_1[C_3] = \cdots = E_1[C_T]$$
The expectation as of period 1 of every future consumption equals current consumption $C_1$.

### Definitions
- **Rational expectations**: A theory in which agents' expectations do not differ systematically from realized outcomes — agents use all available information optimally. ⭐ (exam-important)

### Mechanisms / Processes
**Logical chain**:
1. Permanent income is uncertain
2. Maximize expected utility subject to expected lifetime budget
3. Optimality: $u'(C_1) = E_1[u'(C_t)]$ for all $t$
4. Apply rational expectations: actual $C_t$ = expected $C_t$ + random surprise
5. → Changes in consumption are unpredictable (full random walk result derived in chunk 002)

### Edge Cases & Caveats
- Quadratic utility is a strong assumption used to get the clean linear result; the qualitative random-walk result holds more generally but requires more careful approximation.
- The full random walk equation $C_{t+1} = C_t + e_{t+1}$ and its policy implications are derived in chunk 002.

> **Quick Recall:**
> - Under uncertainty: maximize $E[U] = \sum E[u(C_t)]$
> - Optimality: $u'(C_1) = E_1[u'(C_t)]$ for all future $t$
> - Quadratic utility ⇒ $C_1 = E_1[C_2] = E_1[C_3] = \cdots$
> - Sets up Hall's random walk result (full derivation in chunk 002)

### Connections
- Builds on: Permanent Income Hypothesis (Friedman) — extends PIH to uncertain environment
- Continues in: Random Walk Hypothesis derivation and policy implications (Chunk 002: Random Walk Hypothesis (Hall) — Full Derivation and Policy Implications)


---


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
- Builds on: Permanent Income Hypothesis under uncertainty (Chunk 001: Introduction — The Consumption Puzzle)
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
- Continues in: Steady-state and saddle-path analysis (Chunk 003: Central Planner's Problem — Steady State, Phase Diagram, Modified Golden Rule)


---


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
- Builds on: Central planner's setup (Chunk 002: Random Walk Hypothesis (Hall) — Full Derivation and Policy Implications)
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
- Builds on: Decentralized households' problem (Chunk 003: Central Planner's Problem — Steady State, Phase Diagram, Modified Golden Rule)
- Compare with: OLG model (Chunk 004: Structure of the OLG Model) — Ricardian Equivalence breaks down with finite-life selfish generations

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
- Continues into: Structure of the model + Dynamic Inefficiency + Social Security (Chunk 004: Structure of the OLG Model)


---


## Section: Structure of the OLG Model 🔴
<!-- See chunk 003 for the introduction to the OLG framework -->

### Core Idea
A representative member of generation $t$ is born with one unit of labor, works only when young (period $t$), saves a portion of his wage, and consumes the rest. When old (period $t+1$), he no longer works but consumes his savings plus interest. Two-period utility maximization yields optimal consumption and savings as functions of the wage rate $w_t$ and next-period interest rate $r_{t+1}$. Aggregating across the young and old generations alive at period $t$, plus a neoclassical CRS production technology, gives the **basic dynamic equation** $k_{t+1} = s(w(k_t), r(k_{t+1}))/(1+n)$ — a first-order non-linear difference equation in the capital-labor ratio.

> **In Simple Terms:** Each person works hard while young, parks savings as investment, then lives off those savings when old. Add up everyone's savings (the young) and the dying old people's consumption of capital — and the new capital stock for tomorrow comes purely from today's young people's savings. Trace this rule period by period and you get the long-run dynamics of the economy.

### Key Concepts

#### Individual budget constraints
- **Period 1 (young)**: $c_{1t} + s_t = w_t$ — wage is split between consumption and savings
- **Period 2 (old)**: $c_{2t+1} = (1 + r_{t+1}) s_t$ — savings plus interest funds retirement consumption

where:
- $c_{1t}$ = first-period (young) consumption of generation $t$
- $c_{2t+1}$ = second-period (old) consumption of generation $t$ (occurring in period $t+1$)
- $w_t$ = wage rate when young
- $r_{t+1}$ = interest rate on savings when old

#### Lifetime budget constraint
Eliminating $s_t = c_{2t+1}/(1 + r_{t+1})$ gives:
$$c_{1t} + \frac{c_{2t+1}}{1 + r_{t+1}} = w_t$$
The PDV of lifetime consumption equals the wage income (no other income).

#### Two-period utility maximization
Maximize $U(c_{1t}, c_{2t+1})$ subject to the lifetime budget constraint. FOCs:
1. $\dfrac{U_1}{U_2} = (1 + r_{t+1})$ — MRS equals price ratio
2. $c_{1t} + \dfrac{c_{2t+1}}{1 + r_{t+1}} = w_t$ — budget binds

Solving gives: $c_{1t} = c_1(w_t, r_{t+1})$, $c_{2t+1} = c_2(w_t, r_{t+1})$, and consequently $s_t = s(w_t, r_{t+1})$.

#### Population growth
$L_t$ = number of people in generation $t$, with $L_t = (1+n) L_{t-1}$. Total population alive at period $t$ is $L_t + L_{t-1}$.

#### Production side
Single final good produced via $Y_t = F(K_t, L_t)$ with neoclassical CRS technology (same as RCK). Per-capita: $y = f(k)$ with Inada conditions.

Competitive markets: $w_t = f(k_t) - k_t f'(k_t)$ and $r_t = f'(k_t)$.

#### Aggregating consumption across generations
- $L_{t-1}$ old people each consume $c_{2t}$ → $L_{t-1} c_{2t} = (1 + r_t) K_t$ (old fully consume their interest plus capital — they die at end of period, no bequest)
- $L_t$ young people each consume $c_{1t}$ → $L_t c_{1t} = L_t w_t - L_t s_t$
- Aggregate consumption: $C_t = L_t c_{1t} + L_{t-1} c_{2t}$

#### Goods market equilibrium → basic dynamic equation
Savings-investment equality: $C_t + I_t = Y_t$, where $I_t = K_{t+1} - K_t$ (no depreciation). Combined with $F(K_t, L_t) = w_t L_t + r_t K_t$ (CRS) and the consumption aggregation:
$$K_{t+1} = L_t s_t$$
i.e., **tomorrow's capital stock = today's young's total savings**.

In per-capita terms (dividing by $L_{t+1}$):
$$k_{t+1} = \frac{L_t s_t}{L_{t+1}} = \frac{s(w(k_t), r(k_{t+1}))}{1+n}$$

This is the **basic dynamic equation** of the OLG model — a first-order non-linear difference equation in $k$.

### Definitions
- **Bequest**: A transfer of wealth from one generation to the next. In the standard OLG model, there is no bequest — the old fully consume their wealth.
- **Basic dynamic equation (OLG)**: $k_{t+1} = s(w(k_t), r(k_{t+1}))/(1+n)$ — links tomorrow's capital-labor ratio to today's. ⭐ (exam-important)
- **Savings function**: $s_t = s(w_t, r_{t+1})$, derived from individual two-period utility maximization.

### Mechanisms / Processes
**Why $K_{t+1} = L_t s_t$**:
1. The young earn $w_t L_t$ in total wages, consume $L_t c_{1t}$, save $L_t s_t$.
2. The old fully consume capital + interest: $L_{t-1} c_{2t} = (1 + r_t) K_t$.
3. Goods market: $C_t + (K_{t+1} - K_t) = Y_t = w_t L_t + r_t K_t$.
4. Substitute: $L_t c_{1t} + L_{t-1} c_{2t} + K_{t+1} - K_t = w_t L_t + r_t K_t$
5. Simplify using $L_{t-1} c_{2t} = (1 + r_t) K_t$ and $L_t c_{1t} = L_t w_t - L_t s_t$:
   $L_t w_t - L_t s_t + (1 + r_t) K_t + K_{t+1} - K_t = w_t L_t + r_t K_t$
6. → $K_{t+1} = L_t s_t$. ✓

#### Slope of the dynamic equation
Total differentiation gives:
$$\frac{dk_{t+1}}{dk_t} = \frac{s_w f''(k_t)\cdot(-k_t)}{(1+n) - s_r f''(k_{t+1})}$$
where $s_w = \partial s/\partial w$ and $s_r = \partial s/\partial r$.

Signs:
- Under "consumption is normal in both periods" assumption: $0 < s_w < 1$ ✓
- $s_r$ has ambiguous sign: substitution effect of higher $r$ raises savings, income effect lowers savings
  - If income effect dominates: $s_r < 0$
  - If substitution effect dominates: $s_r > 0$
- The text assumes substitution effect dominates → $s_r > 0$ → $k_{t+1}$ line is positively sloped

#### Multiple steady states (Fig. 10.1)
Plot $k_{t+1}$ on vertical axis, $k_t$ on horizontal. Steady state: $k_{t+1}$ line crosses 45° line.

Depending on curvature, multiple steady states $k^*$ and $k^{**}$ are possible.

**Local stability**:
- $k_{t+1}$ line crosses 45° from *above* → locally stable equilibrium
- $k_{t+1}$ line crosses 45° from *below* → locally unstable equilibrium

So if both $k^*$ (cross-from-above) and $k^{**}$ (cross-from-below) exist, $k^*$ is stable and $k^{**}$ is unstable.

### Examples
**Example: Why the old consume their entire capital stock**
The old generation owns all the capital (no bequest, so the young own nothing yet). They die at end of period and have no descendants to leave wealth to (selfish). In the one-good world, capital is directly consumable, so the old consume both their interest income $r_t K_t$ and the capital itself $K_t$, totaling $(1 + r_t) K_t$.

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking the new capital comes from the old's savings → ✅ Correct: The old fully consume; only the young's savings become next period's capital.
- ❌ Mistake: Believing $s_w > 1$ is possible → ✅ Correct: With both consumptions normal goods, $0 < s_w < 1$.
- ❌ Mistake: Assuming $s_r > 0$ always → ✅ Correct: $s_r$ depends on which of income/substitution effect dominates.

### Edge Cases & Caveats
- The slope analysis depends on the assumption that the substitution effect dominates the income effect for savings ($s_r > 0$).
- Multiple equilibria possible depending on the curvature of $k_{t+1}(k_t)$.
- The "no bequest" assumption is what makes generations effectively selfish — central to dynamic inefficiency.

> **Quick Recall:**
> - Young: $c_{1t} + s_t = w_t$
> - Old: $c_{2t+1} = (1 + r_{t+1}) s_t$
> - Lifetime BC: $c_{1t} + c_{2t+1}/(1 + r_{t+1}) = w_t$
> - FOC: $U_1/U_2 = (1 + r_{t+1})$
> - Capital evolves: $K_{t+1} = L_t s_t$ → $k_{t+1} = s(w(k_t), r(k_{t+1}))/(1+n)$
> - Multiple steady states possible
> - Cross-from-above → stable; cross-from-below → unstable

### Connections
- Builds on: Two-period utility maximization (similar to Fisher, Chunk 001) but with explicit production
- Compare with: Ramsey-Cass-Koopmans (infinite-life dynasty vs. two-period selfish individuals)
- Foundation for: Dynamic inefficiency analysis (next section)

---

## Section: Dynamic Inefficiency in OLG 🔴

### Core Idea
Even when the OLG steady state is unique and stable, it can be **dynamically inefficient** — the economy has accumulated *too much* capital relative to the welfare-maximizing level. Comparing the OLG steady-state $k^*$ to the **golden rule** $k_g$ (where $f'(k_g) = n$, maximizing per-capita consumption): if $k^* > k_g$, people are over-saving and over-investing. They could permanently raise everyone's lifetime utility by consuming part of their savings — a Pareto improvement. This is impossible in RCK (where steady-state $k^* < k_g$ always) but is a real possibility in OLG, because individuals are selfish (no bequest) and ignore the population growth $n$ when valuing the return to investment.

> **In Simple Terms:** Imagine an economy that accumulates so much capital that any extra unit yields almost no return. People could collectively save less — eat more today *and* still have enough capital tomorrow to keep consumption high forever. That's dynamic inefficiency. RCK rules it out, but OLG allows it because each generation only cares about itself.

### Key Concepts

#### Pareto efficiency in steady-state comparison
Compare alternative steady states, each with a different $k$ and corresponding $(c_1^*, c_2^*)$. Each steady state implies a different level of lifetime utility $u(c_1^*, c_2^*)$.

#### Golden rule
The steady-state $k_g$ that maximizes lifetime utility:
$$f'(k_g) = n$$
This is the **best possible steady state** for the representative individual.

#### Two regions:
- **Right of $k_g$ (i.e., $k > k_g$): dynamically inefficient region**
  - Capital is over-accumulated
  - If people consumed part of their savings in period 1, $k$ would fall toward $k_g$ AND lifetime utility would rise
  - Pareto improvement: can raise current consumption *without* sacrificing future consumption
  - These are **dynamically inefficient** points
- **Left of $k_g$ (i.e., $k < k_g$): dynamically efficient region**
  - To move toward $k_g$, must save more (forgo current consumption) — a real cost
  - Cannot say definitively whether moving is welfare-improving (current loss vs. future gain)
  - All points are **Pareto efficient** / dynamically efficient

#### RCK steady state is always dynamically efficient
RCK steady state: $f'(k^*) = \rho + n > n = f'(k_g)$ (since $\rho > 0$)
→ $k_{RCK}^* < k_g$ → always in the dynamically efficient region.

#### OLG steady state can be dynamically inefficient
Under reasonable parameter values, the OLG steady-state $k_{OLG}^*$ can exceed $k_g$.

### Definitions
- **Dynamic efficiency**: A property of an equilibrium where current consumption cannot be increased without reducing future consumption. ⭐ (exam-important)
- **Dynamic inefficiency**: A situation (possible in OLG but not RCK) where the economy has over-accumulated capital — current consumption can be raised *without* sacrificing future consumption, yielding a Pareto improvement. ⭐ (exam-important)
- **Golden rule capital-labor ratio** ($k_g$): The steady-state $k$ that maximizes per-capita steady-state utility, satisfying $f'(k_g) = n$.

### Mechanisms / Processes
**Why dynamic inefficiency arises in OLG (intuition)**:
1. Individuals in OLG are selfish — no bequest to next generation.
2. They do not share the benefits of investment with future generations (who grow at rate $n$).
3. When valuing return on investment, the relevant return for each individual is just $f'(k)$ — *not net of $n$*.
4. They will invest as long as $f'(k) > 0$, even when $f'(k) < n$.
5. → Over-saving relative to the social optimum.

In RCK, the dynastic household internalizes its descendants' welfare → effectively accounts for $n$ → never over-saves.

### Examples
**Example: Worked example with log utility and Cobb-Douglas production**

Setup:
- Utility: $U(c_{1t}, c_{2t+1}) = \ln c_{1t} + \beta \ln c_{2t+1}$, $0 < \beta < 1$
- Production: $f(k_t) = A k_t^\alpha$, $0 < \alpha < 1$ (Cobb-Douglas)

FOCs:
1. $\dfrac{c_{2t+1}}{c_{1t}} = \beta(1 + r_{t+1})$
2. $c_{1t} + \dfrac{c_{2t+1}}{1 + r_{t+1}} = w_t$

Solving gives the savings function:
$$s_t = \frac{\beta}{1 + \beta}\, w_t$$

(A constant fraction of the wage, independent of $r_{t+1}$.)

Wage from CD: $w_t = (1 - \alpha) A k_t^\alpha$.

Basic dynamic equation:
$$k_{t+1} = \frac{1}{1 + n} \cdot \frac{\beta}{1 + \beta} \cdot (1 - \alpha) A k_t^\alpha$$

Steady state ($k_{t+1} = k_t = k^*$):
$$k^* = \left[\frac{\beta(1 - \alpha) A}{(1 + n)(1 + \beta)}\right]^{1/(1-\alpha)}$$

Golden rule: $f'(k_g) = \alpha A k_g^{\alpha - 1} = n$ → $k_g = \left(\dfrac{\alpha A}{n}\right)^{1/(1-\alpha)}$.

**Condition for dynamic inefficiency** ($k^* > k_g$):
$$\frac{\beta(1 - \alpha)}{(1 + n)(1 + \beta)} > \frac{\alpha}{n}$$

Simplifies to:
$$\frac{\beta(1 - \alpha)}{1 + \beta} > \frac{\alpha (1 + n)}{n}$$

Numerical example: $\alpha = 1/4$, $n = 1$ → dynamic inefficiency holds for sufficiently large $\beta$ (high weight on future consumption).

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing dynamic inefficiency with simple welfare loss → ✅ Correct: Specifically means a Pareto improvement is possible by *reducing* savings.
- ❌ Mistake: Thinking dynamic inefficiency means too *little* savings → ✅ Correct: It means too *much* savings — over-accumulation.
- ❌ Mistake: Assuming RCK can be dynamically inefficient too → ✅ Correct: RCK steady state is always to the *left* of $k_g$ (since $\rho > 0$), so always dynamically efficient.

### Edge Cases & Caveats
- Dynamic inefficiency in OLG is parameter-dependent — not guaranteed. Depends on utility, production technology, and growth rate.
- Even if the steady state is unique and stable, it can still be inefficient.

> **Quick Recall:**
> - Golden rule: $f'(k_g) = n$
> - $k > k_g$: dynamically inefficient (over-saving)
> - $k < k_g$: dynamically efficient
> - RCK steady state: $f'(k^*) = \rho + n > n$ → always efficient
> - OLG steady state: can be either; condition $\frac{\beta(1-\alpha)}{1+\beta} > \frac{\alpha(1+n)}{n}$ in CD example
> - Cause: selfish OLG individuals don't account for population growth

### Connections
- Builds on: Structure of OLG model (previous section); golden rule (Chunk 003: Central Planner's Problem — Steady State, Phase Diagram, Modified Golden Rule)
- Contrasts with: RCK steady state (always efficient, Chunk 003)
- Foundation for: Social security analysis (next section)

---

## Section: Social Security 🔴

### Core Idea
If OLG can produce dynamic inefficiency, can government policy fix it? Yes — but only some types. Two systems exist: **fully funded** (your contributions are invested for you and returned with interest) and **pay-as-you-go (PAYG)** (your contributions immediately fund current retirees, while you'll be funded by future workers). Fully funded systems leave private behavior unchanged → cannot eliminate inefficiency. PAYG, however, gives an effective return of $n$ (population growth rate) on contributions; in a dynamically inefficient economy where $r < n$, individuals prefer to save less and contribute more to PAYG → reduces capital accumulation → moves the economy back to the efficient region.

> **In Simple Terms:** Two pension systems: one (fully funded) is like the government putting your money in a savings account for you — you respond by saving less yourself, no net change. The other (PAYG) is "pay it forward": you fund today's retirees, and tomorrow's workers will fund you. PAYG only works as a fix because in over-saving economies, the implicit return $n$ beats the actual return $r$, encouraging less private saving.

### Key Concepts

#### Fully funded social security
Each young person pays a contribution $d_t$ to the government. The government invests it. When the contributor is old (period $t+1$), the government returns it with interest:
$$b_{t+1} = (1 + r_{t+1}) d_t$$
Same set of people contribute and receive — no inter-generational transfer.

**Effect on private savings**: The individual is effectively saving $(s_t + d_t)$ and earning $(1 + r_{t+1})(s_t + d_t)$ in the next period. Knowing this, the individual cuts back on private savings $s_t$ to keep total effective savings the same as before social security.

→ **No net effect** on total savings or capital accumulation. If the economy was dynamically inefficient before, it remains so.

#### Pay-as-you-go (PAYG) social security
Each young person pays contribution $d_t$ to the government. The entire amount is immediately distributed to currently old people. There are $(1 + n)$ times as many young as old (population growth), so:
$$b_t = (1 + n) d_t$$

**Effective rate of return on contributions**: $n$ (population growth rate).

**Comparison**:
| System | Rate of return on contribution |
|--------|--------------------------------|
| Fully funded | $r$ (capital return) |
| Pay-as-you-go | $n$ (population growth rate) |

**Effect on private savings**:
- If $r > n$: private savings have higher return → people prefer to save privately → PAYG less attractive
- If $r < n$ (the dynamically inefficient case): PAYG offers a *higher* return than private savings → people save less privately and contribute more to PAYG → reduces capital accumulation → economy moves toward dynamic efficiency

→ **PAYG eliminates dynamic inefficiency** in over-accumulating economies.

### Definitions
- **Social security programme**: A government scheme that provides income to individuals after retirement.
- **Fully funded social security**: A system where contributions made by individuals when young are invested and returned with interest to the same individuals when old. ⭐ (exam-important)
- **Pay-as-you-go (PAYG) social security**: A system where contributions from current workers are immediately transferred to current retirees; effective rate of return is the population growth rate $n$. ⭐ (exam-important)

### Mechanisms / Processes
**Fully funded mechanism**:
1. Young pay $d_t$, government invests it, returns $(1 + r_{t+1}) d_t$ when they're old.
2. Individual's effective savings: $s_t + d_t$; effective consumption when old: $(1 + r_{t+1})(s_t + d_t)$.
3. Individual chooses optimal total: $s_t^{old} = s_t + d_t$ → cuts private $s_t$ by exactly $d_t$.
4. Net effect on aggregate: 0.

**PAYG mechanism**:
1. Young pay $d_t$ → immediately given to old → $b_t = (1 + n) d_t$.
2. Effective return on contribution = $n$ (vs. $r$ for private capital).
3. If $r < n$ (dynamic inefficiency): individuals prefer higher-return PAYG, save less privately.
4. Lower $s_t$ → lower $K_{t+1}$ → $k$ falls toward $k_g$ → dynamic efficiency restored.

### Examples
**Example: Fully funded — why it doesn't help**
Suppose without social security, individual saves $s = 10$. Government introduces a fully funded scheme requiring $d = 4$. Individual now plans for total effective savings of 10, so reduces private $s$ to 6. Total $s + d = 10$ still. Aggregate capital stock unchanged.

**Example: PAYG with $r < n$**
Suppose $r = 2\%$, $n = 3\%$. Without social security, individual saves $s$ for retirement at return 2%. With PAYG contribution $d$, they get effective return of 3% on $d$. Since 3% > 2%, they reduce $s$ and rely more heavily on PAYG → lower capital stock → economy moves toward $k_g$.

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking both social security systems are equivalent → ✅ Correct: Fully funded is neutral; PAYG affects behavior because effective return differs from $r$.
- ❌ Mistake: Believing PAYG always reduces capital → ✅ Correct: It does so only in dynamically inefficient regions where $r < n$. In dynamically efficient regions, effects can differ.
- ❌ Mistake: Calling the result a violation of Ricardian Equivalence → ✅ Correct: It is — Ricardian Equivalence breaks down in OLG because each generation is finite-lived and selfish, so debt/transfers across generations have real effects.

### Edge Cases & Caveats
- Fully funded results assume government earns same return as private investment.
- PAYG's efficiency gain depends on $r < n$ holding — not always true.
- Real-world systems are mixed and have many complications (myopia, liquidity constraints).

> **Quick Recall:**
> - Fully funded: $b_{t+1} = (1 + r_{t+1}) d_t$ — same return as private capital
> - PAYG: $b_t = (1 + n) d_t$ — effective return = $n$
> - Fully funded: neutral (offset by reduced private saving)
> - PAYG: reduces private savings if $r < n$ → fixes dynamic inefficiency
> - PAYG works precisely because Ricardian Equivalence fails in OLG

### Connections
- Builds on: Dynamic inefficiency analysis (previous section)
- Contrasts with: Ricardian Equivalence in RCK (Chunk 003: Central Planner's Problem — Steady State, Phase Diagram, Modified Golden Rule) — debt-financed government is neutral there but transfers can have real effects in OLG

---

## Section: Unit 10 Summary 🟢

### Core Idea
The standard two-period OLG model with production yields a dynamic equation $K_{t+1} = L_t s_t$: tomorrow's capital is today's young's savings. Steady-state analysis shows the OLG equilibrium can be **dynamically inefficient** (over-accumulation of capital) because each generation is selfish and ignores population growth. Government can restore efficiency, but only via a **pay-as-you-go** social security system (whose effective return $n$ encourages less private saving when $r < n$). A **fully funded** system has no effect — individuals offset it with reduced private saving.

> **Quick Recall:**
> - Basic dynamic equation: $K_{t+1} = L_t s_t$
> - Per-capita: $k_{t+1} = s/(1+n)$
> - Steady state: possibly dynamically inefficient
> - Fully funded SS: no effect on capital
> - PAYG SS: reduces capital if $r < n$ → eliminates inefficiency


---

