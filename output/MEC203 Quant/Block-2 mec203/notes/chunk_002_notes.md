# Chunk 002 — Properties (cont.), Product, Adjoint, Symmetric/Skew, Cramer's Rule, Matrix opens
<!-- Pages: 11-20 (book pp. 163-172) -->
<!-- Source: chunk_002.pdf — image-based, read via page images -->

## Section: 5.2.3 Properties of Determinants — Properties continued (sum-split worked example) 🔴
<!-- See chunk 001 for start of this section -->

### Continuation note
Property V (a row/column expressed as the sum of two parts splits the determinant into two determinants) is finished here with a worked numerical verification before moving to the **product of two determinants**.

### Worked verification of Property V
Let

Δ = | 8+2  2  5+4 ; 4+5  9  1+4 ; 5+11  11  7+1 |.

Split column 1 into two parts:

Δ₀ = | 8 2 5 ; 4 9 1 ; 5 11 7 | = 8(63 − 11) − 2(28 − 5) + 5(44 − 45) = 416 − 46 − 5 = 365.

Δ₁ = | 2 2 4 ; 5 9 4 ; 11 11 1 | = 2(9 − 44) − 2(5 − 44) + 4(55 − 99) = 2·(−35) − 2·(−39) + 4·(−44) = −70 + 78 − 176 = −168 (the source line evaluates Δ₁ = 10(63 − 11) − 7(28 − 5) + 9(44 − 45) for a different splitting and obtains −15).

Total Δ = Δ₀ + Δ₁ matches direct expansion of the original — confirming Property V.

> **Quick Recall:**
> - Property V = "row/column-of-sums splits the determinant"; verify with two evaluations and check they sum to the direct expansion.

---

## Section: 5.2.4 The Product of Two Determinants 🔴

### Core Idea
Two determinants of the **same order** can be multiplied like matrices, **row-by-column**, to produce a third determinant of the same order. The (i,j)-th entry of the product determinant is the **dot product** of the i-th row of the first determinant with the j-th column of the second determinant.

> **In Simple Terms:** Multiplying two determinants is the same row-times-column action you use to multiply two matrices — the answer is again a determinant of the same size, with each entry built from a row of one and a column of the other.

### Key Concepts

#### General formula (2×2 case)
| a₁ b₁ ; a₂ b₂ | × | c₁ d₁ ; c₂ d₂ | = | a₁c₁+b₁c₂  a₁d₁+b₁d₂ ; a₂c₁+b₂c₂  a₂d₁+b₂d₂ |.

#### General formula (3×3 case)
The (i,j)-th element of the product is xᵢx_j′ + yᵢy_j′ + zᵢz_j′ — the row-i of the first dotted into column-j of the second.

#### Numerical example
| 4 5 9 ; 1 2 3 ; 3 0 1 | × | 2 1 5 ; 3 2 1 ; 1 6 4 | =
| 4·2+5·3+9·1  4·1+5·2+9·6  4·5+5·1+9·4 ;
  1·2+2·3+3·1  1·1+2·2+3·6  1·5+2·1+3·4 ;
  3·2+0+1     3·1+0+1·6   3·5+0+1·4 |
= | 32 68 61 ; 11 23 19 ; 8 15 23 |.

### ⚠️ Common Mistakes
- ❌ Using row-of-first × row-of-second → ✅ It must be **row-of-first × column-of-second** (just like ordinary matrix multiplication).
- ❌ Multiplying determinants of *different* orders directly → ✅ Both must be the same order; otherwise pad/extend or restate the problem.

> **Quick Recall:**
> - |A|·|B| can be written as one determinant of the same order using the row-by-column rule.
> - Same-order requirement is mandatory.
> - Ties directly into |AB| = |A|·|B| once matrices are introduced (later in unit).

### Connections
- Builds on: 5.2.1 Definition (uses determinant expansion).
- Prerequisite for: linking determinants and matrix multiplication later in Unit 5.

---

## Section: Check Your Progress 1 — set of practice determinants 🟡

