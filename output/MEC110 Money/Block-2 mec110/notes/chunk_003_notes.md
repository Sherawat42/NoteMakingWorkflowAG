# Chunk 003 — Theories of Money Demand: Quantity Theory, Cambridge, Liquidity Preference, Baumol-Tobin, Tobin & Friedman
<!-- Pages: 21–32 -->
<!-- Source: chunk_003.txt -->

## Section: Quantity Theory of Money (Fisher) 🔴
<!-- See chunk 002 for unit introduction -->
<!-- Reason: foundational named theory, explicit CYP question, derivation included -->

### Core Idea
The **Quantity Theory of Money**, attributed to David Hume and algebraically formalized by **Irving Fisher**, is fundamentally about **money supply**, not demand — but in equilibrium it can be re-arranged to derive money demand. The transactions version states **MV = PT**; the income version (more practical) replaces T with Y: **MV = PY**.

> **In Simple Terms:** It says how much money exists × how fast it changes hands = how much stuff costs × how much stuff gets sold. Once you assume the economy is in equilibrium, you can flip it around to see how much money people want.

### Key Concepts

#### Transaction Version
$$M \times V = P \times T$$

| Symbol | Meaning |
|--------|---------|
| **M** | Quantity of money (money supply) |
| **V** | **Transaction velocity** of money — number of times a rupee changes hands per period |
| **P** | Price per transaction |
| **T** | Number of transactions per period |

**Worked example:** M = ₹25, T = 50 transactions/year, P = ₹5 per transaction → 25V = 5 × 50 = 250 → V = 10. (₹25 must change hands 10 times to support ₹250 of transactions.)

**Practical limitation**: T is impossible to measure in real life → use the income version.

#### Income Version
$$M \times V = P \times Y$$

| Symbol | Meaning |
|--------|---------|
| **M** | Quantity of money |
| **V** | **Income velocity** of money (replaces transaction velocity) |
| **P** | Price level |
| **Y** | Real output |

**Logic of substitution**: T and Y are positively related and proportional, so Y is a workable proxy for T.

#### Deriving Money Demand from the Quantity Theory (Laidler, 1977)
Per Laidler, in equilibrium **money supply = money demand**, so M = Md:
$$M_d \times V = P \times T$$
With V and T constant (V̄, T̄):
$$M_d = P \times \frac{1}{\bar{V}} \times \bar{T}$$
Letting **k = 1/V̄**:
$$M_d = k \times (P \times \bar{T}) = k \times \text{volume of transactions}$$
In the classical framework, T = Y, so:
$$\boxed{M_d = k \times \text{Income}}$$

#### Criticisms of the Quantity Theory

| Critic | Critique |
|--------|----------|
| **J.M. Keynes** (*General Theory*) | Inflation is driven by **aggregate demand**, not money supply. At full employment, AD > AS creates an inflationary gap **independent of money supply changes**. |
| **Paul Krugman** (Nobel laureate) | Theory **fails in a liquidity trap** — when interest rates hit minimum, further fall is unexpected, and monetary policy is ineffective. |
| **Ludwig von Mises** (Austrian-American) | The theory does not focus on the **money demand side** — only equilibrium derivation; not applicable in disequilibrium. |
| Various economists | The quantity theory is dismissed by some as a **tautology** rather than a theory. |

### Definitions
- **Quantity Theory of Money**: MV = PT — relationship between money supply, velocity, price, and transactions. ⭐ (exam-important)
- **Velocity of Money**: Number of times a unit of money is exchanged in a period; transaction velocity (V_T) or income velocity (V_Y).
- **Liquidity Trap**: Situation when interest rate hits its minimum and further fall is not expected — monetary policy becomes ineffective. ⭐ (exam-important)

> **Quick Recall:**
> - **MV = PT** (transactions); **MV = PY** (income).
> - Theory is about supply, but yields Md = kY in equilibrium.
> - 4 critiques: Keynes (AD-driven inflation), Krugman (liquidity trap), Mises (no demand side), tautology charge.

### Connections
- Continues into: Cambridge Approach (next section) — the "demand-side" version.

---

