# Chunk 001 — Qualitative Independent Variables in OLS Models
<!-- Pages: 1-10 -->
<!-- Source: chunk_001.txt -->

## Section: 14.1 Introduction 🟢

### Core Idea
A regression model may experience a change in parameters within a sample, known as a structural change, requiring new methods to represent this shift. Additionally, some explanatory variables are qualitative rather than quantitative, and they can be included in regression models using dummy variables.

> **In Simple Terms:** Just like a sudden event (like an economic policy change) can alter how an entire economy behaves, a "structural change" means our data's underlying rules have shifted. To capture yes/no or category-based factors (like gender or policy changes) in math, we use dummy variables.

### Key Concepts

#### Structural Change
Structural change (or structural break) occurs when the parameters of a relationship change within the sample. For example, the relationship between industrial output and inputs might fundamentally change after economic liberalization. 

#### Qualitative Explanatory Variables
Variables that represent attributes or qualities rather than numerical scales (e.g., gender, marital status, religion). They can be incorporated into regression models to understand their specific influence on a dependent variable.

### Definitions
- **Dummy Variables**: Artificial variables constructed to take the value 1 or 0, indicating the presence (1) or absence (0) of a particular attribute. Also known as binary, indicator, categorical, or dichotomous variables. ⭐ (exam-important)

### Mechanisms / Processes
1. Identify a qualitative attribute affecting the dependent variable.
2. Assign a value of 1 for the presence of the attribute and 0 for its absence.
3. Use this dummy variable as an independent variable in the regression model.

### Examples
**Example: Gender and Earning**
If monthly earning depends on gender, a dummy variable can be defined as `D = 1` for male and `D = 0` for female to include it in the regression.

> **Quick Recall:**
> - Structural change means parameters shift within a sample.
> - Qualitative variables are handled using dummy variables (0 and 1).

### Connections
- Introduces concepts that will be tested using the Chow Test (Chunk 001).

---

## Section: 14.2 Chow Test for Structural Stability 🔴

### Core Idea
The Chow test determines if there is a structural change or structural break in a relationship across different subsets of data. It compares an unrestricted model (separate regressions for each subset) against a restricted model (a single combined regression) to see if their parameters significantly differ.

> **In Simple Terms:** The Chow test tells us whether it's better to use one single rule (line) to describe all our data, or if we need two separate rules (lines) because the data behaves differently in two different situations.

### Key Concepts

#### Assumptions of Chow Test
The test relies on two critical assumptions about the error terms in the two sub-samples:
1. The error terms are normally distributed with the same variance: ε₁ ~ N(0, σ²) and ε₂ ~ N(0, σ²).
2. The error terms are independently distributed.

#### Restricted vs Unrestricted Models
- **Restricted Model**: Combines all observations into one single regression, assuming structural stability. Produces RSS_R (Restricted Residual Sum of Squares) with degrees of freedom (n₁ + n₂ - k).
- **Unrestricted Model**: Estimates separate regressions for each subset. Produces RSS_UR = RSS₁ + RSS₂ with degrees of freedom (n₁ + n₂ - 2k).

| Model | Equation | RSS | Degrees of Freedom |
|-------|----------|-----|--------------------|
| Restricted | Y_t = λ₁ + λ₂X_t + ε_t | RSS_R | n₁ + n₂ - k |
| Unrestricted | Y_t = α₁ + α₂X_t + ε_t (Group 1)<br>Y_t = β₁ + β₂X_t + ε_t (Group 2) | RSS_UR = RSS₁ + RSS₂ | n₁ + n₂ - 2k |

### Definitions
- **Structural Break**: Occurs if the parameters underlying a relationship differ from one subset of the data to another. ⭐ (exam-important)

### Mechanisms / Processes
1. Estimate the Restricted Model (combined data) and obtain RSS_R.
2. Estimate the Unrestricted Models (separate regressions) and obtain RSS₁ and RSS₂.
3. Calculate RSS_UR = RSS₁ + RSS₂.
4. Compute the F-ratio: `F = [ (RSS_R - RSS_UR) / k ] / [ RSS_UR / (n₁ + n₂ - 2k) ]`
5. Compare the computed F-value with the critical F-value. If it exceeds the critical value, reject the hypothesis of structural stability.

### Examples
**Example: Savings Rate**
To test if savings rates differ between rich and poor households, we run separate regressions for each group (RSS₁=0.1396, RSS₂=0.1931). Then we run a combined regression (RSS_R=0.5722). Using the F-test formula, we get F = 5.04. Since this exceeds the critical value of 3.74, we conclude the savings functions are structurally different.

### ⚠️ Common Mistakes
- ❌ Mistake: Assuming the Chow test tells us exactly *why* the models differ (intercept vs slope). → ✅ Correct: The Chow test only confirms *if* there is a difference; it does not specify whether the difference is in the intercept, slope, or both. Dummy variables are needed for that.

> **Quick Recall:**
> - Chow test checks for structural stability.
> - `F = [ (RSS_R - RSS_UR) / k ] / [ RSS_UR / (n₁ + n₂ - 2k) ]`
> - Does not specify if the difference is in slope or intercept.

