# Chunk 004 — Unit 17: Theory of Monetary Policy (Pt 1)
<!-- Pages: 28-37 -->
<!-- Source: chunk_004.txt -->

## Section: Introduction — Three Themes 🟢

### Core Idea
Unit 17 examines the conduct of monetary policy through three lenses. First, the **rules vs discretion debate**: discretion is often arbitrary and suffers from policy lags, while rules (defined variously by Friedman, Barro, and new-Keynesians) generally outperform. Second, the **consensus view**: monetary policy can pin down inflation but cannot lift output above its natural level — a revival of Friedman's neutrality idea. Third, **criticism of the consensus**: if natural output is itself endogenous to demand, activist policy regains effectiveness.

### Key Concepts

#### Why Discretion is Problematic
- Often misplaced (e.g., expansionary stance when contraction is needed).
- Generates **lags** of three types:
  1. **Identification lag** — recognising the problem.
  2. **Decision lag** — deciding the response.
  3. **Implementation lag** — putting the response into effect.

#### Three Definitions of "Rules"
| Author / school | Rule |
|-----------------|------|
| **Friedman** | Constant rate of growth of money supply over time |
| **Robert Barro** | Commitment to zero/low inflation policy |
| **New-Keynesians** | Equations linking the central bank's policy rate to deviations from inflation and output targets |

#### Three Themes Compared
| Theme | Key claim |
|-------|-----------|
| **Rules vs discretion** | Rules superior; but suffer from **dynamic inconsistency** |
| **Consensus view** | Monetary policy fixes inflation; cannot influence output (fixed at natural level) |
| **Criticism (path dependence)** | Natural output is endogenous; high AD raises both actual and natural output |

> **Quick Recall:**
> - Discretion has 3 lags: **identification, decision, implementation**.
> - Rules: Friedman = constant money growth; Barro = zero inflation; new-Keynesian = policy-rate equations.
> - Consensus view = money is *neutral* (Friedman idea revived); critics counter with path dependence.

---

## Section: Friedman's Prescriptions for Monetary Policy 🟡

