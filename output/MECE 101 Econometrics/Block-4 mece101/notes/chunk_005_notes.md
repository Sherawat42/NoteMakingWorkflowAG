# Chunk 005 — Introduction to Simultaneous Equations Models
<!-- Pages: 41-51 -->
<!-- Source: chunk_005.txt -->
<!-- Continues from: N/A -->

## Section: 16.1 Introduction 🟢

### Core Idea
Unlike single-equation regression models where variables on the right strictly determine the variable on the left, real-world economic relationships often feature simultaneity. This means variables mutually influence each other, requiring a system of simultaneous equations to determine their equilibrium values.

> **In Simple Terms:** Instead of a one-way street where X causes Y, we often see a two-way street where X causes Y, but Y also causes X (like price and demand). To solve these, we need multiple equations working together.

### Key Concepts

#### Simultaneous Relationships
A situation where a single equation under investigation is part of a wider phenomenon. For example, aggregate consumption depends on income, but national income also depends on aggregate consumption. Estimating just one equation independently produces inconsistent and biased results.

### Definitions
- **Simultaneous Equations**: Models where the equations are related and cannot be solved independently because the variables mutually determine one another. ⭐ (exam-important)

### Connections
- Shifts the focus from single-equation extensions (Units 14, 15) to multi-equation systems.

---

## Section: 16.2 Some Examples of Simultaneous Equations Models 🟡

### Core Idea
To illustrate the necessity of simultaneous equations models (SEMs), several classic macroeconomic and microeconomic examples show how ignoring interdependent relationships violates OLS assumptions.

> **In Simple Terms:** If you try to guess the demand for a product using only its price, you'll get the wrong answer because the supply also affects the price. You have to consider both supply and demand at the same time.

### Key Concepts

#### Demand and Supply Model
Equilibrium price and quantity are determined by the intersection of supply and demand. If we estimate only the demand equation (`q = α + βp + u`), the error term `u` will absorb shifts in the supply curve. This makes the price `p` correlated with the error term `u` (violating `cov(X,u)=0`), leading to inconsistent OLS estimates.

#### Wage-Price Model
Money wage depends on unemployment and prices, while prices depend on wages and money supply. Because price enters the wage equation and wage enters the price equation, both are interdependent and stochastic, violating classical OLS assumptions.

#### Keynesian Model of Income Determination
Consumption depends on income (`C = β₀ + β₁Y + u`), but income is defined as Consumption plus Investment (`Y = C + I`). Any shock `u` to consumption affects `Y`, making `Y` correlated with `u`. 

#### Macroeconomic IS Model
A more complex system involving consumption, taxes, investment, and disposable income. Attempting to estimate the consumption function in isolation ignores the fact that national income depends on government expenditure and interest rates.

### Definitions
- **Simultaneous Equations Model (SEM)**: A model consisting of a set of equations that jointly determine the values of several endogenous variables. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Believing you can just run OLS on one part of a simultaneous system if you only care about that one equation. → ✅ Correct: Running OLS on a single equation within a simultaneous system yields biased and inconsistent estimates for that equation's parameters.

> **Quick Recall:**
> - SEMs are needed when variables mutually cause each other.
> - Classic examples: Supply & Demand, Wage-Price, Keynesian Income.
> - Main problem: OLS assumption `cov(X,u) = 0` is violated.

---

## Section: 16.3 Endogenous Variables and Exogenous Variables 🔴

### Core Idea
In simultaneous equations models, variables are strictly categorized based on whether their values are determined within the system or outside of it. Proper classification is crucial for model specification and identification.

> **In Simple Terms:** "Endogenous" means the model figures out the value for you (like price). "Exogenous" means you have to feed the value into the model from the outside world (like rainfall).

### Key Concepts

#### Endogenous Variables
Variables whose values are determined jointly and interdependently within the model. They are determined by the exogenous variables and the model's structure. In SEMs, endogenous variables are regarded as stochastic (random). The number of endogenous variables must equal the number of equations.

#### Predetermined Variables
Variables whose values are determined outside the current time period's equation system. They are regarded as non-stochastic. Predetermined variables include:
1. **Current Exogenous variables**: Determined outside the model entirely (e.g., rainfall, government policy).
2. **Lagged Exogenous variables**: Past values of outside variables (e.g., last year's rainfall).
3. **Lagged Endogenous variables**: Past values of inside variables (e.g., last year's consumption). Because they happened in the past, their values are already known and thus non-stochastic for the current period.

### Definitions
- **Endogenous Variables**: Variables which get determined jointly and interdependently within the model. ⭐ (exam-important)
- **Exogenous Variables**: Variables which get determined outside the model, and independently of the endogenous variables. ⭐ (exam-important)
- **Predetermined Variables**: The combined set of current exogenous, lagged exogenous, and lagged endogenous variables. ⭐ (exam-important)

### Mechanisms / Processes
1. Economic theory dictates which variables are included in the model.
2. The researcher classifies them as endogenous (solved by the model) or predetermined (given as inputs).
3. The model must have as many equations as it has endogenous variables to be completely solvable.

> **Quick Recall:**
> - Endogenous = Determined IN the model (stochastic).
> - Exogenous = Determined OUTSIDE the model (non-stochastic).
> - Predetermined = Exogenous + Lagged variables.

### Connections
- Identifying these variables is the first step required to perform Identification (Chunks 006, 007).
<!-- Continues in chunk 006 -->
