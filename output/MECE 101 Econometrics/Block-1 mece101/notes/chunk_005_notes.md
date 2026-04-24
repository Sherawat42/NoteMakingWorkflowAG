# Chunk 005 — Unit 2 CYP Answers & Unit 3: Matrix Algebra — Notation, Types, Multiplication, Determinants, Inverse, Rank
<!-- Pages: 40–49 -->
<!-- Source: chunk_005.txt -->
<!-- Continues from: Estimation Methods (Chunk 004) -->
<!-- Continues into: Partitioned Matrices, Eigenvalues, Special Matrices (Chunk 006) -->

## Section: Unit 2 CYP Answers (Self-Check) 🟡

### Core Idea
The Check Your Progress answers for Unit 2 validate the core concepts of statistical inference: parameter vs statistic, point vs interval estimation, sampling distribution, estimator properties, hypothesis types, and estimation methods.

> **In Simple Terms:** This section is the answer key for Unit 2. Cross-check your understanding against these model answers before an exam.

### Key Concepts

#### CYP 1 Model Answers
1. **Parameter vs Statistic**: Parameter = unknown fixed quantity in the population (e.g., µ, σ²); Statistic = estimated mean or variance from a sample; statistic is a function of sample observations.
2. **Point vs Interval Estimate**: Point estimate = specific numerical value from a statistic. Interval estimate = range (T₁, T₂) such that P(T₁ ≤ Ø ≤ T₂) = 1-α; also called confidence interval.
3. **Estimator vs Estimate**: Estimator is the same rule for all samples; estimate varies from sample to sample. The distribution of many point estimates from different samples is the **sampling distribution** of the statistic.
4. **Four properties of good estimator**: (i) Unbiasedness (ii) Consistency (iii) Efficiency (iv) Sufficiency
5. **Two conditions for consistency**: (i) lim_{n→∞}[E(T) - Ø] = 0 AND (ii) lim_{n→∞} Var(T) = 0

#### CYP 2 Model Answers
1. **Simple vs Composite Hypothesis**: Simple = all parameters specified; Composite = one or more not exactly specified
2. **One-tailed vs Two-tailed**: H₁: µ ≠ µ₀ → two-tailed; H₁: µ < µ₀ or H₁: µ > µ₀ → one-tailed (left or right)
3. **Type-I vs Type-II**: Type-I = rejecting true H₀ (α = max allowed prob; usually 1% or 5%); Type-II = accepting false H₀. Type-I is more serious.
4. **OLS principle**: Choose values minimising S = Σeᵢ²; unique solution when normal equations = unknowns
5. **MLE properties**: (a) consistent, efficient, sufficient; (b) not necessarily unbiased (but correctable); (c) approximately normal for large samples; (d) invariant to functional transformation.

### Quick Recall
> **Quick Recall:**
> - WLLN: P(|Aₙ - µ| < α) = 1; SLLN: P(Aₙ = µ) = 1 (both as n→∞)
> - Type-I (worse): reject true H₀; Type-II: accept false H₀
> - MLE: consistent + efficient + sufficient + approx normal + invariant

### Connections
- Confirms: All Unit 2 content (Chunks 003–004)
- Transitions into: Unit 3 Matrix Algebra (below)

---

## Section: Unit 3 Introduction — Why Matrix Algebra 🟡

### Core Idea
Matrix algebra is integral to econometrics because it allows concise representation of many variables and generalisation of results from simple to complex models. Unit 3 revisits matrix concepts from MEC 203 (Quantitative Methods) with emphasis on special matrices relevant to econometric theory.

> **In Simple Terms:** Instead of writing 10 regression equations with 10 variables each, matrix algebra lets you write Y = Xβ + u — one line. That elegance is why matrices matter in econometrics.

