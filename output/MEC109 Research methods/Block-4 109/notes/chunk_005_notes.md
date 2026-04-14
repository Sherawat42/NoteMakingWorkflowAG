# Chunk 005 — Cluster Analysis Introduction
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
