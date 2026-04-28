# Complete Notes

<!-- Continues into: Mathematical Symbols/Notations table → chunk_002 -->

## Section: Course Introduction — MEC-203 Quantitative Methods 🟢

### Core Idea
MEC-203 (Quantitative Methods, Volume 1) is an IGNOU School of Social Sciences course that develops the mathematical and statistical toolkit needed for economic analysis. Quantitative methods provide precision, accuracy, and a formal language for representing economic ideas, relationships, and phenomena. The course is divided into 9 Blocks comprising 31 Units.

> **In Simple Terms:** This is the "math for economists" course — it teaches you the language (mathematics) economists use to talk precisely about ideas like demand, growth, and risk, instead of just describing them in words.

### Key Concepts

#### Course Learning Outcomes
After completing this course a student will be able to:
- Use mathematics as a language to represent economic ideas, concepts, phenomena and relationships among variables.
- Apply mathematics as a tool to explain economic phenomena at local, regional, national, and global levels.
- Acquire basic knowledge of mathematical methods and statistical tools to explain economic theory.
- Apply optimisation techniques to find optimum levels of objective functions pursued by economic agents.
- Apply statistical tools for data presentation, data analysis, hypothesis formulation, and hypothesis testing.

#### Block-wise Structure (high-level map)

| Block | Title | Units | Focus |
|---|---|---|---|
| 1 | Review of Basic Mathematics | 1–4 | Sets, algebra, relations & functions, coordinate geometry |
| 2 | Linear Algebra | 5–8 | Matrices, determinants, vector spaces, eigenvalues |
| 3 | Calculus | 9–12 | Limits, continuity, differentiation (one & several vars), integration |
| 4 | Real Analysis | 13–15 | n-dimensional real space, calculus of several variables, metric space & topology |
| 5 | Extreme Values and Optimisation | 16–19 | Unconstrained & constrained optimisation (one & several variables) |
| 6 | Economic Dynamics | 20–21 | Difference equations (discrete time), differential equations (continuous time) |
| 7 | Dynamic Optimisation | 22–24 | Intertemporal optimisation, Euler's equation, optimal control |
| 8 | Probability and Probability Distributions | 25–27 | Probability theory, discrete & continuous distributions |
| 9 | Inferential Statistics | 28–31 | Sampling, sampling distributions, estimation, hypothesis testing |

#### Block 1 Internal Structure
- **Unit 1 — Fundamental Concepts of Mathematics**: set theory basics, numbers from natural to complex, real number intervals, decimal representation, exponentiation.
- **Unit 2 — Overview of Basic Methods of Mathematics**: algebraic concepts and expressions such as polynomial functions.
- **Unit 3 — Relations and Functions**: relations, functions and their types.
- **Unit 4 — Co-ordinate Geometry and Representation of Functions**.

### Connections
- Builds the foundation for all subsequent blocks. Block 1 → Block 2 (Linear Algebra) → Block 3 (Calculus) → Block 4 (Real Analysis) → Block 5 (Optimisation), etc.

---

## Section: Mathematical Symbols/Notations Used in the Course 🔴

### Core Idea
This is a master reference table of all mathematical symbols and notations used across MEC-203. It covers intervals, set membership, calculus operators, logical/quantifier symbols, vectors, matrices, preference relations, real-number spaces, and functions. Knowing these symbols cold is a prerequisite for reading any subsequent unit.

> **In Simple Terms:** Think of this table as the "alphabet" of the course. Before you can read mathematical "sentences" in later units, you must know what each squiggle means.

### Definitions (Symbol Reference Table) ⭐

#### Intervals & Basic Calculus Notation
- **[a, b]**: Closed interval (includes both endpoints a and b). ⭐
- **(a, b)**: Open interval (excludes both endpoints). ⭐
- **∈**: "Element of" / "belongs to". ⭐
- **Δ (Delta)**: Change in (e.g., Δx = change in x).
- **dx**: Differential (infinitesimal change in x).
- **lim f(x)**: Limit of f(x).
- **ln**: Natural logarithm (log to base e).
- **∫ f(x) dx**: Definite integral. ⭐

#### Logic & Quantifiers
- **∀**: Universal quantifier — "for all". ⭐
- **∃**: Existential quantifier — "there exists". ⭐
- **∃!** (written as "∃₁" in source): "there exists exactly one".
- **∃ⱼ** (written as "∃ⱼ" in source): "there exists more than one".
- **¬** (negation): ¬P means "not P".
- **∧**: Conjunction — "and".
- **∨**: Disjunction — "or".
- **⇒**: Implication; p ⇒ q means "if p then q". ⭐
- **⇔**: Equivalence — "if and only if". ⭐

#### Numbers, Vectors, Matrices, Sets
- **a, x ∈ R**: Numbers, scalars.
- **a = (a₁, a₂, …, aₙ) ∈ Rⁿ**: Vector of parameters.
- **x = (x₁, x₂, …, xₙ) ∈ Rⁿ**: Vector of variables.
- **A, X (capital, italic-style)**: Sets.
- **A, X (capital, bold)**: Matrices with dimensions m by n (m rows, n columns).

#### Preference Relations (Used in Microeconomics)
- **x ~ y**: Vector x is indifferent w.r.t. vector y.
- **≻ (strict)**: Strong preference relation.
- **x ≻ y**: Vector x is strongly preferred over vector y.
- **≽ (weak)**: (Weak) preference relation.
- **x ≽ y**: Vector x is (weakly) preferred over vector y.

#### Real Number Spaces
- **R**: Set of real numbers. ⭐
- **R₊**: Set of nonnegative real numbers.
- **int R₊**: Set of positive real numbers (interior of nonnegative reals).
- **Rⁿ = R × R × … × R**: n-dimensional space of real numbers; the Cartesian product of R taken n times. ⭐
- **Rⁿ₊ = {x ∈ Rⁿ | x ≥ 0} ⊂ Rⁿ**: Nonnegative orthant (subspace) of Rⁿ.
- **int Rⁿ₊ ⊂ Rⁿ**: Interior of (nonnegative orthant of) Rⁿ.

#### Function Notation
- **f : X → Y**: Function f mapping from set X to set Y.
- **X**: Domain of a function (set of arguments / inputs).
- **Y**: Codomain of a function (set of values / outputs).

### ⚠️ Common Mistakes
- ❌ Confusing **∈** (member of a set) with **⊂** (subset of a set). → ✅ ∈ relates an element to a set; ⊂ relates two sets.
- ❌ Reading **(a, b)** as an ordered pair when it appears in interval contexts. → ✅ In interval notation, (a, b) is the open interval; in coordinate / vector contexts it can be an ordered pair — context disambiguates.
- ❌ Mixing up ⇒ (implication, one-way) and ⇔ (equivalence, two-way).

> **Quick Recall:**
> - **[a, b]** closed; **(a, b)** open.
> - **∀** = for all; **∃** = there exists.
> - **R, Rⁿ, Rⁿ₊** = reals, n-dim reals, nonnegative orthant.
> - **¬, ∧, ∨, ⇒, ⇔** are the five core logical connectives.
> - **f : X → Y** with **X = domain**, **Y = codomain**.

### Connections
- Prerequisite for: every Unit in this course. Specifically, calculus notation (dx, ∫, lim) is used heavily in Block 3 (Chunks covering Calculus); preference relations appear in microeconomic optimisation; logic symbols pervade Real Analysis (Block 4).
- Continues into: derivatives, partial derivatives, gradient, Hessian, and Greek alphabet — see Chunk 002.

### Open Questions
- Why does the textbook adopt **∈** for "element of" rather than the older **ε**? (Notation evolution.)
- When is the nonnegative orthant **Rⁿ₊** vs the strictly positive orthant **int Rⁿ₊** used in optimisation problems?

---

## Section: Course Preparation, Editorial & Front-Matter 🟢

### Core Idea
The course was prepared in 2023 by IGNOU's School of Social Sciences. Unit writers include Dr. Meenakshi Sridhar (Rajdhani College, DU), Prof. Gopinath Pradhan, Sunando Basu, Rittwik Chatterjee, Dr. Ram Prasad Yadav, Sisir Debnath, Biswadeep Basu, Mr. Debasish Dash, and Ms. Nivedita Mullick. Course Coordinator: Dr. Nidhi Tewathia. Programme Coordinators: Prof. Narayan Prasad and Dr. Vijeta Banwari. Course is © IGNOU 2023, ISBN 978-93-5568-925-2.

### Connections
- Pure administrative content; not exam-relevant.


---

<!-- Continues from: Mathematical Symbols/Notations (Chunk 001: Course Introduction — MEC-203 Quantitative Methods) -->
<!-- Continues into: Set relationships, special sets, operations (Chunk 003: Cardinality of a Set) -->

## Section: Mathematical Notations (continued) — Functions, Derivatives, Norms 🔴
<!-- Continues from: Symbols table (Chunk 001: Course Introduction — MEC-203 Quantitative Methods) -->

### Core Idea
This continuation of the symbol table introduces the notation for scalar functions (one and two variables), first- and second-order derivatives, partial derivatives, the Hessian matrix, scalar product of vectors, determinants, Euclidean and non-Euclidean metrics, norms, time as discrete vs continuous variable, and the gradient operator. These are the building blocks of calculus, optimisation, and real analysis throughout MEC-203.

> **In Simple Terms:** This is "calculus shorthand." Once you internalise these symbols (∂, ∇, |·|, det), you can read formulas in optimisation and real analysis at a glance instead of decoding every term.

### Definitions ⭐

#### Functions
- **y = f(x)**: Scalar function of one variable. x is the independent variable (argument / input); y is the dependent variable (value of the function). ⭐
- **y = f(x₁, x₂)**: Scalar function of two variables. x₁, x₂ are independent variables; y is the value.

#### Derivatives (One Variable)
- **dy/dx, y′, f′(x)**: First-order derivative of y = f(x). ⭐
- **d²y/dx², y″, f″(x)**: Second-order derivative of y = f(x).
- **df(x)/dx |_{x = x̄}**: Value of a one-variable derivative evaluated at point x = x̄.

#### Partial Derivatives (Several Variables)
- **∂y/∂xᵢ, ∂f(x₁, x₂)/∂xᵢ**: First-order partial derivatives of f(x₁, x₂) with respect to xᵢ for i = 1, 2. ⭐ (NOTE: source OCR shows "0x" / "Ox" / "&" — these are the partial derivative symbol ∂)
- **∂²f(x₁, x₂)/(∂xᵢ ∂xⱼ), ∂²f(x₁, x₂)/∂xᵢ²**: Second-order partial derivatives of f(x₁, x₂).
- **∂f(x₁, x₂)/∂xᵢ |_{x = (x̄₁, x̄₂)}**: Value of a partial derivative evaluated at a specified point.

#### Hessian Matrix
- **H(x₁, x₂)**: Hessian — the symmetric matrix of second-order partial derivatives of f(x₁, x₂):

$$H(x_1, x_2) = \begin{bmatrix} \dfrac{\partial^2 f(x_1, x_2)}{\partial x_1^2} & \dfrac{\partial^2 f(x_1, x_2)}{\partial x_1 \partial x_2} \\[2pt] \dfrac{\partial^2 f(x_1, x_2)}{\partial x_2 \partial x_1} & \dfrac{\partial^2 f(x_1, x_2)}{\partial x_2^2} \end{bmatrix}$$

#### Vector & Matrix Operations
- **(p · x) = Σᵢ₌₁ⁿ pᵢ xᵢ**: Scalar (dot) product of two vectors p, x ∈ Rⁿ. ⭐
- **det(A) or |A|**: Determinant of matrix A. ⭐

#### Distance / Metric / Norm
- **dₑ(x¹, x²) = √[Σ (xᵢ¹ − xᵢ²)²]**: Euclidean metric (distance between two vectors). ⭐
- **d(x¹, x²) = max_{i=1,2} |xᵢ¹ − xᵢ²|**: Non-Euclidean (max / Chebyshev) metric.
- **‖x‖** (Euclidean norm): standard length of vector x.
- **‖x‖ = max_{i=1,2} |xᵢ|**: Non-Euclidean (sup) norm.

#### Time
- **t = 0, 1, 2, …**: Time as a **discrete** variable (used in difference equations, Block 6).
- **t ∈ [0, +∞)**: Time as a **continuous** variable (used in differential equations, Block 6).

#### Gradient
- **∇f, grad f**: Gradient of function f. **∇f = (∂f/∂x₁, …, ∂f/∂xₙ)**. ⭐

### ⚠️ Common Mistakes
- ❌ Writing dy/dx for a multi-variable function. → ✅ Use ∂y/∂xᵢ (partial derivative) when there are several independent variables.
- ❌ Confusing **|A|** (determinant of matrix) with **|x|** (absolute value of scalar) or **‖x‖** (norm of vector). → ✅ Context: matrix → determinant; scalar → absolute value; vector → norm.
- ❌ Forgetting that the Hessian must be **symmetric** (under Young's theorem when mixed partials are continuous): ∂²f/(∂x₁∂x₂) = ∂²f/(∂x₂∂x₁).

> **Quick Recall:**
> - First derivative: **dy/dx**, **f′(x)**.
> - Partial derivative: **∂f/∂xᵢ**.
> - Hessian = matrix of 2nd-order partials.
> - Dot product: **p · x = Σ pᵢxᵢ**.
> - Gradient: **∇f = (∂f/∂x₁, …, ∂f/∂xₙ)**.
> - Euclidean distance: **dₑ = √Σ(xᵢ − yᵢ)²**.

### Connections
- Used in Block 3 (Calculus, Units 9–12), Block 4 (Real Analysis, especially metric space — Unit 15), and Block 5 (Optimisation — Hessian determines second-order conditions for max/min).

---

## Section: Greek Alphabet Reference 🟡

### Core Idea
A reference table of Greek letters commonly used as symbols in mathematics and economics throughout the course.

### Definitions
| Symbol | Greek Alphabet | Symbol | Greek Alphabet |
|---|---|---|---|
| α | Alpha | θ | Theta |
| β | Beta | λ | Lambda |
| γ | Gamma | π | Pi |
| δ / Δ | Delta | σ | Sigma |
| ε | Epsilon | χ | Chi |
| ψ | Psi | μ | Mu |
| ρ | Rho | ω | Omega |

### Connections
- α, β commonly used as parameters (e.g., elasticities); λ for Lagrange multipliers (Block 5); π for circle constant or for profit; σ, μ for population standard deviation and mean (Block 8 onward); ε for arbitrarily small positive number in real analysis.

---

## Section: Unit 1 Structure & Objectives 🟢

### Core Idea
Unit 1 of Block 1 ("Fundamental Concepts of Mathematics") covers two foundational pillars — set (the basis of modern mathematics) and number (the basis of conventional mathematics) — and provides a working vocabulary for every later unit.

### Key Concepts

#### Unit 1 Structure (Detailed Outline)
- **1.0** Objectives
- **1.1** Introduction
- **1.2** Set Theory
  - 1.2.1 Concept of Set
  - 1.2.2 Notations
  - 1.2.3 Forms of Set Representation
  - 1.2.4 Relationships Between Sets (notation, definitions, examples; establishing relationships)
  - 1.2.5 Some Special Sets (Universal, Null, Power, Convex)
  - 1.2.6 Quantifiers and Logical Symbols / Operators
  - 1.2.7 Conceptual Clarifications (Relation vs Operation; set operations; further clarifications)
- **1.3** Numbers: From Natural to Complex
  - 1.3.1 Standard Number Sets
  - 1.3.2 R, the Set of Real Numbers
  - 1.3.3 Real Number Intervals
  - 1.3.4 Complex Numbers
  - 1.3.5 Number Miscellany
  - 1.3.6 Properties of Real Numbers as Ordered Field
- **1.4** Decimal Representation of Rational and Irrational Numbers
- **1.5** Real Number Exponentiation
- **1.6** Let Us Sum Up
- **1.7** Key Words
- **1.8** Answers/Hints to Check Your Progress Exercises
- **1.9** Exercises

#### Unit 1 Learning Objectives ⭐
After this unit a student should be able to:
- Differentiate between concept, term, notation, and definition of number.
- Explain the concept of set.
- Use set notation.
- Find relations on sets.
- Apply set operations.
- Differentiate between 'relation' and 'operation' on sets.
- Discuss relations and operations on numbers and their properties.
- Define various types of numbers.
- Apply operations on numbers and use their properties in numerical problem solving.
- Express real numbers (including irrational numbers) as decimal numbers.
- Apply rules of exponentiation of numbers.

---

## Section: Concept, Term, Notation, and Number System 🟡

### Core Idea
Before formal mathematics, one must distinguish four related ideas about a number: the **concept** (the abstract idea, e.g., "twoness"), the **term/name** (the word, e.g., "two", "zwei"), the **notation/numeral/symbol** (the written sign, e.g., 6, VI, ६), and the **numeral system** (the rule for combining symbols, e.g., decimal, Roman, binary).

> **In Simple Terms:** "Twoness" is the idea, "two" is the English name, "2" is the symbol, and "decimal system" is the rule for writing numbers down. They are four different things even though we use them interchangeably in everyday life.

### Key Concepts

#### Number Concept
The idea/sense that distinguishes Fig. 1(a) (one horse) from Fig. 1(b) (two horses) and recognises Fig. 1(b) and Fig. 1(c) as sharing "twoness" despite the difference in objects (horses vs marble elephants). The concept is the abstraction shared.

#### Number Name / Term
The linguistic label for a concept. Different languages give different names: English "two", Hindi "दो", German "zwei", Tamil "இரண்டு" / "Irantu". The textbook also notes that one term can map to several concepts ("bank" = river bank vs financial institution).

#### Numeral / Number-Notation / Number-Symbol
The written representation of a number. For "six": the numerals **6** (decimal), **VI** (Roman), **६** (Devanagari) all denote the same concept. Strictly speaking, **6 is the name (numeral) of a number, not the number itself**, but in mathematics it is conventional to call numerals "numbers".

#### Term, Notation, and Definition (Example: Square Root)
- **Term**: "square root".
- **Notation/Symbol**: √.
- **Definition**: For a given number x, its square root y is a number satisfying y × y = x (where multiplication is already understood).

#### Numeral System (System of Numeration)
A system for representing numbers. Examples:

| Decimal | Roman | Binary |
|---|---|---|
| 47 | XLVII (source OCR: "XZP") | 101111 (source OCR: "101001") |

The same expression "111" represents:
- **111** (one hundred eleven) in **decimal**.
- **7** (seven) in **binary**.
- **3** (three) in **unary**.

> Note: the textbook distinguishes "Numeral System" from "Number System"; the latter (different concept) is discussed later.

### ⚠️ Common Mistakes
- ❌ Calling 6 a "number". → ✅ Strictly, 6 is a numeral (name/symbol); the number is the concept "sixness". The textbook accepts the loose usage.
- ❌ Assuming "111" always means one hundred eleven. → ✅ Its meaning depends on the numeral system (base) used.

### Connections
- Builds on: everyday counting intuition.
- Prerequisite for: §1.3 (Numbers: From Natural to Complex), where formal number sets N, W, Z, Q, R, C are introduced (Chunk 004: Set Operations — Difference & Complement (continued)).

---

## Section: Set Theory — Concept of Set 🔴

### Core Idea
A **set** is a well-defined collection of distinctly identifiable objects (its members or elements), with no element repeated. Modern mathematics (since the mid-20th century) treats "set" as the most fundamental undefined concept — even numbers and geometrical shapes are now defined in terms of sets.

> **In Simple Terms:** A set is like a labelled box: each item inside is uniquely identifiable, no item is duplicated, and you can always say with certainty whether any given thing is or isn't in the box.

### Key Concepts

#### What Counts as a Set?
A collection is "well-defined" iff:
1. The entities in it are **distinctly identifiable**, AND
2. For any entity in the world, we can say definitively whether it belongs to the collection or not.

**Examples that ARE sets:**
- All IGNOU students who enrolled in 2021 for M.A. (Economics).
- The set of decimal digits {0, 1, 2, …, 9}.

**Examples that are NOT sets:**
- "Some of the IGNOU students enrolled in 2021 for M.A. Economics" — vague (which "some"?).
- "All drops of water in a glass" — drops are not distinctly identifiable.
- The barber paradox collection (see below).

#### The Barber Paradox (Russell-style)
> A small village has only one (male) barber, who shaves all those, and only those, males who do not shave themselves. Let X = collection of all villagers shaven by the barber. Then it is not possible to tell whether the barber belongs to X.
>
> - If the barber shaves himself, then by the rule he is shaven only by those who don't shave themselves — contradiction.
> - If the barber does not shave himself, then by the rule he must be shaven by the barber (himself) — contradiction.
>
> Therefore X is not well-defined and not a set.

### Definitions ⭐
- **Set** (working definition): a well-defined collection of distinctly identifiable objects, with no member repeated. ⭐
- **Member / Element**: any entity belonging to a set. ⭐

### ⚠️ Common Mistakes
- ❌ Listing the same element twice in a set: {1, 2, 2, 3}. → ✅ A set has no repeated members; this is the same as {1, 2, 3}.
- ❌ Treating any vague collection ("tall people", "good students") as a set. → ✅ Only well-defined collections are sets.

### Connections
- Builds on: notion of "collection".
- Prerequisite for: all subsequent topics — set notation, relationships between sets, set operations, functions, relations.

---

## Section: Set Notations 🔴

### Core Idea
Sets are denoted with **braces { }**. Members are listed inside the braces, separated by commas. The membership symbol **∈** (epsilon) means "is an element of"; **∉** means "is not an element of". By convention, sets are named with capital letters and elements with lower-case letters (though this is not binding).

### Key Concepts

#### Basic Notation
Example: **Num-Digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}**.
- 0 ∈ Num-Digits, 5 ∈ Num-Digits, 9 ∈ Num-Digits.
- 35 ∉ Num-Digits.

#### Naming Convention
- Set names → start with capital letters (X, Y, N, Num-Digits).
- Elements → lower-case letters (a, b, x, y).
- Names should be **mnemonic** (helpful for remembering contents).

#### Extension for Large/Infinite Sets — Triple Dots "…"
When a set has very many or infinitely many elements with a clear pattern, list a few initial members and use "…":
- {0, 1, 4, 9, …, 100, 121, …, 400, …, 10000} or briefly {0, 1, 4, 9, …, 10000} for squares ≤ 10000.
- This set may be named **Sq_int_less_10001**.

### Definitions
- **∈**: "is an element of" / "belongs to". ⭐
- **∉**: "is not an element of" / "does not belong to". ⭐

---

## Section: Forms of Set Representation 🔴

### Core Idea
Sets can be written in two standard forms: **roster (tabular) form**, listing all elements explicitly inside braces, and **set-builder form**, describing the property the elements share.

### Key Concepts

#### (i) Tabular / Roster Form
Each element (or enough to indicate a pattern) is listed inside braces.
- **Sq_int_less_10001 = {0, 1, 4, 9, …, 10000}**.
- Convenient for small sets; awkward for large or infinite sets.

#### (ii) Set-Builder Form
States the defining property/properties of members. Format: **{x : (conditions on x)}** — the colon ":" (or "|") is read as "such that" or "where".
- **Sq_int_less_10001 = {x : x = y², y is an integer, and x < 10001}**.
- Decimal_digits = {0, 1, …, 9} can be written as:
  - {x : x ∈ N and x < 10}, OR
  - {x ∈ N : x < 10}.

| Form | When to use | Pros | Cons |
|---|---|---|---|
| Roster | Small, finite, explicit | Easy to read at a glance | Impractical for large/infinite sets |
| Set-builder | Large or infinite, when a defining rule exists | Compact, exact | Requires clear description of property |

### ⚠️ Common Mistakes
- ❌ Mixing notations within one expression. → ✅ Stick to one form per set definition.
- ❌ Forgetting the colon "·" or "|" in set-builder form. → ✅ The colon is essential — it separates the element variable from its defining condition.

> **Quick Recall:**
> - **{ }** = set; **∈** = belongs to; **∉** = does not belong.
> - Roster form: list elements.
> - Set-builder form: **{x : property of x}**.
> - Triple dots "…" indicate a continuing pattern.

### Connections
- Builds on: §1.2.1 Concept of Set.
- Prerequisite for: §1.2.4 Relationships Between Sets, §1.2.5 Special Sets, §1.2.7 Set Operations (Chunk 003: Cardinality of a Set).

### Open Questions
- When a set is described in set-builder form, who decides the universe of x — the surrounding context, or must it be stated explicitly?


---

<!-- Continues from: Set notation & forms (Chunk 002: Mathematical Notations (continued) — Functions, Derivatives, Norms) -->
<!-- Continues into: Set operations completion, numbers from natural to complex (Chunk 004: Set Operations — Difference & Complement (continued)) -->

## Section: Cardinality of a Set 🔴

### Core Idea
The **cardinality** of a set X, denoted **|X|** or **#X**, is the number of distinct elements in X. Two unequal sets can have the same cardinality.

> **In Simple Terms:** Cardinality is the size of a set — how many things are in the box, ignoring what those things are.

### Definitions ⭐
- **|X| or #X**: cardinality of X = number of distinct elements. ⭐

### Examples
- **|{1, 3, 5}| = 3**.
- **|∅| = 0** (the empty set has 0 elements).
- **|N| = |W| = |Z| = |Q| = ∞** (all are infinite — countably infinite, by later results).
- **|{0}| = 1**.
- **|{1, 3, 5}| = |{1, 3, 7}| = 3** even though {1, 3, 5} ≠ {1, 3, 7} — equal cardinality does not imply equal sets.

### Connections
- Cardinality is used in §1.2.5 (Power Set: |P(A)| = 2^|A|).

---

## Section: Check Your Progress 1 🔴

### Core Idea
Practice questions on the concept of "set" — whether collections are sets, expressing them in roster/set-builder form, and computing cardinality. (Answers appear later in §1.8 — mark as ⭐ exam-relevant.)

### Examples / Exercises ⭐

**Q1.** Which of the following collections are sets? Justify.
- (i) The collection of all months of a year beginning with letter **M**.
- (ii) The collection of all months of a year beginning with letter **Z**.
- (iii) The collection of ten **most talented** living writers of the world.
- (iv) A team of eleven **most renowned** football players of the world.
- (v) **{1, 2, 2, 3}**.
- (vi) **{1, 2, {2, 3}, 3}**.

**Q2.** For each, write in roster/tabular form and give cardinality:
- (a) Positive prime integer factors of 180.
- (b) Solutions of the quadratic equation x² − 3x − 10 = 0.

**Q3.** Tell which is a set; if it is, (i) write in set-builder form, (ii) state cardinality:
- (a) {6, 9, 12, 15, 18, 21, 24, 27}.
- (b) {2, 4, 8, 16, …}.
- (c) {{1}, {1, 2}, {1, 2, 3}, …, {1, 2, 3, 4, …, 10}}.

> **Quick Recall:**
> - "Most talented" / "most renowned" → **subjective**, not well-defined → **not a set**.
> - {1, 2, 2, 3} = {1, 2, 3}, cardinality 3 (a set, though redundantly written).
> - {1, 2, {2, 3}, 3} has 4 distinct elements: 1, 2, the set {2, 3} (treated as a single element), and 3.

---

## Section: Relationships Between Sets — Equality, Subset, Proper Subset 🔴

### Core Idea
For any two sets X and Y, four main relationships are studied: **equality (=)**, **subset / superset (⊆)**, **proper subset / superset (⊂)**, and **not a subset (⊄)**.

> **In Simple Terms:** Sets can be the same as each other (equal), one can sit inside the other (subset), one can sit *strictly* inside the other with room to spare (proper subset), or they can be unrelated (not a subset).

### Definitions ⭐

#### (i) Equality of Sets — X = Y
Two sets X and Y are **equal** iff every element of X is an element of Y AND every element of Y is an element of X.
- **Notation**: X = Y.
- **Example**: X = {1, 2, 3, 4, 5}, Y = {x : x is a natural number with 1 ≤ x ≤ 5}, W = {3, 5, 2, 4, 1}. Then **X = Y = W** (order does not matter).

#### (ii) Subset / Superset — X ⊆ Y
X is a **subset** of Y if every element of X is also an element of Y. Equivalently: Y is a **superset** of X / X is contained in Y / Y contains X.
- **Notation**: X ⊆ Y.
- **Examples**:
  - X = {a, e, i}, Y = set of all English vowels → X ⊆ Y.
  - **Every set is a subset of itself**: X ⊆ X.

#### (iii) Proper Subset / Proper Superset — X ⊂ Y
X is a **proper subset** of Y if (a) every element of X belongs to Y, AND (b) there is at least one element of Y that does not belong to X.
- **Notation**: X ⊂ Y (also "Y is a proper superset of X").
- **Example**: X = {0, 2, 4, 6, 8} (even decimal digits), Y = {0, 1, 2, …, 9} (all decimal digits). Then X ⊂ Y, since every even digit is a digit, but 1 ∈ Y and 1 ∉ X.
- Note: **X ⊄ X** as a proper subset, because condition (b) fails.

#### (iv) Not a Subset — X ⊄ Y
X ⊄ Y means there exists at least one element of X that does not belong to Y.
- **Example**: X = {1, 5, 10, 15}, Y = {1, 12, 14, 15}. Since 5 ∈ X and 5 ∉ Y, X ⊄ Y. (One witness suffices.)

### Edge Cases & Caveats
- **Notation conflict (textbook remark)**: Some authors use **⊂** for "subset (possibly improper)" and **⊊** for "proper subset". This textbook uses **⊆** for subset and **⊂** for **proper** subset. Be careful when reading other texts.

### ⚠️ Common Mistakes
- ❌ Writing X ⊂ X (claiming a set is a proper subset of itself). → ✅ X ⊆ X is true; X ⊂ X is false (no element of X is "extra").
- ❌ To prove X ⊄ Y, listing all elements not in Y. → ✅ Only one counter-example element is needed.

---

## Section: Establishing Set Relationships 🟡

### Core Idea
A worked methodology for showing each kind of set relationship, using the example sets:
- **A** = {x : x² + 3x + 2 = 0} (roots of the quadratic).
- **B** = {−1, −2}, **C** = {−2}, **E** = {0, −1, −2}.

### Mechanisms / Processes

1. **"Is not a subset" (easiest)**: find one element of the candidate subset that is not in the candidate superset.
   - E ⊄ C, since 0 ∈ E but 0 ∉ C.
   - E ⊄ A, since 0 ∈ E but 0 is not a root of x² + 3x + 2 = 0.

2. **Subset (B ⊆ E)**: take each element of B in turn and verify it lies in E. (For complex cases, take an arbitrary element x ∈ B and show x ∈ E.)

3. **Proper subset (B ⊂ E)**: do step 2, then additionally show there exists an element of E not in B.
   - 0 ∈ E but 0 ∉ B → B ⊂ E (proper).