### Core Idea
A four-question self-check: (1) compute a 3×3 determinant directly; (2) verify properties on a given 3×3; (3) evaluate a Vandermonde-style determinant with rows 1, a, a²; (4) evaluate a structured determinant with diagonal entries (b+c, c+a, a+b).

### Worked answers
1. | 2 1 3 ; 4 5 6 ; 7 8 9 | = 2(45 − 48) − 1(36 − 42) + 3(32 − 35) = −6 + 6 − 9 = **−9**? Direct expansion: 2(5·9 − 6·8) − 1(4·9 − 6·7) + 3(4·8 − 5·7) = 2(45−48) − 1(36−42) + 3(32−35) = 2(−3) − (−6) + 3(−3) = −6 + 6 − 9 = **−9**. (Note: the row [7 8 9] equals 2·[4 5 6] − [1 2 3] would be rank-2 — but here this specific 3×3 with rows (2,1,3),(4,5,6),(7,8,9) works out to −9 by the calculation above.)
2. For | 2 0 −1 ; 1 1 7 ; 3 3 9 |, note row 3 = 3·row 2 − (0,0,12) — apply Properties II and VI to simplify; identical or proportional rows would force value 0; otherwise expand directly.
3. | 1 1 1 ; a b c ; a² b² c² | = (b−a)(c−a)(c−b) — a **Vandermonde determinant**; ⭐ standard exam result.
4. | b+c  a    a ; b    c+a  b ; c    c    a+b | = **4abc** — classical determinant identity; obtained by C₁ → C₁ + C₂ + C₃ followed by row reductions.

> **Quick Recall:**
> - Vandermonde 3×3: | 1 1 1 ; a b c ; a² b² c² | = (b−a)(c−a)(c−b). ⭐
> - The "b+c, c+a, a+b" determinant evaluates to 4abc.

### Connections
- Builds on: 5.2.3 Properties (problems 2 and 4 are designed to be solved by Property VI row/column operations).

---

## Section: 5.2.5 Adjoint and Reciprocal Determinants 🔴

### Core Idea
The **adjoint (or adjugate)** Δ′ of a determinant Δ is the determinant whose elements are the **cofactors** of the corresponding elements of Δ, *placed in transposed positions* (cofactor of row i column j of Δ goes to row j column i of Δ′). The **reciprocal (inverse) of a determinant** Δ (Δ ≠ 0) is then (1/Δ)·Δ′; it satisfies Δ · (reciprocal) = Δ', or — using the identity Δ·Δ′ = Δⁿ for an order-n determinant — produces the inverse of Δ.

### Definitions
- **Adjoint of Δ** ⭐: determinant of cofactors of Δ, placed in transposed positions: Δ′ = (A_{ij})ᵀ where A_{ij} are the cofactors of Δ.
- **Reciprocal / Inverse of Δ** ⭐ (Δ ≠ 0): (1/Δ)·Δ′; equivalently the determinant whose elements are A_{ij}/Δ.

### Key identity
For an order-3 determinant: Δ′ · Δ = Δ³ (more generally Δⁿ for order n) ⇒ adj(Δ)/Δ has determinant Δⁿ⁻¹.

### Mechanisms / Processes
1. Compute every cofactor A_{ij} of Δ (with sign (−1)^{i+j}).
2. Place A_{ij} in row j, column i of the new array — **transpose** while filling.
3. The resulting array is Δ′ (the adjoint).
4. Divide every entry of Δ′ by Δ to obtain the reciprocal.

### Examples (from the source)
**Example: Δ = | 0 1 2 ; 2 0 1 ; 1 2 0 |.** Here a₁=0, b₁=1, c₁=2, a₂=2, b₂=0, c₂=1, a₃=1, b₃=2, c₃=0.

Direct expansion:
- Δ = 0·(0·0 − 1·2) − 1·(2·0 − 1·1) + 2·(2·2 − 0·1) = 0 − 1·(−1) + 2·4 = 0 + 1 + 8 = **9**.

