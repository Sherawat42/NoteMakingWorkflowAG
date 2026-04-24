# Running Context

## Key Concepts Introduced
- **Structural Change** (Chunk 001): Change in parameters of a relationship within a sample.
- **Dummy Variable Trap** (Chunk 001): Perfect multicollinearity when too many dummy variables are introduced.
- **Base Category** (Chunk 001): The category assigned value 0 against which comparisons are made.
- **Multiple Qualitative Variables** (Chunk 002): Using multiple sets of dummy variables in one model.
- **Coincident/Parallel/Concurrent/Dissimilar Regressions** (Chunk 002): Types of structural changes differing by intercept, slope, or both.
- **Deseasonalisation** (Chunk 002): Removing seasonal components from a time series using seasonal dummies.
- **Pooling Data** (Chunk 002): Combining cross-sectional and time-series data using dummy variables for units.
- **Qualitative Dependent Variables** (Chunk 003): Variables representing categories rather than continuous numbers.
- **Odds-Ratio** (Chunk 003): The ratio of the probability an event occurs to the probability it does not.
- **Grouped vs Ungrouped Data** (Chunk 003): Grouped data uses frequencies; ungrouped individual data uses 0s and 1s.
- **Latent Variable** (Chunk 004): An unobservable utility index that determines the binary outcome when crossing a threshold.
- **Marginal Effect** (Chunk 004): The change in probability for a unit change in an independent variable.
- **Likelihood Ratio Test** (Chunk 004): Test comparing likelihood of restricted vs unrestricted models.
- **Pseudo R-squared** (Chunk 004): Alternative to R-squared for qualitative response models, e.g., McFadden's R-squared.
- **Simultaneous Relationships** (Chunk 005): Variables mutually influence each other, violating OLS assumptions.
- **Endogenous Variables** (Chunk 005): Variables whose values are determined within the system.
- **Predetermined Variables** (Chunk 005): Current exogenous, lagged exogenous, and lagged endogenous variables.
- **Covariance between X and u** (Chunk 006): In SEMs, endogenous variables are correlated with the error term.
- **Structural vs Reduced Form** (Chunk 006): Structural represents theory; reduced form solves endogenous in terms of exogenous.
- **Identification Problem** (Chunk 006): Whether we can deduce structural parameters from reduced form parameters.
- **Exclusion Restrictions** (Chunk 006): Assuming certain exogenous variables do not appear in specific equations.
- **Necessary and Sufficient Conditions** (Chunk 007): Order condition is necessary; rank condition is both necessary and sufficient.
- **Counting Rule** (Chunk 007): Comparing excluded variables to total equations minus one.
- **Rank of a Matrix / Determinants** (Chunk 007): Used in rank condition to evaluate non-zero determinants of excluded variable parameters.

## Definitions (⭐ exam-important)
- **Dummy Variables** (Chunk 001): Artificial variables constructed to take the value 1 or 0 indicating presence or absence of an attribute. ⭐
- **Structural Break** (Chunk 001): Occurs if parameters underlying a relationship differ from one subset of data to another. ⭐
- **Differential Intercept Coefficient** (Chunk 001): The coefficient attached to the dummy variable representing the difference from the base category. ⭐
- **ANOVA Models** (Chunk 001): Regression models containing only dummy explanatory variables. ⭐
- **ANCOVA Models** (Chunk 001): Regression models containing both qualitative and quantitative explanatory variables. ⭐
- **Multiple Dummy Variables** (Chunk 002): More than one set of dummy variables representing multiple qualitative attributes. ⭐
- **Differential Slope Coefficient** (Chunk 002): Coefficient of an interaction term indicating slope difference from the base category. ⭐
- **Seasonal Adjustment (Deseasonalisation)** (Chunk 002): The process of removing the seasonal factor from a time series. ⭐
- **Pooled Data** (Chunk 002): Data that combines both cross-sectional and time-series dimensions. ⭐
- **Limited Dependent Variable Models** (Chunk 003): Models where the dependent variable is constrained, e.g., binary. ⭐
- **Linear Probability Model (LPM)** (Chunk 003): Regression model where a binary dependent variable is estimated using OLS. ⭐
- **Heteroscedasticity in LPM** (Chunk 003): Error variance changes because Bernoulli variance is a function of its mean. ⭐
- **Logit Model** (Chunk 003): Nonlinear regression model using cumulative logistic distribution to model log-odds. ⭐
- **Maximum Likelihood Method** (Chunk 003): Nonlinear estimation procedure used for logit/probit with individual micro-data. ⭐
- **Probit Model** (Chunk 004): Nonlinear regression model for binary outcomes using standard normal CDF. ⭐
- **Gprobit** (Chunk 004): The grouped probit model, estimated using OLS on transformed frequency data. ⭐
- **LR Test** (Chunk 004): Statistical test for joint significance of explanatory variables in MLE models. ⭐
- **Goodness-of-Fit (Pseudo R²)** (Chunk 004): Statistical measures used instead of R² for qualitative response models. ⭐
- **Simultaneous Equations Model (SEM)** (Chunk 005): Models where variables mutually determine one another. ⭐
- **Endogenous Variables** (Chunk 005): Variables which get determined jointly and interdependently within the model. ⭐
- **Exogenous Variables** (Chunk 005): Variables which get determined outside the model. ⭐
- **Predetermined Variables** (Chunk 005): The combined set of current exogenous, lagged exogenous, and lagged endogenous variables. ⭐
- **Simultaneity Bias** (Chunk 006): Bias from applying OLS to an equation in an SEM due to correlation between X and u. ⭐
- **Endogeneity** (Chunk 006): A situation where an explanatory variable is correlated with the error term. ⭐
- **Biased/Inconsistent Estimators** (Chunk 006): Estimators that do not equal or converge to the true population parameter. ⭐
- **Structural Equation / Parameters** (Chunk 006): Equations/parameters representing the structure of an economic model. ⭐
- **Reduced Form Models / Parameters** (Chunk 006): Models expressing endogenous variables solely via predetermined variables. Parameters are Impact Multipliers. ⭐
- **Identification** (Chunk 006): The possibility of deducing structural parameters from reduced form parameters. ⭐
- **Paradox of Identification** (Chunk 006): Identification is achieved via variables absent from an equation. ⭐
- **Under/Exactly/Over-identified Equation** (Chunk 006): Equations with insufficient, exactly sufficient, or more than sufficient information to deduce structural parameters. ⭐
- **Identification Conditions** (Chunk 007): Formal mathematical rules (order and rank conditions) to determine if structural parameters can be estimated. ⭐
- **Order Condition** (Chunk 007): Necessary counting rule: (K-M) >= (G-1). ⭐
- **Rank Condition** (Chunk 007): Necessary and sufficient condition requiring a non-zero determinant of order G-1 from excluded variable parameters. ⭐

## Named Models / Laws / Theories
- **Chow Test** (Chunk 001): Tests for structural stability between subsets of data using restricted and unrestricted models.

## Key Data & Numbers
