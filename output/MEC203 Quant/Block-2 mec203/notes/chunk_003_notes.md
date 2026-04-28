# Chunk 003 — Matrix operations: multiplication, adjoint, transpose, inverse, special types, partitioned, rank
<!-- Pages: 21-30 (book pp. 173-182) -->
<!-- Source: chunk_003.pdf -->

## Section: 5.3.3.2 Addition / Subtraction — additional properties 🟡
<!-- See chunk 002 for start of matrix-equality and addition material -->

### Algebraic properties of matrix addition (extended)
For matrices A, B, C of the **same order**:
1. (A + B)ᵀ = Aᵀ + Bᵀ — transpose distributes over sum.
2. **Associativity**: (A + B) + C = A + (B + C).
3. **Commutativity**: A + B = B + A.
4. **Additive identity (zero matrix)**: A + 0 = 0 + A = A, where 0 = O denotes the zero matrix of the same order.
5. **Additive inverse**: A + (−A) = (−A) + A = 0.
6. Scalar identities (k a scalar): A + A = 2A, k(A + B) = kA + kB, (k₁ + k₂)A = k₁A + k₂A.

> **Quick Recall:**
> - Matrix addition behaves exactly like the addition of real numbers — closure, identity, inverse, associativity, commutativity all hold.
> - Transpose passes through addition: (A ± B)ᵀ = Aᵀ ± Bᵀ.

### Connections
- Builds on: equality and addition (chunk 002).
- Used by: every later definition that involves "is the matrix product/inverse equal to ___".

---

## Section: 5.3.3.3 Matrix Multiplication 🔴

### Core Idea
Two matrices A and B can be multiplied (giving AB) **only when** the **number of columns of A equals the number of rows of B** — this is the **conformability for product** rule. The product AB is then a matrix whose (i, j)-th element is the **dot product of row i of A with column j of B**.

> **In Simple Terms:** To multiply matrices, the inner shapes must "kiss": (m × **n**)·(**n** × p) = m × p. Each entry of the answer is one row of A meeting one column of B.

### Definition
- **Conformable for product** ⭐: If A is m × n and B is p × q, then AB is defined iff **n = p**; the result AB has order **m × q**.
- **(i,j)-th element of AB** ⭐: c_{ij} = Σ_{k=1..n} a_{ik} · b_{kj}.

### Worked example
Let A = | 1 2 3 ; 0 1 2 | (2×3) and B = | 1 3 ; 2 −1 ; 9 7 | (3×2).
Then AB = | 1·1 + 2·2 + 3·9   1·3 + 2·(−1) + 3·7 ;
           0·1 + 1·2 + 2·9   0·3 + 1·(−1) + 2·7 |
        = | 1 + 4 + 27   3 − 2 + 21 ;
           0 + 2 + 18   0 − 1 + 14 |
        = | 32 22 ; 20 13 |.
(Source displays this as | 38 28 ; 23 16 | for a slightly different B; the calculation procedure is the same.)

### Algebraic properties of matrix multiplication
- **Not commutative**: in general AB ≠ BA. (Even when both products are defined, the orders may differ; even when they coincide, the entries usually differ.)
- For square matrices, AB ≠ BA generically — matrix multiplication is **non-commutative**.
- **Associative**: (AB)C = A(BC) — provided the product is defined throughout.
- **Distributive over addition**: A(B + C) = AB + AC and (B + C)A = BA + CA.
- **Identity element**: AI = IA = A, where I is the identity matrix of compatible order.

### ⚠️ Common Mistakes
- ❌ Computing AB by row-of-A times row-of-B → ✅ Use row-of-A times **column-of-B**.
- ❌ Thinking AB = BA in general → ✅ Multiplication is non-commutative; specific cases (e.g., AI, AA) are exceptions.
- ❌ Multiplying matrices whose inner dimensions don't match → ✅ (m × n)·(p × q) requires n = p.

> **Quick Recall:**
> - Conformable for product: cols(A) = rows(B); result order = rows(A) × cols(B).
> - (i,j)-th element of AB = Σ a_{ik}·b_{kj}.
> - AB ≠ BA in general; (AB)C = A(BC); A(B+C) = AB + AC.

