# Chunk 005 — PPS-WR, Stratified Sampling, Cluster Sampling, Multi-Stage, Choice of Method
<!-- Pages: 42-51 -->
<!-- Source: chunk_005.txt -->
<!-- Continues from: Section: PPS Sampling (Chunk 004) -->
<!-- Continues into: Section: Measurement — Unit 8 (Chunk 006) -->

## Section: Sampling with PPS-WR (continued) 🔴
<!-- See Chunk 004 for start of PPS section -->

### Core Idea
For a pps-wr sample of size n > 1, the overall estimator of the population total is the average of n independent unbiased estimates (each yᵢ/pᵢ). The I-PSS technique can be used to get an unbiased estimate of V(Y*).

### Key Formulae (PPS-WR, n > 1)
| Quantity | Formula | Number |
|---------|---------|--------|
| Estimator of Y | Y*_pps-wr = (1/n)Σ(yᵢ/pᵢ) | 2.62 |
| V(Y*_pps-wr) | (1/n)[Σ(Yᵣ²/Pᵣ) – Y²] | 2.63 |
| V(m*_pps-wr) | (1/N²)(1/n)[Σ(Yᵣ²/Pᵣ) – Y²] | 2.64 |
| v(Y*_pps-wr) | [1/n(n–1)] Σ(yᵣ²/pᵣ² – nY*²) | 2.65 |

> **Quick Recall:**
> - PPS-WR estimator = average of (yᵢ/pᵢ) across n draws
> - V(Y*_pps) is small when Pᵢ ∝ Yᵢ (i.e., size variable X proportional to study variable Y)
> - Use I-PSS to estimate variance for complex designs

---

## Section: Stratified Sampling 🔴

### Core Idea
The population is divided into **k strata** (groups) of N₁, N₂, ..., Nₖ units. A separate random sample is drawn from each stratum. Estimates from individual strata are combined with weights (Wₛ = Nₛ/N) to estimate the population mean. Stratification reduces variance if strata are internally **homogeneous** (minimising within-stratum variation).

> **In Simple Terms:** Stratified sampling is like dividing a mixed bag of apples (red, green, yellow) into separate piles, sampling each pile independently, and then combining results with appropriate weights. The result is more precise because you're not letting one colour crowd out the others.

### Key Concepts

#### Formation of Strata
- **Key rule**: Units within a stratum should be as **homogeneous** as possible.
- This minimises within-stratum variance → minimises V(m_st).
- Equivalently, inter-strata (between-strata) variance should be maximised.

#### Estimators from Stratified Sampling
| Quantity | Formula | Number |
|---------|---------|--------|
| Stratified estimator of M | m_st = Σ Wₛmₛ = (1/N)Σ Nₛmₛ | 2.66 |
| V(m_st) | Σ Wₛ² V(mₛ) | 2.67 |
| Covariance between strata | Cov(mₛ, mᵣ) = 0 for s≠r | 2.68 |
| Estimator of Y | Y*_st = Σ Y*ₛ | 2.69 |
| V(Y*_st) | Σ V(Y*ₛ) | 2.70 |

#### Allocation of Sample Size Among Strata

**Proportional Allocation**: Allocate sample to each stratum in proportion to stratum size.
```
nₛ = n × (Nₛ/N)
```
- Appropriate when no additional information about strata is available.

**Optimum Allocation (Neyman / budget-constrained)**:
With fixed budget F = F₀ + Σnₛ Fₛ, the optimum stratum sample size is:
```
nₛ = [(F – F₀) × Wₛ√(Vₛ/Fₛ)] / [Σ Wₛ√(VₛFₛ)]   (Formula 2.71)
```
Where Vₛ = within-stratum variance, Fₛ = per-unit cost in stratum s.

Minimum variance achieved with optimum nₛ:
```
Min V(m_st) = [Σ Wₛ√(VₛFₛ)]² / (F – F₀)   (Formula 2.72)
```

### Definitions
- **Stratified Sampling**: Dividing the population into strata and drawing independent random samples from each stratum. ⭐ (exam-important)
- **Stratum**: A subgroup of the population; strata are mutually exclusive and exhaustive.
- **Proportional Allocation**: Allocating sample size to strata in proportion to their size (Nₛ).
- **Optimum Allocation**: Allocating sample to minimise V(m_st) subject to a budget constraint, proportional to Wₛ√(Vₛ/Fₛ).

> **Quick Recall:**
> - Stratified: k strata; independent samples from each; combine with weights Wₛ = Nₛ/N
> - m_st = Σ Wₛmₛ (unbiased for M)
> - V(m_st) ↓ when within-stratum homogeneity ↑
> - Proportional allocation: nₛ ∝ Nₛ; Optimum: nₛ ∝ Wₛ√(Vₛ/Fₛ)

### ⚠️ Common Mistakes
- ❌ Mistake: Strata should be heterogeneous internally → ✅ Correct: Strata should be internally homogeneous to minimise V(m_st). Between-strata differences should be maximised.
- ❌ Mistake: Proportional allocation is always optimal → ✅ Correct: Optimum allocation considers both variance and cost per unit (Vₛ and Fₛ). Proportional is only optimal when all strata have equal variance and cost.

---

## Section: Cluster Sampling 🔴

### Core Idea
Instead of selecting individual units, cluster sampling selects **groups (clusters)** of units and surveys **all units** within the selected clusters. Clusters are groups of neighbouring or conveniently co-located units. While operationally convenient (especially when a list of individuals is unavailable), cluster sampling is **less efficient** than direct individual sampling because units within clusters tend to be homogeneous.

> **In Simple Terms:** Cluster sampling is like randomly picking a few city blocks and then surveying every household in those blocks, instead of randomly picking individual households from the entire city. It's easier (you avoid travelling all over), but less precise (households in the same block tend to be similar).

