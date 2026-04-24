# Chunk 011 — 2SLS Summary
<!-- Pages: 98-100 -->
<!-- Source: chunk_011.txt -->

## Section: Two-Stage Least Squares (2SLS) Estimator (Continued) 🔴
<!-- This section continues from chunk 010 -->

### Core Idea
When there are multiple potential instrumental variables ($z_h$) available, there are multiple possible Instrumental Variable (IV) estimators. The 2SLS method resolves the dilemma of choosing among them by mathematically combining all instruments into a single optimal estimation process.

### Key Concepts

#### Summary of Methods
- If an explanatory variable is correlated with the error term, we face the endogeneity problem, and the OLS estimator is biased and inconsistent.
- To solve this, we use the Instrumental Variable (IV) method. An instrument must be strongly correlated with the endogenous variable and completely uncorrelated with the error term.
- Because there are often many more instrumental variables available than endogenous variables (e.g., any linear combination of $z_1, z_2, \\dots, z_M$), the 2SLS method is employed.
- **Why 2SLS is preferred**: The 2SLS estimator mathematically guarantees the most efficient (minimum variance) IV estimator possible when multiple instruments are present.

### Quick Recall
- Endogeneity -> Use IV.
- Multiple Instruments -> Use 2SLS.
- 2SLS provides the most efficient IV estimator.

### Connections
- Concludes the unit on Stochastic Regressors (Unit 13).
- Concludes Block-3 of MECE-101.