### Core Idea
Friedman (1968) argued first that there is no long-run trade-off between inflation and unemployment — pushing output above its natural level only generates inflation. Second, he distrusted central-bank discretion (citing the Federal Reserve's contraction during the Great Depression and tendencies toward over-correction) and proposed a publicly announced rule of **steady money-supply growth**. While most modern central banks reject Friedman's confidence in fixing money supply and his pessimism about inflation targeting, they share his preference for **rules over discretion**.

### Key Concepts

#### Friedman's Two Big Claims
1. **No long-run inflation–unemployment trade-off**: attempts to push output above its 'natural' level just yield more inflation. *(This part of his analysis still drives the modern consensus.)*
2. **Constant money-growth rule**: superior to inflation/price-level rules because *we cannot accurately predict either the size or timing of monetary effects on prices*.

#### Where Mainstream Disagrees
- Modern economists doubt central banks' ability to fix money supply.
- They are *not* pessimistic about inflation targeting.

#### Where Mainstream Agrees
- Rules > discretion.

> **Quick Recall:**
> - **Friedman**: no long-run trade-off + constant money-growth rule.
> - Mainstream: keeps **rules > discretion** but uses inflation targeting, not money growth.

### Connections
- Builds on: Money Neutrality debate (Chunk 002).

---

## Section: Loss Function of the Central Bank 🔴

### Core Idea
Barro and Gordon's framework formalises monetary policy as the central bank minimising a **loss function** — welfare cost rises when inflation differs from its target *and* when output differs from a desired target above the natural level. The bank's optimal choice must lie on the **Phillips Curve**, which links actual inflation to expected inflation and the output gap.

### Key Concepts

#### The Loss Function
$$L = x^2 + (y - y'')^2 \quad \dots (17.1)$$

| Symbol | Meaning |
|--------|---------|
| $x$ | Actual inflation rate |
| $y$ | Actual output |
| $y''$ | Output **target** of the central bank |
| $y'$ | Natural output level (full-employment output) |

**Key assumption**: $y'' > y'$ — the central bank targets output *above* the natural level. The bank dislikes any inflation and any deviation of output from its target.

A **higher L** = greater welfare loss for the economy.

#### The Phillips Curve
$$x = x^e + e(y - y') \quad \dots (17.2)$$

- $x^e$ = expected inflation.
- $e$ > 0 (slope parameter).
- Actual inflation exceeds expected inflation when actual output exceeds natural output.

#### The Optimisation Problem
- Central bank minimises L subject to the Phillips Curve.
- Achieved by varying money supply or interest rate.
- Analogy: like a consumer's utility maximisation. Just as a consumer reaches the highest indifference curve given a budget constraint, the central bank reaches the **lowest loss function** given the Phillips Curve.

#### Geometric Interpretation (Fig. 17.1)
- Loss-function contours = **concentric circles centred at B (the "bliss point")**.
  - Bliss point B: zero inflation **and** output at target $y''$.
  - Larger circle = greater welfare cost.
- On the vertical axis: output is at natural level → actual = expected inflation.
- Phillips Curve is upward-sloping (output rises with inflation).

#### First-Order Condition at Optimum
At the optimum, slope of loss function = slope of Phillips Curve. If $e$ is the PC slope:
$$e = \frac{(y'' - y)}{x}$$
(verifiable by totally differentiating eq. 17.1 and setting dL = 0). Hence:
$$ex = y'' - y \quad \dots (17.3)$$

Multiplying both sides by $e$ and adding (17.2):
$$x = \frac{x^e + e(y'' - y')}{1 + e^2} \quad \dots (17.4)$$

**Interpretation**: The central bank's choice of inflation rate varies *positively* with both its output target ($y''$) and the public's expected inflation ($x^e$).

### Definitions ⭐
- **Loss function (of central bank)**: $L = x^2 + (y - y'')^2$ — welfare cost rising with inflation and with deviation of output from target.
- **Natural output ($y'$)**: output produced when labour force is fully employed.
- **Output target ($y''$)**: output level the central bank aims for; assumed > $y'$.
- **Bliss point (B)**: combination of zero inflation and output at $y''$ — minimum possible loss.

### ⚠️ Common Mistakes
- ❌ Treating $y''$ as equal to $y'$ → ✅ Model assumes $y'' > y'$ — that gap is the source of inflationary bias.
- ❌ Forgetting that the optimisation is *constrained* by the Phillips Curve → ✅ The central bank cannot arbitrarily pick (x, y).

> **Quick Recall:**
> - Loss function: $L = x^2 + (y - y'')^2$.
> - Phillips Curve: $x = x^e + e(y - y')$.
> - Optimum condition: $ex = y'' - y$.
> - **Bliss point** = (0 inflation, $y''$). Loss-contours = concentric circles around B.

---

## Section: Rules vs Discretion (Discretionary Outcome) 🔴

### Core Idea
With **rational expectations**, the public anticipates the central bank's optimisation. So expected inflation equals the actual inflation the bank chooses. Solving this fixed point gives the **discretionary outcome**: a positive inflation rate that *fails* to push output above its natural level. The central bank's attempt to surprise the public produces only inflation, not real growth.

### Key Concepts

#### Endogenising Expectations (Rational Expectations)
Public knows the central bank minimises L subject to PC. So:
$$x = x^e = \frac{x^e + e(y'' - y')}{1 + e^2} \quad \dots (17.5)$$

Solving:
$$x = x^e = \frac{y'' - y'}{e} \quad \dots (17.6)$$

#### Discretionary Outcome — Key Features
- Inflation rate is **endogenous** under discretion.
- Higher output target ($y''$) → higher inflation.
- Output is **NOT** stepped above its natural level.
- Reason: output rises only via *inflation surprise*; with rational expectations, no surprise possible.
- The discretionary outcome is point **A** in Fig. 17.1, where:
  1. Slope of loss function = slope of Phillips Curve.
  2. Actual inflation = expected inflation.

> **Quick Recall:**
> - Discretionary inflation: $x = (y'' - y')/e$.
> - Output stays at natural level; only inflation rises.
> - Rational expectations + minimisation → discretion produces **inflation bias**.

---

## Section: Rules-Based Solution and Dynamic Inconsistency 🔴

### Core Idea
If the central bank declares a "**zero inflation rule**", and the public believes it, the rule-based solution achieves the same output (natural level) at *zero* inflation — clearly superior. But once expectations are anchored at zero, the bank can do better still by *cheating*: violating the rule to create an inflation surprise that lifts output. This is **dynamic inconsistency** — the rule is optimal *ex ante* but not *ex post*. The fix mainstream economists propose is to **delegate** monetary policy to a conservative central banker who weights inflation control more heavily.

### Key Concepts

#### The Zero Inflation Rule (Rules Solution)
$$x_r = x^e = 0 \quad \dots (17.7)$$
where subscript r = "rule".

#### Comparison: Rule vs Discretion
| Aspect | Discretion | Rule (zero-inflation) |
|--------|-----------|----------------------|
| Inflation | $(y'' - y')/e > 0$ | 0 |
| Output | Natural level $y'$ | Natural level $y'$ |
| Welfare cost | Higher | Lower |
| Position in Fig. 17.1 | Point A | Point O (origin) |

**Conclusion**: Rule-based solution is welfare-superior because it produces the same output at lower inflation.

#### Cheating Solution
Public anchors expectations at $x^e = 0$. Bank then minimises L given $x^e = 0$. From eq. (17.5) with $x^e = 0$:
$$x_c = \frac{e(y'' - y')}{1 + e^2} \quad \dots (17.8)$$

(c = "cheating".)

Since $y'' > y'$, $x_c > 0$. Output rises above natural level (because actual inflation > expected). Bank is *better off* at point C than at O (the rule).

#### Dynamic Inconsistency — The Core Insight
- Rules superior to discretion.
- BUT once the rule is announced, the central bank has *incentive to violate it*.
- If it cheats, public learns the bank applies discretion → bank is forced back to the discretionary outcome (point A).
- **Final state after cheating**: inflation with no gain in output. Worst of both worlds.
- Therefore: such a shift in policy must be avoided.

#### Solution: Delegation to a Conservative Central Banker
**Rogoff's model**: delegate policy to an individual whose loss function is:
$$L = \alpha x^2 + (y - y'')^2 \quad \dots (17.9)$$
where $\alpha > 1$.

The conservative banker minimises (17.9) subject to (17.2). Solution under discretion:
$$x = \frac{y'' - y'}{e \alpha} \quad \dots (17.10)$$

Since $\alpha > 1$, inflation **falls** under delegation (compare with eq. 17.6).

**Conditions for delegation to work:**
1. Banker's loss function must place a higher weight on inflation than the government's.
2. **Banker must be independent of government control**.
3. If government is equally inflation-averse, nothing is gained.

### Definitions ⭐
- **Dynamic Inconsistency**: a policy is dynamically inconsistent if, having announced a rule, the central bank subsequently finds it optimal to violate the rule.
- **Cheating outcome**: violating an announced rule to exploit anchored expectations.
- **Delegation to a conservative central banker**: assigning monetary policy to an independent agent who places more weight on inflation control than the government does (Rogoff).

### ⚠️ Common Mistakes
- ❌ Thinking dynamic inconsistency means the rule is bad → ✅ The rule is *optimal*; the bank's incentive to deviate is the problem.
- ❌ Believing delegation works regardless of independence → ✅ Without independence, government's preferences seep through and gains are lost.
- ❌ Confusing the cheating outcome (C) with the long-run equilibrium → ✅ Once trust is lost, economy lands at A (discretionary outcome).

### Edge Cases & Caveats
- Public's belief in the rule is fragile: a single break can reset expectations to discretion.
- Welfare ranking: **Rule (O) > Cheating (C) > Discretion (A)**.

> **Quick Recall:**
> - Rules-based: $x_r = x^e = 0$ → point O.
> - Cheating: $x_c = e(y'' - y')/(1 + e^2) > 0$ → point C.
> - Discretion: $x = (y'' - y')/e$ → point A.
> - **Welfare**: O (best) > C > A (worst).
> - Solution to dynamic inconsistency: **delegate to independent conservative banker** (Rogoff).
> - With $\alpha > 1$ in loss function, inflation under delegation = $(y'' - y')/(e\alpha)$ — strictly lower.

### Connections
- Builds on: Money Neutrality / Policy Ineffectiveness (Chunk 002).
- Builds on: Friedman's prescriptions (Chunk 004).

### Open Questions
1. Is the RBI fully "independent" enough for the Rogoff prescription to bite? (Open question linking to MPFA — Chunk 003.)
2. What happens when the public's expectations adjust slowly (adaptive rather than rational)?

---

## Section: Consensus View of Monetary Policy 🔴

### Core Idea
The modern **consensus** sees the central bank's main *instrument* as the **interest rate** (not money supply, as in older textbooks): the policy rate (e.g. RBI's repo rate) is set, and money supply adjusts endogenously. The bank pursues two objectives — keep inflation at a pre-defined target $x'$ and keep output at its natural level $y'$. The framework uses an **interest-rate rule (Taylor's rule)**, an **IS curve**, and an **accelerationist Phillips curve** to derive an aggregate-demand schedule.

> **In Simple Terms:** Modern central banks don't directly fix the *quantity* of money; they fix the *price* of it (interest rate). They raise rates when inflation or output rises above target — exactly what you'd see in any RBI Monetary Policy Committee announcement.

### Key Concepts

#### Old vs New Consensus
| | Old textbook view | New consensus |
|---|---|---|
| **Main instrument** | Money supply | **Interest rate** |
| **Endogenous variable** | Interest rate | Money supply |
| **Mechanism** | Money demand × supply → interest rate | Central bank fixes policy rate; money supply adjusts |

The relevant variable for AD is the **real interest rate** = nominal rate − expected inflation. The central bank can influence the short-term real rate by varying the short-term nominal rate.

#### Taylor's Rule ⭐
$$r = r' + a(x - x') + b(y - y') \quad \dots (17.11)$$

| Symbol | Meaning |
|--------|---------|
| $r$ | Real rate of interest (set by central bank) |
| $r'$ | Neutral / natural rate of interest |
| $x'$ | Inflation target |
| $y'$ | Natural output |
| $a, b$ | Both positive |

- Rate is positively related to **inflation gap** ($x - x'$) and **output gap** ($y - y'$).
- When both gaps are zero, $r = r'$.
- **You can verify this in RBI Monetary Policy Committee decisions.**

#### IS Curve
$$y - y' = c - dr \quad \dots (17.12)$$

- Output gap responds **negatively** to real interest rate.
- $c$ captures other factors: fiscal policy and external demand.
- $c, d > 0$.
- **Neutral rate of interest**: rate at which output gap = 0, i.e. $r = c/d$.

#### Accelerationist Phillips Curve
$$\Delta x = e(y - y') \quad \dots (17.13)$$

- $\Delta$ is the difference operator (change between two periods).
- Inflation **accelerates** when output is above natural level (demand-pull).
- $e > 0$.
- **Origin**: equation (17.13) is the **adaptive expectations** version of equation (17.2) — i.e., public expects last year's inflation rate.

#### The AD Curve (Aggregate Demand Schedule)
By substituting (17.12) into (17.11) and solving for y:
$$y = y' + \left[\frac{c - dr' + dax'}{1 + bd}\right] - \frac{dax}{1 + bd} \quad \dots (17.14)$$

- AD slopes downward (negative coefficient on x).
- Equilibrium: at the point on AD where output and inflation hit their respective targets.

#### Equilibrium Condition
At equilibrium ($y = y'$, $x = x'$, no tendency to change):
$$r' = c/d \quad \dots (17.15)$$
$$r = r' = c/d \quad \dots (17.16)$$

The central bank must set $r'$ equal to the **neutral rate of interest**. This is hard in practice — the bank may not know the IS-curve parameters and may over- or under-estimate the neutral rate.

#### Off-Equilibrium Dynamics (Fig. 17.2, AD line)
If $r'$ is set correctly, AD passes through $(y', x')$. From any starting point on AD:
- **Left of $(y', x')$** (point B): $y < y'$ → inflation falling → bank cuts $r$ → AD expands → economy moves south-east toward $(y', x')$. Note: at B, *actual* $r >$ neutral $r$.
- **Right of $(y', x')$**: $y > y'$ → inflation rising → bank raises $r$ → economy moves north-west toward $(y', x')$. Actual $r <$ neutral $r$.

If $r' \ne c/d$, AD shifts to $AD'$ — the economy will find $x \ne x'$ when $y = y'$.

### Definitions ⭐
- **Taylor's Rule** ⭐: $r = r' + a(x - x') + b(y - y')$ — the policy rule linking the central bank's interest rate to inflation and output gaps.
- **Neutral rate of interest** ⭐: the rate at which the output gap is zero; $r' = c/d$ from the IS curve.
- **Accelerationist Phillips Curve**: $\Delta x = e(y - y')$ — inflation *accelerates* (rather than just exceeds expectations) when output is above natural level. Adaptive-expectations version of the original PC.
- **Aggregate Demand (AD) curve** (consensus model): the locus of $(y, x)$ combinations consistent with the IS curve and the Taylor-rule reaction function (eq. 17.14).
- **Nominal anchor**: monetary policy's role of providing a credible inflation target around which expectations form.

### ⚠️ Common Mistakes
- ❌ Treating the central bank as a money-supply-setter → ✅ In the consensus, it sets the **interest rate**.
- ❌ Confusing $r'$ (parameter chosen by bank) with $c/d$ (neutral rate from IS) → ✅ At equilibrium they must equal; if not, $x \ne x'$.
- ❌ Confusing the Phillips Curve in (17.2) with (17.13) → ✅ (17.13) is the *adaptive-expectations / accelerationist* version.

### Edge Cases & Caveats
- The bank may not know the true IS-curve parameters → may misset $r'$ → economy lands on $AD'$ rather than AD.
- Under accelerationist PC, even small persistent output gaps drive ongoing inflation acceleration/deceleration.

> **Quick Recall:**
> - **Taylor rule**: $r = r' + a(x - x') + b(y - y')$.
> - **IS curve**: $y - y' = c - dr$.
> - **Accelerationist PC**: $\Delta x = e(y - y')$.
> - **Neutral rate**: $r' = c/d$ (output gap zero).
> - At equilibrium: $y = y'$, $x = x'$, $r = r' = c/d$.
> - Modern view: interest rate is exogenous, money supply is endogenous.

### Connections
- Builds on: Loss Function and Phillips Curve (Chunk 004).
- Builds on: Transmission Mechanism — Interest Rate Channel (Chunk 003).
- Continues into: Policy experiments — higher inflation target and expansionary fiscal policy (Chunk 005).

<!-- Continues in chunk 005 -->

### Open Questions
1. How can a central bank reliably estimate the neutral rate of interest in a developing economy?
2. Under accelerationist PC, why is even a temporary positive output gap so dangerous?