### Connections
- Contrasts with testing through Dummy Variables (Chunk 002) which can isolate intercept vs slope differences.

---

## Section: 14.3 The Nature of Dummy Variables 🔴

### Core Idea
Dummy variables are artificial indicators used to quantify qualitative attributes in regression models. When using multiple categories, a base category must be chosen to avoid perfect multicollinearity, known as the dummy variable trap.

> **In Simple Terms:** Dummy variables are just switches (on/off). If we have multiple categories, we always leave one switch out to serve as our baseline, so we can compare everything else to it.

### Key Concepts

#### Dummy Variable Trap
If a qualitative variable has 'm' categories, you must introduce '(m-1)' dummy variables. If you introduce 'm' dummy variables (e.g., one for male and one for female), it creates perfect linear collinearity, making the regression impossible to estimate. This is the dummy variable trap.

#### Base Category
The category assigned the value 0 is the base or benchmark category. All comparisons and interpretations are made with reference to this category. The assignment of 0 and 1 is arbitrary but crucial for interpreting the coefficients.

### Definitions
- **Differential Intercept Coefficient**: The coefficient attached to the dummy variable. It tells by how much the value of the intercept term of the category receiving value 1 differs from that of the base category. ⭐ (exam-important)
- **Dummy Variable Trap**: A situation of perfect multicollinearity that occurs when too many dummy variables are introduced for a qualitative variable. ⭐ (exam-important)

### Mechanisms / Processes
1. Determine the number of categories 'm' for a qualitative variable.
2. Introduce 'm-1' dummy variables.
3. Choose one category to be the base category (all its dummy values are 0).
4. Interpret the dummy coefficients as the difference from the base category.

### Examples
**Example: Gender**
If gender has 2 categories (male, female), we use 2 - 1 = 1 dummy variable. `D = 1` for male, `D = 0` for female. Female is the base category.

> **Quick Recall:**
> - Rule of thumb: 'm' categories require 'm-1' dummy variables.
> - Dummy Variable Trap = perfect multicollinearity.
> - The coefficient shows the difference from the base category.

### Connections
- Prerequisite for ANOVA and ANCOVA Models (Chunk 001).

---

## Section: 14.3.1 ANOVA Models 🟡

### Core Idea
Analysis of Variance (ANOVA) models in regression analysis are models that contain exclusively qualitative (dummy) explanatory variables.

> **In Simple Terms:** An ANOVA model is a regression where we only use yes/no categories to predict our outcome, like predicting a teacher's salary based solely on whether they are male or female.

### Key Concepts

#### Dummy Variables in ANOVA
In an ANOVA model like `Y_i = α₁ + α₂D_i + u_i`, the intercept `α₁` represents the mean value of the base category (e.g., female teachers where `D_i = 0`). The slope `α₂` represents the differential intercept, and `α₁ + α₂` gives the mean value for the other category.

### Definitions
- **ANOVA Models**: Regression models that contain only dummy explanatory variables. ⭐ (exam-important)

### Examples
**Example: Teacher Salary (Gender Only)**
`Y_i = 18.00 + 3.28 D_i`
Female (D=0) mean salary = 18.00.
Male (D=1) mean salary = 18.00 + 3.28 = 21.28.
We can use a t-test on the `3.28` coefficient to test if the difference is statistically significant.

> **Quick Recall:**
> - ANOVA = Only dummy variables.
> - Intercept = Base category mean.

### Connections
- Contrasts with ANCOVA Models (Chunk 001).

---

## Section: 14.3.2 ANCOVA Models 🟡

### Core Idea
Analysis of Covariance (ANCOVA) models contain a mix of both qualitative (dummy) and quantitative explanatory variables.

> **In Simple Terms:** ANCOVA is a regression where we use both numbers (like years of experience) and categories (like gender) to predict our outcome.

### Key Concepts

#### Combining Variables
In a model like `Y_i = α + βD_i + γX_i + u_i` (where X is a quantitative variable like experience), the qualitative variable provides different intercepts for different groups, while the quantitative variable provides the slope. This assumes the rate of change (slope γ) is the same for both groups, but their starting levels (intercepts) differ.

### Definitions
- **ANCOVA Models**: Regression models that contain both qualitative and quantitative explanatory variables. ⭐ (exam-important)

### Examples
**Example: Teacher Salary (Gender and Experience)**
`Y_i = α + βD_i + γX_i + u_i`
Female mean salary: `E(Y_i|D=0) = α + γX_i`
Male mean salary: `E(Y_i|D=1) = (α + β) + γX_i`
Both have the same slope `γ` for experience, but different intercepts (`α` vs `α + β`).

> **Quick Recall:**
> - ANCOVA = Mix of qualitative and quantitative variables.
> - Represents parallel regression lines with the same slope but different intercepts.

### Connections
- Builds on ANOVA Models (Chunk 001) by adding continuous variables.
<!-- Continues in chunk 002 -->
