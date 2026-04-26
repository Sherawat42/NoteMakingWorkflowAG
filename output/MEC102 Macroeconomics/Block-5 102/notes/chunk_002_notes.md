# Chunk 002 — Wage Rigidity, Efficiency Wage Model, Contracting & Insider-Outsider, Unit 13 Wrap-up
<!-- Pages: 11-22 -->
<!-- Source: chunk_002.txt -->

## Section: New-Keynesian Theories of Wage Rigidity 🔴

### Core Idea
The labour market has two stylised facts that any theory must explain: (1) **persistent unemployment**, and (2) **moderately pro-cyclical real wages** — when demand rises, employment goes up a lot and real wages go up a little. The original Keynesian model (constant nominal wage W) wrongly predicts **counter-cyclical** real wages; New Keynesian theories correct this by predicting mildly pro-cyclical real wages, matching the data.

> **In Simple Terms:** Old Keynesianism said "fix nominal wages and you're done." But that wrongly implies real wages fall in booms (because P rises). The data say real wages mildly *rise* in booms. New Keynesian theories had to do better — and they do.

### Key Concepts

#### Why old Keynesian fails on wage cyclicality
With nominal wage W fixed, real wage W/P moves *opposite* to P. In a boom, P rises → W/P falls → counter-cyclical real wage. In contraction, P falls → W/P rises. Empirically wrong: real wages in fact rise mildly in booms and fall in recessions (mildly pro-cyclical).

| Model | Predicted real-wage cyclicality | Matches data? |
|-------|--------------------------------|---------------|
| Classical | Real wage flexes with employment, equals MPL | Partial |
| Old Keynesian (W fixed) | Counter-cyclical (W/P falls in booms) | ❌ |
| New Keynesian | Mildly pro-cyclical | ✅ |

> **Quick Recall:**
> - Two facts to explain: persistent unemployment + mildly pro-cyclical real wages.
> - Old Keynesian: gets unemployment right, gets wage cyclicality wrong.
> - New Keynesian: gets both right — that's the advance.

### Connections
- Builds on: Real Rigidities in the Labour Market (Chunk 001)
- Continues into: Efficiency-Wage Theories (next section)

---

## Section: Efficiency-Wage Theories 🔴

### Core Idea
Efficiency-wage theories are **non-Walrasian**: they postulate that firms voluntarily pay real wages **above** market-clearing because doing so raises worker efficiency more than it raises wage costs. The unemployment that results is the natural by-product — there are simply more workers willing to work at the high wage than firms are willing to hire.

> **In Simple Terms:** Pay your workers a premium and they work harder, attract better candidates, stay loyal, and don't slack off. The premium more than pays for itself — but it leaves some willing workers without jobs.

### Key Concepts

#### Four reasons firms pay above-market wages
1. **Higher consumption → higher productivity (nutrition argument)**: Especially in low-income economies, higher wages let workers eat better, stay healthier, and work harder.
2. **Selection on reservation wage**: A higher wage attracts workers with higher reservation wages, who tend to have higher (unobservable) abilities — so the firm gets a better-quality applicant pool.
3. **Loyalty / morale / fair-wage**: A premium wage builds loyalty and effort. The flip side: under-paying produces anger, sabotage, revenge.
4. **Anti-shirking (Shapiro–Stiglitz logic)**: When effort cannot be monitored perfectly, paying above-market wages gives workers something to lose if caught shirking — the alternative job pays only the lower market-clearing wage.

### Definitions
- **Efficiency wage**: a real wage paid above market-clearing because higher wages raise effort/efficiency by more than the wage cost. ⭐ (exam-important)
- **Reservation wage**: the minimum wage at which a worker is willing to supply labour. ⭐
- **Non-Walrasian theory**: any theory in which markets do not clear; here, the labour market with persistent unemployment. ⭐

> **Quick Recall:**
> - Efficiency wage = chosen, voluntary, above-market real wage.
> - Four motives: nutrition, selection, loyalty, anti-shirking.
> - Result: persistent involuntary unemployment.

### Connections
- Builds on: Real wage rigidity (Section 13.5.3, Chunk 001)
- Is foundation for: Efficiency Wage Model (next section)

---

## Section: Efficiency Wage Model — An Example (Romer 2001) 🔴