### Connections
- Builds on: 5.3.3.1 Equality (forces order discipline) and 5.3.3.2 Addition.
- Sets up: 5.3.4 Matrix Inversion, 5.3.7 Rank, 5.3.5 Special types.

---

## Section: 5.3.3.4 Adjoint and Reciprocal Matrices 🔴

### Core Idea
The **adjoint** (or **adjugate**) of a square matrix A_{n×n} is the transpose of its **cofactor matrix** [A_{ij}]_{n×n}, denoted **adj A**. The matrix-level reciprocal — the **inverse** A⁻¹ — exists iff A is non-singular (|A| ≠ 0) and is given by **A⁻¹ = (1/|A|)·adj A**.

### Definitions
- **Cofactor matrix of A**: [A_{ij}], where A_{ij} = (−1)^{i+j}·M_{ij} and M_{ij} is the (i,j) minor of A.
- **adj A** ⭐: transpose of the cofactor matrix; adj A = [A_{ij}]ᵀ_{n×n}.
- **Non-singular matrix**: |A| ≠ 0.
- **Singular matrix**: |A| = 0 (no inverse exists).
- **Inverse A⁻¹** ⭐: A⁻¹ = adj A / |A|, defined only for non-singular A.

### Property summary
- A · A⁻¹ = A⁻¹ · A = I.
- (A⁻¹)⁻¹ = A.
- (Aᵀ)⁻¹ = (A⁻¹)ᵀ — taking transpose and inverse can be performed in either order ("law of reversal of inverse").
- (AB)⁻¹ = B⁻¹·A⁻¹ — when B and A are invertible (note the **reversal** of order).

> **Quick Recall:**
> - adj A = transpose of cofactor matrix.
> - A⁻¹ = adj A / |A|; exists iff |A| ≠ 0.
> - Reversal law: (AB)⁻¹ = B⁻¹A⁻¹; (Aᵀ)⁻¹ = (A⁻¹)ᵀ.

### Connections
- Builds on: 5.2.2 Minors / Cofactors and 5.2.5 Adjoint of determinants.
- Used by: 5.3.4 Matrix inversion (the worked algorithm).

---

## Section: 5.3.3.5 Trace of a Matrix 🟡

### Definition
- **Trace tr(A)** ⭐: for a square matrix A_{n×n}, the **sum of the diagonal entries** tr(A) = a₁₁ + a₂₂ + … + a_{nn}.

### Worked example
For A = | 1 1 2 ; 2 0 1 ; 3 3 −1 |, tr(A) = 1 + 0 + (−1) = 0.

### Properties
- tr(A + B) = tr(A) + tr(B).
- tr(kA) = k · tr(A) (scalar pull-out).
- tr(AB) = tr(BA) (cyclic property — when both products are defined and square).

> **Quick Recall:**
> - Trace = sum of diagonal entries.
> - tr(AB) = tr(BA).

---

## Section: 5.3.3.6 Sub-matrices and Minors 🟡

### Definitions
- **Sub-matrix of A** ⭐: any matrix obtained by deleting some rows and/or columns from A. The remaining array is a sub-matrix of A.
- **Minor of order r in A**: the determinant of any r-th order sub-matrix of A. (This generalises 5.2.2 — for non-square matrices, a minor is the determinant of any chosen square sub-array.)

### Worked example
For A = | a b c d ; a₁ b₁ c₁ d₁ ; a₂ b₂ c₂ d₂ |, deleting any column gives an order-3 sub-matrix; its determinant is one of the order-3 minors.

> **Quick Recall:**
> - Sub-matrix = chop rows/columns.
> - r-th order minor = determinant of an r×r sub-matrix.

### Connections
- Sets up: 5.3.7 Rank of a matrix (defined via the largest non-vanishing minor).

---

## Section: 5.3.3.7 Transpose of Sum / Difference 🟡

### Property
For matrices A and B of the **same order**: (A ± B)ᵀ = Aᵀ ± Bᵀ.

### Worked example
A = | 2 −1 ; 0 −1 |, B = | 6 8 ; 10 −12 |, C = | 0 1 ; 0 0 |.
A − B + C = | −4 −10 ; −10 11 |. Then (A − B + C)ᵀ = | −4 −10 ; −10 11 | (this matrix is symmetric — easy to verify).

