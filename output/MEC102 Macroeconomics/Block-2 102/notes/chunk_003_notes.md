# Chunk 003 — Rational Expectations Hypothesis, Lucas Supply Function, Policy Ineffectiveness
<!-- Pages: 20-29 -->
<!-- Source: chunk_003.txt -->

## Section: 7.5 Rational Expectations Hypothesis (REH) — Full Treatment 🔴
<!-- Continues from Chunk 002 -->

### Core Idea
Rational expectations differ from perfect foresight by acknowledging an irreducible random component $\nu_t$ in the data-generating process. Agents using REH form predictions that are correct **on average** — the expectational error has mean zero and known variance — and base their predictions on the **true model**, not naive past trends. REH provides the microeconomic foundation for new-classical macroeconomics: with flexible prices and wages, markets clear and unemployment stays at the natural level.

> **In Simple Terms:** REH is like a meteorologist using physics-based weather models with all current data — predictions are right on average, with errors only from genuine atmospheric noise. Adaptive expectations are like guessing tomorrow's weather from yesterday's.

### Key Concepts

#### Stochastic version of the true model
$$Y_t = \alpha + \beta X_{t-1} + \gamma Y_{t-1} + \eta Z_{t-1} + \nu_t \qquad \text{(7.3)}$$

where $\nu_t$ is a **random term** capturing the inherent stochastic (probabilistic) process in an economy — for instance, the unpredictable nature of human behaviour.

#### Rational expectation of $Y_t$
$$E_{t-1}Y_t = \alpha + \beta X_{t-1} + \gamma Y_{t-1} + \eta Z_{t-1} \qquad \text{(7.4)}$$

— the predicted value of $Y$ at end of period $(t-1)$ for period $t$, based on observed values at $(t-1)$ of $X$, $Y$, $Z$.

#### Expectational error properties
$$\nu_t = Y_t - E_{t-1}Y_t$$

- **Mean = 0** (because if not, we can adjust $\alpha$ to make it so).
- **Variance = $\sigma^2$** (known, finite).
- $\nu_t$ is unknowable until time $t$ — pure noise.

So actual $Y_t$ deviates from expected $Y_t$ only by $\nu_t$. Usually $\nu_t$ is small because it's a composite of several variables pulling in different directions.

#### Why RE is the most accurate expectation
- It's based on the **true model** generating the variable.
- All other methods (astrology, dart-throwing, naive past trends, plain adaptive updating) ignore the underlying process and produce systematically worse forecasts on average.

#### Example — consumption
- Simple model: $C_t$ depends on past wealth, past consumption, past disposable income.
- RE-value of $C_t$ = average/expected consumption of a population.
- Each individual's actual consumption varies around this average (different preferences) — the deviations are the $\nu_t$ for each individual.

#### What REH assumes about agents
Economic agents (workers, consumers, firms, government) are assumed to know:
1. The **relevant variables** ($X, Y, Z$ etc.).
2. The **parameters** ($\alpha, \beta, \gamma, \eta$).
3. The **functional form** (linear here, or quadratic, exponential, etc.).

Given these, agents can predict everything *predictable* about $Y_t$. The only error is the inherent random component.

#### Criticisms of REH
- People in general are **not aware** of the underlying economic processes — assuming full model knowledge is unrealistic.
- Some relevant information is **expensive** to procure.
- However, modern access to **expert forecasts via public media** narrows the gap.
- Even with imperfect knowledge, RE forecasts will still be correct **on average**, just with larger variance.

#### Why economists still adopt REH despite criticisms
- It gives a **microfoundation** for macro theory: agents optimize and decisions are rational and most beneficial to them.
- With **flexible wages and prices**, demand and supply for output and labour clear in their respective markets.
- → no involuntary unemployment, no deviation of output from $Y_N$ on average.
- Microfoundation is an integral part of REH.

#### One key macro implication
Government policy to reduce unemployment (e.g., monetary expansion, debt monetization from fiscal expansion) will **not have the desired effect if it is predictable or announced in advance**. Workers anticipate that all prices (nominal wages and prices of what they buy) rise proportionately → real wages don't rise → no extra employment.

#### Open question raised
*How do RE models explain observed booms and recessions, where output deviates from $Y_N$?* Answer: the **Lucas Supply Function** and the **Policy Ineffectiveness Proposition** (next sections).