### Core Idea
A formal one-firm model with effort as a function of the real wage. Profit-maximisation gives a clean condition: **the optimal wage is set where the elasticity of effort with respect to the wage equals one**. At that point, the firm minimises the per-unit cost of *effective* labour. This single condition explains efficiency-wage rigidity, persistent unemployment, and price stickiness — all together.

> **In Simple Terms:** The firm doesn't ask "how cheap can I get a worker?" but "how cheap can I get a unit of effort?" That's a different number, and it's set higher than the market-clearing wage.

### Key Concepts

#### 13.8.1 Specification
- M identical firms, N identical workers.
- Single-input Neo-Classical production function: **Y = F(e·L)**, where L = physical workers hired, e = effort per worker, e·L = effective (efficiency) labour.
- Effort function: **e = e(w)** — effort is an increasing function of the real wage.
- F'(·) > 0, F''(·) < 0 (positive but diminishing marginal product of efficiency labour).
- Each of N workers supplies one unit of labour inelastically — higher wage raises effort, *not* hours.

#### 13.8.2 Solution
Profit: π = Y − w·L = F(e(w)·L) − w·L. Choose w and L to maximise.

The first-order condition with respect to L (after manipulation) gives the **Solow condition**:

**w · e'(w) / e(w) = 1**

i.e., the **elasticity of effort with respect to the wage equals 1** at the optimum.

**Economic interpretation**: w/e(w) is the cost per *efficiency unit* of labour. The firm picks w to **minimise w/e(w)** — getting the most effective labour per rupee. At the optimum:
- For w below optimum: ↑w yields more-than-proportional ↑e (still gaining)
- For w above optimum: ↑w yields less-than-proportional ↑e (now losing)
- At optimum: marginal product of effective labour = its cost

#### 13.8.3 Implications
Let **w*** and **L*** be the optimum. Total demand for labour = M·L*.

**(i) Unemployment can persist**: If N > M·L*, there are more workers than jobs at wage w*. Workers willing to work for less can't push the wage down — w* is set by effort considerations, not market-clearing. (If N < M·L*, wage is bid up above w* and there's no unemployment.)

**(ii) No real-wage response to demand shocks**: An increase in aggregate demand does *not* raise w* — the efficiency wage depends only on the effort function, not on demand conditions. So a demand shock raises **employment**, not real wages. This rationalises the empirical fact that real wages are only mildly pro-cyclical.

**(iii) Price rigidity is implied**: Since real wage and effort don't change in upswings, **labour costs don't change**, so price-setting firms have no incentive to adjust prices. Efficiency-wage rigidity → cost rigidity → price rigidity.

