# Chunk 008 — Consistency tests, rank-based solution criteria, span/basis/dimension in Rⁿ; Block 2 closes
<!-- Pages: 71-80 (book pp. 223-232) -->
<!-- Source: chunk_008.pdf -->

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
