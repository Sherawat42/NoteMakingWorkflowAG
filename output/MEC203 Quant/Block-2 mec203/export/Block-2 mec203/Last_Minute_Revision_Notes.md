# Last Minute Revision Notes

> *This document contains ONLY ultra-high-yield definitions (⭐), Quick Recall facts, Common Mistakes, and core bullet points.*


## Topics


**Quick Recall:**
- Block 2 = Linear Algebra (Units 5–8).
- Unit 5 covers determinants + matrices in one package.
- Cramer's rule and the inverse-matrix method are the two solution techniques you must master.

### 5.2 Determinants — 5.2.1 Definition and Concept 🔴

**Derivation of the 2×2 determinant**
1. a₁x + b₁y + c₁ = 0
2. a₂x + b₂y + c₂ = 0
- written compactly as |a₁ b₁ ; a₂ b₂| = a₁b₂ − a₂b₁. ⭐

**Order, rows, columns, elements**
- The numbers inside the determinant are **elements**.
- Horizontal lines of elements form **rows**; vertical lines form **columns**.
- A determinant with n rows and n columns is a **determinant of the n-th order**.
- A 2nd-order determinant has 2² = 4 elements; a 3rd-order has 3² = 9 elements; an n-th order has n² elements.

**3×3 determinant — the "Sarrus" diagonal rule**
- "↘" diagonals (top-left to bottom-right) — **positive**: a·q·z + b·r·x + c·p·y.
- "↗" diagonals (top-right to bottom-left) — **negative**: c·q·x + a·r·y + b·p·z.
- Δ = a₁(b₂c₃ − b₃c₂) − b₁(a₂c₃ − a₃c₂) + c₁(a₂b₃ − a₃b₂). ⭐
- **Determinant**: the single scalar value associated with a square array of numbers (the "determinant" of the array). ⭐ (exam-important)
- **Element**: any individual entry inside the determinant.
- **Order of a determinant**: the number of rows (= number of columns) of the square array; an order-n determinant has n² elements.
- The theory of **equations**, geometry, multiple integrals, differential equations, and linear algebra.
- **Concise solution-formulas** for simultaneous linear equations.
- The **Jacobian determinant** ∂(u,v)/∂(x,y), an essential tool of mathematical analysis used to test for **functional dependence** in a system of non-linear equations and to test whether the linear system can be solved with workable algebraic expressions.
- Generalisations of the equations for conic sections in two dimensions.
- **Jacobian determinant** of two functions u(x,y), v(x,y):
- J = | ∂u/∂x  ∂u/∂y ; ∂v/∂x  ∂v/∂y |, written ∂(u,v)/∂(x,y). ⭐ (exam-important — recurring concept across calculus/economics)

**Quick Recall:**
- 2×2 determinant = a₁b₂ − a₂b₁.
- 3×3 determinant via row-1 expansion has six signed terms; positive on ↘ diagonals, negative on ↗ diagonals.
- Order-n determinant has n² elements; expansion has n! terms.
- Jacobian determinant tests functional dependence in non-linear systems.
- Sets up: 5.2.2 Minors and Cofactors (uses sub-determinants formed by deleting rows/columns).
- Sets up: 5.2.3 Properties of Determinants and 5.2.8 Cramer's Rule.

### 5.2.2 Minors and Cofactors 🔴
- **Minor of an element a_{ij}**: the determinant formed by deleting the i-th row and j-th column from the original determinant; denoted M_{ij}. The minor is *minor* in size — its order is one less than the original. ⭐
- **Cofactor of a_{ij}**: A_{ij} = (−1)^{i+j} · M_{ij}. The "cofactor" is just the minor with the appropriate sign attached; it is the *coefficient* of the element a_{ij} in the row/column expansion. ⭐
- **Note on size**: in an n-th order determinant, every minor / cofactor is itself a determinant of order (n−1).
1. Pick element a_{ij}.
2. Strike out row i and column j.
3. The (n−1)×(n−1) determinant that remains = M_{ij} (minor).
4. Multiply by (−1)^{i+j} to get the cofactor A_{ij}.
5. Row-1 expansion of an order-n determinant: Δ = a₁A₁ + a₂A₂ + … + aₙAₙ, where A₁, A₂, … are the cofactors of the elements of the first row.
- A₁ = (−1)¹⁺¹ |1 3 ; 2 1| = (1)(1·1 − 3·2) = (1)(−5) = −5.
- A₂ = (−1)¹⁺² |2 3 ; 7 1| = (−1)(2·1 − 3·7) = (−1)(−19) = 19.
- A₃ = (−1)¹⁺³ |2 1 ; 7 2| = (1)(2·2 − 1·7) = −3.

### ⚠️ Common Mistakes
- ❌ Forgetting the (−1)^{i+j} sign and treating M_{ij} as the cofactor → ✅ A_{ij} = (−1)^{i+j} M_{ij}; always attach the sign.
- ❌ Treating "minor" as smaller than the element it belongs to → ✅ The minor is a *determinant*, not a number; its order is one less than the parent determinant.
- ❌ Mixing up rows and columns of the deleted element → ✅ Cross out the row AND column that pass through a_{ij}; whatever is left is the minor.

**Quick Recall:**
- Minor M_{ij} = determinant after deleting row i + column j.
- Cofactor A_{ij} = (−1)^{i+j} · M_{ij}.
- Δ = Σⱼ aᵢⱼ Aᵢⱼ along any chosen row i (or column j).
- In an order-n determinant, every minor / cofactor has order n−1.
- Builds on: 5.2.1 Definition (cofactors are signed minors of the parent determinant).
- Prerequisite for: 5.2.5 Adjoint and reciprocal determinants (built from cofactors).
- Prerequisite for: matrix inverse via the adjoint formula (later in Unit 5).

### 5.2.3 Properties of Determinants — Properties I to VI 🔴

**Property I — Transpose property**

**Property II — Row/column interchange**

**Property III — Two equal rows / columns**

**Property IV — Multiplying a row/column by a scalar**

**Property V — Splitting a row/column that is a sum**

**Property VI — Row/column operation (the "elimination" property)**

### ⚠️ Common Mistakes
- ❌ Forgetting that **proportional** rows (not only identical rows) make the determinant zero → ✅ Property III says "identical OR proportional".
- ❌ Pulling K out of *every* row when only one row has the factor → ✅ Property IV: K comes out only for the row/column that actually has K as the common factor.
- ❌ Splitting a determinant when only **one element** is a sum → ✅ Property V requires *each element of the row/column* to be a sum; otherwise re-derive.
- ❌ Sign error after row/column swap → ✅ One swap flips the sign once; two swaps restore the sign.
- ❌ Adding a multiple of one row to a non-corresponding position → ✅ Property VI uses the *corresponding* (same column-index) elements only.

**Quick Recall:**
- Six properties: transpose, swap (sign flip), equal/proportional → 0, scalar multiply, sum-split, add multiple of another row.
- Transpose property → all rules apply to both rows and columns.
- Use Property VI to introduce zeros and cut work; use Property IV to pull out common factors before expanding.
- Two identical or proportional rows ⇒ determinant = 0 (test by inspection).
- Builds on: 5.2.1 Definition (these properties operate on the same expansion).
- Used by: every later determinant calculation, including 5.2.4 Product of Two Determinants and 5.2.8 Cramer's Rule.
1. How does Property VI generalise to several simultaneous row operations performed in sequence (do successive applications still preserve the value)?

### 5.2.3 Properties of Determinants — Properties continued (sum-split worked example) 🔴

**Quick Recall:**
- Property V = "row/column-of-sums splits the determinant"; verify with two evaluations and check they sum to the direct expansion.

### 5.2.4 The Product of Two Determinants 🔴

**General formula (2×2 case)**

**General formula (3×3 case)**

**Numerical example**

### ⚠️ Common Mistakes
- ❌ Using row-of-first × row-of-second → ✅ It must be **row-of-first × column-of-second** (just like ordinary matrix multiplication).
- ❌ Multiplying determinants of *different* orders directly → ✅ Both must be the same order; otherwise pad/extend or restate the problem.

**Quick Recall:**
- |A|·|B| can be written as one determinant of the same order using the row-by-column rule.
- Same-order requirement is mandatory.
- Ties directly into |AB| = |A|·|B| once matrices are introduced (later in unit).
- Builds on: 5.2.1 Definition (uses determinant expansion).
- Prerequisite for: linking determinants and matrix multiplication later in Unit 5.
- 3. | 1 1 1 ; a b c ; a² b² c² | = (b−a)(c−a)(c−b) — a **Vandermonde determinant**; ⭐ standard exam result.

**Quick Recall:**
- > - Vandermonde 3×3: | 1 1 1 ; a b c ; a² b² c² | = (b−a)(c−a)(c−b). ⭐
- The "b+c, c+a, a+b" determinant evaluates to 4abc.

### 5.2.5 Adjoint and Reciprocal Determinants 🔴
- **Adjoint of Δ** ⭐: determinant of cofactors of Δ, placed in transposed positions: Δ′ = (A_{ij})ᵀ where A_{ij} are the cofactors of Δ.
- **Reciprocal / Inverse of Δ** ⭐ (Δ ≠ 0): (1/Δ)·Δ′; equivalently the determinant whose elements are A_{ij}/Δ.
1. Compute every cofactor A_{ij} of Δ (with sign (−1)^{i+j}).
2. Place A_{ij} in row j, column i of the new array — **transpose** while filling.
3. The resulting array is Δ′ (the adjoint).
4. Divide every entry of Δ′ by Δ to obtain the reciprocal.
- Δ = 0·(0·0 − 1·2) − 1·(2·0 − 1·1) + 2·(2·2 − 0·1) = 0 − 1·(−1) + 2·4 = 0 + 1 + 8 = **9**.
- B₁ = +|0 1 ; 2 0| = −2; B₂ = −|1 2 ; 2 0| = +4; B₃ = +|1 2 ; 0 1| = 1.
- C₁ = +A₃ = 4; C₂ = −B₃ = −2 (i.e. (−1)^{2+3}·1 with sign), C₃ = −2 etc. — full table built one row at a time.

### ⚠️ Common Mistakes
- ❌ Forgetting to **transpose** when assembling the adjoint → ✅ adj(Δ) = (cofactor matrix)ᵀ.
- ❌ Trying to take a reciprocal when Δ = 0 → ✅ Reciprocal exists only if Δ ≠ 0 (singular determinants have no inverse).
- ❌ Mixing up minors and cofactors when filling the adjoint → ✅ The adjoint uses **cofactors** (signed minors), not raw minors.