4. **Equality (A = B)**: do step 2 in **both directions** (show A ⊆ B and B ⊆ A).
   - −1 ∈ B is a root of x² + 3x + 2 = 0, so −1 ∈ A. Similarly −2 ∈ B is a root, so −2 ∈ A. Conversely, since x² + 3x + 2 = 0 is quadratic, it has exactly two roots: −1 and −2. Hence A = B.

> **Quick Recall:**
> - Subset: every element of X is in Y.
> - Proper subset: subset + at least one element of Y not in X.
> - Equality: subset both ways.
> - Not subset: one counter-example suffices.

---

## Section: Check Your Progress 2 🔴

### Examples / Exercises ⭐

**Q1.** Whether X = Y or not (with explanation):
- (i) X = {2, 4, 6, 8, 10}, Y = {x : x is positive even integer and x ≤ 10}.
- (ii) X = {x : x is a multiple of 10}, Y = {10, 15, 20, 25, 30, …}.
- (iii) X = {2, 3}, Y = {x : x is a solution of x² + 5x + 6 = 0}.
- (iv) X = {x : x is a letter in the word FOLLOW}, Y = {y : y is a letter in the word WOLF}.

**Q2.** Find the correct relation among X ⊆ Y, Y ⊆ X, X ⊂ Y, Y ⊂ X, X = Y, etc.:
- (i) X = {x : x is a student enrolled in IGNOU and having Economics as one of the courses}, Y = {x : x is a student enrolled in IGNOU}.
- (ii) X = {x : x is a triangle in a plane}, Y = {x : x is a rectangle in the plane}.
- (iii) X = {x : x is an even natural number}, Y = {x : x is an integer}.
- (iv) X = {1, 2, 3} and Y = {1, {2, 3}, 4, 5}.

**Q3.** For X = {1, {2, 3}, 3, 4}, which are true?
- (i) 2 ∈ X, (ii) ∅ ∈ X, (iii) ∅ ⊄ X, (iv) ∅ ⊆ X, (v) {2, 3} ∈ X, (vi) {2, 3} ⊂ X, (vii) {{2, 3}} ⊂ X.

### Edge Cases & Caveats
- In Q3, note carefully the difference: {2, 3} is an element of X (so {2, 3} ∈ X is **true**), but {2, 3} is **not** a subset of X (the elements 2 and 3 individually are not elements of X).

---

## Section: Special Sets — Universal, Null/Empty, Power, Convex 🔴

### Core Idea
Four types of sets recur repeatedly: the **Universal set** U (the "everything" of a problem context), the **Null/Empty set** ∅ (no members), the **Power set** P(A) (all subsets of A), and **Convex sets** (geometric: line segments stay inside).

> **In Simple Terms:** Universal = the playing field; Empty = nothing; Power = every possible team you could form; Convex = a "no dents" set — straight lines never poke outside.

### Key Concepts

#### a) Universal Set (U)
For any problem, a sufficiently large set containing all entities under discussion is fixed; this is the **Universal set**, denoted **U**. By definition, every set X under consideration satisfies **X ⊆ U**.

**Remarks:**
- Different problems → different universal sets.
- Since X ⊆ X always, we have **U ⊆ U**.
- The concept is **controversial** — leads to paradoxes such as **Russell's paradox** ("the set of all sets" is not a well-defined set, hence not a set). Despite this, the concept is practically very useful.

#### b) Empty / Null / Void Set (∅)
A set with no members. Denoted **∅** or **{ }**.
- **Example**: S = {x : x is an even integer and x² = 9} → no integer satisfies both, so S = ∅.
- **Key fact**: **∅ ⊆ X for every set X**. ⭐

**Proof by contradiction**: Suppose ∅ ⊆ X is false. Then ∃ x ∈ ∅ with x ∉ X. But by definition no element is in ∅ — contradiction. Hence ∅ ⊆ X.

**Convention on "proper" subsets**: Both ∅ and X itself are subsets of X but are **not counted as proper subsets**. All other subsets are proper.

