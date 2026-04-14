# Complete Notes


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
- Provides the foundation for: Factor Rotation (Chunk 002: Communalities)


---


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
- Builds on: The Orthogonal Factor Model (Chunk 001: Introduction) ambiguity property.


---


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


---


## Section: Canonical Correlation Analysis (CCA) 🔴

### Core Idea
Canonical Correlation Analysis (CCA) is a multivariate statistical model that facilitates the study of interrelationships among two sets of multiple variables. Unlike multiple regression which has one dependent and many independent variables, CCA handles multiple dependent and multiple independent variables simultaneously.

> **In Simple Terms:** Imagine trying to see how a set of psychological traits (anxiety, depression) relates to a set of physical traits (heart rate, blood pressure). Instead of running many separate regressions, CCA finds the maximum correlation between two linear combinations of these sets.

### Key Concepts
#### Purpose of CCA
The goal is to find pairs of linear combinations (one from set X and one from set Y) that have the highest possible correlation. These linear combinations are called canonical variables, and their correlation is the canonical correlation.

### Definitions
- **Canonical Correlation Analysis**: A multivariate technique that investigates the relationship between two sets of variables by finding linear combinations of each set that maximally correlate with each other. ⭐ (exam-important)

## Section: Assumptions of Canonical Correlation 🟡

### Core Idea
CCA operates optimally under certain assumptions about the data: linearity, multivariate normality, homoscedasticity, and absence of multicollinearity within the sets. Violations affect the significance tests and canonical weights.

### Quick Recall
> **Quick Recall:**
> - Linearity must exist between any two variables.
> - Multivariate normality is required for significance tests.
> - Large sample size is often necessary (e.g., at least 10 observations per variable).

## Section: CCA as Generalization of Multiple Regression 🔴

### Core Idea
Multiple regression is a special case of Canonical Correlation where the dependent variable set contains only one variable. In this case, the canonical correlation exactly equals the multiple correlation coefficient ($R$).

### Connections
- Builds on: Basic multiple regression theory.

## Section: Steps and Procedure of CCA 🔴

### Mechanisms / Processes
1. **Derive canonical variates**: Determine the linear equations that combine standard variables for set X and set Y.
2. **Calculate Canonical Correlation ($R_c$)**: Maximize the correlation between the pair of variates. 
3. **Subsequent variates**: After the first (maximum) pair, find the next pair orthogonal to the first that maximizes the remaining correlation, and so on.
4. **Significance Testing**: Use tests like Wilks' Lambda to test if the canonical correlation is statistically significant.

## Section: Illustration of CCA 🟢

### Examples
**Example: Student Performance and Aptitude**
Set X = (Reading Score, Math Score) and Set Y = (Overall GPA, Standardized Test). CCA extracts $V_1$ (a combination of X) and $U_1$ (a combination of Y) that correlate highest.

## Section: Interpretation & Limitations of CCA 🔴

### Core Idea
Interpretation relies on Canonical Weights (the coefficients in the linear combination) and Canonical Loadings (the correlation between the original variable and the canonical variate). Loadings are generally preferred over weights for interpretation because they are not affected by multicollinearity among variables in the same set.

### Edge Cases & Caveats
- CCA maximizes correlation, not necessarily variance explained. The variates might correlate highly but only account for a tiny fraction of the original variables' variance.
- Extremely sensitive to minor changes in the dataset, especially with small sample sizes.


---


## Section: Cluster Analysis Concept and Meaning 🔴

### Core Idea
Cluster Analysis is a multivariate technique used to classify a set of objects, data points, or individuals into distinct groups (clusters) such that objects in the same cluster are highly similar, while objects across different clusters are highly dissimilar.

> **In Simple Terms:** It's like sorting a massive, mixed pile of legos into distinct bins so that pieces inside a bin share color and shape, while different bins hold distinctly different pieces.

### Definitions
- **Cluster Analysis**: A data-reduction and classification technique that groups elements based on similarity of their attributes, creating internally homogenous and externally heterogeneous clusters. ⭐ (exam-important)

## Section: Steps and Algorithm in Cluster Analysis 🔴

### Mechanisms / Processes
1. **Select Variables**: Choose the attributes to compute similarity.
2. **Select Distance Measure**: Choose a metric (e.g., Euclidean distance, Manhattan distance) to measure object similarity.
3. **Select Clustering Procedure**: Choose between Non-hierarchical (Partitioning) or Hierarchical methods.
4. **Determine Number of Clusters**: Use criteria (e.g., dendrogram inspection, scree plots) to decide optimal $k$.
5. **Interpret and Validate**: Analyze cluster profiles to assign meaning to each cluster.

## Section: Methods of Cluster Analysis 🟡

