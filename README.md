# Public Keys Repo

This repository contains public keys in `keys.txt`.

## Static Site

- `/` — HTML preview of the keys
- `/text` — Plaintext version (same as `keys.txt`)

## Local Development

To generate the static files locally:

```fish
python3 generate.py
```

This will create `index.html` and `text` in the repo root.

## GitHub Pages

On every push to `main`, the site is built and deployed to GitHub Pages.