### Definitions
- **Stochastic true model**: $Y_t = \alpha + \beta X_{t-1} + \gamma Y_{t-1} + \eta Z_{t-1} + \nu_t$ — equation (7.3); REH foundation. ⭐
- **Rational expectational error**: $\nu_t = Y_t - E_{t-1}Y_t$; mean 0, variance $\sigma^2$. ⭐ (exam-important)
- **Microfoundations**: building macro relationships from optimizing decisions of individual agents (firms maximize profit, workers maximize utility).

### ⚠️ Common Mistakes
- ❌ Mistake: assuming RE means agents are *always right* → ✅ Correct: they are right **on average**; individual errors $\nu_t$ are random and non-zero.
- ❌ Mistake: equating RE with perfect foresight → ✅ Correct: RE includes $\nu_t$; perfect foresight has $\nu_t = 0$.
- ❌ Mistake: thinking RE rules out **all** policy effects → ✅ Correct: it rules out only **anticipated** policy; surprise policy still works (see 7.7).

> **Quick Recall:**
> - Equation (7.3): adds $\nu_t$ to the deterministic model.
> - Expectational error: mean 0, variance $\sigma^2$.
> - REH provides **microfoundations** for new-classical macro.
> - **Anticipated** policy → no real effect; **unanticipated** policy → real effect.

### Connections
- Builds on: Lucas Critique (Chunk 002), Perfect Foresight (Chunk 002), AS-AD model (Chunk 002).
- Sets up: Lucas Supply Function (this chunk), Policy Ineffectiveness (this chunk).

---

## Section: 7.6 Lucas Supply Function 🔴

### Core Idea
Lucas's supply curve explains why output fluctuates around $Y_N$ even under rational expectations: agents care about **relative prices** but only have **local** information about their own price; they cannot perfectly distinguish relative-price changes from a general (aggregate) price change. A "price surprise" — actual price level above the rationally expected price — fools them symmetrically into supplying more output and labour. Without a price surprise, anticipated changes have **no real effects**.

> **In Simple Terms:** Imagine you're a baker and bread prices rise. Are bread prices higher just for *your* bread (so you should bake more) or are *all* prices up because of inflation (so you should keep production steady)? You can't tell. If you guess "just my bread" when actually it's general inflation, you'll be fooled into baking more — that's the Lucas mechanism.

### Key Concepts

#### What agents care about: relative prices
- A **firm** cares about price of its output relative to prices of inputs it buys.
- A **worker** cares about real wage = nominal wage / prices of goods bought.
- Higher relative price for a firm → more output (assuming substitution > income effect).
- Higher real wage for a worker → more labour supply.

#### Two signal-extraction problems
1. **Aggregate vs. relative price change**: when an agent sees ↑ price for their good, is it only their good (relative ↑) or all goods (aggregate ↑)? Each agent must extract this signal.
2. **Temporary vs. permanent change**: temporary relative price increases are more important — agents must act fast to capture profitable opportunities. If history says general price increases mix relative + aggregate components, agents observing a price rise will assume **part of it** is relative → supply more.

#### Information asymmetry — local vs. global
Firms and households know much more about prices of what they sell than about prices of all the inputs/goods they buy → **local** information, not **global**. This local-only information is what creates the signal-extraction problem.

#### Anticipated vs. surprise inflation under RE
- If agents anticipate / know about a general ↑P (e.g., from announced ↑M), they understand all prices have risen proportionately → no relative price change → **no change in output or labour supply**.
- If there's a **price surprise** ($P_t > E_{t-1}P_t$), agents wrongly attribute part of it to relative ↑ → output / labour supply rise above $Y_N$.

#### The Lucas Supply Curve
Levels form:
$$Y_t / Y_p = f(P_t / E_{t-1}P_t) \qquad \text{(7.5)}$$

Logarithmic form:
$$y_t - y_p = f(p_t - E_{t-1}p_t) \qquad \text{(7.6)}$$

where:
- $Y_t$ = output in period $t$.
- $Y_p$ = potential / full-employment output.
- $P_t$ = price of product.
- $E_{t-1}P_t$ = price of product expected one period prior.
- Lower-case = log of upper-case variable.

**Reading**: output exceeds $Y_p$ exactly when there is a positive **price surprise**.

