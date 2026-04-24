# Chunk 006 — Unit 3: Partitioned Matrices, Eigenvalues, Special Matrices (Symmetric, PD, QR, SVD, Idempotent)
<!-- Pages: 50–59 -->
<!-- Source: chunk_006.txt -->
<!-- Continues from: Rank of a Matrix (Chunk 005) -->
<!-- Continues into: Kronecker Product, Vec-Operator, Matrix Differentiation, CYP Answers (Chunk 007) -->

## Section: Partitioned Matrices 🟡

### Core Idea
A partitioned matrix is a matrix divided into submatrices (blocks). Partition allows complex matrix operations to be broken into smaller, manageable block operations. In econometrics, partitioned matrices appear in simultaneous equations systems (e.g., Keynesian model: AX = B) and in block-diagonal covariance structures.

> **In Simple Terms:** Partitioning a matrix is like organising a big spreadsheet by dividing it into groups. You can then do operations on each group separately, which is much easier than working with the whole thing at once.

### Key Concepts

#### Block Matrix Structure
Y = [[A, B], [C, D]] where A, B, C, D are submatrices.
Dimension rules:
- A and B have the same number of rows (m)
- C and D have the same number of rows (n)
- A and C have the same number of columns (p)
- B and D have the same number of columns (q)
- Y has dimension (m+n) × (p+q)

#### Block Multiplication
If Y₁ = [[A₁,B₁],[C₁,D₁]] and Y₂ = [[A₂,B₂],[C₂,D₂]] are conformable:
Y₁Y₂ = [[A₁A₂+B₁C₂, A₁B₂+B₁D₂], [C₁A₂+D₁C₂, C₁B₂+D₁D₂]]

#### Direct Sum (A ⊕ B)
A ⊕ B = [[A, 0], [0, B]] — a block-diagonal matrix. A block-diagonal matrix is the direct sum of its blocks.

#### Inversion of Block Diagonal
If A and D are non-singular:
[[A,0],[0,D]]⁻¹ = [[A⁻¹,0],[0,D⁻¹]]

#### Trace of Partitioned Matrix
tr([[A,B],[C,D]]) = tr(A) + tr(D) — only diagonal blocks contribute.

### Definitions
- **Partitioned Matrix**: A matrix divided into submatrices (blocks); allows block-level arithmetic. ⭐ (exam-important)
- **Block-Diagonal Matrix**: A square partitioned matrix where all off-diagonal blocks are zero matrices; equals the direct sum of diagonal blocks.
- **Direct Sum (A ⊕ B)**: [[A,0],[0,B]] — creates a block-diagonal matrix from two matrices A and B.

### Examples
**CYP 1 Q1 — Keynesian Model in Matrix Form**:
Y - C = I + G (national income identity)
-bY + C = a (consumption function)

In matrix notation: [[1,-1],[-b,1]] [[Y],[C]] = [[I+G],[a]]
i.e., AX = B where X = [[Y],[C]]

Solution: X = A⁻¹B = [[Y],[C]] = [[(I+G+a)/(1-b)], [(1+G)b+a)/(1-b)]]

(Using 2×2 inverse formula with det(A) = 1-b)

### Quick Recall
> **Quick Recall:**
> - Partitioned matrix: Y = [[A,B],[C,D]]; Y' = [[A',C'],[B',D']]
> - Block diagonal inverse: [[A,0],[0,D]]⁻¹ = [[A⁻¹,0],[0,D⁻¹]]
> - tr([[A,B],[C,D]]) = tr(A) + tr(D)
> - Direct sum: A ⊕ B = [[A,0],[0,B]]

### Connections
- Builds on: Inverse of a Matrix (Chunk 005)
- Connects to: Block structures in simultaneous equations (Block 4, Unit 16)

---

## Section: Eigenvalues and Eigenvectors 🔴

