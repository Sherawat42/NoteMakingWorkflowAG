# Chunk 007 — Unit 3: Kronecker Product, Vec-Operator, Matrix Differentiation & CYP Answers
<!-- Pages: 60–67 -->
<!-- Source: chunk_007.txt -->
<!-- Continues from: Idempotent Matrix / SVD (Chunk 006) -->
<!-- Continues into: N/A (final chunk) -->

## Section: Kronecker Product & Vec-Operator 🟡

### Core Idea
The Kronecker product (A ⊗ B) and the vec-operator together form a powerful framework for vectorising matrix equations. The key identity vec(ABC) = (C' ⊗ A)vec(B) allows complex matrix derivatives to be expressed as standard linear operations. These tools appear in multivariate regression, GLS, and SUR models.

> **In Simple Terms:** The Kronecker product creates a "big matrix" by replacing each element of A with that element times the whole matrix B. The vec-operator stacks the columns of a matrix into one long vector. Together, they let you write complicated matrix equations as standard matrix multiplications.

### Key Concepts

#### Kronecker Product (A ⊗ B)
For matrix A (m×n) and B (p×q), the Kronecker product A ⊗ B is the mp × nq block matrix:

A ⊗ B = [[a₁₁B, a₁₂B, ..., a₁ₙB],
          [a₂₁B, a₂₂B, ..., a₂ₙB],
          [...                    ],
          [aₘ₁B, aₘ₂B, ..., aₘₙB]]

In other words, each element aᵢⱼ of A is replaced by the block aᵢⱼB.

#### Vec-Operator (Vectorisation)
For a matrix A with columns a₁, a₂, ..., aₙ:
**vec(A) = [a₁', a₂', ..., aₙ']'** — stacks columns of A into a single column vector.

**Key identity** (from CYP 3 Q1 proof):
**vec(ab') = b ⊗ a** for vectors a and b.
More generally: **vec(ABC) = (C' ⊗ A) vec(B)** ⭐

**Proof sketch from source**:
Let B = Σ bᵢeᵢ' (B expressed as sum of outer products).
Then vec(ABC) = Σ vec(Abᵢeᵢ'C)
Since vec(ab') = b ⊗ a:
vec(ABCᵢ) = (C'eᵢ) ⊗ (Abᵢ) = (C' ⊗ A)(eᵢ ⊗ bᵢ) = (C' ⊗ A)vec(bᵢeᵢ')
Therefore: vec(ABC) = (C' ⊗ A) vec(B) ✓

### Definitions
- **Kronecker Product (A ⊗ B)**: Block matrix where each element aᵢⱼ of A is replaced by the submatrix aᵢⱼB; dimension: (mp) × (nq). ⭐ (exam-important)
- **Vec-Operator**: An operator that stacks the columns of a matrix into a single column vector; vec(A) = [a₁', a₂', ..., aₙ']'. ⭐ (exam-important)

### Mechanisms / Processes
**Key vec identity**: vec(ABC) = (C' ⊗ A) vec(B)
Special cases:
- vec(AB) = (B' ⊗ I) vec(A) = (I ⊗ A) vec(B)
- vec(ab') = b ⊗ a for column vectors a and b

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing A ⊗ B with B ⊗ A → ✅ Correct: Kronecker product is NOT commutative; A ⊗ B ≠ B ⊗ A in general

### Quick Recall
> **Quick Recall:**
> - Kronecker: A ⊗ B replaces each aᵢⱼ with the block aᵢⱼB; dimension mp×nq
> - vec(A): stacks columns of A into one column vector
> - **vec(ABC) = (C' ⊗ A) vec(B)** ⭐ — the key identity
> - vec(ab') = b ⊗ a

### Connections
- Builds on: Matrix multiplication (Chunk 005)
- Connects to: SUR (Seemingly Unrelated Regressions) and GLS (advanced topics)

---

## Section: Matrix Differentiation — Jacobian, Gradient & Hessian 🔴

### Core Idea
Matrix differentiation extends scalar calculus to matrices. Three key matrices arise: (1) the Jacobian — derivative of a vector function w.r.t. a vector; (2) the Gradient — first derivatives of a scalar function (used as score function in MLE); (3) the Hessian — second derivatives of a scalar function (used to verify maxima in MLE). The Fisher Information Matrix I(θ) is the expected negative Hessian of the log-likelihood, quantifying the information about θ in the data.

> **In Simple Terms:** When a function takes a vector input and gives a scalar output (like log-likelihood), the Gradient tells you which direction is "uphill" (how to increase the function), and the Hessian tells you the curvature (whether you're at a peak or a saddle point). The Fisher Information tells you how precisely you can estimate θ.

### Key Concepts

#### Jacobian Matrix
For a function **f: Rⁿ → Rᵐ** (vector → vector):
The Jacobian J is an m×n matrix of first-order partial derivatives:
Jᵢⱼ = ∂fᵢ/∂xⱼ

The Jacobian generalises the derivative to vector-valued functions.

#### Gradient Matrix (Score Function in MLE)
For a scalar function f: Rⁿ → R (vector → scalar):
The **gradient** is the n×1 vector of first-order partial derivatives:
∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]'

In MLE, the **score function** S(θ) = ∂logL(θ)/∂θ is the gradient of the log-likelihood.

**Worked Example from source** (MLE for Normal distribution — CYP 3 Q2):
Given x₁,...,xₙ i.i.d. from N(µ, σ²), parameter θ = (µ, σ²):

Log-likelihood: logL(θ) = -(n/2)lnσ² - (1/2σ²)Σ(xᵢ - µ)²

Score function S(θ) = ∂logL(θ)/∂θ = [∂lnL/∂µ, ∂lnL/∂σ²]'
= [n/σ²(x̄ - µ), -n/(2σ²) + Σ(xᵢ-µ)²/(2σ⁴)]'

#### Real Hessian Matrix
For scalar function f: Rⁿ → R, the **Hessian** is the n×n matrix of second-order partial derivatives:
Hᵢⱼ = ∂²f/(∂xᵢ∂xⱼ)

The Hessian is symmetric (if f has continuous second-order derivatives).
In MLE: **H = ∂²logL/∂θ∂θ'** — the negative Hessian gives the observed Fisher Information.

#### Fisher Information Matrix I(θ)
**Observed Fisher Information**: I(θ) = -∂²logL/∂θ∂θ'

**Expected Fisher Information**: I(θ) = E_θ[-∂²logL/∂θ∂θ'] = E_θ[S(θ)S(θ)']

The information matrix is a 2×2 variance matrix (for 2-parameter models) and is **positive semi-definite**.

**Worked Example (Fisher Information for Normal)**:
I(θ) = -H = [[n/σ², n/σ⁴(x̄-µ)], [n/σ⁴(x̄-µ), -n/(2σ⁴) + Σ(xᵢ-µ)²/(σ²)³]]

Expected Fisher Information (with E[Σ(xᵢ-µ)²] = nσ²):
I(θ) = [[n/σ², 0], [0, n/(2σ⁴)]]

det(I(θ)) = n²/(2σ⁶) > 0 (since n > 0, σ² > 0) → I(θ) is positive definite.

### Definitions
- **Jacobian Matrix**: m×n matrix of first-order partial derivatives of a vector function **f**: Rⁿ → Rᵐ; Jᵢⱼ = ∂fᵢ/∂xⱼ. ⭐ (exam-important)
- **Gradient Matrix**: The gradient ∇f = [∂f/∂xᵢ]ᵀ; n×1 vector of first-order partial derivatives of a scalar function f. ⭐ (exam-important)
- **Hessian Matrix**: n×n symmetric matrix of second-order partial derivatives of f: Hᵢⱼ = ∂²f/(∂xᵢ∂xⱼ). ⭐ (exam-important)
- **Score Function S(θ)**: The gradient of the log-likelihood: S(θ) = ∂logL(θ)/∂θ; equals zero at the MLE estimate. ⭐ (exam-important)
- **Fisher Information Matrix I(θ)**: I(θ) = -E[∂²logL/∂θ∂θ']; a positive semi-definite matrix quantifying the information about θ in the data. ⭐ (exam-important)
- **Log-Likelihood Function**: logL(θ) = log P(data|θ); maximised in MLE to find θ̂.

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing observed and expected Fisher information → ✅ Correct: Observed I(θ) = -Hessian(logL); Expected I(θ) = E_θ[observed I(θ)]
- ❌ Mistake: Thinking the Hessian is the gradient → ✅ Correct: Gradient = first derivatives (n×1 vector); Hessian = second derivatives (n×n matrix)
- ❌ Mistake: Assuming score function is non-zero at MLE → ✅ Correct: At MLE, S(θ̂) = 0 (gradient = 0 at maximum)

### Quick Recall
> **Quick Recall:**
> - Jacobian: ∂f/∂x (vector-to-vector); Gradient: ∂f/∂x (scalar-to-vector) ⭐
> - Hessian: ∂²f/∂x∂x' (n×n, symmetric) ⭐
> - Score: S(θ) = ∂logL/∂θ = 0 at MLE
> - Fisher Information: I(θ) = -E[Hessian(logL)]; positive semi-definite ⭐
> - For Normal N(µ,σ²): I(θ) = diag(n/σ², n/2σ⁴)

### Connections
- Builds on: Matrix multiplication (Chunk 005), MLE (Chunk 004)
- Connects to: Cramér-Rao lower bound (the inverse of Fisher Information gives the minimum variance of any unbiased estimator)
- Connects to: Block 2 — OLS score equations are normal equations

---

## Section: Unit 3 CYP Answers 🟡
<!-- See Chunk 005-006 for content these answers verify -->

### Core Idea
The CYP answers for Unit 3 provide worked solutions for all three Check Your Progress exercises. CYP 1 tests matrix inverse and rank; CYP 2 tests eigenvector diagonalisation and M-matrix properties; CYP 3 tests the vec identity and Fisher Information matrix derivation.

> **In Simple Terms:** These are the answer keys for Unit 3 — use them to verify your matrix algebra and MLE derivations before the exam.

### Key Concepts

#### CYP 1 Answers — Inverse and Rank

**Q1: Inverse of A = [[2,4,1],[4,3,7],[2,1,3]]**
- det(A) = 10 (cofactor expansion along row 2: 4(-11) + 3(4) + 7(6) = -44+12+42 = 10)
- Cofactor matrix: [[2,2,-2],[-11,4,6],[25,-10,-10]]
- adj(A) = (cofactor)ᵀ = [[2,-11,25],[2,4,-10],[-2,6,-10]]
- A⁻¹ = (1/10) × adj(A)

**Q2: Rank of B = [[3,0,2,2],[-6,42,24,54],[21,-21,0,-15]]**
- R₂ → R₂ + 2R₁: [[3,0,2,2],[0,42,28,58],[21,-21,0,-15]]
- R₃ → R₃ - 7R₁: [[3,0,2,2],[0,42,28,58],[0,-21,-14,-29]]
- R₃ → R₃ + (1/2)R₂: [[3,0,2,2],[0,42,28,58],[0,0,0,0]]
- 2 non-zero rows → **rank = 2** ✓

#### CYP 2 Answers — Eigenvectors and M-Matrix

**Q1: Diagonalisation**
If A has n linearly independent eigenvectors x₁,...,xₙ, let T = (x₁,...,xₙ).
AT = (Ax₁,...,Axₙ) = (λ₁x₁,...,λₙxₙ) = TΛ
Since T is non-singular: **T⁻¹AT = Λ** ✓
(Converse: columns of T that satisfy AT = TΛ are eigenvectors of A)

**Q2: M = Iₙ - X(X'X)⁻¹X'**
(a) **Symmetry**: X(X'X)⁻¹X' is symmetric → M = I - X(X'X)⁻¹X' is symmetric
(b) **Idempotency**: MM = (I-H)(I-H) = I - H - H + H² = I - H = M (since H is idempotent: H²=H)
(c) **MX = 0**: MX = (I-H)X = X - X(X'X)⁻¹X'X = X - X = 0 ✓
(d) **rank(M) = n-k**: rank(M) = trace(M) = n - trace(Iₖ) = n - k

**Q3: X'V⁻¹M = 0 (given)**
(a) X'V⁻¹ = X'V⁻¹X(X'X)⁻¹X' → (X'V⁻¹X)⁻¹X'V⁻¹ = (X'X)⁻¹X'
(b) Post-multiply by VX(X'X)⁻¹: (X'V⁻¹X)⁻¹ = (X'X)⁻¹X'VX(X'X)⁻¹

#### CYP 3 Answers — Vec Identity and Fisher Information

**Q1: vec(ABC) = (C' ⊗ A) vec(B)**
(Proof as in Section above — using B = Σbᵢeᵢ' decomposition)

**Q2: Fisher Information for N(µ, σ²)**
logL(θ) = -(n/2)lnσ² - (1/(2σ²))Σ(xᵢ-µ)²

Score function: S(θ) = [n/σ²(x̄-µ), -n/(2σ²) + Σ(xᵢ-µ)²/(2σ⁴)]'

Fisher Information (expected): I(θ) = [[n/σ², 0], [0, n/(2σ⁴)]]

This is positive definite (det > 0) since n > 0 and σ² > 0.

### Quick Recall
> **Quick Recall:**
> - CYP 1: Inverse via cofactor method; Rank via row reduction
> - CYP 2: T⁻¹AT = Λ (diagonalisation); M symmetric, idempotent, MX=0, rank=n-k
> - CYP 3: vec(ABC)=(C'⊗A)vec(B); Fisher I(θ) = diag(n/σ², n/(2σ⁴)) for Normal

### Connections
- Verifies: All content in Chunks 005 and 006
- Closes: Unit 3 (Block 1 is now complete)
- Connects to: MLE Fisher Information → Cramér-Rao bound → efficiency of OLS vs MLE
