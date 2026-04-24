# Running Context

## Key Concepts Introduced
- **Model Specification Error** (Chunk 001): Errors arising from omitted variables, irrelevant variables, wrong functional forms, or measurement errors.
- **Omitted Variable Bias** (Chunk 001): Omitting a relevant variable causes biased and inconsistent estimators and invalidates hypothesis testing.
- **Irrelevant Variable Inclusion** (Chunk 001): Including a redundant variable keeps estimators unbiased but makes them inefficient (higher variance).

## Definitions (⭐ exam-important)
- **Specification Error** (Chunk 001): Errors arising from incorrect model formulation, including omitted/irrelevant variables, wrong functional forms, incorrect error term assumptions, or measurement errors. ⭐
- **RESET (Regression Specification Error Test)** (Chunk 001): A general test for model misspecification that checks if non-linear functional forms of the estimated dependent variable improve the model's fit. ⭐

## Named Models / Laws / Theories
- **RESET Test** (Chunk 001): Ramsey's Regression Specification Error Test used to detect incorrect functional forms.

## Key Data & Numbers
- **Bias Formula** (Chunk 001): Bias = (coefficient of excluded variable) × (regression coefficient of excluded on included variable).
- **Autocorrelation** (Chunk 002): Correlation between successive error terms over time, violating OLS independence assumptions.
- **Autoregressive AR(1) Process** (Chunk 002): Current error is a proportion of past error plus a random shock.

## Definitions (⭐ exam-important)
- **Autocorrelation** (Chunk 002): The correlation between successive error terms in a dataset, most commonly in time series data. $E(u_i, u_j) \neq 0$. ⭐
- **White noise** (Chunk 002): A purely random error term ($\varepsilon_t$) that has a zero mean, constant variance, and no covariance with other periods. ⭐
- **GLS (Generalized Least Squares)** (Chunk 003): Transforms variables to eliminate autocorrelation, making estimators BLUE.
- **Durbin-Watson Test** (Chunk 003): Tests for AR(1) autocorrelation using $d \approx 2(1 - \rho)$.
- **Breusch-Godfrey Test** (Chunk 003): Generalized LM test for higher-order AR(p) and MA processes.
- **Quasi-first Differencing** (Chunk 003): Subtracting $\rho$ times the previous period's value to remove autocorrelation.
- **Newey-West Method** (Chunk 003): Provides HAC standard errors for large samples.

## Definitions (⭐ exam-important)
- **Durbin-Watson Test** (Chunk 003): A statistical test used to detect the presence of first-order autocorrelation in the residuals of a regression. ⭐
- **Breusch-Godfrey (BG) Test** (Chunk 003): A generalized test for autocorrelation that can detect higher-order autoregressive and moving average processes. ⭐
- **Newey-West Method** (Chunk 003): A technique that corrects OLS standard errors for both heteroscedasticity and autocorrelation in large samples. ⭐
- **Multicollinearity** (Chunk 004): High correlation among explanatory variables, leading to inflated standard errors.
- **VIF & Condition Number** (Chunk 004): Key metrics used to detect the severity of multicollinearity.

## Definitions (⭐ exam-important)
- **Multicollinearity** (Chunk 004): The presence of high correlation between explanatory variables in a multiple regression model. ⭐
- **Perfect Multicollinearity** (Chunk 004): A situation where two or more explanatory variables bear an exact linear relationship, making it impossible to uniquely estimate their coefficients. ⭐
- **Ridge Regression** (Chunk 005): A biased estimation technique that adds a constant $\lambda$ to the variance to resolve multicollinearity, lowering MSE.
- **Principal Component Analysis (PCA)** (Chunk 005): Transforms correlated variables into uncorrelated indices, but often destroys economic interpretability.