### Core Idea
Cluster analysis methods broadly fall into two core categories: Partitioning (Non-hierarchical) and Hierarchical methods. The choice depends on the size of the dataset and whether the user knows the desired number of clusters beforehand.

## Section: Partitioning Clustering Methods 🔴

### Core Idea
Partitioning methods, like K-Means, attempt to directly divide the data into a pre-specified number ($K$) of exclusive clusters. They iteratively reassign items to clusters to minimize the within-cluster variation (variance).

### Key Concepts
#### K-means algorithm
The most popular partitioning method. 
1. The user specifies $k$.
2. $k$ initial cluster centroids (seeds) are chosen.
3. Each observation is assigned to the nearest centroid.
4. Centroids are recalculated.
5. Repeat steps 3 and 4 until assignments no longer change.

## Section: Hierarchical Clustering Methods 🔴

### Core Idea
Hierarchical clustering builds a tree-like hierarchy of clusters (a dendrogram) and does not require pre-specifying the number of clusters. 

### Key Concepts
#### Agglomerative vs Divisive
- **Agglomerative (Bottom-up)**: Starts with each observation as its own cluster. At each step, the two most similar clusters merge until all form a single massive cluster.
- **Divisive (Top-down)**: Starts with all observations in one massive cluster. At each step, it splits the most heterogeneous cluster until every point is its own cluster.

### Connections
- Contrasts with: Partitioning methods which require $k$ initially.


---


## Section: Other Approaches: Two-Step Cluster Analysis 🟡

### Core Idea
The Two-Step cluster analysis is an approach designed to handle very large datasets or datasets that contain both continuous and categorical variables. It first creates many small sub-clusters (pre-clustering) and then clusters those sub-clusters into the final groups.

## Section: Interpretation of Cluster Results 🔴

### Core Idea
Once clusters are formed, the researcher calculates the mean profiles (centroids) of each cluster on the original variables. These profiles are used to label the clusters (e.g., "High-income traditionalists" vs "Low-income urban youth") based on what variables distinguish them.

### Edge Cases & Caveats
- Cluster analysis is largely exploratory. Different algorithms or different distance measures can yield completely different clusters on the exact same dataset. There are few statistical tests to "prove" a cluster solution is correct.

## Section: Correspondence Analysis Concept and Features 🔴

### Core Idea
Correspondence Analysis (CA) is a multivariate technique for exploring cross-tabular (contingency table) data. It transforms categorical data into a graphical display (a biplot) where rows and columns are represented as points in a low-dimensional space, revealing their associations.

> **In Simple Terms:** Just as Factor Analysis simplifies numerical data, Correspondence Analysis takes standard categorical cross-tables (like a survey cross-tabbing Gender vs Product Preference) and turns them into a 2D map so you can visually see which categories are "close" to each other.

### Definitions
- **Correspondence Analysis**: A compositional and dimension reduction technique applied to cross-tabular categorical data to plot rows and columns symmetrically in a shared spatial map. ⭐ (exam-important)


---


## Section: Steps and Algorithm in Correspondence Analysis 🔴

### Mechanisms / Processes
1. **Prepare Contingency Table**: Set up the cross-tabulation of frequency data (Primitive Matrix).
2. **Compute Profiles**: Calculate row profiles and column profiles (relative frequencies).
3. **Compute Masses**: Determine the marginal weight (mass) of each row and column.
4. **Calculate Inertia**: Compute the total inertia (total variance/dispersion) of the table using Chi-square distance.
5. **Dimensionality Reduction**: Apply Singular Value Decomposition (SVD) to extract principal axes that explain the most inertia.
6. **Plotting**: Construct a Biplot where rows and columns are mapped coordinately.

## Section: Basic Concepts and Definitions of CA 🔴

### Definitions
- **Primitive Matrix**: The original contingency table containing raw counts or frequency data where rows represent one categorical variable and columns represent the other. ⭐ (exam-important)
- **Profiles**: The relative frequencies computed by dividing each cell count by its row total (Row Profile) or its column total (Column Profile). ⭐ (exam-important)
- **Masses**: The marginal proportions. The mass of a row is its total sum divided by the grand total of the matrix. Represents the relative importance of that row/column. 
- **Correspondence Matrix**: The matrix formed by dividing every element in the primitive matrix by the grand total.
- **Augmented Correspondence Matrix**: A matrix supplementing the correspondence matrix with vectors of row and column masses.
- **Inertia**: In CA, inertia is the measure of the total variation or dispersion of the profiles around the average profile. It is directly related to the Chi-square statistic ($\chi^2 / n$). ⭐ (exam-important)
- **Distance**: The Chi-square distance measures the metric distance between profiles in the multi-dimensional space, weighting squares inversely by the profile mass.

## Section: Biplots & Interpretation 🟡