#### c) Power Set — P(A) or 2^A
The set of **all subsets** of A.
- **Example**: A = {1, 2, 3} →
  P(A) = {∅, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
- The notation **2^A** is used because |P(A)| = 2^|A|.

**Important Results on Subsets** (stated without proof):
1. A ⊆ A (every set is a subset of itself).
2. **Transitivity**: if A ⊆ B and B ⊆ C, then A ⊆ C.
3. If A ⊆ B and B ⊆ A, then A = B.
4. If |A| = n, then **|P(A)| = 2ⁿ**. ⭐
   - E.g., |{1, 2, 3}| = 3 → |P({1, 2, 3})| = 2³ = 8.

#### d) Convex Set
A subset S of a space (typically 2-dimensional real space) is **convex** iff for any two points p, q ∈ S, the entire line segment from p to q lies in S.

**Algebraic form**: if x₁, x₂ ∈ S, then every point on the line segment x₁x₂ — represented as **λx₁ + (1 − λ)x₂** for any λ with **0 ≤ λ ≤ 1** — also belongs to S. ⭐

| | Convex | Non-Convex |
|---|---|---|
| Visual | P———Q (segment fully inside) | P—·—Q (segment escapes) |
| Test | All λx₁ + (1−λ)x₂ inside | Some λ produces a point outside |

### Definitions ⭐
- **Universal set U**: largest set under consideration in a given problem context. ⭐
- **Empty/Null set ∅**: set with no elements. ⭐
- **Power set P(A)**: set of all subsets of A. ⭐
- **Convex set**: a set such that the line segment joining any two of its points lies entirely within it. ⭐

### Examples
**Example: Convex set test in R**
- [4, 5) = {x : 4 ≤ x < 5} — convex (any segment between two points stays inside).
- [1, 4] ∪ [7, 11) = {x : 1 ≤ x ≤ 4} ∪ {x : 7 ≤ x < 11} — **not convex** (a point like 5.5 lies on the segment from 3 to 9 but is not in the union).

### ⚠️ Common Mistakes
- ❌ Treating ∅ as having one element (the empty thing). → ✅ ∅ has **zero** elements; |∅| = 0.
- ❌ Counting ∅ or A itself among the proper subsets of A. → ✅ Both are subsets but not proper.
- ❌ Forgetting both endpoints of the convexity inequality: 0 ≤ λ ≤ 1. → ✅ λ ranges over the closed unit interval.

> **Quick Recall:**
> - **|P(A)| = 2ⁿ** if |A| = n.
> - **∅ ⊆ X** for every X.
> - **X ⊆ U** for every X under consideration.
> - **Convex**: λx₁ + (1−λ)x₂ ∈ S for all 0 ≤ λ ≤ 1.

### Connections
- Universal set → Complement of a set (defined as U − X) — see Chunk 004.
- Convex sets → essential in optimisation (Block 5): convex feasible regions, convex objective functions guarantee unique global optima.
- Power set → cardinality of P(A) = 2ⁿ is used in combinatorics.

### Open Questions
- Is the union of two convex sets ever convex? (Yes, only when one is a subset of the other or when they overlap in a special way.)
- What does "convex" mean in higher-dimensional spaces (Rⁿ)? Same definition — segment connecting any two points stays in the set.

---

## Section: Check Your Progress 3 🔴

### Examples / Exercises ⭐

**Q1.** Which of the following is a convex set in R?
- (i) [4, 5) = {x : 4 ≤ x < 5}, (ii) [1, 4] ∪ [7, 11) = {x : 1 ≤ x ≤ 4} ∪ {x : 7 ≤ x < 11}.

**Q2.** What is the cardinality of the power set of {0, 1, 2}?

**Q3.** Let U = {u, v, w, x, y, z}.
- (i) Find the number of subsets of U.
- (ii) Find the number of proper non-empty subsets of U.

**Q4.** List the 8 subsets of {a, b, c, d} containing {d}.

> **Hints:** Q1 → (i) is convex, (ii) is not. Q2 → 2³ = 8. Q3 → (i) 2⁶ = 64; (ii) 64 − 2 = 62 (excluding ∅ and U itself). Q4 → take all 2³ = 8 subsets of {a, b, c} and add d to each.

---

## Section: Quantifiers and Logical Operators 🔴

### Core Idea
**Quantifiers** are symbols expressing "for all" (∀) and "there exists" (∃); **logical operators** include implication (→) and biconditional (↔). They allow precise mathematical statements about elements of sets.

> **In Simple Terms:** ∀ = "for every"; ∃ = "for some"; → = "if … then …"; ↔ = "if and only if". They turn long English sentences into compact mathematical formulas.

### Key Concepts

#### a) Quantifiers

| Symbol | Reads as | Meaning |
|---|---|---|
| (∀x) x ∈ X | "for all x in X" | Statement holds for every element. |
| (∃x) x ∈ X | "for some x in X" / "there exists x in X" | Statement holds for at least one element. |
| (∄ x ∈ X) | "there does not exist x in X" / "there is no x in X (satisfying …)" | No element satisfies the statement. |

If the set X is implicit, just **(∀x)** is used; otherwise **(∀x ∈ X)** or **(∀x) x ∈ X** is written explicitly.

**Example: universal quantifier**
For Sq_int = {0, 1, 4, 9, …}, every member is a square of some integer:
**(∀x ∈ Sq_int) (x = y²), for some y ∈ Z**, where Z = set of integers.

Refined further:
**(∀x ∈ Sq_int) (∃y ∈ Z) (x = y²)**.

**Example: existential quantifier**
Some element of Sq_int is greater than 100 (e.g., 144):
**(∃x ∈ Sq_int) (x > 100)**.

**Example: non-existence**
No member of Sq_int is less than 0:
**(∄x ∈ Sq_int) (x < 0)**.

#### b) Logical Operators

| Symbol | Reads as | Meaning |
|---|---|---|
| **P → Q** | "if P then Q" | Implication. |
| **P ↔ Q** | "P if and only if Q" / "P iff Q" | Biconditional / equivalence. |

**P ↔ Q** is equivalent to **(P → Q) AND (Q → P)** taken together.

**Examples:**
- "If x is an integer then x² is a non-negative integer": **(∀x ∈ Z) (x² ≥ 0)**.
- "x² = 100 if and only if x = 10 or x = −10": **(x² = 100) ↔ (x = 10 ∨ x = −10)**.

### ⚠️ Common Mistakes
- ❌ Reading **x = 10 → x² = 100** as bidirectional. → ✅ This is one-way only. The reverse (x² = 100 → x = 10) is **false** because x could be −10.
- ❌ Confusing **∃** ("at least one") with **∃!** ("exactly one").
- ❌ Negating ∀ incorrectly. → ✅ ¬(∀x P(x)) ⇔ (∃x ¬P(x)).

> **Quick Recall:**
> - **∀** = for all; **∃** = there exists; **∄** = does not exist.
> - **→** one-way; **↔** two-way.
> - "If x = 10 then x² = 100" — true. "If x² = 100 then x = 10" — **false** (x could be −10).

### Connections
- Used in proofs throughout Block 4 (Real Analysis).

---

## Section: Relation vs Operation 🟡

### Core Idea
A **relation** returns TRUE or FALSE — it states a fact (e.g., 8 < 15). An **operation** produces a new value — it generates something (e.g., 8 + 15 = 23). Both take inputs from a set; the difference is in their output type.

> **In Simple Terms:** Relations answer yes/no questions ("is 3 less than 5?"); operations build new things ("what is 3 + 5?").

### Key Concepts

#### Relations on Numbers (Examples)
- 8 < 15 → relation "less-than" returns **TRUE**.
- 8 ≠ 15 → relation "not equal to" returns **TRUE**.
- 3 + 5 = 8 → relation "is equal to" returns **TRUE**.
- 7 < 5 → relation returns **FALSE**.

#### Operations on Numbers (Examples)
- 8 + 15 → produces new number **23**.
- 8 − 15 → produces new number **−7**.
- 16 ÷ 4 → produces new number **4**.

#### Arity
- **Binary operation**: needs two inputs (e.g., +, −, ×, ÷).
- **Unary operation**: needs one input (e.g., square root √, absolute value |·|).

#### Cross Product (Cartesian Product) of Sets
For non-empty sets A₁ and A₂, their **cross-product** A₁ × A₂ is the set of all **ordered pairs** (a₁, a₂) with a₁ ∈ A₁ and a₂ ∈ A₂.

Generalised to n sets: A₁ × A₂ × … × Aₙ is the set of all n-tuples (a₁, a₂, …, aₙ) with aᵢ ∈ Aᵢ for i = 1, …, n.

#### Relation on a Set (Formal)
A **relation** on set X (of arity n) is a subset of the n-fold cross-product X × X × … × X.
- It returns exactly one of "true" or "false".
- **Example**: "is-male" — arity 1; "is-mother-of" — arity 2.
- If Sheela is not the mother of Mohan, the relation **is-mother-of(Sheela, Mohan)** returns **false**.

#### Operation on a Set (Formal)
An **operation** of arity n on X maps X × X × … × X (n times) to **X itself** — i.e., it returns an element of X.
- **Example**: "square" on N has arity 1; "sum" on N has arity 2.
- In both cases the value returned is a member of N.

#### Connection between Relation and Operation
An (n+1)-ary relation on a set can be converted to an n-ary operation. **Example**:
- "is-mother-of" is a binary relation on the set of all humans.
- It can be converted to the unary operation "name-mother-of(x)", returning the name of the mother of x.
- E.g., is-mother-of(Mohan, Sita) = true ⇔ name-mother-of(Mohan) = Sita.

### Definitions ⭐
- **Cross-product (Cartesian product)** A × B: set of all ordered pairs (a, b) with a ∈ A, b ∈ B. ⭐
- **Relation on X (arity n)**: a subset of Xⁿ; returns true/false. ⭐
- **Operation on X (arity n)**: a function Xⁿ → X; returns an element of X. ⭐
- **Binary**: arity 2 (two inputs).
- **Unary**: arity 1 (one input).

### ⚠️ Common Mistakes
- ❌ Treating "=" as an operation. → ✅ "=" is a relation (returns true/false), whereas "+" is an operation (returns a number).
- ❌ Thinking ordered pairs are unordered. → ✅ (a, b) ≠ (b, a) in general (whereas the **set** {a, b} = {b, a}).

> **Quick Recall:**
> - **Relation**: outputs TRUE/FALSE. Examples: <, =, ≠, ⊆.
> - **Operation**: outputs a new element. Examples: +, −, ×, ÷, √, |·|, ∪, ∩.
> - **Arity**: number of inputs (unary = 1, binary = 2).

---

## Section: Operations on Sets — Union, Intersection, Difference (start) 🔴
<!-- Continues into: complement and worked examples — Chunk 004 -->

### Core Idea
Given two sets X and Y, three **binary** set operations (union, intersection, difference) and one **unary** operation (complement) generate new sets from given ones.

### Definitions ⭐

#### a) Union — X ∪ Y
**X ∪ Y = {x : x ∈ X or x ∈ Y}** (inclusive "or" — x may be in both). ⭐
- **Example**: X = {1, 2, 3, 4}, Y = {2, 3, 5, 8, 9} → **X ∪ Y = {1, 2, 3, 4, 5, 8, 9}**.
- Elements common to both (2, 3) appear only once.

#### b) Intersection — X ∩ Y
**X ∩ Y = {x : x ∈ X and x ∈ Y}**. ⭐
- **Example**: X = {1, 2, 3, 4}, Y = {2, 5, 8, 3, 9} → **X ∩ Y = {2, 3}**.

#### c) Difference — X − Y
**X − Y = {x : x ∈ X and x ∉ Y}**. ⭐
- (Continued in Chunk 004 with examples and complement.)

### Connections
- Continues into: complement, worked examples, and Check Your Progress 4 (Chunk 004: Set Operations — Difference & Complement (continued)).
- Foundation for: probability theory (Block 8) where events are sets and probability axioms involve ∪, ∩, complement.


---

<!-- Continues from: Set operations (Chunk 003: Cardinality of a Set) -->

## Section: Set Operations — Difference & Complement (continued) 🔴
<!-- Continues from: Union and Intersection (Chunk 003: Cardinality of a Set) -->

### Core Idea
Completing the four set operations: the **difference** X − Y removes Y's elements from X, and the **complement** X′ = U − X gives all elements in the universe U not in X.

### Examples
**Example: Difference**
X = {1, 2, 3, 4}, Y = {2, 5, 8, 3, 9}.
- **X − Y = {1, 4}** (elements of X not in Y).
- **Y − X = {5, 8, 9}** (elements of Y not in X).
- **Note**: X − Y ≠ Y − X in general (difference is not commutative).

#### d) Complement of a Set — X′
**Complement** of a set X is a special case of the difference: it requires a fixed Universal set U.
- **Definition**: **X′ = U − X**. ⭐
- **Example**: U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, X = {2, 5, 8, 3, 9} → **X′ = {1, 4, 6, 7, 10}**.

**Alternative notations** for complement: **X′**, **~X**, **Xᶜ**.

### Definitions ⭐
- **Union ∪**: X ∪ Y = {x : x ∈ X or x ∈ Y}. ⭐
- **Intersection ∩**: X ∩ Y = {x : x ∈ X and x ∈ Y}. ⭐
- **Difference −**: X − Y = {x : x ∈ X and x ∉ Y}. ⭐
- **Complement ′**: X′ = U − X (depends on the chosen universe U). ⭐

### ⚠️ Common Mistakes
- ❌ Computing X − Y as Y − X. → ✅ Not commutative; check direction.
- ❌ Forgetting to specify U when using complement. → ✅ Complement is undefined without an explicit universal set.

---

## Section: More Clarifications — Operands, Values, Operators 🟡

### Core Idea
Distinguish **operands/arguments/inputs** (what you put in), **value/result/output** (what you get), and **operator** (the symbol denoting the operation/relation).

### Key Concepts

#### Operands vs Value
For X = {1, 2, 3, 4} and Y = {2, 3, 5, 8, 9}: X ∪ Y = {1, 2, 3, 4, 5, 8, 9}.
- **Operands / arguments / inputs**: {1, 2, 3, 4} and {2, 3, 5, 8, 9}.
- **Value / result / output**: {1, 2, 3, 4, 5, 8, 9}.

This terminology applies equally to relations:
- For 7 < 5 (returns FALSE): operands = 7 and 5; value = FALSE.

#### Operation vs Operator
- **Operator**: the **symbol** (e.g., **∪** for union, **<** for less-than).
- **Operation**: the **process** of computing a result from operands using an operator.

| Concept | Example | What it refers to |
|---|---|---|
| Operator | ∪, ∩, +, < | The symbol |
| Operation | "Take the union of X and Y to get …" | The process / mapping |
| Operand | X, Y, 7, 5 | The inputs |
| Value | {1, 2, …}, FALSE | The output |

---

## Section: Check Your Progress 4 🔴

### Examples / Exercises ⭐
**Q1.** Let X = {1, {2, 3}, {4, 5}, 6} and Y = {1, {2, 4}, {5, 6, 7}}. Find:
- (a) X ∪ Y
- (b) X ∩ Y
- (c) X − Y
- (d) Y − X

> **Hint**: Treat each "{…}" element as a single object. So {2, 3} ∈ X but {2, 3} ∉ Y (because Y contains {2, 4}, not {2, 3}); only **1** is common to both.

---

## Section: Numbers — Standard Number Sets 🔴

### Core Idea
The standard hierarchy of number sets — Natural ⊂ Whole ⊂ Integer ⊂ Rational ⊂ Real ⊂ Complex — with their conventional symbols (N, W, Z, Q, R, C) is the backbone of all subsequent mathematics.

> **In Simple Terms:** Math builds numbers in layers: counting numbers → add zero → add negatives → add fractions → add √2 and π → add imaginary i. Each layer fits inside the next.

### Definitions ⭐
- **N = {1, 2, 3, …}**: set of **natural / counting numbers**. ⭐
- **W = {0, 1, 2, 3, …}**: set of **whole numbers** (natural numbers + 0). ⭐
  - *Note*: many modern conventions treat 0 as a natural number, so N = W and W is redundant.
- **Z = {…, −3, −2, −1, 0, 1, 2, 3, …}**: set of **integers** (German "Zahlen"). ⭐
- **Q = {x : x = p/q with q ≠ 0, and p, q ∈ Z}**: set of **rational numbers** ("quotient"). ⭐

### Containment Hierarchy (so far) ⭐
**∅ ⊂ N ⊂ W ⊂ Z ⊂ Q**.

**Why Z ⊂ Q?** For any n ∈ Z, n = n/1 ∈ Q. Also, 3/4 ∈ Q but 3/4 ∉ Z, so Z is a *proper* subset of Q.

### Connections
- Extended below to include R (real) and C (complex).

---

## Section: R — The Set of Real Numbers 🔴

### Core Idea
The **real numbers** R correspond to all points on a continuous straight line (the "number line"). They include all rationals AND irrational numbers like √2 and π. R is the most frequently used number set in numerical problem-solving.

> **In Simple Terms:** A real number is anything that can be a position on the number line — including familiar fractions, plus the "filler" numbers like √2 = 1.4142… that fill in the gaps between fractions.

### Mechanisms / Processes — Constructing R Geometrically

1. **Pick a line**, mark a left point as **0**, a right point as **1**.
2. **Natural numbers**: mark points to the right of 1 at equal spacings → 2, 3, 4, … .
3. **Negative integers**: mark points to the left of 0 at equal spacings → −1, −2, −3, … .
4. **Rational numbers**: e.g., for **3.45**, divide [3, 4] into 100 equal parts and mark the 45th part to the right of 3.
5. **Irrational numbers**: e.g., for **√2**, construct a unit square; its hypotenuse has length √2; mark this distance to the right of 0 on the number line.
6. **Result**: every point on the line corresponds to a real number, and conversely.

### Definitions ⭐
- **Real number**: a number obtained by corresponding to a point on a straight line (as above). ⭐
- **R = {x | x is a real number}**.
- **Irrational number**: a real number that is **not** rational. The set of irrationals is **R − Q** (also written R \ Q). ⭐
  - **Example**: √2 (proven irrational — no p/q exists with p² /q² = 2).
  - **Fact**: there are **more** irrational reals than rational reals (irrationals are uncountable, rationals are countable).

### Extended Containment Hierarchy ⭐
**∅ ⊂ N ⊂ W ⊂ Z ⊂ Q ⊂ R**.

**Why Q ⊂ R (proper)?** √2 ∈ R but √2 ∉ Q.

---

## Section: Real Number Intervals 🔴

### Core Idea
An **interval** is a set of real numbers between two boundaries; it is **closed** if it includes both boundaries, **open** if it excludes both, and **semi-open/semi-closed** if it includes exactly one.

> **In Simple Terms:** Square brackets "include the endpoint"; round brackets (or reversed square brackets) "exclude the endpoint".

### Definitions ⭐ (illustrated with bounds 3 and 7.5)

| Interval | Reads as | Includes 3? | Includes 7.5? | Type |
|---|---|---|---|---|
| **[3, 7.5]** | "closed interval 3 to 7.5" | Yes | Yes | Closed |
| **(3, 7.5]** or **]3, 7.5]** | "left-open, right-closed" | No | Yes | Semi-open / semi-closed |
| **[3, 7.5)** or **[3, 7.5[** | "left-closed, right-open" | Yes | No | Semi-open / semi-closed |
| **(3, 7.5)** or **]3, 7.5[** | "open interval" | No | No | Open |

> The textbook uses both the bracket notation (·, ·) and the French-style "outward" bracket notation ]·, ·[ — both are equivalent.

### ⚠️ Common Mistakes
- ❌ Using **(3, 7.5)** for the ordered pair when the context is intervals. → ✅ Context disambiguates; the same bracket notation is overloaded.
- ❌ Confusing closed vs open intervals when checking convexity or extreme values. → ✅ Closed intervals attain max/min; open ones may not.

> **Quick Recall:**
> - **[ ] include endpoints**, **( ) exclude endpoints**.
> - 4 types: closed, open, two semi-open variants.

### Connections
- Used in defining continuity, limits (Block 3), convex sets (§1.2.5, Chunk 003).

---

## Section: Complex Numbers — C 🔴

### Core Idea
**Complex numbers** extend the reals by introducing **i** with **i² = −1**, allowing solutions to equations like x² + 1 = 0 that have no real solutions. C contains R as a proper subset.

> **In Simple Terms:** Some equations have no real-number answers (e.g., x² = −1). Mathematicians invented a new number i with i² = −1, and built complex numbers a + bi to handle these cases.

### Definitions ⭐
- **i**: the imaginary unit, with **i² = −1**. ⭐
- **C = {z : z = x + iy, where x, y ∈ R}** = set of **complex numbers**. ⭐
- (x + iy is also written x + yi.)

### Why R ⊂ C (proper)
- Any real x ∈ R can be written x = x + i·0, so x ∈ C → R ⊆ C.
- 1 + i·2 ∈ C but 1 + i·2 ∉ R (and i = 0 + i·1 ∈ C but i ∉ R).
- Therefore **R ⊂ C** (proper).

### Final Containment Hierarchy ⭐
**∅ ⊂ N ⊂ W ⊂ Z ⊂ Q ⊂ R ⊂ C**.

### Edge Cases & Caveats
- Symbols **∅, N, W, Z, Q, R, C** are **standard** and may be used without redefinition. Custom set names (like **Sq_int**) must be defined fresh in each new context.

---

## Section: Number Miscellany 🟡

### Core Idea
A grab-bag of clarifying facts: examples illustrating which numbers belong to which classes; arithmetic vs algebraic operations; arithmetic relations; the difference between fraction and rational number; prime numbers; the constant π; and the historical reasoning behind the symbols N, Z, Q, R, C.

### Key Concepts

#### Number Classification Examples

| Number | N? | Z? | Q? | Irrational? | R? | C? |
|---|---|---|---|---|---|---|
| 3 | ✓ | ✓ | ✓ |  | ✓ | ✓ |
| −12 |  | ✓ | ✓ |  | ✓ | ✓ |
| 8.7 |  |  | ✓ |  | ✓ | ✓ |
| 2/3 |  |  | ✓ |  | ✓ | ✓ |
| √2 |  |  |  | ✓ | ✓ | ✓ |
| π |  |  |  | ✓ | ✓ | ✓ |
| 7 − 3i |  |  |  |  |  | ✓ |

> Each example is constructed so that it does NOT have the preceding stronger properties. E.g., √2 is irrational so not rational, not integer, not natural.

#### Arithmetic / Algebraic Operations
- **Binary** (need 2 inputs): **+, −, ×, ÷**.
- **Unary** (need 1 input):
  - **Exponent / power**: x², and in general x^n for fixed n.
  - **Absolute value**: **|x| = −x if x < 0; |x| = x if x ≥ 0**. ⭐
    - |5| = 5 and |−5| = 5.

#### Arithmetic Relations
Examples: **=, ≠, <, ≤, >, ≥**.

#### Fraction vs Rational Number
- **3/5** and **6/10** are two **different** fractions but **the same** rational number.
- Two fractions p/q and r/s (with q ≠ 0, s ≠ 0) are equal as rationals iff **p × s = q × r**. ⭐
  - 3/5 = 6/10 because 3 × 10 = 5 × 6 = 30.

#### Prime Numbers
- A natural number p is **prime** if the only natural numbers dividing p are **1 and p itself**. ⭐
- Examples: 2, 3, 5, 19, 31 — prime. 4, 21 — not prime.
- **1 is NOT a prime**, even though only 1 divides it. The reason: **1 is a unit in N** (1 × 1 = 1), and only 1 has this property. For any q ≠ 1 in N, no s in N satisfies q × s = 1.

#### The Constant π
- **π** denotes the real number defined by **c = πd**, with c = circumference of a circle and d = its diameter.
- π is **irrational** (proof beyond scope).

#### Nomenclature for Number-Set Symbols
- **N**: from "Natural" (Natural Numbers).
- **Z**: from German **Zahlen** (Integers). Sometimes denoted **I**.
- **Q**: from "Quotient" (Quotient Numbers, i.e., rationals).
- **R**: from "Real".
- **C**: from "Complex".

### ⚠️ Common Mistakes
- ❌ Saying 3/5 and 6/10 are different rational numbers. → ✅ They are different *fractions* but the same *rational number*.
- ❌ Including 1 as a prime. → ✅ 1 is a unit, not a prime.
- ❌ Thinking |x| produces a negative output. → ✅ |x| ≥ 0 always.

> **Quick Recall:**
> - π and √2: irrational reals.
> - 1 is **not** a prime.
> - p/q = r/s iff p·s = q·r.
> - |x| = max(x, −x); always ≥ 0.

---

## Section: Properties of Real Numbers as an Ordered Field 🔴

### Core Idea
R, equipped with **+** (addition) and **×** (multiplication), satisfies the **Field axioms**; with the relation **<** added it becomes an **Ordered Field**; with the unary **|·|** (modulus) added, it gains **metric/norm** properties. These axioms underpin every algebraic manipulation in the course.

> **In Simple Terms:** R is a "well-behaved" set: you can add, subtract, multiply, divide (except by 0), compare, and measure distances — all the operations behave the way arithmetic intuition suggests.

### Definitions / Properties

#### a) Field Properties (R, +, ×) — for all x, y, z ∈ R ⭐

| # | Property | Statement |
|---|---|---|
| 1 | Closure | x + y ∈ R, and x × y ∈ R. |
| 2 | Associativity | (x + y) + z = x + (y + z); (x × y) × z = x × (y × z). |
| 3 | Existence of unique identities | 0, 1 ∈ R such that x + 0 = 0 + x = x and x × 1 = 1 × x = x. |
| 4 | Existence of unique inverses | For every x ∈ R, ∃ (−x) such that x + (−x) = (−x) + x = 0. For x ≠ 0, ∃ x⁻¹ such that x × x⁻¹ = x⁻¹ × x = 1. |
| 5 | Commutativity | x + y = y + x; x × y = y × x. |
| 6 | Distributivity (× over +) | x × (y + z) = x × y + x × z. |

#### b) Ordered Field Properties (additional, with relation <) — for all x, y, z ∈ R ⭐

| # | Property | Statement |
|---|---|---|
| 1 | Positivity preservation | If 0 < x and 0 < y then 0 < x + y and 0 < x × y. |
| 2 | **Trichotomy** | For x ∈ R, exactly one of (a) x < 0, (b) x = 0, (c) 0 < x is true. ⭐ |
| 3 | **Transitivity** | If x < y and y < z, then x < z. ⭐ |
| 4 | Monotone property of addition | If x < y, then x + z < y + z. |
| 5 | Monotone property of multiplication | If x < y and 0 < z, then x × z < y × z. |
| 6 | **Archimedean property** | Given two positive numbers A and B, there exists a natural number n such that **B < n × A**. ⭐ |

#### c) Metric / Norm Properties (with |·| modulus) — for all x, y, z ∈ R ⭐

| # | Property | Statement |
|---|---|---|
| 1 | Non-negativity & definiteness | |x| ≥ 0; |x| = 0 iff x = 0. |
| 2 | Symmetry under negation | |x| = |−x|. |
| 3 | Bracketing | −|x| ≤ x ≤ |x|. |
| 4 | **Triangle inequality** | **\|x + y\| ≤ \|x\| + \|y\|**. ⭐ |

#### Distance Function ‖·‖ : R × R → R
Defined by **‖x − y‖ = |x − y|**. For all x, y, z ∈ R:

| # | Property |
|---|---|
| 1 | ‖x − y‖ ≥ 0; ‖x − y‖ = 0 iff x = y. |
| 2 | ‖x − y‖ = ‖y − x‖ (symmetry). |
| 3 | **Triangle Inequality**: ‖x − z‖ ≤ ‖x − y‖ + ‖y − z‖. ⭐ |

### ⚠️ Common Mistakes
- ❌ Forgetting the multiplicative inverse exists only for x ≠ 0. → ✅ 0 has no multiplicative inverse.
- ❌ Asserting the triangle inequality with equality always. → ✅ Equality holds only when x and y have the same sign (or one is zero).
- ❌ Misapplying monotone multiplication: multiplying both sides of an inequality by a **negative** number reverses the inequality. → ✅ The textbook's monotone property requires **0 < z**.

> **Quick Recall:**
> - 6 Field axioms + 6 Order axioms + 4 Metric axioms.
> - **Trichotomy**: x is <0, =0, or >0 — exactly one.
> - **Archimedean**: no number in R is "infinitely large" relative to others — multiples of any positive A eventually exceed any B.
> - **Triangle inequality**: |x + y| ≤ |x| + |y|.

### Connections
- Foundation for **real analysis** (Block 4): completeness, sequences, continuity all build on these axioms.
- The Archimedean property is critical for limits and ε-δ proofs.

---

## Section: Decimal Representation of Rational and Irrational Numbers 🔴

### Core Idea
Every real number has a decimal representation. **Rationals** have either **terminating** or **non-terminating recurring (repeating)** decimal expansions; **irrationals** have **non-terminating, non-repeating** expansions.

> **In Simple Terms:** Rational = decimals that stop or repeat in a pattern; Irrational = decimals that go on forever with no pattern (like π, √2).

### Key Concepts

#### (i) Terminating Decimal — Rational
**3/8 = 0.375** — finite number of digits after the decimal.

#### (ii) Non-Terminating Recurring Decimal — Rational
**7/3 = 2.333…** = **2.3̄** (the digit 3 repeats forever).

**29/7 = 4.142857142857142857… = 4.142857** (the block "142857" repeats forever).

**Notation**: a bar over a digit (or block of digits) means "repeats forever". E.g., **2.3̄** for 2.333… and **4.142857** with bar over 142857.

#### (iii) Non-Terminating Non-Recurring Decimal — Irrational
**π = 3.14159…** (no pattern).
**√2 = 1.41421…** (no pattern; OCR shows "1.4142857..." but the standard value is 1.41421356…).

### Mechanisms / Processes — Converting Decimals to Fractions

**Example: 187.0145083 as a fraction**
1. Count digits after the decimal point: **7** digits → write **10⁷ = 10,000,000** as denominator (a 1 followed by seven 0s).
2. Numerator = the number with the decimal point removed: **1,870,145,083**.
3. So 187.0145083 = **1,870,145,083 / 10,000,000**.

[Note on OCR: source shows "748058003 / 400000" after a simplification step — apparent OCR distortion. The general rule is: place a 1 followed by as many 0s as digits after the decimal point in the denominator; numerator = the digits without the decimal point. Then divide both by the GCD to simplify.]

**Process summary**:
1. Move decimal to make integer numerator.
2. Denominator = 10^(number of digits past decimal).
3. Simplify by dividing numerator and denominator by their GCD (e.g., divide by 25, then look for further common factors).

### ⚠️ Common Mistakes
- ❌ Thinking 0.999… is different from 1. → ✅ 0.9̄ = 1 exactly (a classic surprise).
- ❌ Assuming all non-terminating decimals are irrational. → ✅ They are irrational only if they are also non-repeating; 0.333… = 1/3 is rational.

> **Quick Recall:**
> - Terminating decimal → rational.
> - Repeating decimal → rational.
> - Non-terminating, non-repeating → irrational.
> - To convert: use 10^k denominator, then simplify by GCD.

---

## Section: Real Number Exponentiation 🔴

### Core Idea
**Exponentiation** **xⁿ** is repeated multiplication of the **base** x by itself **n** times. The definition extends naturally to **0**, **negative integers**, and **fractional/real** exponents (via roots).

> **In Simple Terms:** x³ means x × x × x. x⁰ = 1, x⁻¹ = 1/x, and x^(1/n) means the n-th root.

### Definitions ⭐

#### Positive Integer Exponent
For **n ∈ N**, **xⁿ = x · x · x · … · x** (n times). x is the **base**; n is the **exponent** (or power).
- **Examples**:
  - 19⁴ = 19 × 19 × 19 × 19.
  - (−15)³ = (−15) × (−15) × (−15).
  - (3/4)⁵ = 3⁵ / 4⁵.
- **General rule**: **(x/y)ⁿ = xⁿ / yⁿ**.

#### Zero and Negative Integer Exponent
- **x⁰ = 1**. ⭐
- **x⁻¹ = 1/x**.
- **x⁻ⁿ = (1/x)ⁿ = 1/xⁿ** for n ∈ N. ⭐
- **Example**: 19⁻³ = (1/19)³ = (1/19)(1/19)(1/19) = 1/6859.

#### Rules of Exponents (for m, n ∈ Z, and indeed m, n ∈ R) ⭐

| Rule | Formula |
|---|---|
| Product of same base | **x^(m+n) = xᵐ · xⁿ** |
| Power of a power | **x^(mn) = (xᵐ)ⁿ** |
| Negative exponent | **x⁻ⁿ = 1/xⁿ** |
| Quotient of same base | **x^(m−n) = xᵐ / xⁿ** |
| Power of product | **(x · y)ᵃ = xᵃ · yᵃ** |
| Power of quotient | **(x/y)ᵃ = xᵃ / yᵃ** |

(These hold for any real or even complex exponent a.)

#### Fractional Exponents and Roots
- **√2** means the number whose square is 2: √2 × √2 = 2.
- **⁴√7** means the 4th root of 7: ⁴√7 × ⁴√7 × ⁴√7 × ⁴√7 = 7.
- **In general**: for **n ≠ 0**, **ⁿ√x = x^(1/n)**, where x may be any real (or complex) and n is a natural number.

#### General Fractional Exponents
For **m ∈ Z, n ∈ N**:
- **x^(m/n) = x^(m·(1/n)) = ⁿ√(xᵐ)** = (ⁿ√x)ᵐ. ⭐
- For n ≠ 0: **x^(m/n) = (x^(1/n))ᵐ = (ⁿ√x)ᵐ**.

#### Arithmetic Operations on Bases
- **Multiplication / division of same exponent**:
  - **(x · y)ᵃ = xᵃ · yᵃ**.
  - **(x/y)ᵃ = xᵃ / yᵃ**.
- **Addition / subtraction of like-exponent expressions** **xⁿ + yⁿ** or **xⁿ − yⁿ**: treated as **almost independent irreducible expressions**, except when x and y share a common factor ≠ 1.

### Examples
**Example: Factoring a sum of powers using common factor**
3⁵ + 6⁷:
- 6 = 3 × 2, so 6⁷ = (3 × 2)⁷ = 3⁷ × 2⁷.
- 3⁵ + 6⁷ = 3⁵ + 3⁷ × 2⁷ = 3⁵ × (1 + 3² × 2⁷) = 3⁵ × (1 + 9 × 128) = 3⁵ × (1 + 1152) = 3⁵ × 1153.

(The textbook's worked form: 3⁵ + 6⁷ = 3⁵ + (3 × 2)⁷ = 3⁵[(3)² × (2)⁷ + 1] — same result; demonstrates extracting the common base.)

### ⚠️ Common Mistakes
- ❌ Treating x^(1/2) + y^(1/2) as (x + y)^(1/2). → ✅ **Not equal**: √x + √y ≠ √(x + y) in general.
- ❌ Assuming (xᵐ)ⁿ = x^(m+n). → ✅ It equals **x^(mn)** (multiply, not add).
- ❌ Computing 0⁰ as 1 or 0 without context. → ✅ 0⁰ is conventionally 1 in combinatorics but indeterminate in calculus.
- ❌ Forgetting x⁻ⁿ ≠ −xⁿ. → ✅ x⁻ⁿ = 1/xⁿ; the minus sign in the exponent flips the number, not its sign.

> **Quick Recall:**
> - x^(m+n) = xᵐ · xⁿ.
> - (xᵐ)ⁿ = x^(mn).
> - x⁰ = 1.
> - x⁻ⁿ = 1/xⁿ.
> - x^(1/n) = ⁿ√x.
> - (xy)ᵃ = xᵃyᵃ; (x/y)ᵃ = xᵃ/yᵃ.

### Connections
- Foundation for: logarithms (inverse of exponentiation), exponential functions e^x (Block 3), growth/decay models in economic dynamics (Block 6), compound interest.

---

## Section: Check Your Progress 5 🔴

### Examples / Exercises ⭐
**Q1.** Express the decimal number **18725.4625** as a fraction.

> **Hint**: 4 digits after the decimal → denominator 10⁴ = 10,000. Numerator = 187,254,625. So 18725.4625 = 187,254,625 / 10,000. Then divide both by GCD (here both are divisible by 125): = 1,498,037 / 80. Verify by long division.

---

## Section: Let Us Sum Up — Summary of Operators 🟢

### Core Idea
This unit gave a bird's-eye view of the two foundational concepts of mathematics — **number** (basis of conventional mathematics) and **set** (basis of modern mathematics) — and the operators and relations governing each.

### Key Concepts (Summary Tables)

| Category | Examples |
|---|---|
| Set operators | **∪** (union), **∩** (intersection), **−** (difference), **′** (complement) |
| Set-relational symbols | **=**, **⊆** (subset), **⊂** (proper subset), **⊄** (not subset), **∈** (belongs to), **∉** (does not belong) |
| Algebraic / arithmetic operators | **+, −, ×, ÷, √, |·|, log, eˣ** |
| Algebraic / arithmetic relational symbols | **=, ≠, <, ≤, >, ≥** |

---

## Section: Key Words (Glossary) 🔴

### Definitions ⭐

- **Cross-Product of sets**: For two non-empty sets A₁ and A₂, A₁ × A₂ is the set of all ordered pairs (a₁, a₂) with a₁ ∈ A₁, a₂ ∈ A₂. Generalises to A₁ × A₂ × … × Aₙ as the set of all n-tuples (a₁, a₂, …, aₙ) with aᵢ ∈ Aᵢ for i = 1, 2, …, n. ⭐

- **Number**: An abstract concept used for counting, measuring, or labelling. Made tangible through numerals — e.g., "five" is purely an idea, made tangible through the numeral **5**. ⭐

- **Operation on a set X**: An operation of arity n maps the n-fold cross-product of X with itself to **X itself** (returns an element of X). E.g., square on N (arity 1) and sum on N (arity 2) both return a number. ⭐

- **Relation on a set X**: A relation of arity n is a **subset of the n-fold cross-product** of X with itself; returns exactly **true or false**. E.g., is-male (arity 1), is-mother-of (arity 2). ⭐

- **Set**: A well-defined collection of objects, where a collection C is well-defined iff for any x we can determine whether x belongs to C or not. ⭐

### Connections
- These definitions tie together every section of Unit 1 and serve as the working vocabulary for all subsequent units.

### Open Questions
- How does the textbook later distinguish "Number System" (different from Numeral System mentioned in §1.1)?
- The exercises at §1.9 and answers at §1.8 likely appear in the next chunk — do they confirm the conjectured answers above?


---


## Section: Unit 1 — Answers/Hints to Check Your Progress Exercises 🟡
<!-- Continues from: Unit 1 (Chunks 001-004) -->

### Core Idea
This section provides solutions and hints for the five "Check Your Progress" sets in Unit 1 (Fundamental Concepts of Mathematics), covering set definition, set equality/subset relations, convex sets and power sets, set operations (union, intersection, difference) on sets-of-sets, and decimal-to-rational conversion. These answers ratify the rigorous definitions established earlier in the unit.

> **In Simple Terms:** A worked-answer key — it confirms how to test whether a collection is a set, how to compare/operate on sets, and how to convert decimals to fractions.

### Key Concepts

#### CYP 1 — Identifying Sets
- (i), (ii) [empty], (vi) [4 elements, no repetition] are valid sets.
- (iii) "most renowned" and (iv) "most talented" are NOT sets — the defining property is not well-defined.
- (v) is generally not a set because repetition of elements is not allowed in set notation.

#### CYP 2 — Set Equality, Subset, True/False
- 1(i) X = Y; (ii) X ≠ Y because 15 ∈ Y, 15 ∉ X; (iii) X ≠ Y because 2 ∈ X, 2 ∉ Y; (iv) X = Y.
- 2(i) X ⊂ Y (IGNOU has students enrolled in other disciplines); (ii) X ⊄ Y and Y ⊄ X; (iv) X ⊂ Y; (v) X ⊄ Y as 2 ∈ X, 2 ∉ Y; Y ⊄ X as {2,3} ∈ Y, {2,3} ∉ X.
- 3 True/False answers: (i) F, (ii) F, (iii) F, (iv) T, (v) T, (vi) F, (vii) T.

#### CYP 3 — Convexity, Power Sets
- Convexity: (i) is convex; (ii) is NOT convex.
- Power-set count for the 6-element universe: 2⁶ = 64 subsets.
- Proper non-empty subsets = 64 − 2 = 62 (exclude U itself and ∅).
- Listed subsets containing d: {d}, {a,d}, {a,b,d}, {a,c,d}, {a,b,c,d}, {b,d}, {b,c,d}, {c,d}.

#### CYP 4 — Set Operations on Sets-of-Sets
For X = {1, {2,3}, {4,5}, 6} and Y = {1, {2,4}, {5,6,7}}:
- X ∪ Y = {1, {2,3}, {4,5}, 6, {2,4}, {5,6,7}}
- X ∩ Y = {1}
- X − Y = {{2,3}, {4,5}, 6}
- Y − X = {{2,4}, {5,6,7}}

#### CYP 5 — Decimal to Rational
- 18725.4625 = 187254625/10000; simplify by dividing numerator and denominator by 25 then again by their G.C.D.
- 2.31/12 = 2.58333... = 2.58 3̄ (the 3 repeats; bar notation).

### Examples
**Example: Power set of X = {1, {2,3}}**
X has 2 elements. P(X) has 2² = 4 elements:
P(X) = {∅, {1}, {{2,3}}, {1, {2,3}}}.

**Example: De Morgan's Laws (statement and proof)**
The two laws (in English):
- The complement of the union of two sets equals the intersection of their complements.
- The complement of the intersection of two sets equals the union of their complements.

In symbols:
1. (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ
2. (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ

**Proof of (i)** — Take an arbitrary x.
x ∈ (A ∩ B)ᶜ
⇔ x ∈ U and x ∉ A ∩ B (definition of complement)
⇔ x ∈ U and (x ∉ A or x ∉ B) (definition of ∩)
⇔ (x ∈ U and x ∉ A) or (x ∈ U and x ∉ B)
⇔ (x ∈ Aᶜ) or (x ∈ Bᶜ)
⇔ x ∈ Aᶜ ∪ Bᶜ. ∎

**Proof of (ii)** — analogous, starting with x ∈ (A ∪ B)ᶜ ⇔ x ∈ U and x ∉ A ∪ B ⇔ x ∉ A and x ∉ B ⇔ x ∈ Aᶜ ∩ Bᶜ.

### ⚠️ Common Mistakes
- ❌ Treating "the most talented students" as a set → ✅ Not a set (ill-defined membership)
- ❌ Counting U and ∅ when asked for proper non-empty subsets → ✅ Exclude both (62, not 64)

> **Quick Recall:**
> - A collection is a set only if membership is unambiguously defined.
> - |P(X)| = 2ⁿ where n = |X|.
> - De Morgan: complement of union = intersection of complements; complement of intersection = union of complements.
> - A set equality proof goes both ways via arbitrary element argument.

### Connections
- Builds on: set definitions and operations (Chunks 001-004)
- Prerequisite for: indicator/characteristic function arguments later, and for Boolean reasoning in Unit 2 Appendix.

---

## Section: Unit 2 — Structure, Objectives, Introduction 🟢

### Core Idea
Unit 2 (Overview of Basic Methods of Mathematics) lays out the toolkit for solving equations: clarifying the meaning of symbol, parameter, variable, constant; defining mathematical expression, equation, identity, polynomial; algebra of polynomials; and methods for linear (one/two/multi-variable) and quadratic equations. An appendix covers proof techniques.

> **In Simple Terms:** Unit 2 is the "how to do algebra cleanly" unit — it nails down what each symbol on the page actually means, then gives standard recipes for solving the basic equation types.

### Definitions
- **Unit Objectives** (after this unit, the learner can):
  - Explain symbol, parameter, variable, constant.
  - Distinguish among them.
  - Explain mathematical expression / formula / well-formed-formula, equation, solution/root of equation, zero of function, polynomial identity, polynomials, polynomial equations.
  - Use polynomial identities to solve problems.
  - Apply algebraic operations (add, subtract, multiply) to polynomials.
  - Solve linear equations (1 var, 2 var, system) and quadratic equations.

### Edge Cases & Caveats
- Fisher equation appears as motivating example: real interest rate ≈ nominal interest rate − inflation rate (≈ ≡ "approximately equal to").

### Connections
- Builds on: number systems, decimal representation (Unit 1)
- Continues into: Polynomials (Section 2.2.3), Solving Equations (Section 2.3)

---

## Section: Symbol, Parameter, Variable, Constant (2.2.1) 🔴

### Core Idea
A *symbol* is any notation that stands for something else. Constants, variables, and parameters are all kinds of symbols, distinguished by what kind of value they may take and the role they play in an equation.

> **In Simple Terms:** The word "lake" is a symbol — touching it doesn't get your finger wet. In math, x, c, 6 etc. are symbols too; what differs is whether the value is fixed (constant), free to vary (variable), or fixed-for-now-but-generic (parameter).

### Key Concepts

#### Symbol
A notation that represents something else. Touching the four-letter word *lake* does not get the finger wet, but touching the actual lake does. To talk about the word itself, write it as 'lake', "lake", or *lake*.

#### Parameter
A "hybrid of constant and variable" — a symbol that is held constant for the purpose of one analysis but can be set to different values to generate a family of problems.
- Example: in x² + y² = c (with real c > 0), c parameterises a family of circles of radius √c centred at origin.
- Setting c = 4 yields the circle x² + y² = 4 (radius 2); c = 15 yields radius √15.
- Significance: questions like "rectangle of maximum area inscribed in the circle" can be solved once for general c, then specialised — a parameter is a *generalised constant*.

#### Variable
A symbol which can be measured and which may change.
- Economics examples: price, interest-rate, wages, quantity-bought, quantity-sold.
- Value of variable at a particular time = its measurement at that time (e.g., 6% interest-rate today).
- A variable assumes only its *possible* values — e.g., √(−8) is not a possible value for "percentage-of-Interest-rate" but is a possible value for x in ax² + bx + c = 0.
- Naming convention: end letters x, y, z (and others) of Latin alphabet.

#### Constant
A symbol whose possible value is a unique single value.
- Example: 6 (Latin) and ६ (Devanagari) each have one value.
- Naming convention: beginning letters a, b, c.

| Concept | Number of values | Typical naming | Example |
|---------|-----------------|---------------|---------|
| Constant | exactly one | a, b, c, ... | 6, ६, π |
| Variable | many possible | x, y, z, ... | price, x in ax²+bx+c=0 |
| Parameter | one *per analysis*, varies between analyses | (context-dependent) | c in x² + y² = c |
| Symbol | (umbrella concept) | any notation | 'lake', x, 6 |

### ⚠️ Common Mistakes
- ❌ Treating a parameter as a "variable" inside its own analysis → ✅ It is locally constant; it generalises only across analyses.
- ❌ Plugging an inadmissible value (e.g. negative for a percentage) → ✅ A variable can only assume its possible values.

### Connections
- Builds on: Set theory (Unit 1) — variable values come from a set of admissible values.
- Continues into: 2.2.2 Mathematical Expressions

---

## Section: Algebraic Concepts and Mathematical Expressions (2.2.2) 🔴

### Core Idea
A *mathematical expression* is a syntactically correct sequence of mathematical terms (constants, variables, parameters, relations, operations) built using the structuring rules of mathematics — analogous to a grammatical sentence in a natural language. Expressions are classified into arithmetic, polynomial, algebraic, and general; an *equation* is a mathematical expression containing exactly one '=' (and no other relations).

> **In Simple Terms:** Math has grammar too. Just like "the cat sat on mat" is grammatical English but "mat sat the on cat" is not, √(8 − y) is a valid expression but "−8√" or "y| |" is not.

### Key Concepts

#### Expression (general)
Whatever is constructed according to a language's structuring rules (its syntax/grammar) is an expression in that language.

#### Mathematical Expression — Construction Rules
1. **Atomic:** Each constant, variable, parameter is itself an ME. So 7, x, c, 14.78 are MEs.
2. **Unary operators** must be in correct position with one operand (constant/variable/parameter/ME containing no relational operator). Valid: √(8−y), (x+y)², eˣ⁺²ʸ⁻⁴ᶻ, log(3x+5), |y+56|. Invalid: −8√, x log, ᵉe, y| | (operator misplaced); √(8 < y), (36x = 49)² (operand contains relational operator).
3. **Binary operators** require two operands at correct positions. Valid: (√867 − eˣ⁺²ʸ), (x + 2y − 4z), (√(8−y) × (x+y)² + log(x − eʸ)). Invalid if any operand contains a relational operator or invalid sub-expression.
4. **Binary relations** require two operands that are themselves expressions without internal relations. So (√867 − eˣ⁺²ʸ) < (√(8−y) × (x+y)² + log(x − eʸ)) is valid, but (√867 = eˣ⁺²ʸ) < ((8−y)×(x+y) > log(x−eʸ)) is NOT (RHS contains '>').
   - Shorthand chain: x < y < z means "x < y and y < z" (similarly for ≤, >, etc.).
5. **Other expressions:** limits limₙ→∞(1+1/n)ⁿ, derivatives dy/dx, integrals ∫f(3x+2)dx — discussed in later units.

#### Classification of Mathematical Expressions
Each preceding type is a special case of the next.

| Type | Restriction | Example |
|------|-------------|---------|
| **Arithmetic** | No variables | (√(−8 + 489) × (7! + 56)² + log(155 − e⁹)) |
| **Polynomial** | Variables only with non-negative integer powers | 7x³ − 5x + 11; (x+y)² |
| **Algebraic** | Variables with rational powers p/q (q ≠ 0, p,q integers) | √(8−y); √(1+x²)/√(1−x²) |
| **General** | Anything constructible by syntax rules | log x, eˣ, dy/dx, ∫ |

Notes:
- Constants in a polynomial may have fractional powers (e.g., x² + (17)¹ᐟ² is polynomial because the variable x has integer power; 17 is a constant).
- √(8−y) = (8−y)¹ᐟ² is algebraic, NOT polynomial.

#### General Forms — Equation
An equation is a special expression with exactly one '=' relation and no other relation. Polynomial equation: both sides are polynomial expressions. Algebraic equation: both sides algebraic.
- Beyond algebraic: equations involving log, e, trigonometric functions; set-theoretic equations (e.g. (X ∩ Y)ᶜ = Xᶜ ∪ Yᶜ — actually an *identity*); logical equations; differential and integral equations.
- General form: any equation may be rewritten as f(x) = 0 (move RHS to LHS).

#### Root / Solution / Zero
- A *root/solution* of f(x) = 0 is a constant a such that f(a) = 0.
- Example: f(x) = x² − 4 = 0; f(2) = 4 − 4 = 0, so x = 2 is a root.
- We also say "2 is a *zero* of the function f(x)". The word "zero" applies to the **function** f, not the equation f(x) = 0.

#### Mathematical Identity vs Equation
| | Equation | Identity |
|---|---|---|
| Holds for | specific value(s) of variable | every value of the variable |
| Example | X² − 16 = 0 (only X = ±4) | X² − 16 = (X+4)(X−4) (every X, real or complex) |
| Symbol | = | ≡ (when emphasis needed) |

Test: with X = 3: LHS of identity = 9 − 16 = −7; RHS = (3+4)(3−4) = −7. ✓

#### Various Usages of '=' in Mathematics
| Usage | Example | More-specific symbol |
|-------|---------|----------------------|
| In equations | find x: x² + 4x + 3 = 0 | = |
| In identities/laws | (a+b)² = a² + b² + 2ab for all real a,b | ≡ |
| In conditional statements | "If x = 7, then ..." | = |
| In relations (T/F evaluations) | 3 = 4+2 (false), 3 = 2+1 (true) | = |
| In assignments | "Let x = 8" | := (Pascal-style) |
| In definitions | Area = length × breadth | ≜ (or ≡) |

### Examples
**Example: Expression vs Non-expression**
- |y + 56| is an ME (unary | | with single operand y+56).
- √(8 − y) × is NOT an ME (binary × missing right operand).
- log((8 < y) × (x+y)²) is NOT an ME (operand contains '<').

### Definitions
- **Mathematical Expression**: a sequence of mathematical terms (constants, variables, parameters, relations, operations) formed by the structuring rules of mathematics. ⭐
- **Arithmetic Expression**: ME with no variables.
- **Polynomial Expression**: ME whose variables appear only with non-negative integer powers. ⭐
- **Algebraic Expression**: ME whose variables appear with rational powers p/q (p,q integers, q ≠ 0).
- **Equation**: ME with exactly one '=' and no other relations.
- **Identity**: equation true for every value of the variable. ⭐
- **Root/Solution** of f(x) = 0: a constant a with f(a) = 0.
- **Zero** of f(x): same value a, but spoken *of the function*.

### ⚠️ Common Mistakes
- ❌ Saying "2 is a zero of the equation" → ✅ 2 is a *zero of the function* / *root of the equation*.
- ❌ Confusing identity and equation → ✅ Identity holds for all values; equation only for solutions.
- ❌ Treating √(8−y) as polynomial → ✅ It is algebraic (rational power 1/2), not polynomial.
- ❌ Writing log x as polynomial → ✅ log is not allowed in polynomials.

### Edge Cases & Caveats
- Parentheses must be paired. An expression like "log (x+y)²" with mismatched parentheses is not an ME.
- Relational operators inside operands of operators or other relations are forbidden.

> **Quick Recall:**
> - Expression ⊃ Algebraic ⊃ Polynomial ⊃ Arithmetic.
> - Polynomial: only non-negative integer powers of variables.
> - Equation: exactly one '='; identity: equation true for all values.
> - Zero of function f = root of equation f(x)=0.

### Connections
- Builds on: numbers, exponents (Unit 1)
- Continues into: 2.2.3 Polynomials (Chunk 006: Polynomials and Polynomial Equations (2.2.3))

---

## Section: Mathematical Identity (2.2.2.5) and Usages of '=' (2.2.2.6) — Check Your Progress 1 🟡

### Examples (CYP 1 — page reference for solutions)
**Q (Chunk 005, p. 49):** Which of the following is not a mathematical expression? Justify.
(i) √|y + 56|, (ii) √(8−y) ×, (iii) log((8 < y) × (x+y)²), (iv) log(x+y)², (v) log(x+y)²

(Answers appear in Chunk 006 / Unit 2 answer key:)
- (i) and (iv) are MEs.
- (ii) is NOT an ME — multiplication symbol '×' must be followed by an expression.
- (iii) is NOT an ME — argument contains relational operator '<'.
- (v) is NOT an ME — has two left parentheses but only one right; an ME must have matching parentheses.

### Connections
- Continues into: Chunk 006 (CYP 1 answers reside in 2.6 of Unit 2)


---


## Section: Polynomials and Polynomial Equations (2.2.3) 🔴
<!-- Continues from: Mathematical Expressions (Chunk 005: Unit 1 — Answers/Hints to Check Your Progress Exercises) -->

### Core Idea
A polynomial expression involves variables only with non-negative integer powers. A polynomial equation has exactly one '=' with polynomial expressions on both sides. These notes formalise terms, factors, coefficients, monomials, the *degree* of a term/polynomial/equation, and how to evaluate a polynomial for given variable values.

> **In Simple Terms:** Polynomials are the well-behaved expressions where every variable appears as x, x², x³ etc. — no roots, no logs, no division by variables. The "degree" tells you the polynomial's highest power.

### Key Concepts

#### Term
Each component separated by '+' or '−' is a term.
- x³ + 8x − 4 has three terms: x³, 8x, −4.
- (x − y)² at the highest level has only one term; on expansion x² + y² − 2xy has 3 terms.
- In x³y + 8x − 4y², the powers are: x: 3 in x³y, 1 in 8x, 0 in −4y²; y: 1, 0, 2 respectively.
- A *term* contains no '+' or '−' at the top level; uses only ×/exponentiation in polynomial terms (no division by variable). (45x²)/(78y) is an algebraic term but not a polynomial term.

#### Factor & Coefficient
For (45 x³ y³): factors include 3, 5, 9, 45, x, x², y, y², and any products of these. The constant factor 45 is the **coefficient** of the term.
- Coefficient of 17xy is 17; coefficient of −25x is −25.

#### Monomial / Binomial / Trinomial / Polynomial
| Name | Number of terms | Example |
|------|----------------|---------|
| Monomial | 1 | 45x²y³ |
| Binomial | 2 | 45x²y³ − 25; a + b |
| Trinomial | 3 | 45x²y³ − 25x⁴ + 71y⁵; a + b − 72 |
| Polynomial (general) | one or more terms (each with non-zero coefficient, variables with non-negative integer exponents) | 45x⁵ − 25x⁴ + 91x − 36 |

A polynomial may involve one variable, two variables (e.g. 45x²y³ + y⁵ − 25), or more (e.g. x + 3y + z + 2u + v).

#### General Form of a Polynomial Equation
For practical purposes, any polynomial equation containing at least one variable can be written by appending "= 0" to a polynomial expression. Example: 45x²y³ + 71y⁵ − 25x⁴ = 0.

#### Degree
- **Degree of a term** = sum of powers of all variables in that term.
  - deg(45x²y³) = 2 + 3 = 5.
  - deg(345) = 0 (constant; can be regarded as 345·x⁰ since x⁰ = 1 for any non-zero x).
- **Degree of a polynomial** = max degree among its terms.
  - For 45x²y³ + 71y⁵ − 25x⁴: degree = 5.
- **Degree of a polynomial equation** = max degree among terms on both sides.
  - For 71y³ + 45x²·z·y³ + 2xy = −25x³: degree = 7 (the 45x²zy³ term contributes 2+1+3 = 6... [the textbook gives 7; OCR ambiguity, but the principle is "max term degree"]).
- Convention: a polynomial is generally written in *order of decreasing degree of its terms*.

#### Naming a Polynomial
A polynomial in two variables x and y can be named, e.g., P(x, y) = 45x²y³ + 71y⁵ − 25x⁴ + 76.

#### Evaluating a Polynomial
Substitute the given (constant) values for the variables.
- For P(x, y) = 4x³ − 7xy² + 11:
  - P(2, −1) = 4(2)³ − 7(2)(−1)² + 11 = 32 − 14 + 11 = 29 [textbook OCR shows "16 − 14 + 11 = 13"; treating the original published value as printed]. Note: the textbook prints 4(2)³ = 16 which appears as an OCR/text artefact; the **method** is what matters.
  - P(−1, 2) = 4(−1)³ − 7(−1)(2)² + 11 = −4 + 28 + 11 = 35 [textbook shows 43 — OCR mismatch in printed source].

#### Solution of a Polynomial Equation (multi-variable)
For polynomials P(x, y) = Q(x, y), constants a (for x) and b (for y) are a *solution* if P(a, b) = Q(a, b).

### ⚠️ Common Mistakes
- ❌ Calling (45x²)/(78y) a polynomial term → ✅ It is algebraic, not polynomial (variable in denominator).
- ❌ Forgetting that the constant term has degree 0 → ✅ 345 = 345·x⁰, so deg = 0.
- ❌ Saying √x or x⁻¹ are allowed in polynomials → ✅ Only non-negative integer powers of variables.

> **Quick Recall:**
> - Polynomial: variables to non-negative integer powers only.
> - Degree of term = sum of exponents; degree of polynomial = max term degree.
> - Standard form: write in decreasing degree.

### Connections
- Builds on: classification of mathematical expressions (Chunk 005: Unit 1 — Answers/Hints to Check Your Progress Exercises)
- Continues into: 2.2.4 Polynomial Identities

---

## Section: Polynomial Identities (2.2.4) 🔴

### Core Idea
Polynomial identities are polynomial equations true for *every* value of the variables. A small toolbox of standard identities (expansion of (x+y)², (x+y)³ etc., factorisation of x²−y², x³+y³+z³−3xyz, etc.) lets you factor and simplify many expressions without expanding from scratch.

> **In Simple Terms:** These are the algebraic "shortcuts" — memorise them once and you can factor 105×95 in your head, or factorise (625/16)x⁴ − (9/49)y² in two lines.

### Key Concepts

#### Standard Polynomial Identities
1. (x + y)² = x² + y² + 2xy
2. (x − y)² = x² + y² − 2xy
3. x² − y² = (x + y)(x − y)
4. (x + a)(x + b) = x² + (a + b)x + ab
5. (x + y + z)² = x² + y² + z² + 2xy + 2xz + 2yz
6. (x − y − z)² = x² + y² + z² − 2xy − 2xz + 2yz   [from (5) by y → −y, z → −z]
7. (x + y)³ = x³ + y³ + 3xy(x + y)
8. (x − y)³ = x³ − y³ − 3xy(x − y)
9. x³ + y³ + z³ − 3xyz = (x + y + z)(x² + y² + z² − xy − yz − zx)

### Examples
**Example: Evaluate 105 × 95 without direct multiplication**
105 × 95 = (100 + 5)(100 − 5) = 100² − 5² (using identity 3)
= 10000 − 25 = 9975. ✓

**Example: Factorise (625/16)x⁴ − (9/49)y²**
- 625/16 = (25/4)² and 9/49 = (3/7)².
- (625/16)x⁴ − (9/49)y² = [(25/4)x²]² − [(3/7)y]²
- = [(25/4)x² + (3/7)y] · [(25/4)x² − (3/7)y]   (using identity 3)

**CYP 2 Q1 — Expand (2a − 4b − 5c)²** (answer in Section 2.6, see chunk 007):
= (2a)² + (−4b)² + (−5c)² + 2(2a)(−4b) + 2(2a)(−5c) + 2(−4b)(−5c)
= 4a² + 16b² + 25c² − 16ab − 20ac + 40bc.

### ⚠️ Common Mistakes
- ❌ Sign errors when applying (x − y)² → ✅ Note middle term is −2xy.
- ❌ Forgetting the all-cross-products in (x+y+z)² → ✅ Six terms total: x²+y²+z² + 2(xy+xz+yz).

> **Quick Recall:**
> - x² − y² = (x+y)(x−y) — most reused identity.
> - (a+b+c)² = a² + b² + c² + 2(ab+bc+ca).
> - x³ + y³ + z³ − 3xyz factors via (x+y+z)(x²+y²+z²−xy−yz−zx).

### Connections
- Builds on: 2.2.3 polynomials.
- Continues into: 2.2.5 Algebra of Polynomials

---

## Section: Algebra of Polynomials (2.2.5) 🔴

### Core Idea
Polynomials are added/subtracted by combining *like terms* (terms identical except for their constant coefficients), and multiplied by distributing every term of one over every term of the other and collecting like terms. Sums/differences don't create new term types; products generally do.

> **In Simple Terms:** "3 cows + 4 cows = 7 cows" but "3 cows + 4 horses" stays as is. In math, 3x³ + 4x³ = 7x³, but 3x + 4x³ stays as 3x + 4x³ (or factors as x(3 + 4x²)).

### Key Concepts

#### Like Terms vs Unlike Terms
- **Like terms**: identical except for their constant parts.
  - 17x²y³ and −39x²y³ are like terms; sum simplifies to (17 − 39)x²y³ = −22x²y³.
- **Unlike terms**: differ in at least one variable's exponent.
  - 17x²y³ and −39x³y² are unlike (cannot be combined as a single term). Sum 17x²y³ + (−39x³y²) may be partially factored as x²y²(17y − 39x).

#### Sum / Difference of Two Polynomials
Process: collect like terms, add/subtract their coefficients.
- For subtraction P − Q, first form R from Q by flipping every '+' to '−' and '−' to '+' (i.e., R = −Q), then compute P + R.

### Examples
**Example: Sum**
P(x,y) = 3x² − 5xy + 3x + 8;  Q(x,y) = 6y² + 12xy − 5x + 16
P + Q = 3x² + (−5+12)xy + (3−5)x + (8+16) + 6y²
     = 3x² + 7xy + 6y² − 2x + 24.

**Example: Difference**
For same P, Q: form R = −6y² − 12xy + 5x − 16.
P − Q = P + R; collect like terms.

#### Product of Two Polynomials
- Simple case: one factor is a constant. Multiply each term by the constant.
  - P(x,y) = 3x² − 5xy + 3x + 8; Q = 7. P × Q = 21x² − 35xy + 21x + 56.
- General: if P = T₁ + T₂ + ... + Tₘ and Q = S₁ + S₂ + ... + Sₙ, then
  P × Q = Σᵢⱼ TᵢSⱼ over i = 1..m, j = 1..n.
- **Term-product rule:** multiply the constants and *add* the powers of each variable that appears.
  - T = 5x²y³, S = −16xyz⁵ ⟹ T × S = (5)(−16)·x²⁺¹·y³⁺¹·z⁰⁺⁵ = −80 x³y⁴z⁵.

**Example: Product**
P(x,y) = 4x − 3y + 5; Q(x,y) = 2x − 7.
(4x − 3y + 5)(2x − 7)
= 4x(2x − 7) − 3y(2x − 7) + 5(2x − 7)
= [8x² − 28x] + [−6xy + 21y] + [10x − 35]
= 8x² − 18x − 6xy + 21y − 35.

### CYP 3 Q1
For P(x, y) = 4x² − 3xy + 5y, Q(x, y) = −4x² − 3xy + 5y²:
- (i) Sum P + Q = (4x² − 4x²) + (−3xy − 3xy) + (5y + 5y²) = −6xy + 5y + 5y² = −6xy + 5y(1 + y) = y[−6x + 5(1+y)]
- (ii) Difference P − Q = [4x² − 3xy + 5y] + [4x² + 3xy − 5y²] = 8x² + 5y − 5y² = 8x² + 5y(1 − y).

### ⚠️ Common Mistakes
- ❌ Combining 17x²y³ with −39x³y² (unlike) → ✅ Cannot simplify as single term.
- ❌ Multiplying powers instead of adding when doing term × term → ✅ Add the exponents of each variable.

> **Quick Recall:**
> - Add/subtract: collect like terms.
> - Multiply terms: multiply coefficients, **add** exponents per variable.
> - Multiply polynomials: distribute every term against every term, then collect.

### Connections
- Continues into: 2.3 Solving polynomial equations.

---

## Section: Solving Polynomial Equations — Linear (2.3, 2.3.1, 2.3.2) 🔴

### Core Idea
Of all polynomial equations, the course focuses on four solvable types: (i) single linear in one variable, (ii) single linear in two variables, (iii) systems of linear equations, (iv) quadratic in one variable. A linear equation has every variable-bearing term of degree 1.

> **In Simple Terms:** Linear means "straight-line": every variable shows up at most to the first power, and there are no products of variables, no logs, no exponentials.

### Definitions
- **Linear equation** in one/two/more variables: every variable-bearing term has degree 1. ⭐
  - 3 − 29x = 5x + 17 (linear in 1 var)
  - 7y − 29x = 5x + 17 (linear in 2 vars)
  - x + 2z − 7y = 17 (linear in 3 vars)
- **NOT linear:**
  - 3 − 29x² = 5x + 17 (degree 2)
  - 45 = 27 + 18 (no variable)
  - xy = x + 55 (product of variables)
  - log x + 17 = 0; eˣ = x + 25 (transcendental functions, not even polynomial)
- **System of linear equations**: two or more linear equations in two or more variables; a solution is a tuple satisfying all equations simultaneously. ⭐
- **Quadratic equation in one variable y**: at least one term has y² (with non-zero coefficient); other terms are constants or constant multiples of y. General form: ay² + by + c = 0, a ≠ 0.

### 2.3.1 Solving Linear Equations in One Variable
General form: ax + b = cx + d, with a ≠ c (else the equation reduces to b = d, no variable).

**Rules:**
1. Move all variable terms to one side (typically LHS), all constants to the other (RHS).
2. When a term switches sides, its sign flips (+ ↔ −).

**Example: Solve 2x + 5 = 4 − 3x**
2x + 3x = 4 − 5
5x = −1
x = −1/5.

#### Reducing non-linear to linear (with caveat)
**Example:** (3x + 2)/(2x − 1) = 2  ... (i)
- (i) is NOT defined at x = 1/2.
- Cross-multiply: 3x + 2 = 2(2x − 1) ... (ii)
- (ii) IS defined at x = 1/2; (i) and (ii) are equivalent **except** at x = 1/2.
- Solve (ii): 3x − 4x = −2 − 2 = −4 ⟹ −x = −4 ⟹ x = 4.
- Since 4 ≠ 1/2, x = 4 is also a solution of (i). ✓

### 2.3.2 Single Linear Equation in Two Variables
General form: Ax + By + C = Dx + Ey + F. Rewrite as (A − D)x + (B − E)y + (C − F) = 0, then in the form ax + by = c.

**Cases:**
| Case | Condition | Result |
|------|-----------|--------|
| (a) | a = 0, b = 0 | reduces to c = 0; not linear; may be false |
| (b) | a = 0, b ≠ 0 | by = c — linear in one variable |
| (c) | a ≠ 0, b = 0 | ax = c — linear in one variable |
| main | a ≠ 0, b ≠ 0 | y = (−ax + c)/b; **infinitely many** (x, y) solutions |

**Example: Solve 3x − 2y + 4 = 4x + 3y − 5**
−2y − 3y = 4x − 3x − 5 − 4
−5y = x − 9
y = (9 − x)/5
Infinitely many solutions: (1, 8/5), (2, 7/5), (3, 6/5), (4, 1), ...

### Connections
- Continues into: 2.3.3 Systems of equations; 2.3.4 Quadratics

---

## Section: 2.3.3 System of Two Linear Equations in Two Variables 🔴

### Core Idea
For a 2×2 linear system ax + by = c, dx + ey = f, one of the standard methods is the *elimination* technique: scale equations to make one variable's coefficients match (or be opposites), then add/subtract to eliminate that variable. (General m×n systems are deferred to the matrices/determinants units.)

> **In Simple Terms:** Make the x-coefficients (or y-coefficients) cancel, solve for the other variable, then back-substitute.

### Mechanisms / Processes
1. Multiply (i) by d (the coefficient of x in (ii)), and (ii) by (−a) (or by a and subtract).
2. Add corresponding terms → equation in y only.
3. Solve for y.
4. Substitute y back into either original equation to get x.

### Examples
**Example: Solve 3x − 5y = −9 ...(iii); 2x + 3y = 13 ...(iv)**
- Multiply (iii) by 2: 6x − 10y = −18  ...(iii′)
- Multiply (iv) by 3: 6x + 9y = 39    ...(iv′)
- (iii′) − (iv′): −10y − 9y = −18 − 39 ⟹ −19y = −57 ⟹ y = 3.
- Substitute y = 3 in (iii): 3x − 5(3) = −9 ⟹ 3x = 6 ⟹ x = 2.
- Unique solution: (x, y) = (2, 3). ✓

### Connections
- Continues into: 2.3.4 Quadratic equations; matrices/determinants in later units.

---

## Section: 2.3.4 Quadratic Equations 🔴

### Core Idea
The general quadratic is ax² + bx + c = 0 with a ≠ 0. Its two roots (not necessarily distinct) are given by the quadratic formula. The discriminant b² − 4ac determines whether the roots are real-equal, real-distinct, or complex conjugates.

> **In Simple Terms:** One formula handles every quadratic; the sign of b² − 4ac tells you the kind of answer to expect.

### Key Concepts

#### Quadratic Formula
i)  x = [−b + √(b² − 4ac)] / (2a)
ii) x = [−b − √(b² − 4ac)] / (2a)

If b² − 4ac = 0, the two roots coincide.

(Continues into Chunk 007, where the three discriminant cases are illustrated with worked examples.)

### Connections
- Continues into: Chunk 007 (discriminant cases, worked examples)
- Builds on: linear equations (2.3.1, 2.3.2, 2.3.3)


---


## Section: Quadratic Equation — Three Discriminant Cases (continued from 2.3.4) 🔴
<!-- Continues from: 2.3.4 Quadratic Equations (Chunk 006: Polynomials and Polynomial Equations (2.2.3)) -->

### Core Idea
For ax² + bx + c = 0 (a ≠ 0), the *discriminant* D = b² − 4ac classifies the roots into three regimes: D = 0 ⟹ two coincident real roots; D > 0 ⟹ two distinct real roots; D < 0 ⟹ two complex conjugate roots.

> **In Simple Terms:** Just check the sign (and zero-ness) of b² − 4ac and you instantly know whether you'll get one repeated answer, two real answers, or a pair of complex answers.

### Key Concepts

| Discriminant | Nature of roots | Roots |
|--------------|----------------|-------|
| b² − 4ac = 0 | two identical real roots | x = −b/(2a) (double) |
| b² − 4ac > 0 | two distinct real roots | x = [−b ± √(b² − 4ac)]/(2a) |
| b² − 4ac < 0 | two distinct complex roots | x = [−b ± i√(4ac − b²)]/(2a) |

### Examples
**Case (i) — D = 0: x² − 4x + 4 = 0**
a = 1, b = −4, c = 4 ⟹ D = 16 − 16 = 0.
Root = [−(−4) + 0]/2 = 4/2 = 2 (double root). Both roots are x = 2.

**Case (ii) — D > 0: x² − 6x + 4 = 0**
a = 1, b = −6, c = 4 ⟹ D = 36 − 16 = 20.
Roots = [6 ± √20]/2 = [6 ± 2√5]/2 = 3 ± √5.
Two real distinct roots: x = 3 + √5 and x = 3 − √5.

**Case (iii) — D < 0: x² − 2x + 4 = 0**
a = 1, b = −2, c = 4 ⟹ D = 4 − 16 = −12.
Roots = [2 ± √(−12)]/2 = [2 ± 2i√3]/2 = 1 ± i√3.
Two complex roots: x = 1 + i√3 and x = 1 − i√3.

### ⚠️ Common Mistakes
- ❌ Forgetting the ± when extracting square root → ✅ Quadratic always yields two roots (counting multiplicity).
- ❌ Treating D = 0 as "no solution" → ✅ It means a *single repeated* real solution.

> **Quick Recall:**
> - D = b² − 4ac (discriminant).
> - D > 0 real distinct; D = 0 real coincident; D < 0 complex.
> - Complex roots of a real-coefficient quadratic always come as conjugate pair.

### Connections
- Builds on: 2.3.4 (Chunk 006: Polynomials and Polynomial Equations (2.2.3)). Builds toward complex numbers (Unit 1, Chunks 001-004).

---

## Section: Check Your Progress 4 (Word problems & Quadratics) 🟡

### Examples
**CYP 4 Q1: Arjun is twice as old as Rahim. Five years ago, Arjun's age was three times Rahim's age. Find their present ages.**
Let Rahim's current age = x; Arjun's = 2x.
Five years ago: Rahim = x − 5; Arjun = 2x − 5.
Given: 2x − 5 = 3(x − 5) = 3x − 15
⟹ 2x − 3x = −15 + 5 = −10 ⟹ −x = −10 ⟹ x = 10.
**Rahim = 10 yrs, Arjun = 20 yrs.**

**CYP 4 Q4: Solve each quadratic.**
General form: ax² + bx + c = 0; roots = [−b ± √(b² − 4ac)]/(2a).

(i) x² + 6x + 9 = 0: a = 1, b = 6, c = 9; D = 36 − 36 = 0.
   Roots: x = −6/2 = **−3** (double).

(ii) x² + 6x + 3 = 0: a = 1, b = 6, c = 3; D = 36 − 12 = 24 > 0.
   Roots: x = [−6 ± √24]/2 = −3 ± √6.

(iii) x² + 6x + 12 = 0: a = 1, b = 6, c = 12; D = 36 − 48 = −12 < 0.
   Roots: x = [−6 ± √(−12)]/2 = −3 ± i√3.

### Connections
- Builds on: 2.3.4 quadratics; word-problem translation builds on 2.3.1.

---

## Section: 2.4 Let Us Sum Up & 2.5 Key Words 🟢

### Core Idea
Unit 2 explained: (a) symbol/parameter/variable/constant; (b) mathematical expression/formula, equation, solution/root, zero of function, polynomial identity, polynomials and polynomial equations; (c) algebra of polynomials and use of polynomial identities; (d) solution methods for linear (one var, two var, system), and quadratic equations.

### Definitions (Key Words)
- **Linguistic Expression**: a structure or sequence of characters constructed according to a language's structuring rules (its syntax/grammar).
- **Mathematical Expression** (also called *formula*): a sequence of mathematical terms (constants, variables, parameters, relations, operations) formed by the structuring rules of mathematics. ⭐
- **Symbol**: a notation that represents, or stands for, something else (e.g. *lake* stands for the water-body — touching the word doesn't get the finger wet).
- **Variable**: a symbol which can be measured and which may change (e.g. price, interest-rate, wages, quantity-bought, quantity-sold). ⭐

### Connections
- Recapitulates Sections 2.2.1–2.3.4 (Chunks 005, 006, 007).

---

## Section: 2.6 Answers/Hints to Check Your Progress Exercises 🟡

### Examples

**CYP 1 (page 49) — Which is not a Mathematical Expression?**
- (i) √|y + 56| — IS an ME.
- (ii) √(8 − y) × — NOT an ME (multiplication symbol must be followed by an expression).
- (iii) log((8 < y) × (x+y)²) — NOT an ME (argument of × contains relational operator '<').
- (iv) log(x + y)² — IS an ME.
- (v) log((x + y)² — NOT an ME (mismatched parentheses: two left, one right).

**CYP 2 (Polynomial Identities)**
1) (2a − 4b − 5c)² = (2a)² + (−4b)² + (−5c)² + 2(2a)(−4b) + 2(2a)(−5c) + 2(−4b)(−5c)
   = 4a² + 16b² + 25c² − 16ab − 20ac + 40bc.

2) Factorise (625/16)x⁴ − (9/49)y⁴
   - 625/16 = (25/4)², 9/49 = (3/7)². So:
   - (625/16)x⁴ − (9/49)y⁴ = [(25/4)x² + (3/7)y²][(25/4)x² − (3/7)y²]   ...(i)
   - Further factor [(25/4)x² − (3/7)y²] = [(5/2)x + √(3/7)·y][(5/2)x − √(3/7)·y]   ...(ii)
   - Substituting (ii) into (i):
     (625/16)x⁴ − (9/49)y⁴ = [(25/4)x² + (3/7)y²]·[(5/2)x + √(3/7)·y]·[(5/2)x − √(3/7)·y].

3) Factorise x² + 4y² + z² − 4xy − 4yz + 2xz.
   = (x)² + (−2y)² + (z)² + 2(x)(−2y) + 2(−2y)(z) + 2(x)(z)
   = (x − 2y + z)² = (x − 2y + z)(x − 2y + z).

**CYP 3 (Algebra of Polynomials)**
1) For P(x, y) = 4x² − 3xy + 5y, Q(x, y) = −4x² − 3xy + 5y²:
   - (i) P + Q = (4x² − 4x²) + (−3xy − 3xy) + (5y + 5y²) = −6xy + 5y + 5y² = −6xy + 5y(1 + y) = y[−6x + 5(1 + y)].
   - (ii) P − Q = [4x² − 3xy + 5y] + [4x² + 3xy − 5y²] = 8x² + 5y − 5y² = 8x² + 5y(1 − y).

2) (4x² − 3xy + 5y) × (2x² − 7y)
   = 4x²(2x² − 7y) − 3xy(2x² − 7y) + 5y(2x² − 7y)
   = (8x⁴ − 28x²y) + (−6x³y + 21xy²) + (10x²y − 35y²)
   = 8x⁴ − 28x²y − 6x³y + 21xy² + 10x²y − 35y²
   = 8x⁴ − 6x³y − 18x²y + 21xy² − 35y².