**Quick Recall:**
- adj(Δ) = transpose of the cofactor matrix.
- Reciprocal Δ⁻¹ = adj(Δ)/Δ, exists iff Δ ≠ 0.
- Δ · adj(Δ) = Δⁿ (= Δ³ for 3×3 case).
- Builds on: 5.2.2 Minors and Cofactors.
- Prerequisite for: matrix inverse via the adjoint formula in 5.3 (inverse of a non-singular matrix).
- **Symmetric determinant** ⭐: a₁ⱼ = aⱼ₁ in general, a_{ij} = a_{ji}; the second row is the same as the second column, etc. Example structure: | a h g ; h b f ; g f c |.

**Quick Recall:**
- a_{ij} = a_{ji} ⇒ symmetric.
- Δᵀ = Δ; adj Δ also symmetric.
- Squaring a symmetric determinant (Δᵀ·Δ) yields a symmetric determinant.
- **Skew-symmetric determinant** ⭐: a_{ij} = −a_{ji} for i ≠ j AND a_{ii} = 0. Example structure: | 0 a b ; −a 0 c ; −b −c 0 |.

**Quick Recall:**
- Skew: a_{ij} = −a_{ji} for i ≠ j (diagonal free).
- Skew-symmetric: a_{ij} = −a_{ji} AND a_{ii} = 0.
- Odd order skew-symmetric ⇒ 0.
- Even order skew-symmetric ⇒ perfect square.

### 5.2.8 Solution of Simultaneous Equations by Cramer's Rule 🔴
1. a₁x + b₁y + c₁z = k₁
2. a₂x + b₂y + c₂z = k₂
3. a₃x + b₃y + c₃z = k₃
- Δ = | a₁ b₁ c₁ ; a₂ b₂ c₂ ; a₃ b₃ c₃ | (coefficient determinant; must be ≠ 0).
- Δ_x = | k₁ b₁ c₁ ; k₂ b₂ c₂ ; k₃ b₃ c₃ |.
- Δ_y = | a₁ k₁ c₁ ; a₂ k₂ c₂ ; a₃ k₃ c₃ |.
- Δ_z = | a₁ b₁ k₁ ; a₂ b₂ k₂ ; a₃ b₃ k₃ |.
- Then **x = Δ_x / Δ, y = Δ_y / Δ, z = Δ_z / Δ**. ⭐
- So (x₁, x₂) = (5, 1). ⭐

### ⚠️ Common Mistakes
- ❌ Applying Cramer's Rule when Δ = 0 → ✅ Either no solution or infinitely many — Cramer fails. Use Gaussian elimination or the rank test.
- ❌ Replacing the wrong column for a variable → ✅ For variable i, replace **column i** of Δ by the constants k.
- ❌ Forgetting that the constants vector must be on the right of A·X = B before reading off → ✅ Move all constants to the right side first; if a system is in the form a₁x + b₁y + c₁ = 0, rewrite as a₁x + b₁y = −c₁.

**Quick Recall:**
- Cramer's Rule: x_i = Δ_i / Δ, where Δ_i replaces column i of Δ with the constants.
- Works only when Δ ≠ 0.
- One determinant per unknown, plus the coefficient determinant.
- Builds on: 5.2.1 Definition + 5.2.3 Properties (used to compute Δ, Δ_x, etc.).
- Contrasts with: matrix inverse method A⁻¹·B and Gaussian elimination — Cramer is conceptually clean but computationally expensive for large n.

### 5.3 MATRIX — 5.3.1 Concept of a Matrix 🔴
- A has 3 pants, 3 shirts, 1 tie.
- B has 5 pants, 5 shirts, 2 ties.
- C has 6 pants, 8 shirts, 0 ties.
- **Matrix** ⭐: a rectangular arrangement of m·n numbers (or symbols) into m rows and n columns. Denoted A = [a_{ij}] where a_{ij} is the element in row i, column j.
- **Order (size) of a matrix**: m × n, read "m by n"; m = number of rows, n = number of columns.
- **Element a_{ij}**: entry of A in the i-th row and j-th column.
- "Matrix algebra": the basic operations and methods for dealing with such arrays in solving simultaneous equations involving many variables.
- A is denoted [a_{ij}] or (a_{ij}); brackets [ ], parentheses ( ), or large parentheses ‖ ‖ are all acceptable.
- Square matrices: m = n; the matrix is then **of order n**.
- Sets up: 5.3.2 Types of matrices, 5.3.3 Matrix relations and operations.

### 5.3.2 Types of Matrices 🔴
| Type | Definition | Schematic |
|------|------------|-----------|
| **Rectangular matrix** | m ≠ n. Order m × n. | A_{m×n} |
| **Square matrix** | m = n. Order n. | A_{n×n} |
| **Row matrix** (row vector) | Order 1×n; a single row. | [a₁₁ a₁₂ … a_{1n}] |
| **Column matrix** (column vector) | Order m×1; a single column. | [a₁₁; a₂₁; …; a_{m1}]ᵀ |
| **Null / zero matrix** | Every element is 0; order m × n; denoted O_{m×n}. | All entries 0 |
| **Non-zero matrix** | Has at least one element ≠ 0. | — |
| **Transpose Aᵀ** | Rows become columns. (m × n) ⇒ (n × m). Denoted Aᵀ or A′. | Reflect across main diagonal |
| **Diagonal matrix** | Square; off-diagonal a_{ij} = 0 for i ≠ j AND at least one a_{ii} ≠ 0. | diag(a₁, a₂, …, aₙ) |
| **Scalar matrix** | Diagonal matrix with all diagonal entries equal: a_{ii} = a (a constant) and a_{ij} = 0 for i ≠ j. | a·I |
| **Identity matrix I_n** ⭐ | Diagonal matrix with all diagonal entries = 1. Sometimes written I_n; denoted I. | a_{ii} = 1, a_{ij} = 0 for i ≠ j |
- **Diagonal matrix**: | 1 0 0 ; 0 2 0 ; 0 0 3 |.
- **Scalar matrix**: a · I, e.g. | a 0 0 ; 0 a 0 ; 0 0 a |.
- **Identity matrix of order 3**: I₃ = | 1 0 0 ; 0 1 0 ; 0 0 1 |.
- **Transpose**: if A = | a₁ b₁ c₁ ; a₂ b₂ c₂ |, then Aᵀ = | a₁ a₂ ; b₁ b₂ ; c₁ c₂ |. The transpose of a matrix of order m×n is of order n×m.
- **Null/zero matrix**: O₂×₃ = | 0 0 0 ; 0 0 0 |.

### ⚠️ Common Mistakes
- ❌ Calling every "diagonal-only" matrix a scalar matrix → ✅ A scalar matrix requires the diagonal entries to be **all equal**; otherwise it is a generic diagonal matrix.
- ❌ Confusing the identity matrix with the **scalar matrix** "1·I" — they coincide, but in general a scalar matrix is not the identity unless the constant is 1.

**Quick Recall:**
- Square matrix has m = n.
- Identity I has 1's on the diagonal, 0 elsewhere; I = Iᵀ.
- Scalar = diagonal with equal entries; Identity = scalar with constant 1.
- Transpose is row-column swap; (Aᵀ)ᵀ = A.
- Builds on: 5.3.1 Concept of Matrix.
- Sets up: more types and matrix operations in chunk 003 (continued types G–N, equality, addition, multiplication).

### 5.3.3 Matrix Relations and Operations — opening (Equality of Matrices, Addition, Subtraction) 🔴
- **Conformable for equality** ⭐: A = [a_{ij}] and B = [b_{ij}] of the **same order** are **equal** iff a_{ij} = b_{ij} for every (i, j).
- **Conformable for sum/difference**: same order m × n.
- Order 1×2 vs 1×3: not conformable for equality. E.g., [1² 2³] vs [1 4 ; 9 16] — different orders → unequal by definition.
- Same-order example: | 1 2 3 ; 3 4 5 | + | 0 1 2 ; 2 3 4 | = | 1+0 2+1 3+2 ; 3+2 4+3 5+4 | = | 1 3 5 ; 5 7 9 |.
- A + B = B + A (matrix addition is **commutative**).
- (A + B) + C = A + (B + C) (matrix addition is **associative**).

### ⚠️ Common Mistakes
- ❌ Trying to add matrices of different orders → ✅ Addition requires the same order m × n.
- ❌ Treating (A − B) as undefined → ✅ A − B = A + (−B) when both are the same order; entry-wise subtraction.

**Quick Recall:**
- Equality: same order AND elementwise equal.
- Addition / Subtraction: same order; entry-wise.
- Addition is commutative and associative.
- Sets up: 5.3.3.3 Matrix multiplication (different conformability rule, treated in next chunk).
1. Why are matrix multiplication conformability requirements (m₁×n₁ · n₁×n₂) different from those for addition? (Resolved in next chunk via the row-by-column definition.)

**Quick Recall:**
- Matrix addition behaves exactly like the addition of real numbers — closure, identity, inverse, associativity, commutativity all hold.
- Transpose passes through addition: (A ± B)ᵀ = Aᵀ ± Bᵀ.

### 5.3.3.3 Matrix Multiplication 🔴
- **Conformable for product** ⭐: If A is m × n and B is p × q, then AB is defined iff **n = p**; the result AB has order **m × q**.
- **(i,j)-th element of AB** ⭐: c_{ij} = Σ_{k=1..n} a_{ik} · b_{kj}.
- **Not commutative**: in general AB ≠ BA. (Even when both products are defined, the orders may differ; even when they coincide, the entries usually differ.)
- For square matrices, AB ≠ BA generically — matrix multiplication is **non-commutative**.
- **Associative**: (AB)C = A(BC) — provided the product is defined throughout.
- **Distributive over addition**: A(B + C) = AB + AC and (B + C)A = BA + CA.
- **Identity element**: AI = IA = A, where I is the identity matrix of compatible order.

### ⚠️ Common Mistakes
- ❌ Computing AB by row-of-A times row-of-B → ✅ Use row-of-A times **column-of-B**.
- ❌ Thinking AB = BA in general → ✅ Multiplication is non-commutative; specific cases (e.g., AI, AA) are exceptions.
- ❌ Multiplying matrices whose inner dimensions don't match → ✅ (m × n)·(p × q) requires n = p.

