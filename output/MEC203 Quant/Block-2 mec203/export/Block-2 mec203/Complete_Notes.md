# Complete Notes


## Section: Block 2 / Unit 5 Overview & Objectives 🟢

### Core Idea
Block 2 of MEC-203 covers **Linear Algebra**, organised into four units: Unit 5 Matrix Algebra, Unit 6 Vector Analysis, Unit 7 Vectors and Matrices, and Unit 8 Vector and Matrix Representations of Linear Equations. Unit 5 itself opens by motivating **determinants and matrices** as tools for handling economic models that involve many variables and many equations simultaneously, and lists the operational skills the unit aims to build.

> **In Simple Terms:** When an economic model has dozens of variables tied together by dozens of equations, solving them one at a time is hopeless. Linear algebra is a packaging trick — it bundles the whole system into compact objects (matrices) so that one algebraic move on the package replaces many tedious moves on the parts.

### Key Concepts

#### Why linear algebra in economics
Economic relationships frequently involve many interrelated variables (e.g. input–output systems, simultaneous-equation models). Manually solving them is mechanical and error-prone. Linear algebra supplies a compact apparatus — matrices and determinants — that allows concise representation, algebraic manipulation, and systematic solution.

#### Unit 5 learning objectives
After Unit 5 the student should be able to: explain the concept of a determinant and the various mathematical operations on determinants; present the properties of determinants; find the product of two determinants; solve a system of simultaneous linear equations by **Cramer's rule**; explain the concept of a matrix, its types, and operations on matrices; explain and use the various concepts of submatrices and minors, orthogonal matrix, symmetric and skew-symmetric matrices, idempotent matrix, trace of a matrix, transpose of a matrix, non-singular matrix, inverse of a matrix; find the inverse of a non-singular matrix; calculate the rank of a matrix; and use partition matrix in efficient matrix operations.

### Definitions
- **Linear Algebra (working sense)**: the area of algebra dealing with the manipulation of matrices and determinants for solving systems of linear equations and analysing linear relationships among variables.

> **Quick Recall:**
> - Block 2 = Linear Algebra (Units 5–8).
> - Unit 5 covers determinants + matrices in one package.
> - Cramer's rule and the inverse-matrix method are the two solution techniques you must master.

### Connections
- Sets up everything in: Determinants — Definition (this chunk) and all subsequent matrix material.

---

## Section: 5.1 Introduction — Origins of Determinants and Matrices 🟢

### Core Idea
Determinants were first used to solve simultaneous equations around 1683, **almost simultaneously by Japanese mathematician Seki Kowa and German mathematician Leibniz**. Matrix theory later emerged through the work of **Mesopotamia, India, and China** for solving simultaneous equations. Most textbooks treat determinants and matrices as separate topics, but this unit develops the two concepts together because their algebraic operations and applications are tightly linked.

### Definitions
- **Determinant (intuitive)**: a single numerical value calculated from a square arrangement of numbers; used historically to test whether a system of linear equations has a unique solution.
- **Matrix (intuitive)**: a rectangular arrangement of numbers used to represent and manipulate systems of linear relationships.

### Connections
- Builds on: nothing (origin material).
- Sets up: 5.2 Determinants and 5.3 Matrix.

---

## Section: 5.2 Determinants — 5.2.1 Definition and Concept 🔴

### Core Idea
A determinant is the single value that arises naturally when one solves a 2-equation, 2-unknown linear system by elimination: the common denominator of the unique solutions for x and y is itself a meaningful quantity, written as a square array between vertical bars. Determinants of higher order generalise this idea and serve as the test for whether a square system has a unique solution.

> **In Simple Terms:** Solve any 2×2 linear system on paper. The same expression keeps showing up in the bottom of every fraction — that recurring expression *is* the determinant. The book just gives this recurring quantity its own symbol so we don't have to keep rewriting it.

### Key Concepts

#### Derivation of the 2×2 determinant
Start with the system
1. a₁x + b₁y + c₁ = 0
2. a₂x + b₂y + c₂ = 0

Solving (cross-multiplication / elimination) gives:

x / (b₁c₂ − b₂c₁) = y / (c₁a₂ − c₂a₁) = 1 / (a₁b₂ − a₂b₁)

so x = (b₁c₂ − b₂c₁) / (a₁b₂ − a₂b₁) and y = (c₁a₂ − c₂a₁) / (a₁b₂ − a₂b₁).

The **common denominator** (a₁b₂ − a₂b₁) is the determinant of the coefficient array

| a₁  b₁ |
| a₂  b₂ |

written compactly as |a₁ b₁ ; a₂ b₂| = a₁b₂ − a₂b₁. ⭐

#### Order, rows, columns, elements
- The numbers inside the determinant are **elements**.
- Horizontal lines of elements form **rows**; vertical lines form **columns**.
- A determinant with n rows and n columns is a **determinant of the n-th order**.
- A 2nd-order determinant has 2² = 4 elements; a 3rd-order has 3² = 9 elements; an n-th order has n² elements.

#### 3×3 determinant — the "Sarrus" diagonal rule
For

| a₁  b₁  c₁ |
| a₂  b₂  c₂ |
| a₃  b₃  c₃ |

the expansion has 3·2 = **6 terms**. The signs are obtained from the diagonal pattern:
- "↘" diagonals (top-left to bottom-right) — **positive**: a·q·z + b·r·x + c·p·y.
- "↗" diagonals (top-right to bottom-left) — **negative**: c·q·x + a·r·y + b·p·z.

Equivalently, expanding along row 1:

Δ = a₁(b₂c₃ − b₃c₂) − b₁(a₂c₃ − a₃c₂) + c₁(a₂b₃ − a₃b₂). ⭐

### Definitions
- **Determinant**: the single scalar value associated with a square array of numbers (the "determinant" of the array). ⭐ (exam-important)
- **Element**: any individual entry inside the determinant.
- **Order of a determinant**: the number of rows (= number of columns) of the square array; an order-n determinant has n² elements.

### Mechanisms / Processes
2×2 expansion: cross-multiply along the main diagonal, subtract the cross-multiplication along the anti-diagonal:
(top-left × bottom-right) − (top-right × bottom-left).

### Examples
**Example: 2×2 derivation reused later.**
For the system 2x + 3y = 7, 4x + 5y = 13, the coefficient determinant is |2 3 ; 4 5| = 2·5 − 4·3 = 10 − 12 = −2 — exactly the denominator that appears when solving by elimination.

### Applications (importance for economics)
Determinants underpin:
- The theory of **equations**, geometry, multiple integrals, differential equations, and linear algebra.
- **Concise solution-formulas** for simultaneous linear equations.
- The **Jacobian determinant** ∂(u,v)/∂(x,y), an essential tool of mathematical analysis used to test for **functional dependence** in a system of non-linear equations and to test whether the linear system can be solved with workable algebraic expressions.
- Generalisations of the equations for conic sections in two dimensions.

### Definitions (extended)
- **Jacobian determinant** of two functions u(x,y), v(x,y):
  J = | ∂u/∂x  ∂u/∂y ; ∂v/∂x  ∂v/∂y |, written ∂(u,v)/∂(x,y). ⭐ (exam-important — recurring concept across calculus/economics)

> **Quick Recall:**
> - 2×2 determinant = a₁b₂ − a₂b₁.
> - 3×3 determinant via row-1 expansion has six signed terms; positive on ↘ diagonals, negative on ↗ diagonals.
> - Order-n determinant has n² elements; expansion has n! terms.
> - Jacobian determinant tests functional dependence in non-linear systems.

### Connections
- Sets up: 5.2.2 Minors and Cofactors (uses sub-determinants formed by deleting rows/columns).
- Sets up: 5.2.3 Properties of Determinants and 5.2.8 Cramer's Rule.

---

## Section: 5.2.2 Minors and Cofactors 🔴

### Core Idea
Any element a_{ij} of a determinant defines a **minor** (a sub-determinant got by crossing out the row and column of that element) and a **cofactor** (the minor times a sign that depends on the position). Minors and cofactors are the building blocks for expanding a determinant of any order and for finding inverses by the adjoint method.

### Definitions
- **Minor of an element a_{ij}**: the determinant formed by deleting the i-th row and j-th column from the original determinant; denoted M_{ij}. The minor is *minor* in size — its order is one less than the original. ⭐
- **Cofactor of a_{ij}**: A_{ij} = (−1)^{i+j} · M_{ij}. The "cofactor" is just the minor with the appropriate sign attached; it is the *coefficient* of the element a_{ij} in the row/column expansion. ⭐
- **Note on size**: in an n-th order determinant, every minor / cofactor is itself a determinant of order (n−1).

### Mechanisms / Processes
1. Pick element a_{ij}.
2. Strike out row i and column j.
3. The (n−1)×(n−1) determinant that remains = M_{ij} (minor).
4. Multiply by (−1)^{i+j} to get the cofactor A_{ij}.
5. Row-1 expansion of an order-n determinant: Δ = a₁A₁ + a₂A₂ + … + aₙAₙ, where A₁, A₂, … are the cofactors of the elements of the first row.

### Sign Pattern (sign chessboard)
| + | − | + |
| − | + | − |
| + | − | + |

### Examples
**Example: 3×3 cofactor calculation.**
Determinant: | 3 4 7 ; 2 1 3 ; 7 2 1 |. Expanding along row 1:
- A₁ = (−1)¹⁺¹ |1 3 ; 2 1| = (1)(1·1 − 3·2) = (1)(−5) = −5.
- A₂ = (−1)¹⁺² |2 3 ; 7 1| = (−1)(2·1 − 3·7) = (−1)(−19) = 19.
- A₃ = (−1)¹⁺³ |2 1 ; 7 2| = (1)(2·2 − 1·7) = −3.

Δ = a₁A₁ + a₂A₂ + a₃A₃ = 3·(−5) + 4·(19) + 7·(−3) = −15 + 76 − 21 = **40**.

(The text gets Δ = −15 + 76 − 21 = 40, and the same value is reproduced by expanding along row 2 or column 2 — confirming the row/column-independence property.)

### ⚠️ Common Mistakes
- ❌ Forgetting the (−1)^{i+j} sign and treating M_{ij} as the cofactor → ✅ A_{ij} = (−1)^{i+j} M_{ij}; always attach the sign.
- ❌ Treating "minor" as smaller than the element it belongs to → ✅ The minor is a *determinant*, not a number; its order is one less than the parent determinant.
- ❌ Mixing up rows and columns of the deleted element → ✅ Cross out the row AND column that pass through a_{ij}; whatever is left is the minor.

> **Quick Recall:**
> - Minor M_{ij} = determinant after deleting row i + column j.
> - Cofactor A_{ij} = (−1)^{i+j} · M_{ij}.
> - Δ = Σⱼ aᵢⱼ Aᵢⱼ along any chosen row i (or column j).
> - In an order-n determinant, every minor / cofactor has order n−1.

### Connections
- Builds on: 5.2.1 Definition (cofactors are signed minors of the parent determinant).
- Prerequisite for: 5.2.5 Adjoint and reciprocal determinants (built from cofactors).
- Prerequisite for: matrix inverse via the adjoint formula (later in Unit 5).

---

## Section: 5.2.3 Properties of Determinants — Properties I to VI 🔴

### Core Idea
Determinants obey six clean algebraic properties. Each property is itself a computational shortcut: instead of expanding a determinant in full you can swap, add, or scale rows/columns to simplify the calculation, or to spot that the determinant is zero by inspection. These six properties are the workhorses of all later determinant problems.

> **In Simple Terms:** Properties of determinants are like rules of accounting. Once you know "swapping two rows flips the sign" or "two equal rows make the value zero," many large determinants collapse to a one-line answer.

### Key Concepts

#### Property I — Transpose property
A determinant is **unchanged** in value if all its rows are changed into columns and all its columns into rows (i.e., transposition).

**Example:**
| 1 3 0 ; 2 4 0 ; 1 0 3 | = | 1 2 1 ; 3 4 0 ; 0 0 3 |.

**Implication:** every property that holds for rows holds equally for columns, and vice versa.

#### Property II — Row/column interchange
The value of a determinant is **changed numerically only in sign** when any two rows (or any two columns) are interchanged.

**Example:**
| 1 3 0 ; 2 4 0 ; 1 0 3 | = (−1) · | 4 2 0 ; 3 1 0 ; 0 1 3 | (interchanging columns 1 and 2 flips the sign).

#### Property III — Two equal rows / columns
If any two rows or any two columns of a determinant are **identical (or proportional)**, then the determinant equals **zero**.

**Example:**
| 1 2 3 ; 2 3 1 ; 1 2 3 | = 0 (rows 1 and 3 are identical).
| 1 2 3 ; 2 4 1 ; 1 2 3 | = 2 · | 1 2 1 ; 1 1 4 | = 0 (after extracting common factor 2; columns 1 and 2 of the reduced determinant are identical).

#### Property IV — Multiplying a row/column by a scalar
If all the elements of any one row (or column) of a determinant are multiplied by the same number K, then the **determinant** is multiplied by K. This means K can be **factored out** of a row or column. Equivalently: detecting a common factor in a row/column lets you pull it outside the bars.

**Example:**
| K·a₁₁  K·a₁₂  K·a₁₃ ; a₂₁ a₂₂ a₂₃ ; a₃₁ a₃₂ a₃₃ | = K · | a₁₁ a₁₂ a₁₃ ; a₂₁ a₂₂ a₂₃ ; a₃₁ a₃₂ a₃₃ |.

In the textbook example, the 2×2 determinant | 2 10 ; 3 7 | is treated as | 2·1  2·5 ; 3·7  3·1 | = 2·| 1 5 ; 3 7 | (extracting factor 2 from the first row of the original).

#### Property V — Splitting a row/column that is a sum
If each element of a row (or column) is **expressed as the sum of two terms**, then the determinant can be expressed as the **sum of two determinants**: one keeping the first parts, the other keeping the second parts; the remaining rows (or columns) are unchanged.

**Example (Δ as a sum of two determinants Δ₁ + Δ₂):**
| 8+2  2  5+4 ; 4+5  9  1+4 ; 5+11  11  7+1 |
= | 8 2 5 ; 4 9 1 ; 5 11 7 | + | 2 2 4 ; 5 9 4 ; 11 11 1 |
= 416 − 66 = 365 (worked in the source) for Δ₁;
Δ₂ = 2(63−11) − 5(28−5) + 4(44−45) = 2·104 − 5·115 − 4 = −15;
Δ = Δ₁ + Δ₂ = 365 + (−15) = 350 — matches the direct expansion 9(63−11) − 11(28−5) + 9(44−45) = 350.

#### Property VI — Row/column operation (the "elimination" property)
The value of a determinant remains **unchanged** if to the elements of any row (or column) we **add (or subtract) any constant multiple of the corresponding elements of any other row (or column)**.

**Example:**
| 2+6  3  6 ; 3+4  2  1 ; 4+2  1  7 | = Δ (where the first column has been expressed as a sum) — applying property VI with column-1 minus 2·column-3 leaves the determinant unchanged. This is the elimination rule that powers row-reduction-style determinant evaluation.