### Key Concepts

#### Estimates from Cluster Sampling (Clusters of Equal Size K)
- Population of NK units divided into N clusters of K units each.
- Sample: one cluster selected by SRS.
- Cluster mean m_c-srs is unbiased estimator of M.
- **V(m_c-srs) = σ_b²** (variance *between* clusters)

#### Total variance decomposition:
```
σ² = σ_w² + σ_b²  (within-cluster + between-cluster variance)
```

#### Efficiency of Cluster Sampling vs. SRSWR
```
E_c/srswr > 1  if  σ_w² > (K–1)σ_b²
```
- Cluster sampling more efficient than SRSWR only if within-cluster variance > (K–1) × between-cluster variance.
- **In practice**: clusters are usually internally homogeneous → σ_b² > σ_w² → cluster sampling is generally **less efficient** than SRSWR.

### Definitions
- **Cluster Sampling**: Random selection of groups (clusters) of units; all units within selected clusters are surveyed. ⭐ (exam-important)
- **Within-cluster variance (σ_w²)**: Variance of units within the same cluster.
- **Between-cluster variance (σ_b²)**: Variance of cluster means around the overall mean = V(m_c-srs).

> **Quick Recall:**
> - Cluster sampling: sample clusters → survey all units in selected clusters
> - V(m_c-srs) = σ_b² (between-cluster variance)
> - Generally less efficient than SRSWR (within-cluster homogeneity → high σ_b²)
> - Operationally convenient when individual frame unavailable

### Edge Cases & Caveats
- Clusters overlapping (non-mutually exclusive) are possible but add complexity.
- Cluster sampling can use SRSWR, SRSWOR, systematic, pps, or stratified methods for selecting clusters.

---

## Section: Multi-Stage Sampling 🟡

### Core Idea
Multi-stage sampling resolves the efficiency-convenience trade-off of cluster sampling by introducing additional selection stages. First, select clusters (primary stage units); then within each selected cluster, select a sub-sample of units (secondary stage units). This is more efficient than pure cluster sampling and more operationally convenient than pure individual sampling.

> **In Simple Terms:** Multi-stage is like breaking data collection into a relay race: first pick districts, then tehsils within those districts, then villages, then households. Each stage refines the selection and utilises available information.

### Examples

**Two-Stage Sampling**:
- Stage 1 (FSU = clusters): Select a random sample of clusters (primary stage units).
- Stage 2 (SSU = individuals): Select a random sub-sample of individual units from each selected cluster.
- Efficiency: Better than cluster sampling, worse than direct individual sampling.

**Multi-Stage Rural Household Survey**:
- Stage 1: Districts (FSU)
- Stage 2: Tehsils/Taluks
- Stage 3: Villages
- Stage 4: Households (USU — Ultimate Stage Units)

Multi-stage estimates are built up stage by stage, using the sampling method appropriate to each stage.

### Definitions
- **Multi-Stage Sampling**: Sampling in two or more stages, selecting sub-samples from already-selected units at each stage.
- **Primary Stage Units (PSU/FSU)**: Clusters selected at the first stage (e.g., districts, factories).
- **Ultimate Stage Units (USU)**: The final units surveyed (e.g., households, workers).

---

## Section: Choice of Appropriate Sampling Method 🔴

### Core Idea
The choice of sampling design depends on four key considerations: (1) a priori information about the population, (2) precision of estimates, (3) operational convenience, and (4) cost. A structured decision framework exists.

> **In Simple Terms:** Choosing a sampling method is like choosing transportation: if you're going a short distance with no luggage, walk (SRSWR/SRSWOR). If you have luggage and stops to make, take a bus (stratified). If roads are bad and you need to be efficient, charter a helicopter (pps). The right choice depends on your destination, budget, and what you know about the route.

### Key Concepts

#### Decision Framework: 7 Situations

| Situation | Recommended Method | Reason |
|-----------|-------------------|--------|
| 1. No a priori information | SRSWOR preferred over SRSWR | V(m_srswor) < V(m_srswr); only when sampling fraction not too small |
| 2. No prior info, operational ease needed | Systematic Sampling | Only 1 random number; but avoid periodic populations |
| 3. Auxiliary variable X related to Y available | PPS | V(Y*) small when Pᵢ ∝ Yᵢ; pps-wr practical for large surveys |
| 4. Sub-population estimates needed, or heterogeneous universe | Stratified Sampling | Sub-universe estimates; freedom to choose design per stratum |
| 5. Frame of clusters available (not of individuals) | Cluster Sampling | Operational convenience; less efficient but unavoidable |
| 6. Clusters at multiple levels available | Two-Stage / Multi-Stage | Balance efficiency and convenience |
| 7. Complex design with variance estimation needed | Add I-PSS to any design | Unbiased V(m) for any design; also monitors fieldwork quality |

#### Most Recommended Set of Designs
- **SRSWOR** (baseline)
- **Stratified sampling with SRSWOR**
- **PPS-WR** (when auxiliary variable available)
- **Stratified sampling with PPS-WR**
- **+ I-PSS** (where possible for variance estimation)

> **Quick Recall:**
> - No info → SRSWOR > SRSWR; avoid systematic if periodicity
> - Auxiliary X ~ Y → PPS (pps-wr in practice)
> - Sub-groups needed → Stratified
> - No individual frame → Cluster → then upgrade to multi-stage
> - Complex design → add I-PSS for variance estimation

### Connections
- Builds on: SRSWR, SRSWOR (Chunk 004), PPS, Stratified, Cluster, Multi-Stage (this chunk)
- Builds on: Non-Random Sampling (Chunk 003) — contrasts by showing when each design is preferred