### Core Idea
For a square matrix A, an eigenvalue λ and eigenvector x satisfy Ax = λx — the matrix "scales" the eigenvector by λ without changing its direction. Eigenvalues and eigenvectors allow a matrix to be diagonalised (A = CΛC⁻¹), which simplifies complex matrix operations. Two key relationships: trace(A) = Σλᵢ and det(A) = Πλᵢ, linking eigenvalues to the trace and determinant.

> **In Simple Terms:** Eigenvectors are the "special directions" of a matrix — they don't change direction when the matrix is applied, they just get scaled by the eigenvalue. Finding these special directions makes matrix computations much simpler.

### Key Concepts

#### Characteristic Equation and Eigenvalues
Eigenvalue equation: **Ax = λx** → **(A - λI)x = 0**
Non-trivial solutions exist when: **det(A - λI) = 0** (characteristic equation)
For an n×n matrix: characteristic equation is an nth-degree polynomial → at most n eigenvalues.

**Worked Example (2×2 matrix B = [[2,5],[2,3]])**:
det(B - λI) = det([[2-λ, 5],[2, 3-λ]]) = (2-λ)(3-λ) - 10
= λ² - 5λ + 6 - 10 = λ² - 5λ - 4 = 0
Factoring: (λ-1)(λ-4) = 0 → eigenvalues: **λ = 1 or λ = 4**

#### Eigenvectors and Eigenspaces
For each eigenvalue λ, the corresponding eigenvectors are found by solving (A - λI)x = 0.
Multiple eigenvectors for the same λ form the **eigenspace** — a subspace closed under scalar multiplication and vector addition.

#### Diagonalisation: A = CΛC⁻¹
If A (n×n) has n linearly independent eigenvectors x₁,...,xₙ:
- C = [x₁,...,xₙ] (matrix of eigenvectors)
- Λ = diag(λ₁,...,λₙ) (diagonal matrix of eigenvalues)
- **AT = TΛ** → **C⁻¹AC = Λ** → **A = CΛC⁻¹**

A is **diagonalizable** if it has n linearly independent eigenvectors.

#### Key Relationships
- **trace(A) = trace(Λ) = Σλᵢ** (sum of eigenvalues = trace)
- **det(A) = det(Λ) = Πλᵢ** (product of eigenvalues = determinant)
- Eigenvalues of A⁻¹ = reciprocals of eigenvalues of A (1/λᵢ)
- Eigenvalues of A² = squares of eigenvalues of A (λᵢ²)
- Eigenvectors of A⁻¹, A², Aᵏ are the **same** as those of A

### Definitions
- **Eigenvalue (λ)**: A scalar satisfying Ax = λx for some non-zero x; root of the characteristic equation det(A - λI) = 0. ⭐ (exam-important)
- **Eigenvector**: A non-zero vector x such that Ax = λx for some eigenvalue λ. ⭐ (exam-important)
- **Characteristic Equation**: det(A - λI) = 0; an nth-degree polynomial whose roots are the eigenvalues of A. ⭐ (exam-important)
- **Eigenspace**: The set of all eigenvectors corresponding to a particular eigenvalue λ, plus the zero vector; forms a subspace.
- **Diagonalizable Matrix**: A matrix A that can be written as A = CΛC⁻¹ where C is a matrix of eigenvectors and Λ is diagonal; possible if A has n linearly independent eigenvectors.

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking all matrices are diagonalizable → ✅ Correct: Only matrices with n linearly independent eigenvectors are diagonalizable
- ❌ Mistake: Computing eigenvalues of A² separately → ✅ Correct: Eigenvalues of A² = (eigenvalues of A)², eigenvectors are the same

### Quick Recall
> **Quick Recall:**
> - Eigenvalue equation: (A - λI)x = 0 → det(A - λI) = 0 → characteristic equation
> - trace(A) = Σλᵢ; det(A) = Πλᵢ ⭐
> - A = CΛC⁻¹ (diagonalisation) → simplifies Aᵏ = CΛᵏC⁻¹
> - A⁻¹ has eigenvalues 1/λᵢ with the same eigenvectors

