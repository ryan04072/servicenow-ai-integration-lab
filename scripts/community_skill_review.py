from pathlib import Path
import re, sys

root = Path(sys.argv[1]) if len(sys.argv) > 1 else None
if not root or not root.exists():
    raise SystemExit("Usage: python scripts/community_skill_review.py <skill-directory>")

patterns = {
    "network": re.compile(r"\b(curl|wget|requests\.|fetch\(|axios|http://|https://)", re.I),
    "destructive": re.compile(r"\b(rm\s+-rf|Remove-Item\s+-Recurse|del\s+/[sq]|format\s+|diskpart)\b", re.I),
    "secrets": re.compile(r"\b(API_KEY|TOKEN|PASSWORD|SECRET|process\.env|os\.environ)\b", re.I),
    "package-install": re.compile(r"\b(npm\s+install|pip\s+install|brew\s+install|choco\s+install)\b", re.I),
}

print(f"Static review: {root}")
for p in sorted(root.rglob("*")):
    if not p.is_file():
        continue
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        continue
    hits = []
    for label, rx in patterns.items():
        if rx.search(text):
            hits.append(label)
    if hits:
        print(f"{p}: {', '.join(hits)}")

print("Static flags are not a safety guarantee. Manual review is still required.")
