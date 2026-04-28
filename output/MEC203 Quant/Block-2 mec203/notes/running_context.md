# Running Context

## Key Concepts Introduced
- **Linear Algebra (Block 2 framing)** (Chunk 001): packaging tool for systems with many variables/equations.
- **Determinant** (Chunk 001): single scalar value of a square array; arises as the common denominator in elimination.
- **Order of a determinant** (Chunk 001): n where the array is n×n; has n² elements.
- **Minor** (Chunk 001): sub-determinant after deleting an element's row + column.
- **Cofactor** (Chunk 001): A_{ij} = (−1)^{i+j} · M_{ij}; signed minor used in expansion.
- **Sarrus / row-1 expansion of 3×3** (Chunk 001): six signed terms.
- **Six properties of determinants** (Chunk 001): transpose, swap (sign flip), equal/proportional rows ⇒ 0, scalar pull-out, sum-split, add multiple of another row.

## Definitions (⭐ exam-important)
- **Determinant** ⭐ (Chunk 001): scalar value associated with a square array.
- **Order n determinant** (Chunk 001): n rows × n columns; n² elements; expansion has n! terms.
- **Minor M_{ij}** ⭐ (Chunk 001): determinant after deleting row i and column j of the parent.
- **Cofactor A_{ij}** ⭐ (Chunk 001): (−1)^{i+j} · M_{ij}.
- **Jacobian determinant** ⭐ (Chunk 001): J = ∂(u,v)/∂(x,y); tests functional dependence.
- **Determinant expansion along row/column** (Chunk 001): Δ = Σⱼ aᵢⱼ Aᵢⱼ for any chosen i.

## Named Models / Laws / Theories
- **Cramer's Rule** (Chunk 001 — preview): determinant-based unique-solution formula for linear systems (full treatment later).
- **Sarrus diagonal rule for 3×3** (Chunk 001).
- **Six Properties of Determinants** (Chunk 001).

## Key Data & Numbers
- 2×2 determinant has 2² = 4 elements; expansion has 2 terms (Chunk 001).
- 3×3 determinant has 9 elements; expansion has 3·2 = 6 terms (Chunk 001).
- An order-n determinant has n² elements and an expansion with n! terms (Chunk 001).
- Determinants first used ~1683, almost simultaneously by Seki Kowa (Japan) and Leibniz (Germany) (Chunk 001).
- Vandermonde 3×3 = (b−a)(c−a)(c−b) (Chunk 002).
- "b+c, c+a, a+b" determinant = 4abc (Chunk 002).
- For Chunk 002 worked Cramer example: x₁ − 2x₂ = 3, 3x₁ + 5x₂ = 20 ⇒ (x₁,x₂) = (5,1).

## More Concepts (Chunk 002)
- **Product of two determinants** (row-of-first × column-of-second).
- **Adjoint Δ′** = transpose of cofactor matrix; Δ⁻¹ = Δ′/Δ.
- **Symmetric determinant**: a_{ij} = a_{ji}. **Skew-symmetric**: a_{ij} = −a_{ji} and diagonal = 0.
- **Cramer's Rule** ⭐: x_i = Δ_i / Δ; works only when Δ ≠ 0.
- **Matrix** ⭐: rectangular m×n array of numbers; element a_{ij}, order m×n.
- **Matrix types** so far: rectangular, square, row, column, null, non-zero, transpose, diagonal, scalar, identity.
- **Conformability**: addition/equality require same order; multiplication has its own rule (next chunk).

## More Concepts (Chunk 004)
- **National-income via Cramer's Rule** ⭐: Y = (a + I + G)/(1 − b); 1/(1−b) = Keynesian multiplier.
- **Tax-augmented multiplier denominator**: (1 − b + bt) for IS-LM-like systems.
- **Vector** ⭐: ordered n-tuple in ℝⁿ; (a, b) ≠ (b, a).
- **Null vector**: every component zero.
- **Vector addition / scalar multiplication** are component-wise.
- **Norm** ‖a‖ = √Σ aᵢ²; **inner product** ⟨a, b⟩ = Σ aᵢ bᵢ. Different from "scalar multiplication" k·a.
- **Cauchy–Schwarz** ⭐: (Σ aᵢ bᵢ)² ≤ (Σ aᵢ²)·(Σ bᵢ²).
- **Orthogonal vectors**: ⟨a, b⟩ = 0; cos θ = ⟨a, b⟩ / (‖a‖·‖b‖).
- **Vector space V over ℝ** ⭐: closed under + and scalar ·, plus 8 axioms.
- **Subspace W**: non-empty subset of V closed under +, scalar ·; must contain 0.