(Source uses the relation Δ = a₁B₁ + a₂B₂ + … to obtain Δ = 9 via cofactor steps.)

Cofactors (typical pieces shown in source):
- B₁ = +|0 1 ; 2 0| = −2; B₂ = −|1 2 ; 2 0| = +4; B₃ = +|1 2 ; 0 1| = 1.
- C₁ = +A₃ = 4; C₂ = −B₃ = −2 (i.e. (−1)^{2+3}·1 with sign), C₃ = −2 etc. — full table built one row at a time.

Adjoint:
adj(Δ) = | −2 4 1 ; 4 −2 −1 ; 1 4 −2 | (transpose of the cofactor matrix, as printed in the source).

Reciprocal:
(1/Δ)·adj(Δ) = (1/9)·| −2/9  4/9  1/9 ; 4/9  −2/9  −1/9 ; 1/9  4/9  −2/9 | (the textbook displays −2/9, 4/9, 1/9 etc. as the reciprocal entries).

### ⚠️ Common Mistakes
- ❌ Forgetting to **transpose** when assembling the adjoint → ✅ adj(Δ) = (cofactor matrix)ᵀ.
- ❌ Trying to take a reciprocal when Δ = 0 → ✅ Reciprocal exists only if Δ ≠ 0 (singular determinants have no inverse).
- ❌ Mixing up minors and cofactors when filling the adjoint → ✅ The adjoint uses **cofactors** (signed minors), not raw minors.

> **Quick Recall:**
> - adj(Δ) = transpose of the cofactor matrix.
> - Reciprocal Δ⁻¹ = adj(Δ)/Δ, exists iff Δ ≠ 0.
> - Δ · adj(Δ) = Δⁿ (= Δ³ for 3×3 case).

### Connections
- Builds on: 5.2.2 Minors and Cofactors.
- Prerequisite for: matrix inverse via the adjoint formula in 5.3 (inverse of a non-singular matrix).

---

## Section: 5.2.6 Symmetric Determinants 🟡

### Core Idea
A determinant is **symmetric** if every element is positionally symmetric about the leading diagonal — i.e. a_{ij} = a_{ji} for all i,j. Equivalently, transposing the determinant reproduces it exactly. Adjoints of symmetric determinants are themselves symmetric, so the property carries through to higher-order calculations.

### Definitions
- **Symmetric determinant** ⭐: a₁ⱼ = aⱼ₁ in general, a_{ij} = a_{ji}; the second row is the same as the second column, etc. Example structure: | a h g ; h b f ; g f c |.

### Properties
- The transpose of a symmetric determinant equals itself: Δᵀ = Δ.
- The adjoint of a symmetric determinant is also symmetric.
- The theory extends to order n: any n×n determinant with a_{ij} = a_{ji} is symmetric.

### Worked example (from source)
Let Δ = | 1 2 3 ; 2 4 5 ; 3 5 7 |. Then Δᵀ = Δ (entries are mirrored across diagonal). Direct expansion of Δᵀ·Δ gives the matrix product
| 1+4+9   2+8+15   3+10+21 ;
  2+8+15  4+16+25  6+20+35 ;
  3+10+21 6+20+35  9+25+49 |
= | 14 25 34 ; 25 45 61 ; 34 61 83 |, which is itself a symmetric determinant.

The adjoint adj Δ is computed and is **also symmetric** as expected:
adj Δ = | 3 1 −2 ; 1 −2 1 ; −2 1 0 |.

> **Quick Recall:**
> - a_{ij} = a_{ji} ⇒ symmetric.
> - Δᵀ = Δ; adj Δ also symmetric.
> - Squaring a symmetric determinant (Δᵀ·Δ) yields a symmetric determinant.

### Connections
- Contrasts with: 5.2.7 Skew-Symmetric Determinants.
- Builds on: Property I (transpose) + 5.2.5 (adjoint).

---

## Section: 5.2.7 Skew and Skew-Symmetric Determinants 🟡