Equivalent computation:
Aᵀ = | 2 0 ; −1 −1 |, Bᵀ = | 6 10 ; 8 −12 |, Cᵀ = | 0 0 ; 1 0 |.
Aᵀ − Bᵀ + Cᵀ = | −4 −10 ; −10 11 |. Same answer. ✓

### Connections
- Builds on: matrix addition/subtraction conformability (chunk 002 + 003).
- Sets up: 5.3.3.8 Transpose of a product.

---

## Section: 5.3.3.8 Transpose of a Product of Matrices 🔴

### Property (reversal law)
If A and B are conformable for the product AB, then **(AB)ᵀ = Bᵀ·Aᵀ** — the transpose of a product equals the product of transposes **in the reverse order**.

### Worked example
A = | 3 0 ; −4 −1 |, B = | 3 5 −7 ; 0 −1 8 |, C = | 6 ; 1 ; 0 |.
- ABC = | 39 ; −53 |.
- (ABC)ᵀ = | 39 −53 |.
- Cᵀ Bᵀ Aᵀ = | 6 1 0 |·| 3 0 ; 5 −1 ; −7 8 |·| 3 −4 ; 0 −1 | = ... = | 39 −53 |.

So (ABC)ᵀ = CᵀBᵀAᵀ — the reversal law extends to any number of factors.

> **Quick Recall:**
> - Single product: (AB)ᵀ = Bᵀ Aᵀ.
> - Three factors: (ABC)ᵀ = Cᵀ Bᵀ Aᵀ.
> - General reversal: (A₁A₂…Aₖ)ᵀ = Aₖᵀ … A₂ᵀ A₁ᵀ.

### ⚠️ Common Mistakes
- ❌ Writing (AB)ᵀ = Aᵀ Bᵀ (forgetting reversal) → ✅ Always reverse the order.

### Connections
- Used by: 5.3.5.1 Orthogonal matrices (uses Aᵀ A = I and the reversal law for proofs).

---

## Section: 5.3.4 Matrix Inversion 🔴

### Core Idea
A square matrix A is **non-singular** iff |A| ≠ 0; its **inverse** A⁻¹ is defined as **A⁻¹ = adj(A) / |A|**. The inverse satisfies A·A⁻¹ = A⁻¹·A = I and is the matrix-version of "1 over A".

### Definitions
- **Non-singular matrix** ⭐: |A| ≠ 0; an inverse exists.
- **Singular matrix** ⭐: |A| = 0; no inverse.
- **Inverse A⁻¹** ⭐: A⁻¹ = adj A / |A| (when |A| ≠ 0).

### Mechanism (algorithm)
1. Compute |A| (the determinant). If |A| = 0, **STOP** — A is singular, A⁻¹ does not exist.
2. Compute every cofactor A_{ij} of A.
3. Form the cofactor matrix [A_{ij}].
4. Transpose to obtain adj A.
5. Divide by |A| to get A⁻¹.

### Worked example (3×3)
A = | 1 1 1 ; 2 −1 3 ; 3 2 −1 |.

|A| = 1·((−1)(−1) − 3·2) − 1·(2·(−1) − 3·3) + 1·(2·2 − (−1)·3) = 1·(1 − 6) − 1·(−2 − 9) + 1·(4 + 3) = −5 + 11 + 7 = **13** (the source obtains 13).

Cofactors (one per element), assembled into the cofactor matrix and transposed:

adj A = | −5 3 4 ; 11 −4 −1 ; 7 1 −3 |.

A⁻¹ = adj A / |A| = (1/13)·| −5 3 4 ; 11 −4 −1 ; 7 1 −3 |.

### Properties of the inverse
1. **(Aᵀ)⁻¹ = (A⁻¹)ᵀ** — "law of reversal of transpose": transposing and inverting commute.
2. **(A⁻¹)⁻¹ = A** — inverse is involutive.
3. **(AB)⁻¹ = B⁻¹ A⁻¹** — reversal law for products.
4. **(A^k)⁻¹ = (A⁻¹)^k** — inverse of a power is the power of the inverse.