## More Concepts (Chunk 003)
- **Matrix multiplication** ⭐: cols(A) = rows(B); c_{ij} = Σ a_{ik} b_{kj}; non-commutative.
- **Adjoint matrix** = transpose of cofactor matrix.
- **Inverse A⁻¹** ⭐ = adj A / |A|; exists iff |A| ≠ 0.
- **Reversal laws** ⭐: (AB)ᵀ = Bᵀ Aᵀ; (AB)⁻¹ = B⁻¹ A⁻¹; (Aᵀ)⁻¹ = (A⁻¹)ᵀ.
- **Trace tr(A)** = sum of diagonal entries; tr(AB) = tr(BA).
- **Sub-matrix / Minor (matrix sense)**: r-th order minor = determinant of an r×r sub-matrix.
- **Orthogonal matrix** ⭐: Aᵀ = A⁻¹; |A| = ±1.
- **Symmetric**: Aᵀ = A. **Skew-symmetric**: Aᵀ = −A; diagonal = 0.
- **Decomposition**: A = (A + Aᵀ)/2 + (A − Aᵀ)/2 ⭐ — symmetric + skew-symmetric.
- **Idempotent**: A² = A.
- **Partitioned matrix**: blocks treated as scalars under conformable rules.
- **Rank r(A)** ⭐: order of largest non-zero minor; r(A) = r(Aᵀ); r(AB) ≤ min(r(A), r(B)); also = #linearly-independent rows = #linearly-independent columns.