**CYP 4 — additional answers**

Q2: (2x + 5)/(3x + 7) = 11/16, except x = −7/3.
Equivalent linear: 16(2x + 5) = 11(3x + 7) ⟹ 32x + 80 = 33x + 77 ⟹ −x = −3 ⟹ **x = 3**. (3 ≠ −7/3, so it solves the original too.)

Q3: (3x + 4y + 1)/(2x + 3y) = 8/5, except 2x + 3y = 0 (i.e., x = −3y/2).
Equivalent linear: 5(3x + 4y + 1) = 8(2x + 3y) ⟹ 15x + 20y + 5 = 16x + 24y
⟹ 4y = x − 5 ⟹ **y = (x − 5)/4** [textbook form: y = (x + 5)/4 — note OCR ambiguity in sign; reproduced here as printed but the algebraic step yields x − 5, not x + 5].
Infinitely many solutions; reject any (x, y) with 2x + 3y = 0.

Q4: see CYP 4 in section above (quadratics).

### Connections
- Builds on: CYP exercises across Chunks 005-006-007.

---

## Section: 2.7 Exercises (End-of-unit) 🟡

### Examples

**Q1. Factorise x² + 4y² + z² − 4xy − 4yz + 2xz.**
Recognise as (a + b + c)² with a = x, b = −2y, c = z:
= (x − 2y + z)² = (x − 2y + z)(x − 2y + z).

**Q2. Find the product of (8x² − 6xy + 10y) and (4x² − 11y).**
[Note: textbook OCR shows answer for (4x² − 3xy + 5y)(2x² − 7y); reproducing the printed worked solution.]
(4x² − 3xy + 5y)(2x² − 7y)
= 4x²(2x² − 7y) − 3xy(2x² − 7y) + 5y(2x² − 7y)
= (8x⁴ − 28x²y) + (−6x³y + 21xy²) + (10x²y − 35y²)
= 8x⁴ − 28x²y − 6x³y + 21xy² + 10x²y − 35y²
= 8x⁴ − 6x³y − 18x²y + 21xy² − 35y².

**Q3. Two-digit number puzzle.** Digits differ by 4. On interchanging digits, original = 2 × (new) − 1. Find original.
- Original ten's digit > unit's digit (since interchange decreases the number).
- Let unit's digit = x; ten's digit = x + 4.
- Original = 10(x + 4) + x = 11x + 40.
- New = 10x + (x + 4) = 11x + 4.
- Equation: 11x + 40 = 2(11x + 4) − 1 = 22x + 7
- ⟹ −11x = −33 ⟹ **x = 3**.
- Ten's digit = 7. **Original number = 73** (new = 37). ✓

**Q4. Solve the system: 2x + 5y = 16; 3x + 2y = 13.**
- Multiply (i) by 3: 6x + 15y = 48 ...(iii)
- Multiply (ii) by 2: 6x + 4y = 26 ...(iv)
- (iii) − (iv): 11y = 22 ⟹ y = 2.
- From (i): 2x + 10 = 16 ⟹ x = 3.
- **Solution: (x, y) = (3, 2).** ✓

### Connections
- Builds on: 2.2.4 identities, 2.2.5 polynomial multiplication, 2.3.1–2.3.3 linear methods.

---

## Section: Appendix — Proof Techniques (Overview) 🔴

### Core Idea
Although applied quantitative work involves mostly calculation, *proof* is the soul of mathematics. This appendix introduces six standard proof techniques: direct proof (and counter-examples), proof by contradiction (and contrapositive), proof by cases, existence proofs (constructive and non-constructive), mathematical induction, and proof of equivalences.

> **In Simple Terms:** Six standard ways to argue rigorously: go forwards from the assumptions, deny the conclusion and derive a clash, split the problem into cases, build/show existence, climb the natural-number ladder, or prove "if and only if" both ways.

### Key Concepts

#### Structure of Any Proof Problem
A proof has two explicit parts:
1. **Hypotheses** — given facts, axioms, postulates.
2. **Conclusion** — what is to be proved.
Implicitly given: definitions, previously proved theorems, rules of inference, useful techniques.

Example problem template: *Prove that for all integers m and n, if m and n are odd, then m·n is odd.* Hypothesis: m, n integers and odd. Conclusion: m·n is odd.

#### I. Direct Proof
Begin with the hypothesis (assumed true). Apply definitions, prior theorems, and valid inference rules to reach the conclusion.

**Example: m, n odd integers ⟹ m·n is odd.**
By definition of odd: m = 2K₁ + 1, n = 2K₂ + 1 for some integers K₁, K₂.
m·n = (2K₁ + 1)(2K₂ + 1) = 4K₁K₂ + 2K₁ + 2K₂ + 1 = 2(2K₁K₂ + K₁ + K₂) + 1.
The bracketed term is an integer, so m·n has the form 2K + 1 ⟹ m·n is odd. ∎

#### Refutation by Counter-Example
To show a universally-quantified statement is *false*, exhibit one counter-example.

**Example: "For all integers m, n: m, n odd ⟹ m + n odd" is FALSE.**
Take m = 1, n = 3: m + n = 4, which is even. One counter-example refutes the claim. ∎

#### II. Proof by Contradiction (Indirect Proof)
Assume ¬C (negation of conclusion). Together with hypothesis H and accepted facts, derive any contradiction (a statement S ∧ ¬S). Conclude C.

**Example: ∅ ⊆ X for any set X.**
Suppose ¬(∅ ⊆ X), i.e., ∅ ⊄ X. Then ∃ x ∈ ∅ such that x ∉ X. But by definition there is no x ∈ ∅. Contradiction. Hence ∅ ⊆ X. ∎

#### Proof by Contrapositive
A special case of contradiction. To prove H ⟹ C, instead prove ¬C ⟹ ¬H.

**Example: For every n ∈ ℤ, if n² is even then n is even.**
Assume ¬C: n is odd, so n = 2k + 1 for some k ∈ ℤ.
Then n² = (2k + 1)² = 4k² + 4k + 1 = 2(2k² + 2k) + 1 — odd.
So n² is odd, i.e., ¬H. By contrapositive, H ⟹ C. ∎

#### III. Proof by Cases
Partition the possibilities into exhaustive cases; prove the conclusion in each.

**Example: Show there are no integers x, y with x² + 3y² = 8.**
- Case (i): |x| ≥ 3 ⟹ x² ≥ 9 > 8 ⟹ x² + 3y² > 8.
- Case (ii): |y| ≥ 2 ⟹ 3y² ≥ 12 > 8 ⟹ x² + 3y² > 8.
- So |x| ≤ 2 and |y| ≤ 1, i.e., x ∈ {−2, −1, 0, 1, 2}, y ∈ {−1, 0, 1}. Then x² ∈ {0, 1, 4} and 3y² ∈ {0, 3}. Maximum (x² + 3y²) = 7 < 8.
- No solution exists. ∎

#### IV. Existence Proofs
- **Constructive:** Exhibit a specific b such that P(b) is true.
  - *Example:* Any positive integer can be written as a sum of two cubes in two different ways. **1729** = 10³ + 9³ = 12³ + 1³.
- **Non-constructive:** Prove existence without producing the witness explicitly.
  - *Example:* There exist irrationals x, y with xʸ rational.
    - √2 is irrational. Consider (√2)^(√2):
      - **Case (i):** if (√2)^(√2) is rational, take x = y = √2 — done.
      - **Case (ii):** if (√2)^(√2) is irrational, take x = (√2)^(√2), y = √2; then xʸ = ((√2)^(√2))^(√2) = (√2)^2 = 2, rational.
    - Either way, such x, y exist. (We don't compute (√2)^(√2)'s value.)

(V Mathematical Induction and VI Proof of Equivalences continue into Chunk 008.)

### Definitions
- **Hypothesis (H)**: the explicitly given assumptions plus implicit ones.
- **Conclusion (C)**: what is to be proved.
- **Contradiction**: a statement of the form S ∧ ¬S (both S true and S false simultaneously) — unacceptable in mathematics.
- **Counter-example**: a single instance falsifying a universal claim.

### ⚠️ Common Mistakes
- ❌ Confusing contrapositive (¬C ⟹ ¬H) with converse (C ⟹ H).
- ❌ Trying many examples to "prove" a universal claim → ✅ Examples confirm but do not prove.
- ❌ In proof by cases, missing a case → ✅ Cases must be *exhaustive*.