### Key Concepts
#### Role of Matrix Algebra in Econometrics
- Compact notation: represents multiple equations in one expression (Y = Xβ + u)
- Facilitates mathematical operations (differentiation, inversion) on systems of equations
- Enables generalisation from small to large variable sets
- Essential for deriving OLS estimator β̂ = (X'X)⁻¹X'y

### Quick Recall
> **Quick Recall:**
> - Matrix algebra compresses multiple regression into Y = Xβ + u
> - Key operation: (X'X)⁻¹X'y = OLS estimator formula

### Connections
- Prerequisite for: OLS estimation in matrix form (Block 2, Unit 4)

---

## Section: Matrix Notation & Basic Types 🔴

### Core Idea
A matrix is a rectangular array of numbers. Key notation: upper-case bold for matrices (A), lower-case bold for vectors (a), lower-case for scalars. The dimension is m × n (rows × columns). Several special matrix types appear repeatedly in econometrics: identity, diagonal, triangular, symmetric, null, and transpose.

> **In Simple Terms:** A matrix is just a table of numbers, organised in rows and columns. Special tables (like the identity matrix) have nice mathematical properties that we exploit in regression derivations.

### Key Concepts

#### Matrix, Vector, Scalar — Definitions
- An m × n matrix A has m rows and n columns; element aᵢⱼ is at row i, column j
- If m = n: **square matrix**
- An n × 1 matrix: **column vector** (a bold lowercase letter, e.g., **a**)
- A 1 × n matrix: **row vector**
- A 1 × 1 matrix: **scalar**

#### Special Matrix Types

| Type | Definition | Symbol |
|------|-----------|--------|
| Diagonal | aᵢⱼ = 0 for i ≠ j, aᵢᵢ ≠ 0 for some i | D |
| Identity | Diagonal with all diagonal elements = 1 | Iₙ |
| Lower-triangular | aᵢⱼ = 0 for i < j | L |
| Upper-triangular | aᵢⱼ = 0 for i > j | U |
| Null (zero) | All elements = 0 | 0 |
| Symmetric | A = A' (transpose equals original) | A |
| Transpose | A' = (aⱼᵢ) — rows and columns swapped | A' or Aᵀ |

### Definitions
- **Matrix**: A rectangular array of numbers; m × n means m rows, n columns. ⭐ (exam-important)
- **Square Matrix**: A matrix where m = n (equal number of rows and columns).
- **Column Vector / Row Vector**: An n×1 or 1×n matrix.
- **Diagonal Matrix**: A matrix where all off-diagonal elements are zero.
- **Identity Matrix (Iₙ)**: A diagonal matrix where all diagonal elements equal 1. ⭐ (exam-important)
- **Lower/Upper Triangular Matrix**: Matrix where elements below/above the main diagonal are zero.
- **Null (Zero) Matrix**: A matrix where all elements are zero.
- **Transpose (A' or Aᵀ)**: Obtained by swapping rows and columns of A; (aᵢⱼ) → (aⱼᵢ).
- **Symmetric Matrix**: A matrix equal to its own transpose: A = A'. ⭐ (exam-important)

### Quick Recall
> **Quick Recall:**
> - Iₙ = n×n identity; diagonal = zeros off-diagonal; symmetric = A = A'
> - Transpose notation: A' or Aᵀ (both used interchangeably in the text)
> - Symmetric matrices have nice properties: orthogonal diagonalisation (Chunk 006)

### Connections
- Prerequisite for: Matrix multiplication (below), Inverse (below), Rank (below)
- Connects to: OLS normal equations in matrix form (Block 2)

---

## Section: Matrix Multiplication 🔴

### Core Idea
Two matrices A (m × n) and B (p × q) can be multiplied **only if n = p** (inner dimensions match). The result AB is m × q. The (i,j) element of AB is the dot product of the i-th row of A and the j-th column of B. Matrix multiplication is generally **not commutative** (AB ≠ BA in general).

> **In Simple Terms:** For AB to work, A's columns must equal B's rows — like making sure the pieces fit together. The result has A's rows and B's columns. Order matters — flipping A and B usually gives a different answer.

### Key Concepts

#### Conformability Condition
A (m × n) × B (p × q) is defined if and only if **n = p**. Result: (m × q).

#### Properties of Matrix Multiplication
For conformable matrices A, B, C and scalar λ:
- (AB)C = A(BC) — **Associativity** ✓
- A(B + C) = AB + AC — **Distributivity** ✓
- AB ≠ BA in general — **Not commutative** ✗
- (AB)' = B'A' — **Transpose of product reverses order** ⭐
- If AB = BA, A and B are said to **commute**

### Definitions
- **Conformable Matrices**: Two matrices where the inner dimensions match for multiplication (columns of A = rows of B). ⭐ (exam-important)
- **Pre-multiplication**: Multiplying from the left (BA); **Post-multiplication**: multiplying from the right (AB) — results differ.

### ⚠️ Common Mistakes
- ❌ Mistake: Assuming AB = BA for all matrices → ✅ Correct: Matrix multiplication is generally NOT commutative
- ❌ Mistake: Confusing (AB)' = A'B' → ✅ Correct: (AB)' = **B'A'** — order reverses

### Quick Recall
> **Quick Recall:**
> - AB defined when: cols(A) = rows(B); result is m×q
> - (AB)' = B'A' — reversal rule ⭐
> - AB ≠ BA (not commutative, in general)

### Connections
- Prerequisite for: Determinants, Inverse, OLS β̂ = (X'X)⁻¹X'y

---

## Section: Determinants, Orthogonal Matrices & Trace 🔴

### Core Idea
The determinant of a square matrix is a scalar that encodes whether the matrix is invertible (non-zero det → invertible). An orthogonal matrix preserves lengths and angles (A'A = I). The trace is the sum of diagonal elements and equals the sum of eigenvalues. These three properties are fundamental to understanding invertibility, orthogonality, and eigenvalue theory in econometrics.

> **In Simple Terms:** The determinant tells you whether the matrix is "usable" (non-zero = invertible). The trace is just the sum of diagonal numbers. Orthogonal matrices are "rotation" matrices that don't distort shapes.

### Key Concepts

#### Determinant
- det(A) ≠ 0 ↔ A is **non-singular** (invertible)
- det(A) = 0 ↔ A is **singular** (not invertible)
- det(AB) = det(A) × det(B)
- det(A') = det(A)
- det(I) = 1
- det(λA) = λⁿ det(A) for n×n matrix

#### Orthogonal Matrix
A matrix A is orthogonal if **A'A = AA' = I** (i.e., A' = A⁻¹).
Key property: **det(A'A) = [det(A)]² = det(I) = 1**, so det(A) = ±1.

#### Trace of a Matrix
**trace(A) = tr(A) = Σ aᵢᵢ** (sum of diagonal elements)

Properties:
- tr(A + B) = tr(A) + tr(B)
- tr(λA + μB) = λtr(A) + μtr(B)
- tr(A) = tr(A')
- tr(AA') = tr(A'A) = Σᵢⱼ aᵢⱼ²
- **tr(In) = n**

### Definitions
- **Determinant**: A scalar value encoding the invertibility of a square matrix; det(A) ≠ 0 ↔ A is invertible. ⭐ (exam-important)
- **Singular Matrix**: A square matrix with det(A) = 0; cannot be inverted. ⭐ (exam-important)
- **Non-Singular Matrix**: A square matrix with det(A) ≠ 0; invertible. ⭐ (exam-important)
- **Orthogonal Matrix**: A matrix where A'A = I (transpose = inverse); det(A) = ±1. ⭐ (exam-important)
- **Trace**: tr(A) = Σ aᵢᵢ; sum of diagonal elements; equals sum of eigenvalues. ⭐ (exam-important)

### Quick Recall
> **Quick Recall:**
> - det(A) ≠ 0 → invertible; det(A) = 0 → singular (cannot invert)
> - Orthogonal: A'A = I → det(A) = ±1
> - trace(A) = Σ diagonal elements = Σ eigenvalues (see Chunk 006)

### Connections
- Is prerequisite for: Inverse (below), Rank (below), Eigenvalues (Chunk 006)
- Connects to: Idempotent matrix trace = rank (Chunk 006)

---

## Section: Inverse of a Matrix 🔴

### Core Idea
The inverse A⁻¹ of a non-singular square matrix A satisfies AA⁻¹ = A⁻¹A = I. Only non-singular matrices (det ≠ 0) are invertible. The inverse is computed using the adjoint (adjugate) matrix: A⁻¹ = (1/det(A)) × adj(A). The OLS estimator β̂ = (X'X)⁻¹X'y requires (X'X) to be invertible — i.e., non-singular.

> **In Simple Terms:** The inverse is the matrix equivalent of "dividing by A." Just like 5 × (1/5) = 1, A × A⁻¹ = I. But you can only divide by a non-singular matrix — singular matrices are like dividing by zero.

### Key Concepts

#### Conditions for Invertibility
Matrix A is invertible ↔ det(A) ≠ 0 ↔ A is non-singular ↔ A has full rank.
A singular matrix **cannot be inverted**.

#### Computing the Inverse — Cofactor/Adjoint Method
For A = [[a₁₁, a₁₂], [a₂₁, a₂₂]] (2×2 case):
A⁻¹ = (1/(a₁₁a₂₂ - a₁₂a₂₁)) × [[a₂₂, -a₁₂], [-a₂₁, a₁₁]]

General formula for n×n:
1. Compute det(A)
2. Compute the cofactor matrix (each cᵢⱼ = (-1)^{i+j} × det(Aᵢⱼ))
3. Adjoint = transpose of cofactor matrix
4. **A⁻¹ = (1/det(A)) × adj(A)** ⭐

#### CYP Worked Example (3×3 Inverse)
For A = [[2,4,1],[4,3,7],[2,1,3]]:
- det(A) = 10 (computed via cofactor expansion along row 2)
- Cofactor matrix = [[2,2,-2],[-11,4,6],[25,-10,-10]]
- adj(A) = (cofactor matrix)ᵀ = [[2,-11,25],[2,4,-10],[-2,6,-10]]
- A⁻¹ = (1/10) × adj(A)

#### Properties of the Inverse
- (λA)⁻¹ = (1/λ)A⁻¹ for scalar λ ≠ 0
- (A⁻¹)⁻¹ = A
- (A⁻¹)' = (A')⁻¹ — inverse and transpose commute
- (AB)⁻¹ = B⁻¹A⁻¹ — **order reverses**
- For diagonal A: diagonal elements of A⁻¹ are 1/aᵢᵢ

### Definitions
- **Inverse of a Matrix (A⁻¹)**: Unique matrix satisfying AA⁻¹ = A⁻¹A = I; exists only for non-singular matrices. ⭐ (exam-important)
- **Adjoint (Adjugate) Matrix**: Transpose of the cofactor matrix of A; used in computing A⁻¹.
- **Cofactor Cᵢⱼ**: (-1)^{i+j} × det(Aᵢⱼ) where Aᵢⱼ is the submatrix obtained by deleting row i and column j.

### ⚠️ Common Mistakes
- ❌ Mistake: (AB)⁻¹ = A⁻¹B⁻¹ → ✅ Correct: **(AB)⁻¹ = B⁻¹A⁻¹** — order reverses (same reversal as transpose)
- ❌ Mistake: Attempting to invert a singular matrix → ✅ Correct: Singular matrices have no inverse

### Quick Recall
> **Quick Recall:**
> - A⁻¹ = (1/det(A)) × adj(A); requires det(A) ≠ 0
> - (AB)⁻¹ = B⁻¹A⁻¹ (reversal rule) ⭐
> - In OLS: β̂ = (X'X)⁻¹X'y — requires (X'X) to be invertible

### Connections
- Builds on: Determinants (above)
- Is prerequisite for: Rank (below), Partitioned Matrices (Chunk 006), OLS estimator derivation (Block 2)

---

## Section: Rank of a Matrix 🔴

### Core Idea
The rank of a matrix is the maximum number of linearly independent rows (or columns). Rank determines whether a system of equations has a unique solution — and whether the OLS estimator β̂ = (X'X)⁻¹X'y can be computed (requires X to have full column rank). Rank is found by reducing the matrix to row echelon form and counting non-zero rows.

> **In Simple Terms:** Rank counts how many "genuinely different" rows a matrix has. If two rows are just multiples of each other, they don't add new information — they're linearly dependent. Only independent rows count toward the rank.

### Key Concepts

#### Row Echelon Form
A matrix is in row echelon form if:
1. All zero rows are at the bottom
2. Each non-zero row has more leading zeros than the row above it
3. Operations allowed: scalar multiplication of rows, addition/subtraction of rows

#### Rank via Row Reduction
Rank = number of non-zero rows in row echelon form = number of **pivot** positions.

**CYP Worked Example**: For A = [[3,0,2,2],[-6,42,24,54],[21,-21,0,-15]]:
- After R₂ → R₂ + 2R₁, R₃ → R₃ - 7R₁, then R₃ → R₃ + (1/2)R₂:
- Result: [[3,0,2,2],[0,42,28,58],[0,0,0,0]]
- 2 non-zero rows → **rank = 2**

#### Key Rank Properties
- rank(A) = 0 ↔ A = 0
- rank(Iₙ) = n
- rank(λA) = rank(A) for λ ≠ 0
- rank(diagonal) = number of non-zero diagonal elements
- rank(A + B) ≤ rank(A) + rank(B)
- rank(AB) ≤ min(rank A, rank B)
- For m×n matrix: rank(A) ≤ min{m, n}
- For n×n matrix: A⁻¹ exists ↔ rank(A) = n (full rank)

### Definitions
- **Rank of a Matrix**: Maximum number of linearly independent rows (= maximum linearly independent columns) in the matrix. ⭐ (exam-important)
- **Row Echelon Form**: A matrix form where all zero rows are at bottom and each non-zero row has strictly more leading zeros than the row above.
- **Linearly Independent Rows**: Rows where no row can be expressed as a linear combination of the others.
- **Full Rank**: For an n×n matrix, rank = n; matrix is invertible. For X (n×k), full column rank = rank k; required for OLS.

### ⚠️ Common Mistakes
- ❌ Mistake: rank of A ≠ rank of A' → ✅ Correct: rank(A) = rank(A') always
- ❌ Mistake: Thinking square matrix = full rank automatically → ✅ Correct: A square matrix can be rank-deficient (singular)

### Quick Recall
> **Quick Recall:**
> - Rank = non-zero rows in row echelon form = number of pivots
> - Full rank (n×n): rank = n ↔ invertible ↔ det ≠ 0
> - X must have full column rank (rank k) for OLS to work
> - rank(AB) ≤ min(rank A, rank B)

### Connections
- Builds on: Determinants and Inverse (above)
- Continues into: Properties verified for M-matrix (Chunk 006)
- Connects to: Multicollinearity in regression — X rank-deficient when variables are perfectly collinear (Block 3)