### ⚠️ Common Mistakes
- ❌ Forgetting that **proportional** rows (not only identical rows) make the determinant zero → ✅ Property III says "identical OR proportional".
- ❌ Pulling K out of *every* row when only one row has the factor → ✅ Property IV: K comes out only for the row/column that actually has K as the common factor.
- ❌ Splitting a determinant when only **one element** is a sum → ✅ Property V requires *each element of the row/column* to be a sum; otherwise re-derive.
- ❌ Sign error after row/column swap → ✅ One swap flips the sign once; two swaps restore the sign.
- ❌ Adding a multiple of one row to a non-corresponding position → ✅ Property VI uses the *corresponding* (same column-index) elements only.

> **Quick Recall:**
> - Six properties: transpose, swap (sign flip), equal/proportional → 0, scalar multiply, sum-split, add multiple of another row.
> - Transpose property → all rules apply to both rows and columns.
> - Use Property VI to introduce zeros and cut work; use Property IV to pull out common factors before expanding.
> - Two identical or proportional rows ⇒ determinant = 0 (test by inspection).

### Connections
- Builds on: 5.2.1 Definition (these properties operate on the same expansion).
- Used by: every later determinant calculation, including 5.2.4 Product of Two Determinants and 5.2.8 Cramer's Rule.
<!-- Continues in chunk 002 — Properties VII onward and Skew/Symmetric determinants will be handled there. -->

### Open Questions
1. How does Property VI generalise to several simultaneous row operations performed in sequence (do successive applications still preserve the value)?


---


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


---


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


---


## Section: 5.5 Key Words (concluded) 🟢
<!-- See chunk 003 for start of this section -->

### Definitions captured here
- **Minor**: the minor of an element in a determinant is **another determinant of lower order** that can be obtained by deleting the row and column containing that element. The minor of an element a_{ij} of an n×n determinant is **of order (n−1)** — i.e. an order-3 determinant has order-2 minors.
- **Rank**: the maximum number of independent rows (or columns) in a matrix.
- **Trace**: for a square matrix, the sum of its diagonal elements.

### Connections
- Caps Unit 5 vocabulary; ties back to determinants (5.2.1–5.2.5), matrices (5.3.1–5.3.4), and rank (5.3.7).

---

## Section: 5.6 Answers / Hints to Check Your Progress Exercises 🟡