> **Quick Recall:**
> - Direct: H ⟹ C step by step.
> - Contradiction: assume ¬C, derive S ∧ ¬S.
> - Contrapositive: prove ¬C ⟹ ¬H.
> - Counter-example: one suffices to refute a universal claim.
> - Existence: produce a witness (constructive) or argue indirectly.

### Connections
- Continues into: Mathematical Induction & Equivalences (Chunk 008: Appendix V — Proof by Mathematical Induction)
- Used implicitly throughout: De Morgan proofs (Chunk 005: Unit 1 — Answers/Hints to Check Your Progress Exercises), set identities (Unit 1).

### Open Questions
- When does proof by cases scale poorly? (Answer hint: when the case-space is infinite or unstructured — then induction or invariants help.)


---


## Section: Appendix V — Proof by Mathematical Induction 🔴
<!-- Continues from: Appendix Proof Techniques I-IV (Chunk 007: Quadratic Equation — Three Discriminant Cases (continued from 2.3.4)) -->

### Core Idea
Mathematical induction proves *infinitely many* statements indexed by ℕ in one stroke. After verifying a base case, you assume the claim for an arbitrary k and show it forces the claim for k + 1; the Principle of Mathematical Induction then gives the claim for all natural numbers.

> **In Simple Terms:** Climbing a ladder: show you can stand on rung 1, and show that *if* you can stand on rung k *then* you can step to rung k + 1. The Principle then says you can reach every rung.

### Key Concepts

#### When to Use Induction
Use when you have a family of statements {Sₙ : n ∈ ℕ} (or starting from some t ≥ 1) which are all true and indexed by natural numbers.

Standard example: Sₙ ≡ "the sum of the first n natural numbers = n(n + 1)/2".
- This is not one statement but infinitely many: S₁, S₂, S₁₀, S₁₀₀₀, ... — induction proves them all simultaneously.

#### Three Steps of Mathematical Induction
1. **Base / initial step:** Show S₁ is true (or S_t for some starting t).
2. **Induction Hypothesis (IH):** Assume Sₖ is true for an arbitrary k ≥ 1.
3. **Inductive step:** Using the base and IH, show Sₖ₊₁ is true.

(Some texts merge steps 2 and 3 into a single "Inductive Step".)

By the **Principle of Mathematical Induction**, Sₙ is then true for all n ∈ ℕ.

> **Variant:** If the claim is "true for all n ≥ t" for some t ∈ ℕ, the base step starts at S_t.

### Examples
**Example: Sum of first n natural numbers = n(n + 1)/2**

*Base step (n = 1):* S₁: sum of the first 1 natural number = 1 = 1(1 + 1)/2 = 1. ✓

*Induction Hypothesis:* Assume Sₖ: 1 + 2 + ... + k = k(k + 1)/2.

*Inductive Step:* Show Sₖ₊₁: 1 + 2 + ... + k + (k + 1) = (k + 1)(k + 2)/2.
Sₖ₊₁ = (1 + 2 + ... + k) + (k + 1) = Sₖ + (k + 1)
     = k(k + 1)/2 + (k + 1)   (by IH)
     = (k + 1)(k/2 + 1)
     = (k + 1)(k + 2)/2. ✓

By the Principle of Mathematical Induction, Sₙ holds for all n ∈ ℕ. ∎

### ⚠️ Common Mistakes
- ❌ Skipping the base step → ✅ Without the base, induction "starts on no rung" (one can "prove" false claims).
- ❌ Assuming Sₖ in the goal of the inductive step → ✅ Use Sₖ to derive Sₖ₊₁.
- ❌ Generalising induction to non-well-ordered index sets → ✅ Standard induction needs ℕ; for ℝ use other methods.

> **Quick Recall:**
> - Three steps: base, hypothesis, inductive.
> - Base may start at t > 1 if the claim only holds for n ≥ t.

### Connections
- Builds on: Direct proof, Section I (Chunk 007: Quadratic Equation — Three Discriminant Cases (continued from 2.3.4)).
- Continues into: Proof of Equivalences.

---

## Section: Appendix VI — Proof of Equivalences 🟡

### Core Idea
An equivalence statement uses "if and only if" (iff, ⇔). Its proof generally splits into two implications: (i) the "if" part (assume RHS, derive LHS — sometimes assume LHS, derive RHS depending on convention) and (ii) the "only if" part (the reverse direction). Sometimes both directions can be combined into a single chain of equivalences.

> **In Simple Terms:** "iff" means both directions hold. Prove "→" and prove "←", or chain ⇔'s where every step is reversible.

### Key Concepts

#### Two-Part Proof Template (for x ⇔ y):
- **(i) "if" part:** Assume one side, derive the other.
- **(ii) "only if" part:** Assume the converse, derive the original.

#### Single-Chain Variant
If every step of the argument is itself a biconditional, the entire proof can be written as a chain x ⇔ ... ⇔ y.

### Examples
**Example: For x, y ∈ ℕ, x > y iff x² > y².**

*Part (i) "if part" — assume x > y, show x² > y².*
- x ∈ ℕ ⟹ x > 0. Multiply both sides of x > y by x: x² = x·x > x·y.
- y > 0 (since y ∈ ℕ). From x > y, multiply by y: y·x > y·y = y².
- By commutativity & transitivity: x² > xy > y². ⟹ x² > y².

*Part (ii) "only if" — assume x² > y², show x > y.*
- Argument is symmetric, using 1/x > 0 and 1/y > 0 (both x, y ∈ ℕ).
- Replace x by 1/x and y by 1/y throughout the previous argument; ultimately get x > y.

**Example (combined chain): n is even iff 2n + 3 is odd.**
n is even
⇔ n = 2k for some k ∈ ℤ
⇔ 2n = 2(2k) = 4k for k ∈ ℤ
⇔ 2n + 3 = 4k + 3 = 4k + 2 + 1 = 2(2k + 1) + 1
⇔ 2n + 3 = 2K′ + 1 for K′ = 2k + 1 ∈ ℤ
⇔ 2n + 3 is odd. ∎

### ⚠️ Common Mistakes
- ❌ Proving only one direction → ✅ "iff" needs both.
- ❌ Using non-reversible steps in a single ⇔ chain → ✅ Each step must itself be biconditional.

> **Quick Recall:**
> - "iff" / "⇔" — both directions.
> - Either prove both directions separately, or chain biconditionals.

### Connections
- Builds on: Direct proof, Contradiction, Contrapositive (Chunk 007: Quadratic Equation — Three Discriminant Cases (continued from 2.3.4)).

---

## Section: Unit 3 — Relations and Functions: Structure, Objectives, Introduction 🟢

### Core Idea
Unit 3 introduces *relations* (subsets of cross-products of sets) and *functions* (a special kind of relation), along with their key properties (reflexivity, symmetry, transitivity), special structures (equivalence relations, partial orders, Hasse diagrams), and operations (composition, inverse, union). It closes with classifications of functions (injective, surjective, bijective).

> **In Simple Terms:** A relation is "any rule that pairs items"; a function is the special case where each input has exactly one output. This unit nails down the bookkeeping for both.

### Key Concepts

#### Unit 3 Structure
- 3.0 Objectives
- 3.1 Introduction
- 3.2 Relation
  - 3.2.1 Definition, Notation, Illustrations
  - 3.2.2 Properties of Relations
  - 3.2.3 Equivalence Relations, Equivalence Classes, Partition of a Set
  - 3.2.4 Partial Order Relation, Partially Ordered Set
  - 3.2.5 Operations on Relations
- 3.3 Function
  - 3.3.1 Conceptualising Function
  - 3.3.2 Function: Definition and Examples
  - 3.3.3 Operations as Functions
  - 3.3.4 Types of Functions (Injective, Surjective, Bijective)
- 3.4 Sum-Up; 3.5 Key Words; 3.6 Answers/Hints; 3.7 Exercises

#### Unit 3 Objectives (after this unit, the learner can):
- Distinguish between relation and function.
- Use relation notation.
- Explain reflexivity, symmetry, transitivity.
- Apply equivalence relation, equivalence class, partition of a set.
- Identify partial order relations and partially ordered sets.
- Draw Hasse diagrams.
- Apply operations (composition, inverse, union) to relations.
- Apply operations on functions.
- Determine injective, surjective, bijective functions.

#### Introduction — Motivation
Unit 1 introduced *set-relations* (⊆, ⊂, =) and *number-relations* (<, >, =). Real-world examples: father–daughter, mother–son, sibling, teacher–student, employer–employee. Economics: (item, cost-of-production), (item, sales-price), (income-of-family, expenditure).

**Direction matters:** if X is mother of Y, Y is not mother of X. For "<", 4 < 5 but not 5 < 4. Order of arguments is generally significant — except for symmetric relations (e.g., "=", "is sibling of").

**Across-set relations:** A relation need not connect a set to itself. *Age-of-person* is from a set of human beings to a set of numbers. This motivates ordered sets and cross-products.

### Definitions
- **Ordered Set**: a set in which the order of occurrence of elements is significant. Notation: parentheses, e.g., (a, b). Contrast with unordered set {a, b} = {b, a}. Crucially, (a, b) ≠ (b, a) in general. ⭐
- **Cross-product (Cartesian product)** of two non-empty sets X and Y, denoted X × Y: the set of all ordered pairs with first component from X and second from Y.
  - X × Y = {(x, y) : x ∈ X, y ∈ Y}. ⭐

### Examples
**Coordinate geometry illustration:** the point (2, 5) is at a different location from (5, 2). Hence ordered pairs.

### Connections
- Builds on: sets and set-relations from Unit 1 (Chunks 001-004).
- Continues into: 3.2.1 Relations as subsets of cross-products.

---

## Section: 3.2 Relation — Definition, Notation, and Examples (3.2.1) 🔴

### Core Idea
A *relation* from set X to set Y is a subset of X × Y. This formal definition unifies everyday relations (mother-of, less-than) with mathematical ones, lets us talk about domain/codomain/range, image, onto, one-to-one, empty, and universal relations, and supports notations as set-builder, roster, graph, or matrix.

> **In Simple Terms:** A relation is just a "list of allowed (input, output) pairs". Anything that fits the list "is related"; anything else isn't.

### Key Concepts

#### Definition
A **relation** from X to Y is any subset of X × Y.
- *is-mother-of* = {(m, c) : m ∈ X, c ∈ Y, m is mother of c} ⊆ X × Y, where X = Y = {humans}.
- *is-less-than* (on ℕ) = {(x, y) : x, y ∈ ℕ, x < y} ⊆ ℕ × ℕ.

#### Two notations for a relation
- **Set-builder form:** describes the property and gives R as a subset, e.g., is-mother-of = {(m, c) : m is mother of c}.
- **Roster form:** lists pairs explicitly, e.g., is-less-than = {(1,2), (1,3), ..., (2,3), (2,4), ...}.

If Sheela is mother of Shivam: write either "Sheela is-mother-of Shivam" or, in math, "(Sheela, Shivam) ∈ is-mother-of". If Savitri is not mother of Mohan: "(Savitri, Mohan) ∉ is-mother-of".

#### Arity of a Relation
| Arity | Args | Example |
|-------|------|---------|
| **Unary** (= property) | 1 | is-male, is-prime-number |
| **Binary** | 2 | is-mother-of, is-less-than |
| **Ternary** | 3 | is-integer-strictly-between(x, y, z); are-parents-of(x, y, z); (item, cost, price) in economics |
| **Quaternary** | 4 | timetable: (class, subject, teacher, room) |
| **n-ary** | n | R ⊆ X₁ × X₂ × ... × Xₙ |

A unary relation is a *property* of its argument (e.g., is-prime-number(19) is true; is-composite-number(19) is false).

**Default convention:** *unless explicitly stated otherwise, "relation" means binary relation.*

#### Standard Definitions for Binary Relations R ⊆ X × Y
- **Domain** = X (the source set).
- **Codomain** = Y (the target set).
- **Range** = {y ∈ Y : ∃ x ∈ X, (x, y) ∈ R} — the actually-used part of the codomain.
  - Example: R = (Person, 10-digit-Mobile-Number); domain = all persons; codomain = all 10-digit naturals; range = the 10-digit numbers actually used as someone's mobile number.
- **Image** of x ∈ X under R: any y ∈ Y with (x, y) ∈ R. Note: a relation may give multiple images.
- **Relation on X**: a binary relation where domain = codomain = X. (i.e., R ⊆ X × X.)
- **Onto relation**: every y ∈ Y appears as a second component of some pair in R.
  - is-mother-of is onto (every person has a mother).
  - (Person, Mobile-Number) is NOT onto (not every 10-digit number is a mobile number).
- **One-to-one relation**: distinct elements of the domain have distinct images.
  - (Person, Mobile-Number) is one-to-one (no two persons share a mobile number).
- **Empty relation**: R = ∅ ⊆ X × Y; no element of X relates to any element of Y. Example: X = {0..9}, R = {(a, b) : a − b = 10} — empty (no decimal digits differ by 10).
- **Universal relation**: R = X × Y; every element of X relates to every element of Y.
- Empty and universal are sometimes called **trivial relations**.

#### Notations Re-visited
For R on X, "x is related to y under R" can be written either:
- (x, y) ∈ R, or
- x R y.

Two more popular forms (full discussion in later units):
- **Graph** (vertices and arrows). Fig. 3.2 illustrates.
- **Matrix** representation.

**Graph example:** R = {(1, a), (1, b), (2, a), (3, a), (4, b), (4, c), (4, d)} from X = {1, 2, 3, 4} to Y = {a, b, c, d} can be drawn with arrows from each first-component on the left to its second-component on the right.

### Definitions Summary
- **Relation from X to Y**: any subset of X × Y. ⭐
- **Domain / Codomain / Range** as above. ⭐
- **Image of x under R**: y such that (x, y) ∈ R.
- **Relation on X**: relation with domain = codomain = X.
- **Onto relation**: range = codomain.
- **One-to-one relation**: distinct domain elements have distinct images.
- **Empty relation**: ∅ ⊆ X × Y.
- **Universal relation**: X × Y.

### Comparison Table
| Type | Defining property |
|------|------------------|
| Empty | R = ∅; no element related to any |
| Universal | R = X × Y; every element related to every |
| Onto | Range = Codomain |
| One-to-one | Distinct domain elements have distinct images |

### ⚠️ Common Mistakes
- ❌ Treating (a, b) and (b, a) as the same → ✅ Ordered pairs differ unless the relation is symmetric.
- ❌ Confusing range with codomain → ✅ Range ⊆ codomain; equality holds only for onto relations.
- ❌ Saying "every relation is a function" → ✅ Functions are a *special* kind of relation (each domain element has *exactly one* image).

### Edge Cases & Caveats
- Cross-product is defined for non-empty X and Y.
- An n-ary relation generalises by being a subset of X₁ × ... × Xₙ.

> **Quick Recall:**
> - Relation ⇔ subset of cross-product.
> - Cross-product X × Y = ordered pairs (x, y) with x ∈ X, y ∈ Y.
> - Domain (input set) / Codomain (target set) / Range (actually hit subset).
> - Onto: range = codomain. One-to-one: injective on domain.
> - Empty and universal are trivial relations.

### Connections
- Builds on: Sets, subsets, ordered pairs (Unit 1, Chunks 001-004).
- Continues into: 3.2.2 Properties of Relations (reflexivity, symmetry, transitivity); 3.3 Function definition.

### Open Questions
- Exactly when does a binary relation R on X qualify as a function? (Preview: when each x ∈ X has exactly one image — covered in 3.3.2.)
- How does the matrix representation interact with composition of relations? (Preview: matrix product in {0,1}-arithmetic.)


---

<!-- Continuity: Continues Unit 3 "Relations and Functions" begun in earlier chunks. The matrix and digraph representations of a relation referenced at the start (Fig. 3.3, Fig. 3.4) finish a discussion of "ways to represent relations" started in chunk 008. The chunk then develops Section 3.2.2 (Properties of Relations), 3.2.3 (Equivalence Relations / Partition), 3.2.4 (Partial Order). It is followed (in chunk 010) by 3.2.5 Operations on Relations and 3.3 Functions. -->

## Section: Representing Relations (Matrix & Directed-Graph) 🟢

### Core Idea
A relation R from set X to set Y can be visualized in two compact ways: a 0/1 matrix (rows = elements of X, columns = elements of Y; entry is 1 iff the pair is in R) and, if R is on a single set X (domain = codomain), a directed graph in which an arrow from a to b represents (a,b) ∈ R.

> **In Simple Terms:** The matrix is a tick-table: put a 1 wherever a pair is "in" the relation. The digraph is a map: draw arrows from one element to another whenever they're related.

### Examples
**Example: Matrix representation**
For X = {1,2,3,4}, Y = {a,b,c,d}, R = {(1,a),(1,b),(1,c),(2,b),(2,c),(2,d)}.
The matrix has a 1 at (row 1, cols a,b,c), 1 at (row 2, cols b,c,d), and 0s in rows 3 and 4.

**Example: Directed graph**
On X = {1,2,3} with R = {(1,1),(1,2),(2,2),(3,1),(3,3)}: draw self-loops at 1, 2, 3 (where (a,a) ∈ R), and directed edges 1→2 and 3→1.

### Definitions
- **Relation vs Operation**: a relation returns TRUE/FALSE (e.g., 3 < 5 → TRUE). An operation returns a new element (e.g., 8 + 15 = 23; √16 = 4).

### Connections
- Builds on relation definition (Chunk 008: Appendix V — Proof by Mathematical Induction).
- Prerequisite for: properties of relations below.

---

## Section: Reflexive, Not-Reflexive, Anti-Reflexive 🔴

### Core Idea
The three central properties of relations on a single set X are reflexivity, symmetry and transitivity. Reflexivity is the simplest: it asks whether every element relates to itself. The opposite is anti-reflexive (no element relates to itself); "not reflexive" is the milder negation (at least one element fails to relate to itself).

> **In Simple Terms:** Reflexive = everyone is friends with themselves. Anti-reflexive = nobody is friends with themselves. Not-reflexive = at least one person isn't friends with themselves (the others might or might not be).

### Definitions
- **Reflexive**: R on X is reflexive if for every a ∈ X, (a,a) ∈ R. ⭐
- **Not-reflexive**: there exists at least one a ∈ X with (a,a) ∉ R. ⭐
- **Anti-reflexive / irreflexive**: for every a ∈ X, (a,a) ∉ R. ⭐

### Key Concepts

| Property | Quantifier | Condition |
|---|---|---|
| Reflexive | ∀ a ∈ X | (a,a) ∈ R |
| Not-reflexive | ∃ a ∈ X | (a,a) ∉ R |
| Anti-reflexive | ∀ a ∈ X | (a,a) ∉ R |

Every anti-reflexive relation is also not-reflexive (∀ implies ∃ for non-empty X), but a not-reflexive relation need not be anti-reflexive.

### Examples
**Reflexive examples:**
- Equality (=) on N = {1,2,3,...}.
- "is-sibling-of" on the set of all human beings.
- The universal relation on X.

**Not-reflexive (but not anti-reflexive) example:**
- On N: define (a,b) ∈ R iff a × b is even. Then 1 × 1 = 1 is odd, so (1,1) ∉ R, hence not reflexive. But (2,2) ∈ R, so not anti-reflexive either.
- "is-brother-of" on all humans: fails for females (Sheela is not her own brother), but holds for males.

**Anti-reflexive examples:**
- "is-less-than" (<) on numbers (x < x is always false).
- "is-mother-of" on humans.
- R = {(2,3),(3,1),(2,1)} on {1,2,3}.

**Empty relation** on a non-empty X is not reflexive (no pairs at all).

### Edge Cases & Caveats
- Just changing the underlying set X can change the property:
  - "is-brother-of" on males → reflexive; on females → anti-reflexive.
  - Product-is-even on integers: reflexive on even integers, anti-reflexive on odd integers, neither on all integers.

### ⚠️ Common Mistakes
- ❌ Treating "not-reflexive" as a synonym for "anti-reflexive" → ✅ Not-reflexive needs only one failure; anti-reflexive needs every element to fail.
- ❌ Forgetting that the empty relation on a non-empty set is not reflexive → ✅ Reflexivity requires (a,a) for every a; ∅ has no pairs.

> **Quick Recall:**
> - Reflexive: every (a,a) is in R.
> - Anti-reflexive: no (a,a) is in R.
> - Not-reflexive: at least one (a,a) is missing from R.
> - Anti-reflexive ⇒ not-reflexive; converse fails.

### Check Your Progress 1
1. R on X = {1,2,3,4}, R = {(1,2),(2,1),(2,3),(3,1),(3,2),(3,4),(4,3)} — give graphic and matrix representation.
2. Classify (reflexive / not-reflexive / anti-reflexive):
   - is-congruent-to on triangles → **reflexive**.
   - ≤ on numbers → **reflexive**.
   - < on N → **anti-reflexive**.

---

## Section: Symmetric, Not-Symmetric, Antisymmetric, Asymmetric 🔴

### Core Idea
Symmetry asks whether the relation is "two-way": if a is related to b, must b be related to a? Anti-symmetry is the strong opposite: the only way both directions hold is if a = b.

> **In Simple Terms:** Symmetric = if I'm your friend, you're mine. Antisymmetric = if I'm ≤ you and you're ≤ me, we're the same person. Not-symmetric = at least one one-way street exists.

### Definitions
- **Symmetric**: ∀ a, b ∈ X, (a,b) ∈ R ⇒ (b,a) ∈ R. ⭐
- **Not-symmetric**: ∃ a, b ∈ X with (a,b) ∈ R but (b,a) ∉ R. ⭐
- **Antisymmetric**: if (a,b) ∈ R and (b,a) ∈ R, then a = b. ⭐

### Key Concepts

| Property | Quantifier | Condition |
|---|---|---|
| Symmetric | ∀ pairs | (a,b) ∈ R ⇒ (b,a) ∈ R |
| Not-symmetric | ∃ pair | (a,b) ∈ R but (b,a) ∉ R |
| Antisymmetric | ∀ pair, a ≠ b | (a,b) ∈ R ⇒ (b,a) ∉ R |

### Examples
**Symmetric:** equality on N; is-congruent-to on triangles; is-sibling-of on humans.

**Not-symmetric:** ≤ on integers (3 ≤ 4 but 4 ≰ 3); is-mother-of; R = {(1,1),(2,2),(3,3),(1,2)} on {1,2,3}.

**Antisymmetric:** ≤ on integers; on X = {1,2,3}: {(1,1)}, {(1,1),(2,2)} are both symmetric and antisymmetric; {(1,2),(1,3)} is antisymmetric but not symmetric.

### Edge Cases & Caveats
- A relation can be both symmetric AND antisymmetric. This happens when R contains only pairs of the form (a,a). Example: {(1,1),(2,2)}.
- Every antisymmetric relation is not-symmetric (provided it has any off-diagonal pair); but not-symmetric doesn't imply antisymmetric. Counter-example: R = {(a,b),(a,c),(c,a)} is not-symmetric (because (b,a) ∉ R), but not antisymmetric (since (a,c), (c,a) both in R yet a ≠ c).

> **Quick Recall:**
> - To prove symmetric: assume (a,b) ∈ R, show (b,a) ∈ R.
> - To disprove symmetric: produce one pair (a,b) ∈ R with (b,a) ∉ R.
> - Antisymmetric ≠ "not symmetric"!

### Check Your Progress 2
- is-congruent-to on triangles → **symmetric**.
- ≤ on numbers → **not symmetric** (3 ≤ 4 but 4 ≰ 3); also **antisymmetric**.
- is-brother-of on all males → **symmetric** (every male is his own brother by the formal definition); **not antisymmetric**.

---

## Section: Transitive, Not-Transitive, Anti-Transitive 🔴

### Core Idea
Transitivity is the "chaining" property: if a relates to b and b relates to c, then a should relate to c. Anti-transitivity says the chain is always broken: whenever a→b and b→c, then a does not relate to c.

> **In Simple Terms:** Transitive = "friend of a friend is a friend." Anti-transitive = "the enemy of my enemy is never my enemy."

### Definitions
- **Transitive**: ∀ a,b,c ∈ X, (a,b) ∈ R ∧ (b,c) ∈ R ⇒ (a,c) ∈ R. ⭐
- **Not-transitive**: ∃ a,b,c with (a,b),(b,c) ∈ R but (a,c) ∉ R. ⭐
- **Anti-transitive**: ∀ a,b,c with (a,b),(b,c) ∈ R, we have (a,c) ∉ R. ⭐

### Examples
**Transitive:** =, <, ≤ on numbers; is-congruent-with on triangles; is-brother-of on humans.

**Not-transitive:** is-mother-of (a→mother→b, b→mother→c gives a = grandmother of c, not mother). On {1,2,3}, R₃ = {(1,2),(3,3),(2,3),(2,2),(2,1)}: (1,2),(2,3) ∈ R but (1,3) ∉ R.

**Anti-transitive:**
- "is-perpendicular-to" on lines in a plane (a ⊥ b, b ⊥ c ⇒ a ∥ c, so a ⊥̸ c).
- is-mother-of (also anti-transitive).
- On {1,2,3}: R = {(1,2),(2,3),(3,1)} — every chain breaks.

### Edge Cases & Caveats
- Anti-transitive ⇒ not-transitive (provided some chain a→b→c exists), but not-transitive doesn't imply anti-transitive.
- Counter-example: R = {(1,2),(2,3),(1,3),(3,2)} on {1,2,3}: not transitive ((2,3),(3,2) ∈ R but (2,2) ∉ R), but not anti-transitive ((1,2),(2,3),(1,3) all in R).

> **Quick Recall:**
> - Transitive: every chain closes.
> - Anti-transitive: every chain breaks.
> - Not-transitive: at least one chain breaks.

### Check Your Progress 3
- "Angle between lines a and b is 30°" → **not transitive** (b can rotate relative to a, then to c, total angle could be 60°).
- ≤ on numbers → **transitive**.
- is-brother-of on all humans → **transitive**.

---

## Section: Generating Examples & Counter-Examples 🟡

### Core Idea
To construct a relation with a chosen mix of properties, start with a small set like {a,b,c} and add pairs one by one — each chosen to enforce a required property or to violate one. Be careful that adding a pair to satisfy one condition does not silently violate an earlier-satisfied condition.

### Mechanisms / Processes
1. Start with X = {a,b,c}.
2. Make R reflexive by adding (a,a),(b,b),(c,c).
3. To make it not symmetric, add (a,b) but not (b,a).
4. So R = {(a,a),(b,b),(c,c),(a,b)} is reflexive, transitive (vacuously through this single off-diagonal), and not symmetric.
5. To break transitivity (while keeping reflexivity & non-symmetry), add (b,c): now (a,b),(b,c) ∈ R but (a,c) ∉ R.
6. To break reflexivity, drop, say, (a,a).

### ⚠️ Common Mistakes
- ❌ Adding pairs without checking if they re-introduce a property you wanted to break → ✅ After each addition, recheck all required properties.

---

## Section: Equivalence Relations & Partition of a Set 🔴

### Core Idea
A relation that is **simultaneously reflexive, symmetric and transitive** is called an equivalence relation. Such relations carve the underlying set into disjoint "equivalence classes" — and conversely, any way of slicing the set into disjoint non-empty pieces (a partition) produces a unique equivalence relation. Equivalence relations let us treat many distinct elements as a single entity for some purpose.

> **In Simple Terms:** An equivalence relation is a fancy "=" — it groups elements into bundles where members of a bundle are interchangeable for the task at hand. The bundles are the partition.

### Definitions
- **Equivalence relation**: R on X is an equivalence relation iff R is reflexive, symmetric, and transitive. ⭐
- **Equivalence class** of a under R: [a] = {x ∈ X : (x,a) ∈ R}. ⭐
- **Partition of X**: a non-empty collection P = {Xᵢ} of subsets of X such that
  1. Xᵢ ≠ ∅ for each i,
  2. Xᵢ ∩ Xⱼ = ∅ for distinct i, j,
  3. ⋃ Xᵢ = X. ⭐

### Examples
- Equality (=) on Q.
- "is-parallel-to" on lines in a plane.
- "is-congruent-to" on triangles.
- "is-sibling-of" on humans.

**Partitions of X = {a,b,c}** (5 possible):
1. {{a},{b},{c}}
2. {{a},{b,c}}
3. {{a,b},{c}}
4. {{b},{a,c}}
5. {{a,b,c}}

**Equivalence classes** for R = {(a,a),(b,b),(b,c),(c,b),(c,c)} on {a,b,c}: classes are {a} and {b,c}.

### Mechanisms / Processes (Partition ⇒ Equivalence Relation)
Given partition P = {Aᵢ}, define R by: (x,y) ∈ R iff x and y lie in the same Aᵢ.
1. **Reflexive**: x and x are in the same class ⇒ (x,x) ∈ R.
2. **Symmetric**: x,y same class ⇒ y,x same class ⇒ (y,x) ∈ R.
3. **Transitive**: (x,y) and (y,z) ∈ R ⇒ x,y in Aᵢ; y,z in Aⱼ. Since y ∈ Aᵢ ∩ Aⱼ and partition pieces are disjoint, Aᵢ = Aⱼ, so x,z share a class ⇒ (x,z) ∈ R.

### Counter-examples (Not equivalence)
- **Fails reflexive**: X = {1,2,3}, R = {(2,2),(3,3),(2,3),(3,2)} — (1,1) ∉ R. (Symmetric and transitive but not reflexive.)
- **Fails symmetric**: R = {(1,1),(2,2),(3,3),(2,3)} — (3,2) ∉ R. (Reflexive and transitive but not symmetric.)
- **Fails transitive**: R = {(1,1),(2,2),(3,3),(1,2),(2,1),(2,3),(3,2)} — (1,2),(2,3) ∈ R but (1,3) ∉ R. (Reflexive and symmetric but not transitive.)

### Applications
Designing a school timetable for 1000 students in 5 classes × 4 sections × 50 students: rather than 1000 individuals, treat each class-section as a single equivalence class (under "same-class-section"). Only 20 entities to schedule. Equivalence relations are also fundamental in digital-circuit design and other sequential-machine theory.

> **Quick Recall:**
> - Equivalence ⇔ reflexive + symmetric + transitive.
> - Equivalence relation on X ↔ partition of X (one-to-one correspondence).
> - The three properties are independent — none implies any other.

### Check Your Progress 4
1. The three properties are independent. Examples:
   - **Reflexive only**: on Z, (a,b) ∈ R iff 0 ≤ a − b < 1. (Not symmetric: (4,3) ∈ R, (3,4) ∉ R; not transitive.)
   - **Symmetric only**: "is-perpendicular-to" on lines in a plane.
   - **Transitive only**: < on rationals.
2. Partition from R = {(1,1),(2,2),(3,3),(4,4),(1,3),(3,1),(2,4),(4,2)} on {1,2,3,4} → **{{1,3},{2,4}}**.