**Quick Recall:**
- Conformable for product: cols(A) = rows(B); result order = rows(A) × cols(B).
- (i,j)-th element of AB = Σ a_{ik}·b_{kj}.
- AB ≠ BA in general; (AB)C = A(BC); A(B+C) = AB + AC.
- Builds on: 5.3.3.1 Equality (forces order discipline) and 5.3.3.2 Addition.
- Sets up: 5.3.4 Matrix Inversion, 5.3.7 Rank, 5.3.5 Special types.

### 5.3.3.4 Adjoint and Reciprocal Matrices 🔴
- **Cofactor matrix of A**: [A_{ij}], where A_{ij} = (−1)^{i+j}·M_{ij} and M_{ij} is the (i,j) minor of A.
- **adj A** ⭐: transpose of the cofactor matrix; adj A = [A_{ij}]ᵀ_{n×n}.
- **Non-singular matrix**: |A| ≠ 0.
- **Singular matrix**: |A| = 0 (no inverse exists).
- **Inverse A⁻¹** ⭐: A⁻¹ = adj A / |A|, defined only for non-singular A.
- A · A⁻¹ = A⁻¹ · A = I.
- (A⁻¹)⁻¹ = A.
- (Aᵀ)⁻¹ = (A⁻¹)ᵀ — taking transpose and inverse can be performed in either order ("law of reversal of inverse").
- (AB)⁻¹ = B⁻¹·A⁻¹ — when B and A are invertible (note the **reversal** of order).

**Quick Recall:**
- adj A = transpose of cofactor matrix.
- A⁻¹ = adj A / |A|; exists iff |A| ≠ 0.
- Reversal law: (AB)⁻¹ = B⁻¹A⁻¹; (Aᵀ)⁻¹ = (A⁻¹)ᵀ.
- Builds on: 5.2.2 Minors / Cofactors and 5.2.5 Adjoint of determinants.
- Used by: 5.3.4 Matrix inversion (the worked algorithm).
- **Trace tr(A)** ⭐: for a square matrix A_{n×n}, the **sum of the diagonal entries** tr(A) = a₁₁ + a₂₂ + … + a_{nn}.

**Quick Recall:**
- Trace = sum of diagonal entries.
- tr(AB) = tr(BA).
- **Sub-matrix of A** ⭐: any matrix obtained by deleting some rows and/or columns from A. The remaining array is a sub-matrix of A.

**Quick Recall:**
- Sub-matrix = chop rows/columns.
- r-th order minor = determinant of an r×r sub-matrix.

### 5.3.3.8 Transpose of a Product of Matrices 🔴
- ABC = | 39 ; −53 |.
- (ABC)ᵀ = | 39 −53 |.
- Cᵀ Bᵀ Aᵀ = | 6 1 0 |·| 3 0 ; 5 −1 ; −7 8 |·| 3 −4 ; 0 −1 | = ... = | 39 −53 |.

**Quick Recall:**
- Single product: (AB)ᵀ = Bᵀ Aᵀ.
- Three factors: (ABC)ᵀ = Cᵀ Bᵀ Aᵀ.
- General reversal: (A₁A₂…Aₖ)ᵀ = Aₖᵀ … A₂ᵀ A₁ᵀ.

### ⚠️ Common Mistakes
- ❌ Writing (AB)ᵀ = Aᵀ Bᵀ (forgetting reversal) → ✅ Always reverse the order.
- Used by: 5.3.5.1 Orthogonal matrices (uses Aᵀ A = I and the reversal law for proofs).

### 5.3.4 Matrix Inversion 🔴
- **Non-singular matrix** ⭐: |A| ≠ 0; an inverse exists.
- **Singular matrix** ⭐: |A| = 0; no inverse.
- **Inverse A⁻¹** ⭐: A⁻¹ = adj A / |A| (when |A| ≠ 0).
1. Compute |A| (the determinant). If |A| = 0, **STOP** — A is singular, A⁻¹ does not exist.
2. Compute every cofactor A_{ij} of A.
3. Form the cofactor matrix [A_{ij}].
4. Transpose to obtain adj A.
5. Divide by |A| to get A⁻¹.
1. **(Aᵀ)⁻¹ = (A⁻¹)ᵀ** — "law of reversal of transpose": transposing and inverting commute.
2. **(A⁻¹)⁻¹ = A** — inverse is involutive.
3. **(AB)⁻¹ = B⁻¹ A⁻¹** — reversal law for products.
4. **(A^k)⁻¹ = (A⁻¹)^k** — inverse of a power is the power of the inverse.

**Quick Recall:**
- A⁻¹ exists ⇔ |A| ≠ 0.
- A⁻¹ = adj A / |A|.
- (AB)⁻¹ = B⁻¹A⁻¹; (Aᵀ)⁻¹ = (A⁻¹)ᵀ.
- Builds on: cofactor + adjoint material from 5.2 and 5.3.3.4.
- Used by: solving A·X = B as X = A⁻¹·B (the inverse-matrix method).

### 5.3.5 Some Other Types of Matrices — 5.3.5.1 Orthogonal Matrix 🔴
- **Orthogonal matrix A** ⭐: a square matrix is orthogonal iff its transpose is its inverse: **Aᵀ = A⁻¹**, equivalently **AᵀA = AAᵀ = I**.
1. An orthogonal matrix is **non-singular**: AᵀA = I ⇒ |Aᵀ|·|A| = |I| = 1, so |A| ≠ 0.
2. Unit matrix is orthogonal (Iᵀ = I and I·I = I).
3. The determinant of an orthogonal matrix is ±1: |Aᵀ|·|A| = |A|² = 1, hence |A| = ±1.
4. The product of two orthogonal matrices is orthogonal: (AB)ᵀ(AB) = BᵀAᵀAB = BᵀIB = I.
5. The transpose of an orthogonal matrix is orthogonal.
6. The inverse of an orthogonal matrix is orthogonal.

**Quick Recall:**
- Orthogonal: Aᵀ = A⁻¹, equivalently AᵀA = I.
- |A| = ±1 for orthogonal A.
- Products and transposes of orthogonal matrices remain orthogonal.
- Builds on: 5.3.4 Inverse and 5.3.3.8 Transpose of product.

### 5.3.5.2 Symmetric and Skew-Symmetric Matrices 🔴
- **Symmetric matrix A** ⭐: A is square and Aᵀ = A; equivalently a_{ij} = a_{ji} for all i, j.
- **Skew-symmetric matrix A** ⭐: A is square and Aᵀ = −A; equivalently a_{ij} = −a_{ji} for all i ≠ j AND a_{ii} = 0 (the diagonal of a skew-symmetric matrix is identically zero).
- **A = ½(A + Aᵀ) + ½(A − Aᵀ)** ⭐ — the first piece is symmetric, the second is skew-symmetric.

### ⚠️ Common Mistakes
- ❌ Forgetting the diagonal-zero requirement of skew-symmetric matrices → ✅ a_{ii} = 0 is forced by a_{ii} = −a_{ii}.
- ❌ Thinking the product of two symmetric matrices is always symmetric → ✅ (AB)ᵀ = BᵀAᵀ = BA, which equals AB only if A and B commute.

**Quick Recall:**
- Symmetric: Aᵀ = A. Skew-symmetric: Aᵀ = −A and diagonal = 0.
- Decomposition: A = (A + Aᵀ)/2 + (A − Aᵀ)/2.
- A·Aᵀ is always symmetric.
- Mirrors at the matrix level the determinant material (5.2.6 and 5.2.7).
- Used by: many quadratic-form / covariance applications.
- **Idempotent matrix A** ⭐: A is square and **A² = A** — squaring reproduces the matrix.

**Quick Recall:**
- Idempotent: A² = A.

**Quick Recall:**
- Partitioning lets you treat blocks as scalars — but conformability rules apply at the block level.
- Useful for large systems and for theoretical proofs (e.g., block-triangular determinants).