## Definitions (⭐ exam-important)
- **Omission bias** (Chunk 005): The bias introduced into estimators when a theoretically relevant variable is deliberately dropped from the model. ⭐
- **Ridge Regression** (Chunk 005): An estimation technique that resolves severe multicollinearity by adding a small constant penalty ($\lambda$) to the variance, resulting in biased but more stable (lower MSE) estimators. ⭐
- **Principal Component Analysis (PCA)** (Chunk 005): A multivariate technique that transforms a set of correlated explanatory variables into a set of completely uncorrelated linear combinations (components). ⭐
- **Heteroscedasticity** (Chunk 006): Non-constant variance of error terms. Most common in cross-sectional data.
- **Weighted Least Squares (WLS)** (Chunk 006): Estimation method that restores efficiency by weighting observations inversely by their variance.
- **Park, Glejser, Goldfeld-Quandt, Breusch-Pagan, White's Tests** (Chunk 006): The 5 main tests for detecting heteroscedasticity.

## Definitions (⭐ exam-important)
- **Heteroscedasticity** (Chunk 006): The condition where the variance of the error term is not constant, but changes with the values of the independent or dependent variable. ⭐
- **Weighted Least Squares (WLS)** (Chunk 006): An estimation method where observations are weighted inversely by their variances to correct for heteroscedasticity, restoring efficiency (BLUE). ⭐
- **Park Test** (Chunk 006): A test for heteroscedasticity that regresses the natural log of squared residuals on the natural log of an explanatory variable. ⭐
- **Goldfeld-Quandt Test** (Chunk 006): A test that orders observations by an explanatory variable, drops central data points, and compares the residual variances of the resulting high and low groups. ⭐
- **White's Estimator** (Chunk 007): Corrects standard errors for heteroscedasticity without requiring knowledge of the variance pattern.
- **Errors in Variables** (Chunk 007): Violates the assumption that regressors are measured without error.

## Definitions (⭐ exam-important)
- **White's Estimator** (Chunk 007): A large-sample procedure that calculates robust standard errors to correct for heteroscedasticity when its exact pattern is unknown. ⭐
- **Errors in Variables** (Chunk 007): A violation of the classical assumption that regressors are measured perfectly, occurring when the observed variables contain random measurement errors (often due to using proxy variables). ⭐
- **Consequences of Error in X** (Chunk 008): OLS estimators become biased and inconsistent (underestimating true $\beta$).
- **Instrumental Variable (IV)** (Chunk 008): A proxy variable used to replace an error-prone $X$ to obtain consistent estimators.
- **Hausman Specification Test** (Chunk 008): Test for measurement error comparing OLS consistency against IV.

## Definitions (⭐ exam-important)
- **Instrumental Variable (IV)** (Chunk 008): A proxy variable $Z$ used in regression analysis that is highly correlated with the explanatory variable but uncorrelated with the error term, used to obtain consistent estimators when variables are measured with error. ⭐
- **Hausman Specification Test** (Chunk 008): A statistical test used to detect measurement errors (or endogeneity) by comparing the consistency of OLS estimators against Instrumental Variables estimators. ⭐
- **Stochastic Regressor** (Chunk 009): A regressor that is a random variable, introducing the risk of correlation with the error term.
- **Endogeneity** (Chunk 009): Correlation between an explanatory variable and the error term. Caused by omitted variables, measurement error, or simultaneity.

## Definitions (⭐ exam-important)
- **Stochastic Regressor** (Chunk 009): An explanatory variable that is a random variable, rather than having fixed, predetermined values in repeated samples. ⭐
- **Endogenous Variable** (Chunk 009): An explanatory variable in a regression model that is correlated with the stochastic error term. ⭐
- **Exogenous Variable** (Chunk 009): An explanatory variable that is NOT correlated with the stochastic error term. ⭐
- **Simultaneity (Reverse Causality)** (Chunk 009): A situation where the explanatory variable is partly determined by the dependent variable, leading to a correlation with the error term (endogeneity). ⭐
- **Two-Stage Least Squares (2SLS)** (Chunk 010): Method to resolve endogeneity when multiple instruments are available, involving a first-stage purification regression and a second-stage estimation regression.

## Definitions (⭐ exam-important)
- **Two-Stage Least Squares (2SLS)** (Chunk 010): An estimation technique used when there are multiple instruments available for an endogenous variable, involving a first-stage regression to create an optimal fitted instrument, and a second-stage regression to estimate the main model. ⭐
