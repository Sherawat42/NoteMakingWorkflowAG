# Chunk 004 — Two-Period Labour Supply, Supply Shocks, New-Keynesian View
<!-- Pages: 31-35 -->
<!-- Source: chunk_004.txt -->

## Section: Two-Period Inter-temporal Labour Supply 🔴
<!-- See chunk 003 for start of this section -->
<!-- Reason: Unit objective "explain the inter-temporal substitution in labour supply"; Check Your Progress 2 Q2, Q3, Q4 -->

### Core Idea
Extending the household problem from one period (where labour supply was wage-independent) to **two periods** shows that **relative wages** and the **interest rate** *do* affect labour supply across time. The household optimises consumption and labour in both periods under a lifetime budget constraint; the FOCs yield a clean expression for the **ratio of labour supplies** in the two periods as a function of the **relative wage** and **interest rate**.

> **In Simple Terms:** When the household lives for two periods, "work now vs work later" becomes a real choice. If the wage is higher today than tomorrow, work more today. If interest rates rise, also work more today (earn now, save now, enjoy later).

### Key Concepts

#### Setup (two-period household)
- One member, no initial wealth, lives two periods.
- No uncertainty about interest rate or second-period wage.
- Lifetime budget constraint:

```
c₁ + (1/(1+r))·c₂ = w₁·ℓ₁ + (1/(1+r))·w₂·ℓ₂          ... (12.16)
```

where r = real interest rate.

#### Lagrangian
```
ζ = ln c₁ + b·ln(1 − ℓ₁) + e^(−ρ)·[ln c₂ + b·ln(1 − ℓ₂)]
    + λ[w₁ℓ₁ + (1/(1+r))·w₂ℓ₂ − c₁ − (1/(1+r))·c₂]    ... (12.17)
```

Choice variables: c₁, c₂, ℓ₁, ℓ₂.

#### First-order conditions for ℓ₁ and ℓ₂

```
b/(1 − ℓ₁) = λ·w₁                                    ... (12.18)
e^(−ρ)·b/(1 − ℓ₂) = (1/(1+r))·λ·w₂                   ... (12.19)
```

Divide (12.18) by w₁ and (12.19) by w₂/(1+r) to isolate λ:

```
b/[(1 − ℓ₁)·w₁] = λ
e^(−ρ)·b·(1+r)/[(1 − ℓ₂)·w₂] = λ                     ... (12.20)
```

Set the two expressions for λ equal and rearrange.

#### The relative-labour-supply equation

```
(1 − ℓ₁) / (1 − ℓ₂) = [b / (e^(−ρ)·b·(1+r))] · (w₂/w₁)
                    = [1 / (e^(−ρ)·(1+r))] · (w₂/w₁)     ... (12.21)
```

(Note: source text writes "(1−r)" in some places where "(1+r)" is intended — the derivation flow makes 1+r the consistent reading.)

#### What the equation tells us

(1 − ℓ₁) is *leisure* in period 1. So the equation relates **relative leisure** and equivalently **relative labour supply** to the relative wage and the interest rate.

##### Effect of a relative wage rise
If **w₁ rises relative to w₂**:
- Then ℓ₁ must increase (leisure (1 − ℓ₁) must decrease) to satisfy (12.21).
- ⇒ Labour supply rises in period 1 relative to period 2 — the household substitutes leisure between time periods to capture the higher first-period wage.
- The **elasticity of substitution** between leisure in the two time periods is **1** (because of log utility).

##### Effect of an interest-rate rise
If **r rises**:
- The right-hand side falls relative to the left (since (1+r) is in the denominator), so labour supply in period 1 must rise relative to period 2.
- Intuition: a higher r increases the incentive to **work more, earn more, and save more** in period 1 because saved earnings grow faster.
- This is why interest rates matter for cyclical employment.

#### What "inter-temporal substitution in labour supply" means
The effect of *relative wage* and *interest rate* on labour supply (or employment or leisure) is called **inter-temporal substitution in labour supply**.

### Definitions
- **Inter-temporal substitution in labour supply (full)**: The shifting of labour supply across time periods in response to changes in *relative wages* and the *interest rate*. ⭐ (exam-important)
- **Elasticity of substitution between leisure in two periods**: Equals **1** under logarithmic utility — a 1% change in the relative wage produces a 1% change in relative leisure. ⭐ (exam-important)

### Mechanisms / Processes

