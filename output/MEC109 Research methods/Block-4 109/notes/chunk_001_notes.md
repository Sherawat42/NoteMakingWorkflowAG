# Chunk 001 — Multivariate Analysis: Factor Analysis (Intro & Orthogonal Model)
<!-- Pages: 1-10 -->
<!-- Source: chunk_001.txt -->

## Section: Introduction 🟢

### Core Idea
Factor analysis extends principal component analysis to reduce and manage large numbers of qualitative and quantitative variables. It discerns underlying regularities and distinct patterns of occurrence in entangled data, allowing researchers to explore content areas and illuminate causal relationships.

> **In Simple Terms:** Imagine you have hundreds of different measurements of human behavior; factor analysis helps group these into a few distinct, underlying patterns or "factors" that explain the overall variation.

### Key Concepts
#### Factor Analysis Scope
Factor analysis is used to map unknown concepts, classify data, illuminate causal nexus, define relationships, and formulate theories. It resolves thousands of measurements into distinct patterns, helping to identify factors causing variation in social or economic issues.

## Section: Factor Analysis: Concept and Meaning 🔴

### Core Idea
Factor analysis comprises distinct multi-variate statistical models where observed variables are represented as linear functions of a set of latent (unobserved) variables called factors. Unlike regression models, the independent variables (factors) are not independently observed from the dependent variables.

> **In Simple Terms:** It’s like a regression analysis where you don't actually have the data for the independent variables—instead, you infer these hidden "factors" from how the observed variables move together.

### Key Concepts

#### Determinate vs Indeterminate Models
Factor models can be determinate (like Principal Components Analysis) or indeterminate (like the common factor model). Determinate models are primarily useful for data reduction, capturing most variation into fewer variables. Indeterminate models account for co-variation between observed variables and common factors that cannot be directly derived as linear combinations of the observed variables.

### Definitions
- **Factor Analysis**: A set of multi-variate statistical models that model observed variables as linear functions of a set of latent or hypothetical variables not directly observed. ⭐ (exam-important)

## Section: Historical Background of Factor Analysis 🟢

### Core Idea
Factor analysis originated with Charles Spearman in 1904, based on his analysis of schoolchildren's examination scores. He proposed the two-factor theory of mental tests, suggesting that test scores consist of a common general intelligence factor and a test-specific factor.

### Examples
**Example: Spearman's Test Scores**
Spearman analyzed correlation matrices of scores in Classics, French, English, Math, Pitch Discrimination, and Music. He noticed rows were nearly proportional, deducing a common factor underlying these disparate metrics.

## Section: The Orthogonal Factor Model 🔴

### Core Idea
The Orthogonal Factor Model treats each observable variable as a linear function of unobservable common factors and an error term (specific factor). It describes the sample covariance matrix using a matrix of factor loadings and a diagonal matrix of specific variances, assuming the factors themselves are uncorrelated and standardized.

> **In Simple Terms:** Every piece of data you observe is made up of a combination of shared hidden factors plus a unique error specific to that data point. 

### Key Concepts

#### Notations and Terminology
- $X$ is the vector of sample means.
- $\Sigma$ is the population covariance matrix, estimated by the sample covariance matrix $S$.
- $F$ is the vector of unobserved common factors ($F_1, F_2, \dots , F_m$), where typically $m < p$ (number of variables).

#### The Factor Model Formulation
The model predicts each observable variable $X_i$ from unobservable factors:
$X_i = \mu_i + \ell_{i1}F_1 + \dots + \ell_{im}F_m + \epsilon_i$
In matrix notation: $X = \mu + L F + \epsilon$.
Here, $\mu$ represents intercepts, $L$ is the matrix of factor loadings (slopes), and $\epsilon$ represents specific factors.

#### Model Assumptions
1. Specific factors ($\epsilon$) have a mean of 0.
2. Common factors ($F$) have a mean of 0.
3. Specific factors are independent of each other (covariance is 0) with variance $\Psi_i$.
4. Common factors have a variance of 1 and are mutually uncorrelated (covariance matrix is $I$).
5. Specific factors and common factors are independent of each other.
Consequently, the covariance structure is: $\Sigma = L L' + \Psi$.

### Definitions
- **Common Factors**: Unobserved latent variables ($F$) that control the variation among the data. ⭐ (exam-important)
- **Factor Loadings**: The regression coefficients ($\ell_{ij}$) denoting the loading of the $i^{th}$ variable on the $j^{th}$ factor. ⭐ (exam-important)
- **Specific Factors (Errors)**: The error term ($\epsilon_i$) representing the part of the variance that is specific to the variable $i$ only.
- **Specific Variance**: The variance ($\Psi_i$) of the specific factor $i$.
- **Communality**: The sum of the squared loadings for a given variable, representing the variance explained by the common factors. ⭐ (exam-important)

### Mechanisms / Processes
1. Represent $X_i$ as a linear combination of common factors and a specific factor.
2. Define the sample mean $\mu$ and covariance $S$.
3. Compute the matrix of factor loadings $L$.
4. Establish the covariance structure $\Sigma = L L' + \Psi$.
5. Acknowledge model ambiguity: An infinite number of orthogonal matrices $T$ exist where $T T' = I$. Thus $L^\ast = L T$ gives a model that fits equally well, justifying factor rotation.

### Quick Recall
> **Quick Recall:**
> - The basic factor equation is $X = \mu + L F + \epsilon$.
> - The covariance matrix is structured as $\Sigma = L L' + \Psi$.
> - The variance of an observed variable is its communality plus its specific variance.
> - The inherent ambiguity (infinite orthogonal matrices) justifies factor rotation.

### Connections
- Provides the foundation for: Factor Rotation (Chunk 002)