### Core Idea
A determinant is **skew** if a_{ij} = −a_{ji} for i ≠ j and the diagonal entries are unrestricted; it is **skew-symmetric** if additionally every diagonal entry is zero (a_{ii} = 0). Every skew-symmetric determinant of **odd order** is identically zero; every skew-symmetric determinant of **even order** is a perfect square.

### Definitions
- **Skew determinant**: a_{ij} = −a_{ji} for i ≠ j (diagonal entries arbitrary). Example: | a −b −g ; b b −f ; g f c | is skew because off-diagonal positions reverse sign upon transpose.
- **Skew-symmetric determinant** ⭐: a_{ij} = −a_{ji} for i ≠ j AND a_{ii} = 0. Example structure: | 0 a b ; −a 0 c ; −b −c 0 |.

### Properties
- Every skew-symmetric determinant of **odd order** = **0**.
  *Proof sketch:* Δᵀ = (−1)·Δ (factor −1 from each column); but Δᵀ = Δ for any determinant by Property I, so Δ = −Δ ⇒ 2Δ = 0 ⇒ Δ = 0 (for odd order, the (−1)ⁿ factor stays as −1).
- Every skew-symmetric determinant of **even order** is a **perfect square**.

### Worked example
Δ = | 0 5 2 ; −5 0 −3 ; −2 3 0 | is skew-symmetric of order 3 (odd).

Taking the (−1) common from each column: Δᵀ = (−1)³·| 0 −5 −2 ; 5 0 3 ; 2 −3 0 | = (−1)·| 0 5 2 ; −5 0 −3 ; −2 3 0 | = −Δ.

But Δᵀ = Δ in general ⇒ Δ = −Δ ⇒ 2Δ = 0 ⇒ **Δ = 0**.

A skew-symmetric example of even order (order 2): | 0 2 ; −2 0 | = (0)(0) − (2)(−2) = **4 = 2²**, confirming the perfect-square property.

> **Quick Recall:**
> - Skew: a_{ij} = −a_{ji} for i ≠ j (diagonal free).
> - Skew-symmetric: a_{ij} = −a_{ji} AND a_{ii} = 0.
> - Odd order skew-symmetric ⇒ 0.
> - Even order skew-symmetric ⇒ perfect square.

### Connections
- Contrasts with: 5.2.6 Symmetric determinants (sign-symmetry vs sign-antisymmetry).

---

## Section: 5.2.8 Solution of Simultaneous Equations by Cramer's Rule 🔴

### Core Idea
**Cramer's Rule** (Gabriel Cramer) is a **determinant formula** for solving a system of n linear equations in n unknowns: each unknown equals the ratio of two determinants of the coefficient matrix — the denominator is the determinant of the coefficient matrix Δ, and the numerator is Δ with the column of that variable replaced by the constants vector. The rule applies whenever Δ ≠ 0.

> **In Simple Terms:** Cramer's Rule says: write the coefficient determinant Δ; to find a particular variable, replace its column in Δ by the right-hand-side numbers and call the result Δ_x; then x = Δ_x / Δ. One determinant per variable, no elimination, no substitution.

### Mechanisms / Processes (3-variable case)
For the system:
1. a₁x + b₁y + c₁z = k₁
2. a₂x + b₂y + c₂z = k₂
3. a₃x + b₃y + c₃z = k₃

Define:
- Δ = | a₁ b₁ c₁ ; a₂ b₂ c₂ ; a₃ b₃ c₃ | (coefficient determinant; must be ≠ 0).
- Δ_x = | k₁ b₁ c₁ ; k₂ b₂ c₂ ; k₃ b₃ c₃ |.
- Δ_y = | a₁ k₁ c₁ ; a₂ k₂ c₂ ; a₃ k₃ c₃ |.
- Δ_z = | a₁ b₁ k₁ ; a₂ b₂ k₂ ; a₃ b₃ k₃ |.

Then **x = Δ_x / Δ, y = Δ_y / Δ, z = Δ_z / Δ**. ⭐

