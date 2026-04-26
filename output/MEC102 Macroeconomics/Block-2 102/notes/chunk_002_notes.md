# Chunk 002 — Unit 6 Sum-Up & Unit 7 Foundations: AS-AD, Lucas Critique, Perfect Foresight
<!-- Pages: 10-19 -->
<!-- Source: chunk_002.txt -->

## Section: Unit 6 — Let Us Sum Up & Closing Concepts 🟡
<!-- Continues from Chunk 001 — Phillips Curve discussion -->

### Core Idea
Unit 6 closes by re-emphasizing the social and economic costs of unemployment, contrasting classical and Keynesian assumptions about wage/price flexibility, and summarizing the key takeaway: the simple Phillips curve trade-off is a **short-run** phenomenon that vanishes in the long run once expectations adjust.

> **In Simple Terms:** The unit's parting message is that the inflation–unemployment "menu" only exists when people don't see what's coming. The moment expectations catch up, the menu disappears.

### Key Concepts

#### Unemployment as a macro and micro problem
- **Macro level**: loss of *potential output*.
- **Individual level**: loss of *income*.
- Widespread unemployment causes **social stigma and psychological trauma**, pushing policy makers to act.

#### Classical vs. Keynesian assumptions

| Assumption | Classical | Keynesian |
|------------|-----------|-----------|
| Real wage and price flexibility | Yes — fully flexible | No — sticky |
| Full employment outcome | Always | Possible to deviate |
| Unemployment in the model | Voluntary at most | Possible (sticky-price) |

#### Summary of expectations-augmented Phillips curve
- **Adaptive expectations** → SRPC stable in short run, **LRPC vertical** in long run; trade-off only in short run.
- **Rational expectations** → no trade-off at all; any anticipated government policy to lower unemployment becomes ineffective because people forecast the change correctly.

### Definitions (recap of CYP 2 Q3)
- **Adaptive Expectations**: expectations are revised on the basis of past observed values of the variable. ⭐
- **Rational Expectations**: expectations formed using all available information and the true economic model. ⭐
- **NAIRU**: rate of unemployment at which inflation is stable; departures cause acceleration/deceleration. ⭐
- **Long-Run Phillips Curve (LRPC)**: vertical line at $u^*$ showing no inflation–unemployment trade-off in the long run. ⭐

> **Quick Recall:**
> - Classicals → flexible wages & prices → automatic full employment.
> - Keynesians → sticky wages & prices → unemployment possible.
> - 1970s stagflation discredited the simple Phillips curve.
> - Adaptive: short-run trade-off only. Rational: no trade-off if policy is anticipated.

### Connections
- Continues from: Phillips Curve & Expectation-Augmented PC sections (Chunk 001).
- Sets up: full formal treatment of Rational Expectations Hypothesis in Unit 7.

---

## Section: Unit 7 — Introduction to Rational Expectations 🟡

### Core Idea
Many economic decisions hinge on **expected** values of variables, not current ones — Friedman's permanent income hypothesis (consumption depends on expected/permanent income), labour supply (depends on expected real wages because nominal wages are fixed *before* work, while prices are realized *afterwards*). How agents form these expectations is therefore central to macroeconomics. Unit 7 introduces the **rational expectations** approach as the new-classical alternative to adaptive expectations.

> **In Simple Terms:** If everyone forecasts using last year's weather only, they'll keep getting blindsided by storms. If they instead use the actual weather model and current information, their forecasts will be wrong only by random noise. That's the leap from adaptive to rational expectations.

### Key Concepts

#### Why expectations matter — examples
- **Permanent income hypothesis (Friedman)**: a tax cut raises consumption only if perceived as **permanent**, not temporary.
- **Labour supply**: workers negotiate **nominal** wages now but receive them later → real wages = nominal/aggregate price level depends on **future** price level; labour effort depends on **expected real wages**.

#### Classical vs. neo-classical view of money
| Framework | Money's effect on real variables |
|-----------|----------------------------------|
| Classical | **Neutral** — affects only nominal variables |
| Neo-classical (AS-AD) | **Non-neutral in the short run** — there's a lag between expected and actual real wages |