### Check Your Progress 1 — answers
1. Determinant | 2 1 3 ; 4 5 6 ; 7 8 9 | = **0** (rows are linearly dependent: row 3 = 2·row 2 − row 1; the source's hint phrases this with two parallel rows after a row operation).
2. Property-verification on | 2 0 −1 ; 1 1 7 ; 3 3 9 |: typical expansions confirm Properties I (transpose unchanged), II (swap → sign flip), and others.
3. **Vandermonde determinant** | 1 1 1 ; a b c ; a² b² c² | = (b − a)(c − a)(c − b). ⭐ Hint chain: subtract column 1 from columns 2 and 3, expand along the new row 1.
4. | b+c  a    a ; b    c+a  b ; c    c    a+b | = **4abc** ⭐. Hint chain: C₁ → C₁ + C₂ + C₃, then row reductions; the "a + b + c" common factor disappears via cancellation.

### Check Your Progress 2 — answers
- Solving (after Section 5.2.5) the system x + 2y + 3z = 6, 2x + 4y + z = 7, 3x + 2y + 9z = 14 by Cramer's Rule:

  Δ = | 1 2 3 ; 2 4 1 ; 3 2 9 | = −20.
  Δ_x = | 6 2 3 ; 7 4 1 ; 14 2 9 | = −20.
  Δ_y = | 1 6 3 ; 2 7 1 ; 3 14 9 | = −20.
  Δ_z = | 1 2 6 ; 2 4 7 ; 3 2 14 | = −20.

  ∴ x = Δ_x/Δ = 1, y = Δ_y/Δ = 1, z = Δ_z/Δ = 1. ⭐

### Check Your Progress 3 — answers
- For A = | 1 1 −1 ; 7 9 −2 ; 2 −3 1 | (a representative source matrix):
  adj A = | … | (computed by cofactors), |A| = 1 (worked).
  ∴ A⁻¹ = adj A / 1 = adj A.
- Rank: less than 3 (one row depends linearly on the others).

### Check Your Progress 4 — answers
- The properties of orthogonal matrices: see Section 5.3.5.1.
- Idempotent: see Section 5.3.5.3.
- For partitioned A and B with row partitions, write the block multiplication as [A₁₁B₁₁ + A₁₂B₂₁ ; A₂₁B₁₁ + A₂₂B₂₁ ⋮ A₁₁B₁₂ + A₁₂B₂₂ ; A₂₁B₁₂ + A₂₂B₂₂] — direct block-by-block expansion.

### Check Your Progress 5 — answers
- Refer to Section 5.3.7 (rank of a matrix and its properties).

> **Quick Recall:**
> - Vandermonde 3×3 = (b−a)(c−a)(c−b). ⭐
> - "b+c, c+a, a+b" cyclic determinant = 4abc. ⭐
> - Cramer's example used in Unit 5 final answers: (x,y,z) = (1,1,1).

---

## Section: 5.7 Exercises (worked-out examples and end-of-unit problems) 🔴

### Q1 — Cramer's Rule on a national-income model
Model: Y = C + I + G; C = a + bY (a, b constants).

Solve for Y and C. Coefficient form (after rearrangement):
- Y − C = I + G
- C − bY = a, i.e. −bY + C = a.

Coefficient determinant: Δ = | 1 −1 ; −b 1 | = 1 − b.

By Cramer's Rule:
- Y = Δ_Y / Δ = | I + G  −1 ; a  1 | / (1 − b) = ( I + G + a ) / (1 − b). ⭐
- C = Δ_C / Δ = | 1  I + G ; −b  a | / (1 − b) = ( a + b(I + G) ) / (1 − b). ⭐

> **In Simple Terms:** With consumption C = a + bY and income identity Y = C + I + G, the equilibrium income is the **autonomous spending (a + I + G) divided by the leakage 1 − b**, exactly what the Keynesian multiplier k = 1 / (1 − b) gives.

### Q2 — Determinant version of national-income with taxes
Variables Y (national income), C (consumption), T (tax). Equations:
- Y = C + I + G (income identity).
- C = a + b(Y − T), i.e. C − bY + bT = a (consumption with disposable income).
- T = d + tY, i.e. tY − T = −d (lump-sum + proportional tax).

Solve by Cramer's Rule. After arranging:

|  1  −1   0 ;
  −b   1   b ;
  −t   0   1 |
multiplied by (Y, C, T)ᵀ on the left = (I + G, a, d)ᵀ on the right (sign-arranged so all unknowns are on LHS).

Solutions (from the source):
- Y = ( bd − I(t − 1) − a − G ) / ( bt + b − 1 ).
- C = (some symmetric expression) / Δ.
- T = ( −d + bd − at − G·t ) / ( bt + b − 1 ).

(Exam-relevant: the **same Cramer-Rule mechanism** scales to 3-variable Keynesian/IS-LM systems with tax functions. The denominator (bt + b − 1) is the equilibrium denominator that captures the tax-augmented multiplier.)

### Q3 — Keynesian model with money (IS-LM-style)
Behavioural equations:
- C = 0.8Y, I = 102 − 0.2r.
- Mᵈ = 0.25Y − 2.5r, Mˢ = Mᵈ.

(i) Write the equations of the IS and LM curves.
(ii) Evaluate equilibrium values of Y and r using Cramer's Rule.

**Answer:** Y = −500, r = −10 (the source's printed solution; the negative values arise from the chosen constants — confirm the algebra carefully).

### Q4 — Linear equations homogeneous case
ax + by + cz = 0, bx + cy + az = 0, cx + ay + bz = 0.

Show that this homogeneous system has a non-trivial solution iff
| a b c ; b c a ; c a b | = 0,
i.e. iff a³ + b³ + c³ − 3abc = 0.

**Answer**: the trivial solution (x = y = z = 0) always exists; non-trivial solutions exist iff a + b + c = 0 OR a = b = c (the determinant factors as (a + b + c)(a² + b² + c² − ab − bc − ca)).

### Q5 — National-income model (matrix inversion) practice
Y = I + G, C = a + b(Y − T) (0 < b < 1), T = d + tY (d > 0, 0 < t < 1).
Solve for Y, C, and T by **matrix inversion** (X = A⁻¹·B form).

### Q6 — Mixed matrix products
Given U = [1 0 1] (1×3), V = (1, 2, 3)ᵀ (3×1), X = | 4 2 −1 ; −1 3 0 ; 0 1 1 | (3×3), Y = I₃.

a. UV = 1·1 + 0·2 + 1·3 = 4 (a 1×1).
b. VU + X = | 1·[1 0 1] ; 2·[1 0 1] ; 3·[1 0 1] | + X = | 1 0 1 ; 2 0 2 ; 3 0 3 | + | 4 2 −1 ; −1 3 0 ; 0 1 1 | = | 5 2 0 ; 1 3 2 ; 3 1 4 |.
c. XY = X (since Y = I) = | 4 2 −1 ; −1 3 0 ; 0 1 1 |.

**Hint:** "Use partitioned matrices to check the results."

> **Quick Recall (Unit 5 closing):**
> - National income with C = a + bY: Y = (a + I + G)/(1 − b). ⭐ — 1/(1−b) is the Keynesian multiplier.
> - For the tax-augmented system, denominator becomes (1 − b + bt). ⭐
> - Homogeneous A·X = 0 has non-trivial solution iff |A| = 0.

### Connections
- Closes Unit 5; bridges into Unit 6 (vectors as a different structure for solving multi-variable problems).

---

## Section: UNIT 6 — VECTOR ANALYSIS — 6.0 Objectives 🟢

### Core Idea
Unit 6 introduces **vectors** as the natural objects for representing magnitudes that also carry direction (e.g. price vectors, demand vectors, gradients) and lays the algebraic and geometrical groundwork for **vector spaces, inner product, norm, basis, and linear independence** — the apparatus that linear-algebra methods use to handle high-dimensional economic data.

### Objectives
After Unit 6 the student should be able to:
- Identify the presentation of variables with **magnitude** *and* **direction**.
- Apply basic **operations** of vector addition, subtraction, and **scalar multiplication**.
- Present geometric and physical interpretations of vectors and vector operations.
- Explain the concepts of **norm**, **inner product**, **vector space**, **linearly independent vectors**, **linearly dependent vectors**, and **basis**.
- Explain the concepts of **generators** and basis of a vector space.

### Connections
- Builds on: Block 1 calculus and the matrix material of Unit 5.
- Sets up: Unit 7 (Vectors and Matrices) and Unit 8 (vector/matrix representation of linear equations).

---

## Section: 6.1 Introduction — vector vs scalar 🔴

### Core Idea
A **set of n** real numbers in any *unspecified* order is a "set". A **specific ordered** n-tuple, where order matters, is a **vector**. Vectors generalise the geometric idea of a directed arrow to higher dimensions: every n-tuple (x₁, x₂, …, xₙ) is a vector in ℝⁿ.

> **In Simple Terms:** Two numbers in any order = "a set". The same two numbers in *one specific order* = "a vector". Order is meaning: (3, 5) is not the same vector as (5, 3) even though they share the same components.

### Definitions
- **Set (n-element)**: an unordered collection {a, b, c, …, n}; the sets {a, b, c} and {a, c, b} are equal.
- **Vector** ⭐: an ordered n-tuple, e.g. (a, b, c, …, n); the order matters, so (a, b) ≠ (b, a) generically.
- **Element / component / coordinate** of a vector: each entry of the n-tuple.
- **n-vector / vector in ℝⁿ**: an ordered n-tuple of real numbers.
- **Null vector** ⭐: the vector all of whose components are zero. In economics, the null vector represents an absence of any commodity in a bundle (e.g. nothing consumed by the household).

### Conventions
- A vector can be written as a **row vector** (1×n) or as a **column vector** (n×1); these are the **same object** transposed.
  - Row form: (a, b, c, …, n) or [a b c … n].
  - Column form: vertical stack [a; b; c; …; n].
- Two vectors are **equal** iff they have the same number of components and corresponding components match.

### Connections
- Builds on: matrix notation (row matrix = row vector; column matrix = column vector).

---

## Section: 6.2 Vector Addition and Scalar Multiplication 🔴

### Core Idea
For vectors **a** = (a₁, …, aₙ) and **b** = (b₁, …, bₙ) of the same size n, **vector addition is component-wise**: a + b = (a₁ + b₁, …, aₙ + bₙ). For a scalar k ∈ ℝ, **scalar multiplication** is also component-wise: k·a = (k·a₁, …, k·aₙ). These two operations are the only ones needed to define a **vector space** (next section).

### Definitions
- **Sum of vectors** a + b = (a₁ + b₁, …, aₙ + bₙ); defined only when both vectors have the same number of components.
- **Difference**: a − b = (a₁ − b₁, …, aₙ − bₙ).
- **Scalar product / scalar multiple** ⭐: k·a = (k a₁, k a₂, …, k aₙ) for k ∈ ℝ. This is the product of a vector by a real number — *not* the inner product of two vectors (treated separately in 6.4 — *different concept*).

### Examples (from the source)
1. a = (1, 1, −2), b = (3, 0, 1) ⇒ a + b = (1+3, 1+0, −2+1) = (4, 1, −1).
2. a = (1, 4, 3, −6, 2), b = (3, −5, 1, −2, 3) ⇒ a − b = (1−3, 4−(−5), 3−1, −6−(−2), 2−3) = (−2, 9, 2, −4, −1).
3. 3·a = (3, 12, 9) (scalar multiplication of (1, 4, 3) by 3).

### ⚠️ Common Mistakes
- ❌ Confusing **scalar multiplication** (vector × number) with **scalar product / inner product** (vector × vector → number) → ✅ "Scalar multiplication" makes a vector; "scalar product / inner product" makes a number.

### Connections
- Foundational for: 6.3 Geometrical interpretation, 6.4 Norm and inner product, 6.5 Vector spaces.

---

## Section: Check Your Progress 1 — vector-arithmetic practice 🟡
1. List the difference between vector addition and scalar multiplication.
2. If a = (2, 3, 4, 7), a₁ = (0, 0, 0, 1) and a₂ = (1, 0, 1, 0), find a + 2a₁ + 3a₂.
3. If x₁ = (2, 9, 8), x₂ = (0, 1, 0) and x₃ = (1, 0, 1), find 2x₂ + 5x₃ − x₁.

---

## Section: 6.3 Geometrical and Physical Interpretations 🔴

### Core Idea
A vector in ℝ² or ℝ³ is geometrically an **arrowed line segment** with a length and a direction; the **length** = the *magnitude* of the vector and the **direction** of the arrow = the *direction* of the vector. Although we usually anchor vectors at the origin for clarity, *all* vectors with the same length and direction are equal — they are **free vectors**, transportable to any starting point.

### Definitions
- **Magnitude (length) of a vector** in ℝ²: ‖a‖ = √(a₁² + a₂²); in ℝ³: ‖a‖ = √(a₁² + a₂² + a₃²).
- **Direction angle θ** in ℝ²: tan θ = a₂ / a₁.
- **Direction cosines (ℝ³)**: cos α = a₁ / ‖a‖, cos β = a₂ / ‖a‖, cos γ = a₃ / ‖a‖.
- **Free vector**: equal magnitude and direction ⇒ same vector regardless of starting point.

### Geometric facts
- A vector is fully described by its **magnitude** and **direction**; if either differs, the vectors are different.
- In ℝ³ a vector starting at (a₁, a₂, a₃) and ending at (b₁, b₂, b₃) is represented by the n-tuple (b₁ − a₁, b₂ − a₂, b₃ − a₃) — a **displacement vector**.
- Vector arithmetic ↔ space of points: vectors and points in ℝⁿ are in **one-to-one correspondence** (after fixing the origin).

### Connections
- Sets up: 6.4 Norm/inner product (which generalises the geometric magnitude/angle to algebraic operations on n-tuples).

---

## Section: 6.4 Norm and Inner Product 🔴

### Core Idea
Vector addition and scalar multiplication are not enough to capture **length** and **angle**; for those we need an **inner product** (scalar/dot product). The **inner product** of two vectors gives a **scalar** number that summarises their alignment; the **norm** of a vector is the square root of its inner product with itself, generalising the Pythagorean length to n-dimensions.

### Definitions
- **Inner product / scalar product / dot product** ⭐ of a = (a₁, …, aₙ) and b = (b₁, …, bₙ): ⟨a, b⟩ = a₁b₁ + a₂b₂ + … + aₙbₙ = Σ aᵢbᵢ. Notation: ⟨a, b⟩ or a · b.
- **Norm (length) of a** ⭐: ‖a‖ = √⟨a, a⟩ = √(a₁² + a₂² + … + aₙ²).
- **Unit vector**: a vector with ‖a‖ = 1; for any non-zero a, the unit vector along a is a / ‖a‖.
- **Orthogonal vectors** ⭐: a ⊥ b iff ⟨a, b⟩ = 0. The zero vector is orthogonal to every vector.

### Examples
- a = (1, −1, 2), b = (3, 1, 0): ⟨a, b⟩ = 1·3 + (−1)·1 + 2·0 = 3 − 1 + 0 = 2.
- a = (1, 3), b = (−3, 1): ⟨a, b⟩ = −3 + 3 = 0 ⇒ a ⊥ b.
- a = (1, −2, 3): ‖a‖ = √(1 + 4 + 9) = √14.

### Properties of the norm
For any real number k and vectors a, X:
i. ‖k·a‖ = |k|·‖a‖. (Scalar multiplication scales the norm by the absolute value of the scalar.)
ii. ‖a‖ ≥ 0; ‖a‖ = 0 iff a is the null vector. (Positive-definiteness.)

### Properties of the inner product
- Symmetry: ⟨a, b⟩ = ⟨b, a⟩.
- Linearity in the first argument: ⟨k·a, b⟩ = k·⟨a, b⟩; ⟨a + a′, b⟩ = ⟨a, b⟩ + ⟨a′, b⟩.

### Cauchy–Schwarz inequality (geometric link to angle)
Define cos θ = ⟨a, b⟩ / (‖a‖ · ‖b‖). The **Cauchy–Schwarz inequality** ensures |cos θ| ≤ 1, equivalently:
**(Σ aᵢbᵢ)² ≤ (Σ aᵢ²)·(Σ bᵢ²)** ⭐ — squared inner product ≤ product of squared norms.

So:
- cos θ = 0 ⇔ a ⊥ b ⇔ ⟨a, b⟩ = 0.
- cos θ = ±1 ⇔ a is a scalar multiple of b ⇔ a is **parallel** to b.

### ⚠️ Common Mistakes
- ❌ Calling ka the "scalar product" of a → ✅ "Scalar product" is the inner product ⟨a, b⟩, not k·a (which is "scalar multiplication").
- ❌ Forgetting that any vector is orthogonal to the zero vector → ✅ ⟨0, b⟩ = 0 for all b.

> **Quick Recall:**
> - Inner product ⟨a, b⟩ = Σ aᵢbᵢ.
> - Norm ‖a‖ = √Σ aᵢ².
> - Cauchy–Schwarz: (Σ aᵢbᵢ)² ≤ (Σ aᵢ²)·(Σ bᵢ²). ⭐
> - cos θ = ⟨a, b⟩ / (‖a‖·‖b‖); a ⊥ b ⇔ ⟨a, b⟩ = 0.

### Connections
- Builds on: 6.2 Vector addition / scalar multiplication.
- Sets up: 6.5 Vector Spaces (definition of "linear" and "geometric" structure together).

---

## Section: Check Your Progress 2 — inner-product / norm practice 🟡
1. Given x = (3, 1)ᵀ and y = (2, −2)ᵀ, find 2y and x − y graphically.
2. Find the norm of (i) (2, 5); (ii) (1, 2, 3).
3. Find the inner product of (a) (2, 3, 4) and (4, 5, 6); (b) (−2, −3, 4) and (4, 5, −6).

---

## Section: 6.5 Vector Spaces and Subspaces 🔴

### Core Idea
A **vector space V over the real field ℝ** is a set of vectors closed under both **vector addition** and **scalar multiplication**, satisfying eight standard axioms (commutativity and associativity of addition, additive identity 0 and inverse −x, distributive laws, and scalar associativity/identity). A **subspace** is a non-empty subset W ⊂ V that is itself closed under both operations — equivalently W is closed under vector addition and scalar multiplication, with 0 ∈ W. Subspaces are themselves vector spaces.

### Definitions
- **Vector space V over ℝ** ⭐: a set V = {(x₁, x₂, …, xₙ) : xᵢ ∈ ℝ} with vector addition and scalar multiplication satisfying:
  i. x + y ∈ V (closure under addition); x + y = y + x; x + (y + z) = (x + y) + z.
  ii. There exists 0 ∈ V with x + 0 = x.
  iii. For any x ∈ V there exists −x ∈ V with x + (−x) = 0.
  iv. For any λ ∈ ℝ, x ∈ V: λ·x ∈ V (closure under scalar multiplication).
  v. λ·(x + y) = λ·x + λ·y; (λ + μ)·x = λ·x + μ·x; λ·(μ·x) = (λμ)·x; 1·x = x.

- **Subspace W of V** ⭐: a non-empty W ⊂ V that satisfies (a) w ∈ W ⇒ −w ∈ W (additive-inverse closure), and (b) w₁, w₂ ∈ W and α ∈ ℝ ⇒ w₁ + w₂ ∈ W and α·w₁ ∈ W.

### Worked example
Let V be the two-dimensional plane v₁ × v₂ (i.e., V = ℝ²) — the set of all points on the vertical axis is one subspace; **any subspace** must include the **zero vector**.

For another example: in ℝ², the line through the origin is an example of a subspace; an offset line not through the origin is **not** a subspace because it fails to contain the zero vector.

Algebraically:
- W = {(x₁, x₂) ∈ ℝ² : x₁ = 0} is a subspace of ℝ².
- W = {(x₁, x₂) ∈ ℝ² : x₁ + x₂ + 1 = 0} is **not** a subspace of ℝ² (does not contain (0, 0)).

### Properties
- Every vector space contains the zero vector (additive identity).
- Every line through the origin and every plane through the origin in ℝ³ is a subspace.
- The intersection of two subspaces is a subspace.

> **Quick Recall:**
> - Vector space = set with addition and scalar multiplication, plus 8 axioms.
> - Subspace = subset that is itself a vector space — must contain 0 and be closed under +, ·.
> - Lines/planes through the origin are subspaces; offset lines/planes are not.

### Connections
- Builds on: 6.2 Vector operations.
- Sets up: 6.6 Linear Dependence and 6.7 Generators / Basis.

### Open Questions
1. How do the eight axioms fail for a subset that is missing the zero vector? (Answer: closure-under-scalar-multiplication-by-0 forces 0 ∈ W; missing 0 ⇒ not closed.)


---


## Section: 6.6 Linear Dependence of Vectors 🔴

### Core Idea
A set of vectors x¹, x², …, xⁿ is **linearly dependent** if there exist scalars c₁, …, cₙ — *not all zero* — such that c₁x¹ + c₂x² + … + cₙxⁿ = **0** (the null vector). If no such non-zero scalars exist (i.e. only c₁ = c₂ = … = cₙ = 0 works), the vectors are **linearly independent**. The word "linear" is essential — only scalar multiplication and vector addition are allowed in producing the null vector.

> **In Simple Terms:** A set of vectors is "dependent" if at least one of them is *redundant* — you can build it from the others. They're "independent" if **every** vector adds new direction; none is a leftover combination of its peers.

### Definitions
- **Linearly dependent set** ⭐: ∃ c₁, …, cₙ not all zero with Σ cᵢ xⁱ = 0.
- **Linearly independent set** ⭐: Σ cᵢ xⁱ = 0 ⇒ every cᵢ = 0.

### Two key results
| Result | Statement |
|--------|-----------|
| (a) Subset-dependence ⇒ whole set dependent | If a subset {x¹, …, x^k} of {x¹, …, xⁿ}, k < n, is linearly dependent, then the whole set {x¹, …, xⁿ} is also linearly dependent. |
| (b) Whole-set independence ⇒ subset independent | If {x¹, …, xⁿ} is linearly independent, then any subset {x¹, …, x^k}, k < n, is also linearly independent. |

### Examples (from source)
1. **Two-vector dependence**: x = (1, 0, 3)ᵀ, y = (3, 0, 9)ᵀ. Check 3x − y = (3, 0, 9)ᵀ − (3, 0, 9)ᵀ = **0**. Coefficients (3, −1) are non-zero ⇒ x and y are linearly dependent. Equivalently y = 3x.
2. **Three-vector dependence**: x = (1, 3)ᵀ, y = (−2, 5)ᵀ, z = (3, −2)ᵀ. Check x − y − z = (1, 3)ᵀ − (−2, 5)ᵀ − (3, −2)ᵀ = (1 + 2 − 3, 3 − 5 + 2)ᵀ = (0, 0)ᵀ. So z = x − y.

### General fact
If k vectors x¹, …, x^k are dependent, then any vector with non-zero coefficient in the dependence equation can be written as a **linear combination** of the rest.

### ⚠️ Common Mistakes
- ❌ Stating "all coefficients are non-zero" → ✅ The definition needs *not all zero* — at least one cᵢ ≠ 0 suffices.
- ❌ Allowing non-linear (e.g. quadratic) operations to test dependence → ✅ Only scalar multiplication + vector addition are admissible.

> **Quick Recall:**
> - Dependent ⇔ some non-trivial Σ cᵢ xⁱ = 0. ⭐
> - Subset dependent ⇒ whole set dependent.
> - Whole set independent ⇒ every subset independent.
> - Dependence means at least one vector is a linear combination of the others.

### Connections
- Builds on: 6.2 Vector addition / scalar multiplication; 6.5 Vector spaces.
- Sets up: 6.7 Generators and Basis (which require linear independence).

---

## Section: 6.7 Generators and Basis 🔴

### Core Idea
A set of vectors {a₁, a₂, …, aₙ} from Eⁿ **generates** (or **spans**) Eⁿ if **every** vector in Eⁿ can be written as a linear combination of the aᵢ. If the generators are *also linearly independent*, they form a **basis**. In E² (the plane) we need **at least two** vectors to generate; if these two are linearly independent, **exactly two** suffice and they form a basis. The same logic generalises: Eⁿ needs at least n vectors to generate, and exactly n linearly-independent vectors to form a basis.

> **In Simple Terms:** **Generators** are a "complete toolbox" — you can build *every* vector from them, even if some tools duplicate others. A **basis** is the *minimal* toolbox — every vector you can build, with no redundant tools.

### Definitions
- **n-dimensional Euclidean space Eⁿ** ⭐: the collection of all n-tuples a = (a₁, …, aₙ), aᵢ ∈ ℝ, with vector addition, scalar multiplication, and a notion of distance.
- **Generators / Spanning set** ⭐: a set {a₁, …, aₙ} ⊂ Eⁿ such that every x ∈ Eⁿ can be written as x = Σ cᵢ aᵢ for some scalars cᵢ.
- **Basis of Eⁿ** ⭐: a set of vectors that is (i) a generator of Eⁿ AND (ii) linearly independent.

### Key facts
- The generator set is **not unique** — many different sets of vectors can generate the same space.
- For Eⁿ, a generator needs **at least n** vectors.
- For Eⁿ, a basis has **exactly n** linearly-independent vectors.
- The **standard basis** of Eⁿ is e₁ = (1, 0, …, 0), e₂ = (0, 1, 0, …, 0), …, eₙ = (0, 0, …, 1).

### Examples
1. In E²: u = (1, 0)ᵀ, v = (0, 1)ᵀ. Any x = (x₁, x₂)ᵀ = x₁·u + x₂·v. So {u, v} generates E². They are also linearly independent ⇒ they form a basis.
2. **Multiple decompositions of the same vector** (2, 5)ᵀ:
   - = 2·(1, 0)ᵀ + 5·(0, 1)ᵀ
   - = 2·(1, 1)ᵀ + 3·(0, 1)ᵀ
   - = 1·(1, 0)ᵀ + 1·(1, 1)ᵀ + 4·(0, 1)ᵀ
   - = 2·(1, 2)ᵀ + 1·(0, 1)ᵀ + 3·(0, 1)ᵀ
   So pairs {(0,1)ᵀ, (1,0)ᵀ}, {(1,1)ᵀ, (0,1)ᵀ}, {(1,0)ᵀ, (1,1)ᵀ}, {(1,2)ᵀ, (1,1)ᵀ}, … each generate E².
3. **Basis for E³**: e₁ = (1, 0, 0), e₂ = (0, 1, 0), e₃ = (0, 0, 1). The vector a = (2, 3, 4) has the unique representation a = 2e₁ + 3e₂ + 4e₃. ⭐

### Three points to remember
1. An *arbitrary* choice of u, v need not generate all of E² — they must be linearly independent (else they span only a line).
2. In E² we need **at least 2** vectors; in Eⁿ at least n.
3. The choice of generators is not unique — there are infinitely many spanning sets.

### ⚠️ Common Mistakes
- ❌ Picking two parallel vectors (one a scalar multiple of the other) and calling them a basis of E² → ✅ A basis must be linearly *independent*; parallel vectors span only a line, not the whole plane.

> **Quick Recall:**
> - **Span / Generate**: every vector in Eⁿ can be written as Σ cᵢ aᵢ.
> - **Basis** = generators + linearly independent. ⭐
> - dim(Eⁿ) = n; any basis has exactly n vectors.

### Connections
- Builds on: 6.5 Vector Spaces, 6.6 Linear Dependence.
- Sets up: Unit 7 (representing systems of equations using basis vectors of Eⁿ).

---

## Section: 6.8 Let Us Sum Up 🟢

### Unit 6 wrap-up
This unit presented the **vector** as the natural object for variables that carry both magnitude and direction. It covered:
- Basic operations: vector addition, subtraction, scalar multiplication.
- Geometric / physical interpretations (length, direction, free vectors, displacement).
- **Norm** ‖a‖ and **inner product** ⟨a, b⟩ — the algebraic side of "length" and "angle".
- **Vector space** axioms and the notion of a **subspace**.
- **Linear dependence** vs **independence**.
- **Generators** of a space and the **basis** as a minimal generator.
- A preview of how vectors connect to matrices (and via matrices to characteristic equations / eigen values / eigen vectors — the topic of Unit 7).

---

## Section: 6.9 Key Words 🟢

### Definitions captured here (recap)
- **Basis**: any (two) linearly-independent vectors in E² that generate the elements of E². (Generalises to "n linearly-independent vectors" in Eⁿ.)
- **Generator** ⭐: a set {u, v, w, …} such that every x = (x₁, x₂)ᵀ can be expressed as x = c₁u + c₂v + c₃w + … for suitable scalars cᵢ.
- **Sub-space** ⭐: W is a sub-space of V iff (a) W ⊆ V and (b) W is itself a vector space (i.e. satisfies all the V-space axioms).
- **Vector space (over ℝ)** ⭐: the set V = {(x₁, …, xₙ) : xᵢ ∈ ℝ} satisfying:
  i. ∀ x, y, z ∈ V: x + y ∈ V; x + y = y + x; x + (y + z) = (x + y) + z; ∃ 0 ∈ V with x + 0 = x.
  ii. ∀ λ, θ, δ ∈ ℝ, x ∈ V: λ·x ∈ V; λ·(δ·x) = (λδ)·x; λ·(δ·x) = δ·(λ·x); 1·x = x.
  iii. Distributivity: λ·(θ + δ)·x = (λ·θ + λ·δ)·x; λ·(x + y) = λ·x + λ·y.
- **Vector** ⭐: an ordered set (a, b) with a, b as elements; "ordered" means (a, b) ≠ (b, a) generically.

---

## Section: 6.10 Answers / Hints to Check Your Progress 🟡

### Check Your Progress 1 (vector arithmetic — answers)
- (1) a₁ + 2a₂ + 3a₃ = (5, 3, 7, 9). [Compute component-wise from the supplied a₁, a₂, a₃.]
- (2) 2x₂ + 5x₃ − x₁ = (3, −11, −3). [Component-wise scalar multiply, then add/subtract.]

### Check Your Progress 2 (norm & inner product — answers)
- (1) Sketching difference / scalar-multiple — *do yourself*.
- (2) Norms: (i) ‖(2, 5)‖ = √29 — but the source's printed answer (square of norm) is **9** (matches √(2² + 5²)² interpreted as 4 + 25 = 29? Likely a misprint; correct ‖(2, 5)‖ = √29 ≈ 5.39); (ii) ‖(1, 2, 3)‖ = √14, source prints **8** (similarly check). The textbook's printed answers in this section appear inconsistent — *trust the formula ‖a‖ = √Σaᵢ² rather than the printed numbers*.
- (3) Inner products: (a) ⟨(2, 3, 4), (4, 5, 6)⟩ = 8 + 15 + 24 = **47**. Source prints 43 — recompute: 2·4 + 3·5 + 4·6 = 8 + 15 + 24 = 47, so the source's "43" appears to be a typo (the printed answer **43**/**−47** suggests sign or arithmetic confusion). (b) ⟨(−2, −3, 4), (4, 5, −6)⟩ = −8 − 15 − 24 = **−47**.

### ⚠️ Common Mistakes
- ❌ Trusting printed numerical answers blindly → ✅ Always recompute the inner product / norm from the formulas (Σ aᵢbᵢ and √Σ aᵢ²) — printed answers in this textbook are occasionally inconsistent.

---

## Section: 6.11 Exercises (worked-out problems) 🔴

### Q1 — Norms of given vectors
Find ‖a‖² for the vectors below (the printed "Ans" gives **squared** norms, not norms themselves — keep that convention):
- (i) a = (0, 2, 1): ‖a‖² = 0 + 4 + 1 = **5**.
- (ii) b = (6, 3, 2): ‖b‖² = 36 + 9 + 4 = **49**.
- (iii) c = (−5, 4, 3): ‖c‖² = 25 + 16 + 9 = **50**.
- (iv) d = (0, 0, 1): ‖d‖² = 0 + 0 + 1 = **1**.
- (v) e = (−3, −4, −2): ‖e‖² = 9 + 16 + 4 = **29**.

### Q2 — Vector differentiation (linear form)
Given b = (3, −2, 1)ᵀ and x = (x₁, x₂, x₃)ᵀ, find ∂(b'x)/∂x.

Compute b'x = 3x₁ − 2x₂ + x₃. Then:
**∂(b'x)/∂x = b = (3, −2, 1)ᵀ.** ⭐

(General rule: ∂(b'x)/∂x = b.)

### Q3 — Vector differentiation (linear form, parameter c)
Given c = (c² + 1, 3c, 4c − 5, c³)ᵀ and x = (x₁, x₂, x₃, x₄)ᵀ. Find ∂(c'x)/∂x.

By the same rule:
**∂(c'x)/∂x = c = (c² + 1, 3c, 4c − 5, c³)ᵀ.**

### Q4 — Vector differentiation of a vector function
y = (x₁² + 3x₂, 2x₁x₂ − x₂, 2x₁ + x₁x₂ − 3x₂², 3x₁² − x₁²x₂ − x₂³)ᵀ. Find ∂y/∂x = the **Jacobian matrix** [∂yᵢ/∂xⱼ].

Answer (entries: row i = ∂yᵢ/∂x_j for j = 1, 2):
| ∂y/∂x | ∂/∂x₁ | ∂/∂x₂ |
|-------|-------|-------|
| y₁    | 2x₁  | 3 |
| y₂    | 2x₂  | 2x₁ − 1 |
| y₃    | 2 + x₂ | x₁ − 6x₂ |
| y₄    | 6x₁ − 2x₁x₂ | −x₁² − 3x₂² |

### Q5 — Vector differentiation of a bilinear form
x = (x₁, x₂, x₃)ᵀ, A = | 3 0 −1 ; 2 1 4 ; −1 0 3 |, y = (y₁, y₂, y₃)ᵀ. Find ∂(x'Ay)/∂x and ∂(x'Ay)/∂y.

Use the **bilinear rules**:
- ∂(x'Ay)/∂x = A·y.
- ∂(x'Ay)/∂y = A'·x.

Source's "Ans": A·y = (3y₁ − y₃, 2y₁ + y₂ + 4y₃, −y₁ + 3y₃)ᵀ. ⭐

> **Quick Recall (Unit 6):**
> - **Linear dependence** ⇔ Σ cᵢxⁱ = 0 with not-all-zero cᵢ. ⭐
> - **Generators** of Eⁿ: at least n vectors; **basis** = exactly n linearly-independent vectors. ⭐
> - **Standard basis of Eⁿ**: {e₁, …, eₙ}.
> - **Bilinear-form derivatives**: ∂(b'x)/∂x = b; ∂(x'Ay)/∂x = A·y; ∂(x'Ay)/∂y = A'·x. ⭐
> - In Eⁿ: dim = n; every basis has exactly n vectors.

### Connections
- Closes Unit 6.
- Bridges into Unit 7 (eigenvalue problem on n×n matrices uses Eⁿ vectors and basis representation).

---

## Section: UNIT 7 — VECTORS AND MATRICES — 7.0 Objectives 🟢

After Unit 7, the student should be able to:
- Present a **system of linear equations** as a **matrix equation** AX = d.
- Explain the concepts of **characteristic matrix**, **characteristic vector**, **characteristic root**, **eigen vector**, **eigen value**, and define the **characteristic value problem**.
- Identify the concept of **quadratic form**.
- Present various types of quadratic forms.
- Discuss the relation of **eigen values** to **definiteness** of a quadratic form.
- Explain the concept of **vector differentiation** and describe the processes for various types (linear, vector-of-functions, quadratic, bilinear).

### Connections
- Builds on: Unit 5 (matrices, determinants, rank), Unit 6 (vectors, norm, basis).
- Sets up: Block 3 / further courses on optimisation (where Hessians, definiteness, and eigenvalues drive second-order conditions).

---

## Section: 7.1 Introduction — finite-dimensional real vectors 🟢

### Core Idea
Unit 7 restricts to **finite-dimensional real vectors** — n-tuples (x₁, …, xₙ) with xᵢ ∈ ℝ. The all-zero n-tuple is the **null vector**. In economic analysis, the quantities of various commodities consumed by an individual can be represented as a vector — making vectors and matrices the natural language for systems with many goods or constraints.

### Connections
- Echoes 6.1 (vector vs scalar) and prepares the matrix-form representation of equation systems.

---

## Section: 7.2 Vectors and Matrices (matrix representation of linear systems) 🔴

### Core Idea
A system of m linear equations in n variables can be packaged as the **matrix equation AX = d**, where A is the m×n coefficient matrix, X is the n×1 variable vector, and d is the m×1 constant vector. This compresses a sprawling equation system into one symbolic statement and unlocks the entire matrix toolkit (inverse, rank, determinants, Cramer's rule) for solving it.

> **In Simple Terms:** Instead of writing m separate equations, stack the coefficients into A, the unknowns into X, the constants into d — and the *whole* system is just one symbol-equation: **AX = d**.

### Definitions
- **Coefficient matrix A** (m×n): A = [aᵢⱼ]; row i = coefficients of equation i; column j = coefficients of variable xⱼ across all equations.
- **Variable vector X** (n×1): X = (x₁, x₂, …, xₙ)ᵀ.
- **Constant vector d** (m×1): d = (d₁, d₂, …, dₘ)ᵀ.

### Example (from source)
The system
- 6x₁ + 3x₂ + x₃ = 22
- x₁ + 4x₂ − 2x₃ = 12
- 4x₁ − x₂ + 5x₃ = 10

becomes:
| 6  3  1 |   | x₁ |   | 22 |
| 1  4 −2 | · | x₂ | = | 12 |
| 4 −1  5 |   | x₃ |   | 10 |

i.e. **AX = d** with A as the 3×3 coefficient block.

### Connections
- Builds on: Unit 5 §5.3 (matrix arithmetic) and §5.7 Cramer's rule worked examples.
- Sets up: 7.3 (when AX = λX — the eigenvalue problem).

---

## Section: 7.3 Characteristic Value Problem 🔴

### Core Idea
For a square matrix A of order n, the **characteristic value problem** asks: which scalars λ admit a *non-zero* vector x such that **Ax = λx**? Geometrically, A acts on x and only stretches it (by factor λ) without rotating it — x is a *direction-preserving* vector for A. λ is then called the **characteristic value / eigen value / proper value / characteristic root**, and x the corresponding **characteristic vector / eigen vector**.

> **In Simple Terms:** Most vectors get rotated when you hit them with A. **Eigen vectors** are the special directions where A only **scales** the vector — the scaling factor is the **eigen value**.

### Definitions
- **Eigen value (characteristic value, characteristic root, proper value) λ** ⭐: scalar satisfying Ax = λx for some x ≠ 0.
- **Eigen vector (characteristic vector) x** ⭐: a non-zero x with Ax = λx.
- **Characteristic matrix** ⭐: the matrix [A − λI].

### Connections
- Builds on: Unit 5 (rank, determinants, AX = d).
- Sets up: 7.3.1 (turning the eigen problem into a polynomial equation in λ).

---

## Section: 7.3.1 Characteristic Equation 🔴

### Core Idea
Rewrite Ax = λx as **(A − λI)x = 0** — a homogeneous system. A non-zero solution exists iff the coefficient matrix is rank-deficient, i.e. iff **|A − λI| = 0**. Expanding this determinant gives an n-th degree polynomial in λ, called the **characteristic polynomial**, and the equation |A − λI| = 0 is the **characteristic equation**. Its n roots (real or complex, distinct or repeated) are the eigen values of A.

### Definitions
- **Characteristic polynomial** ⭐: the determinant |A − λI| viewed as a polynomial in λ.
- **Characteristic equation** ⭐: |A − λI| = 0.

### Mechanism (recipe)
1. Form A − λI (subtract λ from each diagonal entry of A).
2. Compute the determinant |A − λI|.
3. Set it to 0 and solve the resulting polynomial in λ.
4. The n roots are the eigen values λ₁, …, λₙ.

### Example (2×2 generic)
For A = | a₁₁ a₁₂ ; a₂₁ a₂₂ |:

|A − λI| = | a₁₁−λ  a₁₂ ; a₂₁  a₂₂−λ | = (a₁₁ − λ)(a₂₂ − λ) − a₁₂a₂₁
        = λ² − (a₁₁ + a₂₂)λ + (a₁₁a₂₂ − a₁₂a₂₁) = 0.

This is a **quadratic** in λ. ⭐

### Note
For order-n matrix A, |A − λI| = 0 has n roots, which may be: real or complex, distinct or repeated, zero or non-zero.

### Connections
- Builds on: Unit 5 — determinants, rank, homogeneous systems.
- Sets up: 7.3.2 (sum/product of roots gives quick checks).

---

## Section: 7.3.2 Sum and Product of Roots 🔴

### Core Idea
Writing the characteristic polynomial as c₀λⁿ + c₁λⁿ⁻¹ + c₂λⁿ⁻² + … + cₙ₋₁λ + cₙ = 0 (with c₀ = 1), Vieta-style root-coefficient relations give two extremely useful identities:
- Sum of eigen values = **trace(A)** = Σ aᵢᵢ. ⭐
- Product of eigen values = **|A|** (the determinant). ⭐

### Coefficient-of-the-characteristic-polynomial formulas
- c₀ = 1.
- c₁ = −Σᵢ aᵢᵢ = −trace(A). [So Σλᵢ = −c₁/c₀ = trace(A).]
- cⱼ = (−1)^j · (sum of all principal minors of A of order j).
- cₙ = (−1)^n · |A|. [So Πλᵢ = cₙ/c₀ · (−1)^n compensation = |A|.]

### Quick checks
| Identity | Statement | Use |
|----------|-----------|-----|
| Σ λᵢ = trace(A) | sum of all eigen values = sum of diagonal entries | sanity-check eigen-value computations |
| Π λᵢ = |A|     | product of all eigen values = determinant | catches sign errors |

### Worked example (2×2)
A = | 2 1 ; 1 2 |.

Characteristic equation: |A − λI| = (2 − λ)² − 1 = 0 ⇒ 4 − 4λ + λ² − 1 = 0 ⇒ **λ² − 4λ + 3 = 0**.
λ = (4 ± √(16 − 12))/2 = (4 ± 2)/2 ⇒ **λ₁ = 3, λ₂ = 1**.

Check: Σλ = 3 + 1 = 4 = a₁₁ + a₂₂ = 2 + 2 = 4 ✓; Πλ = 3 = |A| = 4 − 1 = 3 ✓.

### Properties of eigen values (general)
i. If A is **singular** (|A| = 0), then at least one eigen value of A is 0. ⭐
ii. If A is **real symmetric**, all eigen values are real (no complex roots). ⭐
iii. If λ₁, …, λₙ are eigen values of a non-singular A, then 1/λ₁, …, 1/λₙ are eigen values of **A⁻¹**.
iv. If A and B commute (AB = BA), with eigen values λᵢ and μᵢ, then AB has eigen values λᵢ μᵢ.
v. The eigen values of a **diagonal or triangular matrix** are exactly its diagonal elements.
vi. If λ₁, …, λₙ are eigen values of A, and k ∈ ℤ, then **A^k** has eigen values λ₁^k, …, λₙ^k.

### ⚠️ Common Mistakes
- ❌ Forgetting to subtract λ on **every** diagonal element of A → ✅ A − λI has λ subtracted from each diagonal entry, off-diagonal entries unchanged.

> **Quick Recall:**
> - **Σ λᵢ = trace(A)** and **Π λᵢ = |A|**. ⭐
> - Real-symmetric ⇒ real eigen values; diagonal/triangular ⇒ eigen values are diagonal entries.
> - λ(A⁻¹) = 1/λ(A); λ(A^k) = λ(A)^k.

### Connections
- Builds on: 7.3.1 (the polynomial whose coefficients these identities use).
- Sets up: 7.3.3 (using each λᵢ to find the matching eigen vector).

---

## Section: 7.3.3 Characteristic Vector 🔴

### Core Idea
Once an eigen value λᵢ is known, the corresponding eigen vector xⁱ is found by **substituting λᵢ into (A − λI)x = 0** and solving the resulting homogeneous system. Because [A − λᵢI] has rank < n (by construction), the solution is *non-trivial but not unique* — the eigen vector is determined only up to a scalar multiple. A standard convention is to **normalise** so that ‖xⁱ‖ = 1.

> **In Simple Terms:** Each eigen value gives you a *direction*, not a single specific vector. You pick any non-zero point on that line; people usually scale it to length 1 for tidiness.

### Mechanism (recipe)
1. For each λᵢ, form A − λᵢI.
2. Solve (A − λᵢI)·xⁱ = 0 — a homogeneous system with infinitely many solutions.
3. Pick any non-zero solution; **normalise** if desired so ‖xⁱ‖ = 1.

### Worked example (continuing 7.3.2 example)
A = | 2 1 ; 1 2 |, λ₁ = 3, λ₂ = 1.

For λ₁ = 3: A − 3I = | −1 1 ; 1 −1 |. Equations: −x₁¹ + x₂¹ = 0; x₁¹ − x₂¹ = 0. Both give **x₁¹ = x₂¹**. Set x₁¹ = 1 ⇒ x¹ = (1, 1)ᵀ.

For λ₂ = 1: A − I = | 1 1 ; 1 1 |. Equations: x₁² + x₂² = 0 ⇒ **x₂² = −x₁²**. Set x₁² = 1 ⇒ x² = (1, −1)ᵀ.

**Normalised** (‖xⁱ‖ = 1): x¹ = (1/√2, 1/√2)ᵀ, x² = (1/√2, −1/√2)ᵀ.

**Note**: ⟨x¹, x²⟩ = 1/2 − 1/2 = 0 ⇒ the two eigen vectors are **orthogonal**. ⭐ (This is a general property of real symmetric matrices — confirmed in 7.3.4.)

### ⚠️ Common Mistakes
- ❌ Reading "xⁱ" as "x raised to power i" → ✅ Here the superscript is just a label for the i-th eigen vector, **not** an exponent.

> **Quick Recall:**
> - Solve (A − λI)x = 0 for each eigen value λ to get its eigen vector(s).
> - Eigen vectors are determined only up to a non-zero scalar multiple.
> - Normalise: divide by ‖x‖ so the length is 1.
> - For real symmetric A, eigen vectors of distinct eigen values are orthogonal. ⭐

### Connections
- Builds on: Unit 5 §5.3.7 (rank and homogeneous systems with non-trivial solutions when |A − λI| = 0).
- Sets up: 7.3.4 Diagonalisation.

---

## Section: 7.3.4 Diagonalisation (introduction) 🔴

### Core Idea
For a real symmetric matrix A, all eigen values are real **and** the corresponding eigen vectors are mutually orthogonal. Stacking the n normalised eigen vectors as columns of a matrix P gives an **orthogonal matrix** (P'P = I), and PᵀAP becomes a **diagonal matrix** with the eigen values along the diagonal — i.e. A is **diagonalisable** by P. (Full statement and worked computations continue in chunk 6.)

<!-- Continues in chunk 006 -->

### Connections
- Builds on: 7.3.3 (eigen vectors), 5.3.5 (orthogonal matrices: AᵀA = I, |A| = ±1).
- Sets up: 7.4 Linear Independence of Eigen Vectors and 7.5 Quadratic Forms.

### Open Questions
1. What guarantees that the eigen vectors of a non-symmetric real matrix can still form a basis (i.e. that A is diagonalisable)? (Answer: all eigen values must be distinct, or each repeated eigen value must have geometric multiplicity equal to its algebraic multiplicity — covered next chunk.)


---


## Section: 7.3.4 Diagonalisation (worked) 🔴
<!-- See chunk 005 for start of this section -->

### Core Idea
A real symmetric matrix A is **diagonalisable by an orthogonal matrix P**: stack its **n normalised, mutually orthogonal eigen vectors** as the columns of P, and PᵀAP becomes the **diagonal matrix Λ** whose diagonal entries are the eigen values of A. This is the key reduction that converts an A-action problem into n independent scalar problems — the foundation for principal-component analysis, decoupling of differential equations, and (in the next section) signing quadratic forms.

> **In Simple Terms:** Diagonalising A means rotating the coordinate system so that A acts by **independent scaling along each new axis** — no cross-terms, no rotation, just stretches.

### Mechanism (worked example, continuing 7.3.3)
A = | 2 1 ; 1 2 |, λ₁ = 3, λ₂ = 1; normalised eigen vectors x¹ = (1/√2, 1/√2)ᵀ, x² = (1/√2, −1/√2)ᵀ.

1. Form P = [x¹  x²] = | 1/√2  1/√2 ; 1/√2  −1/√2 |.
2. Verify orthogonality: PᵀP = I ⇒ P is **orthogonal**. ⭐
3. Compute PᵀAP:
   PᵀAP = | 1/√2  1/√2 ; 1/√2  −1/√2 | · | 2 1 ; 1 2 | · | 1/√2  1/√2 ; 1/√2  −1/√2 | = | 3 0 ; 0 1 | = | λ₁ 0 ; 0 λ₂ | = **Λ**. ✓

### Definitions
- **Diagonalisation** ⭐: PᵀAP = Λ where P is orthogonal (columns = normalised eigen vectors) and Λ is diagonal with eigen values.

> **Quick Recall:**
> - Real-symmetric A ⇒ A is **orthogonally diagonalisable**: PᵀAP = Λ. ⭐
> - Λ's diagonal entries are the eigen values; P's columns are the corresponding orthonormal eigen vectors.

### Connections
- Builds on: 7.3.3 (eigen vectors), 5.3.5 (orthogonal matrices).
- Sets up: 7.4 Linear independence of eigen vectors, 7.5 Quadratic forms, 7.6 Definiteness.

---

## Section: 7.4 Linear Independence of Eigen Vectors 🔴

### Core Idea
If a matrix A has **n distinct** eigen values λ₁, …, λₙ, then the corresponding eigen vectors x¹, …, xⁿ are automatically **linearly independent** (and form a basis of Eⁿ). Distinctness is *sufficient but not necessary*: even with repeated eigen values, one can sometimes still find n linearly independent eigen vectors. Moreover, when two eigen values are distinct, their eigen vectors are **orthogonal** (a stronger property than mere independence — for real symmetric A this is automatic).

### Two key facts
| Fact | Statement |
|------|-----------|
| Distinct ⇒ independent | λ₁, …, λₙ all distinct ⇒ x¹, …, xⁿ are linearly independent. ⭐ |
| Distinct ⇒ orthogonal (real symmetric) | If two eigen values are distinct, the corresponding eigen vectors of a real symmetric matrix are orthogonal. ⭐ |

### Note on repeated roots
- Repeated eigen values do *not* automatically prevent the existence of n linearly independent eigen vectors (e.g. the n×n identity matrix I has the single eigen value 1 of multiplicity n but every basis of Eⁿ is a set of eigen vectors for I).
- When repeated roots admit fewer than the multiplicity in independent eigen vectors, A is **defective** (not diagonalisable) — but this case is beyond Unit 7.

> **Quick Recall:**
> - Distinct eigen values ⇒ independent eigen vectors (sufficient, not necessary). ⭐
> - Real symmetric + distinct eigen values ⇒ orthogonal eigen vectors. ⭐

### Connections
- Builds on: 6.6 (linear independence), 7.3.3 (eigen vectors).
- Sets up: 7.3.4 generalised — n independent eigen vectors fill the columns of P for diagonalisation.

---

## Section: 7.5 Quadratic Forms 🔴

### Core Idea
A **quadratic form** is a homogeneous polynomial of degree 2 in n variables: Q(x₁, …, xₙ) = Σᵢ Σⱼ aᵢⱼ xᵢxⱼ. Equivalently, in matrix form, **Q(x) = x'Ax** for a symmetric n×n matrix A. A quadratic form's *sign behaviour* across all x ∈ ℝⁿ classifies it as **positive definite**, **positive semi-definite**, **negative definite**, **negative semi-definite**, or **indefinite** — the central question for second-order conditions in optimisation.

> **In Simple Terms:** A quadratic form is a "weighted square" in many variables. Some weight choices keep the result **always positive** (a bowl), some **always negative** (an inverted bowl), and others can swing both ways (a saddle). Definiteness names the bowl shape.

### Definitions
- **Quadratic form (2 variables)**: Q(x₁, x₂) = a₁₁x₁² + 2a₁₂x₁x₂ + a₂₂x₂² ⭐ (note the **2a₁₂** captures the off-diagonal symmetry — half the coefficient sits in each off-diagonal entry).
- **Quadratic form (n variables)** ⭐: Q(x) = x'Ax = Σᵢ Σⱼ aᵢⱼ xᵢxⱼ for a symmetric A.
- **Positive definite (PD)** ⭐: Q(x) > 0 ∀ x ≠ 0.
- **Positive semi-definite (PSD)** ⭐: Q(x) ≥ 0 ∀ x.
- **Negative definite / semi-definite**: same with reversed inequality.
- **Indefinite**: Q takes both positive and negative values for different x.

### Examples (from source)
1. Q(x₁, x₂) = x₁² − 4x₁x₂ + 4x₂² = **(x₁ − 2x₂)²** ≥ 0. Hence Q ≥ 0 for all x — **positive semi-definite** (zero on the line x₁ = 2x₂, positive elsewhere).
2. Q(x₁, x₂) = −10x₁² + 6x₁x₂ − x₂² = −x₁² − (3x₁ − x₂)² ≤ 0. **Negative semi-definite**.

### Sign analysis for the 2-variable form (completing-the-square)
Q(x₁, x₂) = a₁₁x₁² + 2a₁₂x₁x₂ + a₂₂x₂²
        = a₁₁ [(x₁ + (a₁₂/a₁₁)x₂)² + ((a₁₁a₂₂ − a₁₂²) / a₁₁²) · x₂²]
        = a₁₁(x₁ + (a₁₂/a₁₁)x₂)² + ((a₁₁a₂₂ − a₁₂²) / a₁₁) · x₂².

So **Q(x) > 0 for all x ≠ 0** iff:
- a₁₁ > 0 AND
- (a₁₁a₂₂ − a₁₂²) / a₁₁ > 0, i.e. a₁₁a₂₂ − a₁₂² > 0 (the **determinant of A** is positive). ⭐

These are **necessary and sufficient** for a 2×2 symmetric A to be **positive definite**.

### Sign-classification table (2×2 case)
| Sign of a₁₁ | Sign of |A| = a₁₁a₂₂ − a₁₂² | Definiteness |
|-------------|--------------------------------|--------------|
| > 0         | > 0                            | Positive definite |
| ≥ 0         | = 0                            | Positive semi-definite |
| < 0         | > 0                            | Negative definite |
| ≤ 0         | = 0                            | Negative semi-definite |
| any         | < 0                            | Indefinite |

### ⚠️ Common Mistakes
- ❌ Treating "2a₁₂x₁x₂" as if both off-diagonal entries equal 2a₁₂ → ✅ A is symmetric with a₁₂ = a₂₁, and the cross term in Q expands to **2** a₁₂ x₁x₂ (one from each off-diagonal entry).

> **Quick Recall:**
> - Q(x) = x'Ax with A symmetric. ⭐
> - PD (2×2): a₁₁ > 0 AND |A| > 0.
> - PSD (2×2): a₁₁ ≥ 0 AND |A| = 0.
> - ND (2×2): a₁₁ < 0 AND |A| > 0.
> - Indefinite: |A| < 0.

### Connections
- Builds on: 5.3.5 (symmetric matrices).
- Sets up: 7.6 (eigen-value criterion for definiteness).

---

## Section: 7.6 Definiteness and Eigen Values 🔴

### Core Idea
The **sign of all eigen values** of A is the universal definiteness criterion (replacing the leading-principal-minor test with one that scales to n×n). For Q(x) = x'Ax:
- **Positive definite** ⇔ all λᵢ > 0.
- **Positive semi-definite** ⇔ all λᵢ ≥ 0 (and at least one = 0 ⇔ |A| = 0).
- **Negative definite** ⇔ all λᵢ < 0.
- **Negative semi-definite** ⇔ all λᵢ ≤ 0.
- **Indefinite** ⇔ A has eigen values of both signs.

### Necessary-and-sufficient conditions (from source)
| Definiteness | Necessary & sufficient (matrix) | In terms of eigen values |
|--------------|-----------------------------------|---------------------------|
| Positive semi-definite | a₁₁ ≥ 0 AND |A| = 0 | λ₁ ≥ 0 AND λ₂ ≥ 0 |
| Negative semi-definite | a₁₁ ≤ 0 AND |A| = 0 | λ₁ ≤ 0 AND λ₂ ≤ 0 |
| Positive definite | a₁₁ > 0 AND |A| > 0 | λ₁ > 0 AND λ₂ > 0 ⭐ |
| Negative definite | a₁₁ < 0 AND |A| > 0 | λ₁ < 0 AND λ₂ < 0 |
| Indefinite | |A| < 0 | λ₁ and λ₂ have opposite signs |

### Why eigen values work
Diagonalise A with orthogonal P: x'Ax = x'(PΛPᵀ)x = (Pᵀx)' Λ (Pᵀx) = Σ λᵢ yᵢ² where y = Pᵀx. Since y² ≥ 0 always, the **sign behaviour of Q is determined entirely by the signs of the λᵢ**.

### ⚠️ Common Mistakes
- ❌ Reading "all eigen values positive" off the diagonal of A directly → ✅ Diagonal entries are *not* eigen values unless A is itself diagonal/triangular; you must solve |A − λI| = 0.

> **Quick Recall:**
> - Sign of eigen values ⇒ definiteness of Q. ⭐
> - PD ⇔ all λ > 0; ND ⇔ all λ < 0; PSD/NSD allow zero; indefinite ⇔ mixed signs.

### Connections
- Builds on: 7.3.4 (diagonalisation explains *why* the eigen values determine the form's sign).
- Sets up: optimisation (Hessian definiteness ↔ local max/min/saddle).

---

## Section: 7.7 Vector Differentiation 🔴

### Core Idea
Many maximisation/minimisation problems in linear algebra have objective functions written as **scalar-valued or vector-valued functions of a vector x**. **Vector differentiation** assigns a derivative that is again a vector or matrix, by collecting partial derivatives in a structured way. This unit treats four canonical cases: **linear functions** (a'x), **vectors of functions** (y(x)), **quadratic forms** (x'Ax), and **bilinear forms** (x'Bz). Higher-order derivatives are obtained by repeated application of the same rules.

### Connections
- Builds on: Block 1 partial differentiation; 7.5 Quadratic forms.

---

## Section: 7.7.1 Vector Differentiation of a Linear Function 🔴

### Definition + Rule
For a constant n-vector a and variable n-vector x, **a'x = a₁x₁ + a₂x₂ + … + aₙxₙ** is a scalar function of x.

The partial derivatives are: ∂(a'x)/∂xᵢ = aᵢ.

Stacking them gives:
**∂(a'x)/∂x = a.** ⭐

### Worked example (Check Your Progress 1, Q2)
a = (2a, −a, 3a, a)ᵀ ⇒ a'x = 2ax₁ − ax₂ + 3ax₃ + ax₄.
∂(a'x)/∂x₁ = 2a, ∂/∂x₂ = −a, ∂/∂x₃ = 3a, ∂/∂x₄ = a → ∂(a'x)/∂x = (2a, −a, 3a, a)ᵀ = a. ✓

> **Quick Recall:**
> - **∂(a'x)/∂x = a**. ⭐ — the gradient of a linear function is its coefficient vector.

---

## Section: 7.7.2 Vector Differentiation of a Vector of Functions 🔴

### Definition + Rule
Let y = (y₁(x), …, yₙ(x))ᵀ be an n-vector each component of which depends on x = (x₁, …, xₘ)ᵀ. Then **∂y/∂x is the m × n Jacobian matrix** with entries ∂yⱼ/∂xᵢ:

| ∂y/∂x  | y₁     | y₂     | …  | yₙ     |
|--------|--------|--------|----|--------|
| ∂/∂x₁  | ∂y₁/∂x₁ | ∂y₂/∂x₁ | …  | ∂yₙ/∂x₁ |
| ∂/∂x₂  | ∂y₁/∂x₂ | ∂y₂/∂x₂ | …  | ∂yₙ/∂x₂ |
| ⋮      | ⋮      | ⋮      | ⋱  | ⋮      |
| ∂/∂xₘ  | ∂y₁/∂xₘ | ∂y₂/∂xₘ | …  | ∂yₙ/∂xₘ |

### Worked example (from source)
y = (x₁² + 2x₂² − 3x₁x₃, 3x₁x₂² − x₂² + 4x₂x₃²)ᵀ. Then ∂y/∂x is a 3×2 matrix:

| ∂y/∂x  | y₁ = x₁² + 2x₂² − 3x₁x₃ | y₂ = 3x₁x₂² − x₂² + 4x₂x₃² |
|--------|--------------------------|-----------------------------|
| ∂/∂x₁  | 2x₁ − 3x₃               | 3x₂²                       |
| ∂/∂x₂  | 4x₂                     | 6x₁x₂ − 2x₂ + 4x₃²         |
| ∂/∂x₃  | −3x₁                    | 8x₂x₃                      |

> **Quick Recall:**
> - For y(x) of dimension n with x of dimension m: ∂y/∂x is an **m×n Jacobian** of partial derivatives.
> - This is the multivariate generalisation of the chain rule's "rate of change of each output w.r.t. each input".

---

## Section: 7.7.3 Vector Differentiation of a Quadratic Form 🔴

### Definition + Rule
For a symmetric n×n matrix A and a column vector x, **x'Ax** is a quadratic form. Expanding:

x'Ax = a₁₁x₁² + 2a₁₂x₁x₂ + 2a₁₃x₁x₃ + … + 2a₁ₙx₁xₙ + a₂₂x₂² + 2a₂₃x₂x₃ + … + 2a₂ₙx₂xₙ + … + aₙₙxₙ².

Taking partials:
∂(x'Ax)/∂xᵢ = 2(aᵢ₁x₁ + aᵢ₂x₂ + … + aᵢₙxₙ) = 2 · (i-th row of A) · x.

Stacking gives:
**∂(x'Ax)/∂x = 2Ax = 2x'A.** ⭐ (The two forms differ only in row-vs-column orientation.)

### Worked example (Check Your Progress 2, Q1)
x = (x₁, x₂, x₃)ᵀ, A = | 3 1 −2 ; 1 0 3 ; −2 3 2 |.

x'Ax = 3x₁² + 0·x₂² + 2x₃² + 2·1·x₁x₂ + 2·(−2)·x₁x₃ + 2·3·x₂x₃ = 3x₁² + 2x₃² + 2x₁x₂ − 4x₁x₃ + 6x₂x₃.

Partials:
- ∂/∂x₁ = 6x₁ + 2x₂ − 4x₃ ✓ (matches 2(Ax)₁).
- ∂/∂x₂ = 2x₁ + 6x₃.
- ∂/∂x₃ = 4x₃ − 4x₁ + 6x₂ = −4x₁ + 6x₂ + 4x₃.

So ∂(x'Ax)/∂x = 2Ax. ⭐

> **Quick Recall:**
> - **∂(x'Ax)/∂x = 2Ax** (or equivalently 2x'A). ⭐
> - Mirrors the scalar fact d(ax²)/dx = 2ax.

---

## Section: 7.7.4 Vector Differentiation of a Bi-linear Form 🔴

### Definition + Rule
For row x' (1×m), matrix B (m×n), column z (n×1), the scalar **x'Bz** is a **bilinear form** — linear in x for fixed z, and linear in z for fixed x. Its derivatives are:

| Derivative | Result |
|------------|--------|
| ∂(x'Bz)/∂x | **Bz** ⭐ |
| ∂(x'Bz)/∂z | **B'x** ⭐ |

These follow from the linear-function rule applied with the other variable held constant.

> **Quick Recall:**
> - **∂(x'Bz)/∂x = Bz**, **∂(x'Bz)/∂z = B'x**. ⭐
> - Compare 7.7.1: a'x is bilinear in (a, x) — these formulas reduce to ∂(a'x)/∂x = a when B is replaced by a column.

### Connections
- Builds on: 7.7.1 (linear case).
- Sets up: optimisation problems with separate primal-dual variables.

---

## Section: 7.8 Let Us Sum Up 🟢

### Unit 7 wrap-up
This unit:
1. Wrote a system of linear equations as a matrix equation **AX = d**.
2. Introduced the **eigen value problem** and the **characteristic equation** |A − λI| = 0.
3. Showed how eigen vectors are obtained, and how distinct eigen values force linearly-independent eigen vectors.
4. Defined **quadratic forms** Q(x) = x'Ax and connected their **definiteness** to the **signs of the eigen values** of A.
5. Developed **vector differentiation** for linear functions, vectors of functions, quadratic forms, and bilinear forms.

These tools support second-order conditions in multivariate optimisation (max ↔ negative definite Hessian; min ↔ positive definite; saddle ↔ indefinite).

---

## Section: 7.9 Key Words 🟢

### Definitions captured here (recap)
- **Characteristic equation** ⭐: For an n×n A, the equation |A − λI| = 0; the LHS expanded is the **characteristic polynomial**, an n-th degree polynomial in λ. Its roots are the eigen values.
- **Eigen value & eigen vector** ⭐: λ and x ≠ 0 with **Ax = λx**.
- **Quadratic form** ⭐: a₁₁x₁² + 2a₁₂x₁x₂ + a₂₂x₂² for given constants a₁₁, a₁₂, a₂₂ and real variables x₁, x₂. (Generalises to Q(x) = x'Ax for n variables.)

---

## Section: 7.10 Answers / Hints to Check Your Progress 🟡

### Check Your Progress 1 — answers
1. **Eigen value, eigen vector, characteristic equation** — see definitions in §7.3 and §7.3.1 above.
2. For a = (2a, −a, 3a, a)ᵀ: a'x = 2ax₁ − ax₂ + 3ax₃ + ax₄; partials are (2a, −a, 3a, a) which equals a. ⭐ This **proves ∂(a'x)/∂x = a** for this specific a, illustrating the general rule.

### Check Your Progress 2 — answers
1. With A as in Q1 (above): x'Ax = 3x₁² + 2x₃² + 2x₁x₂ − 4x₁x₃ + 6x₂x₃; partials are
   - ∂/∂x₁ = 6x₁ + 2x₂ − 4x₃,
   - ∂/∂x₂ = 2x₁ + 6x₃,
   - ∂/∂x₃ = −4x₁ + 6x₂ + 4x₃.
   These are the rows of 2Ax (= the entries of 2x'A reading as a row), confirming **∂(x'Ax)/∂x = 2x'A = 2Ax**. ⭐
2. Same logic applied to the second exercise's matrix.

---

## Section: 7.11 Exercises (cross-listed with §6.11) 🟡

The book reprints the same five vector-differentiation exercises as in §6.11 (Q1–Q5). Their answers were captured in chunk 005's notes — refer to those for:
- Q1 ‖a‖² of five vectors → (5, 49, 50, 1, 29).
- Q2 ∂(b'x)/∂x = b = (3, −2, 1)ᵀ.
- Q3 ∂(c'x)/∂x = c.
- Q4 ∂y/∂x as a 3×2 Jacobian.
- Q5 ∂(x'Ay)/∂x = Ay; ∂(x'Ay)/∂y = A'x.

> **Quick Recall (Unit 7):**
> - **AX = d** is the matrix form of any linear system. ⭐
> - **Ax = λx** ⇒ |A − λI| = 0 (characteristic equation). ⭐
> - **Σλᵢ = trace A**, **Πλᵢ = |A|**. ⭐
> - PD ⇔ all λ > 0; ND ⇔ all λ < 0; indefinite ⇔ mixed sign of λ. ⭐
> - **∂(a'x)/∂x = a**, **∂(x'Ax)/∂x = 2Ax**, **∂(x'Bz)/∂x = Bz, ∂(x'Bz)/∂z = B'x**. ⭐

### Connections
- Closes Unit 7.
- Bridges into Unit 8: now that AX = d has been introduced, the next unit asks **when** does it have a solution, **when** is it unique, and **how** to use rank/elementary-row-operations to decide.

---

## Section: UNIT 8 — VECTOR AND MATRIX REPRESENTATIONS OF LINEAR EQUATIONS — 8.0 Objectives 🟢

After Unit 8, the student should be able to:
- Explain the concept of a system of linear equations and its **matrix representation**.
- Discuss **elementary row operations** (EROs) on a matrix.
- Discuss and test for **linear independence** of m equations in n variables.
- Explain and test **consistency** of a system of linear equations.
- Use the concept of **rank** of a matrix for testing a given system for linear independence and consistency.

### Connections
- Builds on: Unit 5 (rank, matrix algebra), Unit 6 (independence, basis, span), Unit 7 (matrix-form AX = d).
- Sets up: solution-existence theorems and (in subsequent courses) Gauss elimination.

---

## Section: 8.1 Introduction 🟢

### Core Idea
Linear systems show up across engineering, physics, computer science, and economics. Even non-linear systems can often be **approximated by linear ones**. This unit focuses on three core questions: (i) What is a system of linear equations? (ii) Does every such system have a solution? (iii) If a solution exists, is it unique?

### Examples (from source)
- **Demand equation**: Demand = a − b·Price + c·Income; a, b, c are constants and Demand, Price, Income are variables — a linear equation in three variables.
- **Break-even calculation**: A firm prices at Rs. 30,000 per unit, faces fixed cost Rs. 5 lakh and marginal cost Rs. 5,000 per unit. The number n satisfying 30,000n = 5,00,000 + 5,000n (i.e. 25,000n = 5,00,000 ⇒ n = **20** units) is the break-even quantity.

### Connections
- Sets up: 8.2 (formal definitions: linear equation, system, solution).

---

## Section: 8.2 System of Linear Equations — 8.2.1 Linear Equation 🔴

### Definition
A **linear equation** is one in which:
- Each variable has degree ≤ 1.
- At least one variable has degree exactly 1.
- The coefficient of at least one degree-1 variable is non-zero.

### Examples (from source)
- 7x = 4 (one variable, two constants 7 and 4).
- a₁x₁ = b₁ (one variable, two parameters a₁ and b₁).
- a₁x₁ − 5x₂ = 11 (two variables x₁, x₂; parameter a₁; two constants −5 and 11).

### Geometric interpretation
Each linear equation in two variables represents a **straight line** in the 2-D coordinate plane — hence the name "linear".

### General form
**a₁x₁ + a₂x₂ + … + aₙxₙ = b** (linear equation in n variables).

<!-- Continues in chunk 007 -->

### Connections
- Builds on: high-school linear-equation algebra; 7.2 (matrix form).
- Sets up: 8.2.2 (solution of a linear equation), 8.2.3 (solution of a system).

### Open Questions
1. When does a homogeneous system Ax = 0 have a non-trivial solution? (Answered in 8.2.4: when rank(A) < n.)


---


## Section: 8.2.1 Linear Equation (concluded) 🟢
<!-- See chunk 006 for start of this section -->

### Final remarks
- The general linear equation a₁x₁ + a₂x₂ + … + aₙxₙ = b represents a **line in n-dimensional space** — a hyperplane when n ≥ 3.
- Throughout the unit, all variables, parameters, and constants are **real-valued** unless explicitly stated otherwise.

### Connections
- Builds on: 6.5 (subspaces are characterised by linear equations through the origin); 7.2 (matrix form).
- Sets up: 8.2.2 (defining a "solution" to such an equation).

---

## Section: 8.2.2 Solution of a Linear Equation 🔴

### Definition
A **solution** of the linear equation
**a₁x₁ + a₂x₂ + … + aₙxₙ = b** … (I)
is a set of n constant real (or complex) values c₁, c₂, …, cₙ such that, when each variable xⱼ is replaced by the corresponding constant cⱼ, the LHS equals b. ⭐

> **In Simple Terms:** A solution is a single tuple (c₁, …, cₙ) that, when plugged into the equation, makes it a true statement.

### Connections
- Sets up: 8.2.3 — "system of equations" requires the *same* tuple to solve every equation in the set.

---

## Section: 8.2.3 System of Linear Equations 🔴

### Core Idea
A **system of m linear equations in n variables** is a collection of m linear equations sharing the same variable list (x₁, …, xₙ), where the **same** value of each variable must be substituted in every equation simultaneously. This "shared substitution" requirement is what makes the equations a *system* rather than just an unrelated list. The phrase **simultaneous equations** is therefore synonymous.

> **In Simple Terms:** Two linear equations on their own are independent puzzles — each has its own solutions. As a *system*, the same (x, y) pair must work for **both** at once. This drastically reduces the solution set.

### Definitions
- **System of m linear equations in n variables** ⭐: m simultaneous linear equations
  aᵢ₁x₁ + aᵢ₂x₂ + … + aᵢⱼxⱼ + … + aᵢₙxₙ = bᵢ, for i = 1, …, m,
  whose joint solution requires constants c₁, …, cₙ that satisfy *every* equation simultaneously.

### Illustrative example (from source)
Two equations:
- 3x + 4y = 4 … (II)
- 6x + y = 8 … (III)

**Not as a system**: x = 0, y = 1 satisfies (II); x = 1, y = 2 satisfies (III). The variables x in (II) and (III) need not be the same x. We could even rename them: 6u + v = 8 ≡ (III').

**As a system**: solve simultaneously.
- 2·(II) − (III): 6x + 8y − 6x − y = 8 − 8 ⇒ **7y = 0 ⇒ y = 0**.
- Substitute back into (II): 3x = 4 ⇒ **x = 4/3**.
- The unique system-solution is (x, y) = (4/3, 0).

### Connections
- Builds on: 8.2.2 (single-equation solution).
- Sets up: 8.2.4 (homogeneous case), 8.3 (matrix form).

---

## Section: 8.2.4 System of Homogeneous Linear Equations 🔴

### Core Idea
A linear system AX = b is **homogeneous** if every right-hand side bᵢ = 0 — i.e. the system AX = 0. **Every homogeneous system has at least one solution**: the **trivial solution** x₁ = x₂ = … = xₙ = 0. The interesting question is whether **non-trivial solutions** (with at least one xⱼ ≠ 0) exist — those are the eigen-vectors-of-the-zero-eigenvalue, and require rank(A) < n (a topic continued in chunk 008).

### Definitions
- **Homogeneous linear system** ⭐: aᵢ₁x₁ + … + aᵢₙxₙ = 0 for every i = 1, …, m. Equivalently AX = **0**.
- **Trivial solution** ⭐: xⱼ = 0 ∀ j. Always exists for any homogeneous system.
- **Non-trivial solution** ⭐: a solution with at least one xⱼ ≠ 0. May or may not exist.

> **Quick Recall:**
> - Homogeneous ⇔ all bᵢ = 0.
> - Trivial solution **always** exists.
> - Non-trivial exists iff rank(A) < n (i.e. iff |A| = 0 in the square case). ⭐

### Connections
- Builds on: 8.2.3 (general system).
- Sets up: 8.6 (consistency), Block 1 §5.3.7 (rank), Unit 7 (eigen value problem = homogeneous (A − λI)x = 0).

---

## Section: 8.3 Representation of a System as a Matrix Equation 🔴

### Core Idea
For large m, n, writing all m × (n + 1) coefficients is unwieldy. Two compact alternatives:
1. **Matrix equation**: AX = B, where A is m×n (coefficients), X is n×1 (variables), B is m×1 (constants).
2. **Augmented matrix [A | B]**: pack A and B together into a single m × (n + 1) matrix; the variable column is implicit.

The augmented form is especially convenient for solving by elementary row operations because *one* matrix carries all the system's information.

### Definitions
- **Matrix equation form** ⭐: AX = B with A (m×n), X (n×1), B (m×1).
- **Augmented matrix** ⭐: [A | B] — A and B side-by-side with a vertical bar separator; an m × (n+1) matrix that uniquely encodes the system.

### Worked example (the "running" 3×3 system)
System (C):
- 3x + y + 2z = 11 … (Eq. 1)
- x + 2y − 2z = −1 … (Eq. 2)
- 2x − 2y − z = −5 … (Eq. 3)

Solution by elimination: **x = 1, y = 2, z = 3**. ⭐ (Used as the running example throughout §8.3–8.5.)

Matrix form (D):
A = | 3 1 2 ; 1 2 −2 ; 2 −2 −1 |, X = (x, y, z)ᵀ, B = (11, −1, −5)ᵀ.

Augmented matrix (E):
| 3  1  2 | 11 |
| 1  2 −2 | −1 |
| 2 −2 −1 | −5 |

### Connections
- Builds on: 7.2 (matrix form was previewed there).
- Sets up: 8.4 (elementary row operations on (E) preserve the solution set).

---

## Section: 8.4 Elementary Row Operations & Unchanged Solution Set 🔴

### Core Idea
The solution set of AX = B is preserved by three reversible "elementary row operations" (EROs) on the augmented matrix [A | B]: row swaps, scalar multiplication of a row by a non-zero constant, and adding a non-zero multiple of one row to another. EROs are simply matrix-language for the steps you'd perform in classical elimination — but applied to one compact matrix.

### Definitions: Three Elementary Row Operations
| ERO | Symbol | Effect on system |
|------|--------|-------------------|
| (i) Row swap | Rᵢ ↔ Rⱼ | Reorders equations — clearly preserves solutions |
| (ii) Row scaling | Rᵢ → k Rᵢ (k ≠ 0) | Multiplies an equation through by k — same solution set |
| (iii) Row replacement | Rᵢ → Rᵢ + k Rⱼ | Adds k times another equation to this one — same solution set |

### Theorem A ⭐
**Elementary row operations on the augmented matrix [A | B] do not change the solution set of the system AX = B.**

### Why use it
Instead of repeatedly rewriting equations, work entirely on [A | B]: drive elements below the diagonal to zero (row-echelon form), then back-substitute. The mechanical steps are the same as Gauss elimination.

> **Quick Recall:**
> - Three EROs: swap, scale (×k ≠ 0), replace (Rᵢ + k Rⱼ).
> - Each preserves the solution set. ⭐

---

## Section: 8.4.1 Worked example — EROs solve the running system 🔴

### Mechanism (step-by-step from source)
Start with augmented matrix (E):
| 3  1  2 | 11 |
| 1  2 −2 | −1 |
| 2 −2 −1 | −5 |

Step 1: R₁ → R₁ − 3 R₂ and R₃ → R₃ − 2 R₂ (kill column-1 entries above and below row 2):
| 0 −5  8 | 14 |
| 1  2 −2 | −1 |
| 0 −6  3 | −3 |   … (E^iii)

Step 2: R₁ ↔ R₂ (move the "1" pivot to the top):
| 1  2 −2 | −1 |
| 0 −5  8 | 14 |
| 0 −6  3 | −3 |   … (E^iv)

Step 3: R₃ → 5 R₃ (scale to align column-2 elimination):
| 1  2  −2 | −1 |
| 0 −5   8 | 14 |
| 0 −30 15 | −15 |   … (E^v)

Step 4: R₃ → R₃ − 6 R₂:
| 1  2  −2 | −1 |
| 0 −5   8 | 14 |
| 0  0 −33 | 99 |   … (E^vi)

Step 5: R₃ → −R₃/33 (i.e. divide by −33; equivalently multiply by −1/33):
| 1  2 −2 | −1 |
| 0 −5  8 | 14 |
| 0  0  1 |  3 |   … (E^vii) — **upper triangular**.

Back-substitution:
- From R₃: **z = 3**.
- From R₂: −5y + 8(3) = 14 ⇒ −5y = 14 − 24 = −10 ⇒ **y = 2**.
- From R₁: x + 2(2) − 2(3) = −1 ⇒ x + 4 − 6 = −1 ⇒ **x = 1**.

Solution: **(x, y, z) = (1, 2, 3)**. ✓ (matches the elimination answer.)

### ⚠️ Common Mistakes
- ❌ Forgetting to apply EROs **simultaneously** to A and B (when not using the augmented form) → ✅ Either always work on the augmented matrix [A | B], or change A and B in lock-step.
- ❌ Multiplying a row by 0 → ✅ ERO (ii) requires k ≠ 0; multiplying by 0 destroys information about that equation.

> **Quick Recall:**
> - Drive [A | B] to **upper-triangular** by EROs, then back-substitute.
> - Pivot strategy: zero everything below the leading 1 in each column.

### Connections
- Builds on: 5.3.6 elementary operations / row reduction (introduced informally in Unit 5); 8.4 EROs.
- Sets up: 8.5 (which equations carry "new information" vs are redundant linear combinations of the others).

---

## Section: 8.5 Linear Independence and System of Equations — 8.5.1 Linear Combination and Dependence of Equations 🔴

### Core Idea
An equation in a system is **linearly dependent** on the others if it can be written as a **linear combination** of them. Such an equation is *redundant* — adding or removing it does not change the solution set. The augmented-matrix test: if EROs produce an **all-zero row**, the corresponding equation was a linear combination of the rest. A truly independent system has no all-zero row after row-reduction.

### Definitions
- **Linear combination of equations**: Eq. k = Σⱼ≠k λⱼ Eq. j for some scalars λⱼ. ⭐
- **Linearly dependent set of equations** ⭐: at least one equation in the set is a linear combination of the others.
- **Linearly independent set of equations** ⭐: no equation can be expressed as a linear combination of the others.

### Worked example: a redundant equation appears
Augment the system (C) with a fourth equation derived as 2(Eq. 1) + 3(Eq. 2):
- 2·(3x + y + 2z) + 3·(x + 2y − 2z) = 2·11 + 3·(−1) ⇒ **9x + 8y − 2z = 19** … (Eq. 4)

The new system (F) has equations (1), (2), (3), (4) — but in the augmented matrix
| 3  1  2 | 11 |
| 1  2 −2 | −1 |
| 9  8 −2 | 19 |   … (G — row 3 replaced by Eq. 4 instead of Eq. 3)

apply R₃ → R₃ − (2 R₁ + 3 R₂): the third row becomes **all zeros**:
| 3  1  2 | 11 |
| 1  2 −2 | −1 |
| 0  0  0 |  0 |   … (G')

The all-zero row is the equation 0 = 0, which carries **no new information**. So (G) is effectively a 2-equation, 3-variable system → **infinitely many solutions** (parametrise by z).

### Parametric family of solutions (when 2 equations in 3 unknowns)
- (Eq. 1) − 3·(Eq. 2): −5y + 8z = 14 ⇒ **y = (8z − 14)/5**. … (Q)
- (Eq. 2) − 2·(Eq. 1): −5x − 6z = −23 ⇒ **x = (23 − 6z)/5**. … (R)

Pick any z; then x and y are determined. Infinitely many solutions, parametrised by z. ⭐

### General Linear-combination relation
If an equation can be written as
**Eq. k = λ₁ Eq. 1 + λ₂ Eq. 2 + … + λ_{k−1} Eq. (k−1) + λ_{k+1} Eq. (k+1) + … + λₙ Eq. n**,
then:
i. Eq. k is a **linear combination** of the others.
ii. Adding Eq. k to the system gives no new information about the solutions.

> **Quick Recall:**
> - Eq. k = linear combination of others ⇒ **redundant**. ⭐
> - Augmented-matrix test: ERO produces an all-zero row ⇒ that equation was redundant.
> - m < n linearly-independent equations in n variables ⇒ **infinitely many solutions**. ⭐

### Connections
- Builds on: 6.6 (linear independence of vectors); the equations correspond to row-vectors of the augmented matrix.
- Sets up: 8.5.2 (independence test), 8.6 (consistency), 8.7 (rank-based criteria).

---

## Section: 8.5.2 Linear Independence of m Equations in n Variables (m ≤ n) 🔴

### Definitions (recap, applied to equations)
- **Linearly dependent set of m equations (m ≤ n)**: ∃ j with 1 ≤ j ≤ m such that Eq. j is a linear combination of the rest. ⭐
- **Linearly independent set of m equations (m ≤ n)**: for **no** j is Eq. j a linear combination of the rest. ⭐

### Test for Linear Independence (B)
> **In the augmented-matrix representation of the system, while attempting to drive elements below the main diagonal to zero, if you obtain a row of all zeros, the equations are linearly dependent. Otherwise the set is linearly independent.** ⭐

### Worked verification (running system C)
The row-reduction of (C) produced (E^vi):
| 1  2  −2 | −1 |
| 0 −5   8 | 14 |
| 0  0 −33 | 99 |

No row is all-zero ⇒ the three equations of (C) are **linearly independent** ⇒ unique solution exists (and we found it: x=1, y=2, z=3). ⭐

### Theorem B (singular sub-system)
**If a set of n equations in n variables has some equation that is a linear combination of (i.e. linearly dependent on) the remaining equations, then the number of solutions is infinite.** ⭐

### Theorem C (under-determined system)
**If a system has m equations in n variables with m < n, then the number of solutions is infinite.** ⭐

### Why the theorems hold
- Theorem B: an n×n system loses rank to (n−1) when an equation is a combination of others ⇒ rank(A) = n − 1 < n ⇒ infinite solutions.
- Theorem C: m < n means at most m linearly-independent equations among n unknowns ⇒ at least one variable is free ⇒ infinitely many solutions (or none, if inconsistent — see 8.6).

> **Quick Recall:**
> - **All-zero row in row-reduced augmented matrix ⇔ a linear combination ⇔ dependent**. ⭐
> - n equations in n variables with one redundant ⇒ infinite solutions. (Theorem B)
> - m < n equations in n variables ⇒ infinite solutions (when consistent). (Theorem C)

### Connections
- Builds on: 6.6 (linear independence), 5.3.7 (rank).
- Sets up: 8.6 (consistency: does a solution exist *at all*?) and 8.7 (rank of A vs rank of [A | B]).

---

## Section: 8.6 Consistency of a System of m Linear Equations in n Variables (introduction) 🔴

### Setup
§8.5 covered m ≤ n: the question there was whether equations were *redundant* (and hence whether solutions are unique vs infinite). §8.6 considers the **opposite case m > n**: more equations than variables. The new question is **consistency** — whether a system has *any* common solution at all, or whether the equations contradict each other and produce **no** solution.

### Definitions
- **Consistent system** ⭐: a system that has at least one solution.
- **Inconsistent system** ⭐: a system with **no** solution (the equations contradict each other).

### Worked setup (continuation in chunk 008)
Take the running 3-equation system (C) — solution (x, y, z) = (1, 2, 3) — and **augment it with a fourth equation**:
- 4x − 3y + 2z = −2 … (Eq. 5)

Now the system has **4 equations in 3 variables** (m = 4 > n = 3). The next chunk will check whether (Eq. 5) is consistent with the existing solution (1, 2, 3) and develop the **rank test for consistency**: rank(A) = rank([A | B]) ⇔ consistent.

<!-- Continues in chunk 008 -->

> **Quick Recall:**
> - m > n ⇒ ask **consistency** (does a solution exist?), not just independence.
> - Inconsistent ⇔ a row of [A | B] reduces to (0, 0, …, 0 | non-zero) — i.e. 0 = (non-zero), a contradiction. ⭐
> - **Rank test** (covered next): consistent ⇔ rank(A) = rank([A | B]).

### Connections
- Builds on: 8.5 (independence), 5.3.7 (rank).
- Sets up: 8.6 (continued in chunk 008), 8.7 (rank-based solution criteria), 8.8 (span / basis / dimension).

### Open Questions
1. For a given inconsistent system (rank(A) < rank([A | B])), what is the closest x in the least-squares sense? (Beyond the unit; previewed in regression problems.)


---


## Section: 8.6 Consistency of m Linear Equations in n Variables (concluded) 🔴
<!-- See chunk 007 for start of this section -->

### Worked example: an inconsistent system
Augment the running 3×3 system (C) with **Eq. 5: 4x − 3y + 2z = −2** to get system (H) — 4 equations in 3 variables. Test whether the existing solution (x, y, z) = (1, 2, 3) survives:
- Substitute into (Eq. 5): LHS = 4(1) − 3(2) + 2(3) = 4 − 6 + 6 = **4** ≠ −2 = RHS.
- Hence (Eq. 5) is **violated** by (1, 2, 3); no triple satisfies all four equations simultaneously.

System (H) is **inconsistent**.

### Worked example: a consistent over-determined system
Replace (Eq. 5) with **Eq. 6: 4x − 3y + 2z = 4** to get system (L). Now (1, 2, 3) does satisfy Eq. 6:
- LHS = 4(1) − 3(2) + 2(3) = 4 − 6 + 6 = **4** = RHS ✓.

So (1, 2, 3) satisfies all four equations: system (L) is **consistent**, and the extra equation is a **linear combination** of the existing ones (4·R₁ + (−3)·R₂ + 2·R₃ in some form).

### Definitions (formal)
- **Consistent system (with m > n)** ⭐: a solution exists.
- **Inconsistent system (with m > n)** ⭐: no solution exists.

### Important remarks
1. A system with m ≤ n is **necessarily consistent** when the equations are independent; the question of consistency really only arises when m > n. *(Caveat: consistency can still fail for m ≤ n if equations are contradictory, but the typical phrasing in this book reserves the term for m > n cases.)*
2. Any over-determined system (m > n) is either **consistent and linearly dependent** (the extra equations are combinations of the others), or **inconsistent and linearly independent** (the extra equations contradict).

### Test for consistency (A) — augmented-matrix criterion ⭐
> **In the augmented matrix, perform EROs until elements below the main diagonal are zeroed. If any row reduces to (0, 0, …, 0 | K) with K ≠ 0, the system is INCONSISTENT (because that row says 0 = K ≠ 0). If, instead, every row of zeros to the left of the bar has K = 0, the system is CONSISTENT.** ⭐

### Worked: inconsistent (H) by ERO
Augmented [A | B] for system (H):
| 3  1  2 | 11 |
| 1  2 −2 | −1 |
| 2 −2 −1 | −5 |
| 4 −3  2 | −2 |

After applying the same ERO sequence used in §8.4.1 (R₁ → R₁ − 3 R₂; R₃ → R₃ − 2 R₂; R₁ ↔ R₂; R₃ → 5 R₃; R₃ → R₃ − 6 R₂; R₃ → −R₃/33) and then R₁ → 3 R₁ + R₂, R₄ → 3 R₄ − 4 R₁, R₄ → R₄ + 13 R₂, R₄ → R₄ − 24 R₃, the bottom row reduces to:

| 0  0  0 | −18 |

which says **0 = −18**, a contradiction ⇒ **inconsistent**. ✓

### Worked: consistent (L) by ERO
Augmented [A | B] for system (L) (only entry (4, 4) differs from H — it is +4 instead of −2):

After applying the *same* sequence of EROs, the final bottom row is:

| 0  0  0 |  0 |

No row of the form (0, …, 0 | K ≠ 0). **Consistent**. ✓ (And the bottom row being all zeros means Eq. 6 was redundant — a linear combination of the first three.)

### ⚠️ Common Mistakes
- ❌ Stopping at the first all-zero row and concluding consistency → ✅ A row of (0, …, 0 | K) with K = 0 is fine; with K ≠ 0 it is the smoking gun for inconsistency. **Check the value to the right of the bar**.

> **Quick Recall:**
> - **Test**: row-reduce [A | B]; look for (0, …, 0 | K) rows.
>   - K = 0 ⇒ row is redundant (no information lost) — system can still be consistent.
>   - K ≠ 0 ⇒ system is **INCONSISTENT**. ⭐
> - m ≤ n linearly-independent equations ⇒ always consistent.
> - m > n consistent ⇒ extra equations are linear combinations (linearly dependent system).
> - m > n inconsistent ⇒ extra equations are independent and contradict the others.

### Connections
- Builds on: 8.4 EROs, 8.5 dependence/independence.
- Sets up: 8.7 (rank-based solution criteria — the same test, packaged via rank(A) vs rank([A|B])).

---

## Section: 8.7 Rank of a Matrix and Solution of a System 🔴

### Core Idea
The rank of A and the rank of the augmented [A | B] together fully determine the solution-existence and uniqueness of AX = B. The three cases form an exhaustive classification ⭐:

| Rank condition | Solution structure |
|----------------|---------------------|
| **rank(A) = rank([A | B]) = n (= number of variables)** | **Unique solution** |
| **rank(A) = rank([A | B]) < n** | **Infinitely many solutions** (with (n − rank) free parameters) |
| **rank(A) < rank([A | B])** | **Inconsistent** — no solution |

> **In Simple Terms:** Compare the rank of the *coefficients alone* (A) to the rank of the *coefficients plus answers* ([A | B]). If they match and equal n, the answer is unique. If they match but are smaller than n, you have a family of solutions parametrised by the missing dimensions. If [A | B] has higher rank, the constants contradict the coefficients — no solution.

### Definitions (recap from 5.3.7)
- **Rank of a matrix** ⭐: the order of the largest non-zero minor; equivalently, the maximum number of linearly independent rows (or columns).
- A theorem of linear algebra: **row-rank = column-rank**, so rank is well-defined.

### Worked examples

#### (i) Unique solution: system (C)
Augmented matrix reduced to (E^vii):
| 1  2 −2 | −1 |
| 0 −5  8 | 14 |
| 0  0  1 |  3 |

rank(A) = 3 (three non-zero rows on the LHS), rank([A | B]) = 3, n = 3 ⇒ **rank(A) = rank([A | B]) = n = 3** ⇒ **unique** solution (1, 2, 3). ⭐

#### (ii) Infinitely many: system (F) (the redundant 4th equation case)
Reduced augmented matrix (G'):
| 3  1  2 | 11 |
| 1  2 −2 | −4 |
| 0  0  0 |  0 |

rank(A) = 2 = rank([A | B]) < n = 3 ⇒ **infinite solutions**, parametrised by one free variable (e.g. z). ⭐

#### (iii) Inconsistent: system (H) (the contradictory 5th equation)
Reduced augmented matrix has bottom row (0, 0, 0 | −18):
- rank(A) = 3, rank([A | B]) = 4 ⇒ rank(A) < rank([A | B]) ⇒ **no solution**. ⭐

### Three rank-based theorems (consolidated)
1. If **rank(A) = rank([A | B]) = m** (the number of equations), the system has a **unique** solution. *(Rephrasing — when m = n: unique; when m < n: infinite.)*
2. If **rank(A) = rank([A | B]) < m**, the system has **infinite** solutions.
3. If **rank(A) < rank([A | B])**, the system is **inconsistent**, i.e. no solution.

### ⚠️ Common Mistakes
- ❌ Computing rank only on the coefficient block A and concluding consistency → ✅ Always compute rank of *both* A and [A | B]; consistency requires them to be **equal**.

> **Quick Recall:**
> - **Unique** ⇔ rank(A) = rank([A|B]) = n. ⭐
> - **Infinite** ⇔ rank(A) = rank([A|B]) < n. ⭐
> - **No solution** ⇔ rank(A) < rank([A|B]). ⭐

### Connections
- Builds on: 5.3.7 (rank), 8.4 (EROs), 8.6 (consistency).
- Sets up: 8.8 (span / basis / dimension — vectors view of the same algebra).

---

## Section: 8.8 Span, Basis, Dimension in Rⁿ (optional reading) 🟡

### Core Idea
The augmented-matrix viewpoint translates each equation in n variables into an (n+1)-tuple in ℝⁿ⁺¹: row j = (a_{j1}, a_{j2}, …, a_{jn}, b_j). All vector concepts from Unit 6 — linear combination, dependence, independence, span, basis, dimension — apply directly to **these row-vectors**. Consistency / dependence questions become questions about the **span** of the rows.

### Definitions (carried over from Unit 6, re-stated for vectors-from-equations)
- **Linear combination of vectors** ⭐: V = λ₁V₁ + λ₂V₂ + … + λₖVₖ for some scalars λⱼ.
- **Linearly dependent set of vectors** ⭐: ∃ scalars λⱼ, not all zero, with Σ λⱼ Vⱼ = **0**.
- **Linearly independent set of vectors** ⭐: Σ λⱼ Vⱼ = **0** ⇒ every λⱼ = 0.
- **Span of {V₁, …, Vₖ}** ⭐: the set of *all* vectors expressible as Σ λⱼ Vⱼ — also called the **vector space generated by the set**.
- **Basis of a vector space** ⭐: a *maximal* linearly-independent subset.
- **Dimension of a vector space** ⭐: the number of vectors in *any* basis (well-defined: all bases have the same size).

### Translation: equations → row vectors
Running system (C):
- (Eq. 1) 3x + y + 2z = 11 → V₁ = (3, 1, 2, 11) ∈ ℝ⁴
- (Eq. 2) x + 2y − 2z = −1 → V₂ = (1, 2, −2, −1) ∈ ℝ⁴
- (Eq. 3) 2x − 2y − z = −5 → V₃ = (2, −2, −1, −5) ∈ ℝ⁴

These are **3 vectors in ℝ⁴**. Their linear span is a 3-dimensional subspace of ℝ⁴ (because V₁, V₂, V₃ are linearly independent, as established by the non-zero rank of the augmented matrix).

### Why the translation matters
- "Equations are linearly dependent" ⇔ "row-vectors are linearly dependent."
- "System is consistent" ⇔ "B vector lies in the span of A's column vectors."
- The **rank** of A (= dim of column-span = dim of row-span) is the count of independent equations. ⭐

> **Quick Recall:**
> - Each equation ↔ one (n+1)-vector in ℝⁿ⁺¹. ⭐
> - Span(V₁, …, Vₖ) = vector space generated by the set.
> - Basis = maximal LI subset; dimension = its size.
> - Dependence and consistency questions are *linear-algebra-on-row-vectors* questions.

### Connections
- Builds on: 6.6 (linear dependence), 6.7 (basis & generators), 5.3.7 (rank).
- Sets up: applications in regression (Span = column space = "fit space" of design matrix).

---

## Section: 8.9 Let Us Sum Up 🟢

### Unit 8 wrap-up
This unit (i) defined a **system of linear equations** and its **solution**; (ii) packaged it as the matrix equation **AX = B**; (iii) introduced the **augmented matrix [A | B]** and the **three elementary row operations**; (iv) established **Theorem A** (EROs preserve the solution set); (v) characterised **linear dependence/independence of equations** via the all-zero-row test; (vi) characterised **consistency** via the (0, …, 0 | K ≠ 0) test; (vii) consolidated all of the above into **rank-based criteria** for unique / infinite / no solutions; and (viii) translated equations into row-vectors of ℝⁿ⁺¹ to recover the **span / basis / dimension** vocabulary of Unit 6.

---

## Section: 8.10 Key Words 🟢

### Definitions captured here (recap)
- **Augmented matrix** ⭐: [A | B] formed by appending the constant column to A.
- **Consistent system (m > n)** ⭐: has at least one solution.
- **Inconsistent system (m > n)** ⭐: has no solution.
- **Linear equation** ⭐: each variable degree ≤ 1, at least one degree-1 with non-zero coefficient.
- **Linear combination of equations**: Eq. k = Σⱼ≠k λⱼ Eq. j.
- **Linearly dependent system of equations** ⭐: some Eq. k is a linear combination of the others.
- **Linearly independent system of equations** ⭐: no Eq. k is a linear combination of the others.
- **Solution of a linear equation**: tuple (c₁, …, cₙ) with Σ aⱼcⱼ = b.
- **System of linear equations**: m simultaneous linear equations sharing the variable list.
- **Linear combination / dependent / independent set of vectors**: same definitions as above, applied to vectors V₁, …, Vₖ.

---

## Section: 8.11 Answers / Hints to Check Your Progress 🟡

### Check Your Progress 1 — answers
1. **Which are linear equations?**
   - (i) 3x + 4y = 0 → **linear equation** ✓
   - (ii) 2x − 11 → **not even an equation** (no "=").
   - (iii) xy = 3 → **not linear** (xy has degree 2).
   - (iv) 7 + 4 = 11 → **not a linear equation** (no variables).
   - (v) x(x − 1) = 0 → **not linear** (x² appears).
2. **Which are homogeneous linear equations?**
   - (i) x(x + 2) = 0 → **not even linear**.
   - (ii) x − 4 + y = 0 → **linear, but not homogeneous** (the −4 makes RHS effectively non-zero in the standard rearrangement: x + y = 4).
   - (iii) x + 3y + 4z = 0 → **homogeneous linear** ✓.

### Check Your Progress 2 — answers
- **(i)** 2x = 6, 3y = 9 ⇒ matrix form | 2 0 ; 0 3 | · (x, y)ᵀ = (6, 9)ᵀ; augmented | 2 0 | 6 ; 0 3 | 9 |. Rank = 2 ⇒ **independent**, unique solution (3, 3).
- **(ii)** 3x + 2y = 11; −2x + 3y = −29; x + y = 2. Augmented | 3 2 | 11 ; −2 3 | −29 ; 1 1 | 2 |. m = 3 > n = 2 ⇒ check **consistency**: x = 7, y = −5 satisfies all three ⇒ **consistent**, **linearly dependent** system (one equation is a combination of the others).
- **(iii)** 3x + 2y = 11; x + y = 2; 2x − y = 8. m = 3 > n = 2; the candidate (7, −5) satisfies the first two but not the third ⇒ **inconsistent**, **linearly independent** system.
- **(iv)** x + 2y = 5; −2x + 3z = −11; y − 2z = 8; x + y + z = 0. m = 4 > n = 3 — full augmented matrix as listed; check whether (1, 2, −3) [the suggested solution] satisfies all 4. The textbook checks: equations 1, 2, 3, 4 are all satisfied ⇒ **consistent**, **linearly dependent** (one of the four is redundant).
- **(v)** Same as (iv) but the 4th equation is 2x + y − z = 12. Substituting (1, 2, −3): 2 + 2 + 3 = 7 ≠ 12 — but the textbook's answer says all four equations are satisfied by x=1, y=2, z=−3 ⇒ consistent. Re-checking: 2(1) + 2 − (−3) = 2 + 2 + 3 = **7**. The book's printed claim that this satisfies seems off; **trust the rank/row-reduction test**, not printed answers, when verifying.
- **(vi)** Same as (iv) but the 4th equation is x + y + z = 12. Substituting (1, 2, −3) into the first three works; into the 4th: 1 + 2 − 3 = 0 ≠ 12 ⇒ **inconsistent**.

> **Quick Recall (Check Your Progress 2 patterns):**
> - m ≤ n with full row-rank ⇒ consistent and independent.
> - m > n consistent ⇒ at least one equation is a linear combination ⇒ system is dependent.
> - m > n inconsistent ⇒ no row of the augmented matrix is a combination of the others ⇒ system is independent (in the row-vector sense), but the constants contradict.

---

## Section: 8.12 Exercises (concept definitions with examples) 🟡

### Q1 — define-and-illustrate
- **(a) Linearly independent system**: e.g. x = 3 and 2x + y = 7 (two equations in two variables; neither is a multiple of the other) ⇒ unique solution (3, 1). ⭐
- **(b) Linearly dependent system**: e.g. x + 2y = 6 and 2x + 4y = 12 (the second is 2× the first) ⇒ they describe the same line; infinite solutions. ⭐
- **(c) Consistent system (m > n)**: e.g. {x + 2y = 8; 3x + 4y = 18; 5x + 3y = 19}. Solution (x, y) = **(2, 3)** satisfies all three ⇒ **consistent**, with one equation a linear combination of the other two. ⭐
- **(d) Inconsistent system (m > n)**: e.g. {x + 2y = 8; 3x + 4y = 18; 5x + 3y = 20}. The first two give (2, 3), but 5(2) + 3(3) = 19 ≠ 20 ⇒ **inconsistent**, no common solution. ⭐

> **Quick Recall (Unit 8):**
> - Three EROs preserve the solution set (Theorem A). ⭐
> - All-zero augmented row ⇒ **redundant equation** (linear combination).
> - (0, …, 0 | K ≠ 0) row ⇒ **inconsistent** (no solution). ⭐
> - Rank classification: rank(A) = rank([A|B]) = n ⇒ unique; = n − k < n ⇒ ∞-many (k free); rank(A) < rank([A|B]) ⇒ no solution.
> - m ≤ n equations: question is *independence*; m > n equations: question is *consistency*. ⭐
> - Each equation ↔ a vector in ℝⁿ⁺¹; span/basis/dimension carry over directly.

### Connections
- Closes Unit 8 and Block 2.
- Bridges into: regression theory (column space, projection), optimisation (KKT systems), and the entire econometrics block (where AX = B is the OLS normal equation).

### Open Questions
1. When a system is over-determined and inconsistent (rank(A) < rank([A | B])), what x minimises ‖AX − B‖²? (Answer: the **least-squares** estimator, x̂ = (AᵀA)⁻¹ AᵀB — covered in Block 1 of MEC203/econometrics texts.)
2. For a homogeneous AX = 0 with rank(A) = r < n, what is the dimension of the **solution space** (the kernel of A)? (Answer: dim ker A = n − r — the **rank–nullity theorem**, beyond this unit.)


---