## More Concepts (Chunk 005)
- **Linear dependence** ⭐: ∃ scalars cᵢ not all zero with Σ cᵢxⁱ = 0; subset-dependence ⇒ whole-set-dependence.
- **Linear independence** ⭐: Σ cᵢxⁱ = 0 ⇒ all cᵢ = 0.
- **Generators / Span** ⭐: {a₁, …, aₙ} ⊂ Eⁿ generates Eⁿ if every x ∈ Eⁿ = Σcᵢaᵢ; need at least n vectors.
- **Basis of Eⁿ** ⭐: generators that are linearly independent; exactly n vectors.
- **Standard basis of Eⁿ**: e₁ = (1,0,…,0), …, eₙ = (0,…,0,1).
- **n-dimensional Euclidean space Eⁿ**: collection of all real n-tuples with vector ops + distance.
- **Matrix form of linear system** ⭐: AX = d (A is m×n coefficient matrix).
- **Eigen value / Characteristic value λ** ⭐: scalar with Ax = λx, x ≠ 0.
- **Eigen vector / Characteristic vector x** ⭐: non-zero x satisfying Ax = λx.
- **Characteristic matrix**: A − λI.
- **Characteristic equation** ⭐: |A − λI| = 0; n-degree polynomial in λ.
- **Sum of eigen values = trace(A)** ⭐; **Product of eigen values = |A|** ⭐.
- **Properties**: singular ⇒ some λ = 0; real-symmetric ⇒ real λ; A⁻¹ has 1/λᵢ; A^k has λᵢ^k; diagonal/triangular A ⇒ λᵢ = aᵢᵢ.
- **Bilinear/linear form derivatives**: ∂(b'x)/∂x = b; ∂(x'Ay)/∂x = Ay; ∂(x'Ay)/∂y = A'x. ⭐
- **Real-symmetric A**: eigen vectors of distinct eigen values are orthogonal.

## More Concepts (Chunk 006)
- **Diagonalisation** ⭐: real-symmetric A ⇒ PᵀAP = Λ; columns of P are normalised eigen vectors.
- **Distinct eigen values ⇒ linearly independent eigen vectors** ⭐ (sufficient, not necessary).
- **Quadratic form Q(x) = x'Ax** ⭐ (A symmetric); 2D form: a₁₁x₁² + 2a₁₂x₁x₂ + a₂₂x₂².
- **Definiteness classes**: PD/PSD/ND/NSD/Indefinite.
- **2×2 PD criterion** ⭐: a₁₁ > 0 AND |A| > 0.
- **Eigen-value criterion** ⭐: PD ⇔ all λ > 0; ND ⇔ all λ < 0; indefinite ⇔ mixed signs.
- **Vector differentiation** rules: ∂(a'x)/∂x = a; ∂(x'Ax)/∂x = 2Ax; ∂(x'Bz)/∂x = Bz; ∂(x'Bz)/∂z = B'x. ⭐
- **Jacobian ∂y/∂x** for vector-of-functions y(x): m×n matrix of partials.
- **Linear equation** ⭐: Σ aᵢxᵢ = b; a straight line in 2D.

## More Concepts (Chunk 007)
- **Solution of a linear equation** ⭐: tuple (c₁, …, cₙ) that, when substituted, makes LHS = RHS.
- **System of m linear equations in n variables** ⭐: same tuple must satisfy every equation simultaneously.
- **Homogeneous system** ⭐: AX = 0; **trivial solution** (xⱼ = 0) always exists.
- **Non-trivial solution** ⭐: at least one xⱼ ≠ 0; exists iff rank(A) < n.
- **Augmented matrix [A | B]** ⭐: m × (n+1) matrix combining coefficients and constants.
- **Three Elementary Row Operations (EROs)** ⭐: (i) Rᵢ ↔ Rⱼ swap, (ii) Rᵢ → k·Rᵢ scale (k ≠ 0), (iii) Rᵢ → Rᵢ + k·Rⱼ replacement.
- **Theorem A**: EROs preserve solution set of AX = B. ⭐
- **Linear combination of equations**: Eq. k = Σλⱼ Eq. j; redundant equation.
- **All-zero row test**: row-reduced [A | B] has an all-zero row ⇔ that equation was a linear combination.
- **Theorem B**: n equations in n variables with one redundant ⇒ infinite solutions.
- **Theorem C**: m < n linearly-independent equations in n variables ⇒ infinite solutions (when consistent).
- **Consistent / Inconsistent system** ⭐: has at least one / has no solution.
- For running 3×3 example: (x, y, z) = (1, 2, 3) is the unique solution.

## More Concepts (Chunk 008)
- **Consistency test (m > n)** ⭐: row-reduce [A|B]; (0,…,0|K) with K ≠ 0 ⇒ inconsistent; otherwise consistent.
- **Rank-based solution criteria** ⭐:
  - rank(A) = rank([A|B]) = n ⇒ unique solution.
  - rank(A) = rank([A|B]) < n ⇒ infinite solutions.
  - rank(A) < rank([A|B]) ⇒ inconsistent (no solution).
- **m ≤ n consistent + independent**: unique solution.
- **m > n consistent**: linearly dependent system (extra equations are combinations).
- **m > n inconsistent**: linearly independent system but contradictory.
- **Equations as row-vectors**: equation aⱼ₁x₁+…+aⱼₙxₙ=bⱼ ↔ Vⱼ = (aⱼ₁,…,aⱼₙ,bⱼ) ∈ ℝⁿ⁺¹.
- **Span / Basis / Dimension** (vector-space form) ⭐: Span = vector space generated; Basis = maximal LI set; Dimension = #basis-vectors.
- For Q1(a) of §8.12: x=3 and 2x+y=7 illustrate independent system.
- For Q1(b): x+2y=6 and 2x+4y=12 illustrate dependent system (one is 2× the other).
- For Q1(c): {x+2y=8, 3x+4y=18, 5x+3y=19} consistent with (2,3).
- For Q1(d): {x+2y=8, 3x+4y=18, 5x+3y=20} inconsistent.
