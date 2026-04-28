# Chunk 004 — Unit 5 wrap + Unit 6 opening: vectors, scalar multiplication, geometry, norm/inner product, vector spaces
<!-- Pages: 31-40 (book pp. 183-192) -->
<!-- Source: chunk_004.pdf -->

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
