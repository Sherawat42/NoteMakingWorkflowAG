# Running Context
**Source**: Block-1 mece101.pdf | **Updated through**: Chunk 007 (All chunks complete)

## Key Concepts Introduced

### Unit 1 — Introduction to Econometrics (Chunks 001–003)
- **Econometrics** (Chunk 001): Application of mathematics and statistics to economic data to test hypotheses and estimate relationships
- **Theoretical vs Applied Econometrics** (Chunk 001): Theoretical develops methods; Applied uses them on real data
- **MECE 101 Block Structure** (Chunk 001): 4 Blocks, 16 Units
- **Econometric Model** (Chunk 002): Mathematical + stochastic model of an economic relationship; simplification of reality
- **PRF vs SRF** (Chunk 002): PRF = unknown population truth; SRF = sample estimate of PRF
- **6 Steps in Econometric Study** (Chunk 002): Hypothesis → Model → Data → Estimation → Testing → Interpretation
- **Deterministic vs Stochastic relationship** (Chunk 002): Deterministic has no error term; stochastic adds random error u
- **Error Term (u)** (Chunk 002): Captures omitted variables, wrong functional form, sampling error
- **DGP** (Chunk 002): Hidden real-world data-generating mechanism; approximated by econometric models
- **General-to-Specific vs Specific-to-General** (Chunk 002): Preferred approach starts with large model and trims irrelevant variables
- **Functional Forms** (Chunk 002): Linear (absolute Δ), Semi-Log (% change / growth rate), Log-Linear (elasticity)
- **Econometric Software** (Chunk 003): R (free/open-source), STATA/E-Views/SPSS (licensed), Gretl/EasyReg (freeware)

### Unit 2 — Statistical Concepts (Chunks 003–005)
- **Statistical Inference** (Chunk 003): Drawing population conclusions from sample data
- **Point Estimation** (Chunk 003): Single numerical estimate of a parameter; estimator (rule) vs estimate (value)
- **Interval Estimation** (Chunk 003): Range (T₁, T₂) containing parameter with prob 1-α (confidence interval)
- **Sampling Distribution** (Chunk 003): Distribution of a statistic across many samples of size n
- **4 Properties of Good Estimator** (Chunk 003): Unbiasedness, Consistency, Efficiency, Sufficiency
- **MVUE** (Chunk 003): Minimum Variance Unbiased Estimator — unbiased + smallest variance
- **MSE** (Chunk 003): Mean Squared Error = Var(T) + [bias(T)]²; composite measure for biased estimators
- **Asymptotic Unbiasedness** (Chunk 004): bias→0 as n→∞
- **Asymptotic Consistency** (Chunk 004): Both bias→0 AND variance→0 as n→∞
- **WLLN** (Chunk 004): P(|Aₙ-µ|<α)→1 as n→∞ (convergence in probability)
- **SLLN** (Chunk 004): P(Aₙ=µ)=1 as n→∞ (almost sure convergence; stronger)
- **CLT** (Chunk 004): X̄~N(µ,σ²/n) as n→∞ regardless of population distribution
- **Hypothesis Testing** (Chunk 004): H₀/H₁, Type-I (reject true H₀), Type-II (accept false H₀), α, p-value
- **3 Estimation Methods** (Chunk 004): OLS (min Σeᵢ²), MLE (max logL), Method of Moments (match sample moments)