#### "Fooling models"
- Initial impact of ↑ money supply: ↑ goods demand → ↑ prices → ↑ nominal wages.
- **Workers** are "fooled" — they think nominal wage rise = real wage rise; they offer more labour.
- **Firms** are NOT fooled — they realize real wages have fallen; they hire more workers.
- Hence the asymmetry of information between firms and workers — a key feature of the AS-AD short-run story.

#### Roadmap to Unit 7 (sets up later sections)
1. **AS-AD model & non-neutrality of money** in the short run.
2. **Lucas Critique** — why fooled-worker stories cannot persist.
3. **Perfect foresight** as the limit case where money is neutral even in the short run.
4. **Rational Expectations Hypothesis (REH)** — the formal model of expectations.
5. **Lucas Supply Function** — supply-side justification for short-run non-neutrality.
6. **Policy Ineffectiveness Theorem** — only unanticipated money matters for output.

#### New-classical setting vs. classical setting
- **Classical**: perfect information, perfectly flexible wages/prices, instantaneous market-clearing → full employment.
- **New-classical (rational expectations)**: allows **imperfect information** (agents have **local**, not global, information). Workers and firms know their own wages/prices but not the aggregate price level.
- Crucially, new-classical RE models do **NOT** rely on **asymmetric** information across agents — workers and firms are fooled equally (unlike AS-AD).

### Definitions
- **Rational expectations**: the value a variable will take in the future, formed by incorporating *all* information about the variable and knowing the true model that explains it. ⭐ (exam-important)
- **Perfect foresight**: rational expectations + zero random component, so expected value = actual value.
- **Permanent income hypothesis**: consumption depends on permanent (expected long-run) income, not current income.
- **Money neutrality**: a change in the money supply affects only nominal variables; real variables remain unchanged.

> **Quick Recall:**
> - Classicals: money is **neutral**.
> - AS-AD short run: money is **NOT neutral** — workers fooled.
> - Rational expectations come from new-classical economics.
> - In RE models with local-only info, **both** workers and firms can be symmetrically fooled.

### Connections
- Builds on: Adaptive vs. Rational expectations (Chunk 001).
- Sets up: AS-AD analysis (this chunk), Lucas Critique (this chunk), REH (Chunk 003).

---

## Section: 7.2 AS-AD Model and Non-Neutrality of Money 🔴

### Core Idea
The AS-AD framework formalizes how an unexpected change in money supply can move output and employment in the short run, even though money is neutral in the long run. The mechanism turns on the gap between actual prices ($P$) and expected prices ($P^e$): when $P > P^e$, real wages have effectively fallen, firms hire more, workers (mistakenly) supply more, and output rises above the natural level. As workers update $P^e$ towards $P$, the AS curve shifts up iteratively until $P = P^e$ and output returns to $Y_N$.

> **In Simple Terms:** A monetary boost first jolts the economy because workers haven't yet noticed that prices are also rising. As they figure it out, wage demands catch up and the boost fades. The "long run" arrives the moment expectations are right again.

### Key Concepts

#### Aggregate Demand (AD) function
$$Y = f(G, T, M/P)$$

