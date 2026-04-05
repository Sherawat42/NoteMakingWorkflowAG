#!/usr/bin/env python3
"""
split_pdf.py — Split a PDF into fixed-size page chunks.

Usage:
    python split_pdf.py <input_pdf> <output_dir> [--chunk-size 3]

Outputs:
    - chunk_001.pdf, chunk_002.pdf, ... in <output_dir>/chunks/
    - chunk_001.txt, chunk_002.txt, ... (extracted text) in <output_dir>/chunks/
    - index.json in <output_dir>/

Dependencies:
    pip install pypdf
"""

import argparse
import json
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    print("ERROR: 'pypdf' is not installed. Run: pip install pypdf", file=sys.stderr)
    sys.exit(1)


def extract_text_from_pages(reader: PdfReader, start_page: int, end_page: int) -> str:
    """Extract text from a range of pages (0-indexed, inclusive)."""
    text_parts = []
    for page_num in range(start_page, end_page + 1):
        page = reader.pages[page_num]
        page_text = page.extract_text() or ""
        text_parts.append(f"--- Page {page_num + 1} ---\n{page_text}")
    return "\n\n".join(text_parts)


def split_pdf(input_pdf: str, output_dir: str, chunk_size: int = 3) -> dict:
    """
    Split a PDF into chunks of `chunk_size` pages each.

    Args:
        input_pdf: Path to the source PDF file
        output_dir: Directory to write chunks and index
        chunk_size: Number of pages per chunk (default: 3)

    Returns:
        The index dictionary describing all chunks
    """
    input_path = Path(input_pdf).resolve()
    output_path = Path(output_dir).resolve()

    if not input_path.exists():
        print(f"ERROR: Input PDF not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    # Create output directories
    chunks_dir = output_path / "chunks"
    chunks_dir.mkdir(parents=True, exist_ok=True)
    
    input_dir = output_path / "input"
    input_dir.mkdir(parents=True, exist_ok=True)

    # Copy the input PDF into the input directory
    copied_pdf_path = input_dir / input_path.name
    if not copied_pdf_path.exists() or input_path != copied_pdf_path:
        shutil.copy2(input_path, copied_pdf_path)

    # Read the copied PDF (so we don't hold lock on original or run into issues)
    reader = PdfReader(str(copied_pdf_path))
    total_pages = len(reader.pages)

    if total_pages == 0:
        print("ERROR: PDF has no pages.", file=sys.stderr)
        sys.exit(1)

    # Calculate chunks
    total_chunks = (total_pages + chunk_size - 1) // chunk_size  # ceiling division
    chunks_info = []

    print(f"Source: {input_path.name}")
    print(f"Total pages: {total_pages}")
    print(f"Chunk size: {chunk_size} pages")
    print(f"Total chunks: {total_chunks}")
    print(f"Output: {output_path}")
    print("-" * 50)

    for chunk_idx in range(total_chunks):
        start_page = chunk_idx * chunk_size  # 0-indexed
        end_page = min(start_page + chunk_size - 1, total_pages - 1)  # 0-indexed, inclusive
        pages_in_chunk = end_page - start_page + 1

        chunk_num = chunk_idx + 1
        chunk_filename = f"chunk_{chunk_num:03d}.pdf"
        text_filename = f"chunk_{chunk_num:03d}.txt"

        # Write PDF chunk
        writer = PdfWriter()
        for page_num in range(start_page, end_page + 1):
            writer.add_page(reader.pages[page_num])

        chunk_pdf_path = chunks_dir / chunk_filename
        with open(chunk_pdf_path, "wb") as f:
            writer.write(f)

        # Extract and write text
        text_content = extract_text_from_pages(reader, start_page, end_page)
        chunk_text_path = chunks_dir / text_filename
        with open(chunk_text_path, "w", encoding="utf-8") as f:
            f.write(text_content)

        chunk_info = {
            "chunk_id": chunk_num,
            "filename": chunk_filename,
            "text_filename": text_filename,
            "page_range": [start_page + 1, end_page + 1],  # 1-indexed for humans
            "pages": pages_in_chunk,
        }
        chunks_info.append(chunk_info)
        print(f"  ✓ Chunk {chunk_num:03d}: pages {start_page + 1}-{end_page + 1} ({pages_in_chunk} pages)")

    # Build index
    index = {
        "source_pdf": str(copied_pdf_path),
        "source_filename": input_path.name,
        "total_pages": total_pages,
        "chunk_size": chunk_size,
        "total_chunks": total_chunks,
        "chunks_directory": str(chunks_dir),
        "chunks": chunks_info,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }

    # Write index
    index_path = output_path / "index.json"
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)

    print("-" * 50)
    print(f"  ✓ Index written: {index_path}")
    print(f"\nDone! {total_chunks} chunks created in {chunks_dir}")

    return index


def main():
    parser = argparse.ArgumentParser(
        description="Split a PDF into fixed-size page chunks with text extraction.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python split_pdf.py book.pdf ./output
    python split_pdf.py book.pdf ./output --chunk-size 5
        """,
    )
    parser.add_argument("input_pdf", help="Path to the input PDF file")
    parser.add_argument("output_dir", help="Directory to write chunks and index.json")
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=3,
        help="Number of pages per chunk (default: 3)",
    )

    args = parser.parse_args()

    if args.chunk_size < 1:
        print("ERROR: Chunk size must be at least 1.", file=sys.stderr)
        sys.exit(1)

    split_pdf(args.input_pdf, args.output_dir, args.chunk_size)


if __name__ == "__main__":
    main()
