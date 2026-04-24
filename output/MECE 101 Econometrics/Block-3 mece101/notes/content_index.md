# Content Index
**Source**: Block-3 mece101 | **Chunks**: 11 | **Completed**: 2024-04-24

## Notes Files
| Chunk | Title | Pages | Top Sections |
|-------|-------|-------|--------------|
| 001 | Model Specification Errors | 1-13 | Specification Errors, Omitted Variables, Irrelevant Variables, RESET Test |
| 002 | Model Selection & Autocorrelation | 14-23 | Model Selection Criteria, Concept of Autocorrelation |
| 003 | Autocorrelation Detection & Remedies | 24-32 | Consequences of Autocorrelation, Detection (DW/BG), Remedies (GLS, Newey-West) |
| 004 | Estimating Rho & Multicollinearity | 33-42 | Estimating Rho, Concept of Multicollinearity, Consequences |
| 005 | Multicollinearity Remedies | 43-51 | Detection, Remedial Measures for Multicollinearity (Ridge, PCA) |
| 006 | Heteroscedasticity Concept & Detection | 52-61 | Concept, Consequences, Detection (Park, Glejser, GQ, BP) |
| 007 | Heteroscedasticity Remedies & Errors in Variables | 62-71 | White's Test, Remedial Measures (WLS, GLS), Errors in Variables |
| 008 | Consequences & Remedies for Errors in Variables | 72-81 | Consequences of Measurement Error, Instrumental Variables, Hausman Test |
| 009 | Inverse Regression & Stochastic Regressors | 82-89 | Inverse Regression, Stochastic Regressors, Endogeneity |
| 010 | Instrumental Variables & 2SLS | 90-97 | IV Estimator, Two-Stage Least Squares (2SLS) |
| 011 | 2SLS Summary | 98-100 | 2SLS Summary |

## Key Terms Glossary
| Term | Definition | First Appears |
|------|-----------|---------------|
| **Specification Error** | Errors arising from incorrect model formulation, including omitted/irrelevant variables, wrong functional forms, incorrect error term assumptions, or measurement errors. | Chunk 001 |
| **RESET** | Ramsey's Regression Specification Error Test used to detect incorrect functional forms. | Chunk 001 |
| **Autocorrelation** | The correlation between successive error terms in a dataset, most commonly in time series data. $E(u_i, u_j) \neq 0$. | Chunk 002 |
| **White noise** | A purely random error term ($\varepsilon_t$) that has a zero mean, constant variance, and no covariance with other periods. | Chunk 002 |
| **Durbin-Watson Test** | A statistical test used to detect the presence of first-order autocorrelation in the residuals of a regression. | Chunk 003 |
| **Breusch-Godfrey Test** | A generalized test for autocorrelation that can detect higher-order autoregressive and moving average processes. | Chunk 003 |
| **Newey-West Method** | A technique that corrects OLS standard errors for both heteroscedasticity and autocorrelation in large samples. | Chunk 003 |
| **Multicollinearity** | The presence of high correlation between explanatory variables in a multiple regression model. | Chunk 004 |
| **Perfect Multicollinearity** | A situation where two or more explanatory variables bear an exact linear relationship, making it impossible to uniquely estimate their coefficients. | Chunk 004 |
| **Omission bias** | The bias introduced into estimators when a theoretically relevant variable is deliberately dropped from the model. | Chunk 005 |
| **Ridge Regression** | An estimation technique that resolves severe multicollinearity by adding a small constant penalty ($\lambda$) to the variance. | Chunk 005 |
| **Principal Component Analysis (PCA)** | A multivariate technique that transforms a set of correlated explanatory variables into a set of completely uncorrelated linear combinations (components). | Chunk 005 |
| **Heteroscedasticity** | The condition where the variance of the error term is not constant, but changes with the values of the independent or dependent variable. | Chunk 006 |
| **Weighted Least Squares (WLS)** | An estimation method where observations are weighted inversely by their variances to correct for heteroscedasticity. | Chunk 006 |
| **Park Test** | A test for heteroscedasticity that regresses the natural log of squared residuals on the natural log of an explanatory variable. | Chunk 006 |
| **Goldfeld-Quandt Test** | A test that orders observations by an explanatory variable, drops central data points, and compares the residual variances. | Chunk 006 |
| **White's Estimator** | A large-sample procedure that calculates robust standard errors to correct for heteroscedasticity when its exact pattern is unknown. | Chunk 007 |
| **Errors in Variables** | A violation of the classical assumption that regressors are measured perfectly, occurring when the observed variables contain random measurement errors. | Chunk 007 |
| **Instrumental Variable (IV)** | A proxy variable $Z$ used in regression analysis that is highly correlated with the explanatory variable but uncorrelated with the error term. | Chunk 008 |
| **Hausman Specification Test** | A statistical test used to detect measurement errors (or endogeneity) by comparing the consistency of OLS estimators against IV estimators. | Chunk 008 |
| **Stochastic Regressor** | An explanatory variable that is a random variable, rather than having fixed, predetermined values in repeated samples. | Chunk 009 |
| **Endogenous Variable** | An explanatory variable in a regression model that is correlated with the stochastic error term. | Chunk 009 |
| **Exogenous Variable** | An explanatory variable that is NOT correlated with the stochastic error term. | Chunk 009 |
| **Simultaneity** | A situation where the explanatory variable is partly determined by the dependent variable, leading to a correlation with the error term. | Chunk 009 |
| **Two-Stage Least Squares (2SLS)** | An estimation technique used when there are multiple instruments available for an endogenous variable. | Chunk 010 |
