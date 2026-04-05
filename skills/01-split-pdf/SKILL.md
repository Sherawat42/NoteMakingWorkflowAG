---
name: split-pdf
description: >
  Split a PDF file into 3-page chunks for the note-making pipeline.
  Use when the user asks to "split a PDF", "prepare a PDF for notes",
  "start the note-making pipeline", or provides a PDF file path to process.
---

# Split PDF into 3-Page Chunks

This skill splits a source PDF into 3-page chunks and extracts text from each chunk.
It is the **first step** in the PDF-to-Notes pipeline.

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
<project_root>/output/<book-name>/
```

Where `<book-name>` is derived from the PDF filename (without extension), converted to lowercase with hyphens replacing spaces.

Example: `Machine Learning Basics.pdf` → `output/machine-learning-basics/`

> **Multi-PDF isolation**: Each PDF MUST get its own unique `<book-name>/` folder.
> All pipeline outputs (chunks, notes, and exports) for this PDF will live
> exclusively inside this folder. This ensures that running the pipeline on
> multiple PDFs never causes files to mix up or overwrite each other.

### Step 3: Run the Split Script

Execute the split script:

```bash
python skills/01-split-pdf/scripts/split_pdf.py "<input_pdf_path>" "<working_dir>" --chunk-size 3
```

The script will create:
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
Chunks:       <M> chunks of 3 pages each
Output:       <working_dir>
Index:        <working_dir>/index.json

Next step: Run the Structure Pass (skill 02-structure-pass) to create
the notes outline for each chunk.
```

## Error Handling

- If `pypdf` is not installed, run `pip install pypdf` and retry
- If the PDF is password-protected, inform the user and ask for the password
- If text extraction yields empty results for a chunk, warn the user but continue — the chunk may contain only images/diagrams

## Output Structure

After this skill completes, the directory should look like:

```
output/<book-name>/
├── index.json
└── chunks/
    ├── chunk_001.pdf
    ├── chunk_001.txt
    ├── chunk_002.pdf
    ├── chunk_002.txt
    └── ...
```

Later pipeline steps will add:
```
output/<book-name>/
├── notes/          # Created by skills 02-04
│   └── ...
└── export/         # Created by skill 04 (critique pass)
    ├── FINAL_NOTES.md
    └── EXAM_PREP.md
```
