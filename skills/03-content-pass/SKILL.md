---
name: content-pass
description: >
  Fill the notes structure with detailed content for each PDF chunk.
  Use when the user asks to "fill the notes", "add content", "run pass 2",
  "run the content pass", or after the structure pass has completed.
---

# Content Pass — Fill Structure with Content (Pass 2)

This skill takes the structure outlines from Pass 1 and fills them with **detailed, 
substantive content** extracted from the original PDF chunks. This is NOT summarization —
the goal is to create comprehensive notes that capture the full depth of the source material.

This is the **third step** in the PDF-to-Notes pipeline.

## Prerequisites

- PDF has been split using `01-split-pdf`
- Structure Pass (`02-structure-pass`) has been completed
- All `chunk_*_structure.md` files exist in `<working_dir>/notes/`

## Instructions

### Step 1: Load the Index and Verify Readiness

1. Read `<working_dir>/index.json`
2. Verify all `chunk_*_structure.md` files exist in `notes/`
3. Read `notes/structure_index.md` to understand the overall section flow

### Step 2: Process Each Chunk (Sequential, With Context)

For each chunk `i` (from 1 to total_chunks), do the following:

#### 2a. Load Required Files

| File | Purpose | Required? |
|------|---------|-----------|
| `notes/chunk_{i-1}_notes.md` | Previous chunk's **completed notes** — for continuity and avoiding repetition | Only if i > 1 |
| `chunks/chunk_{i}.txt` | Current chunk's **source text** — ground truth | Always |
| `notes/chunk_{i}_structure.md` | Current chunk's **structure** — the outline to fill | Always |

**Important**: Use the previous chunk's COMPLETED notes (not structure) for context.
This ensures content builds on what has already been written.

#### 2b. Fill Each Section

For every section and subsection in the structure file, replace the `<!-- placeholder -->` 
comments with actual content. Follow these rules:

##### Exam Importance Markers

Every `## Section` heading MUST include an **exam importance tag** based on how
likely the topic is to appear in exams. Determine importance by looking for these signals
in the source text:

| Marker | Meaning | When to use |
|--------|---------|-------------|
| 🔴 **HIGH YIELD** | Very likely in exams | Core theories, named laws/models, derivations the text emphasizes, topics with Check Your Progress questions |
| 🟡 **MODERATE** | May appear in exams | Supporting concepts, secondary mechanisms, elaborations on core topics |
| 🟢 **CONTEXT** | Unlikely as a direct question | Historical background, introductory material, administrative content |

