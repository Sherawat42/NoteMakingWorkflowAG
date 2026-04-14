# Chunk 010 — Axioms of Inequality Measures (Appendix to Unit 11)
<!-- Pages: 85-92 -->
<!-- Source: chunk_010.txt -->

---

## Section: Axioms of Inequality Measures 🔴
<!-- Appendix to Unit 11 - Measures of Inequality -->

### Core Idea

Beyond basic desirable statistical properties (simplicity, ease of computation, clear range), inequality measures must satisfy a set of **axioms** — intuitively appealing conditions about how inequality measures ought to behave. These axioms help evaluate and compare different inequality indices. Key axioms include: Scale Independence, Population Size Independence, Equal Income Addition, Pigou-Dalton Transfer Condition, Sen Transfer Condition, Symmetry, Interval Condition, and Decomposability.

> **In Simple Terms:** Axioms are like "fairness tests" for inequality measures. Before using an index, ask: Does it behave sensibly when all incomes double? When you transfer money from rich to poor? When you add the same pension to everyone? An index that fails too many axioms is not trustworthy.

### Key Concepts

#### General Desirable Properties of Any Statistical Measure

1. Simplicity of comprehension
2. Ease of computation
3. Clear range of variation
4. Minimum data requirements

The following are axioms **specific to inequality measures:**

---

#### 1. Axiom of Scale Independence ⭐

If every income is multiplied by a constant θ (proportional change — e.g., currency change, proportional tax), the measured inequality should not change.

**I(θx₁, θx₂, …, θxₙ) = I(x₁, x₂, …, xₙ)**

**Why it matters**: Inequality should be about **relative shares**, not absolute income levels.

**Example**: Changing units from rupees to paise should not change India's inequality level.

**Important corollary**: Equal proportional additions to all incomes don't change inequality (income shares unchanged → Lorenz curve unchanged → all Lorenz-based measures satisfy this axiom).

**Conflict with Dalton**: Dalton initially believed proportional additions should *reduce* inequality — this is wrong; proportional changes don't change income shares.

---

#### 2. Axiom of Population Size Independence ⭐

Inequality level is unchanged if a proportionate number of persons is added to each income level (population replication).

If we merge two economies of identical income distributions, the resulting combined economy should have the same inequality level.

**Also called**: Principle of Population Replication.

**Satisfied by**: All Lorenz-based measures (Lorenz curve unchanged when population proportions unchanged).

**Counter-intuitive example**: Replicating a two-person world (one with all income, one with none) yields a four-person world where each 50% group shares equally — some argue this changes the nature of inequality.

---

#### 3. Axiom of Equal Income Addition ⭐

