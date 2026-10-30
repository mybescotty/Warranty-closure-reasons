"""Builds the shareable claude.ai artifact copy of warranty-tracker.html.

The artifact host wraps the page in its own <html>/<head>/<body>, so this strips
those tags (and the charset/viewport metas it supplies) and keeps everything else.
Usage: python3 tools/build_artifact.py <output.html>
"""
import re
import sys
from pathlib import Path

src = Path(__file__).resolve().parent.parent / "warranty-tracker.html"
html = src.read_text(encoding="utf-8")
for pattern in [r"<!DOCTYPE html>\s*", r"<html[^>]*>\s*", r"</?head>\s*", r"<body>\s*", r"</body>\s*", r"</html>\s*",
                r'<meta charset="utf-8">\s*', r'<meta name="viewport"[^>]*>\s*']:
    html = re.sub(pattern, "", html, flags=re.I)
Path(sys.argv[1]).write_text(html, encoding="utf-8")
print(f"Wrote {sys.argv[1]} ({len(html):,} bytes)")
