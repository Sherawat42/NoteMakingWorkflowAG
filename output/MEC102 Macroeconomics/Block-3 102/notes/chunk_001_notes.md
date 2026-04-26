# Chunk 001 — Unit 8: Consumption and Asset Prices (Intertemporal Choice, LCH, PIH, Random Walk Setup)
<!-- Pages: 1-10 -->
<!-- Source: chunk_001.txt -->

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
- Continues in: Random Walk Hypothesis derivation and policy implications (Chunk 002)
