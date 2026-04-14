# Chunk 003 — Oblique Rotation & Factor Scores
<!-- Pages: 21-29 -->
<!-- Source: chunk_003.txt -->

## Section: Oblique Rotation 🟡

### Core Idea
Unlike orthogonal rotation, which forces factors to remain completely independent (uncorrelated at 90-degree angles), oblique rotation allows the factors themselves to be correlated. This is often more realistic in social sciences where underlying latent constructs naturally influence one another.

> **In Simple Terms:** Instead of forcing factors to be completely independent, oblique rotation lets the factors "talk" to each other and be correlated, which often matches the messy reality of human behaviour.

### Key Concepts

#### Oblique vs Orthogonal
Orthogonal rotation (e.g., Varimax) maintains $Cov(F_i, F_j) = 0$. Oblique rotation (e.g., Promax, Direct Oblimin) relaxes this, resulting in a factor correlation matrix that is no longer an identity matrix. While it can produce a simpler structure, interpreting the results becomes more complex.

## Section: Factor Scores 🔴

### Core Idea
Factor scores are the estimated values of the underlying, unobservable common factors for each specific individual or observation in the dataset. While factor loadings tell us how variables relate to factors, factor scores tell us where an individual "stands" on that factor.

### Definitions
- **Factor Scores**: Estimates of the unobserved common factor values for individual observations, derived from the observed data and estimated factor loadings. ⭐ (exam-important)

## Section: Methods for Estimating Factor Scores 🔴

### Core Idea
Since the common factors $F$ are unobservable, their exact values cannot be calculated directly. We must estimate them from the data $X$, the loadings $\hat{L}$, and the specific variances $\hat{\Psi}$. The primary methods for estimating these scores are Ordinary Least Squares (OLS), Weighted Least Squares (WLS), and the Regression Method.

### Key Concepts

#### Ordinary Least Squares Method
This method estimates factor scores by minimizing the sum of squared specific factors (errors). It treats the factor model $X = \mu + LF + \epsilon$ like a standard regression where $L$ is known and $F$ is to be estimated.
Formula: $\hat{F} = (L'L)^{-1} L' (X - \mu)$.
This method treats all errors symmetrically.

#### Weighted Least Squares Method
WLS improves upon OLS by recognizing that specific factors $\epsilon$ do not have equal variances; their variances are given by the diagonal elements of $\Psi$. It weighs the squared errors inversely by their specific variances $\Psi^{-1}$. variables with smaller specific variances (more reliable variables) are weighted more heavily.
Formula: $\hat{F} = (L'\Psi^{-1}L)^{-1} L' \Psi^{-1} (X - \mu)$.

#### Regression Method
This method uses the joint multivariate normal distribution of $X$ and $F$ to find the conditional expectation of $F$ given $X$. It essentially runs a multiple regression to predict the factor scores from the observed variables using the population covariance relationships.
Formula for population: $\hat{F} = L'\Sigma^{-1}(X - \mu)$.

### Mechanisms / Processes
1. **OLS Prediction**: Standard unweighted error minimization. Used when specific variances are largely assumed equal or ignored.
2. **WLS Prediction**: Minimizes $\epsilon' \Psi^{-1} \epsilon$. The most common method advocated for maximum likelihood extraction because it directly incorporates $\Psi$. 
3. **Regression Prediction**: Focuses on maximum validity relative to the true factor scores, but generated scores may be slightly correlated even for orthogonal factors because it relies on the sample covariance matrix inverse ($S^{-1}$).

### Quick Recall
> **Quick Recall:**
> - OLS: treats all errors equally; $\hat{F} = (L'L)^{-1} L' X_{centered}$.
> - WLS: weighs highly reliable variables more using $\Psi^{-1}$.
> - Regression Method: uses conditional expectation $\hat{F} = L'\Sigma^{-1}X_{centered}$.
