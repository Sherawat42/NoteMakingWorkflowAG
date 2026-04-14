# Chunk 006 — Advanced Cluster Analysis & Correspondence Analysis
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
