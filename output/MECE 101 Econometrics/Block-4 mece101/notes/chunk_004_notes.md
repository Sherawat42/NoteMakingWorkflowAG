# Chunk 004 — Probit Models and Model Evaluation
<!-- Pages: 31-40 -->
<!-- Source: chunk_004.txt -->
<!-- Continues from: 15.3.2 Estimation of Logit Model (Chunk 003) -->

## Section: 15.3.2 Interpretation of Logit Model 🟡

### Core Idea
The logit model can be interpreted in three ways: interpreting the logit (log-odds), the odds ratio, or the marginal effect (change in probability).

> **In Simple Terms:** We can't just say "X increases Y by 5%" like in standard math. Instead, we have to look at how X changes the *log-odds*, the *odds ratio*, or we calculate the *marginal effect* at a specific point on the curve.

### Key Concepts

#### Logit Interpretation
The slope coefficient `α₁` tells us how the *log-odds* change for a one-unit change in `X`. The sign (positive or negative) indicates the direction of the relationship, but the number itself is not intuitive to interpret directly as a probability.

#### Odds-Ratio Interpretation
By taking the antilog of the logit coefficient (`e^{α₁}`), we get the odds ratio. For example, if `e^{α₁} = 1.6`, a one-unit increase in `X` multiplies the odds of the event occurring by 1.6.

#### Marginal Effect Interpretation
The marginal effect measures the change in probability for a one-unit change in `X`. Because the logit curve is non-linear (S-shaped), this effect changes depending on where you are on the curve. It is usually calculated at the mean values of the explanatory variables.
Marginal Effect formula for logit: `dP / dX = p_i * (1 - p_i) * β_j`

### Definitions
- **Marginal Effect**: The change in the probability of the dependent variable for a one-unit change in an independent variable, calculated at a specific base point (usually the mean). ⭐ (exam-important)

### Connections
- Concludes the Logit Model discussion started in Chunk 003.

---

## Section: 15.4 Probit Model 🔴

### Core Idea
The Probit model is the primary alternative to the Logit model. It achieves the same goal—keeping probabilities bounded between 0 and 1—but uses the Cumulative Distribution Function (CDF) of the standard normal distribution instead of the logistic distribution.

> **In Simple Terms:** Probit is just a different flavor of Logit. They both draw an S-curve to keep probabilities between 0% and 100%, but Probit uses the famous "bell curve" math instead of the logistic math.

### Key Concepts

#### Normal CDF
The model assumes the unobservable underlying variable is normally distributed. The probabilities are derived from calculating the area under the standard normal curve up to a certain point (the Z-score).

### Definitions
- **Probit Model**: A nonlinear regression model for binary outcomes that assumes the error term follows a standard normal distribution. ⭐ (exam-important)

### Connections
- Alternative to Logit Model (Chunk 003) and superior to LPM (Chunk 003).

---

## Section: 15.4.1 Specification of Probit Model 🟡

### Core Idea
The probit model is theoretically grounded in the concept of an unobservable "utility index" or "latent variable."

> **In Simple Terms:** We imagine there is an invisible "desire meter" inside a person. If their desire meter crosses a certain threshold, they take the action (e.g., buy a house). We model the desire meter, even though we only see the final yes/no action.

### Key Concepts

#### Unobservable Utility Index (Latent Variable)
Let `I_i` be an unobservable utility index determined by explanatory variables: `I_i = β₁ + β₂X_i`. There is a critical threshold `I_i^*`. If `I_i > I_i^*`, the event occurs (Y=1). Assuming `I_i^*` is normally distributed, the probability of Y=1 is the probability that the normal variable `I_i^*` is less than or equal to `I_i`, which is precisely the CDF of the normal distribution.

### Definitions
- **Latent Variable**: An unobservable underlying variable (like an index or utility) that crosses a threshold to produce the observed binary outcome. ⭐ (exam-important)

---

## Section: 15.4.2 Estimation of Probit Model 🟡