#### Stable vs. volatile-price economies
| Environment | Effect of monetary expansion |
|-------------|------------------------------|
| Prices generally stable; past ↑P often = relative ↑ | Agents fooled → ↑ output, ↑ labour supply |
| Prices generally volatile (high inflation, e.g., some Latin American economies) | Agents NOT fooled → no output / labour effect |

#### Crucial contrast with AS-AD
- **AS-AD (Section 7.2)**: workers fooled, firms not — **asymmetric** information.
- **Lucas Supply Curve**: workers AND firms **symmetrically** fooled by local-only information.

#### Lucas explanation of the business cycle
Output fluctuations around $Y_N$ are driven by **price surprises** that fool agents symmetrically. Had information been perfect, agents would distinguish nominal vs. real price changes → classical dichotomy holds, money is neutral, and there'd be no cycle.

### Mechanisms / Processes
$$\text{Surprise } \uparrow M \rightarrow \uparrow P_t > E_{t-1}P_t \rightarrow \text{agents attribute partly to relative price} \rightarrow \uparrow \text{output/labour} \rightarrow Y_t > Y_p$$

### Definitions
- **Lucas Supply Function**: $y_t - y_p = f(p_t - E_{t-1}p_t)$; output deviates from full-employment output only with a price surprise. ⭐ (exam-important)
- **Signal extraction problem**: each agent's task of distinguishing a relative-price change from a general-price change using only local information. ⭐ (exam-important)
- **Local vs. global information**: agents know more about prices of what they sell than what they buy.
- **Price surprise**: $P_t - E_{t-1}P_t > 0$; the unanticipated component of inflation.

### ⚠️ Common Mistakes
- ❌ Mistake: treating the Lucas Supply Curve as a Phillips curve in disguise → ✅ Correct: it's a *supply* function with **anticipated** changes having NO effect, unlike the original Phillips curve.
- ❌ Mistake: assuming Lucas's framework allows expected inflation to lower unemployment → ✅ Correct: only **unexpected** inflation does.
- ❌ Mistake: applying Lucas's mechanism to high-inflation economies the same way → ✅ Correct: in volatile-price economies the fooling is much weaker because agents *expect* general inflation.

### Edge Cases & Caveats
- High-inflation economies (Latin American examples cited) erode the fooling mechanism.
- The "fooling" here is symmetric — different from AS-AD's asymmetric fooling story.

> **Quick Recall:**
> - Equation (7.6): $y_t - y_p = f(p_t - E_{t-1}p_t)$.
> - Output deviates only with a **price surprise**.
> - Workers AND firms are symmetrically fooled (vs. AS-AD).
> - In high-inflation economies, mechanism is weak → money close to neutral.

### Connections
- Builds on: REH (this chunk), AS-AD model (Chunk 002).
- Sets up: Policy Ineffectiveness Theorem (this chunk).

---

## Section: 7.7 Policy Ineffectiveness Theorem 🔴

### Core Idea
While the Lucas Supply Function uses the **supply** side, the policy ineffectiveness theorem (Sargent–Wallace, 1976) builds the **demand-side** counterpart. Combining an AD relation, a Lucas-type AS relation, a money-supply rule, and rational expectations, the theorem proves: only the **unanticipated** part of monetary policy can move output. Any **systematic / predictable** monetary policy leads only to proportionate price changes — no impact on real output. This negates the possibility of any rule-based policy keeping $Y$ permanently above $Y_p$.

> **In Simple Terms:** If the central bank always cuts rates by 50 bps after a recession, everyone factors that in before it happens. The real effect is gone before the rate cut even arrives. Only the unpredictable part of policy "surprises" the economy and moves output.

### Key Concepts

#### Setup
- Only **monetary** policy is considered (no fiscal).
- Agents have **rational expectations** about the central bank's money-supply rule.
- A random component $\epsilon_t$ in money supply represents what the central bank cannot fully control (capital flows, banks holding excess reserves, public preferring cash, etc.).

#### The four-equation model

**(1) Aggregate Demand (in logs)**
$$M_t + V_t = P_t + y_t \qquad \text{(7.7)}$$

