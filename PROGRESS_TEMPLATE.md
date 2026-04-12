# Progress: [PDF Name]

> Copy this file to `output/<subject>/<book-name>/PROGRESS.md` at the start of each run.
> Fill in the header and check off items as each stage completes.
> Expand the per-chunk lists in Stages 2 and 3 after splitting (one line per chunk).

**PDF**: [full path]
**Subject**: [subject name]
**Working Directory**: `output/<subject>/<book-name>/`
**Started**: [timestamp]
**Completed**: —

---

## Stage 1: Split PDF

- [ ] Working directory created
- [ ] Progress file copied and header filled
- [ ] Split script executed
  - Chunk size: [N pages]
  - Smart split: [yes / no]
- [ ] Total pages: [N]
- [ ] Total chunks: [N]
- [ ] `index.json` verified (valid JSON, no page gaps)
- [ ] Text extraction spot-checked (`.txt` file is readable)
- [ ] Empty `.txt` files noted (if any): [list chunk numbers or "none"]

---

## Stage 2: Structure Pass

> **If document is under ~60 pages**: mark every item below as `N/A` and skip to Stage 3.

- [ ] `notes/` directory created
- [ ] Section tracker initialized

### Per-chunk structure files
> After splitting, replace this block with one line per chunk:
> `- [ ] Chunk NNN — structure: [section title(s)]`

- [ ] Chunk 001 — structure: [section title(s)]
<!-- agent: expand this list to match total_chunks after split -->

### Stage 2 wrap-up
- [ ] `notes/structure_index.md` created
- [ ] All structure files reviewed (section titles are specific, continuity markers set)

---

## Stage 3: Content Pass

- [ ] `notes/running_context.md` initialized (or confirmed existing from prior run)

### Per-chunk notes files
> After splitting, replace this block with one line per chunk:
> `- [ ] Chunk NNN — notes complete`

- [ ] Chunk 001 — notes complete
<!-- agent: expand this list to match total_chunks after split -->

### Stage 3 wrap-up
- [ ] `notes/content_index.md` created
- [ ] `notes/running_context.md` has entries for all key concepts

---

## Stage 4: Combine Notes

- [ ] `combine_notes.py` executed
- [ ] `export/<book-name>/Complete_Notes.md` generated and non-empty
- [ ] `export/<book-name>/Last_Minute_Revision_Notes.md` generated and non-empty

---

## Completion

- [ ] All stages complete
- **Completed**: [timestamp]
- **Export location**: `output/<subject>/<book-name>/export/<book-name>/`