## Section: Cambridge / Neoclassical Approach 🔴
<!-- Reason: named theory, exam-eligible, paired with Fisher in syllabus -->

### Core Idea
The **Cambridge approach** (Marshall, Pigou, Robertson, Keynes) is an improvement over Fisher's quantity theory because it **explicitly models money demand**. Cambridge economists argue that people don't hold all income as cash (cash earns no interest); only a fraction **k** is held for transactions. Hence: **M_d = k(PY)**.

> **In Simple Terms:** Cambridge said, "of every ₹100 you earn, you'll keep some fraction k as cash for transactions and put the rest in interest-bearing assets." That fraction k is the heart of money demand.

### Key Concepts

#### Cambridge Equation
$$M_d = k \times (P \times Y)$$

| Symbol | Meaning |
|--------|---------|
| **M_d** | Money demand |
| **k** | **Cambridge k** — fraction of income held as cash for transactions |
| **P** | Price level |
| **Y** | Real income |

**Cambridge k** is the **reciprocal of k** as defined in the quantity theory's V (where k = 1/V̄). Money supply is determined in equilibrium by setting Md = Ms.

#### Cambridge vs Fisher

| Aspect | Fisher (Quantity Theory) | Cambridge / Neoclassical |
|--------|--------------------------|---------------------------|
| Primary focus | Money supply | Money demand |
| Equation | MV = PT (or PY) | Md = k(PY) |
| Role of k | k = 1/V̄ (derived) | k is a structural constant of demand |
| Money demand | Derived only in equilibrium | Modelled directly |

### Definitions
- **Cambridge k**: Fraction of nominal income (PY) people choose to hold as cash for transactions; reciprocal of velocity (1/V̄). ⭐ (exam-important)
- **Cambridge / Neoclassical Theory of Money Demand**: Md = k(PY). ⭐ (exam-important)

> **Quick Recall:**
> - Md = k(PY).
> - Cambridge k = 1/V̄.
> - Cambridge models demand directly; Fisher derives it only in equilibrium.

### Connections
- Builds on: Quantity Theory (previous section).
- Continues into: Liquidity Preference Theory (next section) — adds non-transactional motives.

---

## Section: Liquidity Preference Theory (Keynes) 🔴
<!-- Reason: cornerstone Keynesian theory, CYP question on three motives, derivation -->

### Core Idea
Keynes' **Liquidity Preference Theory** decomposes money demand into **three motives**: **Transaction (M_d^T), Precautionary (M_d^p), and Speculative (M_d^sp)**. The first two depend on **income**; the third depends on the **interest rate** and operates through bond price expectations. Total Md = αY + βY + (P×W)·f(i).

> **In Simple Terms:** Keynes said you hold cash for three reasons: (1) to pay your bills, (2) for "what if" emergencies, and (3) to wait for a better deal on bonds. Income drives the first two; the interest rate drives the third.

### Key Concepts

#### The Three Motives — Comparison

| Motive | Formula | Driver | Interest sensitivity |
|--------|---------|--------|----------------------|
| **Transaction** (M_d^T) | M_d^T = α(PY) | Income/transactions | Generally inelastic (some economists: elastic above i₃ when opportunity cost is high) |
| **Precautionary** (M_d^p) | M_d^p = β(PY) | Income/uncertainty about future | Generally inelastic (similar caveat as above) |
| **Speculative** (M_d^sp) | M_d^sp = (P×W)·f(i) | Interest rate / bond price expectations | Strongly interest-elastic |

#### 1) Transaction Motive
Need for cash to bridge the gap between **receipts** and **planned regular payments** (school fees, electricity, salaries, rent, loan repayments, etc.). Higher income → higher transaction volume → higher Md.
- Nominal: $M_d^T = \alpha(PY)$
- Real: $M_d^T / P = \alpha Y$
- α = fraction of nominal income demanded for transactions.

#### 2) Precautionary Motive
Holding cash for **unforeseen events** (e.g., death of family member, illness). People save part of income for odd circumstances.
- Nominal: $M_d^p = \beta(PY)$
- Real: $M_d^p / P = \beta Y$
- β = fraction of nominal income demanded for precaution.