### Connections
- Builds on: Determinants and Trace (Chunk 005)
- Is prerequisite for: Symmetric matrices (below), Idempotent matrices (below)
- Connects to: Variance-covariance matrices (positive definite) in OLS

---

## Section: Special Matrices — Symmetric, Positive Definite, PSD 🔴

### Core Idea
For symmetric matrices, all eigenvalues are real and eigenvectors corresponding to distinct eigenvalues are orthogonal. This enables orthogonal diagonalisation (C'AC = Λ where C is orthogonal). A positive definite (PD) matrix has all eigenvalues strictly positive, guaranteeing invertibility. A positive semi-definite (PSD) matrix has all eigenvalues ≥ 0. PD matrices appear in variance-covariance matrices, ensuring valid statistical inference.

> **In Simple Terms:** Symmetric matrices are "nice" — their eigenvectors always point at right angles to each other. Positive definite means all eigenvalues are positive — like checking all springs in a machine are under tension. If any spring has zero or negative tension, the system may be unstable (or non-invertible).

### Key Concepts

#### Symmetric Matrices and Orthogonal Diagonalization
For symmetric A: eigenvectors for distinct eigenvalues are **orthogonal** (C₂'C₁ = 0).
This means symmetric A is **orthogonally diagonalizable**:
**C'AC = Λ** where C is an orthogonal matrix (C'C = I) and Λ = diag(eigenvalues)
Equivalently: **A = CΛC'**

Key consequences:
- rank(A) = rank(Λ) = number of non-zero eigenvalues of A
- det(A) = Πλᵢ; trace(A) = Σλᵢ for symmetric A (same as general case)
- Rank is preserved under non-singular and orthogonal transformations

#### Positive Definite (PD) Matrix
A symmetric matrix A is **positive definite** if **b'Ab > 0** for all vectors b ≠ 0.

Equivalent condition: A is PD ↔ **all eigenvalues are strictly positive (λᵢ > 0)**.
- PD matrices are always non-singular (invertible).
- Variance-covariance matrices are positive definite.

#### Positive Semi-Definite (PSD) Matrix
A symmetric matrix A is **positive semi-definite** if **b'Ab ≥ 0** for all b ≠ 0.

Equivalent condition: A is PSD ↔ **all eigenvalues are non-negative (λᵢ ≥ 0)**.
- PSD matrices may be singular.

| Property | Condition | Eigenvalues | Invertible? |
|----------|-----------|-------------|------------|
| Positive Definite (PD) | b'Ab > 0 | All λᵢ > 0 | Yes |
| Positive Semi-Definite (PSD) | b'Ab ≥ 0 | All λᵢ ≥ 0 | Maybe |

#### Matrix Square Root and Cholesky Decomposition
For symmetric PD matrix A: A^{1/2} exists where (A^{1/2})(A^{1/2}) = A
By orthogonal diagonalisation: **A^{-1/2} = CΛ^{-1/2}C'** and **A^{1/2} = CΛ^{1/2}C'**
Square root of PSD matrix can be found using **Cholesky Decomposition**: A = LL' where L is lower triangular.

Given two symmetric PD matrices A and B: if A-B is PSD, then B⁻¹ - A⁻¹ is also PSD.

### Definitions
- **Symmetric Matrix**: A = A'; all eigenvalues are real; eigenvectors for distinct eigenvalues are orthogonal. ⭐ (exam-important)
- **Positive Definite (PD) Matrix**: Symmetric matrix where b'Ab > 0 for all b ≠ 0; all eigenvalues strictly positive; always invertible. ⭐ (exam-important)
- **Positive Semi-Definite (PSD) Matrix**: Symmetric matrix where b'Ab ≥ 0 for all b ≠ 0; all eigenvalues non-negative; may be singular. ⭐ (exam-important)
- **Cholesky Decomposition**: Factorisation of a symmetric PSD matrix as A = LL' where L is lower triangular; used to compute matrix square roots.
- **Matrix Square Root (A^{1/2})**: Matrix such that A^{1/2} × A^{1/2} = A; exists for symmetric PSD matrices.

### Quick Recall
> **Quick Recall:**
> - Symmetric: real eigenvalues; orthogonal eigenvectors for distinct λ; C'AC = Λ, A = CΛC'
> - PD: b'Ab > 0 ↔ all λᵢ > 0 → always invertible ⭐
> - PSD: b'Ab ≥ 0 ↔ all λᵢ ≥ 0 → may be singular
> - Variance-covariance matrix is always PD (in regular cases)

### Connections
- Builds on: Eigenvalues (above), Orthogonal matrices (Chunk 005)
- Is prerequisite for: Idempotent matrix (below), Fisher Information Matrix (Chunk 007)
- Connects to: Gauss-Markov theorem — variance of OLS estimator involves PD matrix (Block 2)

---

## Section: QR Factorization 🟡

### Core Idea
QR factorisation decomposes a real m×n matrix A (of rank n) into A = QR, where Q is a semi-orthogonal matrix (Q'Q = Iₙ) and R is a n×n upper triangular matrix with positive diagonal elements. The columns q₁, q₂,...,qₙ of Q form an orthonormal basis obtained by the Gram-Schmidt process.

> **In Simple Terms:** QR breaks a matrix into a "rotation part" (Q) and a "scaling/triangular part" (R). This decomposition is used in numerical computing to solve least squares problems stably.

### Key Concepts

#### QR Decomposition: A = QR
- A: real m×n matrix with rank n (n ≤ m)
- Q: m×n semi-orthogonal matrix (Q'Q = Iₙ, note: NOT QQ' = I unless m=n)
- R: n×n upper triangular matrix with positive diagonal elements
- Columns of Q: q₁,...,qₙ computed by **Gram-Schmidt orthogonalisation** of columns of A

### Definitions
- **Semi-Orthogonal Matrix (Q)**: A real matrix satisfying Q'Q = Iₙ; columns form an orthonormal set.
- **Upper Triangular Matrix (R)**: Matrix where all elements below the main diagonal are zero.
- **Gram-Schmidt Process**: An algorithm to produce an orthonormal set of vectors from a set of linearly independent vectors.

### Quick Recall
> **Quick Recall:**
> - QR: A = QR where Q'Q = Iₙ (semi-orthogonal) and R upper triangular
> - Gram-Schmidt orthogonalisation produces the columns of Q
> - Used for numerical stability in OLS computation

### Connections
- Builds on: Orthogonal matrices (Chunk 005), Rank (Chunk 005)
- Connects to: Numerically stable OLS computation (Block 2)

---

## Section: Singular Value Decomposition (SVD) 🟡

### Core Idea
SVD generalises eigendecomposition to non-square matrices. Any real m×n matrix A of rank r can be written as A = SΛ^{1/2}T', where S and T are orthogonal matrices of left/right singular vectors and Λ is diagonal with positive elements (squared singular values). SVD is used for computing Moore-Penrose pseudoinverses and dimensionality reduction.

> **In Simple Terms:** SVD is like eigendecomposition, but it works for any matrix — even rectangular ones. It reveals the fundamental "shapes" of a transformation.

### Key Concepts
#### SVD: A = SΛ^{1/2}T'
- A: real m×n matrix with rank r > 0
- S: m×r matrix with S'S = Iᵣ (left singular vectors)
- T: n×r matrix with T'T = Iᵣ (right singular vectors)
- Λ: r×r diagonal matrix with positive diagonal elements (eigenvalues of AA')
- Finding S and T: AA'S = SΛ; T = A'SΛ^{-1/2}

### Definitions
- **Singular Value Decomposition (SVD)**: Factorisation A = SΛ^{1/2}T' for any m×n matrix; S and T are orthogonal, Λ diagonal with singular values.
- **Singular Values**: Square roots of eigenvalues of AA'; represent "scaling factors" in the SVD.

### Quick Recall
> **Quick Recall:**
> - SVD: A = SΛ^{1/2}T'; works for any m×n matrix (unlike eigendecomposition)
> - S'S = Iᵣ, T'T = Iᵣ; Λ = diag(singular values squared)

### Connections
- Builds on: Eigenvalues (above), Symmetric PD matrices (above)
- Connects to: Ridge regression, principal component analysis (advanced topics, MECE 102)

---

## Section: Idempotent Matrix 🔴

### Core Idea
A matrix M is idempotent if MM = M. Idempotent matrices appear naturally in OLS: the hat matrix H = X(X'X)⁻¹X' and the annihilator matrix M = I - H = I - X(X'X)⁻¹X' are both idempotent. The rank of an idempotent matrix equals its trace. M satisfies MX = 0, meaning it projects residuals orthogonal to the column space of X.

> **In Simple Terms:** An idempotent matrix "does it once and stays done." Applying it a second time gives the same result: MM = M. In regression, M projects the data onto the residual space — applying it twice is the same as applying it once.

### Key Concepts

#### Definition: MM = M
A matrix M is idempotent if and only if **M² = M**.

#### Key Property: rank(M) = trace(M)
For idempotent matrix M:
**rank(M) = trace(M)** ⭐ (unique to idempotent matrices!)

#### The M-Matrix (Annihilator) and H-Matrix (Hat)
**Hat matrix**: H = X(X'X)⁻¹X'
**Annihilator matrix**: M = Iₙ - X(X'X)⁻¹X' = I - H

CYP 2 Q2 proves these properties for M:

**Symmetry of M** (M = M'):
Since X(X'X)⁻¹X' is symmetric, M = I - X(X'X)⁻¹X' is also symmetric.

**Idempotency of M** (MM = M):
MM = (I - X(X'X)⁻¹X')(I - X(X'X)⁻¹X')
= I - X(X'X)⁻¹X' - X(X'X)⁻¹X' + X(X'X)⁻¹X'X(X'X)⁻¹X'
= I - X(X'X)⁻¹X' - X(X'X)⁻¹X' + X(X'X)⁻¹X'  [since X'X(X'X)⁻¹ = I]
= I - X(X'X)⁻¹X' = M ✓

**MX = 0** (M annihilates X):
MX = (I - X(X'X)⁻¹X')X = X - X(X'X)⁻¹X'X = X - X = **0** ✓

**Rank of M**:
rank(M) = trace(M) = tr(I - X(X'X)⁻¹X') = tr(Iₙ) - tr(X(X'X)⁻¹X')
= n - tr(X'X(X'X)⁻¹) = n - tr(Iₖ) = **n - k** ✓

(where k = number of parameters estimated)

### Definitions
- **Idempotent Matrix**: A matrix M where M² = MM = M. ⭐ (exam-important)
- **Annihilator Matrix (M)**: M = Iₙ - X(X'X)⁻¹X'; idempotent and symmetric; projects onto orthogonal complement of column space of X; MX = 0. ⭐ (exam-important)
- **Hat Matrix (H)**: H = X(X'X)⁻¹X'; idempotent and symmetric; projects Y onto fitted values Ŷ = HY. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking rank(M) = n for the M-matrix → ✅ Correct: rank(M) = n - k (n observations minus k parameters)
- ❌ Mistake: Forgetting that rank(idempotent) = trace(idempotent) → ✅ Correct: This is the defining trick for idempotent matrices

### Quick Recall
> **Quick Recall:**
> - Idempotent: MM = M ⭐
> - rank(M) = trace(M) for idempotent M ⭐
> - M = I - X(X'X)⁻¹X': symmetric, idempotent, MX = 0, rank = n-k
> - H = X(X'X)⁻¹X': symmetric, idempotent, HX = X, rank = k

### Connections
- Builds on: Matrix inverse (Chunk 005), Symmetric matrices (above)
- Is prerequisite for: OLS residuals ê = MY (Block 2), Degrees of freedom in regression
- Continues into: CYP 2 Q2(b) proof of MX=0, Q2(c) rank computation (Chunk 007)