If the same amount d is added to every income, measured inequality should **decrease** (since the poorer person's relative share increases):

**I(x₁+d, x₂+d, …, xₙ+d) < I(x₁, x₂, …, xₙ)**

Conversely, equal subtraction from all incomes (e.g., uniform tax) should increase measured inequality.

**Corresponds to**: Dalton's principle of equal additions to incomes.

---

#### 4. First Axiom of Income Transfer: Pigou-Dalton Condition ⭐

If income is transferred from a richer person to a poorer person (without reversing their relative order), measured inequality must **strictly decrease**:

- Transfer from person with income xₖ to person with income xⱼ (where xₖ > xⱼ)
- Transfer amount ≤ (xₖ − xⱼ)/2 (so rankings are preserved)
- Result: I(new distribution) < I(original distribution)

**This is the minimum requirement** for any sensible inequality measure.

**Named after**: Pigou (1912) and Dalton (1920) jointly.

**Also called**: Weak Transfer Axiom (specifies direction of change but not magnitude).

**Failure cases**: Relative Range and Relative Mean Deviation fail this condition (they are insensitive to transfers between non-extreme or within-mean recipients).

---

#### 5. Second Axiom of Income Transfer: Sen Condition ⭐

A transfer at a **lower income level** should have a **greater impact** on the inequality measure than an equal transfer at a higher income level.

**Example**: Transferring ₹100 from someone with ₹1000 to someone with ₹900 should reduce inequality *more* than transferring ₹100 from a person with ₹1,000,100 to a person with ₹1,000,000.

- This axiom implies the Pigou-Dalton condition (but is stricter)
- Measures satisfying Sen Condition automatically satisfy Pigou-Dalton
- Gini and Theil satisfy the Pigou-Dalton condition; SDL/log variance can fail both conditions

---

#### 6. Axiom of Symmetry ⭐

If income ranks are merely permuted (people swap incomes), inequality must not change:

**I(x_π₁, x_π₂, …, x_πₙ) = I(x₁, x₂, …, xₙ)** for any permutation π

**Implication**: Inequality depends only on the **frequency distribution** of incomes, not on which individual holds which income. The evaluator is impartial to non-income characteristics (gender, religion, caste, etc.).

---

#### 7. Axiom of Interval ⭐

The inequality measure should lie in the closed interval [0, 1]:
- Minimum value = **0** (all incomes equal: perfect equality)
- Maximum value = **1** (one person has all income: perfect inequality)

**Debate**: Theil and Cowell object — a 2-person society where one has everything vs. a 2-crore-person society where one has everything should not have the same inequality measure = 1.

**Working principle**: Measures with finite maxima can always be normalized to [0,1]. But normalization changes cardinal properties.

---

#### 8. Axiom of Decomposability ⭐

If the population is sub-divided into groups (by region, occupation, religion, etc.), the overall inequality index should be expressible as a consistent function of group-level inequalities:

**I(total) = f(I(group 1), I(group 2), …, weights)**

**Critical failure of Gini**: Gini is decomposable **only if groups are non-overlapping**. If groups overlap in income ranges, Gini can give paradoxical results. Cowell's experiment:
- Population A: (60,70,80) and (30,30,130) — group means same in A and B
- Population B: (60,60,90) and (10,60,120)
- Group inequalities in B > Group inequalities in A
- Yet **overall Gini in B < overall Gini in A** → paradox!

**Naturally decomposable**: Theil Entropy Index (can cleanly separate within-group and between-group components).

---

### Definitions

- **Pigou-Dalton Condition**: A transfer from a richer to a poorer person must strictly reduce the inequality measure (provided the transfer doesn't reverse income rankings). ⭐ (exam-important)
- **Sen Condition**: Transfer at a lower income level must have a greater inequality-reducing impact than an equal transfer at a higher level. ⭐ (exam-important)
- **Axiom of Scale Independence**: Inequality measure must be unchanged when all incomes are multiplied by a positive constant. ⭐ (exam-important)
- **Axiom of Decomposability**: Overall inequality can be expressed as a function of group-level inequalities; Theil satisfies this; Gini does not (when groups overlap). ⭐ (exam-important)
- **Population Replication**: Inequality unaffected by proportionate replication of all income groups.

### Mechanisms / Processes

**Axiom Satisfaction Summary by Major Measures:**

| Axiom | Relative Range | Gini | Theil | Atkinson |
|-------|---------------|------|-------|---------|
| Scale Independence | ✅ | ✅ | ✅ | ✅ |
| Population Independence | ✅ | ✅ | ✅ | ✅ |
| Equal Income Addition | ❌ | ✅ | ✅ | ✅ |
| Pigou-Dalton | ❌ | ✅ | ✅ | ✅ |
| Sen Condition | ❌ | Partially | ✅ | ✅ (with ε>0) |
| Symmetry | ✅ | ✅ | ✅ | ✅ |
| Interval [0,1] | No | ✅ | ❌ (logN) | ✅ |
| Decomposability | ❌ | Partial | ✅ | ❌ |

### ⚠️ Common Mistakes

- ❌ Mistake: Gini satisfies all axioms → ✅ Correct: Gini fails decomposability when groups overlap (Cowell's paradox)
- ❌ Mistake: SDL always satisfies Pigou-Dalton → ✅ Correct: SDL can violate Pigou-Dalton if the poor recipient's income exceeds 2.72μ

> **Quick Recall: 8 Axioms**
> 1. **Scale Independence**: All incomes × constant → no change
> 2. **Population Replication**: Proportionate cloning → no change
> 3. **Equal Income Addition**: Same d to all → inequality ↓
> 4. **Pigou-Dalton**: Rich → Poor transfer (rank-preserving) → I ↓
> 5. **Sen Condition**: Lower-end transfer → greater I reduction
> 6. **Symmetry**: Permuting incomes → no change
> 7. **Interval**: I ∈ [0, 1]
> 8. **Decomposability**: Overall = f(group inequalities) [Theil: ✅; Gini: ❌ when groups overlap]

### Connections

- Summarizes and synthesizes: All measures in Unit 11 (Chunks 007-009)
- Provides criteria for: Choosing which inequality measure to use in specific contexts
- Leads to: Unit 12 Composite Index (Chunks 011-013)