#### 3) Speculative Motive — The Bond Market Logic
**Speculation** = profiting from price fluctuations (e.g., buy bond at ₹1000, price rises to ₹1200 in a year → ₹200 capital gain + interest/coupon). For a **perpetual bond**:
$$V = \frac{C}{i}$$
where V = bond value, C = coupon, i = market interest rate.

**Inverse i ↔ V relationship**: ↑ i → ↓ bond price; ↓ i → ↑ bond price.

##### Keynes' Bullish/Bearish Logic
- There is a **normal interest rate**.
- If i > normal → individual expects i to **fall** → expects ↑ bond prices → **bearish on cash** = capital gain + interest → holds **bonds**.
- If i < normal → individual expects i to **rise** → expects ↓ bond prices → **bullish on cash** = capital loss but still earns coupon → holds **bonds only if** coupon > capital loss; otherwise holds **all cash**.
- At aggregate level, individuals' weights smooth out → **aggregate speculative Md = smooth function of i**.

$$M_d^{sp} = (P \times W) \times f(i)$$
where W = real wealth.

#### Total Money Demand (Keynes)
$$M_d = \alpha Y + \beta Y + (P \times W) \times f(i)$$
or:
$$M_d = (\alpha + \beta)Y + (P \times W) \times f(i)$$
**Md is a function of Y, W, and i.**

#### Mankiw's Compact Form
- Nominal: $M_d = P \cdot L(i, Y)$
- Real: $M_d / P = L(i, Y)$

where L(·) captures the liquidity-preference function.

#### Criticisms of Liquidity Preference Theory
1. **Single purse problem**: People don't keep separate purses for each motive; in reality one common balance serves all needs.
2. **Empirical weakness**: Fails to fully explain observed fluctuations in interest rates and money demand. Other factors (inflation expectations, growth, central-bank policy) also drive these.
3. **Homogeneous expectations**: Assumes all individuals share the same interest-rate and income expectations; in reality expectations are heterogeneous.

### Definitions
- **Transaction Motive**: Demand for money to bridge gap between receipts and regular planned payments. ⭐ (exam-important)
- **Precautionary Motive**: Demand for money as a buffer for unforeseen future expenses. ⭐ (exam-important)
- **Speculative Motive**: Demand for money tied to expectations about future interest rates / bond prices. ⭐ (exam-important)
- **Capital Gain**: Profit due to asset price appreciation (e.g., bond price rise).
- **Bullish Expectation**: Expectation of price increase / interest rate fall.
- **Bearish Expectation**: Expectation of price decrease / interest rate rise.
- **Perpetual Bond**: A bond with infinite maturity; V = C/i.

### ⚠️ Common Mistakes
- ❌ Mistake: Saying transaction & precautionary demand depend on i → ✅ Correct: Both are interest-**inelastic** in Keynes (some say elastic above a threshold).
- ❌ Mistake: Confusing bullish/bearish with rate movements directly → ✅ Correct: Bullish on **bonds** = expects bond **prices** to rise = expects **interest rates to fall**.
- ❌ Mistake: Applying V = C/i to all bonds → ✅ Correct: This formula is for **perpetual** bonds (infinite maturity).

> **Quick Recall:**
> - Md = M_d^T + M_d^p + M_d^sp.
> - Transaction & Precautionary = f(Y); Speculative = f(i).
> - Md = αY + βY + (P×W)·f(i).
> - Bond value (perpetual): V = C/i — inverse of interest rate.
> - 3 criticisms: single purse, empirical weakness, homogeneous expectations.

### Connections
- Builds on: Cambridge Approach (transaction k → α here).
- Continues into: Baumol-Tobin (transaction motive made rigorous) and Tobin's speculative model (speculative motive made rigorous).

---

## Section: Baumol-Tobin Model of Transaction Demand 🔴
<!-- Reason: named model, derivation, worked numerical, exam-favourite -->