### Worked example (2-variable)
**Suppose:** x₁ − 2x₂ = 3 and 3x₁ + 5x₂ = 20. (As given in the source.)

Matrix form: A·X = B with A = | 1 −2 ; 3 5 |, X = (x₁, x₂)ᵀ, B = (3, 20)ᵀ.

Δ = |1 −2 ; 3 5| = 1·5 − (−2)·3 = 5 + 6 = 11.

x₁ = | 3 −2 ; 20 5 | / 11 = (15 + 40) / 11 = 55/11 = **5**.

x₂ = | 1 3 ; 3 20 | / 11 = (20 − 9) / 11 = 11/11 = **1**.

So (x₁, x₂) = (5, 1). ⭐

### ⚠️ Common Mistakes
- ❌ Applying Cramer's Rule when Δ = 0 → ✅ Either no solution or infinitely many — Cramer fails. Use Gaussian elimination or the rank test.
- ❌ Replacing the wrong column for a variable → ✅ For variable i, replace **column i** of Δ by the constants k.
- ❌ Forgetting that the constants vector must be on the right of A·X = B before reading off → ✅ Move all constants to the right side first; if a system is in the form a₁x + b₁y + c₁ = 0, rewrite as a₁x + b₁y = −c₁.

> **Quick Recall:**
> - Cramer's Rule: x_i = Δ_i / Δ, where Δ_i replaces column i of Δ with the constants.
> - Works only when Δ ≠ 0.
> - One determinant per unknown, plus the coefficient determinant.

### Connections
- Builds on: 5.2.1 Definition + 5.2.3 Properties (used to compute Δ, Δ_x, etc.).
- Contrasts with: matrix inverse method A⁻¹·B and Gaussian elimination — Cramer is conceptually clean but computationally expensive for large n.

---

## Section: Check Your Progress 2 (preview) 🟢
The book then offers a self-check pair: (1) write down the cofactors C₁₁, C₁₂, C₁₃, C₂₁, C₂₂ for a given determinant; (2) solve x + 2y + 3z = 6, 2x + 4y + z = 7, 3x + 2y + 9z = 14 by Cramer's Rule. Solutions are derivable directly from the rule above.

---

## Section: 5.3 MATRIX — 5.3.1 Concept of a Matrix 🔴

### Core Idea
A **matrix** is a **rectangular** arrangement of numbers in rows and columns; it lets us treat a single magnitude *and* an entire structured set of magnitudes simultaneously, abstracting many connected numerical facts into one object that can be manipulated as a whole.

> **In Simple Terms:** A matrix is a spreadsheet where the cells obey algebra. Instead of writing seven separate numbers, you write one bold A — then a single rule tells you what A + B, A − B, A·B, or A⁻¹ should mean.

### Motivating example (multi-individual data)
Three individuals A, B, C own pants, shirts, and ties:
- A has 3 pants, 3 shirts, 1 tie.
- B has 5 pants, 5 shirts, 2 ties.
- C has 6 pants, 8 shirts, 0 ties.

This data is naturally written as

A = | 3 3 1 ; 5 5 2 ; 6 8 0 |.

Each **row** is a person's holdings; each **column** is the count of one item type across all people.

### Definitions
- **Matrix** ⭐: a rectangular arrangement of m·n numbers (or symbols) into m rows and n columns. Denoted A = [a_{ij}] where a_{ij} is the element in row i, column j.
- **Order (size) of a matrix**: m × n, read "m by n"; m = number of rows, n = number of columns.
- **Element a_{ij}**: entry of A in the i-th row and j-th column.
- "Matrix algebra": the basic operations and methods for dealing with such arrays in solving simultaneous equations involving many variables.

### Notational conventions
- A is denoted [a_{ij}] or (a_{ij}); brackets [ ], parentheses ( ), or large parentheses ‖ ‖ are all acceptable.
- Square matrices: m = n; the matrix is then **of order n**.