This is the familiar $MV = PY$ in log form, hence linear. $V_t$ is treated as constant for simplicity (relaxing this isn't critical to the argument).
- $M_t$: log money supply.
- $V_t$: log velocity (constant).
- $P_t$: log price level.
- $y_t$: log real output.

An increase in $M_t$ shifts the AD line right.

**(2) Aggregate Supply (Lucas form)**
$$y_t = y_p + \beta(P_t - {}_{t-1}P^e_t) \qquad \text{(7.8)}$$

- $y_p$: log full-employment output.
- ${}_{t-1}P^e_t$: log expected price for period $t$, formed in period $(t-1)$.
- Output exceeds $y_p$ only if there is a positive price surprise.

**(3) Money-Supply Rule**
$$M_t = \alpha y_{t-1} + \epsilon_t \qquad \text{(7.9)}$$
$$\text{with } E(\epsilon_t \mid I_{t-1}) = 0$$

- $\alpha y_{t-1}$ is the **systematic / anticipatable** part of money supply, derived from past observed output (the central bank's reaction function).
- $\epsilon_t$ is the **unpredictable / random** part with conditional mean zero.

**(4) Rational Expectations**
$${}_{t-1}P^e_t = E(P_t \mid I_{t-1}) \qquad \text{(7.10)}$$

The expected price is **endogenous** — derived from within the same model that explains actual prices.

#### Graphical preview (Figs. 7.2 and 7.3)
- Without RE (Fig. 7.2): ↑M shifts AD right; AS unchanged → both $P$ and $y$ rise — looks like the original Phillips curve trade-off.
- With RE (Fig. 7.3): in period $(t-1)$ agents already anticipate the systematic shift in AD due to expected ↑M → AS shifts up by exactly the expected price increase. The dotted AD curve $AD^e_1$ shows the *anticipated* shift; the solid $AD_1$ may be to the right of $AD^e_1$ if the random component $\epsilon_t > 0$.
- Only the **gap** between $AD_1$ and $AD^e_1$ (the unanticipated part) generates a price surprise → output deviates.

#### Algebraic derivation — step-by-step

**Step 1 — substitute (7.8) and (7.9) into (7.7)**:
$$\alpha y_{t-1} + \epsilon_t + V = P_t + y_p + \beta(P_t - {}_{t-1}P^e_t) \qquad \text{(7.11)}$$

**Step 2 — take mathematical expectation as of $(t-1)$** to find ${}_{t-1}P^e_t$:
$$\alpha y_{t-1} + E(\epsilon_t) + V = {}_{t-1}P^e_t + y_p + \beta({}_{t-1}P^e_t - {}_{t-1}P^e_t)$$

Since $E(\epsilon_t) = 0$ and the $\beta$ term cancels:
$${}_{t-1}P^e_t = \alpha y_{t-1} + V - y_p \qquad \text{(7.12)}$$

**Step 3 — express $P_t$ from (7.7)**:
From (7.7), $P_t = M_t + V_t - y_t$. Substituting $M_t$ from (7.9) and $y_t$ from (7.8):
$$P_t = \alpha y_{t-1} + \epsilon_t + V - y_p + \beta(P_t - {}_{t-1}P^e_t) \qquad \text{(7.13)}$$

(Note: $y_p$ replaces $y_t$ where the Lucas-supply structure absorbs the surprise term into the $\beta$ term.)

**Step 4 — subtract (7.12) from (7.13)**:
$$P_t - {}_{t-1}P^e_t = \epsilon_t + \beta(P_t - {}_{t-1}P^e_t) \qquad \text{(7.14)}$$

**Step 5 — rearrange to isolate the price surprise**:
$$P_t - {}_{t-1}P^e_t = \frac{\epsilon_t}{1 + \beta} \qquad \text{(7.15)}$$

**Step 6 — substitute back into Lucas Supply (7.8)**:
$$y_t = y_p + \beta \cdot \frac{\epsilon_t}{1 + \beta} \qquad \text{(7.16)}$$

#### Interpretation of (7.15) and (7.16)
- (7.15): the price surprise is driven entirely by $\epsilon_t$ — the **unanticipated** part of money supply.
- (7.16): output exceeds $y_p$ **only** when $\epsilon_t \neq 0$.
- (7.15) also implies $P_t = {}_{t-1}P^e_t + \epsilon_t/(1+\beta)$ → both **expected** price and the **unanticipated** money component affect actual prices, but only **unanticipated** money affects **output**.

#### The two key results
1. Only **unanticipated (surprise)** monetary policy moves output, given RE and a known money-supply rule.
2. Whatever functional form the rule takes, the moment it's known, agents incorporate it → no real effect.

This **negates** the possibility of any **systematic** policy rule keeping $y_t > y_p$.

#### Money's neutrality status
- Lucas Supply Curve & Policy Ineffectiveness → money is **NOT neutral** in the short run (because of $\epsilon_t$).
- But **systematic** money is neutral — only unsystematic surprises matter.

#### Keynesian critique
- Correct information should be available **within a short time** → booms / recessions spanning **several years** are not well explained by RE-based fooling.
- The assumption that all markets clear (implying voluntary unemployment) is implausible during high unemployment.
- Despite criticism, RE remains "an appealing way to incorporate microeconomic foundations" of macro relations.
- It has further implications elsewhere — e.g., the **random walk of consumption** and **Ricardian Equivalence**.

### Mechanisms / Processes
1. Agents observe past money-supply behaviour → infer rule $\alpha y_{t-1} + \epsilon_t$.
2. Anticipate systematic component $\alpha y_{t-1}$ → adjust $P^e$ → AS shifts up correspondingly.
3. Actual $M_t$ may differ from $E_{t-1}M_t$ by $\epsilon_t$ → AD shifts beyond expected position.
4. Difference $P_t - {}_{t-1}P^e_t = \epsilon_t/(1+\beta)$ creates a price surprise.
5. Lucas Supply: $y_t = y_p + \beta\epsilon_t/(1+\beta)$ → output deviation depends ONLY on $\epsilon_t$.

### Definitions
- **Policy Ineffectiveness Theorem (Sargent & Wallace, 1976)**: under rational expectations and a known money-supply rule, only the **unanticipated** part of monetary policy moves output; any predictable rule has no real effect. ⭐ (exam-important)
- **Money supply rule**: $M_t = \alpha y_{t-1} + \epsilon_t$, where $\alpha y_{t-1}$ is anticipatable, $\epsilon_t$ is random with conditional mean 0. ⭐
- **Endogenous expectations**: expected value derived within the same model that explains the actual variable (eq. 7.10).

### Examples
**Worked derivation: from (7.7)–(7.10) to (7.16)**:
1. Substitute $M_t$ and $y_t$ into AD equation → (7.11).
2. Take $E_{t-1}$ of (7.11), use $E(\epsilon_t)=0$ → solve for ${}_{t-1}P^e_t$ → (7.12).
3. Express $P_t$ from AD and substitute → (7.13).
4. Subtract (7.12) from (7.13) → (7.14).
5. Solve for price surprise → $P_t - {}_{t-1}P^e_t = \epsilon_t / (1 + \beta)$ → (7.15).
6. Substitute into Lucas supply → $y_t = y_p + \beta\epsilon_t/(1 + \beta)$ → (7.16).

### ⚠️ Common Mistakes
- ❌ Mistake: assuming the theorem says **all** policy is ineffective → ✅ Correct: only the **anticipated/systematic** part is ineffective; the **random** part still moves output.
- ❌ Mistake: confusing anticipated price level with anticipated price change → ✅ Correct: it's the **expected level** $E_{t-1}P_t$ that gets baked into AS via wage demands.
- ❌ Mistake: forgetting velocity assumption → ✅ Correct: $V_t$ is taken as constant for simplicity; relaxing it doesn't change the conclusion.
- ❌ Mistake: applying the theorem to fiscal policy → ✅ Correct: the model considers **only** monetary changes.

### Edge Cases & Caveats
- The model considers only monetary policy.
- Velocity is assumed constant — relaxing isn't critical to the conclusion.
- Keynesians dispute the "all markets clear" assumption and the long persistence of cycles.

> **Quick Recall:**
> - Four equations: AD (7.7), AS-Lucas (7.8), money rule (7.9), RE (7.10).
> - Key result (7.15): $P_t - {}_{t-1}P^e_t = \epsilon_t/(1+\beta)$.
> - Key result (7.16): $y_t = y_p + \beta\epsilon_t/(1+\beta)$.
> - **Only $\epsilon_t$ moves output**; systematic policy is impotent.
> - Sargent–Wallace (**1976**), via Sheffrin (1996).

### Connections
- Builds on: Lucas Supply Function (this chunk), REH (this chunk), AS-AD model (Chunk 002).
- Critiqued by: Keynesians (this chunk).
- Extends to: random walk of consumption, Ricardian Equivalence (mentioned, not derived).

### Open Questions
1. Why does it take "several years" for booms/recessions to play out if information is plentiful? (Keynesian critique — left open in the unit.)
2. How would the result change if fiscal policy were also incorporated?
