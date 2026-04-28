# Chunk 005 — Unit 6 close (linear dependence, generators, basis) + Unit 7 opening (matrix form, eigenvalue problem)
<!-- Pages: 41-50 (book pp. 193-202) -->
<!-- Source: chunk_005.pdf -->

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
