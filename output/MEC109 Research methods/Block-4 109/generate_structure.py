import os

structures = {
    "003": """# Chunk 003 — Oblique Rotation & Factor Scores
<!-- Pages: 21-29 -->
<!-- Continues from: N/A -->
<!-- Continues into: N/A -->

## Section: Oblique Rotation 🟡
<!-- Exam importance: 🟡 MODERATE -->
<!-- Reason: Advanced rotation method, contrast with orthogonal -->

### Core Idea
<!-- placeholder -->

### In Simple Terms
<!-- placeholder -->

### Key Concepts
#### Oblique vs Orthogonal
<!-- placeholder -->

## Section: Factor Scores 🔴
<!-- Exam importance: 🔴 HIGH YIELD -->
<!-- Reason: Core concept of deriving factor values -->

### Core Idea
<!-- placeholder -->

### Definitions
- **Factor Scores**: <!-- placeholder -->

## Section: Methods for Estimating Factor Scores 🔴
<!-- Exam importance: 🔴 HIGH YIELD -->
<!-- Reason: OLS, WLS, Regression are fundamental methods -->

### Core Idea
<!-- placeholder -->

### Key Concepts
#### Ordinary Least Squares Method
<!-- placeholder -->

#### Weighted Least Squares Method
<!-- placeholder -->

#### Regression Method
<!-- placeholder -->

### Mechanisms / Processes
<!-- placeholder -->

### Quick Recall
<!-- placeholder -->
""",

    "004": """# Chunk 004 — Canonical Correlation Analysis Introduction
<!-- Pages: 30-39 -->
<!-- Continues from: N/A -->
<!-- Continues into: N/A -->

## Section: Canonical Correlation Analysis (CCA) 🔴
<!-- Exam importance: 🔴 HIGH YIELD -->
<!-- Reason: Introduction to a major topic covering Unit 14 -->

### Core Idea
<!-- placeholder -->

### In Simple Terms
<!-- placeholder -->

### Key Concepts
#### Purpose of CCA
<!-- placeholder -->

### Definitions
- **Canonical Correlation Analysis**: <!-- placeholder -->

## Section: Assumptions of Canonical Correlation 🟡
<!-- Exam importance: 🟡 MODERATE -->
<!-- Reason: Important for application -->

### Core Idea
<!-- placeholder -->

### Quick Recall
<!-- placeholder -->

## Section: CCA as Generalization of Multiple Regression 🔴
<!-- Exam importance: 🔴 HIGH YIELD -->
<!-- Reason: Connects two major concepts -->

### Core Idea
<!-- placeholder -->

### Connections
<!-- placeholder -->

## Section: Steps and Procedure of CCA 🔴
<!-- Exam importance: 🔴 HIGH YIELD -->
<!-- Reason: Practical application steps -->

### Mechanisms / Processes
<!-- placeholder -->

## Section: Illustration of CCA 🟢
<!-- Exam importance: 🟢 CONTEXT -->
<!-- Reason: Example application -->

### Examples
<!-- placeholder -->

## Section: Interpretation & Limitations of CCA 🔴
<!-- Exam importance: 🔴 HIGH YIELD -->
<!-- Reason: How to analyze the output and know its bounds -->

### Core Idea
<!-- placeholder -->

### Edge Cases & Caveats
<!-- placeholder -->
""",

    "005": """# Chunk 005 — Cluster Analysis Introduction
<!-- Pages: 40-49 -->
<!-- Continues from: N/A -->
<!-- Continues into: N/A -->

## Section: Cluster Analysis Concept and Meaning 🔴
<!-- Exam importance: 🔴 HIGH YIELD -->
<!-- Reason: Introduction to Unit 15 core topic -->

### Core Idea
<!-- placeholder -->

### In Simple Terms
<!-- placeholder -->

### Definitions
- **Cluster Analysis**: <!-- placeholder -->

## Section: Steps and Algorithm in Cluster Analysis 🔴
<!-- Exam importance: 🔴 HIGH YIELD -->
<!-- Reason: Procedural knowledge -->

### Mechanisms / Processes
<!-- placeholder -->

## Section: Methods of Cluster Analysis 🟡
<!-- Exam importance: 🟡 MODERATE -->
<!-- Reason: Categorization of approaches -->

### Core Idea
<!-- placeholder -->

## Section: Partitioning Clustering Methods 🔴
<!-- Exam importance: 🔴 HIGH YIELD -->
<!-- Reason: Core clustering method (k-means) -->

### Core Idea
<!-- placeholder -->

### Key Concepts
#### K-means algorithm
<!-- placeholder -->

## Section: Hierarchical Clustering Methods 🔴
<!-- Exam importance: 🔴 HIGH YIELD -->
<!-- Reason: Alternative primary clustering method -->

### Core Idea
<!-- placeholder -->

### Key Concepts
#### Agglomerative vs Divisive
<!-- placeholder -->

### Connections
<!-- placeholder -->
""",

    "006": """# Chunk 006 — Advanced Cluster Analysis & Correspondence Analysis
<!-- Pages: 50-59 -->
<!-- Continues from: hierarchical methods -->
<!-- Continues into: N/A -->

## Section: Other Approaches: Two-Step Cluster Analysis 🟡
<!-- Exam importance: 🟡 MODERATE -->
<!-- Reason: Secondary clustering approach -->

### Core Idea
<!-- placeholder -->

## Section: Interpretation of Cluster Results 🔴
<!-- Exam importance: 🔴 HIGH YIELD -->
<!-- Reason: Final part of cluster analysis evaluation -->

### Core Idea
<!-- placeholder -->

### Edge Cases & Caveats
<!-- placeholder -->

## Section: Correspondence Analysis Concept and Features 🔴
<!-- Exam importance: 🔴 HIGH YIELD -->
<!-- Reason: Introduction to Unit 16 core topic -->

### Core Idea
<!-- placeholder -->

### In Simple Terms
<!-- placeholder -->

### Definitions
- **Correspondence Analysis**: <!-- placeholder -->
""",

    "007": """# Chunk 007 — Correspondence Analysis Mechanisms
<!-- Pages: 60-69 -->
<!-- Continues from: N/A -->
<!-- Continues into: N/A -->

## Section: Steps and Algorithm in Correspondence Analysis 🔴
<!-- Exam importance: 🔴 HIGH YIELD -->
<!-- Reason: Methodological steps -->

### Mechanisms / Processes
<!-- placeholder -->

## Section: Basic Concepts and Definitions of CA 🔴
<!-- Exam importance: 🔴 HIGH YIELD -->
<!-- Reason: Mathematical and terminological foundations -->

### Definitions
- **Primitive Matrix**: <!-- placeholder -->
- **Profiles**: <!-- placeholder -->
- **Masses**: <!-- placeholder -->
- **Correspondence Matrix**: <!-- placeholder -->
- **Augmented Correspondence Matrix**: <!-- placeholder -->
- **Inertia**: <!-- placeholder -->
- **Distance**: <!-- placeholder -->

## Section: Biplots & Interpretation 🟡
<!-- Exam importance: 🟡 MODERATE -->
<!-- Reason: Visualisation and analysis reading -->

### Core Idea
<!-- placeholder -->

## Section: Multiple Correspondence Analysis 🟡
<!-- Exam importance: 🟡 MODERATE -->
<!-- Reason: Extension of basic CA -->

### Core Idea
<!-- placeholder -->
""",

    "008": """# Chunk 008 — Structural Equation Modeling Introduction
<!-- Pages: 70-79 -->
<!-- Continues from: N/A -->
<!-- Continues into: N/A -->

## Section: Structural Equation Modelling (SEM) Concept 🔴
<!-- Exam importance: 🔴 HIGH YIELD -->
<!-- Reason: Core topic of Unit 17 -->

### Core Idea
<!-- placeholder -->

### In Simple Terms
<!-- placeholder -->

### Definitions
- **Structural Equation Modeling (SEM)**: <!-- placeholder -->

## Section: Why conduct SEM? 🟡
<!-- Exam importance: 🟡 MODERATE -->
<!-- Reason: Purpose and use cases -->

### Core Idea
<!-- placeholder -->

## Section: Assumptions of SEM 🔴
<!-- Exam importance: 🔴 HIGH YIELD -->
<!-- Reason: Pre-requisites for SEM validity -->

### Core Idea
<!-- placeholder -->

### Quick Recall
<!-- placeholder -->
""",

    "009": """# Chunk 009 — SEM Methodology & Specification
<!-- Pages: 80-89 -->
<!-- Continues from: N/A -->
<!-- Continues into: N/A -->

## Section: Differences & Similarities with Traditional Methods 🟡
<!-- Exam importance: 🟡 MODERATE -->
<!-- Reason: Placing SEM in context of other statistical tools -->

### Key Concepts
#### Traditional vs SEM
<!-- placeholder -->

## Section: Concepts and Terminology used in SEM 🔴
<!-- Exam importance: 🔴 HIGH YIELD -->
<!-- Reason: Essential vocabulary like path diagrams -->

### Definitions
- **Path Diagram**: <!-- placeholder -->
- **Latent Variable**: <!-- placeholder -->

## Section: SEM Models Specification 🔴
<!-- Exam importance: 🔴 HIGH YIELD -->
<!-- Reason: Reflective vs Formative models are key -->

### Key Concepts
#### Reflective Indicators
<!-- placeholder -->

#### Formative Indicators
<!-- placeholder -->

## Section: Issues in SEM Technique 🟡
<!-- Exam importance: 🟡 MODERATE -->
<!-- Reason: Sample size, missing data, normality -->

### Edge Cases & Caveats
<!-- placeholder -->

## Section: Steps in SEM (Initial Spec & Estimation) 🔴
<!-- Exam importance: 🔴 HIGH YIELD -->
<!-- Reason: First stages of SEM execution -->

### Mechanisms / Processes
<!-- placeholder -->
""",

    "010": """# Chunk 010 — SEM Evaluation & Examples
<!-- Pages: 90-99 -->
<!-- Continues from: Steps in SEM -->
<!-- Continues into: N/A -->

## Section: Steps in SEM (Evaluation, Modification, Reporting) 🔴
<!-- Exam importance: 🔴 HIGH YIELD -->
<!-- Reason: Final stages of SEM execution -->

### Mechanisms / Processes
<!-- placeholder -->

## Section: Example of SEM 🟢
<!-- Exam importance: 🟢 CONTEXT -->
<!-- Reason: Illustrates SEM computation -->

### Examples
<!-- placeholder -->

## Section: Software Programs for SEM 🟢
<!-- Exam importance: 🟢 CONTEXT -->
<!-- Reason: LISREL, EQS, Mplus, Amos -->

### Core Idea
<!-- placeholder -->

## Section: Advantages and Disadvantages of SEM 🟡
<!-- Exam importance: 🟡 MODERATE -->
<!-- Reason: Pros and cons summary -->

### Quick Recall
<!-- placeholder -->
""",

    "011": """# Chunk 011 — SEM Wrap-up
<!-- Pages: 100-103 -->
<!-- Continues from: Advantages/Disadvantages -->
<!-- Continues into: N/A -->

## Section: SEM Wrap-up 🟢
<!-- Exam importance: 🟢 CONTEXT -->
<!-- Reason: Final remarks and disadvantage continuations -->

### Core Idea
<!-- placeholder -->

### Quick Recall
<!-- placeholder -->
"""
}

for chunk_num, content in structures.items():
    with open(f"notes/chunk_{chunk_num}_structure.md", "w") as f:
        f.write(content)

