# Chunk 012 — Principal Component Analysis (PCA)
<!-- Pages: 103-112 -->
<!-- Source: chunk_012.txt -->

---

## Section: Methods to Construct Composite Index (Part 2) 🔴

### Core Idea

Continuing from the simple indexing methods, we encounter the **Range Equalization Method** (used by UNDP) and **Principal Component Analysis (PCA)**. PCA is an advanced mathematical tool used when variables are highly correlated. It transforms a large set of correlated variables into a smaller set of uncorrelated variables (principal components), ensuring that the composite index captures the maximum possible variance without double-counting information.

> **In Simple Terms:** If you measure "wealth" by looking at 1) number of cars, 2) size of house, and 3) bank balance, these three things are highly related (correlated). Adding them all up might double-count "wealth." PCA is a mathematical trick that finds the underlying hidden factor ("wealthiness") and gives you a single, clean score that strips out the overlap.

### Key Concepts

#### Method 4: Range Equalization Method (RE Method)

Also known as the **max-min approach**, famously used by UNDP to compute the Human Development Index (HDI). 

1. **Purpose**: Normalizes variables so they all sit on a scale exactly between 0 and 1, preventing variables with large numerical ranges (e.g., income in thousands) from dominating variables with small ranges (e.g., literacy rates in percentages).
2. **Formula**: 
   **RE Index = (Actual Value − Minimum Value) / (Maximum Value − Minimum Value)**
3. **Goalposts**: Instead of just using the sample's max and min, researchers often define theoretically desirable "goalposts" (e.g., Min literacy = 0%, Max literacy = 100%).
4. **Composite Index**: Average of the RE indices of all variables.

*Note*: MS (Mean Standardization) and RE methods usually yield highly correlated results, but RE is generally preferred because it handles wider variations better and correlates strongly with PCA.

---

## Section: Principal Component Analysis (PCA) 🔴

### Core Idea

When building an index with many variables, they are often correlated. PCA is a **data reduction technique**. It mathematically transforms the original correlated variables into a new set of *uncorrelated* variables called **Principal Components (PCs)**. The first principal component is the single line (vector) that explains the greatest amount of variation in the original dataset, serving as an excellent weighting system for a composite index.

### Key Concepts

#### When to use PCA?

- Useful when you have an array of variables with **high correlation**.
- **Not suitable for categorical data** (e.g., Religion: 1=Hindu, 2=Muslim, 3=Christian). Categorical data must be converted to binary/dummy variables (e.g., Dalit=1, Non-Dalit=0) before using PCA.

#### How PCA Works

1. **Extracting Components**: PCA creates equations where each Principal Component (PC) is a linear combination of all the original variables (weighted by coefficients).
   - PC₁ = a₁₁X₁ + a₁₂X₂ + ... + a₁ₙXₙ
2. **Variance Explanation**: Components are ordered. 
   - **PC₁** explains the *largest* possible amount of variation in the data.
   - **PC₂** is completely uncorrelated to PC₁ and explains the second largest amount of variation, and so on.
3. **Eigenvalues (λ)**: The eigenvalue tells you how much variance is captured by that component. 
   - Total variance = Number of variables (if data is standardized).
   - Proportion of variation explained by PCᵢ = λᵢ / n.
   - *Rule of thumb*: We only keep components with an **Eigenvalue > 1**.

#### Pre-PCA Checks

Before running PCA, you must check if the data is suitable:
1. **Correlation Matrix**: Variables should be correlated. If two variables are perfectly correlated, one should be removed.
2. **Kaiser-Meyer-Olkin (KMO) Test**: Measures sampling adequacy. Value should be close to 1 (minimum acceptable is 0.6).
3. **Bartlett's Test of Sphericity (BTS)**: Tests the null hypothesis that the correlation matrix is an identity matrix (variables are totally uncorrelated). We want this test to be **significant** (p < 0.05), allowing us to reject the null hypothesis and proceed with PCA.

### Understanding PCA Outputs (SPSS)

#### Output 1: Communalities
- Shows the proportion of each variable's variance that is explained by the extracted components.
- Value ranges from 0 to 1. Closer to 1 = the variable is well-represented by the PCA model.
- If communality is very low, the variable doesn't fit well with the others and might need to be dropped or treated as a stand-alone variable.

#### Output 2: Total Variance Explained
- Lists the Eigenvalues for all components.
- Shows the % of variance explained by each component and the cumulative %.
- Example: If Component 1 explains 31.4% and Component 2 explains 21.8%, then cumulatively they explain 53.2% of the total variation in the data.

#### Output 3: Scree Plot
- A line graph plotting Component Number (X-axis) against Eigenvalue (Y-axis).
- The curve drops steeply at first and then flattens out.
- **Use**: Helps visually determine how many components to keep (usually the ones on the steep slope before it flattens).

#### Output 4: Component Matrix
- Shows the "loadings" (correlations) between the original variables and the extracted Principal Components.
- Values range from -1 to +1. High absolute values mean the variable is strongly associated with that component.
- The sum of squared loadings for a variable across the kept components equals its communality.

### Definitions

- **Principal Component Analysis (PCA)**: A mathematical data reduction technique that transforms a set of correlated variables into a smaller set of uncorrelated variables called principal components. ⭐ (exam-important)
- **Eigenvalue**: A number representing the amount of variance in the dataset explained by a specific principal component. ⭐ (exam-important)
- **KMO Test**: Kaiser-Meyer-Olkin measure of sampling adequacy; validates if data is suitable for PCA (should be ≥ 0.6).
- **Communalities**: The proportion of a variable's variation that is explained by the retained principal components.
- **Range Equalization (UNDP method)**: Index = (Actual − Min) / (Max − Min). ⭐ (exam-important)

### Mechanisms / Processes

**The complete PCA workflow:**
1. Check correlations and convert categorical variables to binary.
2. Standardize data (optional but recommended; e.g., Value/Mean).
3. Run KMO and Bartlett's Test (ensure KMO > 0.6 and BTS is significant).
4. Run PCA extraction.
5. Review Communalities (drop items with very low values).
6. Review Total Variance Explained / Scree Plot (keep components where Eigenvalue > 1).
7. Review Component Matrix to understand which variables "load" onto which components.

### ⚠️ Common Mistakes

- ❌ Mistake: Using categorical classifications (like 1=General, 2=SC, 3=ST) directly in PCA → ✅ Correct: Convert to binary variables first (e.g., 1=ST, 0=Non-ST)
- ❌ Mistake: Keeping all principal components → ✅ Correct: Only keep components that capture significant variance (Eigenvalue > 1)

> **Quick Recall:**
> - PCA solves the problem of double-counting highly correlated variables.
> - KMO test tells you if you *should* run PCA (>0.6).
> - Eigenvalue tells you how much variance a component explains.
> - PC1 always explains the most variance.
> - Range Equalization sets everything between 0 and 1 using Max and Min goalposts (UNDP method).

### Connections

- Builds on: Normalization techniques from Chunk 011.
- Leads to: Finalizing the composite index using PCA weights (Chunk 013).
