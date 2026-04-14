import re

notes_4 = """# Chunk 004 — Canonical Correlation Analysis Introduction
<!-- Pages: 30-39 -->
<!-- Source: chunk_004.txt -->

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
"""

notes_5 = """# Chunk 005 — Cluster Analysis Introduction
<!-- Pages: 40-49 -->
<!-- Source: chunk_005.txt -->

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
"""

notes_6 = """# Chunk 006 — Advanced Cluster Analysis & Correspondence Analysis
<!-- Pages: 50-59 -->
<!-- Source: chunk_006.txt -->

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
"""

with open("notes/chunk_004_notes.md", "w") as f: f.write(notes_4)
with open("notes/chunk_005_notes.md", "w") as f: f.write(notes_5)
with open("notes/chunk_006_notes.md", "w") as f: f.write(notes_6)

# Update running context
with open("notes/running_context.md", "a") as f:
    f.write("\n- **Principal Component Method vs Maximum Likelihood Method** (Chunk 002): Different methods for estimating factor parameters.\n")
    f.write("- **Factor Rotation** (Chunk 002): Improves interpretability by rotating axes to achieve simple structure.\n")
    f.write("- **Oblique Rotation** (Chunk 003): Allows factors to be correlated.\n")
    f.write("- **Factor Scores** (Chunk 003): Estimated values of factors for observations.\n")
    f.write("- **Canonical Correlation Analysis** (Chunk 004): Investigates relationship between two sets of variables.\n")
    f.write("- **Cluster Analysis** (Chunk 005): Classifies objects into internally homogenous groups.\n")
    f.write("- **K-Means vs Hierarchical Clustering** (Chunk 005): Partitioning vs Tree-building clustering methods.\n")
    f.write("- **Correspondence Analysis** (Chunk 006): Dimension reduction explicitly for categorical cross-tabular data.\n")