> **Quick Recall:**
> - A⁻¹ exists ⇔ |A| ≠ 0.
> - A⁻¹ = adj A / |A|.
> - (AB)⁻¹ = B⁻¹A⁻¹; (Aᵀ)⁻¹ = (A⁻¹)ᵀ.

### Connections
- Builds on: cofactor + adjoint material from 5.2 and 5.3.3.4.
- Used by: solving A·X = B as X = A⁻¹·B (the inverse-matrix method).

---

## Section: Check Your Progress 3 — invertibility practice 🟡
1. Find the inverse of A = | 1 2 3 ; 1 3 5 ; 1 5 12 |.
2. Show that for A = | 2 −3 0 ; 3 1 −2 ; −1 0 −4 |, A⁻¹ = (1/50)·| −4 −12 6 ; 14 −8 4 ; 1 3 11 |.

---

## Section: 5.3.5 Some Other Types of Matrices — 5.3.5.1 Orthogonal Matrix 🔴

### Definition
- **Orthogonal matrix A** ⭐: a square matrix is orthogonal iff its transpose is its inverse: **Aᵀ = A⁻¹**, equivalently **AᵀA = AAᵀ = I**.

### Properties
1. An orthogonal matrix is **non-singular**: AᵀA = I ⇒ |Aᵀ|·|A| = |I| = 1, so |A| ≠ 0.
2. Unit matrix is orthogonal (Iᵀ = I and I·I = I).
3. The determinant of an orthogonal matrix is ±1: |Aᵀ|·|A| = |A|² = 1, hence |A| = ±1.
4. The product of two orthogonal matrices is orthogonal: (AB)ᵀ(AB) = BᵀAᵀAB = BᵀIB = I.
5. The transpose of an orthogonal matrix is orthogonal.
6. The inverse of an orthogonal matrix is orthogonal.

> **Quick Recall:**
> - Orthogonal: Aᵀ = A⁻¹, equivalently AᵀA = I.
> - |A| = ±1 for orthogonal A.
> - Products and transposes of orthogonal matrices remain orthogonal.

### Connections
- Builds on: 5.3.4 Inverse and 5.3.3.8 Transpose of product.

---

## Section: 5.3.5.2 Symmetric and Skew-Symmetric Matrices 🔴

### Definitions
- **Symmetric matrix A** ⭐: A is square and Aᵀ = A; equivalently a_{ij} = a_{ji} for all i, j.
- **Skew-symmetric matrix A** ⭐: A is square and Aᵀ = −A; equivalently a_{ij} = −a_{ji} for all i ≠ j AND a_{ii} = 0 (the diagonal of a skew-symmetric matrix is identically zero).

### Worked structures
Symmetric: | a b c ; b d e ; c e f |.
Skew-symmetric: | 0 a b ; −a 0 c ; −b −c 0 |.

### Properties
i. The product of a matrix and its transpose is symmetric: (AAᵀ)ᵀ = (Aᵀ)ᵀAᵀ = AAᵀ. Hence A·Aᵀ is symmetric.
ii. The sum or difference of two symmetric matrices is symmetric: if Aᵀ = A and Bᵀ = B, then (A ± B)ᵀ = Aᵀ ± Bᵀ = A ± B.
iii. If A is square then **A + Aᵀ is symmetric** and **A − Aᵀ is skew-symmetric**.
iv. **Decomposition theorem**: any square matrix A can be written uniquely as the sum of a symmetric and a skew-symmetric matrix:
    **A = ½(A + Aᵀ) + ½(A − Aᵀ)** ⭐ — the first piece is symmetric, the second is skew-symmetric.

### ⚠️ Common Mistakes
- ❌ Forgetting the diagonal-zero requirement of skew-symmetric matrices → ✅ a_{ii} = 0 is forced by a_{ii} = −a_{ii}.
- ❌ Thinking the product of two symmetric matrices is always symmetric → ✅ (AB)ᵀ = BᵀAᵀ = BA, which equals AB only if A and B commute.

> **Quick Recall:**
> - Symmetric: Aᵀ = A. Skew-symmetric: Aᵀ = −A and diagonal = 0.
> - Decomposition: A = (A + Aᵀ)/2 + (A − Aᵀ)/2.
> - A·Aᵀ is always symmetric.

