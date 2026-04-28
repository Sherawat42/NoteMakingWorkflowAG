# Chunk 008 — Mathematical Induction, Proof of Equivalences, and Start of Unit 3 (Relations and Functions)
<!-- Pages: 71-80 -->
<!-- Source: chunk_008.txt -->

## Section: Appendix V — Proof by Mathematical Induction 🔴
<!-- Continues from: Appendix Proof Techniques I-IV (Chunk 007) -->

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
- Builds on: Direct proof, Section I (Chunk 007).
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
- Builds on: Direct proof, Contradiction, Contrapositive (Chunk 007).

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
