# Chunk 007 — Linear systems: solutions, homogeneous case, augmented matrix, EROs, dependence vs independence
<!-- Pages: 61-70 (book pp. 213-222) -->
<!-- Source: chunk_007.pdf -->

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
