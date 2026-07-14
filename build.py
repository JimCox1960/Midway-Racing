#!/usr/bin/env python3
"""
Build script for Midway Racing Stable site.

Reads index.html (which references files under assets/ by relative path)
and produces dist/midway-racing-index.html with every image and video
inlined as a base64 data URI, so the final file has zero external
dependencies and can be opened/moved anywhere without breaking.

Usage: python3 build.py
"""
import base64
import os

SRC = "index.html"
OUT_DIR = "dist"
OUT = os.path.join(OUT_DIR, "midway-racing-index.html")

MIME = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".mp4": "video/mp4"}

def main():
    with open(SRC, "r", encoding="utf-8") as f:
        html = f.read()

    asset_paths = []
    for root, _dirs, files in os.walk("assets"):
        for fname in files:
            asset_paths.append(os.path.join(root, fname).replace(os.sep, "/"))

    count = 0
    for path in sorted(asset_paths):
        ext = os.path.splitext(path)[1].lower()
        if ext not in MIME:
            continue
        if path not in html:
            print(f"  (skipped, not referenced in {SRC}): {path}")
            continue
        with open(path, "rb") as f:
            data = f.read()
        data_uri = f"data:{MIME[ext]};base64,{base64.b64encode(data).decode('ascii')}"
        html = html.replace(path, data_uri)
        count += 1
        print(f"  embedded: {path} ({len(data)/1e6:.2f} MB)")

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\nDone. Embedded {count} assets.")
    print(f"Output: {OUT} ({os.path.getsize(OUT)/1e6:.1f} MB)")

if __name__ == "__main__":
    main()