### Core Idea
Independently developed by **William J. Baumol (1952)** and **James Tobin (1956)**, this model treats cash management like inventory management — analogous to **Economic Order Quantity (EOQ)**. The optimal cash holding minimizes **total cost = transaction cost + opportunity cost of holding money** (forgone interest). The result: optimum number of bank visits Q* = √(iY/2b); average cash holding A = √(bY/2i).

> **In Simple Terms:** Like deciding how often to refill your bike's petrol tank, Baumol-Tobin tells you how often to visit the bank — frequent small withdrawals save interest but cost time/transaction fees, infrequent big withdrawals lose interest. There's a sweet spot.

### Key Concepts

#### Setup
- Annual spending: ₹Y, withdrawn from a bank account paying interest **i**.
- Withdrawals are made in equal lumps; cash is spent at a **constant rate**.
- Each bank visit incurs **transaction cost b** (e.g., travel cost).

#### Average Cash Holding for Q Visits
- 1 visit/year: opens with Y, ends with 0 → average = **Y/2**.
- 2 visits/year: half-year cycles → average = **Y/4**.
- Q visits/year: average = **Y/(2Q)**.

#### Costs
- **Transaction cost** of Q visits: $bQ$.
- **Opportunity cost** (interest forgone on average holding): $\frac{iY}{2Q}$.
- **Total cost**:
$$TC = \frac{iY}{2Q} + bQ$$

#### First-Order Condition (Cost Minimization)
$$\frac{d(TC)}{dQ} = -\frac{iY}{2Q^2} + b = 0$$
$$Q^{*2} = \frac{iY}{2b}$$
$$\boxed{Q^* = \sqrt{\frac{iY}{2b}}}$$

#### Average Money Holding (Optimum)
$$A = \frac{Y}{2Q^*} = \frac{Y}{2}\sqrt{\frac{2b}{iY}}$$
$$\boxed{A = \sqrt{\frac{bY}{2i}}}$$

#### Worked Example (from text)
**Mr. M** wants to spend ₹1,00,000 from bank balance.
- i = 5% = 0.05/year
- b = ₹4 per visit
- $Q^* = \sqrt{\frac{0.05 \times 1{,}00{,}000}{2 \times 4}} = \sqrt{\frac{5000}{8}} = \sqrt{625} = 25$ visits.
- $A = \sqrt{\frac{4 \times 1{,}00{,}000}{2 \times 0.05}} = \sqrt{\frac{4{,}00{,}000}{0.1}} = \sqrt{40{,}00{,}000} = ₹2000$.

#### Verification Table — TC Minimum at Q = 25

| Q | A = Y/2Q | Visit cost (Q×4) | Opportunity cost (A × 0.05) | Total cost |
|---|----------|-------------------|------------------------------|------------|
| 5 | 10000 | 20 | 500.00 | 520.00 |
| 10 | 5000 | 40 | 250.00 | 290.00 |
| 16 | 3125 | 64 | 156.25 | 220.25 |
| 22 | 2273 | 88 | 113.64 | 201.64 |
| **25** | **2000** | **100** | **100.00** | **200.00** ← minimum |
| 28 | 1786 | 112 | 89.29 | 201.29 |
| 34 | 1471 | 136 | 73.53 | 209.53 |
| 49 | 1020 | 196 | 51.02 | 247.02 |

At optimum (Q = 25), **visit cost = opportunity cost = ₹100** — TC curve is at its trough.

#### Comparative Statics
- ↑ i → ↑ Q* (more visits) → ↓ A (less cash held). Higher rates make holding cash costly.
- ↑ Y → ↑ Q* and ↑ A but **square-root relation** (so A grows slower than Y — economies of scale in cash management).
- ↑ b → ↓ Q* and ↑ A. Higher transaction cost ⇒ fewer visits, more cash per visit.

#### Criticisms of Baumol-Tobin
1. Assumes spending happens at **constant rate**, but real spending is uneven and uncertain.
2. **Hard to quantify** transaction costs in practice.

### Definitions
- **Baumol-Tobin Model / Cash Management Model**: Optimal cash-holding model that minimizes total transaction + opportunity cost; A = √(bY/2i). ⭐ (exam-important)
- **EOQ Analogy**: Cash-management problem mirrors inventory-management problem with purchase, order, and carrying costs.

