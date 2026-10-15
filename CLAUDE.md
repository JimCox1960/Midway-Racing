# Midway Racing Stable — Website

Marketing site for Midway Racing Stable (Davant Latham), a Thoroughbred
racing operation in Midway, Kentucky. Modeled loosely on
littleredfeather.com but with its own visual identity pulled from the
stable's racing silks.

## How this project is structured

- `index.html` — the actual source file. Edit this. It references images
  and one video under `assets/` by relative path (e.g.
  `assets/street-beast/race-1.jpg`).
- `assets/` — all photos, pedigree scans, conformation shots, and the
  Trendsetter workout video, organized by horse.
- `build.py` — run `python3 build.py` to produce
  `dist/midway-racing-index.html`, a single self-contained HTML file with
  every asset inlined as base64. **This is the file that actually gets
  delivered to the client** — it has zero external dependencies, so it
  can't break from a missing folder when opened or moved. Always rebuild
  after editing `index.html` or swapping any asset, and hand off the
  `dist/` output, not the raw `index.html`.
- No other build tooling — plain HTML/CSS/JS, no framework, no npm deps.

## Design system

- Colors: deep racing blue `#152F55` (`--blue`), darker blue `#0E2140`
  (`--blue-deep`), kelly green `#2E7D46` (`--green`), brighter green
  `#3FA45C` (`--green-bright`), cream/parchment background `#F6F1E6`,
  gold accent `#A9822F` used sparingly for stakes wins.
- Type: Fraunces (serif, headlines) + Inter (body) + Roboto Condensed
  (stats, labels, nav — the "tote board" utility face). Loaded via Google
  Fonts CDN link in `<head>`.
- Signature motif: horse cards styled like saddle towels / a tote board
  (dark stat strip with green digits) rather than generic product cards.

## Current page structure

1. **Header/nav** — logo + "MIDWAY RACING / Stable · Midway, Kentucky",
   sticky, tabs: Stable / About / Contact.
2. **Hero** — full-bleed static photo (Trendsetter winner's circle) with
   a "MIDWAY RACING" wordmark (green fill, white outline) above a
   headline ("Purchased, raced and campaigned the right way." — client's
   exact wording) and one-line lede. No CTAs, no video embed (a YouTube embed
   was tried and removed — see "Things already tried" below).
3. **Stable** — grid of horse cards (Street Beast, Trendsetter, Monet's
   Magic, Admiral's Order), each with a racing photo, breeding line,
   earnings/tote-board strip, race results, and a "Sales, Pedigree &
   Pictures" button that opens a modal (`openModal(key)` in the inline
   `<script>`) with race photos, winner's circle, conformation, video
   (Trendsetter only, see below), and pedigree scan.
4. **About** — bio copy + a silks image panel ("Stable Colors").
   Heading: "We'll Keep You On Track" (this was changed from "Founded on
   Farm & Track Experience" — the client may want it changed again).
5. **Contact** — Davant Latham's contact card + a generic ownership
   inquiry card.

## Things already tried (don't redo without asking)

- **Autoplay YouTube hero video**: tried embedding a looping YouTube clip
  behind the hero text. Removed at client's request — likely fails
  silently when the file is opened via `file://` (null origin), and the
  client found it "wonky." Replaced with a static photo. If revisiting
  video in the hero, test on a real hosted URL first, not a local file.
- **Assets as a separate folder shipped alongside index.html**: caused
  broken images/video for the client when the zip wasn't fully
  extracted. This is why `build.py` exists — always ship the embedded
  `dist/` build, never the raw folder.
- **Same YouTube clip reused across multiple horses' modals**: turned out
  to be Trendsetter-specific footage (his G3 Lexington Stakes win), not
  generic stable footage. It was mistakenly attached to Street Beast's
  and Monet's Magic's modals too — now only on Trendsetter's, large
  (full modal width), labeled
  "Trendsetter's G3 Lexington Stakes Win." Don't re-add it elsewhere
  without confirming which horse the footage actually shows.
- **Trendsetter OBS workout video in his modal**: removed at the client's
  request ("for now"). It was ~35 MB and made the `dist/` build ~75 MB.
  The file is still at `assets/trendsetter-workout.mp4`; to restore it,
  add back `'<div><h4>OBS Workout</h4><video controls playsinline
  src="assets/trendsetter-workout.mp4"></video></div>' +` above the
  YouTube link in the `trendsetter` entry of `HORSES`. Consider
  compressing it first.

- **Aftercare section** (three numbered commitments, own nav tab):
  removed entirely at the client's request, along with its nav tab and
  CSS. It had been rewritten once already for being too close to Little
  Red Feather's aftercare copy. Don't re-add without asking.

## Open items / known gaps

- **Admiral's Order** has no racing photo yet (debuted July 11 at Ellis
  Park, won). Card currently uses his conformation photo as the main
  image. Swap in a race photo once the client sends one.
- The `Street_Beast_OBS_workout.png` file that was originally uploaded is
  not a real image (it's a screenshot of an unloaded video player) —
  don't use it. If a real Street Beast workout video shows up, add it
  the same way Trendsetter's OBS workout video was handled (a `<video>`
  tag, not the YouTube pattern).
- No backend, no CMS — every edit is a direct `index.html` edit. If this
  grows past a handful of horses, consider extracting horse data into a
  JSON/JS object that both the card grid and the modal read from (right
  now the card markup and the `HORSES` JS object are maintained
  separately, which is a duplication risk).

## Working conventions from this client

- Prefers being shown the actual working file over descriptions of
  changes — always rebuild `dist/` and hand that off after edits.
- Gives feedback in small, specific batches (e.g. "reduce the size of X
  by 20%, move Y down, remove Z") — apply literally and precisely rather
  than reinterpreting broadly.
- Sensitive to visual polish issues: image sharpness (don't upscale
  small source images), spacing between headings and body copy, exact
  color match to the stable's silks.
