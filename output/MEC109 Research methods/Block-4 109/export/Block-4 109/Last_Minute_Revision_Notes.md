# Last Minute Revision Notes

> *This document contains ONLY ultra-high-yield definitions (⭐), Quick Recall facts, Common Mistakes, and core bullet points.*


## Topics


### Factor Analysis: Concept and Meaning 🔴

**Determinate vs Indeterminate Models**
- **Factor Analysis**: A set of multi-variate statistical models that model observed variables as linear functions of a set of latent or hypothetical variables not directly observed. ⭐ (exam-important)

### The Orthogonal Factor Model 🔴

**Notations and Terminology**
- $X$ is the vector of sample means.
- $\Sigma$ is the population covariance matrix, estimated by the sample covariance matrix $S$.
- $F$ is the vector of unobserved common factors ($F_1, F_2, \dots , F_m$), where typically $m < p$ (number of variables).

**The Factor Model Formulation**

**Model Assumptions**
1. Specific factors ($\epsilon$) have a mean of 0.
2. Common factors ($F$) have a mean of 0.
3. Specific factors are independent of each other (covariance is 0) with variance $\Psi_i$.
4. Common factors have a variance of 1 and are mutually uncorrelated (covariance matrix is $I$).
5. Specific factors and common factors are independent of each other.
- **Common Factors**: Unobserved latent variables ($F$) that control the variation among the data. ⭐ (exam-important)
- **Factor Loadings**: The regression coefficients ($\ell_{ij}$) denoting the loading of the $i^{th}$ variable on the $j^{th}$ factor. ⭐ (exam-important)
- **Specific Factors (Errors)**: The error term ($\epsilon_i$) representing the part of the variance that is specific to the variable $i$ only.
- **Specific Variance**: The variance ($\Psi_i$) of the specific factor $i$.
- **Communality**: The sum of the squared loadings for a given variable, representing the variance explained by the common factors. ⭐ (exam-important)
1. Represent $X_i$ as a linear combination of common factors and a specific factor.
2. Define the sample mean $\mu$ and covariance $S$.
3. Compute the matrix of factor loadings $L$.
4. Establish the covariance structure $\Sigma = L L' + \Psi$.
5. Acknowledge model ambiguity: An infinite number of orthogonal matrices $T$ exist where $T T' = I$. Thus $L^\ast = L T$ gives a model that fits equally well, justifying factor rotation.

**Quick Recall:**
- The basic factor equation is $X = \mu + L F + \epsilon$.
- The covariance matrix is structured as $\Sigma = L L' + \Psi$.
- The variance of an observed variable is its communality plus its specific variance.
- The inherent ambiguity (infinite orthogonal matrices) justifies factor rotation.
- Provides the foundation for: Factor Rotation (Chunk 002)

**Quick Recall:**
- $Communality (h_i^2) = l_{i1}^2 + l_{i2}^2 + \dots + l_{im}^2$
- Total Variance = Communality + Specific Variance

### Methods of Estimation 🔴

**Principal Component Method**

**Maximum Likelihood Method**
- **Principal Component Method**: A descriptive factor estimation method that approximates the covariance matrix using spectral (eigenvalue) decomposition without initially relying on specific variances. ⭐ (exam-important)
- **Maximum Likelihood Method**: An estimation technique maximizing the likelihood function based on a multivariate normal distribution assumption to estimate $L$ and $\Psi$. ⭐ (exam-important)
1. Compute the sample covariance matrix $S$.
2. Find eigenvalues $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_p$ and their eigenvectors $e_1, e_2, \dots, e_p$.
3. Compute unrotated factor loadings: $\hat{l}_{ij} = \sqrt{\hat{\lambda}_j} \hat{e}_{ij}$.
4. Compute communalities and specific variances $\Psi = S - \hat{L}\hat{L}'$.
- The Principal Component Method is technically factoring the total variance rather than just the common variance.
- ML estimation requires large sample sizes and the assumption of multivariate normality, which may not always hold true.

**Quick Recall:**
- PCA method uses $\hat{L} = \sqrt{\Lambda} E$.
- ML method relies on maximizing normal likelihoods.

### Factor Rotation 🔴

