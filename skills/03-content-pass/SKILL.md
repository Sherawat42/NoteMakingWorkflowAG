---
name: content-pass
description: >
  Fill the notes structure with detailed content for each PDF chunk.
  Use when the user asks to "fill the notes", "add content", "run pass 2",
  "run the content pass", or after the structure pass has completed.
  Can also be run directly after splitting (skipping the structure pass) for
  documents under ~60 pages.
---

# Content Pass — Fill Structure with Content (Pass 2)

This skill takes the structure outlines from Pass 1 and fills them with **detailed,
substantive content** extracted from the original PDF chunks. This is NOT summarization —
the goal is comprehensive notes that capture the full depth of the source material.

This is the **third step** in the PDF-to-Notes pipeline (or the **second step** if the
structure pass was skipped for a short document).

## Prerequisites

- PDF has been split using `01-split-pdf`
- Either: structure files (`chunk_*_structure.md`) exist in `<working_dir>/notes/`
- Or: you are running without a prior structure pass (see "Running Without Structure Files" below)

## Running Without Structure Files

For documents under ~60 pages where the structure pass was skipped:

When processing each chunk, **generate the structure inline** before filling content:
1. Read the source text for the current chunk
2. Identify sections and create the outline mentally (no need to write a separate `_structure.md`)
3. Write the fully-filled `_notes.md` directly, including all section headers

The output format is identical — only the intermediate step is skipped.

---

## Instructions

### Step 1: Load the Index and Verify Readiness

1. Read `<working_dir>/index.json`
2. If structure files exist: verify all `chunk_*_structure.md` files are present in `notes/`
3. Create the `notes/` directory if it doesn't exist: `mkdir -p <working_dir>/notes`

### Step 2: Load or Initialize the Running Context

The **running context** is a lightweight file (`notes/running_context.md`) that accumulates
key facts discovered across all previously processed chunks. It gives every chunk awareness
of what has been introduced earlier in the document — preventing repeated definitions,
enabling accurate cross-references, and keeping terminology consistent.

**At the start of the content pass:**
- If `notes/running_context.md` exists: read it as additional context
- If it doesn't exist yet: it will be created after the first chunk

**The running context format:**

```markdown
# Running Context

## Key Concepts Introduced
- **[Concept]** (Chunk NNN): [one-line description]

## Definitions (⭐ exam-important)
- **[Term]** (Chunk NNN): [definition]

## Named Models / Laws / Theories
- **[Name]** (Chunk NNN): [brief description]

## Key Data & Numbers
- [statistic or figure] (Chunk NNN): [context]
```

Keep each entry to one line. The file should remain under ~3KB for a typical 100-page book.

### Step 3: Process Each Chunk (Sequential, With Context)

For each chunk `i` (from 1 to total_chunks), load these files:

| File | Purpose | Required? |
|------|---------|-----------|
| `notes/running_context.md` | Accumulated facts from all prior chunks | If it exists |
| `notes/chunk_{i-1}_notes.md` | Previous chunk's **completed notes** — for continuity | Only if i > 1 |
| `chunks/chunk_{i}.txt` | Current chunk's **source text** — ground truth | Always |
| `notes/chunk_{i}_structure.md` | Current chunk's **structure outline** to fill | If it exists |

> **Important**: Use the previous chunk's COMPLETED notes (not structure) for context.
> The running context covers the whole document; the previous chunk's notes provide
> immediate continuity for sections that span chunks.

#### 3a. Fill Each Section

For every section and subsection, replace `<!-- placeholder -->` comments with actual content.

##### Exam Importance Markers

Every `## Section` heading MUST include an exam importance tag:

| Marker | Meaning | When to use |
|--------|---------|-------------|
| 🔴 **HIGH YIELD** | Very likely in exams | Core theories, named laws/models, derivations, topics with Check Your Progress questions |
| 🟡 **MODERATE** | May appear | Supporting concepts, secondary mechanisms, elaborations |
| 🟢 **CONTEXT** | Unlikely as direct question | Historical background, introductions, admin content |

