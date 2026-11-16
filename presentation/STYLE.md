# OOMP presentation style

## Reference and adaptation

This follows the [OOBB base directory](https://github.com/oomlout/oomlout_oobb_version_5), its [presentation style](https://github.com/oomlout/oomlout_oobb_version_5/blob/main/presentation/STYLE.md), and the [plate catalogue generator](https://github.com/oomlout/oomlout_oobb_part_plate_version_5/blob/main/working_navigation.py), inspected 16 November 2026.

Keep OOBB's plain introduction, representative object image, compact directory discovery and four catalogue headings: Summary, Details, Parts, Assembly. OOMP records cover purchased hardware and electronic components as well as generated models: do not transfer plate-specific printing instructions, inferred fasteners or an unsupported assertion that every source is AI-generated.

## Base directory

Explain what OOMP provides and help the reader select electronics, breakouts, electronic projects, fasteners, bearings or mechanical parts. Show an actual catalogue render with a named example and source link. Separate full catalogues from lightweight exports and the pretty electronics browser. Include every known version-five repository, retaining its exact published spelling. Keep setup in a secondary README linked near the end.

## Catalogue root

Summary states the component family and purpose in ordinary language. Show one existing representative image, with descriptive alt text and an accurate illustration/render caption. Details links the base directory and maintenance guide. Parts links canonical folders or an existing taxonomy browser; do not embed thousands of rows. Assembly explains how to choose a record, and links specialist instructions where they exist.

## Canonical part page

Summary names the exact variant. Details shows its full ID, actual taxonomy and relevant dimensions with explicit units. Preserve the complete working.yaml mapping in an expandable block and link its source. Parts points to the canonical folder; never treat different file formats as separate BOM items. Assembly uses sourced instructions only, or explicitly says no procedure has been established. Preserve existing technical notes and interactive explorer links.

## Visual language

Use a white page, dark text and restrained teal accents. Prefer actual catalogue geometry, a warm neutral studio background and clear views. Do not use decorative badges or infer measured dimensions from pictures. Store images once beside the canonical part; root images may reuse them. Mark AI illustrations when their provenance is known. A rendered or generated picture is not a photograph or proof of fit.

## Data and editing contract

Use relative links with URL-encoded paths. Escape Markdown table values. Do not fabricate supplier numbers, short codes, stock, prices, BOM quantities or installation steps. Keep specialist data and original notes. Generated sections use explicit markers and fail on malformed markers. Rebuild code and templates with outputs; never leave a hand-edited output that its next build will discard.
