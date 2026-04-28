# Chunk 001 — Block 7 Front Matter & Mathematical Notation
<!-- Pages: 1-10 -->
<!-- Source: chunk_001.txt + page_images/page-01..10.png -->

## Section: Block Overview & Course Placement 🟢

### Core Idea
Block 7 of MEC-203 Quantitative Methods (Vol. 3) covers **Dynamic Optimisation**, comprising three units: Intertemporal Optimisation-I (Unit 22), Intertemporal Optimisation-II (Unit 23), and Economic Applications of Dynamic Optimisation (Unit 24). The block is the analytical bridge between earlier static optimisation (Block 5) and economic dynamics (Block 6) on one side, and probability/inferential statistics (Blocks 8–9) on the other.

> **In Simple Terms:** Earlier blocks taught you to find the best choice once. Block 7 teaches you to find the best *path* of choices over time — like deciding not just how much to eat today, but how to eat a finite cake over many days.

### Key Concepts

#### Block 7 unit map
| Unit | Title | Page (Vol. 3) | Focus |
|------|-------|---------------|-------|
| 22 | Intertemporal Optimisation-I | 11 | Calculus of Variations + intro to dynamic programming |
| 23 | Intertemporal Optimisation-II | 39 | Optimal control / Pontryagin's maximum principle |
| 24 | Economic Applications of Dynamic Optimisation | 66 | Ramsey, optimal investment, Hotelling, etc. |

### Definitions
- **Dynamic Optimisation**: optimisation in which the decision variables are **time-variant** (change over time), in contrast to static optimisation where they are fixed at one instant. ⭐ (exam-important)

> **Quick Recall:**
> - Block 7 = Dynamic Optimisation = 3 units (22, 23, 24)
> - Two main approaches: (i) Calculus of Variations / Pontryagin's Maximum Principle (continuous), (ii) Bellman's Dynamic Programming (recursive / discrete)

---

## Section: Mathematical Notation Used in the Course 🟡

### Core Idea
The course standardises a notation set used throughout Block 7 (and the whole MEC-203 course). Knowing these symbols is a prerequisite for reading derivations in subsequent units; misreading a symbol is a frequent source of student error.

### Definitions
Selected symbols (full list in source pages 7–9):

- **[a, b]** — closed interval; **(a, b)** — open interval.
- **∈** — element of.
- **Δ** — change / "delta" of a variable.
- **dx** — differential of x.
- **lim f(x)** — limit of f(x).
- **ln** — natural logarithm.
- **∫ f(x) dx** — definite integral.
- **∀** — universal quantifier ("for all").
- **∃** — existential quantifier ("there exists"); **∃!** — exists exactly one.
- **¬, ∧, ∨, ⇒, ⇔** — negation, conjunction, disjunction, implication, equivalence.
- **a, x ∈ ℝ** — real numbers / scalars.
- **a = (a₁, …, aₙ) ∈ ℝⁿ** — vector of parameters / variables.
- **A, X (matrices)** — capital letters denote matrices, dim m×n.
- **x ~ y** — vector x is **indifferent** to y (preference relation).
- **x ≻ y** / **x ≽ y** — strong / weak preference of x over y.
- **ℝ** — set of real numbers; **ℝ₊** — non-negative reals; **int ℝ₊** — strictly positive reals.
- **ℝⁿ = ℝ × ℝ × … × ℝ** — n-dimensional real space (Cartesian product).
- **ℝⁿ₊ = {x ∈ ℝⁿ | x ≥ 0} ⊂ ℝⁿ** — non-negative orthant.
- **f : X → Y** — function with domain X and codomain Y. ⭐
- **y = f(x)** — scalar function of one variable; **y = f(x₁, x₂)** — of two variables.
- **dy/dx, y′, f′(x)** — first derivative; **d²y/dx², y″, f″(x)** — second derivative.
- **∂f/∂xᵢ** — partial derivative; **∂²f/∂xᵢ ∂xⱼ** — second partial. ⭐
- **H(x₁, x₂)** — **Hessian** matrix (symmetric matrix of second partials). ⭐
- **(p, x) = Σᵢ pᵢ xᵢ** — scalar product of two vectors.
- **det(A) or |A|** — determinant of matrix A.
- **d(x¹, x²) = √(Σᵢ (xᵢ¹ − xᵢ²)²)** — Euclidean metric (distance).
- **d(x¹, x²) = max |xᵢ¹ − xᵢ²|** — non-Euclidean (Chebyshev / sup) metric.
- **‖x‖ = (Σᵢ xᵢ²)^(1/2)** — Euclidean norm.
- **‖x‖ = max |xᵢ|** — non-Euclidean (sup) norm.
- **t = 0, 1, 2, …** — time as discrete variable; **t ∈ [0, +∞)** — time as continuous variable. ⭐ (Block 7 will hinge on this distinction.)
- **∇f, grad f** — gradient of f, ∇f = (∂f/∂x₁, …, ∂f/∂xₙ). ⭐

### Greek letters used:
α (alpha), β (beta), γ (gamma), δ (delta), ε (epsilon), ψ (psi), ρ (rho), θ (theta), λ (lambda), π (pi), σ (sigma), χ (chi), μ (mu), ω (omega).

> **Quick Recall:**
> - Continuous time: t ∈ [0, ∞); discrete time: t = 0, 1, 2, …
> - Hessian = symmetric matrix of second partials → used for second-order conditions
> - ‖x‖ Euclidean = √Σxᵢ² ; sup-norm = max|xᵢ|

### Connections
- Builds on: notation already introduced in Blocks 1–6 (calculus, linear algebra, optimisation).
- Prerequisite for: every derivation in Units 22–24.

### Open Questions
1. None — this is reference material.