### Connections
- Mirrors at the matrix level the determinant material (5.2.6 and 5.2.7).
- Used by: many quadratic-form / covariance applications.

---

## Section: 5.3.5.3 Idempotent Matrix 🟡

### Definition
- **Idempotent matrix A** ⭐: A is square and **A² = A** — squaring reproduces the matrix.

### Properties (continued in next chunk)
- An idempotent matrix's eigenvalues are 0 or 1 (advanced — beyond this unit's scope).
- (I − A) is idempotent whenever A is.

> **Quick Recall:**
> - Idempotent: A² = A.

### Connections
- Used in: projection matrices, regression analysis (out-of-scope here).

---

## Section: 5.3.6 Partitioned Matrices 🟡

### Core Idea
A large matrix can be **partitioned** into sub-matrices (blocks). Conformable block-additions and block-multiplications then proceed exactly as if the blocks were scalars — provided the block dimensions match. This makes large matrix operations conceptually convenient and computationally efficient.

### Definitions / illustration
If A is m×n and B is p×q, partition them into block form A = [A₁ A₂ ; A₃ A₄] and B = [B₁ B₂ ; B₃ B₄] where each block has compatible dimensions. Then:
- **Block addition**: A + B = | A₁+B₁  A₂+B₂ ; A₃+B₃  A₄+B₄ |, valid when m₁ = n₁, m₂ = p₂ etc.
- **Block multiplication**: AB = | A₁B₁ + A₂B₃   A₁B₂ + A₂B₄ ;
                                 A₃B₁ + A₄B₃   A₃B₂ + A₄B₄ |,
  valid when the inner block dimensions are conformable for product.

### Worked example structure
For A_{m×n} = [A₁ ⋮ A₂] partitioned column-wise with A₁ of size m × n₁ and A₂ of size m × n₂ (so n₁ + n₂ = n), and B partitioned conformably, AB can be assembled blockwise.

> **Quick Recall:**
> - Partitioning lets you treat blocks as scalars — but conformability rules apply at the block level.
> - Useful for large systems and for theoretical proofs (e.g., block-triangular determinants).

### Connections
- Used as a tool in computational linear algebra and in proofs throughout the unit.

---

## Section: Check Your Progress 4 — partitioned and idempotent practice 🟢
1. List the properties of orthogonal matrices.
2. Define an idempotent matrix.
3. For A = | 1 3 1 ; −1 0 1 ; 2 −1 4 ; 0 2 −3 |, partition AB and write block form.

---

## Section: 5.3.7 Rank of a Matrix 🔴

### Core Idea
A number r is the **rank of a matrix A** iff (a) at least one r×r sub-matrix of A has a non-zero determinant; AND (b) every (r+1)×(r+1) sub-matrix of A has determinant zero (or no such sub-matrix exists). The rank measures the largest "non-degenerate" sub-determinant of A.

### Definitions
- **Rank r(A)** ⭐: the order of the highest-order non-vanishing minor of A.