**Signals of high exam importance:**
- The text has "Check Your Progress" exercises on the topic
- The topic is a named model, law, or theorem (e.g., Say's Law, IS-LM, Multiplier)
- The text includes equations or derivations
- The topic is mentioned in the unit's Objectives or Summary
- Multiple pages are devoted to it

Format: `## Section: [Title] 🔴` or `## Section: [Title] 🟡`

##### Core Idea
- Write 2-4 sentences capturing the main idea
- This should stand alone — a reader should understand the topic from this alone
- Do NOT copy-paste from the source; rephrase in clear, precise language

##### In Simple Terms (NEW)
- After the Core Idea, add a `> **In Simple Terms:**` blockquote
- Explain the concept as if talking to a friend who has never studied economics
- Use everyday analogies, plain language, and relatable examples
- Keep it to 1-3 sentences
- Example: `> **In Simple Terms:** The multiplier is like a ripple effect — when the government spends ₹100, it doesn't just add ₹100 to the economy. That money gets spent again and again, creating a much larger total impact.`

##### Key Concepts
- For each concept, write a **paragraph** (3-6 sentences) explaining:
  - What it is
  - Why it matters
  - How it relates to the broader topic
- Use the source text as the authority — do NOT hallucinate details
- **Use tables for comparisons** — whenever two or more concepts are being contrasted
  (e.g., Classical vs Keynesian, fiscal vs monetary policy), use a comparison table
  instead of separate paragraphs

##### Definitions
- Provide **precise definitions** from the text
- If the text gives a formal definition, preserve its precision
- Add a brief clarifying sentence if the definition uses jargon
- Mark definitions that are likely exam questions with: `⭐ (exam-important)`

##### Mechanisms / Processes
- Describe step-by-step if the source does
- Use numbered lists for sequential processes
- Include any conditions, inputs, outputs mentioned
- For causal chains, use arrow notation: `A → B → C → D` to make the
  logic flow visually clear

##### Examples
- Reproduce examples from the text with clear context
- Explain what each example demonstrates
- If the text gives numerical examples, include the numbers
- **Add worked-through calculations** — don't just state the formula,
  show the step-by-step computation so students can follow along

##### Quick Recall Box (NEW)
- At the end of each major section, add a `> **Quick Recall:**` blockquote
- Summarize the 3-5 most important takeaways from the section in bullet points
- These should be the facts a student would want to memorize the night before an exam
- Example:
  ```
  > **Quick Recall:**
  > - Multiplier = 1/(1-MPC)
  > - Higher MPC → larger multiplier
  > - Tax multiplier is always smaller than spending multiplier
  > - Balanced budget multiplier = 1 (always)
  ```

##### Common Mistakes (NEW)
- If the topic is one where students commonly get confused, add a
  `### ⚠️ Common Mistakes` subsection
- List 2-3 typical errors students make, with the correct understanding
- Format: `- ❌ Mistake: ... → ✅ Correct: ...`

##### Edge Cases & Caveats
- Note any exceptions, limitations, or warnings from the text
- Include "gotchas" that a learner might miss
- If the source says "commonly confused with...", capture that

##### Connections
- Reference specific other sections by name
- Explain the nature of the connection:
  - "builds on [Section X]"
  - "contrasts with [Section Y]"
  - "is a prerequisite for [Section Z]"
- Reference the chunk number for cross-references

##### Open Questions
- Note questions the text explicitly raises but doesn't answer
- Note areas where the text is ambiguous or incomplete
- Add questions that a curious learner would naturally ask

#### 2c. Maintain Continuity

When a section continues from the previous chunk:
- Read the previous chunk's notes for that section
- Do NOT repeat what was already written
- Start with a transition that connects to the previous content
- Add a brief recap comment: `<!-- See chunk NNN for the beginning of this section -->`

When a section will continue in the next chunk:
- End with a natural stopping point
- Add: `<!-- This section continues in chunk NNN -->`

#### 2d. Save the Notes File

Save to: `<working_dir>/notes/chunk_{NNN}_notes.md`

The file should use this format:

```markdown
# Chunk [NNN] — [Descriptive Title]
<!-- Pages: [start]-[end] -->
<!-- Source: chunk_NNN.txt -->

## Section: [Section Title] 🔴

### Core Idea

[2-4 sentences capturing the essence]

> **In Simple Terms:** [Plain-language explanation with everyday analogy]

### Key Concepts

#### [Concept Name]

[Detailed paragraph explaining the concept]

| Concept A | Concept B |
|-----------|-----------|
| [Feature 1] | [Feature 1] |
| [Feature 2] | [Feature 2] |

### Definitions

- **[Term]**: [Precise definition]. [Optional clarification]. ⭐ (exam-important)

### Mechanisms / Processes

1. [Step 1] → [Step 2] → [Step 3]
...

### Examples

**Example: [Title/Description]**
[Detailed example with worked-through calculation]

### ⚠️ Common Mistakes

- ❌ Mistake: [what students get wrong] → ✅ Correct: [right understanding]

### Edge Cases & Caveats

- [Caveat 1]

> **Quick Recall:**
> - [Key fact 1]
> - [Key fact 2]
> - [Key formula]

### Connections

- Builds on: [Section Name] (Chunk NNN)
- Related to: [Section Name] (Chunk NNN)

### Open Questions

1. [Question 1]
```

### Step 3: Create the Content Index

After ALL chunks are processed, create `<working_dir>/notes/content_index.md`:

```markdown
# Notes Content Index

**Source**: [PDF filename]
**Total Chunks**: [N]
**Completed**: [timestamp]

## All Notes Files

| Chunk | Title | Pages | Sections | Key Terms |
|-------|-------|-------|----------|-----------|
| 001 | [Title] | 1-3 | [Section Names] | [Top 5 terms] |
| 002 | [Title] | 4-6 | [Section Names] | [Top 5 terms] |
...

## Cross-References

Lists all connections between sections:

| From | To | Relationship |
|------|----|-------------|
| [Section A] (Chunk N) | [Section B] (Chunk M) | builds on |
...

## Key Terms Glossary

Consolidated list of all defined terms across all chunks:

| Term | Definition | First Appears |
|------|-----------|---------------|
| [Term] | [Brief definition] | Chunk NNN |
...
```

### Step 4: Report to User

```
✅ Content Pass Complete
━━━━━━━━━━━━━━━━━━━━━━━
Chunks processed:  [N]
Notes files:       <working_dir>/notes/chunk_*_notes.md
Content index:     <working_dir>/notes/content_index.md
Terms defined:     [M]
Cross-references:  [K]

Next step: Run the Critique Pass (skill 04-critique-pass) to review
and refine the notes.
```

## Quality Standards

The content pass MUST produce notes that meet these standards:

1. **Faithful to source**: Every claim in the notes must come from the source text
2. **No hallucination**: Do not add information not present in the chunks
3. **Comprehensive**: Capture ALL key concepts, not just the obvious ones
4. **Precise**: Use exact terminology from the source
5. **Well-structured**: Follow the template consistently
6. **Connected**: Cross-references should be meaningful and accurate
7. **Deep, not shallow**: This is NOT a summary — it's a knowledge extraction
8. **Student-friendly**: A student reading these notes should understand the topic
   WITHOUT needing the original PDF. Use plain language, analogies, and visual
   aids (tables, arrow chains) wherever possible.
9. **Exam-oriented**: Every section is tagged with exam importance (🔴/🟡/🟢).
   Key definitions are marked with ⭐. Quick Recall boxes highlight must-know facts.

## Writing Style Guide

- **Prefer short sentences** over long, complex ones
- **Use bullet points and tables** liberally — walls of text are hard to study from
- **Bold key terms** on first use
- **Use arrow notation** (→) for causal chains instead of prose
- **Include "why it matters"** — students remember better when they know the purpose
- **Front-load the important stuff** — put the key insight first, details after
- Imagine your reader is a **tired student at 2 AM** before an exam — make it scannable

## Error Handling

- If the structure file seems wrong or has poor section boundaries, adjust it — but note the adjustment with a comment: `<!-- Structure adjusted from original outline -->`
- If a section has very little content in the source, note it: `<!-- This section is brief in the source text -->`
- If you encounter content that doesn't fit any section, add a new `### Additional Notes` subsection