#### 13.8.4 Extensions of the model
The simple e = e(w) model has a flaw: it predicts *no* trend in the real wage in the long run, contradicting the empirical secular rise in real wages. Fix: extend the effort function to **e = e(w, w', u)**, where:
- w' = real wage available in alternative firms
- u = unemployment rate
- e is increasing in w, increasing in u, decreasing in w'

**Logic**: The threat of getting caught shirking only bites if (a) other firms pay less (w' low) and (b) you can't quickly find another job (u high). If w' is high and u is low, getting fired is no punishment, so high wages don't deter shirking.

In equilibrium with identical firms, w = w'. Unemployment can still arise if firms' total demand for L is below total supply of L at the common efficiency wage. The extended model produces the right short-run/long-run pattern: short-run demand shocks → larger employment effect; long-run growth → trend rise in real wages.

### Definitions
- **Effort function e(w)**: per-worker effort as an increasing function of the real wage. ⭐
- **Solow condition / first-order condition**: w·e'(w)/e(w) = 1 — elasticity of effort with respect to wage equals one at the optimum. ⭐ (exam-important)
- **Per-unit cost of effective labour**: w/e(w); the firm chooses w to minimise this. ⭐
- **Extended effort function**: e(w, w', u) — effort depends on own wage, alternative wage, and unemployment rate. ⭐

### Mechanisms / Processes
1. Firm specifies effort function e(w)
2. Maximises π = F(e(w)·L) − w·L over (w, L)
3. FOC w.r.t. L gives w·e'(w)/e(w) = 1
4. This determines w* independently of demand
5. L* determined by F'(e·L) = w/e (marginal product of effective labour = its cost)
6. Aggregate demand for labour = M·L*
7. If N > M·L* → involuntary unemployment at w*

### Examples
**Worked example: interpreting the FOC**
- Suppose at w = ₹100, e(w) = 50, e'(w) = 0.5. Elasticity = 100·0.5/50 = 1. ✓ At optimum.
- Cost per efficiency unit = w/e(w) = 100/50 = 2.
- If w were ₹80 with e = 30, e' = 0.5: elasticity = 80·0.5/30 = 1.33 > 1. Below optimum — raising w further yields more effort gain than cost.
- If w were ₹120 with e = 60, e' = 0.4: elasticity = 120·0.4/60 = 0.8 < 1. Above optimum — raising w further wastes money.

### ⚠️ Common Mistakes
- ❌ Mistake: "The efficiency wage equals the marginal product of labour." → ✅ Correct: It is set by minimising w/e(w); the FOC is about the elasticity of effort, not the value of MPL.
- ❌ Mistake: "Higher demand for output raises efficiency wage." → ✅ Correct: w* depends only on the effort function — demand changes affect L*, not w*.
- ❌ Mistake: "The simple model captures both short and long run." → ✅ Correct: It uniformly predicts employment effects only; the extended model with e(w, w', u) is needed for long-run real-wage trend.

### Edge Cases & Caveats
- If M·L* > N at w*, the wage is bid above w* and unemployment vanishes — the model only explains unemployment in the "excess supply" case.
- The simple model is silent on the long-run secular rise in real wages. The extension repairs this.

> **Quick Recall:**
> - Production: Y = F(e·L)
> - Effort: e = e(w), e increasing in w
> - FOC: **w·e'(w)/e(w) = 1** (elasticity of effort w.r.t. wage = 1)
> - Optimum: minimises w/e(w) (cost per efficiency unit)
> - Extension: e = e(w, w', u) — needed for long-run dynamics
> - Three implications: unemployment persists, no real-wage response to demand, price rigidity implied

### Connections
- Builds on: Efficiency-Wage Theories (previous section)
- Reinforces: Price rigidity from Mankiw model (Chunk 001) — efficiency wages keep marginal costs constant, so prices stay constant
- Contrasts with: Walrasian labour market (always clears via wage adjustment)

---

## Section: Contracting and Insider-Outsider Models 🔴

### Core Idea
Wage rigidity can arise not from efficiency considerations but from **long-term relationships** between firms and workers. Workers stay in jobs for many years (US average ≈ 10 years) because of firm-specific skills and training costs. So wages are set by long-term contracts, not by spot-market clearing. Two contract types: **fixed-wage** (inefficient) and **implicit** (efficient). The **insider-outsider** extension shows why wage bargaining favours the employed at the expense of the unemployed.

> **In Simple Terms:** Workers and firms are stuck with each other for years, so they don't haggle wages every month — they sign contracts. The unemployed have no seat at the table, so wages stay too high and unemployment lingers.

### Key Concepts

#### Why long-term relationships matter
- Many jobs require **firm-specific skills** worth less outside the firm.
- Training new workers each period is **costly**.
- Workers stay if their *long-term* expected earnings exceed outside opportunities, even if current earnings are low.
- US average tenure ≈ 10 years.
- Hence wages don't adjust period-to-period to clear the labour market — labour market is **non-Walrasian**.

#### Two types of contracts

| Aspect | Fixed-wage contract | Implicit contract |
|--------|---------------------|-------------------|
| What's specified | Pre-determined wage; firm chooses employment | Wage AND employment for each state of economy |
| Stated explicitly? | Yes | No (implicit / understood) |
| Pareto efficient? | ❌ No — MPL ≠ marginal disutility | ✅ Yes |
| Wage rigidity implied? | Yes | Yes |
| Unemployment implied? | Yes | Yes |

**Fixed-wage contract**: Wage W is fixed; firm freely chooses employment L given the state of the economy. Workers supply whatever firm demands. When labour demand falls, firms reduce L at fixed W → unemployment. **Inefficient** because at the contract wage, marginal product of labour ≠ marginal disutility of work — a different deal could make both parties better off.

**Implicit contract**: Real-world contracts don't explicitly tie wage and employment to the state of the economy, but behave *as if* they do. The firm specifies (w, L) for each possible state. **Pareto efficient**, but still implies real wage rigidity and the same kind of unemployment consequences.

#### Insider-Outsider Models
Three categories of agents:
- **Firms**
- **Insiders**: currently-employed workers (have bargaining power via unions)
- **Outsiders**: unemployed workers (no bargaining power)

**Key insight**: The unemployed (outsiders) would *like* contracts that lower wages and raise employment. But they aren't at the bargaining table. The deal is struck between firms and insiders, who prefer high wages over high employment. So wages stay rigid and outsiders stay unemployed — a non-Walrasian feature explaining persistent unemployment.

### Definitions
- **Fixed-wage contract**: pre-specified wage; firm chooses employment freely; **inefficient** (MPL ≠ marginal disutility). ⭐
- **Implicit contract**: contract between firm and workers specifying both wage and employment for each state of the economy; not explicitly written but behavioural; **Pareto efficient**. ⭐
- **Pareto efficiency**: a contract is Pareto efficient if it is impossible to make one party better off without making the other worse off. ⭐
- **Insiders**: currently-employed workers, with bargaining power. ⭐
- **Outsiders**: unemployed workers, without bargaining power. ⭐

### ⚠️ Common Mistakes
- ❌ Mistake: "Implicit contracts are inefficient because they're vague." → ✅ Correct: They are *Pareto efficient*; the term "implicit" refers to their unwritten nature, not their efficiency.
- ❌ Mistake: "Fixed-wage contracts give the firm bad outcomes." → ✅ Correct: They are inefficient *for both parties together* — there's a different contract that would make both better off. The inefficiency is joint, not unilateral.
- ❌ Mistake: "Insider-outsider models are about wage discrimination." → ✅ Correct: They're about who has bargaining power — the *unemployed* would lobby for lower wages and more jobs, but they have no voice at the bargaining table.

### Edge Cases & Caveats
- Contracting models depart from efficiency-wage models: efficiency-wage rigidity comes from worker effort; contract rigidity comes from long-term relationships. Both produce real wage rigidity.

> **Quick Recall:**
> - Fixed-wage contract = inefficient (MPL ≠ marginal disutility).
> - Implicit contract = efficient, but *also* implies real wage rigidity.
> - Insider-outsider: insiders + firms bargain; outsiders excluded → wages too high, unemployment persists.

### Connections
- Parallels: Efficiency wage model — both produce non-Walrasian labour market with real-wage rigidity, but for different reasons (effort vs. long-term relations).

---

## Section: Unit 13 Summary 🟢

### Core Idea
Unit 13 explained how the **New Keynesian school** rationalises persistent unemployment using two kinds of rigidities: **nominal rigidities** (Mankiw model — menu costs in monopolistic markets keep nominal prices fixed) and **real rigidities** in goods (countercyclical mark-ups), credit (information asymmetries → credit rationing), and labour markets (efficiency wages, contracts, insider-outsider dynamics).

### Key Concepts (consolidated)
- **Classical vs Keynesian** (and New Classical vs New Keynesian) hinges on flexibility/rigidity.
- **Mankiw model**: menu costs > private re-pricing gain in monopolistic markets → nominal price rigidity → unemployment.
- **Real rigidities**:
  - Goods market: countercyclical mark-ups
  - Credit market: information asymmetries → credit rationing → magnification
  - Labour market: efficiency wages → real-wage rigidity → unemployment
- **Efficiency wage model**: firm sets wage where elasticity of effort equals 1, minimising cost per effective unit of labour. Simple version misses long-run real-wage trend; extended e(w, w', u) version captures both short and long run.
- **Contracting and insider-outsider**: long-term relationships generate non-Walrasian wage rigidity. Fixed-wage contracts are inefficient; implicit contracts are efficient. Insider-outsider explains why wages stay too high — outsiders have no bargaining power.

### Connections
- Continues into: Unit 14 — Search Theory and Unemployment (Chunks 003–004), an alternative explanation for unemployment within a Walrasian setting.
<!-- Continues in chunk 003 -->

> **Quick Recall:**
> - Two pillars of New Keynesian unemployment: nominal rigidity (Mankiw / menu costs) + real rigidity (goods / credit / labour).
> - Three labour-market mechanisms: efficiency wages, contracts, insider-outsider.
