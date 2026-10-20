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

## Current deck (15 slides, one argument)

The deck is ordered as an argument, in six parts; `SCRIPT.md` is the spoken script that goes with it. Brandon asked for materiality to come early, straight after the thesis, and for the envelope slide to carry no annotations.
1. **Problem:** 01 Title · 02 Provocation (Ukeles quote) · 03 Problem: Devil's Gate timeline and the County's Rose Bowl dot chart (sourced).
2. **Claim:** 04 Thesis + sediment loop.
3. **Material:** 05 Material: rammed-earth lifts + six steps from load to wall · 06 Assemblies (floor labels say why each layer is there) · 07 Section detail, with each fastener tagged permanent / rarely / seasonal / continuous and the retension point circled · 08 Sag: two-state diagram.
4. **Place:** 09 Site plan, annotated (upstream, bridge, masses) · 10 Overall section, annotated.
5. **Building:** 11 Sliver section, annotated with leaders (crew, hopper, edge, hoist, plates, mast) · 12 Sliver render · 13 Envelope: `img/render_top.jpg` (from `prez_render.jpg`), unannotated · 14 Model photographs.
6. **Why architecture:** 15 Permanence / publicness / demonstration, network, plus the "permanent place for temporary healing" diagram.

The building section slide was removed at Brandon's request. Its image is still in `deck/img/building_section.png`.
Powers of Ten was dropped because the deck now zooms from site down to joint in order. The annotation helpers (`note`, `lead`, `col`) are at the top of the slide section in `deck.html`. Annotation and new-slide text was drafted by Claude from THESIS.md and `FINAL_QA.md`, and needs Brandon's review. `ASSN_Deck_Updated.pdf` is still the old 12-slide Mac export: rebuild on the Mac for the right fonts (Linux substitutes Helvetica Neue and IBM Plex Mono).

How slide 10 was made: `deck/img/overall_comp.pdf` places `BUILDING_SECTION.pdf` over `OVERALL_SECTION.pdf` with a multiply blend, scale 1.00407, offset (-1739.9, -28.98) pt. The alignment was taken from the bridge lamp posts and deck lines. The original single sliver was erased (x 2576-2782, y 688-957, measured top-down in overall-page points).

## Known issues to raise with Brandon

- The detail drawing labels the tile "FIRED CLAY TILE", but slide 06 and the thesis say sediment earth tiles. One fix: tile pressed from the node's own clay and low-fired.
- The detail does not draw where the crew retensions the Dyneema strap. Slide 07 only circles the pad-eye; slides 07 and 08 and the script depend on it.
- Thesis content now in the deck and script: the Devil's Gate and Eaton record, labor and the crew, permanence / publicness / demonstration, network, contamination. Still not drawn: the elevated public walk, the stables program, crew housing, the testing lab. Not yet cited: Mattern, Jackson, Russell and Vinsel.
- Slide 07's caption (the detail) was written by Claude. The other drawing captions come from the print set.
- The title slide now says "Final Review" with no date; add the date.
- The upstream arrow on the site plan assumes the channel runs upstream to the upper right (northeast). Check it.
- Rammed earth (slide 05) is not yet labelled in the drawings.
