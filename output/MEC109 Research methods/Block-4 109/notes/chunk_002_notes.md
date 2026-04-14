# Chunk 002 — Communalities & Methods of Estimation
<!-- Pages: 11-20 -->
<!-- Source: chunk_002.txt -->

## Section: Communalities 🟡

### Core Idea
Communality represents the proportion of variance of an observed variable that is accounted for or shared by the common factors in the factor model. It is mathematically the sum of the squared factor loadings for that specific variable.

> **In Simple Terms:** Communality measures how much of a single variable's behavior can be chalked up to exactly the same underlying factors driving everything else, rather than its own unique quirks.

### Key Concepts

#### Shared Variance
The variance of variable $X_i$ is partitioned into two parts: $\sigma_i^2 = \sum l_{ij}^2 + \psi_i$. The first term ($\sum l_{ij}^2$) is the communality (often denoted $\hat{h}_i^2$), and the second part ($\psi_i$) is the specific variance unique to that variable.

### Quick Recall
> **Quick Recall:**
> - $Communality (h_i^2) = l_{i1}^2 + l_{i2}^2 + \dots + l_{im}^2$
> - Total Variance = Communality + Specific Variance

## Section: Methods of Estimation 🔴

### Core Idea
To use the factor model, the parameters (factor loadings $L$ and specific variances $\Psi$) must be estimated from the sample covariance matrix $S$. Two primary approaches are the Principal Component Method, which is descriptive and derived from eigenvalue decomposition, and the Maximum Likelihood Method, which requires the assumption of multivariate normality.

> **In Simple Terms:** We have data, and we need to find the numbers that represent our hidden factors and errors. We can either purely hack at the variance mathematically (Principal Component Method), or use probability laws (Maximum Likelihood Method) to find the most likely fit.

### Key Concepts

#### Principal Component Method
This method ignores specific factors initially, approximating the covariance matrix $\Sigma$ (or correlation matrix $R$) directly as $LL'$. It uses spectral decomposition (eigenvalues $\lambda$ and eigenvectors $e$) where estimated loadings are $\hat{l}_{ij} = \sqrt{\hat{\lambda}_j} \hat{e}_{ij}$. It extracts factors sequentially: the first factor accounts for the maximum variance, the second for the maximum remaining variance, etc.

#### Maximum Likelihood Method
Assuming the data $X$ follows a multivariate normal distribution, we construct a likelihood function. This method relies on maximizing the likelihood of observing the given sample covariance $S$ given the population covariance $\Sigma = LL' + \Psi$. 

### Definitions
- **Principal Component Method**: A descriptive factor estimation method that approximates the covariance matrix using spectral (eigenvalue) decomposition without initially relying on specific variances. ⭐ (exam-important)
- **Maximum Likelihood Method**: An estimation technique maximizing the likelihood function based on a multivariate normal distribution assumption to estimate $L$ and $\Psi$. ⭐ (exam-important)

### Mechanisms / Processes
**Principal Component Extraction Strategy:**
1. Compute the sample covariance matrix $S$.
2. Find eigenvalues $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_p$ and their eigenvectors $e_1, e_2, \dots, e_p$.
3. Compute unrotated factor loadings: $\hat{l}_{ij} = \sqrt{\hat{\lambda}_j} \hat{e}_{ij}$.
4. Compute communalities and specific variances $\Psi = S - \hat{L}\hat{L}'$.

### Edge Cases & Caveats
- The Principal Component Method is technically factoring the total variance rather than just the common variance.
- ML estimation requires large sample sizes and the assumption of multivariate normality, which may not always hold true.

### Quick Recall
> **Quick Recall:**
> - PCA method uses $\hat{L} = \sqrt{\Lambda} E$.
> - ML method relies on maximizing normal likelihoods.

## Section: Factor Rotation 🔴

### Core Idea
Because the factor model contains an inherent mathematical ambiguity (any orthogonal matrix $T$ applied to $L$ gives an equally valid model where $L^* = LT$), the initial extracted factors are often difficult to interpret. Factor rotation applies orthogonal transformations to "rotate" the coordinate axes, maximizing high loadings and minimizing low loadings without altering communalities or the reproduced covariance matrix, yielding a simpler, interpretable structure.

> **In Simple Terms:** Imagine a 3D scatter plot where the axes are skewed. "Rotating" the shape doesn't change the shape itself, but it lets us look at it from a pure top, side, or front angle so we can clearly interpret what's going on.

### Key Concepts

#### Purpose of Rotation
The goal is "simple structure"—where each variable loads heavily on only one factor, and each factor is defined by a small core group of variables, making the theoretical meaning of the factors clearer.

### Mechanisms / Processes
1. Extract initial unrotated matrix of factor loadings $L$.
2. Choose an orthogonal transformation matrix $T$ (such that $TT' = I$).
3. Compute the rotated loadings $L^* = LT$.
4. Ensure communal variance (communality) of each variable remains exactly the same as in the unrotated solution.

### Quick Recall
> **Quick Recall:**
> - Rotation simplifies structure for interpretability.
> - $L^* = LT$, where $TT' = I$.
> - Rotated and unrotated models explain exactly the same amount of variance ($\Sigma = L^* L^{*'} + \Psi$).

### Connections
- Builds on: The Orthogonal Factor Model (Chunk 001) ambiguity property.
