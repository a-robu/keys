#!/usr/bin/env python3
"""
Generate index.html and text from keys.txt for static hosting.
"""
from pathlib import Path

KEYS_FILE = Path("keys.txt")
HTML_FILE = Path("index.html")
TEXT_FILE = Path("text")

def main():
    keys = KEYS_FILE.read_text(encoding="utf-8")
    # Write plaintext copy
    TEXT_FILE.write_text(keys, encoding="utf-8")
    # Write HTML
    html = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <title>Public Keys</title>
  <link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/prismjs@1.29.0/themes/prism-tomorrow.min.css\">
  <style>
    body {{ background: #f9f9f9; font-family: sans-serif; }}
    .container {{ margin: 2em auto; }}
    pre {{ background: #222; color: #eee; padding: 1em; border-radius: 6px; font-size: 1.1em; overflow-x: auto; }}
  </style>
</head>
<body>
  <div class=\"container\">
    <h1>Public Keys</h1>
    <pre><code class=\"language-ssh\">{keys}</code></pre>
    <p><a href=\"/text\">View as plaintext</a></p>
  </div>
  <script src=\"https://cdn.jsdelivr.net/npm/prismjs@1.29.0/prism.min.js\"></script>
  <script src=\"https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-clike.min.js\"></script>
  <script src=\"https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-bash.min.js\"></script>
  <script src=\"prism.js\"></script>
</body>
</html>"""
    HTML_FILE.write_text(html, encoding="utf-8")

if __name__ == "__main__":
    main()
