# Chunk 001 — Unit 5 Opening: Determinants (Definition, Minors/Cofactors, Properties)
<!-- Pages: 1-10 (book pp. 153-162) -->
<!-- Source: chunk_001.pdf — image-based PDF, read via multimodal page images -->

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