### Core Idea
Like the Logit model, the Probit model requires different estimation techniques depending on whether the data is individual (ungrouped) or grouped.

> **In Simple Terms:** Just like Logit, we use Maximum Likelihood for individual data, and we can group people to use OLS if we have many people with identical characteristics.

### Key Concepts

#### Grouped vs Ungrouped
- **Ungrouped Data**: Handled exclusively using Maximum Likelihood Estimation (MLE).
- **Grouped Data**: The relative frequencies `p_i` are calculated for groups. We then find the inverse of the normal CDF (`Z_i`) corresponding to those probabilities. The resulting equation `Z_i = β₁ + β₂X_i + u_i` can be estimated using OLS. This is known as the *gprobit* model.

### Definitions
- **Gprobit**: The grouped probit model, estimated using OLS on grouped frequency data transformed via the inverse normal CDF. ⭐ (exam-important)

---

## Section: 15.4.3 Interpretation of Probit Model 🟡

### Core Idea
The raw coefficients of a probit model give the change in the Z-score for a unit change in the explanatory variable. To get meaningful probabilities, one must calculate the marginal effects.

> **In Simple Terms:** A coefficient of 0.5 means the Z-score goes up by 0.5. To know what that means for the actual percentage chance, we have to look up the Z-score on a normal curve table.

### Key Concepts

#### Marginal Effects in Probit
Similar to the logit model, the marginal effect in a probit model depends on the specific values of the explanatory variables. It is calculated by multiplying the coefficient by the value of the standard normal probability density function evaluated at that specific point.

### Definitions
- **Interpretation**: Interpreting probit models relies on reading standard normal CDF tables to convert Z-scores back into probabilities or calculating marginal effects. ⭐ (exam-important)

---

## Section: 15.5 Joint Significance in Qualitative Response Regression Models 🔴

### Core Idea
Instead of the standard F-test used in OLS to test if all slope coefficients are simultaneously zero, qualitative response models estimated via MLE use the Likelihood Ratio (LR) test.

> **In Simple Terms:** In regular math, we use the F-test to see if our model is better than nothing. In Logit/Probit math, we use the LR test to do the exact same thing.

### Key Concepts

#### Likelihood Ratio (LR) Test
The LR test compares the likelihood of the restricted model (where all slope coefficients are zero) to the unrestricted model (the full model). The test statistic follows a Chi-square (χ²) distribution with degrees of freedom equal to the number of explanatory variables.
`LR Statistic = -2 * (L_Restricted - L_Unrestricted)`

### Definitions
- **LR Test (Likelihood Ratio Test)**: A statistical test used in maximum likelihood estimation to determine the joint significance of all explanatory variables, analogous to the F-test in OLS. ⭐ (exam-important)

### Connections
- Analogous to the F-test used in the Chow Test (Chunk 001) but specifically for MLE models.

---

## Section: 15.6 Goodness-of-Fit in Logit and Probit Models 🔴

### Core Idea
Since the traditional R-squared is inappropriate for models with binary dependent variables, alternative measures known as pseudo R-squareds are used to evaluate model fit.

> **In Simple Terms:** Because R-squared doesn't work for yes/no predictions, statisticians invented "pseudo" R-squareds. One popular one is McFadden's, which compares the likelihood of the full model against a model with only an intercept.

### Key Concepts

#### Pseudo R-squared
The most common measure is the **McFadden R-squared**. It is calculated as:
`Pseudo R² = 1 - (L_UR / L_R)`
Where `L_UR` is the log-likelihood of the unrestricted (full) model, and `L_R` is the log-likelihood of the restricted (intercept-only) model. The value lies between 0 and 1, where higher values indicate better fit, but it is generally much lower than OLS R-squared values.

### Definitions
- **Goodness-of-Fit (Pseudo R²)**: Statistical measures used to evaluate how well a qualitative response model fits the data, since traditional R² is invalid. ⭐ (exam-important)

### Connections
- Solves the "R-squared is not appropriate" limitation of the LPM identified in Chunk 003.
<!-- Continues in chunk 005 -->