### ⚠️ Common Mistakes
- ❌ Mistake: Mixing up the Q* and A formulas → ✅ Correct: Q* = √(iY/2b), A = √(bY/2i). At optimum, **visit cost = opportunity cost**.
- ❌ Mistake: Saying Md grows linearly in Y → ✅ Correct: Square-root relation — economies of scale.

> **Quick Recall:**
> - **Q* = √(iY/2b)**, **A = √(bY/2i)**.
> - At optimum, transaction cost = opportunity cost.
> - Square-root law → Md grows slower than income.
> - 2 criticisms: constant-rate spending, hard to measure b.

### Connections
- Builds on: Keynes' transaction motive (previous section, this chunk).
- Connects to: Friedman's modern theory (later this chunk) — both treat money like an asset.

---

## Section: Tobin's Theory of Speculative Demand 🔴
<!-- Reason: named theory, portfolio-based, contrasts with Keynes -->

### Core Idea
Tobin (1958, *"Liquidity Preference as Behavior Towards Risk"*) reframed speculative demand as a problem of **portfolio choice under uncertainty**, not interest-rate expectations. Investors hold a **mix of cash and bonds** rather than 100% one or the other (as Keynes assumed). Optimization happens where an indifference curve over (risk, return) is tangent to the linear opportunity locus R = βδ.

> **In Simple Terms:** Tobin disagreed with Keynes' "all-cash or all-bonds" view. He said most people split their portfolio — some cash, some bonds — to balance risk and return like a normal investor.

### Key Concepts

#### Mathematical Setup
- V = value of bonds; r = rate of return; θ = rate of risk.
- **Total return**: $R = rV$
- **Total risk**: $\delta = \theta V$
- Combining: $R = \frac{r}{\theta} \delta$
- Let $\beta = r/\theta$: $R = \beta \delta$ → **linear positive relation between R and δ** (the line **OZ**).

#### Geometric Construction (Figure 5.3 in text)
- **Panel (a)**: Risk (horizontal), Return (vertical).
- IC₁, IC₂ = indifference curves over (risk, return) — higher utility on IC₂.
- Line **OZ** = opportunity set; investor cannot move off it.
- **Optimum at point E** where OZ is tangent to highest reachable IC.
- **Panel (b)**: Wealth axis (vertical) shows the bonds–cash split.
  - At E, bond holding = OD; cash = WD (where W = total wealth).
  - Line **OM** maps each portfolio combination back to a (risk, return) point on OZ.

#### Effect of an Interest-Rate Change
If interest rate **falls** → OZ rotates **clockwise** to OZ' → new tangency at point F (lower IC₁) → bond holding falls to OS, cash rises to WS.

**Result**: ↓ interest rate → ↓ bond holding (OS < OD) → ↑ cash holding → confirms negative relation between interest rate and money demand.

#### Tobin vs Keynes — Key Difference

| Aspect | Keynes (Liquidity Preference) | Tobin (Portfolio Theory) |
|--------|-------------------------------|--------------------------|
| Portfolio choice | All cash OR all bonds (corner solution) | Mix of cash AND bonds (interior solution) |
| Driver | Expectation about future interest rates | Risk-return optimization (uncertainty) |
| Result | Discontinuous demand at individual level | Smooth demand at individual level |

### Definitions
- **Tobin's Theory of Speculative Demand**: Portfolio-choice model where investors hold a mix of cash and bonds; speculative Md is driven by uncertainty (risk preferences), not expectations alone. ⭐ (exam-important)
- **Indifference Curve (over risk-return)**: Combinations of risk and return that yield equal utility; higher curve = higher utility.

> **Quick Recall:**
> - R = βδ, β = r/θ.
> - Optimum where OZ is tangent to highest IC.
> - ↓ i → OZ rotates clockwise → ↓ bonds, ↑ cash.
> - **Tobin: cash + bonds (mix). Keynes: all cash OR all bonds.**

### Connections
- Builds on: Keynes' speculative motive — Tobin generalizes it to portfolio theory.
- Connects to: Modern portfolio theory and the term "liquidity preference as behaviour towards risk".

