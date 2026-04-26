# Chunk 004 — OLG Model: Structure, Dynamic Inefficiency, Social Security
<!-- Pages: 31-40 -->
<!-- Source: chunk_004.txt -->

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
- Builds on: Structure of OLG model (previous section); golden rule (Chunk 003)
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
- Contrasts with: Ricardian Equivalence in RCK (Chunk 003) — debt-financed government is neutral there but transfers can have real effects in OLG

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