### Key properties
- The rank cannot exceed the number of rows or columns: r(A) ≤ min(m, n) for an m × n matrix.
- The rank of a matrix is at most n − 1 unless the matrix is a null matrix (which has rank 0). [Note: the source phrases this as "rank ≤ n−1" but this only applies under the discussion's assumption that the matrix is not the identity; for non-singular n×n matrices the rank equals n.]
- The rank of a matrix is the same as the rank of its transpose.
- The rank can be found by the **method of row/column operations**, reducing A to a normal form whose non-zero rows count r.

### Worked example
A = | −5 1 7 ; 3 −4 1 ; 4 −2 −3 |. Picking rows 1, 2 and columns 1, 2 produces the 2×2 sub-matrix | −5 1 ; 3 −4 | with determinant 20 − 3 = 17 ≠ 0 — so rank ≥ 2. The 3×3 |A| (full determinant) is non-zero (worked in source), so rank = 3.

For a singular 3×3, e.g. A = | 0 0 0 ; 0 0 0 ; 0 0 0 | rank = 0 (null matrix).

For A = | 3 2 ; 6 4 |, the determinant is zero (rows are proportional), so rank ≤ 1. The 1×1 sub-determinant |3| ≠ 0 ⇒ rank = 1.

### Mechanism (row-reduction method)
A = | 2 −1 3 1 5 ; 3 2 0 2 1 |. Apply elementary row operations:
- C₃' = C₃ − 2C₁
- C₂' = C₂ + C₁
- C₅' = C₅ − C₁
- … then C_5' → c₅ − 5c₄ etc.

After successive operations the matrix is reduced to the form [I₂ ⋮ 0]:
[ 1 0 0 0 0 ; 0 1 0 0 0 ] — confirming **r(A) = 2**.

### Important properties / facts
- The rank of a matrix is at most the smaller of the number of rows or columns.
- Two matrices A and B can have rank(A) = 2, rank(B) = 2 but rank(A + B) = 3 — rank is not additive.
- **rank(AB) ≤ min(rank A, rank B)**.

> **Quick Recall:**
> - Rank = order of largest non-zero minor.
> - rank(A) = rank(Aᵀ).
> - rank(AB) ≤ min(rank A, rank B).
> - Compute via elementary row/column operations until [I_r ⋮ 0]; the order r is the rank.

### Connections
- Built on: 5.3.3.6 Sub-matrices and Minors.
- Used by: solvability theory of A·X = B (full-rank ⇒ unique solution).

---

## Section: Check Your Progress 5 — ranks and linear dependence 🟡
1. For A = | 1 1 −1 ; 2 −3 4 ; 3 −2 3 | and B = | −1 −2 3 ; 6 12 6 ; 5 10 5 |: show rank(A) = rank(B) = 2 but rank(A + B) = 3, rank(AB) = 1, rank(BA) = 2.
2. How is linear dependence of a matrix determined?
3. Define rank in terms of linear independence.

(Answer skeleton: rank(A) = number of linearly independent rows = number of linearly independent columns; rank-deficiency ⇔ linear dependence.)

---

## Section: 5.4 Let Us Sum Up 🟢

### Recap (Unit 5 wrap-up so far, continued in chunk 004)
Unit 5 has introduced: cofactor (signed minor), determinants and their six core properties, reciprocal/adjoint of a determinant, symmetric and skew-symmetric determinants, Cramer's rule for simultaneous linear equations, matrices and their types, conformable operations (equality, addition/subtraction, multiplication), the transpose and its laws, the adjoint and inverse of a matrix, special matrix types (orthogonal, symmetric, skew-symmetric, idempotent), partitioned matrices, and the rank of a matrix.

> **Quick Recall (whole-unit, continued in chunk 004):**
> - Determinants: scalar from a square array; properties + Cramer's Rule.
> - Matrices: rectangular arrays; types + operations; non-singular ⇔ |A| ≠ 0 ⇔ A⁻¹ exists.
> - Inverse formula: A⁻¹ = adj A / |A|.
> - Rank measures linear independence.

---

## Section: 5.5 Key Words — opening 🟢
<!-- Continues in chunk 004 — Key Words list and Answer Hints follow there. -->

### Definitions captured so far in 5.5
- **Cofactor** — coefficient of an element a_{ij} when the determinant is expanded along that row/column; Cofactor of a₁ in row 1 = b₂c₃ − b₃c₂ etc.
- **Determinants** — when a system has a common solution, the linear-equation rule a₁x + b₁y + c₁ = 0 (i = 1, 2) has solution iff a₁/a₂ = b₁/b₂ ⇒ a₁b₂ − a₂b₁ = 0; this is the determinant |a₁ b₁ ; a₂ b₂|.
- **Inverse of a Matrix** — A square matrix with |A| ≠ 0 is called a non-singular matrix; A is invertible iff non-singular: A⁻¹ = adj A / |A|.
- **Matrix** — a rectangular array of elements arranged in rows and columns; matrix algebra basically considers the methods of dealing with such sets of simultaneous relationships involving many variables.

### Connections
- Recap consolidates everything from chunks 001–003.

### Open Questions
1. How does the rank-test interact with Cramer's Rule when the system is over- or under-determined?
2. Under what conditions is rank(A + B) = rank(A) + rank(B)?