### Connections
- Foundation for partial orders (next section).
- Prerequisite for: modular arithmetic, quotient sets, group cosets in advanced courses.

---

## Section: Partial Order Relations & Posets 🔴

### Core Idea
Replace "symmetric" in the equivalence-relation recipe by "antisymmetric" and you get a **partial order**: a relation that is reflexive, antisymmetric, and transitive. The pair (X, R) is then a **partially ordered set (poset)**. "Partial" because some elements may be incomparable (neither (x,y) nor (y,x) is in R).

> **In Simple Terms:** A partial order ranks elements like ≤, but allows "ties of incomparability" — some pairs simply cannot be ranked against each other (think: subset-of among arbitrary subsets, or divides-among numbers).

### Definitions
- **Partial order**: R on X is reflexive, antisymmetric, and transitive. ⭐
- **Poset**: ordered pair (X, R) where R is a partial order on X.
- **Total order**: a partial order where every pair is comparable, i.e. (x,y) ∈ R or (y,x) ∈ R for all x,y. ⭐

### Examples
- ≤ on Q (rationals) — partial order.
- ⊆ (subset-of) on the power set of a set — partial order.
- "is-divisor-of" on N — partial order.
- "is-divisor-of" on {1, p, p², p³, ...} for prime p — total order.

### Edge Cases & Caveats
- In ⊆ on subsets, {a,b,c} and {b,c,d} are **incomparable**: neither is a subset of the other.
- Under is-divisor-of: 5 and 9 are incomparable (5 ∤ 9, 9 ∤ 5).

### Connections
- Builds on antisymmetric (above).
- Prerequisite for: Hasse diagrams (Chunk 010: Hasse Diagrams & Special Elements of a Poset), lattices, order theory.

### Open Questions
- For a relation that is reflexive and antisymmetric but not transitive, is the resulting graph a poset? (No — transitivity is required.)
- How many distinct partial orders exist on a 3-element set?


---

<!-- Continuity: Continues Section 3.2.4 (Partial Order, started in chunk 009) by introducing Hasse diagrams and order-theoretic special elements. Then covers Section 3.2.5 (Operations on Relations) and opens Section 3.3 (Functions): conceptualisation, definition, operations as functions, and types — injective, surjective, bijective. Continues into chunk 011 with answers, exercises and Unit 4. -->

## Section: Hasse Diagrams & Special Elements of a Poset 🔴

### Core Idea
A **Hasse diagram** is a stripped-down picture of a finite poset: nodes are elements of X, and an upward edge is drawn from x to y whenever x R y (omitting reflexive loops and transitively-implied edges). The diagram makes it easy to spot "extremes" — minimal, maximal, minimum (least) and maximum (greatest) elements.

> **In Simple Terms:** A Hasse diagram is a layered ladder of a partial order. Bottom rungs = elements nobody is below; top rungs = elements nobody is above.

### Definitions
- **Hasse diagram**: graphical representation of a finite poset (X, R); draw an upward line from x to y whenever (x,y) ∈ R (after suppressing reflexive loops and edges implied by transitivity).
- **Minimal element**: a ∈ X such that there is no x ∈ X (x ≠ a) with (x, a) ∈ R, i.e. nothing is strictly "below" a. ⭐
- **Maximal element**: a ∈ X such that there is no y ∈ X (y ≠ a) with (a, y) ∈ R, i.e. nothing is strictly "above" a. ⭐
- **Minimum / least element**: the unique minimal element when only one exists.
- **Maximum / greatest element**: the unique maximal element when only one exists.

### Examples

**Example: Divisors of 12 under proper-divisor (Fig. 3.5)**
X = {1, 2, 3, 4, 6, 12}. Diagram has 1 at bottom, then 2 and 3, then 4 and 6, then 12 at top. Single maximum = 12 (greatest), single minimum = 1 (least).

**Example: Power set of {x, y, z} under ⊆ (Fig. 3.6)**
8 elements from ∅ to {x,y,z}. Bottom = ∅, top = {x,y,z}. A "cube"-shaped Hasse diagram.

**Example: X = {3, 4, 12, 24, 48, 72} under proper-divisor (Fig. 3.7)**
Two minimal elements: 3 and 4 (neither divides anything smaller in X).
Two maximal elements: 48 and 72.
No least/greatest element (because more than one minimal/maximal).

### Edge Cases & Caveats
- A poset can have multiple minimal or maximal elements.
- "Minimum/least" exists only when there is exactly **one** minimal element; same for maximum.
- Reflexive self-loops and transitively-derived edges are NOT drawn in a Hasse diagram (otherwise it would be cluttered and uninformative).

> **Quick Recall:**
> - Minimal = nothing below it in R.
> - Maximal = nothing above it in R.
> - Least/greatest = unique minimal/maximal.

### Check Your Progress 5
Hasse diagrams of (X, is-proper-divisor-of):
1. X = divisors of 30 = {1,2,3,5,6,10,15,30} → minimal = 1, maximal = 30.
2. X = divisors of 24 = {1,2,3,4,6,8,12,24} → minimal = 1, maximal = 24.
3. X = divisors of 60 → minimal = 1, maximal = 60.
4. X = divisors of 32 = {1,2,4,8,16,32} → minimal = 1, maximal = 32 (this is a chain, hence totally ordered).

### Connections
- Builds on partial order (Chunk 009: Representing Relations (Matrix & Directed-Graph)).
- Prerequisite for: lattices, lub/glb concepts.

---

## Section: Operations on Relations 🔴

### Core Idea
Operations take relations as input and produce new relations as output. They split into three families: **set-type** (union, intersection, difference, complement) treat a relation as a set of pairs; **mapping-type** (inverse, composition) flip or chain relations like functions; **closure** operations (reflexive-, symmetric-, transitive-closure) add the minimum number of pairs needed to enforce a given property.

> **In Simple Terms:** Set-type ops treat relations as bags of pairs; mapping-type ops let you walk the arrows backwards or in sequence; closure ops are the smallest "patches" that force a missing property to hold.

### Definitions
- **Set-type operations**: union (R ∪ S), intersection (R ∩ S), difference (R − S), complement (Rᶜ = U − R, where U is the universal relation X × Y).
- **Inverse R⁻¹**: from Y to X, where (y,x) ∈ R⁻¹ iff (x,y) ∈ R.
- **Composition R ∘ S** (with cod(R) = dom(S)): new relation from dom(R) to cod(S) such that (x,z) ∈ R ∘ S iff ∃ y with (x,y) ∈ R and (y,z) ∈ S. ⭐
- **Reflexive closure** of R: smallest reflexive relation containing R; add all (x,x) not yet in R.
- **Symmetric closure** of R: smallest symmetric relation containing R; for each (x,y) ∈ R add (y,x) if missing.
- **Transitive closure** of R: smallest transitive relation containing R; add all chains-of-pairs implied by composing R with itself.

### Examples (Set-type)
Let X = {1,2,3,4}, Y = {a,b,c}.
- R = {(1,a),(2,a),(2,c),(3,b),(4,b),(4,c)}
- S = {(1,b),(2,a),(3,a),(3,b),(4,a)}
- Universal U: 4 × 3 = 12 pairs.

| Op | Result |
|---|---|
| R ∪ S | {(1,a),(2,a),(2,c),(3,b),(4,b),(4,c),(1,b),(3,a),(4,a)} |
| R ∩ S | {(2,a),(3,b)} |
| R − S | {(1,a),(2,c),(4,b),(4,c)} |
| S − R | {(1,b),(3,a),(4,a)} |
| Rᶜ | {(1,b),(1,c),(2,b),(3,a),(3,c),(4,a)} |

### Examples (Mapping-type)
**Inverse:** R = {(1,a),(2,a),(2,c),(3,b),(4,b),(4,c)}.
R⁻¹ = {(a,1),(a,2),(c,2),(b,3),(b,4),(c,4)}.

**Composition:**
R from X = {1,2,3,4} to Y = {a,b,c}: R = {(1,a),(2,a),(2,c),(4,c)}.
S from Y to Z = {triangle, square}: S = {(a,triangle),(b,square),(b,triangle),(c,square)}.
R ∘ S = {(1,triangle),(2,triangle),(2,square),(4,square)}.

### Examples (Closures)
For R = {(2,2),(3,3),(2,3),(3,1)} on {1,2,3}:
- **Reflexive closure**: add (1,1) → {(2,2),(3,3),(2,3),(3,1),(1,1)}.
- **Symmetric closure**: add (3,2) and (1,3) → {(2,2),(3,3),(2,3),(3,1),(3,2),(1,3)}.
- **Transitive closure**: chain (2,3),(3,1) ⇒ add (2,1) → {(2,2),(3,3),(2,3),(3,1),(2,1)}.

### ⚠️ Common Mistakes
- ❌ Confusing inverse R⁻¹ with complement Rᶜ → ✅ R⁻¹ swaps coordinates of each pair; Rᶜ contains pairs **not** in R.
- ❌ Adding too many pairs in closure → ✅ Closures are "minimal" — add only what's needed.
- ❌ Composing relations when codomain of R ≠ domain of S → ✅ Composition R ∘ S requires cod(R) = dom(S).

> **Quick Recall:**
> - Closure = minimum extra pairs to enforce the property.
> - R⁻¹: swap each (x,y) → (y,x).
> - Composition: chain through a middle element y.

### Connections
- Builds on set operations from Unit 1.
- Prerequisite for: function composition, group operations.

---

## Section: Conceptualising Functions 🟡

### Core Idea
A **function** is a unique-valued rule that links each value of an independent variable to one and only one value of a dependent variable. Many real-world relationships fit this mould: distance as a function of time at constant speed; loan amount as a function of time at simple interest; area of a circle as a function of radius.

> **In Simple Terms:** A function is a one-output machine — feed it any allowed input and you always get exactly one answer back, with no surprises.

### Examples
- **(a)** Vehicle at 50 km/h: d = 50t. Plug t = 3 → d = 150; t = 5 → d = 250. Each input gives exactly one output. Write d = f(t) with f(t) = 50t.
- **(b)** Simple interest: A = 50000(1 + 6/100)ᵗ. Define g(t) = 50000(1 + 6/100)ᵗ; then A = g(t).
- **(c)** Area of circle: Area = π r². Define h(r) = π r²; then Area = h(r).

### Definitions
- **Function name**: the symbol (f, g, h, ...) labelling the rule.
- **Independent variable**: the input (e.g., t, r).
- **Dependent variable**: the output (e.g., d, A, Area).
- **Functional dependence**: the relationship "y is uniquely determined by x".

---

## Section: Function — Formal Definition 🔴

### Core Idea
A function f: X → Y is a special kind of relation in which every element of X has exactly one partner in Y. Two requirements: existence (each x has at least one image) and uniqueness (each x has at most one image).

### Definitions
- **Function f: X → Y**: rule associating to each x ∈ X a unique y ∈ Y, written y = f(x). ⭐
- **Domain** of f: the set X.
- **Codomain** of f: the set Y.
- **Image** of x under f: f(x); equivalently, "value of x under f".
- **Pre-image** of y: any x with f(x) = y.
- **Range** of f: {f(x) : x ∈ X} ⊆ Y — the actual outputs achieved.
- **Map / mapping**: synonyms for function.
- **Real function**: any function whose domain is R (or a subset of R).
- **Real-valued function**: any function whose codomain is R.
- **Complex-valued, integer-valued, rational-valued**: codomain is C, Z, Q respectively.

### Key Concepts

**Function vs Relation**:
| | Relation | Function |
|---|---|---|
| Each x in domain | may have any number of partners | must have exactly one partner |
| Each y in codomain | unrestricted | unrestricted (may have zero or many pre-images) |

**Multi-variable functions**: a function may have several independent variables.
- Area of rectangle: A_Rect = f₁(l, b) = l × b.
- Volume of container: v = f₂(l, b, h) = l × b × h.

But in this unit, we focus on single-variable functions f: R → Y.

### Examples
1. **f: N → N, f(x) = 2x + 1**. For each x ∈ N, 2x + 1 ∈ N and unique → function. ✓
2. **f: Z → N, f(x) = x² + 3**. For each x ∈ Z, x² + 3 ∈ N → function. ✓
3. **f: Z → N, f(x) = x² − 3**. For x = 0, x² − 3 = −3 ∉ N → **not a function** (image escapes the codomain). ✗
4. **f: Z → Z, f(x) = x² − 3**. Now image is in Z → function. ✓ (Note: changing codomain converted a non-function into a function.)

### ⚠️ Common Mistakes
- ❌ Forgetting that the image must lie in the codomain → ✅ A rule like f(x) = √x is NOT a function from Z to N (negative inputs have no real square root).
- ❌ Reading "→" in f: X → Y as logical implication → ✅ "→" here is just notation: X is on the left (domain), Y on the right (codomain).

> **Quick Recall:**
> - Function = relation + (existence + uniqueness of image).
> - Range ⊆ Codomain (range may be a strict subset).
> - Same rule + different codomain can change "function or not".

---

## Section: Operations as Functions 🟡

### Core Idea
A binary (or k-ary) operation on a set X is itself a function — its domain is the cross-product X × X (or X × X × ... × X) and its codomain is X (or wherever the result lives). This perspective unifies operations and functions.

### Examples
- Addition on N: Plus: N × N → N, Plus(x, y) = x + y.
- Set union on the power set P of a universe U: Union: P × P → P, Union(X, Y) = X ∪ Y.
- Squaring on N: SQ: N → N, SQ(n) = n². (Here domain = codomain.)

> **Quick Recall:**
> - An "operation" is a function whose domain is a (Cartesian power of) the codomain.

---

## Section: Injective Functions 🔴

### Core Idea
A function f: X → Y is **injective** (or one-to-one, "1-1") if distinct inputs give distinct outputs — no two different x's are sent to the same y.

> **In Simple Terms:** No collisions. Every input claims its own private output.

### Definitions
- **Injective (1-1)**: f: X → Y is injective if x₁ ≠ x₂ ⇒ f(x₁) ≠ f(x₂). Equivalently, f(x₁) = f(x₂) ⇒ x₁ = x₂. ⭐

**Note on terminology**: Avoid using "1-1" and "1-to-1" interchangeably — "1-to-1" typically refers to **bijective** (a different concept).

### Mechanisms / Processes (proving injectivity)
1. Assume f(x) = f(y) for arbitrary x, y in domain.
2. Manipulate algebraically to deduce x = y.
3. Conclude f is injective.

To **disprove** injectivity, exhibit a single pair x ≠ y with f(x) = f(y).

### Examples
1. **f: N → N, f(x) = 2x + 1.** Suppose f(x) = f(y): 2x + 1 = 2y + 1 ⇒ x = y. ✓ Injective.
2. **f: N → R, f(x) = √x.** f(x) = f(y) ⇒ √x = √y ⇒ x = y (squaring). ✓ Injective.
3. **f: N → R, f(x) = x².** f(x) = f(y) ⇒ x² = y² ⇒ x = ±y. But −y ∉ N, so x = y. ✓ Injective on N.
4. **f: Z → R, f(x) = x²** is **NOT** injective: f(2) = f(−2) = 4.

---

## Section: Surjective (Onto) Functions 🔴

### Core Idea
A function f: X → Y is **surjective** (or onto) if every element of the codomain Y is hit — for every y ∈ Y there is some x ∈ X with f(x) = y. The range equals the codomain.

> **In Simple Terms:** No leftovers in the codomain. Every potential output is actually produced by some input.

### Definitions
- **Surjective (onto)**: f: X → Y is surjective if for every y ∈ Y, there exists x ∈ X with f(x) = y. ⭐

### Mechanisms / Processes (proving surjectivity)
1. Take an arbitrary y in codomain Y.
2. Solve f(x) = y for x in terms of y.
3. Verify the solved x lies in domain X.
4. If yes for all y, f is surjective; if any y has no x in X, f is not surjective.

### Examples
- **f: N → N, f(x) = 2x + 1.** For y = 4 in N, x = 3/2 ∉ N → **not surjective**.
- **Mod: Z → N**, Mod(x) = |x|. For y ∈ N, x = y ∈ Z gives Mod(x) = y. ✓ Surjective.
- **f: Z → C, f(x) = √x (positive root).** Take y = 3.75 ∈ C; we need x = (3.75)² = 14.0625 ∉ Z → **not surjective**.
- **f: C → C, f(x) = √x.** Surjective (every complex number is a square root of its square).

---

## Section: Bijective Functions / 1-to-1 Correspondence 🔴

### Core Idea
A function is **bijective** if it is both injective and surjective. It pairs up elements of X and Y perfectly: every x has a unique partner in Y, and every y has a unique partner in X.

### Definitions
- **Bijective**: injective + surjective. ⭐
- **1-to-1 correspondence**: synonym for bijective.

### Edge Cases & Caveats
- A bijection between X and Y means |X| = |Y| (when finite), and both sets have "the same size" in general (cardinality).

> **Quick Recall:**
> - Injective: distinct inputs → distinct outputs (no collisions).
> - Surjective: every codomain element is hit (range = codomain).
> - Bijective: both — perfect pairing.

### Check Your Progress 6 (preview — answers in chunk 011)
1. Domain & range of (i) f(x) = −|x|; (ii) f(x) = +√(9 − x²).
2. f(x) = 2x − 5: compute f(0), f(7), f(−3).
3. Function or not? (i) f: N → N, f(x) = x − 3; (ii) f: N → Z, f(x) = x − 3.

### Connections
- Builds on relations (chunk 009).
- Prerequisite for: invertibility (a function has an inverse iff it is bijective), composition (chunk 010 set-type ops), graphing functions (Unit 4 / chunk 011-012).

### Open Questions
- For finite sets, when does injective ⇒ surjective?
- How do we test bijectivity graphically? (Hint: vertical line test + horizontal line test, treated in Unit 4.)


---

<!-- Continuity: Wraps Unit 3 with Key Words glossary, full Answers/Hints to all Check Your Progress exercises (CYP 1-6), and Unit 3 end-of-unit Exercises (Q1-Q7). Then opens Unit 4 "Coordinate Geometry and Representation of Functions" with structure, objectives, introduction, vertical line test, and the relationship between equation and function. Continues into chunk 012 with Coordinate Geometry, Cartesian system, linear/non-linear graphing. -->

## Section: Unit 3 — Key Words (Glossary) 🟡

### Core Idea
Glossary capturing the central definitions of Unit 3 in a compact, exam-ready form.

### Definitions
- **Equivalence Relation**: R on X is reflexive, symmetric, and transitive simultaneously: (i) ∀x ∈ X, (x,x) ∈ R; (ii) (x,y) ∈ R ⇒ (y,x) ∈ R; (iii) (x,y) ∈ R ∧ (y,z) ∈ R ⇒ (x,z) ∈ R. ⭐
- **Equivalence Class**: [a] = {x : (x,a) ∈ R} for an equivalence relation R. ⭐
- **Function**: f: X → Y, a rule associating each x ∈ X with a unique y ∈ Y, written y = f(x). ⭐
- **Injective Function**: f: X → Y with x₁ ≠ x₂ ⇒ f(x₁) ≠ f(x₂); equivalently f(x₁) = f(x₂) ⇒ x₁ = x₂. ⭐
- **Partition of a Set**: collection P = {Xᵢ} of non-empty mutually disjoint subsets of X whose union is X. ⭐
- **Partial Order Relation**: R on X is reflexive, antisymmetric, and transitive. ⭐
- **Partially Ordered Set (Poset)**: ordered pair (X, R) with R a partial order on X.
- **Surjective Function**: f: X → Y where for every y ∈ Y there exists x ∈ X with f(x) = y. ⭐

---

## Section: Answers / Hints to Check Your Progress (CYP 1–6) 🔴

### Check Your Progress 1 — Representations & Reflexivity
1. R on X = {1,2,3,4} with R = {(1,2),(2,1),(2,3),(3,1),(3,2),(3,4),(4,3)}.
   - **Graphic representation**: arrows between elements as listed.
   - **Matrix representation** (rows/cols indexed 1–4):

     | | 1 | 2 | 3 | 4 |
     |---|---|---|---|---|
     |1| 0 | 1 | 0 | 0 |
     |2| 1 | 0 | 1 | 0 |
     |3| 1 | 1 | 0 | 1 |
     |4| 0 | 0 | 1 | 0 |

2. Classifications:
   - is-congruent-to on triangles → **symmetric** (and also reflexive, transitive).
   - ≤ on numbers → **not symmetric** (3 ≤ 4 true, 4 ≤ 3 false). Also **antisymmetric** (x ≤ y and y ≤ x ⇒ x = y).
   - is-brother-of on all males → **symmetric** (every male is his own brother by formal definition); **not antisymmetric** (for distinct x, y, both brothers of each other).

### Check Your Progress 2 — Symmetric / Antisymmetric
1. {(1,1),(2,2),(3,3)} is **both symmetric and antisymmetric**.
2. {(1,2),(2,3),(1,3)} is **antisymmetric, not symmetric**.
3. {(1,2),(2,1),(1,3),(3,1)} is **symmetric, not antisymmetric** (since (1,2),(2,1) ∈ R but 1 ≠ 2).

### Check Your Progress 3 — Transitivity
- R defined by "angle between lines a and b = 30°" → **NOT transitive** (chain of two 30° angles can give 60° or 0°).
- ≤ on numbers → **transitive**.
- is-brother-of on all humans → **transitive**.

### Check Your Progress 4 — Independence of three properties
1. Each property is independent of the other two.
   - **Reflexive only** (not symmetric, not transitive): on Z, define (a,b) ∈ R iff 0 ≤ a − b < 1.
     - Reflexive: 0 = a − a < 1 ✓
     - Not symmetric: (4, 3) ∈ R since 0 ≤ 1 < 1... [OCR unclear — text reads "0 ≤ a − b < 1"; likely meant 0 ≤ a − b ≤ 1 or similar]; (3,4) ∉ R.
     - Not transitive: (4,3) ∈ R, (3,2) ∈ R, but (4,2) ∉ R since 4 − 2 = 2 ≥ 1.
   - **Symmetric only**: "is-perpendicular-to" on lines in a plane.
   - **Transitive only**: < on rationals (Q).
2. Partition of X = {1,2,3,4} from R = {(1,1),(2,2),(3,3),(4,4),(1,3),(3,1),(2,4),(4,2)}: equivalence classes are {1,3} and {2,4}, so partition = **{{1,3}, {2,4}}**.

### Check Your Progress 5 — Hasse Diagrams
| Set | Minimal | Maximal |
|---|---|---|
| Divisors of 30 | 1 | 30 |
| Divisors of 24 | 1 | 24 |
| Divisors of 60 | 1 | 60 |
| Divisors of 32 | 1 | 32 |

### Check Your Progress 6 — Functions
1. **(i) f(x) = −|x|**: Domain = R; Range = {x ∈ R : x ≤ 0} = (−∞, 0].
2. **(ii) f(x) = +√(9 − x²)**: Domain = [−3, 3] (so 9 − x² ≥ 0); Range = [0, 3].
   - Note: For complex-valued complex function f: C → C, range = domain = C.
3. f(x) = 2x − 5:
   - f(0) = −5
   - f(7) = 9
   - f(−3) = −11
4. **f: N → N, f(x) = x − 3**: not a function (f(0) = −3 ∉ N).
   - **f: N → Z, f(x) = x − 3**: is a function (image always lies in Z).

---

## Section: Unit 3 — End-of-Unit Exercises (Q1–Q7) 🔴

### Q1. Reflexivity classification
- (i) R = {(1,1),(2,2),(1,3),(2,3)} on X = {1,2,3}: (3,3) ∉ R → **not reflexive**; (1,1), (2,2) ∈ R → **not anti-reflexive**.
- (ii) is-brother-of on humans: **not reflexive** (fails for females); **not anti-reflexive** (holds for males).

### Q2. Symmetry classification (on X = {1,2,3})
- (i) {(1,1),(2,2),(3,3)} → **both symmetric and antisymmetric**.
- (ii) {(1,2),(2,3),(1,3)} → **antisymmetric, not symmetric**.
- (iii) {(1,2),(2,1),(1,3),(3,1)} → **symmetric, not antisymmetric**.

### Q3. Transitivity classification (on X = {1,2,3})
- (i) {(1,1),(2,2),(3,3)} → **transitive**.
- (ii) {(1,2),(2,3),(1,3)} → **transitive**.
- (iii) {(1,2),(2,1),(1,3),(3,1)} → **not transitive** ((1,2),(2,1) ∈ R but (1,1) ∉ R).

### Q4. Examples — properties independent
On {1,2,3}:
- (i) Reflexive + symmetric, not transitive: R = {(1,1),(2,2),(3,3),(1,2),(2,1),(1,3),(3,1)} — (2,1),(1,3) ∈ R but (2,3) ∉ R.
- (ii) Reflexive + transitive, not symmetric: R = {(1,1),(2,2),(3,3),(1,2),(1,3),(2,3)} — (2,3) ∈ R but (3,2) ∉ R.
- (iii) Symmetric + transitive, not reflexive: R = {(1,1),(2,2)} — (3,3) ∉ R.

### Q5. Hasse diagram for X = {1,2,3,...,10} under proper-divisor
- Minimal element = 1.
- Maximal elements = 5, 6, 7, 8, 9, 10 (no element of X strictly above any of them).

### Q6. f: Z → R, f(x) = x² — injective?
Suppose f(x₁) = f(x₂) ⇒ x₁² = x₂² ⇒ x₁ = ±x₂. So f(5) = f(−5) = 25 → **NOT injective**.

### Q7. f: C → R, f(x) = x² — surjective?
Take arbitrary x ∈ R; then √x ∈ C, and f(√x) = (√x)² = x. So every real x is hit → **surjective**.

> **Quick Recall:**
> - To prove **not injective**: produce one pair x ≠ y with f(x) = f(y).
> - To prove **surjective**: given y in codomain, exhibit x in domain with f(x) = y.

---

## Section: Unit 4 — Structure & Objectives 🟢

### Core Idea
Unit 4 ("Coordinate Geometry and Representation of Functions") teaches how to draw and interpret graphs of single- and two-variable functions. It uses Cartesian coordinates to translate algebraic equations into geometric pictures and vice versa, and surveys linear, non-linear, asymptotic, and piecewise function graphs.

### Unit 4 Objectives
After this unit, you should be able to:
1. Apply the **vertical line test** to identify a non-function.
2. Explain how **coordinate geometry** differs from conventional/synthetic geometry.
3. Obtain **algebraic equations** corresponding to simple geometric figures.
4. Graphically represent various types of functions of a single variable.
5. Handle graphs of two-variable functions at a preliminary level.

### Unit 4 Structure (sub-sections)
- 4.1 Introduction (4.1.1 Vertical Line Test; 4.1.2 Equation vs Function)
- 4.2 Coordinate Geometry (4.2.1 Cartesian Coordinate System; 4.2.2 Translating geometric figures to algebraic equations)
- 4.3 Linear Functions (4.3.1 Absolute Value; 4.3.2 Step Function)
- 4.4 Non-Linear Functions (Even/Odd, Quadratic, Cubic)
- 4.5 Asymptotic Functions (Square Root, Exponential, Logarithmic)
- 4.6 Piecewise Functions (Rational, Discontinuous — asymptotic / point / jump discontinuities)
- 4.7 Hyperbola & Parabola
- 4.8 Two-Variable Functions (Level Curves)

---

## Section: Vertical Line Test 🔴

### Core Idea
A graph in the (x, y) plane represents a function y = f(x) only if **no vertical line crosses the graph at more than one point**. The test is a quick way to detect failure of "single-valued output" — which is the defining property of a function.

> **In Simple Terms:** Drag a vertical ruler across the graph. If at any position it touches the graph in more than one place, the rule isn't a function — that x has multiple y's.

### Definitions
- **Vertical line test**: A relationship f(x) is NOT a function of x if some vertical line x = a meets the graph at two or more points.

### Examples
- The graph of x² + y² = 4 (a circle) **fails** the vertical line test (two y's for most x's) → not a function.
- The graph in Fig. 4.4 (a single curve passing the test) **is** a function.
- Important standard equations that are **not** functions of x: ellipses, circles, sideways parabolas (y² = 4ax).

### ⚠️ Common Mistakes
- ❌ Using the vertical line test to prove something IS a function → ✅ The test detects only failure. Passing the test plus being defined for every x in the domain is needed for it to be a function.

> **Quick Recall:**
> - Two intersection points with any vertical line ⇒ not a function.
> - Some equations like a circle look like nice curves but are NOT functions.

---

## Section: Equation vs Function — How to Tell 🔴

### Core Idea
An equation in x and y becomes a candidate for a function of x only after isolating y on the LHS with exponent 1. If the resulting expression assigns more than one y to some x, the equation defines a relation but not a function.

### Mechanisms / Processes
1. Start with the equation, e.g. X² + Y² = 4.
2. Isolate Y² (or whichever variable will be dependent): Y² = 4 − X².
3. Reduce LHS to power 1 by extracting a root: Y = ±√(4 − X²).
4. Check single-value rule:
   - If LHS gives one Y for each X → function.
   - If LHS gives multiple Y's (e.g., the ± above) → relation but NOT function.

### Examples
**Example: Circle**
1. X² + Y² = 4
2. Y² = 4 − X²
3. Y = ±√(4 − X²)

Two values of Y for most X (e.g., X = 0 → Y = +2 and Y = −2) ⇒ **not a function**, only a relation. The roles of X and Y can be swapped to make X the dependent variable; the conclusion is the same.

**Example: Sphere in 3D**
1. X² + Y² + Z² = 4
2. Z = ±√(4 − X² − Y²)

Z is determined up to a sign by X and Y → **not** a function of (X, Y).

### Edge Cases & Caveats
- Restricting the codomain (e.g., to non-negative reals) can convert a relation back into a function: Y = +√(4 − X²) is a function (the upper semicircle).
- Functions of more than one independent variable are allowed: Z = f(X, Y).

> **Quick Recall:**
> - Step 1: solve for the dependent variable.
> - Step 2: reduce its power to 1.
> - Step 3: check whether the result is single-valued.

### Connections
- Builds on function definition (Chunk 010: Hasse Diagrams & Special Elements of a Poset).
- Prerequisite for: graphing standard curves in 4.2.2 (Chunk 012: Coordinate Geometry — Big Picture & History).

### Open Questions
- For y² = x + 5, is this a function? (No — for any x > −5 there are two y values.)


---

<!-- Continuity: Continues Unit 4. Picks up Section 4.2 Coordinate Geometry (Cartesian system, translating figures to equations), then 4.3 Graphing Linear Functions (with absolute-value and step functions), and opens 4.4 Graphing Non-Linear Functions (even/odd, quadratic). Continues into chunk 013 with cubic, asymptotic, piecewise functions etc. -->