**Signals of high exam importance:**
- "Check Your Progress" exercises in the source text
- Named models, laws, or theorems (Say's Law, IS-LM, Multiplier)
- Equations or derivations
- Mentioned in unit Objectives or Summary
- Multiple pages devoted to the topic

##### Core Idea
- 2-4 sentences capturing the main idea
- Must stand alone — reader should understand the topic from this alone
- Do NOT copy-paste from source; rephrase clearly

##### In Simple Terms
- Add a `> **In Simple Terms:**` blockquote immediately after Core Idea
- Explain as if talking to someone who has never studied the subject
- Use everyday analogies, plain language, relatable examples
- 1-3 sentences

Example:
> **In Simple Terms:** The multiplier is like a ripple effect — when the government spends ₹100, it doesn't stop there. That money gets spent again and again, making the total economic impact much larger than the original ₹100.

##### Key Concepts
- One **paragraph** per concept (3-6 sentences): what it is, why it matters, how it relates
- Use source text as authority — do NOT add information not present in the chunks
- **Use comparison tables** whenever two or more concepts are contrasted

##### Definitions
- Precise definitions from the text
- Brief clarifying sentence if the definition uses jargon
- Mark exam-critical definitions: `⭐ (exam-important)`

##### Mechanisms / Processes
- Numbered steps for sequential processes
- Arrow notation for causal chains: `A → B → C → D`
- Include conditions, inputs, outputs

##### Examples
- Reproduce examples from the text with context
- Include worked-through calculations — show the steps, don't just state formulas

##### Quick Recall Box
- At the end of each major section, add a `> **Quick Recall:**` blockquote
- 3-5 must-know facts in bullet points

```
> **Quick Recall:**
> - Multiplier = 1/(1-MPC)
> - Higher MPC → larger multiplier
> - Tax multiplier is always smaller than spending multiplier
```

##### Common Mistakes
- If students commonly get confused on this topic, add `### ⚠️ Common Mistakes`
- 2-3 errors with corrections: `- ❌ Mistake: ... → ✅ Correct: ...`

##### Edge Cases & Caveats
- Exceptions, limitations, warnings from the text
- "Commonly confused with..." notes

##### Connections
- Reference other sections by name
- State the relationship type: "builds on", "contrasts with", "is prerequisite for"
- Include chunk number for cross-reference: `[Section Name] (Chunk NNN)`

##### Open Questions
- Questions the text raises but doesn't fully answer
- Ambiguities or gaps a curious learner would notice

#### 3b. Maintain Continuity

When a section continues from the previous chunk:
- Read the previous chunk's notes for that section
- Do NOT repeat content already written
- Start with a connecting transition
- Add: `<!-- See chunk NNN for the beginning of this section -->`

When a section will continue in the next chunk:
- End at a natural stopping point
- Add: `<!-- This section continues in chunk NNN -->`

#### 3c. Save the Notes File

Save to: `<working_dir>/notes/chunk_{NNN}_notes.md`

```markdown
# Chunk [NNN] — [Descriptive Title]
<!-- Pages: [start]-[end] -->
<!-- Source: chunk_NNN.txt -->

## Section: [Section Title] 🔴

### Core Idea

[2-4 sentences]

> **In Simple Terms:** [Plain-language explanation with analogy]

### Key Concepts

#### [Concept Name]

[Detailed paragraph]

| Concept A | Concept B |
|-----------|-----------|
| [Feature] | [Feature] |

### Definitions

- **[Term]**: [Precise definition]. ⭐ (exam-important)

### Mechanisms / Processes

1. [Step 1] → [Step 2] → [Step 3]

### Examples

**Example: [Title]**
[Worked-through calculation or case]

### ⚠️ Common Mistakes

- ❌ Mistake: [what students get wrong] → ✅ Correct: [right understanding]

### Edge Cases & Caveats

- [Caveat]

> **Quick Recall:**
> - [Key fact]
> - [Key formula]

### Connections

- Builds on: [Section Name] (Chunk NNN)

### Open Questions

1. [Question]
```

#### 3d. Update the Running Context

After saving the notes file, append new discoveries to `notes/running_context.md`:
- Any **new** key concepts introduced (not already in the file)
- Any **new** definitions marked ⭐
- Any **new** named models, laws, or theories
- Any **new** key data points or numbers

Only add entries not already present. Keep each entry to one line.

### Step 4: Inline Self-Review (Per Chunk)

After writing each chunk's notes file, perform a quick self-review before moving on:

1. **Faithfulness check**: Pick 3 specific claims in your notes. Verify each appears in `chunk_{NNN}.txt`. If anything was added from outside the source, remove it.
2. **Repetition check**: Scan the previous chunk's notes. Are any sentences or definitions copied verbatim? If so, rephrase or remove them.
3. **Marker check**: Do all `⭐` definitions actually appear in the source text? Are all 🔴 sections genuinely high-yield based on the signals listed above?

If a check fails, fix the issue in the notes file before moving to the next chunk.

### Step 5: Create the Content Index

After ALL chunks are processed, create `<working_dir>/notes/content_index.md`:

```markdown
# Notes Content Index

**Source**: [PDF filename]
**Total Chunks**: [N]
**Completed**: [timestamp]

## All Notes Files

| Chunk | Title | Pages | Sections | Key Terms |
|-------|-------|-------|----------|-----------|
| 001 | [Title] | 1-10 | [Section Names] | [Top 5 terms] |
...

## Cross-References

| From | To | Relationship |
|------|----|-------------|
| [Section A] (Chunk N) | [Section B] (Chunk M) | builds on |
...

## Key Terms Glossary

| Term | Definition | First Appears |
|------|-----------|---------------|
| [Term] | [Brief definition] | Chunk NNN |
...
```

### Step 6: Report to User

```
✅ Content Pass Complete
━━━━━━━━━━━━━━━━━━━━━━━
Chunks processed:  [N]
Notes files:       <working_dir>/notes/chunk_*_notes.md
Running context:   <working_dir>/notes/running_context.md
Content index:     <working_dir>/notes/content_index.md
Terms defined:     [M]

Next step: Run `python combine_notes.py "<working_dir>"` to combine
the notes into Complete_Notes.md and Last_Minute_Revision_Notes.md.
```

## Quality Standards

1. **Faithful to source**: Every claim must come from the source text
2. **No hallucination**: Do not add information not in the chunks
3. **Comprehensive**: Capture ALL key concepts, not just obvious ones
4. **Precise**: Use exact terminology from the source
5. **Connected**: Cross-references are meaningful and use real section names
6. **Deep, not shallow**: This is knowledge extraction, not summarization
7. **Student-friendly**: A student should understand without needing the original PDF
8. **Exam-oriented**: 🔴/🟡/🟢 tags on every section; ⭐ on exam-critical definitions

## Writing Style

- Short sentences over long, complex ones
- Bullet points and tables over walls of text
- **Bold** key terms on first use
- Arrow notation (→) for causal chains
- Include "why it matters" — students remember purpose better than facts
- Front-load the important information
- Target reader: tired student at 2 AM before an exam — make it scannable

## Error Handling

- If a structure file has poor section boundaries, adjust it and note the change:
  `<!-- Structure adjusted from original outline -->`
- If a section has very little source content:
  `<!-- This section is brief in the source text -->`
- If content doesn't fit any section, add `### Additional Notes`