### Unit 3 — Matrix Algebra (Chunks 005–007)
- **Matrix notation** (Chunk 005): m×n matrix A; aᵢⱼ; special types: diagonal, identity, symmetric, triangular
- **Matrix multiplication** (Chunk 005): AB requires cols(A)=rows(B); result is m×q; (AB)'=B'A'; NOT commutative
- **Determinant** (Chunk 005): det(A)≠0 → invertible; det(A)=0 → singular; det(AB)=det(A)det(B)
- **Orthogonal matrix** (Chunk 005): A'A=I; det=±1; preserves lengths and angles
- **Trace** (Chunk 005): tr(A)=Σaᵢᵢ; additive; tr(AB)=tr(BA)
- **Matrix inverse** (Chunk 005): A⁻¹=(1/det(A))adj(A); (AB)⁻¹=B⁻¹A⁻¹; requires det≠0
- **Matrix rank** (Chunk 005): Max linearly independent rows; full rank ↔ invertible; rank=pivots in echelon form
- **Partitioned matrix** (Chunk 006): Block matrix; [[A,0],[0,D]]⁻¹=[[A⁻¹,0],[0,D⁻¹]]
- **Eigenvalues & Eigenvectors** (Chunk 006): Ax=λx; det(A-λI)=0; trace=Σλᵢ; det=Πλᵢ; A=CΛC⁻¹
- **Symmetric matrices** (Chunk 006): All eigenvalues real; orthogonal eigenvectors; C'AC=Λ; A=CΛC'
- **Positive Definite** (Chunk 006): b'Ab>0 ↔ all λᵢ>0; always invertible
- **Positive Semi-Definite** (Chunk 006): b'Ab≥0 ↔ all λᵢ≥0; may be singular
- **QR Factorization** (Chunk 006): A=QR; Q semi-orthogonal, R upper triangular; Gram-Schmidt
- **SVD** (Chunk 006): A=SΛ^{1/2}T'; works for any m×n matrix; S'S=T'T=Iᵣ
- **Idempotent matrix** (Chunk 006): MM=M; rank(M)=trace(M); M=I-X(X'X)⁻¹X'; MX=0; rank=n-k
- **Kronecker product** (Chunk 007): A⊗B replaces each aᵢⱼ with aᵢⱼB; dim=mp×nq
- **Vec-operator** (Chunk 007): Stacks columns of matrix into column vector; vec(ABC)=(C'⊗A)vec(B)
- **Jacobian** (Chunk 007): Matrix of ∂fᵢ/∂xⱼ for vector functions
- **Gradient / Score** (Chunk 007): Vector of ∂f/∂xᵢ; score=∂logL/∂θ=0 at MLE
- **Hessian** (Chunk 007): Matrix of ∂²f/∂xᵢ∂xⱼ; symmetric
- **Fisher Information** (Chunk 007): I(θ)=-E[Hessian(logL)]; positive semi-definite; inverse=Cramér-Rao bound

## Definitions (⭐ exam-important)
- **Econometrics** (Chunk 001): Application of mathematical statistics to economic data to test hypotheses ⭐
- **Econometric Model** (Chunk 002): Statistical model specifying economic relationships; estimated with real data ⭐
- **PRF** (Chunk 002): Theoretical population relationship; E(Y|X)=β₀+β₁X ⭐
- **Hypothesis** (Chunk 002): Assertion about a population property; tested as H₀ vs H₁ ⭐
- **Stochastic Error (u)** (Chunk 002): Random disturbance; captures omitted variables + specification error ⭐
- **Classical Regression Model** (Chunk 002): Linear regression where u fulfils classical assumptions ⭐
- **DGP** (Chunk 002): True unknown mechanism generating observed data ⭐
- **Semi-Log Model** (Chunk 002): lnY=β₀+β₁X+u; β₁=proportional rate of change in Y (growth rate) ⭐
- **Log-Linear Model** (Chunk 002): lnY=β₀+β₁lnX+u; β₁=elasticity of Y w.r.t. X ⭐
- **Elasticity** (Chunk 002): %ΔY per 1%ΔX; β₁ in log-linear model ⭐
- **Point Estimate** (Chunk 003): Specific value of statistic estimating a parameter ⭐
- **Confidence Interval** (Chunk 003): Range (T₁,T₂) with P(T₁≤θ≤T₂)=1-α ⭐
- **Unbiased Estimator** (Chunk 003): E(T)=Ø; targets true parameter on average ⭐
- **MVUE** (Chunk 003): Unbiased estimator with smallest variance ⭐
- **Consistent Estimator** (Chunk 003): T→Ø as n→∞ (bias→0 AND variance→0) ⭐
- **Efficient Estimator** (Chunk 003): Minimum variance among all consistent estimators ⭐
- **Sufficient Estimator** (Chunk 003): Uses all sample information about Ø ⭐
- **Asymptotic Unbiasedness** (Chunk 004): lim E(T)=Ø as n→∞ ⭐
- **Asymptotic Consistency** (Chunk 004): lim[E(T)-Ø]=0 AND lim Var(T)=0 ⭐
- **WLLN** (Chunk 004): P(|Aₙ-µ|<α)→1 as n→∞; convergence in probability ⭐
- **SLLN** (Chunk 004): P(Aₙ=µ)=1 as n→∞; almost sure convergence ⭐
- **CLT** (Chunk 004): X̄~N(µ,σ²/n) as n→∞; basis for large-sample inference ⭐
- **H₀ / H₁** (Chunk 004): Null and alternative hypothesis ⭐
- **Type-I Error** (Chunk 004): Rejecting true H₀; prob=α ⭐
- **Type-II Error** (Chunk 004): Not rejecting false H₀ ⭐
- **Level of Significance (α)** (Chunk 004): Max allowed P(Type-I error) ⭐
- **p-value** (Chunk 004): Lowest α at which H₀ can be rejected ⭐
- **OLS / Method of Least Squares** (Chunk 004): Min Σeᵢ² → normal equations ⭐
- **MLE** (Chunk 004): Max logL(θ); consistent, efficient, sufficient, approx normal ⭐
- **Identity Matrix (Iₙ)** (Chunk 005): Diagonal matrix with all 1s; AA⁻¹=I ⭐
- **Symmetric Matrix** (Chunk 005): A=A' ⭐
- **Conformable Matrices** (Chunk 005): cols(A)=rows(B) for AB to be defined ⭐
- **Determinant** (Chunk 005): det≠0→invertible; det=0→singular ⭐
- **Orthogonal Matrix** (Chunk 005): A'A=I; det=±1 ⭐
- **Trace** (Chunk 005): tr(A)=Σaᵢᵢ ⭐
- **Matrix Inverse (A⁻¹)** (Chunk 005): AA⁻¹=I; A⁻¹=(1/det)adj(A); (AB)⁻¹=B⁻¹A⁻¹ ⭐
- **Rank** (Chunk 005): Max linearly independent rows; full rank↔invertible ⭐
- **Eigenvalue (λ)** (Chunk 006): Ax=λx; det(A-λI)=0 ⭐
- **Eigenvector** (Chunk 006): Non-zero x satisfying Ax=λx ⭐
- **Positive Definite** (Chunk 006): b'Ab>0 ↔ all λ>0 ⭐
- **Idempotent Matrix** (Chunk 006): MM=M; rank=trace ⭐
- **M-Matrix (Annihilator)** (Chunk 006): M=I-X(X'X)⁻¹X'; MX=0; rank=n-k ⭐
- **Hat Matrix (H)** (Chunk 006): H=X(X'X)⁻¹X'; projects Y onto Ŷ ⭐
- **Kronecker Product (A⊗B)** (Chunk 007): Replaces aᵢⱼ with aᵢⱼB; dim=mp×nq ⭐
- **Vec-Operator** (Chunk 007): Stacks columns; vec(ABC)=(C'⊗A)vec(B) ⭐
- **Score Function S(θ)** (Chunk 007): ∂logL/∂θ; =0 at MLE ⭐
- **Fisher Information I(θ)** (Chunk 007): -E[Hessian(logL)]; PSD; inverse=Cramér-Rao ⭐

## Named Models / Laws / Theories
- **Classical Regression Model** (Chunk 002): Yᵢ=β₀+β₁Xᵢ+uᵢ (two-var); Y=Xβ+u (matrix); OLS estimable when u satisfies classical assumptions
- **Semi-Log Model** (Chunk 002): lnYt=β₀+β₁t+u_t; β₁=growth rate
- **Log-Linear (Double-Log) Model** (Chunk 002): lnYᵢ=β₀+β₁lnXᵢ+uᵢ; β₁=elasticity
- **Keynesian Consumption Model** (Chunk 002/006): AX=B; partitioned matrix form
- **Weak Law of Large Numbers (WLLN)** (Chunk 004): lim P(|Aₙ-µ|<α)=1
- **Strong Law of Large Numbers (SLLN)** (Chunk 004): lim P(Aₙ=µ)=1 (almost sure)
- **Central Limit Theorem (CLT)** (Chunk 004): X̄~N(µ,σ²/n) as n→∞
- **Gauss-Markov Theorem** (mentioned, Chunks 003/006): OLS is BLUE — requires Block 2
- **QR Factorization** (Chunk 006): A=QR; Q semi-orthogonal, R upper triangular
- **Singular Value Decomposition (SVD)** (Chunk 006): A=SΛ^{1/2}T'
- **Cholesky Decomposition** (Chunk 006): A=LL' for symmetric PSD matrix

## Key Data & Numbers
- **16 Units** across 4 Blocks in MECE 101 (Chunk 001)
- **6 Steps** in econometric study (Chunk 002)
- **3 Sources of error term** (Chunk 002): Omitted variables, wrong functional form, sampling error
- **3 Estimation methods** (Chunk 002): OLS, MLE, Method of Moments
- **4 Properties of good estimator** (Chunk 003): Unbiasedness, Consistency, Efficiency, Sufficiency
- **Coin-toss example**: n=30, heads=13, x̄=0.43, Z≈-0.77, fail to reject H₀ (unbiased coin) (Chunk 004)
- **Fisher Information for N(µ,σ²)**: I(θ)=diag(n/σ², n/(2σ⁴)) — positive definite (Chunk 007)
- **M-matrix rank = n-k**: degrees of freedom in OLS regression (Chunk 006)