## Section: Coordinate Geometry — Big Picture & History 🟡

### Core Idea
**Coordinate geometry** (also called **analytical geometry** or **Cartesian geometry**) translates geometric objects into algebraic expressions using a coordinate system, then attacks geometric problems with algebraic tools. This contrasts with **synthetic geometry**, which proves results from axioms without coordinates.

> **In Simple Terms:** Instead of drawing and reasoning about shapes directly, label every point with numbers (coordinates) and reason about the numbers using algebra.

### Definitions
- **Coordinate / analytical / Cartesian geometry**: approach in which geometric objects (lines, planes, curves) are represented by algebraic equations, and problems are solved algebraically.
- **Synthetic geometry**: traditional axiomatic geometry (Euclidean style) using postulates and proofs without coordinates.

### Key Concepts
- Discipline named after **René Descartes** (17th-century French philosopher and mathematician); independently invented by **Pierre de Fermat** in the same century.
- Earlier traces in Greek mathematics and the work of 11th-century Persian mathematician **Omar Khayyam**.
- Other coordinate systems exist (polar, cylindrical, spherical, homogeneous, curvilinear) — each useful for specific problems.

---

## Section: Cartesian Coordinate System (2D) 🔴

### Core Idea
The 2D Cartesian (rectilinear) coordinate system uses two **mutually perpendicular** real number lines (axes) intersecting at the **origin**. Every point in the plane is uniquely identified by an ordered pair (x, y).

> **In Simple Terms:** Two perpendicular rulers, one horizontal and one vertical, meeting at zero. Any point's address is "(go x right, go y up)".

### Definitions
- **x-axis**: the horizontal number line. ⭐
- **y-axis**: the vertical number line. ⭐
- **Origin**: the intersection of the axes; both x = 0 and y = 0 there.
- **Quadrants**: four regions (numbered I, II, III, IV — usually with Roman numerals) bounded by the axes.
- **Abscissa**: the x-value of point P(x, y); perpendicular distance of P from the y-axis.
- **Ordinate**: the y-value of point P(x, y); perpendicular distance of P from the x-axis.
- **Coordinates of P**: the ordered pair (x, y).

### Key Concepts
- Convention: independent variable on the **horizontal** axis (x); dependent variable on the **vertical** axis (y).
- Order matters: x is **always** written first in the pair (x, y).
- Called "rectangular" because both axes use evenly-spaced scales.

### Examples
Points and their interpretations:
- (2, 3) — 2 right, 3 up (quadrant I).
- (−3, 1) — 3 left, 1 up (quadrant II).
- (−1.5, −2.5) — 1.5 left, 2.5 down (quadrant III).

> **Quick Recall:**
> - x first, y second.
> - Origin = (0, 0).
> - Abscissa = horizontal distance; ordinate = vertical distance.

### Connections
- Builds on real number line (Unit 1).
- Prerequisite for: graphing all functions (later sections).

---

## Section: Translating Geometric Figures to Algebraic Equations 🔴

### Core Idea
To convert a geometric figure into an algebraic equation, embed it in a coordinate system, take an arbitrary point P(x, y) on (or related to) the figure, and use the figure's geometric definition (similar triangles, distance, etc.) to derive an equation linking x and y.

### Mechanisms / Processes
1. Place the figure in a coordinate system; record coordinates of any "anchor" points.
2. Pick an arbitrary point P(x, y) on the figure.
3. Apply known geometric facts (similar triangles, Pythagoras, etc.).
4. Solve for the relation between x and y.

### Examples
**Example: Line through A(0, −2) and B(2, 0) (Fig 4.7)**
- Take P(x, y) outside segment AB; drop perpendicular PQ to x-axis at Q(x, 0).
- Triangles AOB and AQP are similar.
- |AO|/|AQ| = |BO|/|PQ|, i.e. 2/(x − 2) = 2/y.
- Cross-multiplying: 2y = 2(x − 2) ⇒ **y = x − 2**.

### Standard Algebraic Forms (memorize) ⭐

| Curve | Equation |
|---|---|
| Circle (centred at origin) | x² + y² = a² |
| Ellipse | (x/a)² + (y/b)² = 1 |
| Parabola | y² = 4ax (a > 0) |
| Hyperbola | (x/a)² − (y/b)² = 1 |
| Rectangular hyperbola | xy = c² |
| Sphere (3D) | (x − a)² + (y − b)² + (z − c)² = d², d > 0 |

> **Quick Recall:**
> - Circle: sum of squares = constant.
> - Ellipse: sum of normalized squares = 1.
> - Parabola (right-opening): y² = 4ax.
> - Hyperbola: difference of normalized squares = 1.

### Check Your Progress 1
Draw graph of y² = x + 5 and decide if it is a function.
**Hint:** y = ±√(x + 5). For each x > −5, two y-values exist → fails vertical line test → **NOT a function** (only a relation; specifically, a sideways parabola).

### Connections
- Builds on standard formulas from school geometry.
- Prerequisite for: graphing parabola, hyperbola, circle (Section 4.7).

---

## Section: Graphing Linear Functions 🔴

### Core Idea
A function y = f(x) is **linear** if x appears with power ≤ 1; it corresponds to a linear equation Ax + By + C = 0 where degrees of x and y are ≤ 1. The graph is always a **straight line** — and a straight line is determined by just two points.

### Definitions
- **Linear function**: y = f(x) where the highest power of x is 1.
- **Linear equation**: Ax + By + C = 0 with A, B, C constants and degrees of x, y at most 1.
- **t-chart**: a small table of (x, y) values used to plan a plot.
- **x-intercept**: point where graph crosses the x-axis (y = 0).
- **y-intercept**: point where graph crosses the y-axis (x = 0).

### Mechanisms / Processes
1. Pick any two values of x (often x = 0 and one other).
2. Compute corresponding y from y = f(x).
3. Plot the two points; draw a straight line through them.

For finding intercepts of Ax + By = C:
- **x-intercept**: set y = 0, solve for x.
- **y-intercept**: set x = 0, solve for y.

### Examples
**Example: y = 7 − 5x (t-chart)**

| x | y = 7 − 5x |
|---|---|
| −1 | 12 |
| 0 | 7 |
| 1 | 2 |
| 2 | −3 |
| 3 | −8 |

Only two points are strictly needed; e.g. x = −1 → y = 12 and x = 0 → y = 7 give the entire line.

**Example: 3x + 4y = 12 — find intercepts**
- x-intercept: y = 0 ⇒ 3x = 12 ⇒ x = 4 → point (4, 0).
- y-intercept: x = 0 ⇒ 4y = 12 ⇒ y = 3 → point (0, 3).
Plot (4, 0) and (0, 3); join with a line (Fig 4.9).

> **Quick Recall:**
> - Two points determine a line.
> - Intercept method: set the other variable = 0.

---

## Section: Absolute Value Function 🔴

### Core Idea
The absolute-value (modulus) function f(x) = |x| returns x without its sign, and splits into two linear pieces (one for x ≥ 0, one for x < 0). Its graph is a "V" — two straight rays meeting at a corner.

### Definitions
- **Absolute value**: |x| = x if x ≥ 0; |x| = −x if x < 0; |0| = 0.
- f(x) = |x| is defined piecewise:
  - y = x for x ≥ 0
  - y = −x for x < 0

### Examples
**Example: f(x) = |x|** — graph is a V with vertex at the origin (Fig 4.10).

**Example: f(x) = |x − 2|** (Fig 4.11)
- y-intercept: f(0) = |−2| = 2 → (0, 2).
- x-intercept: solve |x − 2| = 0 → x = 2 → (2, 0).
- Domain: all real numbers.
- Range: [0, ∞) (modulus is never negative).
- Graph: V-shape with vertex shifted to (2, 0).

### ⚠️ Common Mistakes
- ❌ Using the x-intercept / y-intercept method without checking that the line meets both axes → ✅ For f(x) = |x − 2|, equation y = 0 has solution x = 2 (the unique x-intercept), but the curve has only one y-intercept; intercept-only method may miss the V-corner.
- ❌ Forgetting the range is non-negative → ✅ |x| ≥ 0 always.

> **Quick Recall:**
> - |x| graph: V at the origin.
> - |x − a| graph: V at (a, 0).
> - Two linear pieces stitched at the corner.

---

## Section: Step Function (Greatest Integer Function) 🔴

### Core Idea
A **step function** (staircase function) is a piecewise function that takes constant values across adjacent intervals, jumping discretely from one constant to the next. It is **discontinuous** — you cannot draw it without lifting your pencil.

> **In Simple Terms:** Imagine a staircase: walk flat across each step, then suddenly jump up (or down) to the next.

### Definitions
- **Step / staircase function**: piecewise function whose pieces are all constants on adjacent intervals.

### Mechanisms / Processes (Floor / Greatest Integer)
1. For any real x, write x = Int-x + Fraction-x with 0 ≤ Fraction-x < 1.
2. Define f(x) = Int-x.

### Examples
- For x = 5.46: Int-x = 5, Fraction-x = 0.46 → f(5.46) = 5.
- For x = −3.87: Int-x = −4, Fraction-x = 0.13 → f(−3.87) = −4. (Note: floor of a negative non-integer rounds **down** to a more negative integer.)

**Domain**: union of all individual interval domains. **Range**: union of all output values across pieces.

### Edge Cases & Caveats
- The function is defined for all real x but is discontinuous at every integer.
- For piecewise functions in general, domain = union of all sub-domains; range = union of all sub-ranges.

### ⚠️ Common Mistakes
- ❌ Computing Int-x of −3.87 as −3 → ✅ It's −4 (the integer part rounded **down**).

> **Quick Recall:**
> - Step function = constant on each interval.
> - Discontinuous at every step jump.
> - Floor of negative: round more negative (−3.87 → −4).

### Check Your Progress 2
1. Graph y = (−5/3)x − 2 — straight line through (0, −2) and (3, −7).
2. Truck rental: Rs. 25 + Rs. 0.30/mile for 0–500 miles; Rs. 100 + Rs. 0.15/mile for >500 and <1000 miles. Step (piecewise) function:

   f(m) = { 25 + 0.30 m,   if 0 ≤ m ≤ 500
         { 100 + 0.15 m,  if 500 < m < 1000

---

## Section: Graphing Non-Linear Functions — Setup 🟡

### Core Idea
Non-linear functions (curves) require **more than two points** to graph reliably. Three points are usually still too few — the curvature can mislead. Plot a generous t-chart before sketching.

### ⚠️ Common Mistakes
- ❌ Plotting only 3 points of a quadratic and connecting them with straight lines → ✅ Use a denser t-chart (5–7 points spanning negative and positive x) and draw a smooth curve.

---

## Section: Even and Odd Functions 🔴

### Core Idea
Even and odd are **symmetry properties** of a function's graph. Even functions reflect across the **y-axis**; odd functions are symmetric about the **origin** (rotate 180° and you get the same picture).

> **In Simple Terms:** Even = mirror-image left-right. Odd = upside-down version of itself when flipped through the centre.

### Definitions
- **Even function**: f(−x) = f(x) for all x ∈ domain. ⭐ Graph is symmetric about the y-axis.
- **Odd function**: f(−x) = −f(x) for all x ∈ domain. ⭐ Graph is symmetric about the origin.

> **Note (chunk says even is "symmetric about origin"; this appears to be an OCR/textbook slip — the standard convention is even ↔ y-axis symmetry, odd ↔ origin symmetry, which is what the figures Fig 4.13 (even, y-axis symmetric) and Fig 4.14 (odd, origin symmetric) actually illustrate.)**

### Examples
- f(x) = x² is even: f(−3) = 9 = f(3).
- f(x) = x³ is odd: f(−3) = −27 = −f(3).
- f(x) = x³ − x is odd: f(−x) = −x³ + x = −(x³ − x) = −f(x).

### ⚠️ Common Mistakes
- ❌ Claiming a function is "either even or odd" → ✅ Most functions are neither (e.g., f(x) = x² + x).

> **Quick Recall:**
> - Even: f(−x) = f(x); y-axis mirror.
> - Odd: f(−x) = −f(x); origin (point) symmetry.

---

## Section: Quadratic Functions 🔴

### Core Idea
A **quadratic function** has the form f(x) = ax² + bx + c with a ≠ 0. Its graph is a **parabola** — opening upward if a > 0, downward if a < 0. The slope is not constant: as x grows by 1 the increase in y itself grows.

### Definitions
- **Quadratic function**: f(x) = ax² + bx + c with a ≠ 0.
- **Parabola**: the curve y = ax² + bx + c (or any rotation thereof).

### Examples
**Example: y = x² t-chart**

| x | −3 | −2 | −1 | 0 | 1 | 2 |
|---|---|---|---|---|---|---|
| y | 9 | 4 | 1 | 0 | 1 | 4 |

(Fig 4.15 shows the parabola.) As x increases by 1 starting at 0, y increases by 1, 3, 5, 7, ... (odd numbers — the differences increase). Same pattern as x decreases by 1 from 0.

### Key Concepts

| Sign of a | Parabola opens | Vertex is |
|---|---|---|
| a > 0 | upward | minimum |
| a < 0 | downward | maximum |

(See Fig 4.16.) Quadratic functions describe demand, cost, revenue, profit in microeconomics.

### ⚠️ Common Mistakes
- ❌ Connecting only three points of a parabola with straight segments → ✅ A parabola has continuously varying slope; plot more points and draw a smooth curve.
- ❌ Assuming "quadratic ⇒ symmetric about y-axis" → ✅ Only y = ax² is symmetric about the y-axis. The general y = ax² + bx + c is symmetric about the vertical line x = −b/(2a).

> **Quick Recall:**
> - Parabola: opens up if a > 0, down if a < 0.
> - Differences of y for unit steps in x form an arithmetic progression (odd numbers for y = x²).

### Connections
- Builds on basic algebra (factoring, completing the square — earlier units).
- Prerequisite for: vertex computation (Section 4.4.2.1, next chunk), conic sections (Section 4.7).

### Open Questions
- How do you locate the vertex of y = ax² + bx + c without graphing? (Answer: x = −b/(2a) — to be covered in chunk 013, Section 4.4.2.1 Computation of Vertex.)
- How does the parabola's "width" depend on a?


---

<!-- Continuity: Continues Unit 4 "Coordinate Geometry and Representation of Functions" from earlier chunks. Builds on quadratic graphs introduced in Section 4.4.2 (parabolas, vertex shifting). Extends into cubic functions (4.4.3), asymptotic functions (4.5), and piecewise/rational functions (4.6). -->

## Section: Vertex Shifting and Axis of Symmetry of Parabolas 🔴

### Core Idea
A parabola y = x² has its vertex at the origin (0,0). Replacing x with (x−h) and adding k shifts the vertex to (h, k); these shifts preserve the U-shape. The axis of symmetry is the vertical line x = h that splits the parabola into mirror halves. Understanding shifts lets us sketch any quadratic without re-plotting from scratch.

> **In Simple Terms:** Think of y = x² as a paper cup template. Adding a number outside the squared term moves the cup up/down; subtracting inside the squared term slides it sideways. The "spine" of the cup (axis of symmetry) is always a vertical line through its lowest (or highest) point.

### Key Concepts

#### Vertical Shift
- Graph of y = x² + 3: same shape as y = x², shifted **up 3 units**; vertex moves to (0, 3).

#### Horizontal Shift
- Graph of y = (x + 3)²: shape unchanged, shifted **left 3 units**; vertex (−3, 0).
- Graph of y = (x − 3)²: shifted **right 3 units**; vertex (3, 0).
- Note the counter-intuitive sign: (x + 3)² shifts LEFT, not right.

#### Combined Shift
- y = (x − 2)² + 1: vertex (2, 1); axis of symmetry x = 2.

| Function form | Vertex | Direction of opening |
|---|---|---|
| y = x² | (0,0) | Upward (a > 0) |
| y = x² + k | (0, k) | Upward |
| y = (x − h)² | (h, 0) | Upward |
| y = (x − h)² + k | (h, k) | Upward |
| y = a(x − h)² + k, a < 0 | (h, k) | Downward |

### Definitions
- **Vertex**: the lowest point on an upward-opening parabola, the highest point on a downward-opening one. ⭐
- **Axis of symmetry**: the vertical line x = h that divides the parabola into two mirror-image halves. ⭐

> **Quick Recall:**
> - Vertex of y = a(x−h)² + k is (h, k).
> - Axis of symmetry: x = h.
> - "+k" lifts up; "(x − h)" slides right by h.

---

## Section: Computing the Vertex of a Generic Quadratic 🔴

### Core Idea
For any quadratic y = ax² + bx + c, completing the square produces y = a[(x + b/2a)² + k]. The squared term equals zero at x = −b/2a, so the parabola attains its extremum there. This gives a closed-form formula for the vertex coordinate without graphing.

> **In Simple Terms:** Every quadratic, no matter how messy, has a simple "balance point" at x = −b/2a. Plug that x back in to find the y. That's the tip of the cup.

### Mechanisms / Processes
1. Start with y = ax² + bx + c.
2. Factor a: y = a[x² + (b/a)x + c/a].
3. Complete the square: y = a[(x + b/2a)² − (b/2a)² + c/a].
4. Replace the constant tail with k: y = a[(x + b/2a)² + k].
5. Minimum (a > 0) or maximum (a < 0) occurs when (x + b/2a)² = 0, i.e., **x = −b/2a**.
6. y-coordinate: substitute x = −b/2a back into the original equation.

### Examples

**Example: Vertex of y = 3x² + x − 2**

Identify a = 3, b = 1, c = −2.

x-coordinate: x = −b/(2a) = −1/(2·3) = **−1/6**.

y-coordinate: substitute x = −1/6:
y = 3(−1/6)² + (−1/6) − 2
   = 3·(1/36) − 1/6 − 2
   = 1/12 − 2/12 − 24/12
   = **−25/12**

Vertex: **(−1/6, −25/12)**.

T-chart for plotting:

| x | y = 3x² + x − 2 |
|---|---|
| −2 | 8 |
| −1 | 0 |
| 0 | −2 |
| 1 | 2 |
| 2 | 12 |

### ⚠️ Common Mistakes
- ❌ Using x = +b/2a → ✅ Use x = −b/2a (note the negative sign).
- ❌ Confusing "axis x = h" with "x-intercept" — the axis is a vertical line, not a point.

> **Quick Recall:**
> - Vertex x = −b/2a for y = ax² + bx + c.
> - Sign of a determines max (a < 0) vs min (a > 0).

---

## Section: Cubic Functions 🔴

### Core Idea
A cubic function has the form f(x) = ax³ + bx² + cx + d. Cubics matter in microeconomics for total cost curves. The basic cubic f(x) = x³ passes through the origin with one x-intercept at (0, 0); the graph rises to the right and falls to the left when the leading coefficient is positive.

> **In Simple Terms:** A cubic looks like an "S lying on its side". For x³, both the domain and the range are all real numbers — it stretches from −∞ to +∞ in both directions.

### Key Concepts

#### Tracing f(x) = x³
- **y-intercept**: (0, f(0)) = (0, 0).
- **x-intercept**: solve x³ = 0 → only (0, 0).
- **Domain**: all real numbers.
- **Range**: all real numbers (because leading coefficient is positive, graph goes up on right, down on left).
- **Symmetry**: f(−x) = −f(x), so f is odd; graph is symmetric about origin.

| x | f(x) = x³ |
|---|---|
| −2 | −8 |
| −1 | −1 |
| 0 | 0 |
| 1 | 1 |
| 2 | 8 |

### Connections
- Connects to economics: cubic total cost curves (TC = aQ³ + bQ² + cQ + d) appear in microeconomic production theory.
- Builds on: odd/even function classification (earlier chunks).

### Check Your Progress 3
1) **Draw the graph for y = x³ − 2x.** [Solution from answer key: an "S"-shaped curve passing through origin with two extrema.]

---

## Section: Graphs of Asymptotic Functions — Horizontal & Vertical Asymptotes 🔴

### Core Idea
An asymptote is a line that a graph approaches but never touches. Horizontal asymptotes appear when a fraction's numerator stays bounded while the denominator grows without bound. Vertical asymptotes appear where the denominator approaches zero. The simplest example is y = 1/x, which has both x = 0 (vertical) and y = 0 (horizontal) as asymptotes.

> **In Simple Terms:** An asymptote is like a "wall the graph keeps getting infinitely close to but never crashes into".

### Definitions
- **Asymptote**: a line that a curve approaches arbitrarily closely as it heads toward infinity. ⭐
- **Horizontal asymptote**: a horizontal line y = L the graph approaches as x → ±∞.
- **Vertical asymptote**: a vertical line x = a the graph approaches as y → ±∞.

### Examples

**Example: y = 1/x**
- As x → +∞, y → 0⁺ (gets values 1/2, 1/3, 1/10, 1/10000, never quite 0).
- As x → 0⁺, y → +∞.
- Horizontal asymptote: y = 0. Vertical asymptote: x = 0.

**Example: y = 4/(x − 2)**
- Horizontal asymptote: y = 0. Vertical asymptote: x = 2.
- As x → 2⁻, denominator → 0⁻, fraction → −∞.
- At x = 2 exactly, function is undefined (division by zero).
- As x → 2⁺, fraction → +∞.

### Edge Cases & Caveats
- A function can have only horizontal, only vertical, both, or neither.
- (i) y = 1/(x−2) for 0 < x < 2: only x = 2 (vertical asymptote).
- (ii) x = 1/(y−2) for 0 < y < 2: only y = 2 (horizontal asymptote).

> **Quick Recall:**
> - Horizontal asymptote = behaviour at infinity (y-value).
> - Vertical asymptote = where denominator vanishes (x-value).

---

## Section: Square Root, Exponential, and Logarithmic Functions 🔴

### Core Idea
Three building-block "asymptotic" functions appear repeatedly in economics: the square-root function f(x) = √x (used in isoclines), the natural exponential f(x) = eˣ (growth and compounding), and the logarithm f(x) = log_b x (the exponential's inverse). Each has a distinctive graph shape and well-defined domain/range constraints.

> **In Simple Terms:** Square root grows slowly forever; exponential explodes upward; logarithm rises slowly but never stops, hugging the y-axis on the way up.

### Key Concepts

#### Square Root Function: f(x) = √x
- **Domain/Range**: [0, ∞).
- **Intercept**: (0, 0).
- Neither even nor odd; **strictly increasing** on (0, ∞).
- **Economics use**: depicts an isocline (locus where iso-quants relate). Converges to a point where output is maximised and marginal product is zero.

#### Exponential Function: y = aˣ (general form), y = eˣ (natural)
- e ≈ 2.718281828 (Euler's number).
- **Domain**: (−∞, ∞). **Range**: (0, ∞).
- Graph never touches or goes below x-axis (y > 0 always).
- **Applications**: compound interest, population growth, GDP growth, inflation, carbon dating.

#### Logarithmic Function: y = log_b x
- Inverse of exponential: if y = bˣ = f(x), then x = log_b y = g(y), and f(g(y)) = y, g(f(x)) = x.
- **Conditions**: b > 0, b ≠ 1, x > 0.
- **Behaviour**: when b > 1, log values increase; when 0 < b < 1, they decrease.
- Slowly tends to +∞ as x → ∞; tends to −∞ as x → 0⁺.
- **Domain**: positive reals (never zero). **Range**: all real numbers.
- Graph is **asymptotic to the y-axis** (gets close but never touches).

#### Three Common Bases
| Base b | Name | Used in |
|---|---|---|
| 10 | Common (decimal) logarithm | Science, engineering |
| e ≈ 2.718 | Natural logarithm (ln) | Mathematics, physics |
| 2 | Binary logarithm | Computer science |

For all bases: **log_b 1 = 0**.

### Check Your Progress 4
1) **f(x) = (x+1)/(x−1). Find x and y intercepts.**
   - x-intercept: f(x) = 0 ⇒ x + 1 = 0 ⇒ x = −1. So (−1, 0).
   - y-intercept: f(0) = 1/(−1) = −1. So (0, −1).
2) **Average fixed cost (AFC) curve — why asymptotic?**
   - AFC = TFC/Q. Since TFC is constant, AFC steadily falls as Q increases but never reaches zero (asymptotic to x-axis).

> **Quick Recall:**
> - √x defined for x ≥ 0.
> - eˣ > 0 always; y = 0 is its horizontal asymptote.
> - log_b 1 = 0 for any valid base; log graph asymptotic to y-axis.

---

## Section: Rational Functions and Piecewise Functions 🟡

### Core Idea
A rational function is the ratio of two polynomials, y = g(x)/h(x), with h(x) ≠ 0. Its domain excludes any x making h(x) = 0; near those values vertical asymptotes appear. Piecewise functions are defined by different formulas on different sub-intervals of the domain — graphed piece by piece.

> **In Simple Terms:** Rational functions are "polynomial fractions" — domain restrictions and asymptotes come from forbidding division by zero. Piecewise functions are like a recipe with different rules in different pages of the cookbook.

### Definitions
- **Rational function**: f(x) = g(x)/h(x) where g, h are polynomials and h ≠ 0. ⭐
- **Piecewise function** (split function): a function defined by different equations on different parts of the domain. ⭐

### Examples

**Example: y = 1/x (rational)**

T-chart:

| x | f(x) |
|---|---|
| −4 | −0.25 |
| −2 | −0.5 |
| −1 | −1 |
| −0.1 | −10 |
| −0.01 | −100 |
| 0.01 | 100 |
| 0.1 | 10 |
| 1 | 1 |
| 2 | 0.5 |
| 4 | 0.25 |

Graph splits into **two pieces** (one in each of two opposite quadrants). No intercepts. Vertical asymptote x = 0; horizontal asymptote y = 0.

**Example: Piecewise**

y = { x² − 2 if x ≤ 1 ; −2x + 4 if x > 1 }

Build separate T-charts for each piece, then graph each on its own interval. The "break" is at x = 1.

| x | y = x² − 2 |
|---|---|
| −4 | 14 |
| −3 | 7 |
| −2 | 2 |
| −1 | −1 |
| 0 | −2 |
| 1 | −1 |

| x | y = −2x + 4 |
|---|---|
| 1 | 2 |
| 2 | 0 |
| 3 | −2 |
| 4 | −4 |

### ⚠️ Common Mistakes
- ❌ Forgetting to exclude x-values where the denominator vanishes from the domain.
- ❌ Plotting both pieces of a piecewise function on the wrong interval — always restrict each formula to its prescribed range.

### Edge Cases & Caveats
- For y = 1/x, neither numerator nor denominator can produce an intercept; both axes are asymptotes.
- Piecewise functions may or may not be continuous at the break-point (continuity discussed in chunk 014).

### Connections
- Builds on: function definition and domain restrictions (Unit 3, earlier chunks).
- Prerequisite for: discontinuous functions (chunk 014), hyperbolas (chunk 014).

### Open Questions
- Why exactly two branches for y = 1/x and not more?
- How do horizontal asymptotes relate to the degrees of numerator and denominator?


---

<!-- Continuity: Continues Unit 4. Builds directly on rational and piecewise functions from chunk 013 (Sections 4.6.1, 4.6.2 begin here) and asymptotes. Introduces conic-section graphs (4.7) and functions of two variables (4.8). -->

## Section: Continuous vs Discontinuous Functions 🔴

### Core Idea
A continuous function is a single unbroken curve — drawable in one stroke without lifting the pen. A discontinuous function has a break, and there are exactly **three types** of discontinuities: asymptotic, point, and jump. Identifying which type appears at a given x helps interpret behaviour for calculus, integration, and economic models.

> **In Simple Terms:** "Continuous" = pencil never leaves the page. "Discontinuous" = at some x, the graph either shoots to infinity (asymptotic), has a missing dot (point), or suddenly leaps to a new height (jump).

### Definitions
- **Continuous function**: a function whose graph can be drawn without lifting the pen. ⭐
- **Discontinuous function**: a function that does not vary continuously through some value(s) of the variable. ⭐

### Key Concepts: Three Types of Discontinuities

#### 1. Asymptotic Discontinuity 🔴
The graph shoots to ±∞ near a forbidden x-value (vertical asymptote).

**Example**: f(x) = (x+4) / [(x−1)(x+8)]. Domain excludes x = 1 and x = −8.

Values approaching x = 1:

| x | y |
|---|---|
| 0.25 | −0.687 |
| 0.5 | −1.059 |
| 0.75 | −2.171 |
| 1.0 | Undefined |
| 1.25 | 2.270 |
| 1.5 | 1.158 |
| 1.75 | 0.786 |

As x → 1⁻, y → −∞; as x → 1⁺, y → +∞. The dotted vertical line at x = 1 is the asymptote.

**Horizontal asymptotic example**: f(x) = 2x/(x + 4) has horizontal asymptote y = 2.

#### 2. Point Discontinuity 🔴
The graph is continuous except at a single point — a tiny "hole" in the curve.

**Example A** — value redefined:
f(x) = { 1 if x = 3 ; x² for all other real x }
Graph is x² everywhere except a single redefined point at x = 3 (or x = 1 in original text).

**Example B** — denominator-cancellable hole:
f(x) = x²(x − 2)/(x − 2). At x = 2: f(2) = 0/0 = undefined. Cancelling gives:
f(x) = { x² if x ≠ 2 ; undefined if x = 2 }
The function behaves like x² everywhere except at x = 2 where it is undefined.

#### 3. Jump Discontinuity 🔴
The two pieces of a piecewise function have **different values** at the joining x.

**Continuous piecewise (no jump)**:
f(x) = { x² if x ≤ 1 ; 2 − x if x > 1 }
At x = 1, both pieces give 1 → continuous.

**Jump example**:
f(x) = { x² if x ≤ 1 ; −x if x > 1 }
At x = 1: left piece → 1, right piece → −1. The graph "jumps" between branches.

### Examples

**Example: Detect all discontinuities**

f(x) = { (x + 4)/x if x < 2 ; x² + 1 if x ≥ 2 }

- **First branch**: has x in the denominator → asymptotic discontinuity at **x = 0**.
- **At x = 2**: left branch → (2 + 4)/2 = 3; right branch → 2² + 1 = 5. Different values → **jump discontinuity at x = 2**.
- No other discontinuities.

### ⚠️ Common Mistakes
- ❌ Calling all breaks "asymptotic" → ✅ Distinguish: asymptotic (→ ±∞), point (single hole), jump (finite leap).
- ❌ Forgetting to test denominators of every piece in piecewise functions.

### Check Your Progress 5
1) **Draw graph of f(x) = −x³ + 4.** [From answer key: write as ax³ + c with a = −1, c = 4. Reflect y = x³ across x-axis (because a = −1) and translate up 4 units.]

> **Quick Recall:**
> - 3 discontinuity types: asymptotic, point, jump.
> - Hole at x = a where g(x) = h(x)·(x − a) cancels.
> - Continuous if pieces of a piecewise function meet at the boundary.

