from pathlib import Path
import subprocess, json
from collections import Counter

root = Path.cwd()
try:
    raw = subprocess.check_output(["git", "ls-files"], text=True, cwd=root)
    files = sorted(x.strip() for x in raw.splitlines() if x.strip())
except Exception:
    files = sorted(str(p.relative_to(root)) for p in root.rglob("*")
                   if p.is_file() and ".git" not in p.parts)

markdown = [f for f in files if f.lower().endswith(".md")]
top = Counter(Path(f).parts[0] if Path(f).parts else "." for f in files)

Path("repository-inventory.json").write_text(json.dumps({
    "total_files": len(files),
    "total_markdown": len(markdown),
    "files_by_top_level": dict(sorted(top.items())),
    "markdown_files": markdown,
    "all_files": files
}, indent=2), encoding="utf-8")

with Path("repository-audit-coverage.md").open("w", encoding="utf-8") as fh:
    fh.write("# Repository Audit Coverage\n\n")
    fh.write("| Status | File |\n|---|---|\n")
    for f in markdown:
        fh.write(f"| Pending | `{f}` |\n")

print(f"Inventory complete: {len(files)} files / {len(markdown)} Markdown")
