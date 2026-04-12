---
name: split-pdf
description: >
  Split a PDF file into chunks for the note-making pipeline.
  Use when the user asks to "split a PDF", "prepare a PDF for notes",
  "start the note-making pipeline", or provides a PDF file path to process.
---

# Split PDF into Chunks

This skill splits a source PDF into page chunks and extracts text from each chunk.
It is the **first step** in the PDF-to-Notes pipeline.

Default chunk size is **10 pages**. For documents with clear section structure,
use `--smart-split` to automatically align chunk boundaries with section headings.

## Prerequisites

- Python 3.8+ installed
- `pypdf` library installed (`pip install pypdf`)

## Instructions

### Step 1: Identify the Input PDF

The user will provide a path to a PDF file. Verify the file exists.

If the user has not provided a path, ask them:
> "Please provide the full path to the PDF file you want to process."

### Step 2: Create the Working Directory

Create a working directory for this PDF under the project:

```
<project_root>/output/<subject>/<book-name>/
```

Where `<subject>` is the subject name and `<book-name>` is derived from the PDF filename (without extension).

Example: `Machine Learning Basics.pdf` in Subject `CS101` → `output/CS101/Machine Learning Basics/`

> **Multi-PDF isolation**: Each PDF MUST get its own unique `<subject>/<book-name>/` folder.
> All pipeline outputs (chunks, notes, and exports) for this PDF will live
> exclusively inside this folder. This ensures that running the pipeline on
> multiple PDFs never causes files to mix up or overwrite each other.

### Step 3: Run the Split Script

#### Standard split (default — use for most documents):

```bash
python skills/01-split-pdf/scripts/split_pdf.py "<input_pdf_path>" "<working_dir>"
```

This uses a default chunk size of **10 pages**.

#### Smart split (recommended for textbooks with clear unit/chapter structure):

```bash
python skills/01-split-pdf/scripts/split_pdf.py "<input_pdf_path>" "<working_dir>" --smart-split
```

Smart split detects headings like `UNIT 1`, `Chapter 2`, `1.1 Introduction` and snaps
chunk boundaries to align with them (within a ±2 page window around each planned split).
This eliminates artificial mid-section cuts.

#### Custom chunk size:

```bash
python skills/01-split-pdf/scripts/split_pdf.py "<input_pdf_path>" "<working_dir>" --chunk-size 15 --smart-split
```

**Choosing chunk size:**
- 10 pages (default) — good for most academic textbooks
- 15–20 pages — for books with long self-contained chapters
- 5–8 pages — for very dense technical content where deep focus per chunk is needed

The script creates:
- `<working_dir>/chunks/chunk_001.pdf` — PDF chunk files
- `<working_dir>/chunks/chunk_001.txt` — Extracted text for each chunk
- `<working_dir>/index.json` — Index file describing all chunks

### Step 4: Verify the Output

1. Check that `index.json` exists and is valid JSON
2. Read `index.json` and verify:
   - `total_chunks` matches the expected number
   - All chunk files (both `.pdf` and `.txt`) exist
   - Page ranges cover all pages without gaps
3. Spot-check one `.txt` file to confirm text was extracted

### Step 5: Report to User

Provide a summary:

```
✅ PDF Split Complete
━━━━━━━━━━━━━━━━━━━━
Source:       <filename>
Total Pages:  <N>
Chunks:       <M> chunks (~10 pages each)
Smart Split:  enabled / disabled
Output:       <working_dir>
Index:        <working_dir>/index.json

Next step: Run the Structure Pass (skill 02-structure-pass) to create
the notes outline for each chunk. For documents under 60 pages, you may
skip directly to the Content Pass (skill 03-content-pass).
```

## Error Handling

- If `pypdf` is not installed, run `pip install pypdf` and retry
- If the PDF is password-protected, inform the user and ask for the password
- If text extraction yields empty results for a chunk, warn the user but continue —
  the chunk may contain only images or be a scanned page

## Output Structure

After this skill completes, the directory looks like:

```
output/<subject>/<book-name>/
├── index.json
├── input/
│   └── <book-name>.pdf
└── chunks/
    ├── chunk_001.pdf
    ├── chunk_001.txt
    ├── chunk_002.pdf
    ├── chunk_002.txt
    └── ...
```

Later pipeline steps add:
```
output/<subject>/<book-name>/
├── notes/          # Created by skills 02-03
│   └── ...
└── export/         # Created by combine_notes.py
    └── <book-name>/
        ├── Complete_Notes.md
        └── Last_Minute_Revision_Notes.md
```