### Core Idea
A biplot graphically displays both the rows and the columns of the contingency table in the same reduced-dimensional space. The proximity between a row point and a column point loosely indicates strength of association, while distance between two row points indicates the similarity of their profiles.

## Section: Multiple Correspondence Analysis 🟡

### Core Idea
While simple Correspondence Analysis works on two categorical variables (a 2-way contingency table), Multiple Correspondence Analysis (MCA) extends this logic to three or more categorical variables, usually by performing CA on an indicator matrix or a Burt matrix.


---


## Section: Structural Equation Modelling (SEM) Concept 🔴

### Core Idea
Structural Equation Modeling (SEM) is an advanced multivariate technique that combines elements of multiple regression and factor analysis. It attempts to simultaneously model and estimate complex causal relationships (the structural model) among both directly observed variables and unobserved latent variables (the measurement model).

> **In Simple Terms:** SEM allows researchers to test complicated "pathways" of cause and effect between abstract concepts (like "customer satisfaction" and "loyalty"), using the actual measurable survey questions that stand in for those abstract concepts.

### Definitions
- **Structural Equation Modeling (SEM)**: A comprehensive statistical methodology for evaluating complex causal theoretical models hypothesizing relationships among both observed (manifest) and unobserved (latent) variables. ⭐ (exam-important)

## Section: Why conduct SEM? 🟡

### Core Idea
SEM is conducted because it allows for the simultaneous estimation of multiple interconnected dependence relationships. Unlike regular regression which looks at one dependent variable at a time,, SEM can handle variables that are independent in one relationship and dependent in another. It also crucially accounts for measurement error explicitly in the model.

## Section: Assumptions of SEM 🔴

### Core Idea
Because SEM relies heavily on parameter estimation techniques like Maximum Likelihood, it carries strict mathematical prerequisites. Violating these assumptions can lead to severely biased estimates and incorrect inferences.

### Quick Recall
> **Quick Recall:**
> - **Large sample size**: Usually $N > 200$ or at least 10 observations per parameter estimated.
> - **Multivariate normality**: Variables and their joint distributions should be normally distributed.
> - **Continuous indicator variables**: Likert scales are often treated as continuous but true continuous variables are preferable.
> - **Linearity**: The relationships between variables are assumed to be strictly linear.
> - **No Specification error**: All relevant variables are included and irrelevant ones excluded.


---


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


---


## Section: Steps in SEM (Evaluation, Modification, Reporting) 🔴

### Mechanisms / Processes
1. **Model Evaluation**: Assess how well the theorized model fits the actual data matrix. This involves checking:
   - Absolute fit indices (e.g., Chi-square, RMSEA).
   - Incremental fit indices (e.g., CFI, TLI).
2. **Model Modification**: If the fit is poor, the model is re-specified by freeing or constraining pathways, guided by "modification indices" produced by the software, but strictly justified by theory.
3. **Reporting Results**: Present clear diagrams, specify all fit metrics used, and clarify interpretation of parameter estimates.

## Section: Example of SEM 🟢

### Examples
**Example: Consumer Purchasing Behavior**
A researcher asserts that "Perceived Quality" and "Brand Image" (latent constructs) drive "Purchase Intention". Survey questions (manifest indicators) measure these abstract ideas. SEM evaluates whether the data supports the structural paths between Quality, Image, and Intention while simultaneously tracking measurement reliability for the survey questions.

## Section: Software Programs for SEM 🟢

### Core Idea
SEM requires specialized statistical software due to the complexity of the matrix algebra and maximum likelihood estimations involved.
- **LISREL**: The oldest and historically most prominent SEM software.
- **AMOS**: Popular due to its highly visual, drag-and-drop graphical interface for drawing path diagrams, now bundled with SPSS.
- **EQS, Mplus, Mx**: Alternatives offering specific strengths, such as Mplus for categorical and complex survey data.

## Section: Advantages and Disadvantages of SEM 🟡

### Quick Recall
> **Quick Recall:**
> - **Advantages**: Estimates multiple interrelated dependence relationships at once; explicitly accounts for measurement error; permits testing of entire theoretical models instead of single coefficients.
> - **Disadvantages**: (Continued in next chunk) Requires rigorous theoretical justification; mathematically complex; demands large sample sizes and strict assumptions.


---


## Section: SEM Wrap-up 🟢

### Core Idea
Structural Equation Modelling is a robust technique, but researchers must remain aware of its limitations. Unlike simple experimental designs, SEM cannot universally prove causality—it only demonstrates statistical alignment with a proposed causal theory. If a model fits well, it proves the theory is plausible, not that it is definitively correct.

### Quick Recall
> **Quick Recall:**
> - Disadvantages include: High reliance on strict assumptions, high sensitivity to sample size and missing data, and the risk of researcher confirmation bias if modifications are made purely for statistical fit without theoretical backing.


---

