# Chunk 006 — Diagonalisation, eigen-vector independence, quadratic forms, definiteness, vector differentiation; Unit 8 opens
<!-- Pages: 51-60 (book pp. 203-212) -->
<!-- Source: chunk_006.pdf -->

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
