# Arroyo Seco Sediment Node: presentation deck

Brandon Avalos, Hume Vertical Studio, SCI-Arc FA26. Midterm review October 19, 2026; working toward the final review.
Site: Arroyo Seco Stables, South Pasadena (Lower Arroyo, downstream of Devil's Gate Dam).
The argument behind the project is in `THESIS.md`. Read it before writing any slide text.

## Layout

- `deck/deck.html`: the deck source. It is one HTML page whose script builds 1920x1080 spreads (two 960 px halves around a centre fold, 12-column grid, M=80, gutter 24). The fonts are Helvetica Neue for body text and IBM Plex Mono / Menlo, uppercase and tracked, for labels. Each slide is a `page(name,label)` call followed by `tf()` text frames, `img()` / `crop()` images, and `done(p)`. Page numbers are assigned automatically in order.
- `deck/img/`: images the deck uses, prepared from `materials/`.
- `deck/ASSN_Deck_Updated.pdf`: the current export (12 slides).
- `build.sh`: re-exports the PDF with headless Chrome or Chromium.
- `materials/`: the original drawings (PDF), model photos, renders and print set. `PRINT/` holds the board PDFs, which carry the approved one-line captions.
- `reference/`: the original midterm deck PDF and `MID_AXON.3dm`, the Rhino model of the sliver.
- `tools/`: the macOS Swift helpers used to prepare images. They use CoreGraphics, so they do not run on Linux. On Linux, use poppler (`pdftoppm`) or PyMuPDF instead.
  - `trim.swift`: rasterizes a PDF page and crops away the white margins.
  - `comp.swift`: makes a vector composite of the building section into the overall section.

## Current deck (12 slides + 11 question slides)

01 Title · 02 Provocation (Ukeles quote) · 03 Site plan (`materials/PLAN.pdf`) · 04 Thesis + sediment loop · 05 Powers of Ten (crops of joint, sliver, building, site) · 06 Section detail · 07 Assemblies (floor plate / wall) · 08 Sliver section drawing · 09 Sliver render (full bleed) · 10 Building section · 11 Overall section with the full building composited in · 12 Model photographs.

Questions appendix (backup slides for the final review, built by the `QUESTIONS` block near the end of `deck.html`): 13 Index · 14 Floor plates · 15 Peel (`img/render_top.jpg`, from `prez_render.jpg`) · 16 Lost maintenance (timeline + Rose Bowl unit chart, sourced) · 17 Labor (`img/sliver_crew.png`) · 18 Permanence · 19 Sag (two-state diagram) · 20 Cork (`img/detail_cork.png`) · 21 Strap (`img/detail_strap.png`) · 22 Fastening · 23 Rammed earth (lift diagram). Their text was drafted by Claude from `FINAL_QA.md` and needs Brandon's review. `ASSN_Deck_Updated.pdf` is still the 12-slide Mac export; rebuild on the Mac to include the appendix with the right fonts (Linux substitutes Helvetica Neue and IBM Plex Mono).

How slide 11 was made: `deck/img/overall_comp.pdf` places `BUILDING_SECTION.pdf` over `OVERALL_SECTION.pdf` with a multiply blend, scale 1.00407, offset (-1739.9, -28.98) pt. The alignment was taken from the bridge lamp posts and deck lines. The original single sliver was erased (x 2576-2782, y 688-957, measured top-down in overall-page points).

## Known issues to raise with Brandon

- The detail drawing labels the tile "FIRED CLAY TILE", but slide 07 and the thesis say sediment earth tiles.
- The detail does not show where the crew retensions the Dyneema strap.
- The building section linework is light grey, so it reads faintly when projected.
- `materials/RENDER/prez_render.jpg` was added after the deck was built and is not used yet.
- The thesis is not yet shown anywhere in the deck: the four moves (Devil's Gate 1994-2009, the Eaton Fire in 2025), labor and the crew, why architecture rather than policy (permanence, publicness, demonstration), the elevated public walk, the stables program, crew housing, the testing lab, the network argument, the four vulnerabilities, and the texts to cite.
- Slide 06's caption was written by Claude. All other captions come from the print set.
