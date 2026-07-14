# Midway Racing Stable — Website

Marketing site for Midway Racing Stable. Plain HTML/CSS/JS, no framework,
no npm dependencies. See [CLAUDE.md](CLAUDE.md) for the design system,
page structure, and project history.

## Project layout

- `index.html` — the source file. Edit this. It references images and one
  video under `assets/` by relative path.
- `assets/` — all photos, pedigree scans, conformation shots, and the
  workout video, organized by horse.
- `build.py` — combines the two into a single deployable file.
- `dist/` — build output (gitignored, generated locally — see below).

## Prerequisites

- Python 3 (standard library only — no pip installs needed).

## Build

```
python3 build.py
```

This reads `index.html`, walks `assets/`, and inlines every referenced
image and video as a base64 data URI, producing:

```
dist/midway-racing-index.html
```

That output file has **zero external dependencies** — no `assets/`
folder, no relative paths, nothing that can go missing. It can be
opened directly by double-clicking, emailed, or dropped on any static
host and it will render identically.

Run the build after every edit to `index.html` or any change under
`assets/` — `dist/` is not kept in sync automatically and is not
committed to the repo (it's fully reproducible from source, and at
70+ MB it doesn't belong in git history).

The build script prints each embedded asset and its size, and warns
if a file under `assets/` isn't referenced anywhere in `index.html`
(useful for catching stale or unused files).

## Deploy

Hand off `dist/midway-racing-index.html` — never the raw `index.html`
or the `assets/` folder on their own. Shipping them separately is what
caused broken images/video for the client in the past if the folder
wasn't fully extracted alongside the HTML file.

To host it: upload `dist/midway-racing-index.html` as-is to any static
file host (or S3/Netlify/GitHub Pages/etc.) — no build step, server,
or config needed on the hosting side, since everything is already
embedded in the one file.

## Local preview while editing

Before running the build, you can preview `index.html` directly in a
browser — just be aware it's reading assets from disk via relative
paths at that point, so open it from within this folder (don't move
just the HTML file elsewhere) or the images won't resolve.