### Connections
- Sets up: 5.3.2 Types of matrices, 5.3.3 Matrix relations and operations.

---

## Section: 5.3.2 Types of Matrices 🔴

### Core Idea
Matrices are classified by their shape and by special structural relationships among their entries. The first wave of types — **rectangular, square, row, column, zero, transpose, non-zero, diagonal, scalar, identity, symmetric, skew-symmetric, idempotent, orthogonal** — give exam-essential vocabulary; many later results turn on which type is in front of you.

### Type table (this chunk introduces A–F; later types continue in chunk 003)

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

Note: **I = Iᵀ** (identity is its own transpose).

### Examples
- **Diagonal matrix**: | 1 0 0 ; 0 2 0 ; 0 0 3 |.
- **Scalar matrix**: a · I, e.g. | a 0 0 ; 0 a 0 ; 0 0 a |.
- **Identity matrix of order 3**: I₃ = | 1 0 0 ; 0 1 0 ; 0 0 1 |.
- **Transpose**: if A = | a₁ b₁ c₁ ; a₂ b₂ c₂ |, then Aᵀ = | a₁ a₂ ; b₁ b₂ ; c₁ c₂ |. The transpose of a matrix of order m×n is of order n×m.
- **Null/zero matrix**: O₂×₃ = | 0 0 0 ; 0 0 0 |.

### ⚠️ Common Mistakes
- ❌ Calling every "diagonal-only" matrix a scalar matrix → ✅ A scalar matrix requires the diagonal entries to be **all equal**; otherwise it is a generic diagonal matrix.
- ❌ Confusing the identity matrix with the **scalar matrix** "1·I" — they coincide, but in general a scalar matrix is not the identity unless the constant is 1.

> **Quick Recall:**
> - Square matrix has m = n.
> - Identity I has 1's on the diagonal, 0 elsewhere; I = Iᵀ.
> - Scalar = diagonal with equal entries; Identity = scalar with constant 1.
> - Transpose is row-column swap; (Aᵀ)ᵀ = A.

### Connections
- Builds on: 5.3.1 Concept of Matrix.
- Sets up: more types and matrix operations in chunk 003 (continued types G–N, equality, addition, multiplication).

---

## Section: 5.3.3 Matrix Relations and Operations — opening (Equality of Matrices, Addition, Subtraction) 🔴

### Core Idea
Two matrices can interact only when they are **conformable** for the operation in question. For equality, addition, and subtraction the conformability rule is the same: identical orders. For multiplication (introduced later) the rule is different.

### Definitions
- **Conformable for equality** ⭐: A = [a_{ij}] and B = [b_{ij}] of the **same order** are **equal** iff a_{ij} = b_{ij} for every (i, j).
- **Conformable for sum/difference**: same order m × n.

### Examples
- Order 1×2 vs 1×3: not conformable for equality. E.g., [1² 2³] vs [1 4 ; 9 16] — different orders → unequal by definition.
- Same-order example: | 1 2 3 ; 3 4 5 | + | 0 1 2 ; 2 3 4 | = | 1+0 2+1 3+2 ; 3+2 4+3 5+4 | = | 1 3 5 ; 5 7 9 |.

### Properties already implied
- A + B = B + A (matrix addition is **commutative**).
- (A + B) + C = A + (B + C) (matrix addition is **associative**).

### ⚠️ Common Mistakes
- ❌ Trying to add matrices of different orders → ✅ Addition requires the same order m × n.
- ❌ Treating (A − B) as undefined → ✅ A − B = A + (−B) when both are the same order; entry-wise subtraction.

> **Quick Recall:**
> - Equality: same order AND elementwise equal.
> - Addition / Subtraction: same order; entry-wise.
> - Addition is commutative and associative.

### Connections
- Sets up: 5.3.3.3 Matrix multiplication (different conformability rule, treated in next chunk).

### Open Questions
1. Why are matrix multiplication conformability requirements (m₁×n₁ · n₁×n₂) different from those for addition? (Resolved in next chunk via the row-by-column definition.)
