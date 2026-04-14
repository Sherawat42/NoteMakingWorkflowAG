# Chunk 009 — SEM Methodology & Specification
<!-- Pages: 80-89 -->
<!-- Source: chunk_009.txt -->

## Section: Differences & Similarities with Traditional Methods 🟡

### Key Concepts
#### Traditional vs SEM
- **Similarities**: Both SEM and traditional methods (like ANOVA, multiple regression) are based on linear statistical models and rely on similar fundamental assumptions (like normality). Neither can definitively "prove" causality without an experimental design underlying the data.
- **Differences**: Traditional methods typically analyze only measured variables sequentially and assume variables are measured without error. SEM analyzes both measured and latent (unmeasured) variables simultaneously, explicitly models measurement error, and allows for simultaneous evaluation of multiple interconnected dependence relationships.

## Section: Concepts and Terminology used in SEM 🔴

### Definitions
- **Path Diagram**: A graphical representation of the theoretical model showing variables and the hypothesized causal (directed arrows) and correlational (curved, double-headed arrows) relationships among them. ⭐ (exam-important)
- **Latent Variable**: Unobserved theoretical constructs (factors) that are inferred from a set of observed measured variables. ⭐ (exam-important)
- **Manifest (Observed) Variable**: The actual measurable data points (like survey answers) used as indicators for latent variables.

## Section: SEM Models Specification 🔴

### Key Concepts
#### Reflective Indicators
Indicators are considered "reflective" when the underlying latent construct is theorized to cause the observable variables. Thus, a change in the latent variable causes a change in all its indicators simultaneously. Internal consistency reliability (like Cronbach's alpha) is highly relevant here because the indicators should be highly correlated.

#### Formative Indicators
Indicators are "formative" when they conceptually define or "cause" the latent construct itself. Changes in the indicators combine to form the construct. In this case, indicators do not necessarily correlate highly with one another, and dropping one indicator completely changes the meaning of the latent construct.

## Section: Issues in SEM Technique 🟡

### Edge Cases & Caveats
- **Sample Size**: Small samples can cause convergence failures where the algorithm cannot find a solution. Larger samples are required as model complexity increases.
- **Missing Data**: Listwise deletion reduces sample size drastically. Imputation strategies (like FIML - Full Information Maximum Likelihood) are usually preferred.
- **Outliers and Normality**: Severe outliers can skew covariances drastically affecting MLE. Non-normality inflates chi-square values, making the model look worse than it is.

## Section: Steps in SEM (Initial Spec & Estimation) 🔴

### Mechanisms / Processes
1. **Initial Model Specification**: The researcher mathematically and graphically defines the hypothesized relationships based strictly on theory.
2. **Model Estimation**: The software uses algorithms (usually Maximum Likelihood) to calculate parameter estimates (path coefficients, variances) that minimize the difference between the sample covariance matrix and the covariance matrix implied by the specified theoretical model.