### 5.3.7 Rank of a Matrix 🔴
- **Rank r(A)** ⭐: the order of the highest-order non-vanishing minor of A.
- The rank cannot exceed the number of rows or columns: r(A) ≤ min(m, n) for an m × n matrix.
- The rank of a matrix is at most n − 1 unless the matrix is a null matrix (which has rank 0). [Note: the source phrases this as "rank ≤ n−1" but this only applies under the discussion's assumption that the matrix is not the identity; for non-singular n×n matrices the rank equals n.]
- The rank of a matrix is the same as the rank of its transpose.
- The rank can be found by the **method of row/column operations**, reducing A to a normal form whose non-zero rows count r.
- C₃' = C₃ − 2C₁
- C₂' = C₂ + C₁
- C₅' = C₅ − C₁
- … then C_5' → c₅ − 5c₄ etc.
- The rank of a matrix is at most the smaller of the number of rows or columns.
- Two matrices A and B can have rank(A) = 2, rank(B) = 2 but rank(A + B) = 3 — rank is not additive.
- **rank(AB) ≤ min(rank A, rank B)**.

**Quick Recall:**
- Rank = order of largest non-zero minor.
- rank(A) = rank(Aᵀ).
- rank(AB) ≤ min(rank A, rank B).
- Compute via elementary row/column operations until [I_r ⋮ 0]; the order r is the rank.
- Built on: 5.3.3.6 Sub-matrices and Minors.
- Used by: solvability theory of A·X = B (full-rank ⇒ unique solution).

**Quick Recall:**
- Determinants: scalar from a square array; properties + Cramer's Rule.
- Matrices: rectangular arrays; types + operations; non-singular ⇔ |A| ≠ 0 ⇔ A⁻¹ exists.
- Inverse formula: A⁻¹ = adj A / |A|.
- Rank measures linear independence.
- 3. **Vandermonde determinant** | 1 1 1 ; a b c ; a² b² c² | = (b − a)(c − a)(c − b). ⭐ Hint chain: subtract column 1 from columns 2 and 3, expand along the new row 1.
- 4. | b+c  a    a ; b    c+a  b ; c    c    a+b | = **4abc** ⭐. Hint chain: C₁ → C₁ + C₂ + C₃, then row reductions; the "a + b + c" common factor disappears via cancellation.
- ∴ x = Δ_x/Δ = 1, y = Δ_y/Δ = 1, z = Δ_z/Δ = 1. ⭐

**Quick Recall:**
- > - Vandermonde 3×3 = (b−a)(c−a)(c−b). ⭐
- > - "b+c, c+a, a+b" cyclic determinant = 4abc. ⭐
- Cramer's example used in Unit 5 final answers: (x,y,z) = (1,1,1).

### 5.7 Exercises (worked-out examples and end-of-unit problems) 🔴
- Y − C = I + G
- C − bY = a, i.e. −bY + C = a.
- Y = Δ_Y / Δ = | I + G  −1 ; a  1 | / (1 − b) = ( I + G + a ) / (1 − b). ⭐
- C = Δ_C / Δ = | 1  I + G ; −b  a | / (1 − b) = ( a + b(I + G) ) / (1 − b). ⭐
- Y = C + I + G (income identity).
- C = a + b(Y − T), i.e. C − bY + bT = a (consumption with disposable income).
- T = d + tY, i.e. tY − T = −d (lump-sum + proportional tax).
- Y = ( bd − I(t − 1) − a − G ) / ( bt + b − 1 ).
- C = (some symmetric expression) / Δ.
- T = ( −d + bd − at − G·t ) / ( bt + b − 1 ).
- C = 0.8Y, I = 102 − 0.2r.
- Mᵈ = 0.25Y − 2.5r, Mˢ = Mᵈ.

**Quick Recall:**
- > - National income with C = a + bY: Y = (a + I + G)/(1 − b). ⭐ — 1/(1−b) is the Keynesian multiplier.
- > - For the tax-augmented system, denominator becomes (1 − b + bt). ⭐
- Homogeneous A·X = 0 has non-trivial solution iff |A| = 0.
- Closes Unit 5; bridges into Unit 6 (vectors as a different structure for solving multi-variable problems).

### 6.1 Introduction — vector vs scalar 🔴
- **Set (n-element)**: an unordered collection {a, b, c, …, n}; the sets {a, b, c} and {a, c, b} are equal.
- **Vector** ⭐: an ordered n-tuple, e.g. (a, b, c, …, n); the order matters, so (a, b) ≠ (b, a) generically.
- **Element / component / coordinate** of a vector: each entry of the n-tuple.
- **n-vector / vector in ℝⁿ**: an ordered n-tuple of real numbers.
- **Null vector** ⭐: the vector all of whose components are zero. In economics, the null vector represents an absence of any commodity in a bundle (e.g. nothing consumed by the household).
- A vector can be written as a **row vector** (1×n) or as a **column vector** (n×1); these are the **same object** transposed.
  - Row form: (a, b, c, …, n) or [a b c … n].
  - Column form: vertical stack [a; b; c; …; n].
- Two vectors are **equal** iff they have the same number of components and corresponding components match.
- Builds on: matrix notation (row matrix = row vector; column matrix = column vector).

### 6.2 Vector Addition and Scalar Multiplication 🔴
- **Sum of vectors** a + b = (a₁ + b₁, …, aₙ + bₙ); defined only when both vectors have the same number of components.
- **Difference**: a − b = (a₁ − b₁, …, aₙ − bₙ).
- **Scalar product / scalar multiple** ⭐: k·a = (k a₁, k a₂, …, k aₙ) for k ∈ ℝ. This is the product of a vector by a real number — *not* the inner product of two vectors (treated separately in 6.4 — *different concept*).
1. a = (1, 1, −2), b = (3, 0, 1) ⇒ a + b = (1+3, 1+0, −2+1) = (4, 1, −1).
2. a = (1, 4, 3, −6, 2), b = (3, −5, 1, −2, 3) ⇒ a − b = (1−3, 4−(−5), 3−1, −6−(−2), 2−3) = (−2, 9, 2, −4, −1).
3. 3·a = (3, 12, 9) (scalar multiplication of (1, 4, 3) by 3).

### ⚠️ Common Mistakes
- ❌ Confusing **scalar multiplication** (vector × number) with **scalar product / inner product** (vector × vector → number) → ✅ "Scalar multiplication" makes a vector; "scalar product / inner product" makes a number.
- Foundational for: 6.3 Geometrical interpretation, 6.4 Norm and inner product, 6.5 Vector spaces.

### 6.3 Geometrical and Physical Interpretations 🔴
- **Magnitude (length) of a vector** in ℝ²: ‖a‖ = √(a₁² + a₂²); in ℝ³: ‖a‖ = √(a₁² + a₂² + a₃²).
- **Direction angle θ** in ℝ²: tan θ = a₂ / a₁.
- **Direction cosines (ℝ³)**: cos α = a₁ / ‖a‖, cos β = a₂ / ‖a‖, cos γ = a₃ / ‖a‖.
- **Free vector**: equal magnitude and direction ⇒ same vector regardless of starting point.
- A vector is fully described by its **magnitude** and **direction**; if either differs, the vectors are different.
- In ℝ³ a vector starting at (a₁, a₂, a₃) and ending at (b₁, b₂, b₃) is represented by the n-tuple (b₁ − a₁, b₂ − a₂, b₃ − a₃) — a **displacement vector**.
- Vector arithmetic ↔ space of points: vectors and points in ℝⁿ are in **one-to-one correspondence** (after fixing the origin).
- Sets up: 6.4 Norm/inner product (which generalises the geometric magnitude/angle to algebraic operations on n-tuples).

### 6.4 Norm and Inner Product 🔴
- **Inner product / scalar product / dot product** ⭐ of a = (a₁, …, aₙ) and b = (b₁, …, bₙ): ⟨a, b⟩ = a₁b₁ + a₂b₂ + … + aₙbₙ = Σ aᵢbᵢ. Notation: ⟨a, b⟩ or a · b.
- **Norm (length) of a** ⭐: ‖a‖ = √⟨a, a⟩ = √(a₁² + a₂² + … + aₙ²).
- **Unit vector**: a vector with ‖a‖ = 1; for any non-zero a, the unit vector along a is a / ‖a‖.
- **Orthogonal vectors** ⭐: a ⊥ b iff ⟨a, b⟩ = 0. The zero vector is orthogonal to every vector.
- a = (1, −1, 2), b = (3, 1, 0): ⟨a, b⟩ = 1·3 + (−1)·1 + 2·0 = 3 − 1 + 0 = 2.
- a = (1, 3), b = (−3, 1): ⟨a, b⟩ = −3 + 3 = 0 ⇒ a ⊥ b.
- a = (1, −2, 3): ‖a‖ = √(1 + 4 + 9) = √14.
- Symmetry: ⟨a, b⟩ = ⟨b, a⟩.
- Linearity in the first argument: ⟨k·a, b⟩ = k·⟨a, b⟩; ⟨a + a′, b⟩ = ⟨a, b⟩ + ⟨a′, b⟩.
- **(Σ aᵢbᵢ)² ≤ (Σ aᵢ²)·(Σ bᵢ²)** ⭐ — squared inner product ≤ product of squared norms.
- cos θ = 0 ⇔ a ⊥ b ⇔ ⟨a, b⟩ = 0.
- cos θ = ±1 ⇔ a is a scalar multiple of b ⇔ a is **parallel** to b.

### ⚠️ Common Mistakes
- ❌ Calling ka the "scalar product" of a → ✅ "Scalar product" is the inner product ⟨a, b⟩, not k·a (which is "scalar multiplication").
- ❌ Forgetting that any vector is orthogonal to the zero vector → ✅ ⟨0, b⟩ = 0 for all b.

**Quick Recall:**
- Inner product ⟨a, b⟩ = Σ aᵢbᵢ.
- Norm ‖a‖ = √Σ aᵢ².
- > - Cauchy–Schwarz: (Σ aᵢbᵢ)² ≤ (Σ aᵢ²)·(Σ bᵢ²). ⭐
- cos θ = ⟨a, b⟩ / (‖a‖·‖b‖); a ⊥ b ⇔ ⟨a, b⟩ = 0.
- Builds on: 6.2 Vector addition / scalar multiplication.
- Sets up: 6.5 Vector Spaces (definition of "linear" and "geometric" structure together).

### 6.5 Vector Spaces and Subspaces 🔴
- **Vector space V over ℝ** ⭐: a set V = {(x₁, x₂, …, xₙ) : xᵢ ∈ ℝ} with vector addition and scalar multiplication satisfying:
- **Subspace W of V** ⭐: a non-empty W ⊂ V that satisfies (a) w ∈ W ⇒ −w ∈ W (additive-inverse closure), and (b) w₁, w₂ ∈ W and α ∈ ℝ ⇒ w₁ + w₂ ∈ W and α·w₁ ∈ W.
- W = {(x₁, x₂) ∈ ℝ² : x₁ = 0} is a subspace of ℝ².
- W = {(x₁, x₂) ∈ ℝ² : x₁ + x₂ + 1 = 0} is **not** a subspace of ℝ² (does not contain (0, 0)).
- Every vector space contains the zero vector (additive identity).
- Every line through the origin and every plane through the origin in ℝ³ is a subspace.
- The intersection of two subspaces is a subspace.

**Quick Recall:**
- Vector space = set with addition and scalar multiplication, plus 8 axioms.
- Subspace = subset that is itself a vector space — must contain 0 and be closed under +, ·.
- Lines/planes through the origin are subspaces; offset lines/planes are not.
- Builds on: 6.2 Vector operations.
- Sets up: 6.6 Linear Dependence and 6.7 Generators / Basis.
1. How do the eight axioms fail for a subset that is missing the zero vector? (Answer: closure-under-scalar-multiplication-by-0 forces 0 ∈ W; missing 0 ⇒ not closed.)

### 6.6 Linear Dependence of Vectors 🔴
- **Linearly dependent set** ⭐: ∃ c₁, …, cₙ not all zero with Σ cᵢ xⁱ = 0.
- **Linearly independent set** ⭐: Σ cᵢ xⁱ = 0 ⇒ every cᵢ = 0.
| Result | Statement |
|--------|-----------|
| (a) Subset-dependence ⇒ whole set dependent | If a subset {x¹, …, x^k} of {x¹, …, xⁿ}, k < n, is linearly dependent, then the whole set {x¹, …, xⁿ} is also linearly dependent. |
| (b) Whole-set independence ⇒ subset independent | If {x¹, …, xⁿ} is linearly independent, then any subset {x¹, …, x^k}, k < n, is also linearly independent. |
1. **Two-vector dependence**: x = (1, 0, 3)ᵀ, y = (3, 0, 9)ᵀ. Check 3x − y = (3, 0, 9)ᵀ − (3, 0, 9)ᵀ = **0**. Coefficients (3, −1) are non-zero ⇒ x and y are linearly dependent. Equivalently y = 3x.
2. **Three-vector dependence**: x = (1, 3)ᵀ, y = (−2, 5)ᵀ, z = (3, −2)ᵀ. Check x − y − z = (1, 3)ᵀ − (−2, 5)ᵀ − (3, −2)ᵀ = (1 + 2 − 3, 3 − 5 + 2)ᵀ = (0, 0)ᵀ. So z = x − y.

### ⚠️ Common Mistakes
- ❌ Stating "all coefficients are non-zero" → ✅ The definition needs *not all zero* — at least one cᵢ ≠ 0 suffices.
- ❌ Allowing non-linear (e.g. quadratic) operations to test dependence → ✅ Only scalar multiplication + vector addition are admissible.

**Quick Recall:**
- > - Dependent ⇔ some non-trivial Σ cᵢ xⁱ = 0. ⭐
- Subset dependent ⇒ whole set dependent.
- Whole set independent ⇒ every subset independent.
- Dependence means at least one vector is a linear combination of the others.
- Builds on: 6.2 Vector addition / scalar multiplication; 6.5 Vector spaces.
- Sets up: 6.7 Generators and Basis (which require linear independence).

### 6.7 Generators and Basis 🔴
- **n-dimensional Euclidean space Eⁿ** ⭐: the collection of all n-tuples a = (a₁, …, aₙ), aᵢ ∈ ℝ, with vector addition, scalar multiplication, and a notion of distance.
- **Generators / Spanning set** ⭐: a set {a₁, …, aₙ} ⊂ Eⁿ such that every x ∈ Eⁿ can be written as x = Σ cᵢ aᵢ for some scalars cᵢ.
- **Basis of Eⁿ** ⭐: a set of vectors that is (i) a generator of Eⁿ AND (ii) linearly independent.
- The generator set is **not unique** — many different sets of vectors can generate the same space.
- For Eⁿ, a generator needs **at least n** vectors.
- For Eⁿ, a basis has **exactly n** linearly-independent vectors.
- The **standard basis** of Eⁿ is e₁ = (1, 0, …, 0), e₂ = (0, 1, 0, …, 0), …, eₙ = (0, 0, …, 1).
1. In E²: u = (1, 0)ᵀ, v = (0, 1)ᵀ. Any x = (x₁, x₂)ᵀ = x₁·u + x₂·v. So {u, v} generates E². They are also linearly independent ⇒ they form a basis.
2. **Multiple decompositions of the same vector** (2, 5)ᵀ:
   - = 2·(1, 0)ᵀ + 5·(0, 1)ᵀ
   - = 2·(1, 1)ᵀ + 3·(0, 1)ᵀ
   - = 1·(1, 0)ᵀ + 1·(1, 1)ᵀ + 4·(0, 1)ᵀ
   - = 2·(1, 2)ᵀ + 1·(0, 1)ᵀ + 3·(0, 1)ᵀ
- 3. **Basis for E³**: e₁ = (1, 0, 0), e₂ = (0, 1, 0), e₃ = (0, 0, 1). The vector a = (2, 3, 4) has the unique representation a = 2e₁ + 3e₂ + 4e₃. ⭐
1. An *arbitrary* choice of u, v need not generate all of E² — they must be linearly independent (else they span only a line).
2. In E² we need **at least 2** vectors; in Eⁿ at least n.
3. The choice of generators is not unique — there are infinitely many spanning sets.

### ⚠️ Common Mistakes
- ❌ Picking two parallel vectors (one a scalar multiple of the other) and calling them a basis of E² → ✅ A basis must be linearly *independent*; parallel vectors span only a line, not the whole plane.

**Quick Recall:**
- **Span / Generate**: every vector in Eⁿ can be written as Σ cᵢ aᵢ.
- > - **Basis** = generators + linearly independent. ⭐
- dim(Eⁿ) = n; any basis has exactly n vectors.
- Builds on: 6.5 Vector Spaces, 6.6 Linear Dependence.
- Sets up: Unit 7 (representing systems of equations using basis vectors of Eⁿ).
- **Generator** ⭐: a set {u, v, w, …} such that every x = (x₁, x₂)ᵀ can be expressed as x = c₁u + c₂v + c₃w + … for suitable scalars cᵢ.
- **Sub-space** ⭐: W is a sub-space of V iff (a) W ⊆ V and (b) W is itself a vector space (i.e. satisfies all the V-space axioms).
- **Vector space (over ℝ)** ⭐: the set V = {(x₁, …, xₙ) : xᵢ ∈ ℝ} satisfying:
- **Vector** ⭐: an ordered set (a, b) with a, b as elements; "ordered" means (a, b) ≠ (b, a) generically.

### ⚠️ Common Mistakes
- ❌ Trusting printed numerical answers blindly → ✅ Always recompute the inner product / norm from the formulas (Σ aᵢbᵢ and √Σ aᵢ²) — printed answers in this textbook are occasionally inconsistent.
---

### 6.11 Exercises (worked-out problems) 🔴
- (i) a = (0, 2, 1): ‖a‖² = 0 + 4 + 1 = **5**.
- (ii) b = (6, 3, 2): ‖b‖² = 36 + 9 + 4 = **49**.
- (iii) c = (−5, 4, 3): ‖c‖² = 25 + 16 + 9 = **50**.
- (iv) d = (0, 0, 1): ‖d‖² = 0 + 0 + 1 = **1**.
- (v) e = (−3, −4, −2): ‖e‖² = 9 + 16 + 4 = **29**.
- **∂(b'x)/∂x = b = (3, −2, 1)ᵀ.** ⭐
| ∂y/∂x | ∂/∂x₁ | ∂/∂x₂ |
|-------|-------|-------|
| y₁    | 2x₁  | 3 |
| y₂    | 2x₂  | 2x₁ − 1 |
| y₃    | 2 + x₂ | x₁ − 6x₂ |
| y₄    | 6x₁ − 2x₁x₂ | −x₁² − 3x₂² |
- ∂(x'Ay)/∂x = A·y.
- ∂(x'Ay)/∂y = A'·x.
- Source's "Ans": A·y = (3y₁ − y₃, 2y₁ + y₂ + 4y₃, −y₁ + 3y₃)ᵀ. ⭐

**Quick Recall:**
- > - **Linear dependence** ⇔ Σ cᵢxⁱ = 0 with not-all-zero cᵢ. ⭐
- > - **Generators** of Eⁿ: at least n vectors; **basis** = exactly n linearly-independent vectors. ⭐
- **Standard basis of Eⁿ**: {e₁, …, eₙ}.
- > - **Bilinear-form derivatives**: ∂(b'x)/∂x = b; ∂(x'Ay)/∂x = A·y; ∂(x'Ay)/∂y = A'·x. ⭐
- In Eⁿ: dim = n; every basis has exactly n vectors.
- Closes Unit 6.
- Bridges into Unit 7 (eigenvalue problem on n×n matrices uses Eⁿ vectors and basis representation).

### 7.2 Vectors and Matrices (matrix representation of linear systems) 🔴
- **Coefficient matrix A** (m×n): A = [aᵢⱼ]; row i = coefficients of equation i; column j = coefficients of variable xⱼ across all equations.
- **Variable vector X** (n×1): X = (x₁, x₂, …, xₙ)ᵀ.
- **Constant vector d** (m×1): d = (d₁, d₂, …, dₘ)ᵀ.
- 6x₁ + 3x₂ + x₃ = 22
- x₁ + 4x₂ − 2x₃ = 12
- 4x₁ − x₂ + 5x₃ = 10
- Builds on: Unit 5 §5.3 (matrix arithmetic) and §5.7 Cramer's rule worked examples.
- Sets up: 7.3 (when AX = λX — the eigenvalue problem).

### 7.3 Characteristic Value Problem 🔴
- **Eigen value (characteristic value, characteristic root, proper value) λ** ⭐: scalar satisfying Ax = λx for some x ≠ 0.
- **Eigen vector (characteristic vector) x** ⭐: a non-zero x with Ax = λx.
- **Characteristic matrix** ⭐: the matrix [A − λI].
- Builds on: Unit 5 (rank, determinants, AX = d).
- Sets up: 7.3.1 (turning the eigen problem into a polynomial equation in λ).

### 7.3.1 Characteristic Equation 🔴
- **Characteristic polynomial** ⭐: the determinant |A − λI| viewed as a polynomial in λ.
- **Characteristic equation** ⭐: |A − λI| = 0.
1. Form A − λI (subtract λ from each diagonal entry of A).
2. Compute the determinant |A − λI|.
3. Set it to 0 and solve the resulting polynomial in λ.
4. The n roots are the eigen values λ₁, …, λₙ.
- This is a **quadratic** in λ. ⭐
- Builds on: Unit 5 — determinants, rank, homogeneous systems.
- Sets up: 7.3.2 (sum/product of roots gives quick checks).

### 7.3.2 Sum and Product of Roots 🔴
- Sum of eigen values = **trace(A)** = Σ aᵢᵢ. ⭐
- Product of eigen values = **|A|** (the determinant). ⭐
- c₀ = 1.
- c₁ = −Σᵢ aᵢᵢ = −trace(A). [So Σλᵢ = −c₁/c₀ = trace(A).]
- cⱼ = (−1)^j · (sum of all principal minors of A of order j).
- cₙ = (−1)^n · |A|. [So Πλᵢ = cₙ/c₀ · (−1)^n compensation = |A|.]
| Identity | Statement | Use |
|----------|-----------|-----|
| Σ λᵢ = trace(A) | sum of all eigen values = sum of diagonal entries | sanity-check eigen-value computations |
| Π λᵢ = |A|     | product of all eigen values = determinant | catches sign errors |
- i. If A is **singular** (|A| = 0), then at least one eigen value of A is 0. ⭐
- ii. If A is **real symmetric**, all eigen values are real (no complex roots). ⭐

### ⚠️ Common Mistakes
- ❌ Forgetting to subtract λ on **every** diagonal element of A → ✅ A − λI has λ subtracted from each diagonal entry, off-diagonal entries unchanged.

**Quick Recall:**
- > - **Σ λᵢ = trace(A)** and **Π λᵢ = |A|**. ⭐
- Real-symmetric ⇒ real eigen values; diagonal/triangular ⇒ eigen values are diagonal entries.
- λ(A⁻¹) = 1/λ(A); λ(A^k) = λ(A)^k.
- Builds on: 7.3.1 (the polynomial whose coefficients these identities use).
- Sets up: 7.3.3 (using each λᵢ to find the matching eigen vector).

### 7.3.3 Characteristic Vector 🔴
1. For each λᵢ, form A − λᵢI.
2. Solve (A − λᵢI)·xⁱ = 0 — a homogeneous system with infinitely many solutions.
3. Pick any non-zero solution; **normalise** if desired so ‖xⁱ‖ = 1.
- **Note**: ⟨x¹, x²⟩ = 1/2 − 1/2 = 0 ⇒ the two eigen vectors are **orthogonal**. ⭐ (This is a general property of real symmetric matrices — confirmed in 7.3.4.)

### ⚠️ Common Mistakes
- ❌ Reading "xⁱ" as "x raised to power i" → ✅ Here the superscript is just a label for the i-th eigen vector, **not** an exponent.

**Quick Recall:**
- Solve (A − λI)x = 0 for each eigen value λ to get its eigen vector(s).
- Eigen vectors are determined only up to a non-zero scalar multiple.
- Normalise: divide by ‖x‖ so the length is 1.
- > - For real symmetric A, eigen vectors of distinct eigen values are orthogonal. ⭐
- Builds on: Unit 5 §5.3.7 (rank and homogeneous systems with non-trivial solutions when |A − λI| = 0).
- Sets up: 7.3.4 Diagonalisation.

### 7.3.4 Diagonalisation (introduction) 🔴
- Builds on: 7.3.3 (eigen vectors), 5.3.5 (orthogonal matrices: AᵀA = I, |A| = ±1).
- Sets up: 7.4 Linear Independence of Eigen Vectors and 7.5 Quadratic Forms.
1. What guarantees that the eigen vectors of a non-symmetric real matrix can still form a basis (i.e. that A is diagonalisable)? (Answer: all eigen values must be distinct, or each repeated eigen value must have geometric multiplicity equal to its algebraic multiplicity — covered next chunk.)

### 7.3.4 Diagonalisation (worked) 🔴
1. Form P = [x¹  x²] = | 1/√2  1/√2 ; 1/√2  −1/√2 |.
- 2. Verify orthogonality: PᵀP = I ⇒ P is **orthogonal**. ⭐
3. Compute PᵀAP:
- **Diagonalisation** ⭐: PᵀAP = Λ where P is orthogonal (columns = normalised eigen vectors) and Λ is diagonal with eigen values.

**Quick Recall:**
- > - Real-symmetric A ⇒ A is **orthogonally diagonalisable**: PᵀAP = Λ. ⭐
- Λ's diagonal entries are the eigen values; P's columns are the corresponding orthonormal eigen vectors.
- Builds on: 7.3.3 (eigen vectors), 5.3.5 (orthogonal matrices).
- Sets up: 7.4 Linear independence of eigen vectors, 7.5 Quadratic forms, 7.6 Definiteness.

### 7.4 Linear Independence of Eigen Vectors 🔴
| Fact | Statement |
|------|-----------|
| Distinct ⇒ independent | λ₁, …, λₙ all distinct ⇒ x¹, …, xⁿ are linearly independent. ⭐ |
| Distinct ⇒ orthogonal (real symmetric) | If two eigen values are distinct, the corresponding eigen vectors of a real symmetric matrix are orthogonal. ⭐ |
- Repeated eigen values do *not* automatically prevent the existence of n linearly independent eigen vectors (e.g. the n×n identity matrix I has the single eigen value 1 of multiplicity n but every basis of Eⁿ is a set of eigen vectors for I).
- When repeated roots admit fewer than the multiplicity in independent eigen vectors, A is **defective** (not diagonalisable) — but this case is beyond Unit 7.

**Quick Recall:**
- > - Distinct eigen values ⇒ independent eigen vectors (sufficient, not necessary). ⭐
- > - Real symmetric + distinct eigen values ⇒ orthogonal eigen vectors. ⭐
- Builds on: 6.6 (linear independence), 7.3.3 (eigen vectors).
- Sets up: 7.3.4 generalised — n independent eigen vectors fill the columns of P for diagonalisation.

### 7.5 Quadratic Forms 🔴
- **Quadratic form (2 variables)**: Q(x₁, x₂) = a₁₁x₁² + 2a₁₂x₁x₂ + a₂₂x₂² ⭐ (note the **2a₁₂** captures the off-diagonal symmetry — half the coefficient sits in each off-diagonal entry).
- **Quadratic form (n variables)** ⭐: Q(x) = x'Ax = Σᵢ Σⱼ aᵢⱼ xᵢxⱼ for a symmetric A.
- **Positive definite (PD)** ⭐: Q(x) > 0 ∀ x ≠ 0.
- **Positive semi-definite (PSD)** ⭐: Q(x) ≥ 0 ∀ x.
- **Negative definite / semi-definite**: same with reversed inequality.
- **Indefinite**: Q takes both positive and negative values for different x.
1. Q(x₁, x₂) = x₁² − 4x₁x₂ + 4x₂² = **(x₁ − 2x₂)²** ≥ 0. Hence Q ≥ 0 for all x — **positive semi-definite** (zero on the line x₁ = 2x₂, positive elsewhere).
2. Q(x₁, x₂) = −10x₁² + 6x₁x₂ − x₂² = −x₁² − (3x₁ − x₂)² ≤ 0. **Negative semi-definite**.
- a₁₁ > 0 AND
- (a₁₁a₂₂ − a₁₂²) / a₁₁ > 0, i.e. a₁₁a₂₂ − a₁₂² > 0 (the **determinant of A** is positive). ⭐
| Sign of a₁₁ | Sign of |A| = a₁₁a₂₂ − a₁₂² | Definiteness |
|-------------|--------------------------------|--------------|
| > 0         | > 0                            | Positive definite |
| ≥ 0         | = 0                            | Positive semi-definite |
| < 0         | > 0                            | Negative definite |
| ≤ 0         | = 0                            | Negative semi-definite |
| any         | < 0                            | Indefinite |

### ⚠️ Common Mistakes
- ❌ Treating "2a₁₂x₁x₂" as if both off-diagonal entries equal 2a₁₂ → ✅ A is symmetric with a₁₂ = a₂₁, and the cross term in Q expands to **2** a₁₂ x₁x₂ (one from each off-diagonal entry).

**Quick Recall:**
- > - Q(x) = x'Ax with A symmetric. ⭐
- PD (2×2): a₁₁ > 0 AND |A| > 0.
- PSD (2×2): a₁₁ ≥ 0 AND |A| = 0.
- ND (2×2): a₁₁ < 0 AND |A| > 0.
- Indefinite: |A| < 0.
- Builds on: 5.3.5 (symmetric matrices).
- Sets up: 7.6 (eigen-value criterion for definiteness).

### 7.6 Definiteness and Eigen Values 🔴
- **Positive definite** ⇔ all λᵢ > 0.
- **Positive semi-definite** ⇔ all λᵢ ≥ 0 (and at least one = 0 ⇔ |A| = 0).
- **Negative definite** ⇔ all λᵢ < 0.
- **Negative semi-definite** ⇔ all λᵢ ≤ 0.
- **Indefinite** ⇔ A has eigen values of both signs.
| Definiteness | Necessary & sufficient (matrix) | In terms of eigen values |
|--------------|-----------------------------------|---------------------------|
| Positive semi-definite | a₁₁ ≥ 0 AND |A| = 0 | λ₁ ≥ 0 AND λ₂ ≥ 0 |
| Negative semi-definite | a₁₁ ≤ 0 AND |A| = 0 | λ₁ ≤ 0 AND λ₂ ≤ 0 |
| Positive definite | a₁₁ > 0 AND |A| > 0 | λ₁ > 0 AND λ₂ > 0 ⭐ |
| Negative definite | a₁₁ < 0 AND |A| > 0 | λ₁ < 0 AND λ₂ < 0 |
| Indefinite | |A| < 0 | λ₁ and λ₂ have opposite signs |

### ⚠️ Common Mistakes
- ❌ Reading "all eigen values positive" off the diagonal of A directly → ✅ Diagonal entries are *not* eigen values unless A is itself diagonal/triangular; you must solve |A − λI| = 0.

**Quick Recall:**
- > - Sign of eigen values ⇒ definiteness of Q. ⭐
- PD ⇔ all λ > 0; ND ⇔ all λ < 0; PSD/NSD allow zero; indefinite ⇔ mixed signs.
- Builds on: 7.3.4 (diagonalisation explains *why* the eigen values determine the form's sign).
- Sets up: optimisation (Hessian definiteness ↔ local max/min/saddle).

### 7.7 Vector Differentiation 🔴
- Builds on: Block 1 partial differentiation; 7.5 Quadratic forms.

### 7.7.1 Vector Differentiation of a Linear Function 🔴
- **∂(a'x)/∂x = a.** ⭐

**Quick Recall:**
- > - **∂(a'x)/∂x = a**. ⭐ — the gradient of a linear function is its coefficient vector.

### 7.7.2 Vector Differentiation of a Vector of Functions 🔴
| ∂y/∂x  | y₁     | y₂     | …  | yₙ     |
|--------|--------|--------|----|--------|
| ∂/∂x₁  | ∂y₁/∂x₁ | ∂y₂/∂x₁ | …  | ∂yₙ/∂x₁ |
| ∂/∂x₂  | ∂y₁/∂x₂ | ∂y₂/∂x₂ | …  | ∂yₙ/∂x₂ |
| ⋮      | ⋮      | ⋮      | ⋱  | ⋮      |
| ∂/∂xₘ  | ∂y₁/∂xₘ | ∂y₂/∂xₘ | …  | ∂yₙ/∂xₘ |
| ∂y/∂x  | y₁ = x₁² + 2x₂² − 3x₁x₃ | y₂ = 3x₁x₂² − x₂² + 4x₂x₃² |
|--------|--------------------------|-----------------------------|
| ∂/∂x₁  | 2x₁ − 3x₃               | 3x₂²                       |
| ∂/∂x₂  | 4x₂                     | 6x₁x₂ − 2x₂ + 4x₃²         |
| ∂/∂x₃  | −3x₁                    | 8x₂x₃                      |

**Quick Recall:**
- For y(x) of dimension n with x of dimension m: ∂y/∂x is an **m×n Jacobian** of partial derivatives.
- This is the multivariate generalisation of the chain rule's "rate of change of each output w.r.t. each input".

### 7.7.3 Vector Differentiation of a Quadratic Form 🔴
- **∂(x'Ax)/∂x = 2Ax = 2x'A.** ⭐ (The two forms differ only in row-vs-column orientation.)
- ∂/∂x₁ = 6x₁ + 2x₂ − 4x₃ ✓ (matches 2(Ax)₁).
- ∂/∂x₂ = 2x₁ + 6x₃.
- ∂/∂x₃ = 4x₃ − 4x₁ + 6x₂ = −4x₁ + 6x₂ + 4x₃.
- So ∂(x'Ax)/∂x = 2Ax. ⭐

**Quick Recall:**
- > - **∂(x'Ax)/∂x = 2Ax** (or equivalently 2x'A). ⭐
- Mirrors the scalar fact d(ax²)/dx = 2ax.

### 7.7.4 Vector Differentiation of a Bi-linear Form 🔴
| Derivative | Result |
|------------|--------|
| ∂(x'Bz)/∂x | **Bz** ⭐ |
| ∂(x'Bz)/∂z | **B'x** ⭐ |

**Quick Recall:**
- > - **∂(x'Bz)/∂x = Bz**, **∂(x'Bz)/∂z = B'x**. ⭐
- Compare 7.7.1: a'x is bilinear in (a, x) — these formulas reduce to ∂(a'x)/∂x = a when B is replaced by a column.
- Builds on: 7.7.1 (linear case).
- Sets up: optimisation problems with separate primal-dual variables.
- **Characteristic equation** ⭐: For an n×n A, the equation |A − λI| = 0; the LHS expanded is the **characteristic polynomial**, an n-th degree polynomial in λ. Its roots are the eigen values.
- **Eigen value & eigen vector** ⭐: λ and x ≠ 0 with **Ax = λx**.
- **Quadratic form** ⭐: a₁₁x₁² + 2a₁₂x₁x₂ + a₂₂x₂² for given constants a₁₁, a₁₂, a₂₂ and real variables x₁, x₂. (Generalises to Q(x) = x'Ax for n variables.)
- 2. For a = (2a, −a, 3a, a)ᵀ: a'x = 2ax₁ − ax₂ + 3ax₃ + ax₄; partials are (2a, −a, 3a, a) which equals a. ⭐ This **proves ∂(a'x)/∂x = a** for this specific a, illustrating the general rule.
- These are the rows of 2Ax (= the entries of 2x'A reading as a row), confirming **∂(x'Ax)/∂x = 2x'A = 2Ax**. ⭐

**Quick Recall:**
- > - **AX = d** is the matrix form of any linear system. ⭐
- > - **Ax = λx** ⇒ |A − λI| = 0 (characteristic equation). ⭐
- > - **Σλᵢ = trace A**, **Πλᵢ = |A|**. ⭐
- > - PD ⇔ all λ > 0; ND ⇔ all λ < 0; indefinite ⇔ mixed sign of λ. ⭐
- > - **∂(a'x)/∂x = a**, **∂(x'Ax)/∂x = 2Ax**, **∂(x'Bz)/∂x = Bz, ∂(x'Bz)/∂z = B'x**. ⭐

### 8.2 System of Linear Equations — 8.2.1 Linear Equation 🔴
- Each variable has degree ≤ 1.
- At least one variable has degree exactly 1.
- The coefficient of at least one degree-1 variable is non-zero.
- 7x = 4 (one variable, two constants 7 and 4).
- a₁x₁ = b₁ (one variable, two parameters a₁ and b₁).
- a₁x₁ − 5x₂ = 11 (two variables x₁, x₂; parameter a₁; two constants −5 and 11).
- Builds on: high-school linear-equation algebra; 7.2 (matrix form).
- Sets up: 8.2.2 (solution of a linear equation), 8.2.3 (solution of a system).
1. When does a homogeneous system Ax = 0 have a non-trivial solution? (Answered in 8.2.4: when rank(A) < n.)

### 8.2.2 Solution of a Linear Equation 🔴
- is a set of n constant real (or complex) values c₁, c₂, …, cₙ such that, when each variable xⱼ is replaced by the corresponding constant cⱼ, the LHS equals b. ⭐
- Sets up: 8.2.3 — "system of equations" requires the *same* tuple to solve every equation in the set.

### 8.2.3 System of Linear Equations 🔴
- **System of m linear equations in n variables** ⭐: m simultaneous linear equations
- 3x + 4y = 4 … (II)
- 6x + y = 8 … (III)
- 2·(II) − (III): 6x + 8y − 6x − y = 8 − 8 ⇒ **7y = 0 ⇒ y = 0**.
- Substitute back into (II): 3x = 4 ⇒ **x = 4/3**.
- The unique system-solution is (x, y) = (4/3, 0).
- Builds on: 8.2.2 (single-equation solution).
- Sets up: 8.2.4 (homogeneous case), 8.3 (matrix form).

### 8.2.4 System of Homogeneous Linear Equations 🔴
- **Homogeneous linear system** ⭐: aᵢ₁x₁ + … + aᵢₙxₙ = 0 for every i = 1, …, m. Equivalently AX = **0**.
- **Trivial solution** ⭐: xⱼ = 0 ∀ j. Always exists for any homogeneous system.
- **Non-trivial solution** ⭐: a solution with at least one xⱼ ≠ 0. May or may not exist.

**Quick Recall:**
- Homogeneous ⇔ all bᵢ = 0.
- Trivial solution **always** exists.
- > - Non-trivial exists iff rank(A) < n (i.e. iff |A| = 0 in the square case). ⭐
- Builds on: 8.2.3 (general system).
- Sets up: 8.6 (consistency), Block 1 §5.3.7 (rank), Unit 7 (eigen value problem = homogeneous (A − λI)x = 0).

### 8.3 Representation of a System as a Matrix Equation 🔴
1. **Matrix equation**: AX = B, where A is m×n (coefficients), X is n×1 (variables), B is m×1 (constants).
2. **Augmented matrix [A | B]**: pack A and B together into a single m × (n + 1) matrix; the variable column is implicit.
- **Matrix equation form** ⭐: AX = B with A (m×n), X (n×1), B (m×1).
- **Augmented matrix** ⭐: [A | B] — A and B side-by-side with a vertical bar separator; an m × (n+1) matrix that uniquely encodes the system.
- 3x + y + 2z = 11 … (Eq. 1)
- x + 2y − 2z = −1 … (Eq. 2)
- 2x − 2y − z = −5 … (Eq. 3)
- Solution by elimination: **x = 1, y = 2, z = 3**. ⭐ (Used as the running example throughout §8.3–8.5.)
- Builds on: 7.2 (matrix form was previewed there).
- Sets up: 8.4 (elementary row operations on (E) preserve the solution set).

### 8.4 Elementary Row Operations & Unchanged Solution Set 🔴
| ERO | Symbol | Effect on system |
|------|--------|-------------------|
| (i) Row swap | Rᵢ ↔ Rⱼ | Reorders equations — clearly preserves solutions |
| (ii) Row scaling | Rᵢ → k Rᵢ (k ≠ 0) | Multiplies an equation through by k — same solution set |
| (iii) Row replacement | Rᵢ → Rᵢ + k Rⱼ | Adds k times another equation to this one — same solution set |

**Quick Recall:**
- Three EROs: swap, scale (×k ≠ 0), replace (Rᵢ + k Rⱼ).
- > - Each preserves the solution set. ⭐

### 8.4.1 Worked example — EROs solve the running system 🔴
- From R₃: **z = 3**.
- From R₂: −5y + 8(3) = 14 ⇒ −5y = 14 − 24 = −10 ⇒ **y = 2**.
- From R₁: x + 2(2) − 2(3) = −1 ⇒ x + 4 − 6 = −1 ⇒ **x = 1**.

### ⚠️ Common Mistakes
- ❌ Forgetting to apply EROs **simultaneously** to A and B (when not using the augmented form) → ✅ Either always work on the augmented matrix [A | B], or change A and B in lock-step.
- ❌ Multiplying a row by 0 → ✅ ERO (ii) requires k ≠ 0; multiplying by 0 destroys information about that equation.

**Quick Recall:**
- Drive [A | B] to **upper-triangular** by EROs, then back-substitute.
- Pivot strategy: zero everything below the leading 1 in each column.
- Builds on: 5.3.6 elementary operations / row reduction (introduced informally in Unit 5); 8.4 EROs.
- Sets up: 8.5 (which equations carry "new information" vs are redundant linear combinations of the others).

### 8.5 Linear Independence and System of Equations — 8.5.1 Linear Combination and Dependence of Equations 🔴
- **Linear combination of equations**: Eq. k = Σⱼ≠k λⱼ Eq. j for some scalars λⱼ. ⭐
- **Linearly dependent set of equations** ⭐: at least one equation in the set is a linear combination of the others.
- **Linearly independent set of equations** ⭐: no equation can be expressed as a linear combination of the others.
- 2·(3x + y + 2z) + 3·(x + 2y − 2z) = 2·11 + 3·(−1) ⇒ **9x + 8y − 2z = 19** … (Eq. 4)
- (Eq. 1) − 3·(Eq. 2): −5y + 8z = 14 ⇒ **y = (8z − 14)/5**. … (Q)
- (Eq. 2) − 2·(Eq. 1): −5x − 6z = −23 ⇒ **x = (23 − 6z)/5**. … (R)
- Pick any z; then x and y are determined. Infinitely many solutions, parametrised by z. ⭐

**Quick Recall:**
- > - Eq. k = linear combination of others ⇒ **redundant**. ⭐
- Augmented-matrix test: ERO produces an all-zero row ⇒ that equation was redundant.
- > - m < n linearly-independent equations in n variables ⇒ **infinitely many solutions**. ⭐
- Builds on: 6.6 (linear independence of vectors); the equations correspond to row-vectors of the augmented matrix.
- Sets up: 8.5.2 (independence test), 8.6 (consistency), 8.7 (rank-based criteria).

### 8.5.2 Linear Independence of m Equations in n Variables (m ≤ n) 🔴
- **Linearly dependent set of m equations (m ≤ n)**: ∃ j with 1 ≤ j ≤ m such that Eq. j is a linear combination of the rest. ⭐
- **Linearly independent set of m equations (m ≤ n)**: for **no** j is Eq. j a linear combination of the rest. ⭐
- > **In the augmented-matrix representation of the system, while attempting to drive elements below the main diagonal to zero, if you obtain a row of all zeros, the equations are linearly dependent. Otherwise the set is linearly independent.** ⭐
- No row is all-zero ⇒ the three equations of (C) are **linearly independent** ⇒ unique solution exists (and we found it: x=1, y=2, z=3). ⭐
- **If a set of n equations in n variables has some equation that is a linear combination of (i.e. linearly dependent on) the remaining equations, then the number of solutions is infinite.** ⭐
- **If a system has m equations in n variables with m < n, then the number of solutions is infinite.** ⭐
- Theorem B: an n×n system loses rank to (n−1) when an equation is a combination of others ⇒ rank(A) = n − 1 < n ⇒ infinite solutions.
- Theorem C: m < n means at most m linearly-independent equations among n unknowns ⇒ at least one variable is free ⇒ infinitely many solutions (or none, if inconsistent — see 8.6).

**Quick Recall:**
- > - **All-zero row in row-reduced augmented matrix ⇔ a linear combination ⇔ dependent**. ⭐
- n equations in n variables with one redundant ⇒ infinite solutions. (Theorem B)
- m < n equations in n variables ⇒ infinite solutions (when consistent). (Theorem C)
- Builds on: 6.6 (linear independence), 5.3.7 (rank).
- Sets up: 8.6 (consistency: does a solution exist *at all*?) and 8.7 (rank of A vs rank of [A | B]).

### 8.6 Consistency of a System of m Linear Equations in n Variables (introduction) 🔴
- **Consistent system** ⭐: a system that has at least one solution.
- **Inconsistent system** ⭐: a system with **no** solution (the equations contradict each other).
- 4x − 3y + 2z = −2 … (Eq. 5)

**Quick Recall:**
- m > n ⇒ ask **consistency** (does a solution exist?), not just independence.
- > - Inconsistent ⇔ a row of [A | B] reduces to (0, 0, …, 0 | non-zero) — i.e. 0 = (non-zero), a contradiction. ⭐
- **Rank test** (covered next): consistent ⇔ rank(A) = rank([A | B]).
- Builds on: 8.5 (independence), 5.3.7 (rank).
- Sets up: 8.6 (continued in chunk 008), 8.7 (rank-based solution criteria), 8.8 (span / basis / dimension).
1. For a given inconsistent system (rank(A) < rank([A | B])), what is the closest x in the least-squares sense? (Beyond the unit; previewed in regression problems.)

### 8.6 Consistency of m Linear Equations in n Variables (concluded) 🔴
- Substitute into (Eq. 5): LHS = 4(1) − 3(2) + 2(3) = 4 − 6 + 6 = **4** ≠ −2 = RHS.
- Hence (Eq. 5) is **violated** by (1, 2, 3); no triple satisfies all four equations simultaneously.
- LHS = 4(1) − 3(2) + 2(3) = 4 − 6 + 6 = **4** = RHS ✓.
- **Consistent system (with m > n)** ⭐: a solution exists.
- **Inconsistent system (with m > n)** ⭐: no solution exists.
1. A system with m ≤ n is **necessarily consistent** when the equations are independent; the question of consistency really only arises when m > n. *(Caveat: consistency can still fail for m ≤ n if equations are contradictory, but the typical phrasing in this book reserves the term for m > n cases.)*
2. Any over-determined system (m > n) is either **consistent and linearly dependent** (the extra equations are combinations of the others), or **inconsistent and linearly independent** (the extra equations contradict).
- > **In the augmented matrix, perform EROs until elements below the main diagonal are zeroed. If any row reduces to (0, 0, …, 0 | K) with K ≠ 0, the system is INCONSISTENT (because that row says 0 = K ≠ 0). If, instead, every row of zeros to the left of the bar has K = 0, the system is CONSISTENT.** ⭐

### ⚠️ Common Mistakes
- ❌ Stopping at the first all-zero row and concluding consistency → ✅ A row of (0, …, 0 | K) with K = 0 is fine; with K ≠ 0 it is the smoking gun for inconsistency. **Check the value to the right of the bar**.

**Quick Recall:**
- **Test**: row-reduce [A | B]; look for (0, …, 0 | K) rows.
- K = 0 ⇒ row is redundant (no information lost) — system can still be consistent.
- >   - K ≠ 0 ⇒ system is **INCONSISTENT**. ⭐
- m ≤ n linearly-independent equations ⇒ always consistent.
- m > n consistent ⇒ extra equations are linear combinations (linearly dependent system).
- m > n inconsistent ⇒ extra equations are independent and contradict the others.
- Builds on: 8.4 EROs, 8.5 dependence/independence.
- Sets up: 8.7 (rank-based solution criteria — the same test, packaged via rank(A) vs rank([A|B])).

### 8.7 Rank of a Matrix and Solution of a System 🔴
- The rank of A and the rank of the augmented [A | B] together fully determine the solution-existence and uniqueness of AX = B. The three cases form an exhaustive classification ⭐:
| Rank condition | Solution structure |
|----------------|---------------------|
| **rank(A) = rank([A | B]) = n (= number of variables)** | **Unique solution** |
| **rank(A) = rank([A | B]) < n** | **Infinitely many solutions** (with (n − rank) free parameters) |
| **rank(A) < rank([A | B])** | **Inconsistent** — no solution |
- **Rank of a matrix** ⭐: the order of the largest non-zero minor; equivalently, the maximum number of linearly independent rows (or columns).
- A theorem of linear algebra: **row-rank = column-rank**, so rank is well-defined.

**(i) Unique solution: system (C)**
- rank(A) = 3 (three non-zero rows on the LHS), rank([A | B]) = 3, n = 3 ⇒ **rank(A) = rank([A | B]) = n = 3** ⇒ **unique** solution (1, 2, 3). ⭐

**(ii) Infinitely many: system (F) (the redundant 4th equation case)**
- rank(A) = 2 = rank([A | B]) < n = 3 ⇒ **infinite solutions**, parametrised by one free variable (e.g. z). ⭐

**(iii) Inconsistent: system (H) (the contradictory 5th equation)**
- rank(A) = 3, rank([A | B]) = 4 ⇒ rank(A) < rank([A | B]) ⇒ **no solution**. ⭐
1. If **rank(A) = rank([A | B]) = m** (the number of equations), the system has a **unique** solution. *(Rephrasing — when m = n: unique; when m < n: infinite.)*
2. If **rank(A) = rank([A | B]) < m**, the system has **infinite** solutions.
3. If **rank(A) < rank([A | B])**, the system is **inconsistent**, i.e. no solution.

### ⚠️ Common Mistakes
- ❌ Computing rank only on the coefficient block A and concluding consistency → ✅ Always compute rank of *both* A and [A | B]; consistency requires them to be **equal**.

**Quick Recall:**
- > - **Unique** ⇔ rank(A) = rank([A|B]) = n. ⭐
- > - **Infinite** ⇔ rank(A) = rank([A|B]) < n. ⭐
- > - **No solution** ⇔ rank(A) < rank([A|B]). ⭐
- Builds on: 5.3.7 (rank), 8.4 (EROs), 8.6 (consistency).
- Sets up: 8.8 (span / basis / dimension — vectors view of the same algebra).
- **Linear combination of vectors** ⭐: V = λ₁V₁ + λ₂V₂ + … + λₖVₖ for some scalars λⱼ.
- **Linearly dependent set of vectors** ⭐: ∃ scalars λⱼ, not all zero, with Σ λⱼ Vⱼ = **0**.
- **Linearly independent set of vectors** ⭐: Σ λⱼ Vⱼ = **0** ⇒ every λⱼ = 0.
- **Span of {V₁, …, Vₖ}** ⭐: the set of *all* vectors expressible as Σ λⱼ Vⱼ — also called the **vector space generated by the set**.
- **Basis of a vector space** ⭐: a *maximal* linearly-independent subset.
- **Dimension of a vector space** ⭐: the number of vectors in *any* basis (well-defined: all bases have the same size).
- The **rank** of A (= dim of column-span = dim of row-span) is the count of independent equations. ⭐

**Quick Recall:**
- > - Each equation ↔ one (n+1)-vector in ℝⁿ⁺¹. ⭐
- Span(V₁, …, Vₖ) = vector space generated by the set.
- Basis = maximal LI subset; dimension = its size.
- Dependence and consistency questions are *linear-algebra-on-row-vectors* questions.
- **Augmented matrix** ⭐: [A | B] formed by appending the constant column to A.
- **Consistent system (m > n)** ⭐: has at least one solution.
- **Inconsistent system (m > n)** ⭐: has no solution.
- **Linear equation** ⭐: each variable degree ≤ 1, at least one degree-1 with non-zero coefficient.
- **Linearly dependent system of equations** ⭐: some Eq. k is a linear combination of the others.
- **Linearly independent system of equations** ⭐: no Eq. k is a linear combination of the others.

**Quick Recall:**
- m ≤ n with full row-rank ⇒ consistent and independent.
- m > n consistent ⇒ at least one equation is a linear combination ⇒ system is dependent.
- m > n inconsistent ⇒ no row of the augmented matrix is a combination of the others ⇒ system is independent (in the row-vector sense), but the constants contradict.
- **(a) Linearly independent system**: e.g. x = 3 and 2x + y = 7 (two equations in two variables; neither is a multiple of the other) ⇒ unique solution (3, 1). ⭐
- **(b) Linearly dependent system**: e.g. x + 2y = 6 and 2x + 4y = 12 (the second is 2× the first) ⇒ they describe the same line; infinite solutions. ⭐
- **(c) Consistent system (m > n)**: e.g. {x + 2y = 8; 3x + 4y = 18; 5x + 3y = 19}. Solution (x, y) = **(2, 3)** satisfies all three ⇒ **consistent**, with one equation a linear combination of the other two. ⭐
- **(d) Inconsistent system (m > n)**: e.g. {x + 2y = 8; 3x + 4y = 18; 5x + 3y = 20}. The first two give (2, 3), but 5(2) + 3(3) = 19 ≠ 20 ⇒ **inconsistent**, no common solution. ⭐

**Quick Recall:**
- > - Three EROs preserve the solution set (Theorem A). ⭐
- All-zero augmented row ⇒ **redundant equation** (linear combination).
- > - (0, …, 0 | K ≠ 0) row ⇒ **inconsistent** (no solution). ⭐
- Rank classification: rank(A) = rank([A|B]) = n ⇒ unique; = n − k < n ⇒ ∞-many (k free); rank(A) < rank([A|B]) ⇒ no solution.
- > - m ≤ n equations: question is *independence*; m > n equations: question is *consistency*. ⭐
- Each equation ↔ a vector in ℝⁿ⁺¹; span/basis/dimension carry over directly.