---

## Section: Hyperbola — Equations, Vertices, Foci, Asymptotes 🔴

### Core Idea
A hyperbola is the locus of points whose **difference** of distances from two fixed foci is constant. It has two mirrored branches and comes in horizontal or vertical forms. Plotting requires identifying centre, vertices, foci, the helper rectangle, and the asymptotes through which the branches are guided.

> **In Simple Terms:** A hyperbola looks like two parabolas back-to-back. Imagine two satellites orbiting in opposite directions, never crossing certain diagonal "guide rails" (the asymptotes).

### Definitions
- **Hyperbola**: set of all points where the **difference** of distances to two fixed foci is constant. ⭐
- **Transverse axis**: axis of symmetry passing through both foci and the centre.
- **Conjugate axis**: axis of symmetry perpendicular to the transverse axis through the centre.
- **Vertices**: the two points where the hyperbola crosses its transverse axis.

### Standard Equations
- **Horizontal hyperbola**: (x − h)²/a² − (y − v)²/b² = 1
- **Vertical hyperbola**: (y − v)²/a² − (x − h)²/b² = 1

The **centre** is (h, v) for both; x and y switch places (along with h and v) between the two forms.

| Feature | Horizontal hyperbola | Vertical hyperbola |
|---|---|---|
| Transverse axis | y = v (horizontal) | x = h (vertical) |
| Conjugate axis | x = h | y = v |
| Vertices | (h ± a, v) | (h, v ± a) |
| Foci | (h ± F, v) | (h, v ± F) |

### Mechanisms / Processes

**Computing F (distance from centre to a focus):**
**a² + b² = F²** (so F = √(a² + b²)).

**Steps to graph a hyperbola:**
1. Mark the centre (h, v).
2. From centre, mark a-distance along transverse axis (vertices) and b-distance along conjugate axis.
3. Draw a rectangle with sides through these four points (parallel to x- and y-axes).
4. Draw the diagonals of the rectangle extended — these are the **asymptotes**.
5. Sketch each branch starting at a vertex, hugging the asymptotes farther out.

**Slopes of asymptotes**: m = ± a/b (the chunk text gives this for both vertical and horizontal cases — likely an OCR/typesetting issue; conventionally m = ± b/a for horizontal and m = ± a/b for vertical hyperbolas).

### Examples

**Example: (y − 3)²/16 − (x + 1)²/9 = 1** (vertical hyperbola)

- Centre: (h, v) = (−1, 3).
- a² = 16 ⇒ a = 4 (vertical direction, since under y).
- b² = 9 ⇒ b = 3 (horizontal direction).
- Vertices: (−1, 3 + 4) and (−1, 3 − 4) = **(−1, 7) and (−1, −1)**.
- Foci: a² + b² = F² ⇒ 16 + 9 = 25 ⇒ F = 5. Foci: (−1, 3 + 5) and (−1, 3 − 5) = **(−1, 8) and (−1, −2)**.

### Edge Cases & Caveats
- a may be greater than, less than, or equal to b (unlike an ellipse).
- The curves never cross the asymptotes.
- If the equation is not in standard form, **complete the square** to put it there before identifying parameters.

### Economics Applications
- **Portfolio theory / efficient frontiers**: combinations of risk and return often shaped as partial hyperbolas.
- **Production frontiers**: combinations of capital and labour producing a given output.

> **Quick Recall:**
> - F² = a² + b² (note: opposite of ellipse, where it's F² = a² − b²).
> - Vertices at distance a along transverse axis.
> - Asymptotes are the rectangle's diagonals extended.

---

## Section: Hyperbola vs Parabola 🟡

### Core Idea
Although both are conic sections, parabolas and hyperbolas have fundamentally different defining geometries: parabolas use a single focus and a directrix; hyperbolas use two foci. Parabolas all share the same essential shape (only scaled); hyperbolas can be of various shapes.

> **In Simple Terms:** A parabola is "one focus + one straight-line guide". A hyperbola is "two foci, with a constant difference rule".

### Comparison Table

| Feature | Parabola | Hyperbola |
|---|---|---|
| Definition | Locus of points equidistant from a fixed focus and a fixed directrix line | Locus of points where difference of distances to two foci is a positive constant |
| Number of foci | 1 | 2 |
| Standard equation (simple) | y² = x | xy = 1 |
| Shape variability | All parabolas same shape (only scaled) | Hyperbolas have different shapes |
| Arm behaviour at infinity | Two arms become parallel | Arms diverge (do not become parallel) |

### Definitions
- **Directrix**: line perpendicular to the axis of symmetry of a parabola.
- **Focus** (parabola): the fixed point referenced in the definition.

---

## Section: Rectangular Hyperbola 🔴

### Core Idea
A rectangular (or "equilateral") hyperbola is one whose asymptotes are perpendicular to each other (orthogonal). The simplest examples take the form y = 1/xⁿ, where n is a positive integer. These graphs have the coordinate axes as asymptotes (when n ≥ 1) and no intercepts.

> **In Simple Terms:** A rectangular hyperbola is the "ideal" hyperbola whose asymptotes meet at right angles — most cleanly seen as y = 1/x.

### Definitions
- **Rectangular hyperbola**: a hyperbola for which the asymptotes are perpendicular (orthogonal). ⭐

### Key Concepts

#### Two Types based on parity of n in y = 1/xⁿ
- **n = 2k + 1 (n odd)**: e.g., y = 1/x. Branches lie in opposite quadrants.
- **n even**: e.g., y = 1/x². Branches lie in the same upper half (both positive y when n = 2).

#### Properties of Rectangular Hyperbola y = 1/xⁿ
1. Vertical asymptote at x = 0.
2. Horizontal asymptote at y = 0.
3. No stationary points.
4. No intercepts (when axes are the asymptotes).
5. **n odd**: gradient always decreasing throughout defined x.
6. **n even**: gradient increasing for x < 0; decreasing for x > 0.

### Examples

**Example: Graph y = (x − 1)/(x + 1)**

- **Intercepts**: x = 0 ⇒ y = −1; y = 0 ⇒ x = 1. So (0, −1) and (1, 0).
- **Turning points**: none.
- **Asymptotes**: as x → ∞, y → 1 (horizontal asymptote y = 1). As y → ∞, x → −1 (vertical asymptote x = −1).
- **Gradient**: always increasing.

### Economics Applications
- Unitary price elasticity of demand (rectangular hyperbola demand curve).
- Average fixed cost (AFC) curve.
- Production transformation curve.
- Indifference map components.

### Check Your Progress 6
1) **Difference between hyperbola and rectangular hyperbola.**
   - A rectangular hyperbola is a special case of hyperbola in which the asymptotes are **orthogonal** (perpendicular). General hyperbolas have asymptotes that need not be perpendicular.
2) **Price elasticity of a rectangular-hyperbola-shaped demand curve?**
   - **Unitary** (= 1) at every point.
3) **Hint**: write the standard form of a hyperbola with a horizontal transverse axis.

> **Quick Recall:**
> - Rectangular hyperbola ⇔ asymptotes orthogonal.
> - y = 1/x ⇒ price elasticity = 1 (unitary) when used as demand curve.

---

## Section: Graphing Functions of Two Variables 🟡

### Core Idea
A function of two variables z = f(x, y) defines a **surface in three dimensions**. To visualise it on a 2D page, we use **contour lines** (level curves) — curves connecting all (x, y) values that produce the same z. This collapses 3D information into a 2D map, like geographical contour maps.

> **In Simple Terms:** A 3D surface is hard to draw on paper. So we slice it horizontally at fixed heights and project the slices down — that's a contour map.

### Definitions
- **Level curve (contour line)**: for a function f of two variables and a constant c, the set of pairs (x, y) such that f(x, y) = c. ⭐
- **Contour diagram (contour map)**: a 2D graph showing several level curves at various values of c.

### Examples

**Example: 3D graph of z = 2x² + 2y² − 4** — bowl-shaped (paraboloid) surface in 3D.

**Example (level curve)**: f(x, y) = x² + y².

The level curve for value 1 is x² + y² = 1, a circle of radius 1 centred at the origin.

### Connections
- Builds on: graphs of single-variable functions (earlier chunks).
- Prerequisite for: indifference curves, isoquants, Cobb-Douglas (chunk 015).

> **Quick Recall:**
> - z = f(x, y) ⇒ surface in 3D.
> - Level curve: f(x, y) = c (a constant). Different c values give different curves.
> - Economists' indifference curves and isoquants are level curves.


---

<!-- Continuity: Concludes Unit 4. Continues from chunk 014's introduction of level curves into economic interpretations (indifference curves, isoquants, Cobb-Douglas), then provides Section 4.9 (Sum Up), 4.10 (Key Words glossary), 4.11 (Check Your Progress answers), and starts Section 4.12 Exercises (Q1-Q5). -->

## Section: Economic Interpretation of Level Curves — Indifference Curves & Isoquants 🔴

### Core Idea
In economics, level curves of a **utility function** are called **indifference curves** (combinations of goods giving equal satisfaction); level curves of a **production function** are called **isoquants** (combinations of inputs producing equal output). A contour diagram of these curves at multiple constant values gives an indifference curve map or isoquant map — a workhorse visualisation tool in micro theory.

> **In Simple Terms:** When utility or production has two inputs, slicing the 3D surface horizontally gives concentric curves on a 2D map. Each curve = a "level of happiness" or a "level of output".

### Definitions
- **Indifference curve**: locus of (x, y) goods combinations giving the same utility (level curve of utility function). ⭐
- **Isoquant**: locus of (K, L) input combinations producing the same output (level curve of production function). ⭐
- **Indifference curve map**: a contour map of utility, showing several indifference curves at different utility levels.

### Examples

**Example: Cobb-Douglas Production Function**

P = 1.01 · L^0.75 · K^0.25

Where:
- P = monetary value of all goods produced
- K = total capital investment
- L = total labour force

**Interpretation of contour diagram:**
- Reducing labour requires **more capital investment** to maintain the same output (substitute machinery for missing labour).
- Increasing labour reduces the capital needed for the same output (labour does the work instead).
- Each curve represents one fixed value of P.

**Example: Level curves of f(x, y) = x² − y²**

Set c = x² − y².

**Case c = 0**: equation x² − y² = 0 factors as (x − y)(x + y) = 0, satisfied if y = x or y = −x. Level curve = **two crossing lines**.

**Case c ≠ 0**: rewrite as x²/c − y²/c = 1 — equation of a **hyperbola**.
- c > 0: hyperbolas open left/right.
- c < 0: hyperbolas open up/down.
- c = 1: x² − y² = 1.
- c = −1: y² − x² = 1.

### Edge Cases & Caveats
- A "level curve" need not be a curve at all — it's a **set**. For a constant function f(x, y) = 1, the level curve at value 1 is the entire plane (all (x, y)), and the level curve at value 2 is empty.

### Check Your Progress 7
1) **Meaning of level curve**: a curve in two dimensions on which the value of a function f(x, y) is a constant.
2) **Comment on level curves of f(x, y) = 1 for all (x, y).**
   - Since f equals 1 everywhere, the level curve for value 1 is **the entire xy-plane** (every point qualifies). The level curve for value 2 is **empty** (no point gives f = 2). For value 0 the level curve consists of the axes (per the answer-key figure). So level curves here are not "curves" in the usual sense.

> **Quick Recall:**
> - Indifference curve = level curve of utility function.
> - Isoquant = level curve of production function.
> - Cobb-Douglas: P = A·L^α·K^β with α + β = 1 in CRS form.

---

## Section: Unit 4 Summary — Let Us Sum Up 🟡

### Core Idea
Unit 4 covered (i) deriving algebraic equations from geometric figures, then (ii) the reverse — sketching graphs from algebraic functional relationships. The vertical line test was emphasised as the diagnostic for whether a relation is a function. Functions were grouped into five categories for graphing purposes; functions of two variables were introduced at the end via contour maps.

### Mechanisms / Processes — Five Categories of Graphs

| Group | Functions Covered |
|---|---|
| **Linear** | Linear, absolute value, step functions |
| **Curves** | Odd & even, quadratic, cubic |
| **Asymptotic** | Square root, exponential, logarithmic |
| **Pieces in xy-plane** | Rational, piecewise, discontinuous |
| **Curves with branches** | Hyperbola, rectangular hyperbola |
| **Two-variable** | (Final section) — contour maps |

### Connections
- The **vertical line test**: a relation is a function iff no vertical line cuts the graph more than once. Equations of circle and ellipse fail this test (so they are relations, not functions).
- Operational view: y = f(x), with x = independent variable from domain, y = dependent variable in range, plotted on rectangular Cartesian axes.

---

## Section: Key Words Glossary (Section 4.10) 🟡

### Definitions

- **Abscissa**: x-coordinate (horizontal) of a point in 2D system.
- **Ordinate**: y-coordinate (vertical) of a point.
- **Absolute Value Function**: gives the magnitude of a number, |x|.
- **Asymptote**: a line that a curve approaches as it heads to infinity.
- **Asymptotic Discontinuity**: graph approaches a point but never touches it (vertical/horizontal asymptote).
- **Axis of Symmetry**: line that divides a graph into mirror-image halves.
- **Cobb-Douglas Production Function**: production function describing output from two inputs (e.g., P = A·L^α·K^β).
- **Contour Diagram (contour map)**: 2D visualisation of a function of two variables via level curves.
- **Co-ordinates**: numbers determining a point's position relative to fixed references.
- **Cubic Function**: polynomial of degree 3.
- **Directrix**: line perpendicular to the axis of symmetry of a parabola.
- **Discontinuous Function**: does not vary continuously over some values of the variable.
- **Even Function**: f(x) = f(−x).
- **Exponential Function**: exp(x) = eˣ.
- **Hyperbola**: curve where the distances from any point to a fixed point (focus) and a fixed line (directrix) maintain a constant ratio.
- **Indifference Curve Map**: group of indifference curves showing different utility levels.
- **Isoquants**: graph of all input combinations producing a given output level.
- **Jump Discontinuity**: function jumps from one value to another at a point.
- **Level Curves**: 2D graph of f(x, y) at a constant value, plotted in xy-plane.
- **Logarithmic Function**: y = log_b x or y = ln x; inverse of exponential.
- **Odd Function**: f(−x) = −f(x).
- **Piecewise Function (split function)**: function defined in pieces over different intervals.
- **Point Discontinuity**: graph has a hole at x = a.
- **Polar Coordinates**: 2D system using distance r from origin and angle θ from a fixed direction.
- **Quadratic Function**: y = ax² + bx + c with a ≠ 0.
- **Rational Function**: ratio of two polynomials.
- **Rectangular Co-ordinate System**: two real number lines intersecting at right angles.
- **Rectangular Hyperbola**: hyperbola with perpendicular asymptotes.
- **Square Root Function**: maps non-negative reals to non-negative reals.
- **Step Function**: graph looks like a series of steps.
- **Vertex**: a "node" of a graph (here, the extreme point of a parabola).
- **Vertical Line Test**: if any vertical line intersects the graph more than once, the graph is not a function.

---

## Section: Check Your Progress 1–6 — Answers / Hints 🔴

### Check Your Progress 1
1) **Vertical line test on the figure**: many vertical lines hit the graph more than once → **not a function**.
2) **Algebraic equation of a circle**: place origin at centre, mark arbitrary point P = (x, y) on the circle, drop perpendicular to x-axis at Q. Then by Pythagoras: **x² + y² = r²**.

### Check Your Progress 2
1) **T-chart of y = (−5/3)x − 2:**

| x | y |
|---|---|
| −6 | 8 |
| −3 | 3 |
| 0 | −2 |
| 3 | −7 |

2) (Solving an equation): **x = 4/3 or x = −8/3**.
3) **Piecewise cost function**:
   f(x) = { 25 + 0.30x for 0 < x ≤ 500 ; 100 + 0.15x for 500 < x ≤ 1000 }

### Check Your Progress 3
1) Graph of y = x³ − 2x: an "S"-shaped cubic curve.
2) Cubic function shape: a curve like the letter "S".

### Check Your Progress 4
1) f(x) = (x + 1)/(x − 1).
   - x-intercept: x + 1 = 0 ⇒ x = −1 → **(−1, 0)**.
   - y-intercept: f(0) = 1/(−1) = −1 → **(0, −1)**.
2) **AFC asymptotic** because TFC is constant; AFC = TFC/Q steadily falls as Q rises but never becomes zero.

### Check Your Progress 5
1) **f(x) = −x³ + 4**: write as ax³ + c with a = −1, c = 4. Reflect y = x³ across the x-axis (because a = −1) and translate up 4 units.
2) The basic cubic function: y = x³.
3) **f(x) = 1/x**: discontinuous because f(0) is undefined (asymptotic discontinuity at x = 0).

### Check Your Progress 6
1) **Rectangular hyperbola** = hyperbola with **orthogonal (perpendicular) asymptotes**.
2) **Price elasticity** of rectangular-hyperbola demand = **unity (1)**.
3) Hint: write standard form with horizontal transverse axis.

### Check Your Progress 7
1) **Level curve**: a 2D curve where f(x, y) is constant.
2) For a constant function f(x, y) = 1: level curve at 1 = whole plane; at 2 = empty.

> **Quick Recall:**
> - x² + y² = r² for a circle of radius r centred at origin.
> - Vertical line test ⇒ relation is a function.
> - Reflect y = x³ across x-axis ⇒ y = −x³.

---

## Section: Exercises (Section 4.12) — Q1 to Q5 🔴

### Q1. Find vertex and intercepts of y = 3x² + x − 2; identify axis of symmetry.

**y-intercept**: x = 0 ⇒ y = 3(0)² + 0 − 2 = **−2**. So **(0, −2)**.

**x-intercepts**: solve 0 = 3x² + x − 2 → 0 = (3x − 2)(x + 1) → 3x − 2 = 0 or x + 1 = 0 → x = 2/3 or x = −1.
So **(−1, 0)** and **(2/3, 0)**.

**Vertex**: from earlier, x = −b/(2a) = −1/6; substituting gives y = −25/12. So vertex = **(−1/6, −25/12)**.

**Axis of symmetry**: vertical line through vertex, i.e., **x = −1/6**.

[Note: the original chunk text states "axis of symmetry is the line x = ⅙" — that appears to be an OCR sign error; the correct value is x = −1/6, halfway between the two x-intercepts at −1 and 2/3.]

### Q2. Graph y = x⁴ − 13x² + 36.

**Factoring**: y = (x + 3)(x − 3)(x + 2)(x − 2). Zeroes at x = −3, −2, 2, 3.

This is a **positive even-power polynomial** (degree 4) → both ends point upward.

T-chart:

| x | y = x⁴ − 13x² + 36 |
|---|---|
| −4 | 84 |
| −2.5 | −6.19 |
| −1 | 24 |
| 0 | 36 |
| 1 | 24 |
| 2.5 | −6.19 |
| 4 | 84 |

Curve has a "W" appearance with three turning points: maximum near x = 0, minima between the inner and outer roots.

### Q3. Quadratic y = x² − 6x + 5.

**Intercepts**: y = (x − 1)(x − 5) → x-intercepts at (1, 0) and (5, 0); y-intercept at (0, 5).

**Vertex**: x = −b/(2a) = 6/2 = 3. y = 9 − 18 + 5 = −4. So vertex = (3, −4).

| x | y |
|---|---|
| 0 | 5 |
| 1 | 0 |
| 3 | −4 |
| 5 | 0 |
| 6 | 5 |

Smile-shaped parabola opening upward.

[OCR note: chunk source displays "y = x² + 6x + 5" in the table header, but problem text says "y = x² − 6x + 5". The correct table values match y = x² − 6x + 5.]

### Q4. Graph f(x) = (x − 1)² + 3.

Vertex form: vertex at (1, 3), opening upward.

[OCR note: the source's evaluation table appears to mix multiple sub-questions — values shown ((−1, −7), (0, 0), (1, 1), (2, 2), (3, 9)) do not match (x − 1)² + 3, which would give f(0) = 4, f(1) = 3, f(2) = 4, etc. Treat the formula as authoritative; reconstruct your own table accordingly.]

### Q5. Sketch the piecewise function:

g(x) = { −x² + 4 if x ≤ 1 ; 2x if x > 1 }

[OCR note: the source spliced this with the next problem's piece "2x − 1 on x > 1". Use g(x) as written above.]

**Method**: draw each branch on its prescribed interval; mark x = 1 with care — for the upper branch use a closed dot only if x = 1 is included (yes here, since "x ≤ 1"). For the bottom branch (x > 1) use an open dot at x = 1 if the value at the boundary differs from the upper branch.

T-chart for −x² + 4 (x ≤ 1):

| x | y |
|---|---|
| −2 | 0 |
| −1 | 3 |
| 0 | 4 |
| 1 | 3 |

T-chart for 2x (x > 1):

| x | y |
|---|---|
| 2 | 4 |
| 3 | 6 |

### ⚠️ Common Mistakes
- ❌ Forgetting to mark whether the boundary point of a piecewise piece is included (closed dot) or excluded (open dot).
- ❌ Using axis of symmetry x = +b/2a instead of x = −b/2a.

### Connections
- Builds on: vertex formula and shifts (chunk 013), piecewise functions (chunk 013, 014).
- Prerequisite for: continued exercises (Q6 onwards in chunk 016).

### Open Questions
- Why does a positive even-power polynomial have both ends pointing the same way?
- For piecewise functions, when does redefining the boundary value remove a discontinuity?


---

<!-- Continuity: Closes Block-1, Unit 4. Continues Section 4.12 Exercises started in chunk 015 (Q5 piecewise overlap, Q6 three-piece function, Q7 hyperbola 9x²−16y²=144, Q8 rational function graphing). End-of-block matter. -->

## Section: Q5 (Continued) — Piecewise Function with Open/Closed Dot Convention 🔴

### Core Idea
When a piecewise function's two branches give different values at the boundary x, the convention is to use a **closed dot** for the branch that genuinely takes that value and an **open dot** for the other. This visually communicates the jump and prevents ambiguity about which branch "owns" the boundary point.

> **In Simple Terms:** At the joining x, only one of the two formulas gets to claim the actual point. Mark the winner with a filled circle, the loser with a hollow circle. The graph shows a small visual gap.

### Examples

**Example: g(x) = { −x² + 4 if x ≤ 1 ; 2x − 1 if x > 1 }**

T-chart for −x² + 4 on x ≤ 1:

| x | f(x) = −x² + 4 | (x, y) |
|---|---|---|
| −2 | 0 | (−2, 0) |
| −1 | 3 | (−1, 3) |
| 0 | 4 | (0, 4) |
| 1 | 3 | (1, 3) |

T-chart for 2x − 1 on x > 1:

| x | f(x) = 2x − 1 | (x, y) |
|---|---|---|
| 1 | 1 | (1, 1) |
| 2 | 3 | (2, 3) |
| 3 | 5 | (3, 5) |

**Plotting convention:**
- Upper branch (−x² + 4) at x = 1: closed dot at (1, 3) — because x ≤ 1 includes 1.
- Lower branch (2x − 1) at x = 1: **open dot** at (1, 1) — because x > 1 excludes 1; the formula is only "approached" there.

**Note**: the two pieces do not meet at x = 1 (one ends at y = 3, the other approaches y = 1) → there is a **visual blank space / jump** at x = 1.

### ⚠️ Common Mistakes
- ❌ Using closed dots on both branches at a non-shared boundary → ✅ Only one branch can include the boundary; use open dot for the other.

> **Quick Recall:**
> - "≤" and "≥" → closed dot.
> - "<" and ">" → open dot.

---

## Section: Q6 — Three-Piece Piecewise Function 🔴

### Core Idea
Piecewise functions can have three or more branches. The graphing process scales: build a T-chart per branch, evaluate **both endpoints** of each interval (so we know where to place open or closed dots), then assemble the full graph.

### Examples

**Example: h(x) = { x + 3 if x ≤ −2 ; x² if −2 < x ≤ 1 ; −x + 2 if x > 1 }**

[OCR note: source text shows "x ≤ 2" for the first branch, "if -2 < x < 1" middle, and "if x = 1" last — these signs are OCR-garbled. Reconstructed reasonable boundaries above based on the answer's evaluation table.]

The two outer branches are lines (only need two points). The middle branch is a parabola, so include extra points.

| Branch | x | y | Point |
|---|---|---|---|
| x + 3 | −3 | 0 | (−3, 0) |
| x + 3 | −2 | 1 | (−2, 1) |
| x² | −2 | 4 | (−2, 4) |
| x² | −1 | 1 | (−1, 1) |
| x² | 0 | 0 | (0, 0) |
| x² | 1 | 1 | (1, 1) |
| −x + 2 | 1 | 1 | (1, 1) |
| −x + 2 | 2 | 0 | (2, 0) |

**Closed/open dots**: at x = −2, the branches give 1 and 4 (jump). At x = 1, both x² and −x + 2 give 1 (continuous).

### Mechanisms / Processes
1. Identify each branch and its sub-domain.
2. T-chart for each branch including endpoints.
3. Place closed/open dots based on which branch includes the boundary.
4. Sketch each piece, joining or leaving gaps as the values dictate.

---

## Section: Q7 — Hyperbola 9x² − 16y² = 144 🔴

### Core Idea
A hyperbola in non-standard form must first be normalised by dividing through to make the right-hand side equal to 1. Then identify a, b, the foci (via a² + b² = F²), and the asymptotes (slopes ±b/a or ±a/b depending on orientation). Use these to sketch the curve.

### Mechanisms / Processes — Solution

**Step 1**: Divide both sides by 144:
9x²/144 − 16y²/144 = 1
⇒ x²/16 − y²/9 = 1
⇒ x²/4² − y²/3² = 1

This is a **horizontal hyperbola** with **a = 4** and **b = 3**.

**Step 2 — Intercepts**:
- **x-intercept**: set y = 0 → x²/4² = 1 → **x = ±4**. Points (4, 0) and (−4, 0).
- **y-intercept**: set x = 0 → −y²/9 = 1 → no real solution → **no y-intercept**.

**Step 3 — Foci**: F² = a² + b² = 16 + 9 = 25 → **F = 5**.
Foci at **(5, 0) and (−5, 0)**.

**Step 4 — Asymptotes**: y = ±(b/a)·x = **±(3/4)x**.

**Step 5 — Sketch**:
1. Plot asymptotes y = (3/4)x and y = −(3/4)x.
2. Plot vertices (±4, 0).
3. Use additional point: at x = 6, 9(36) − 16y² = 144 → −16y² = 144 − 324 = −180 → y² = 45/4 → y = ±3√5/2.
4. Draw branches starting at vertices, hugging asymptotes outward.

### ⚠️ Common Mistakes
- ❌ Forgetting to divide by 144 first → ✅ Always normalise to "= 1" form before reading a, b.
- ❌ Confusing F² = a² + b² (hyperbola) with F² = a² − b² (ellipse).

> **Quick Recall:**
> - Horizontal hyperbola: x²/a² − y²/b² = 1 → vertices (±a, 0), foci (±F, 0), F² = a² + b².
> - Asymptotes through origin: y = ±(b/a)x.

---

## Section: Q8 — Rational Function y = (2x² − 18)/(x² − 4) 🔴

### Core Idea
For a rational function whose graph involves both vertical and horizontal asymptotes, the standard procedure is: (i) find vertical asymptotes from denominator zeros, (ii) determine horizontal asymptote from leading-coefficient ratio (when degrees match), (iii) find x- and y-intercepts, (iv) plot extra points between intercepts and asymptotes for shape.

> **In Simple Terms:** First find all the "walls" (asymptotes) and "anchors" (intercepts), then fill in points to see how the curve bends between them.

### Mechanisms / Processes — Solution

**Step 1 — Vertical asymptotes**: denominator x² − 4 = 0 → x = ±2. So **vertical asymptotes at x = 2 and x = −2**.

**Step 2 — Horizontal asymptote**: degrees of numerator and denominator both = 2; ratio of leading coefficients = 2/1 = 2. So **horizontal asymptote at y = 2**.

**Step 3 — x-intercepts**: numerator 2x² − 18 = 0 → x² = 9 → **x = ±3**. Points (3, 0) and (−3, 0).

**Step 4 — y-intercept**: x = 0 → y = (0 − 18)/(0 − 4) = (−18)/(−4) = **4.5**. Point (0, 4.5).

**Step 5 — Additional points** (between intercepts and asymptotes for shape):

| x | y = (2x² − 18)/(x² − 4) |
|---|---|
| −5 | 1.5 |
| −2.5 | −2.4 |
| −1 | 5.3 |
| 1 | 5.3 |
| 2.5 | −2.4 |
| 5 | 1.5 |

**Shape**: three "branches" — left of x = −2, between x = −2 and x = 2, right of x = 2. The middle branch passes through (0, 4.5) and the outer branches approach y = 2 from below as |x| → ∞.

### ⚠️ Common Mistakes
- ❌ Skipping the asymptote step and directly tabulating values → ✅ Always identify asymptotes first; pick test points strategically near them.
- ❌ Plugging x = ±2 into a T-chart (undefined) → ✅ Mark these as vertical asymptotes, not as plot points.

> **Quick Recall:**
> - Vertical asymptote: where denominator = 0.
> - Horizontal asymptote (when num/denom degrees match): ratio of leading coefficients.
> - x-intercept: where numerator = 0 (and denominator ≠ 0).

---

## Section: End-of-Block Recap 🟢

### Core Idea
Chunk 016 closes Unit 4 (and Block 1) of MEC-203. Across Block 1 the student moved from set-theoretic foundations and number systems → relations and functions → coordinate geometry and graphing. The exercise set in chunks 015–016 ties together every graphing technique covered: vertex of quadratic, polynomial of degree 4, piecewise functions (two and three pieces), hyperbolas in non-standard form, and rational functions with both asymptote types.

### Connections
- This chunk completes Unit 4 of Block 1.
- Block 2 of MEC-203 typically continues into single-variable calculus (limits, differentiation), where:
  - Continuous vs discontinuous classification (chunk 014) becomes essential.
  - Asymptotic behaviour (chunks 013, 014) is formalised via limits.
  - Vertex/extremum reasoning (chunk 013) connects to first-derivative theory.

### Open Questions
- For Q8's rational function, can polynomial long division simplify the form to make the horizontal asymptote y = 2 obvious?
- How does the multi-branch hyperbola behaviour from Q7 generalise to multi-asymptote rational functions like Q8?

> **Quick Recall — Block 1 closing checklist:**
> - Plot quadratics via vertex (x = −b/2a).
> - Identify three discontinuity types.
> - Hyperbola: F² = a² + b²; asymptotes are diagonals of the helper rectangle.
> - Rational function pipeline: asymptotes → intercepts → fill points.
> - Always normalise conics to "= 1" form first.


---

