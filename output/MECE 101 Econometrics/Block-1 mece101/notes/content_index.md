# Content Index
**Source**: Block-1 mece101.pdf | **Chunks**: 7 | **Completed**: 2026-04-24T03:08:00Z

## Notes Files

| Chunk | Title | Pages | Top Sections | Key Terms |
|-------|-------|-------|--------------|-----------|
| 001 | Course Introduction & Unit 1 Objectives | 1–8 | Course Overview, Scope of Econometrics | Econometrics, Theoretical vs Applied |
| 002 | Econometric Models, Steps, Specification, DGP, Functional Forms | 9–18 | Econometric Models, 6 Steps, DGP, Semi-Log, Log-Linear | PRF, SRF, u, Elasticity, DGP |
| 003 | End of Unit 1 & Unit 2: Estimation & Properties | 19–28 | Software, Key Words, Point/Interval Estimation, Estimator Properties | MVUE, MSE, Unbiasedness, Consistency, Efficiency |
| 004 | Asymptotic Properties, LLN, CLT, Hypothesis Testing, Estimation Methods | 29–39 | WLLN, SLLN, CLT, H₀/H₁, Type I/II Errors, OLS, MLE | α, p-value, Normal Equations, Score Function |
| 005 | Unit 2 CYP Answers & Matrix Algebra Fundamentals | 40–49 | Unit 2 CYP, Matrix Types, Multiplication, Determinants, Inverse, Rank | Iₙ, Symmetric, Orthogonal, Trace, (AB)⁻¹=B⁻¹A⁻¹ |
| 006 | Partitioned Matrices, Eigenvalues, Special Matrices | 50–59 | Partitioned, Eigenvalues, PD/PSD, QR, SVD, Idempotent | λ, Diagonalisation, M-matrix, H-matrix, Cholesky |
| 007 | Kronecker Product, Vec-Operator, Matrix Differentiation, CYP Answers | 60–67 | Kronecker ⊗, Vec, Jacobian, Gradient/Score, Hessian, Fisher I(θ) | vec(ABC)=(C'⊗A)vec(B), S(θ), I(θ) |

---

## Cross-References

| From | To | Relationship |
|------|----|-------------|
| Econometric Models (Chunk 002) | Scope of Econometrics (Chunk 001) | Builds on |
| Stochastic Specification (Chunk 002) | Econometric Models (Chunk 002) | Builds on |
| DGP (Chunk 002) | Stochastic Specification (Chunk 002) | Builds on |
| Functional Forms (Chunk 002) | Classical Regression Model (Chunk 002) | Extends |
| Statistical Inference (Chunk 003) | Classical Assumptions on u (Chunk 002) | Prerequisite for |
| Properties of Estimators (Chunk 003) | Statistical Inference (Chunk 003) | Builds on |
| Asymptotic Properties (Chunk 004) | Estimator Properties (Chunk 003) | Extends (large-sample version) |
| WLLN & SLLN (Chunk 004) | Consistency (Chunk 003) | Formalises |
| CLT (Chunk 004) | Sampling Distribution (Chunk 003) | Derives |
| Hypothesis Testing (Chunk 004) | CLT + Confidence Interval (Chunks 003–004) | Builds on |
| OLS / MLE (Chunk 004) | Properties of Estimators (Chunk 003) | Applies |
| Matrix Notation (Chunk 005) | Unit 3 Introduction (Chunk 005) | Foundation for |
| Matrix Multiplication (Chunk 005) | Matrix Notation (Chunk 005) | Builds on |
| Determinants (Chunk 005) | Matrix Multiplication (Chunk 005) | Builds on |
| Matrix Inverse (Chunk 005) | Determinants (Chunk 005) | Builds on |
| Matrix Rank (Chunk 005) | Matrix Inverse (Chunk 005) | Builds on |
| Partitioned Matrices (Chunk 006) | Matrix Inverse (Chunk 005) | Extends |
| Eigenvalues (Chunk 006) | Determinants + Trace (Chunk 005) | Builds on |
| Symmetric/PD Matrices (Chunk 006) | Eigenvalues (Chunk 006) | Builds on |
| Idempotent Matrix (Chunk 006) | Symmetric/PD Matrices + Eigenvalues (Chunk 006) | Builds on |
| Kronecker Product (Chunk 007) | Matrix Multiplication (Chunk 005) | Extends |
| Matrix Differentiation (Chunk 007) | MLE (Chunk 004), Matrix Multiplication (Chunk 005) | Connects |
| Fisher Information (Chunk 007) | Score Function (Chunk 007), PSD Matrices (Chunk 006) | Builds on |
| OLS β̂ = (X'X)⁻¹X'y | Matrix Inverse (Chunk 005), M-matrix (Chunk 006) | Is derived via |
| BLUE (Gauss-Markov) | MVUE (Chunk 003), OLS (Chunk 004) | Connects (Block 2) |

---

## Key Terms Glossary

| Term | Definition | First Appears |
|------|-----------|---------------|
| Econometrics | Application of mathematics and statistics to economic data for testing hypotheses | Chunk 001 |
| Theoretical Econometrics | Branch that develops new statistical methods for economic analysis | Chunk 001 |
| Applied Econometrics | Branch that applies established methods to specific economic questions | Chunk 001 |
| Econometric Model | Mathematical + stochastic model specifying economic relationships; simplification of reality | Chunk 002 |
| Population Regression Function (PRF) | True theoretical relationship in the population; E(Y|X); unknown | Chunk 002 |
| Sample Regression Function (SRF) | Estimated relationship from sample data; used to infer about PRF | Chunk 002 |
| Hypothesis | Assertion about a population property; tested as H₀ vs H₁ | Chunk 002 |
| Null Hypothesis (H₀) | Hypothesis tested for rejection; asserts no relationship or specific value | Chunk 002 |
| Alternative Hypothesis (H₁) | Condition opposite to H₀; accepted/rejected via H₀ | Chunk 002 |
| Stochastic Error (u) | Random disturbance capturing omitted variables, wrong form, sampling error | Chunk 002 |
| Classical Regression Model | Linear regression where u satisfies all classical assumptions | Chunk 002 |
| Data Generation Process (DGP) | True unknown mechanism generating observed data | Chunk 002 |
| Semi-Log Model | lnY = β₀ + β₁X + u; β₁ = growth rate (proportional change in Y) | Chunk 002 |
| Log-Linear (Double-Log) Model | lnY = β₀ + β₁lnX + u; β₁ = elasticity of Y w.r.t. X | Chunk 002 |
| Elasticity | % change in Y per 1% change in X; β₁ in log-linear model | Chunk 002 |
| Intrinsically Linear Model | Non-linear model transformable to linear form (e.g., via logs) | Chunk 002 |
| Point Estimate | Specific numerical value of a statistic estimating a parameter | Chunk 003 |
| Interval Estimate | Range (T₁, T₂) with P(T₁ ≤ θ ≤ T₂) = 1-α; confidence interval | Chunk 003 |
| Estimator | Rule/formula (function of sample) used to compute a parameter estimate | Chunk 003 |
| Estimate | Specific numerical value of an estimator for a particular sample | Chunk 003 |
| Sampling Distribution | Probability distribution of a statistic across many samples of size n | Chunk 003 |
| Unbiased Estimator | E(T) = Ø; targets true parameter on average | Chunk 003 |
| MVUE | Unbiased estimator with smallest variance in its class | Chunk 003 |
| Consistent Estimator | lim P(T→Ø) = 1; bias→0 AND variance→0 as n→∞ | Chunk 003 |
| Efficient Estimator | Minimum variance among all consistent estimators | Chunk 003 |
| Sufficient Estimator | Uses all information in the sample about Ø | Chunk 003 |
| Mean Squared Error (MSE) | MSE(T) = Var(T) + [bias(T)]²; composite measure for biased estimators | Chunk 003 |
| Asymptotic Unbiasedness | lim E(T) = Ø as n→∞ | Chunk 004 |
| Asymptotic Consistency | lim[E(T)-Ø]=0 AND lim Var(T)=0 as n→∞ | Chunk 004 |
| WLLN (Weak LLN) | lim P(\|Aₙ-µ\|<α)=1 for all α>0; convergence in probability | Chunk 004 |
| SLLN (Strong LLN) | lim P(Aₙ=µ)=1; almost sure convergence | Chunk 004 |
| i.i.d. | Independent and identically distributed random variables | Chunk 004 |
| Central Limit Theorem | X̄~N(µ,σ²/n) as n→∞; regardless of population distribution | Chunk 004 |
| Standard Normal Variable (Z) | Z=(X̄-µ)/(σ/√n); approaches N(0,1) as n→∞ | Chunk 004 |
| Simple Hypothesis | Completely specifies all parameters of the population | Chunk 004 |
| Composite Hypothesis | At least one parameter unspecified or in a range | Chunk 004 |
| Type-I Error | Rejecting H₀ when it is actually true; probability = α | Chunk 004 |
| Type-II Error | Not rejecting H₀ when it is actually false | Chunk 004 |
| Level of Significance (α) | Maximum permissible P(Type-I error); usually 1% or 5% | Chunk 004 |
| Confidence Coefficient (1-α) | Probability of correctly not rejecting true H₀ | Chunk 004 |
| Critical Region | Set of test statistic values leading to rejection of H₀ | Chunk 004 |
| p-value | Lowest α at which H₀ can be rejected; reject if p-value < α | Chunk 004 |
| Method of Least Squares (OLS) | Minimises Σeᵢ²; gives normal equations; requires full rank X | Chunk 004 |
| Normal Equations | System of n equations from dS/dxⱼ=0; solved to get OLS estimates | Chunk 004 |
| Maximum Likelihood (MLE) | Maximises logL(θ); consistent, efficient, sufficient, approx normal | Chunk 004 |
| Method of Moments | Equates sample moments to population moments; solves for parameters | Chunk 004 |
| Matrix | Rectangular array of numbers; m×n; element aᵢⱼ | Chunk 005 |
| Identity Matrix (Iₙ) | n×n diagonal matrix with all 1s on diagonal; AA⁻¹=I | Chunk 005 |
| Symmetric Matrix | A = A' (transpose = original) | Chunk 005 |
| Transpose (A') | Swap rows and columns of A; (aᵢⱼ)→(aⱼᵢ) | Chunk 005 |
| Determinant | Scalar; det≠0↔invertible; det=0↔singular; det(AB)=det(A)det(B) | Chunk 005 |
| Singular Matrix | Square matrix with det=0; cannot be inverted | Chunk 005 |
| Non-Singular Matrix | Square matrix with det≠0; invertible | Chunk 005 |
| Orthogonal Matrix | A'A=I; det=±1; preserves lengths and angles | Chunk 005 |
| Trace | tr(A)=Σaᵢᵢ; additive; tr(In)=n; equals sum of eigenvalues | Chunk 005 |
| Matrix Inverse (A⁻¹) | AA⁻¹=A⁻¹A=I; A⁻¹=(1/det(A))adj(A); (AB)⁻¹=B⁻¹A⁻¹ | Chunk 005 |
| Adjoint Matrix | Transpose of cofactor matrix; used in computing inverse | Chunk 005 |
| Cofactor Cᵢⱼ | (-1)^{i+j}×det(Aᵢⱼ); submatrix deletes row i and column j | Chunk 005 |
| Rank | Max linearly independent rows; = pivots in row echelon form | Chunk 005 |
| Row Echelon Form | Matrix form with zero rows at bottom; leading zeros increase each row | Chunk 005 |
| Full Rank | For n×n: rank=n ↔ invertible; for X (n×k): rank=k ↔ OLS valid | Chunk 005 |
| Partitioned Matrix | Matrix divided into submatrices (blocks) | Chunk 006 |
| Block-Diagonal Matrix | Square matrix with zero off-diagonal blocks; direct sum of diagonal blocks | Chunk 006 |
| Direct Sum (A⊕B) | [[A,0],[0,B]]; block-diagonal from A and B | Chunk 006 |
| Eigenvalue (λ) | Scalar: Ax=λx; root of det(A-λI)=0 | Chunk 006 |
| Eigenvector | Non-zero vector x: Ax=λx; "special direction" of transformation | Chunk 006 |
| Characteristic Equation | det(A-λI)=0; nth-degree polynomial in λ | Chunk 006 |
| Diagonalizable Matrix | A=CΛC⁻¹; C=eigenvectors, Λ=eigenvalues; requires n lin.ind. eigenvectors | Chunk 006 |
| Positive Definite (PD) | b'Ab>0 ↔ all λᵢ>0; always invertible | Chunk 006 |
| Positive Semi-Definite (PSD) | b'Ab≥0 ↔ all λᵢ≥0; may be singular | Chunk 006 |
| Cholesky Decomposition | A=LL' for symmetric PSD A; L lower triangular | Chunk 006 |
| QR Factorization | A=QR; Q semi-orthogonal (Q'Q=Iₙ), R upper triangular with positive diagonal | Chunk 006 |
| SVD | A=SΛ^{1/2}T'; S'S=T'T=Iᵣ; Λ diagonal; works for any m×n | Chunk 006 |
| Idempotent Matrix | MM=M; rank(M)=trace(M) | Chunk 006 |
| M-Matrix (Annihilator) | M=I-X(X'X)⁻¹X'; symmetric, idempotent, MX=0, rank=n-k | Chunk 006 |
| Hat Matrix (H) | H=X(X'X)⁻¹X'; symmetric, idempotent, HX=X, rank=k | Chunk 006 |
| Kronecker Product (A⊗B) | Block matrix; each aᵢⱼ replaced by aᵢⱼB; dim=mp×nq | Chunk 007 |
| Vec-Operator | Stacks columns of matrix into column vector; vec(ABC)=(C'⊗A)vec(B) | Chunk 007 |
| Jacobian Matrix | m×n matrix of ∂fᵢ/∂xⱼ for vector function f:Rⁿ→Rᵐ | Chunk 007 |
| Gradient Matrix | n×1 vector [∂f/∂xᵢ]; first derivatives of scalar function | Chunk 007 |
| Hessian Matrix | n×n symmetric matrix of ∂²f/∂xᵢ∂xⱼ; second derivatives | Chunk 007 |
| Score Function S(θ) | ∂logL(θ)/∂θ; gradient of log-likelihood; =0 at MLE | Chunk 007 |
| Fisher Information I(θ) | -E[∂²logL/∂θ∂θ']; PSD; inverse=Cramér-Rao lower bound | Chunk 007 |
| Log-Likelihood Function | logL(θ)=log P(data\|θ); maximised in MLE | Chunk 007 |
