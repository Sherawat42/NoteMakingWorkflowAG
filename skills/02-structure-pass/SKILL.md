---
name: structure-pass
description: >
  Create a notes structure/outline for each PDF chunk using a sliding context window.
  Use when the user asks to "create the structure", "outline the notes",
  "run pass 1", "run the structure pass", or after the PDF has been split into chunks.
---

# Structure Pass — Create Notes Outline (Pass 1)

This skill processes each 3-page chunk of a split PDF and creates a **structure-only** 
outline for notes. It uses a sliding window of 3 chunks (previous + current + next) to 
maintain context and continuity across section boundaries.

This is the **second step** in the PDF-to-Notes pipeline.

## Prerequisites

- PDF has been split using the `01-split-pdf` skill
- `index.json` exists in the working directory
- All `.txt` chunk files are present in the `chunks/` directory

## Instructions

### Step 1: Load the Index

Read `<working_dir>/index.json` to get the list of all chunks.

Identify the working directory. It should be:
```
<project_root>/output/<subject>/<book-name>/
```

### Step 2: Create the Notes Directory

```bash
mkdir -p <working_dir>/notes
```

### Step 3: Initialize the Section Tracker

Maintain a running list of section titles and topics encountered so far.
This helps ensure:
- No duplicate section names
- Consistent naming conventions
- Logical flow between chunks

Start with an empty tracker:
```
section_tracker = []
```

### Step 4: Process Each Chunk (Sliding Window)

For each chunk `i` (from 1 to total_chunks), do the following:

#### 4a. Load Context Window

Load the **text content** (`.txt` files) for up to 3 chunks:

| File | Purpose | Required? |
|------|---------|-----------|
| `chunk_{i-1}.txt` | Previous chunk — backward context | Only if i > 1 |
| `chunk_{i}.txt` | Current chunk — the one being outlined | Always |
| `chunk_{i+1}.txt` | Next chunk — forward context | Only if i < total |

#### 4b. Analyze the Content

With the 3-chunk window loaded, analyze the current chunk and determine:

1. **What topics/sections does this chunk cover?**
2. **Does a section continue from the previous chunk?** (Check the ending of the previous chunk)
3. **Does a section start here and continue into the next chunk?** (Check the beginning of the next chunk)
4. **What are the key concepts, terms, and mechanisms mentioned?**

#### 4c. Generate the Structure

Create a structure file for the current chunk using this exact template.
Fill in the headings/subheadings based on the content, but leave the body as placeholders:

```markdown
# Chunk [NNN] — [Descriptive Title Based on Content]
<!-- Pages: [start]-[end] -->
<!-- Continues from: [previous section title, or "N/A"] -->
<!-- Continues into: [next section title, or "N/A"] -->

## Section: [Section/Topic Title] [🔴|🟡|🟢]
<!-- This section [starts here | continues from chunk NNN] -->
<!-- Exam importance: 🔴 HIGH YIELD / 🟡 MODERATE / 🟢 CONTEXT -->
<!-- Reason: [why this importance level — e.g., "has CYP questions", "named theorem", "background only"] -->

### Core Idea
<!-- placeholder: 1-2 sentence summary of the main idea -->

### In Simple Terms
<!-- placeholder: plain-language explanation with everyday analogy -->

### Key Concepts
#### [Concept Name 1]
<!-- placeholder -->
#### [Concept Name 2]
<!-- placeholder -->

### Definitions
- **[Term 1]**: <!-- placeholder -->
- **[Term 2]**: <!-- placeholder -->

### Mechanisms / Processes
<!-- placeholder: list any processes, algorithms, workflows described -->

### Examples
<!-- placeholder: list examples given in the text -->

### Common Mistakes
<!-- placeholder: typical student errors for this topic (if applicable) -->

### Edge Cases & Caveats
<!-- placeholder: any warnings, exceptions, or edge cases -->

### Quick Recall
<!-- placeholder: 3-5 key facts a student should memorize -->

### Connections
<!-- placeholder: how this connects to other sections/topics -->

### Open Questions
<!-- placeholder: questions raised by the text or worth exploring -->
```

**Important rules:**
- A chunk may contain **multiple sections** — create a `## Section:` block for each
- If a section started in the previous chunk, mark it as `continues from chunk NNN`
- If a section will continue in the next chunk, mark it as `continues into chunk NNN`
- Concept names, term names, and section titles should be **specific** — not generic
- Use the actual terminology from the text
- Include ALL key terms found, even if you're not sure they're important

#### 4d. Update the Section Tracker

After processing each chunk, update the section tracker:
```
section_tracker.append({
    "chunk_id": i,
    "sections": ["Section Title 1", "Section Title 2"],
    "continues_from_previous": true/false,
    "continues_to_next": true/false
})
```

#### 4e. Save the Structure File

Save to: `<working_dir>/notes/chunk_{NNN}_structure.md`

### Step 5: Create the Structure Index

After ALL chunks are processed, create `<working_dir>/notes/structure_index.md`:

```markdown
# Notes Structure Index

**Source**: [PDF filename]
**Total Chunks**: [N]
**Created**: [timestamp]

## Table of Contents

### Chunk 001 — [Title] (Pages X-Y)
- Section: [Section Name]
  - Key Concepts: [list]
  - Definitions: [count] terms

### Chunk 002 — [Title] (Pages X-Y)
- Section: [Section Name] (continues from Chunk 001)
  - Key Concepts: [list]
  - Definitions: [count] terms

...

## Section Flow

Shows how sections span across chunks:

| Section | Starts | Ends | Chunks |
|---------|--------|------|--------|
| [Section Name] | Chunk 001 | Chunk 003 | 3 |
| [Section Name] | Chunk 004 | Chunk 004 | 1 |
...
```

### Step 6: Report to User

```
✅ Structure Pass Complete
━━━━━━━━━━━━━━━━━━━━━━━━
Chunks processed:  [N]
Sections found:    [M]
Structure files:   <working_dir>/notes/chunk_*_structure.md
Index:             <working_dir>/notes/structure_index.md

Next step: Review the structure files, then run the Content Pass
(skill 03-content-pass) to fill the outlines with content.
```

## Error Handling

- If a `.txt` file is empty or very short, note it in the structure file as `<!-- WARNING: minimal text extracted from this chunk -->`
- If the content doesn't fit neatly into sections (e.g., it's a table or index), adapt the template accordingly
- If you're unsure about section boundaries, err on the side of creating more sections — they can be merged in the content pass

## Quality Checklist

Before marking this pass as complete, verify:
- [ ] Every chunk has a corresponding `_structure.md` file
- [ ] Section continuity is tracked (continues from/into)
- [ ] All key terms from the text appear in the structure
- [ ] Section titles are specific, not generic (e.g., "Gradient Descent Optimization" not "Topic 1")
- [ ] The structure index covers all chunks and shows section flow