---

## Section: Friedman's Modern Quantity Theory of Money 🔴
<!-- Reason: named theory, exam target, restatement of QTM -->

### Core Idea
**Milton Friedman** (1976 Nobel laureate) developed a "**modern quantity theory**" — a restatement of the classical theory in **money-demand terms**. He treats money like any other asset and models money demand as a function of permanent income, non-human wealth, returns on multiple alternatives, expected inflation, and tastes.

> **In Simple Terms:** Friedman said: don't treat money as something special — treat it like a stock, a bond, a piece of land. People will hold more of it when its return rises and less when other assets' returns rise.

### Key Concepts

#### Friedman's 1970 Money Demand Function
$$M_d = f(Y_p,\ W,\ i_m,\ i_b,\ i_e,\ \pi^e,\ u) \times P$$

#### Variables Explained

| Symbol | Meaning | Sign of relation with Md |
|--------|---------|---------------------------|
| **P** | Price level | + (↑ P → ↓ real balance → people demand more nominal money) |
| **Y_p** | **Permanent income** — weighted average of past & present incomes; proxy for human wealth (labour earnings) | + (↑ Y_p → ↑ Md) |
| **W** | Non-human wealth (land, machines) | + (more wealth → more money held) |
| **i_m** | Return on money itself | + (↑ i_m → people willing to hold more money) |
| **i_b** | Return on bonds | − (↑ i_b → capital loss / better alternative → ↓ Md) |
| **i_e** | Return on equities | − (↑ i_e → ↑ dividends attract investors → ↓ Md) |
| **π^e** | Expected inflation rate | − (↑ π^e → ↓ purchasing power → spend/invest now → ↓ Md) |
| **u** | All other factors (tastes & preferences) | Either direction |

#### Expected Inflation Formula
$$\pi^e = \frac{1}{P} \cdot \frac{dP^e}{dt}$$

#### Why "Modern" / "Restatement"
- Classical QTM: about money supply.
- Friedman: same equation reframed as **demand for an asset**.
- **Money is just one asset in a wealth portfolio** — same logic as demanding bonds, stocks, land.

#### Friedman vs Keynes

| Aspect | Friedman | Keynes |
|--------|----------|--------|
| View of money | Asset like any other | Special — three motives (T, P, sp) |
| Wealth concept | Permanent income (Y_p) + non-human wealth (W) | Current income (Y) + real wealth (W) |
| Determinants | Y_p, W, i_m, i_b, i_e, π^e, u | i and Y |
| Stability of velocity | Stable (predictable Md) | Unstable (depends on speculative motive) |

### Definitions
- **Friedman's Modern Quantity Theory**: Md = f(Y_p, W, i_m, i_b, i_e, π^e, u) × P — money demand as demand for an asset. ⭐ (exam-important)
- **Permanent Income (Y_p)**: Weighted average of past and present incomes; serves as proxy for human wealth in money-demand functions. ⭐ (exam-important)
- **Non-human Wealth (W)**: Tangible/financial wealth excluding human capital (e.g., land, machines, financial assets).
- **Expected Inflation (π^e)**: Anticipated rate of change of price level.

### ⚠️ Common Mistakes
- ❌ Mistake: Treating Friedman's theory as identical to Fisher's → ✅ Correct: Friedman **restates** it as demand-for-asset; Fisher's is supply-side mechanical.
- ❌ Mistake: Using current income Y in Friedman's function → ✅ Correct: Use **permanent income Y_p**.
- ❌ Mistake: Saying ↑ i_b → ↑ Md → ✅ Correct: ↑ i_b → ↓ Md (bond is more attractive than money).

> **Quick Recall:**
> - Md = f(Y_p, W, i_m, i_b, i_e, π^e, u) × P.
> - Permanent income Y_p replaces current Y.
> - +Md drivers: P, Y_p, W, i_m. −Md drivers: i_b, i_e, π^e.
> - Treats money as an asset → "modern quantity theory".

### Connections
- Builds on: Quantity Theory (Fisher) and Cambridge approach.
- Compares with: Keynes' Liquidity Preference Theory.
