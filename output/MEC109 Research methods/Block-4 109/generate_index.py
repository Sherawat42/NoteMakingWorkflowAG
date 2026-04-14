import re
import os

files = sorted([f for f in os.listdir("notes") if f.endswith("_structure.md")])
index_content = """# Structure Index
**Source**: Block-4 109.pdf | **Chunks**: 11
## Table of Contents
"""

for file in files:
    with open(f"notes/{file}", "r") as f:
        lines = f.readlines()
        
    title = ""
    pages = ""
    sections = []
    
    for line in lines:
        if line.startswith("# Chunk"):
            title = line.strip().split("—", 1)[-1].strip()
        elif "<!-- Pages:" in line:
            pages = line.split("Pages:")[1].split("-->")[0].strip()
        elif line.startswith("## Section:"):
            sec = line.replace("## Section:", "").strip().split(" ")[0:-1]
            sections.append(" ".join(sec))

    chunk_num = file.split("_")[1]
    index_content += f"### Chunk {chunk_num} — {title} (Pages {pages})\n"
    for s in sections:
        index_content += f"- {s}\n"
    index_content += "\n"

with open("notes/structure_index.md", "w") as f:
    f.write(index_content)

