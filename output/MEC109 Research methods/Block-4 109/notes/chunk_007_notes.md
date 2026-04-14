# Chunk 007 — Correspondence Analysis Mechanisms
<!-- Pages: 60-69 -->
<!-- Source: chunk_007.txt -->

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
