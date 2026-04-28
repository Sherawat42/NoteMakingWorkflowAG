# Chunk 009 — Properties of Relations: Reflexive, Symmetric, Transitive & Equivalence/Partial Order
<!-- Pages: 81-90 -->
<!-- Source: chunk_009.txt -->
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
- Builds on relation definition (Chunk 008).
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
- Prerequisite for: Hasse diagrams (Chunk 010), lattices, order theory.

### Open Questions
- For a relation that is reflexive and antisymmetric but not transitive, is the resulting graph a poset? (No — transitivity is required.)
- How many distinct partial orders exist on a 3-element set?