- Increasing in **G** (government expenditure), **T** (taxes — note book's wording), and **M/P** (real money balances).
- AD curve is **downward-sloping** in $(P, Y)$ space: lower $P$ → higher real money balances → lower interest rates → higher investment → higher AD.

#### Aggregate Supply (AS) — derivation
1. **Wage equation**: $W = P^e f(u, z)$, where $W$ = wage, $P^e$ = expected price, $u$ = unemployment, $z$ = other factors.
2. **Price-setting (cost-plus)**: $P = (1 + m)W$, where $m$ = mark-up (lower for more competitive economy).

Combining:
$$P = P^e (1+m) f(u, z) = P^e (1+m) f\left(1 - \tfrac{Y}{L}, z\right)$$

(using $u = 1 - Y/L$ and the simple production function $Y = N$, $L$ = labour force).

#### When $P = P^e$ (long run)
- Real wage is what firms and workers jointly determine in the labour market given $u$ and $z$.
- The resulting unemployment rate is the **natural rate of unemployment**.
- Any gap between $P$ and $P^e$ closes over time as workers reduce expectational errors → natural rate prevails in the long run.

#### When $P \neq P^e$ (short run)
- Workers' expected real wages aren't met → AS curve shifts → output deviates from the natural level $Y_N$.

#### Iterative adjustment to a money supply shock (Fig. 7.1)
Starting at $(AD_0, AS_0)$, $Y = Y_N$, $P = P^e = P_0$. Then ↑ M:
1. AD shifts right: $AD_0 \rightarrow AD_1$.
2. New short-run equilibrium: $Y_1 > Y_N$, $P_1 > P_0$.
3. Workers initially keep $P^e = P_0$ (adaptive); they're fooled into supplying more labour.
4. When workers spend wages, they realize $P_1 > P_0$ → demand higher nominal wages → AS shifts up to $AS_2$ ($P^e = P_1$).
5. New equilibrium: $P_2 > P_1$, $Y_2 < Y_1$ but $Y_2 > Y_N$ (still short run).
6. Process iterates until AS reaches $AS_f$ where $P = P^e$ again, output returns to $Y_N$, but at a permanently higher price level.

#### "Modified" Phillips curve restatement
- Price expectations rise when $P > P^e$.
- Therefore only an **unexpected** price rise (above what was expected) raises employment / output.
- In these AS-AD fooling models, **firms know real wages have fallen; workers don't** → asymmetric information.

#### Adaptive expectations in this model
- The model assumes $P^e_t = P_{t-1}$ — workers form expectations from the **past period's** price.
- This is a form of **adaptive expectations**.

### Mechanisms / Processes
$$\uparrow M \rightarrow AD \uparrow \rightarrow P \uparrow \;(P > P^e) \rightarrow W/P \downarrow \rightarrow N \uparrow,\; Y \uparrow \rightarrow \text{workers update } P^e \rightarrow AS \uparrow \rightarrow \text{repeat until } P = P^e,\; Y = Y_N$$

### Definitions
- **Aggregate Demand function**: $Y = f(G, T, M/P)$, downward sloping in $(P, Y)$. ⭐
- **Aggregate Supply function**: $P = P^e(1+m)f(u, z)$ — derived from wage equation and cost-plus pricing. ⭐
- **Mark-up ($m$)**: price-cost margin in the price-setting equation; lower for more competitive economies.
- **Natural rate of unemployment (in AS-AD)**: rate prevailing when $P = P^e$.

### ⚠️ Common Mistakes
- ❌ Mistake: assuming AD is downward-sloping because of the law of demand → ✅ Correct: it slopes down via the **real money balance / interest rate / investment** channel.
- ❌ Mistake: thinking firms are fooled in the AS-AD short run → ✅ Correct: only **workers** are fooled; firms know real wages have fallen and hire more.

> **Quick Recall:**
> - $AS$: $P = P^e(1+m)f(u, z)$.
> - $AD$: $Y = f(G, T, M/P)$.
> - Short run: $P \neq P^e$ → output deviates from $Y_N$.
> - Long run: $P = P^e$ → output back at $Y_N$.
> - In AS-AD, expectation rule is $P^e_t = P_{t-1}$ — adaptive.

### Connections
- Builds on: Expectation-Augmented Phillips Curve (Chunk 001).
- Contrasts with: Lucas Supply Curve (Chunk 003) where workers AND firms are symmetrically fooled.

---

## Section: 7.3 The Lucas Critique 🔴

### Core Idea
**John Muth (1961)** introduced the rational-expectations concept; **Robert E. Lucas** and **Thomas Sargent** brought it into economics in the 1970s. The Lucas Critique argues that statistical relationships from past data rest on a *given* policy environment. When the policy environment changes, agents revise expectations, and the past relationships **no longer hold**. So policy makers cannot assume past relationships are stable parameters — they are **endogenous** to policy.

> **In Simple Terms:** If you've always given a child cookies after dinner, you can predict they'll eat dinner quickly. The moment you announce no more cookies, the prediction breaks. Past data was conditional on the cookie policy, not a law of nature.

### Key Concepts

#### Why "fooling" can't last
In the AS-AD story, repeated rounds of ↑M-induced inflation should teach workers that increases in money supply are persistently followed by price rises. After observing several such episodes, why would workers keep underestimating future prices?

Lucas's answer: **they wouldn't.** Sensible forecasts must be made on the basis of:
- The **true model / actual process** generating prices.
- **All relevant information** that comes up.

Hence past inflation expectations of "zero" cannot remain stable under a policy that systematically raises prices.

#### The critique formally
> Past statistical relationships in data rest on certain expectations. When the policy environment changes, expectations change, and the past statistical relationships may no longer hold.

#### Worked illustration 1 — expansionary money
- Policy maker increases growth of money supply.
- Expected price = $P_0$, actual price = $P_1 > P_0$.
- Agents adapt: next period's expectation $= P_1$.
- Actual price now $P_2 > P_1$ → workers still trail behind → real wages still falling.
- This "fooling" is *exactly* what Lucas questions.

#### Worked illustration 2 — disinflation announcement
- Government announces it will reduce inflation by slowing money supply growth, and people **believe** it (past credibility).
- Rational agents incorporate the announcement → reduce expected price → reduce nominal wage demands.
- When actual prices fall, **real wages don't rise** and unemployment doesn't rise either.
- Disinflation can be costless if credible.

### Mechanisms / Processes
1. Past data → estimated relationship (e.g., Phillips curve).
2. Policy maker exploits relationship → policy environment changes.
3. Agents update expectations using the new policy environment.
4. The estimated relationship breaks down → policy fails.

### ⚠️ Common Mistakes
- ❌ Mistake: thinking the Lucas Critique just means "models are wrong" → ✅ Correct: it specifically says **estimated parameters are not invariant** to policy regime changes.
- ❌ Mistake: applying the critique only to monetary policy → ✅ Correct: it generalizes to any policy that changes the environment in which agents form expectations.

### Definitions
- **Lucas Critique**: past statistical relationships in macroeconomic data are based on a particular set of expectations under a given policy regime; once the policy environment changes, those expectations and relationships change. ⭐ (exam-important)

> **Quick Recall:**
> - Concept: Muth (1961). Brought into economics: **Lucas & Sargent**, 1970s.
> - Past relationships ≠ structural laws — they are **conditional on the policy regime**.
> - Credible disinflation announcements can be costless under rational expectations.

### Connections
- Critiques: AS-AD adaptive-expectations story (this chunk).
- Sets up: REH (Chunk 003), Lucas Supply Function (Chunk 003), Policy Ineffectiveness Theorem (Chunk 003).

---

## Section: 7.4 Perfect Foresight and the Neutrality of Money 🟡

### Core Idea
**Perfect foresight** is the extreme case where agents know the AS-AD model's equations and parameters and can therefore set $P^e$ exactly equal to $P$. Combined with full wage/price flexibility, this restores classical money neutrality even in the short run: monetary changes flow instantly into prices, real wages stay put, employment stays at the natural rate.

> **In Simple Terms:** If you can read the magician's mind in real time, the trick never works on you. Perfect foresight is mind-reading; money's "tricks" stop working.

### Key Concepts

#### Conditions for money neutrality even in the short run
1. Agents know the **true model** (equations + parameters) determining $P$.
2. So they can compute $P^e = P$ — no expectational error.
3. Wages and prices are **fully flexible**.
4. → Real wage stays at the desired level.
5. → Employment stays at the natural rate.
6. → ↑M flows entirely into proportional ↑P; no real effects.

#### Outcome on the AS-AD diagram (Fig. 7.1)
If $P^e = P$, output stays at $Y_N$. The price level rises in proportion to the increase in $M$. **No role for monetary policy** — every announced policy is instantly priced in. Only nominal variables move.

#### Why the real world isn't perfect-foresight
- Economic variables are influenced by **human behaviour with random elements**.
- Therefore agents at best have **rational expectations**, not perfect foresight.
- This motivates the formal REH (next section).

### Definitions
- **Perfect foresight**: a state in which the AS-AD model's equations and parameters are known so that $P^e = P$ always; expectational error $= 0$; money is neutral even in the short run. ⭐
- **Money neutrality (perfect foresight)**: changes in $M$ change only nominal variables proportionately; real variables unchanged.

### ⚠️ Common Mistakes
- ❌ Mistake: equating perfect foresight with rational expectations → ✅ Correct: perfect foresight has **no random component**; rational expectations does, with random error mean = 0.
- ❌ Mistake: thinking perfect foresight requires only knowing past data → ✅ Correct: it requires knowing the **true model** AND having flexible wages/prices.

> **Quick Recall:**
> - Perfect foresight $\Rightarrow$ $P^e = P$ exactly.
> - Money is neutral **even in the short run**.
> - Real world ≠ perfect foresight → use rational expectations as the realistic limit.

### Connections
- Contrasts with: AS-AD model with adaptive expectations (this chunk).
- Sets up: Rational Expectations Hypothesis (Chunk 003).

---

## Section: 7.5 Rational Expectations Hypothesis (REH) — Setup 🔴
<!-- Continues into Chunk 003 -->

### Core Idea
The REH replaces ad-hoc forecasting (astrology, dart-throwing, raw past trends, naive adaptive updating) with a method that uses the **true data-generating process** of the variable. Agents are assumed to know the explanatory factors and the systematic way they enter the model, so they can predict everything that is *predictable*. Any remaining error is purely random.

> **In Simple Terms:** Stop guessing tomorrow's bus arrival time from yesterday's lateness. Look up the bus schedule, the traffic patterns, the driver's break times — that's the model. Your prediction will be right on average; only random delays remain.

### Key Concepts

#### The "true model" — algebraic representation
$$Y_t = \alpha + \beta X_{t-1} + \gamma Y_{t-1} + \eta Z_{t-1} \qquad \text{(7.1)}$$

where $Y_t$ is the actual value at time $t$, dependent on observed values at $(t-1)$ of variables $X$, $Y$, $Z$. $\alpha$ is a constant; $\beta, \gamma, \eta$ are coefficients.

This is a **deterministic** model — RHS variables completely determine $Y_t$.

#### Mathematical expectation under perfect foresight
$$E_{t-1}Y_t = \alpha + \beta X_{t-1} + \gamma Y_{t-1} + \eta Z_{t-1} \qquad \text{(7.2)}$$

Equation (7.1) is therefore a **perfect-foresight** model: expectational error = $Y_t - Y^e_t = 0$.

#### Perfect-foresight illustration
With perfect foresight, expected price following ↑M is an **equi-proportionate** increase in the price level.

#### Bridge to RE (continues in Chunk 003)
The next step is to add a **random term $\nu_t$** to the deterministic model — that's where rational expectations diverge from perfect foresight. <!-- Continues in chunk 003 -->

### Definitions
- **Rational Expectations Hypothesis (REH)**: agents form expectations using the true data-generating process of the variable, including all systematic explanatory factors. ⭐ (exam-important)
- **Perfect foresight (formal)**: the case where the true model has no random component, so $E_{t-1}Y_t = Y_t$ exactly; $\nu_t = 0$.

> **Quick Recall:**
> - REH uses the **true model**, not past trends.
> - Equation (7.1): $Y_t = \alpha + \beta X_{t-1} + \gamma Y_{t-1} + \eta Z_{t-1}$ — deterministic.
> - Perfect foresight = REH minus the random component.

### Connections
- Builds on: Lucas Critique (this chunk), Perfect Foresight (this chunk).
- Continues into: random component, expectational error properties, microfoundations (Chunk 003).

### Open Questions
1. How does the addition of $\nu_t$ change the welfare and predictability properties of REH? (Answered in Chunk 003.)