**Purpose of Rotation**
1. Extract initial unrotated matrix of factor loadings $L$.
2. Choose an orthogonal transformation matrix $T$ (such that $TT' = I$).
3. Compute the rotated loadings $L^* = LT$.
4. Ensure communal variance (communality) of each variable remains exactly the same as in the unrotated solution.

**Quick Recall:**
- Rotation simplifies structure for interpretability.
- $L^* = LT$, where $TT' = I$.
- Rotated and unrotated models explain exactly the same amount of variance ($\Sigma = L^* L^{*'} + \Psi$).
- Builds on: The Orthogonal Factor Model (Chunk 001) ambiguity property.

### Factor Scores 🔴
- **Factor Scores**: Estimates of the unobserved common factor values for individual observations, derived from the observed data and estimated factor loadings. ⭐ (exam-important)

### Methods for Estimating Factor Scores 🔴

**Ordinary Least Squares Method**

**Weighted Least Squares Method**

**Regression Method**
1. **OLS Prediction**: Standard unweighted error minimization. Used when specific variances are largely assumed equal or ignored.
2. **WLS Prediction**: Minimizes $\epsilon' \Psi^{-1} \epsilon$. The most common method advocated for maximum likelihood extraction because it directly incorporates $\Psi$. 
3. **Regression Prediction**: Focuses on maximum validity relative to the true factor scores, but generated scores may be slightly correlated even for orthogonal factors because it relies on the sample covariance matrix inverse ($S^{-1}$).

**Quick Recall:**
- OLS: treats all errors equally; $\hat{F} = (L'L)^{-1} L' X_{centered}$.
- WLS: weighs highly reliable variables more using $\Psi^{-1}$.
- Regression Method: uses conditional expectation $\hat{F} = L'\Sigma^{-1}X_{centered}$.

### Canonical Correlation Analysis (CCA) 🔴

**Purpose of CCA**
- **Canonical Correlation Analysis**: A multivariate technique that investigates the relationship between two sets of variables by finding linear combinations of each set that maximally correlate with each other. ⭐ (exam-important)

**Quick Recall:**
- Linearity must exist between any two variables.
- Multivariate normality is required for significance tests.
- Large sample size is often necessary (e.g., at least 10 observations per variable).

### CCA as Generalization of Multiple Regression 🔴
- Builds on: Basic multiple regression theory.

### Steps and Procedure of CCA 🔴
1. **Derive canonical variates**: Determine the linear equations that combine standard variables for set X and set Y.
2. **Calculate Canonical Correlation ($R_c$)**: Maximize the correlation between the pair of variates. 
3. **Subsequent variates**: After the first (maximum) pair, find the next pair orthogonal to the first that maximizes the remaining correlation, and so on.
4. **Significance Testing**: Use tests like Wilks' Lambda to test if the canonical correlation is statistically significant.

### Interpretation & Limitations of CCA 🔴
- CCA maximizes correlation, not necessarily variance explained. The variates might correlate highly but only account for a tiny fraction of the original variables' variance.
- Extremely sensitive to minor changes in the dataset, especially with small sample sizes.

### Cluster Analysis Concept and Meaning 🔴
- **Cluster Analysis**: A data-reduction and classification technique that groups elements based on similarity of their attributes, creating internally homogenous and externally heterogeneous clusters. ⭐ (exam-important)

### Steps and Algorithm in Cluster Analysis 🔴
1. **Select Variables**: Choose the attributes to compute similarity.
2. **Select Distance Measure**: Choose a metric (e.g., Euclidean distance, Manhattan distance) to measure object similarity.
3. **Select Clustering Procedure**: Choose between Non-hierarchical (Partitioning) or Hierarchical methods.
4. **Determine Number of Clusters**: Use criteria (e.g., dendrogram inspection, scree plots) to decide optimal $k$.
5. **Interpret and Validate**: Analyze cluster profiles to assign meaning to each cluster.

### Partitioning Clustering Methods 🔴

**K-means algorithm**
1. The user specifies $k$.
2. $k$ initial cluster centroids (seeds) are chosen.
3. Each observation is assigned to the nearest centroid.
4. Centroids are recalculated.
5. Repeat steps 3 and 4 until assignments no longer change.

### Hierarchical Clustering Methods 🔴

**Agglomerative vs Divisive**
- **Agglomerative (Bottom-up)**: Starts with each observation as its own cluster. At each step, the two most similar clusters merge until all form a single massive cluster.
- **Divisive (Top-down)**: Starts with all observations in one massive cluster. At each step, it splits the most heterogeneous cluster until every point is its own cluster.
- Contrasts with: Partitioning methods which require $k$ initially.

### Interpretation of Cluster Results 🔴
- Cluster analysis is largely exploratory. Different algorithms or different distance measures can yield completely different clusters on the exact same dataset. There are few statistical tests to "prove" a cluster solution is correct.

### Correspondence Analysis Concept and Features 🔴
- **Correspondence Analysis**: A compositional and dimension reduction technique applied to cross-tabular categorical data to plot rows and columns symmetrically in a shared spatial map. ⭐ (exam-important)

### Steps and Algorithm in Correspondence Analysis 🔴
1. **Prepare Contingency Table**: Set up the cross-tabulation of frequency data (Primitive Matrix).
2. **Compute Profiles**: Calculate row profiles and column profiles (relative frequencies).
3. **Compute Masses**: Determine the marginal weight (mass) of each row and column.
4. **Calculate Inertia**: Compute the total inertia (total variance/dispersion) of the table using Chi-square distance.
5. **Dimensionality Reduction**: Apply Singular Value Decomposition (SVD) to extract principal axes that explain the most inertia.
6. **Plotting**: Construct a Biplot where rows and columns are mapped coordinately.

### Basic Concepts and Definitions of CA 🔴
- **Primitive Matrix**: The original contingency table containing raw counts or frequency data where rows represent one categorical variable and columns represent the other. ⭐ (exam-important)
- **Profiles**: The relative frequencies computed by dividing each cell count by its row total (Row Profile) or its column total (Column Profile). ⭐ (exam-important)
- **Masses**: The marginal proportions. The mass of a row is its total sum divided by the grand total of the matrix. Represents the relative importance of that row/column. 
- **Correspondence Matrix**: The matrix formed by dividing every element in the primitive matrix by the grand total.
- **Augmented Correspondence Matrix**: A matrix supplementing the correspondence matrix with vectors of row and column masses.
- **Inertia**: In CA, inertia is the measure of the total variation or dispersion of the profiles around the average profile. It is directly related to the Chi-square statistic ($\chi^2 / n$). ⭐ (exam-important)
- **Distance**: The Chi-square distance measures the metric distance between profiles in the multi-dimensional space, weighting squares inversely by the profile mass.

### Structural Equation Modelling (SEM) Concept 🔴
- **Structural Equation Modeling (SEM)**: A comprehensive statistical methodology for evaluating complex causal theoretical models hypothesizing relationships among both observed (manifest) and unobserved (latent) variables. ⭐ (exam-important)

### Assumptions of SEM 🔴

**Quick Recall:**
- **Large sample size**: Usually $N > 200$ or at least 10 observations per parameter estimated.
- **Multivariate normality**: Variables and their joint distributions should be normally distributed.
- **Continuous indicator variables**: Likert scales are often treated as continuous but true continuous variables are preferable.
- **Linearity**: The relationships between variables are assumed to be strictly linear.
- **No Specification error**: All relevant variables are included and irrelevant ones excluded.

### Concepts and Terminology used in SEM 🔴
- **Path Diagram**: A graphical representation of the theoretical model showing variables and the hypothesized causal (directed arrows) and correlational (curved, double-headed arrows) relationships among them. ⭐ (exam-important)
- **Latent Variable**: Unobserved theoretical constructs (factors) that are inferred from a set of observed measured variables. ⭐ (exam-important)
- **Manifest (Observed) Variable**: The actual measurable data points (like survey answers) used as indicators for latent variables.

### SEM Models Specification 🔴

**Reflective Indicators**

**Formative Indicators**

### Steps in SEM (Initial Spec & Estimation) 🔴
1. **Initial Model Specification**: The researcher mathematically and graphically defines the hypothesized relationships based strictly on theory.
2. **Model Estimation**: The software uses algorithms (usually Maximum Likelihood) to calculate parameter estimates (path coefficients, variances) that minimize the difference between the sample covariance matrix and the covariance matrix implied by the specified theoretical model.

### Steps in SEM (Evaluation, Modification, Reporting) 🔴
1. **Model Evaluation**: Assess how well the theorized model fits the actual data matrix. This involves checking:
   - Absolute fit indices (e.g., Chi-square, RMSEA).
   - Incremental fit indices (e.g., CFI, TLI).
2. **Model Modification**: If the fit is poor, the model is re-specified by freeing or constraining pathways, guided by "modification indices" produced by the software, but strictly justified by theory.
3. **Reporting Results**: Present clear diagrams, specify all fit metrics used, and clarify interpretation of parameter estimates.

**Quick Recall:**
- **Advantages**: Estimates multiple interrelated dependence relationships at once; explicitly accounts for measurement error; permits testing of entire theoretical models instead of single coefficients.
- **Disadvantages**: (Continued in next chunk) Requires rigorous theoretical justification; mathematically complex; demands large sample sizes and strict assumptions.

**Quick Recall:**
- Disadvantages include: High reliance on strict assumptions, high sensitivity to sample size and missing data, and the risk of researcher confirmation bias if modifications are made purely for statistical fit without theoretical backing.