**Wage rise in period 1 chain:**
w₁/w₂ ↑ → ℓ₁ ↑ relative to ℓ₂ → labour supply ↑ in period 1 → output ↑ in period 1 → expansion (or boom) phase

**Interest-rate rise in period 1 chain:**
r ↑ → incentive to save ↑ → work more in period 1 → labour supply in period 1 ↑ relative to period 2 → output ↑ in period 1

### Examples
**Example: Calculation flow for the relative labour-supply equation.**
1. Lifetime budget constraint (12.16).
2. Set up Lagrangian (12.17).
3. Take FOCs for ℓ₁ (12.18) and ℓ₂ (12.19).
4. Divide each FOC by the corresponding wage so λ stands alone (12.20).
5. Equate the two expressions for λ and rearrange to get (12.21).

This is the derivation a student is expected to reproduce per Check Your Progress 2 Q2 and Q3.

### ⚠️ Common Mistakes
- ❌ Mistake: A higher interest rate decreases labour supply in period 1. → ✅ Correct: A higher r raises the *return to saving*, so households work *more* in period 1 to earn and save more.
- ❌ Mistake: The static one-period result (wage doesn't matter) carries over to two periods. → ✅ Correct: Once the household lives two periods, *relative* wages and interest enter the labour-supply decision.
- ❌ Mistake: Inter-temporal substitution depends only on wages. → ✅ Correct: It depends on both relative wages **and** the interest rate.

> **Quick Recall:**
> - (1 − ℓ₁)/(1 − ℓ₂) = [1/(e^(−ρ)·(1+r))] · (w₂/w₁)
> - w₁/w₂ ↑ ⇒ ℓ₁ ↑ relative to ℓ₂
> - r ↑ ⇒ ℓ₁ ↑ relative to ℓ₂ (work more now to save more)
> - Elasticity of substitution between period leisures = 1 (log utility)
> - Static (1-period) result: wage irrelevant; dynamic (2-period): wage and r both matter

### Connections
- Builds on: Inter-temporal Substitution Setup (Chunk 003) — the static case.
- Is prerequisite for: Impact of Supply Shocks (next section) — labour-supply response to productivity shocks operates through this mechanism.

---

## Section: Impact of Supply Shocks to the Economy 🔴
<!-- Reason: Unit objective "assess the role of supply shocks"; Check Your Progress 3 Q1; central RBC mechanism -->

### Core Idea
A favourable, exogenous, **temporary** technology shock raises Aₜ in equation (12.1), which shifts the production function upward and makes it *steeper*. Marginal productivity of labour rises, so output rises at the existing labour input and rises further if labour input also expands. Households save part of the windfall — leading to higher capital stock in future periods. **Permanent** shocks behave differently: lower incentive to save, more consumption, and possibly smaller increase in labour input — but capital and employment still rise persistently.

> **In Simple Terms:** A productivity shock is like a sudden upgrade to the economy's machines. Workers get more productive (steeper production function), so firms pay more, hire more, and produce more. Households save part of the bonus, which means more machines tomorrow — the boom doesn't end overnight.

### Key Concepts

#### Mechanics of a temporary positive technology shock (Fig. 12.2)
- Initial level of technology: A₀ₜ → production function: Kₜ^α · (A₀ₜ Lₜ)^(1−α).
- L₀ is the optimal labour at this level → equilibrium output Y₀.
- Shock raises technology to A₁ₜ → production function shifts upward to Kₜ^α · (A₁ₜ Lₜ)^(1−α).
- The shifted production function is **steeper** at any L → marginal product of labour ↑.
- **At the same labour input L₀** → output rises from Y₀ to Y₁′.
- **If labour input rises to L₁** → output rises further to Y₁.
- The favourable shock thus shifts the *entire production possibilities frontier*.

#### Distribution of the increased output (saving vs consumption)
- One possibility: consume all of the increase. Unlikely for a *temporary* shock — households want to save part for future consumption.
- If saving rises, equation (12.2) implies investment rises.
- Higher investment → higher capital stock in next and future periods.
- Therefore: **temporary technology shock → higher future capital stock**.

#### Permanent shock — different response
A permanent (or long-lasting) shock causes higher output for a longer period. So:
- Incentive to save *falls* (no need to smooth a one-off windfall).
- Consumption *rises*.
- Increase in labour input may not be high.
- Nevertheless, a *persistent* productivity shock causes increases in output, capital stock, and employment.

| Shock type | Saving | Consumption | Labour input change | Capital stock |
|------------|--------|-------------|---------------------|---------------|
| Temporary positive | ↑ (smooth windfall) | small ↑ | ↑ | ↑ in future |
| Permanent positive | small/no ↑ (no need to smooth) | ↑↑ | smaller ↑ | ↑ persistently |

#### Persistence in RBC
The effect of technology shocks *persists* even after the shock ends, because optimising agents adjust capital, employment, and consumption gradually. This is RBC's answer to *why business cycles last so long*.

#### Keynesian criticism of RBC's persistence claim
Keynesian economists argue this persistence story **cannot explain the persistence of real-world business cycles**. RBC believers counter that the dynamic responses of optimising agents to changes in economic conditions have *sustained effects* that explain periods of persistently high or low activity.

### Definitions
- **Temporary supply shock**: A productivity shock lasting one period; households respond by saving part of the windfall.
- **Permanent supply shock**: A long-lasting shock to productivity; households consume more and save less because there is no need to smooth.
- **Persistence (in RBC)**: The property that shocks have *sustained* effects on output, capital, and employment because optimising agents adjust gradually. ⭐ (exam-important)

### Mechanisms / Processes

**Temporary positive technology shock (full chain):**
A₀ₜ → A₁ₜ (rise) → production function shifts up + steeper → MP_L ↑ → at L₀, Y₀ → Y₁′ → if L rises to L₁, Y rises further to Y₁ → households save part → I ↑ → K_(t+1) ↑ → boom persists into future periods even after shock ends

**Adverse temporary supply shock (recap from Chunk 003):**
A ↓ → MP_L ↓ → labour demand ↓ → real wage ↓ → labour supply ↓ → output ↓ → recession

### Examples
**Example: Effect of a positive technology shock (Fig. 12.2 in source).**
- Pre-shock: production function K^α·(A₀L)^(1−α); equilibrium at L₀, Y₀.
- Post-shock: production function K^α·(A₁L)^(1−α); same L₀ produces Y₁′ > Y₀; raising labour to L₁ produces Y₁ > Y₁′.
- Income distribution: part to consumption, part to saving → investment ↑ → future K ↑.

### ⚠️ Common Mistakes
- ❌ Mistake: Temporary and permanent shocks have the same effect on consumption. → ✅ Correct: Permanent shocks raise consumption *more* (no smoothing needed); temporary shocks raise saving more.
- ❌ Mistake: A positive shock only shifts the production function up — slope is unchanged. → ✅ Correct: The production function also becomes *steeper* (marginal product of labour rises).
- ❌ Mistake: After the shock ends, the economy returns instantly to pre-shock state. → ✅ Correct: There is **persistence** — capital accumulated during the shock keeps output and employment elevated.

> **Quick Recall:**
> - Positive shock: production function shifts up *and* gets steeper
> - Same L₀ → higher Y (Y₀ → Y₁′); more L (L₁) → even higher Y (Y₁)
> - Temporary shock ⇒ households save → future K ↑ → persistence
> - Permanent shock ⇒ households consume more, save less, smaller L change, but persistent ↑ in Y, K, employment
> - Keynesian criticism: persistence story can't fully explain real-world cycle length
> - RBC counter: dynamic responses of optimisers create sustained effects

### Connections
- Builds on: Real Factors vs Monetary Factors and Baseline RBC Model (Chunk 003).
- Builds on: Two-Period Inter-temporal Labour Supply (this chunk) — labour responds to wage and interest changes triggered by the shock.

---

## Section: New-Keynesian View on Business Cycle 🔴
<!-- Reason: Unit objective "discuss new-Keynesian approach"; Check Your Progress 3 Q2 -->

### Core Idea
**New-Keynesian macroeconomics** keeps Keynes' central insight (market imperfections, sticky wages and prices, activist government role) but addresses Lucas's two main criticisms by adding **microfoundation** and **rational expectations** — and adopting **DSGE models**. Methodologically it looks much like new-classical macro; the key differences are *imperfect competition* and *price/wage rigidities*, captured by price-setting and wage-setting equations with adjustment costs (e.g., menu costs), mark-ups, and a Taylor-rule-type interest-rate policy.

> **In Simple Terms:** New-Keynesians say: "We agree with the math (microfoundations, rational expectations, DSGE) but we don't agree that prices adjust instantly. Real businesses face menu costs, mark-up power, and sticky wages — once you put those in, government policy regains its bite."

### Key Concepts

#### Where new-Keynesian comes from
- **New-classical assumption:** continuous market clearing → perfect competition + flexible wages and prices → adjustments instantaneous (this also matched classical economics).
- **Keynes' departure:** rejected the above — emphasised market imperfections; advocated an *activist* role for government.
- **Lucas's two criticisms of Keynes:** (i) no microfoundation; (ii) does not take expectations about future prices into account.

**New-Keynesian fix:** include microfoundation and rational expectations *while retaining* market imperfections and price/wage rigidities → DSGE models with frictions.

#### Methodology vs assumptions
| Dimension | New-Classical | New-Keynesian |
|-----------|--------------|---------------|
| Microfoundation | Yes | Yes |
| Rational expectations | Yes | Yes |
| DSGE framework | Yes | Yes |
| Continuous market clearing | Yes (flexible prices/wages) | **No** — sticky prices/wages |
| Imperfect competition | No | **Yes** |
| Use of menu costs / mark-ups / Taylor rule | No (typically) | **Yes** |

So methodology is largely shared; the *key* contrast is in market clearing assumptions.

#### What new-Keynesian DSGE models include
To bring imperfections into DSGE, new-Keynesians add:
- **Price-setting and wage-setting equations** (rather than instantaneous adjustment).
- **Adjustment costs** such as **menu costs** in wage setting.
- **Mark-up in price setting** (a measure of market imperfection / imperfect competition).
- **Some form of Taylor Rule** for interest rate setting (a policy rule).

### Definitions
- **New-Keynesian economics**: A macroeconomic school that combines microfoundation and rational expectations with sticky prices/wages and imperfect competition; uses DSGE models with frictions. ⭐ (exam-important)
- **Menu costs**: Adjustment costs faced by firms in changing posted prices or wages — one micro reason for nominal rigidity. ⭐ (exam-important)
- **Mark-up (in price setting)**: A wedge between price and marginal cost reflecting imperfect competition; introduced into new-Keynesian DSGE to capture market imperfection. ⭐ (exam-important)
- **Taylor Rule**: A policy rule for setting the central-bank interest rate, included in new-Keynesian DSGE models as the monetary-policy block. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: New-Keynesian and new-classical models are methodologically incompatible. → ✅ Correct: They share microfoundation, rational expectations, and DSGE structure; the difference lies in market clearing and imperfections.
- ❌ Mistake: New-Keynesian retains old Keynesian assumption that agents are non-optimising. → ✅ Correct: New-Keynesian agents *are* rational optimisers — but the markets they operate in have rigidities and imperfect competition.

> **Quick Recall:**
> - New-Keynesian fixes Lucas's criticisms while keeping Keynesian rigidities
> - Three retained Keynesian features: market imperfections, sticky prices, sticky wages
> - Three adopted new-classical tools: microfoundation, rational expectations, DSGE
> - DSGE add-ons: menu costs, mark-ups, Taylor rule
> - Difference from new-classical = market clearing assumption (NK rejects continuous clearing)

### Connections
- Contrasts with: New-Classical View on Business Cycle (Chunk 003) — same methodology, different market-clearing assumption.
- Contrasts with: Real Business Cycle theory (Chunk 003) — RBC is a strict-clearing branch of new-classical; NK is the rigidity-friendly response.

---

## Section: Unit 12 Summary 🟢

### Core Idea
RBC theory rests on microeconomic foundations: it analyses firm behaviour through production functions and household behaviour through consumption-leisure substitution, all within a general-equilibrium framework with rational expectations. New-Keynesian macroeconomics challenges RBC's continuous-market-clearing assumption and incorporates adjustment costs, staggered prices, and mark-up pricing into DSGE models.

### Key Concepts

#### What RBC is, in one paragraph
- Microfoundation: production function for firms; consumption function with labour-leisure substitution for households.
- Rational expectations: agents optimise with all available information.
- General equilibrium framework for empirical estimation.
- Source of cycles: real shocks, especially productivity.

#### What new-Keynesian adds
While adopting microfoundation, rational expectations, and the general-equilibrium framework, new-Keynesian economists incorporate:
- Adjustment costs
- Staggered prices
- Mark-up pricing
into DSGE (DGSE in source) models.

> **Quick Recall:**
> - RBC = microfoundation + rational expectations + GE + real shocks + market clearing
> - New-Keynesian = microfoundation + rational expectations + GE + market imperfections (adjustment costs, staggered prices, mark-ups)
