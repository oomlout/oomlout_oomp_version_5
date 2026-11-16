# Directory illustrations

The five gallery previews are reduced from the hardware catalogues' full-detail
`three_d_model/render_high.png` images, preserving threads and complete geometry.
Do not substitute `render_low.png` or `render_product_low.png`: the current low
previews can depict simplified geometry.

Selections, labels and canonical IDs live in
[`data/directory_gallery.json`](../../data/directory_gallery.json).
[`gallery_sources.json`](gallery_sources.json) records source paths, dimensions
and SHA-256 hashes. Both source catalogues are read-only inputs.

Refresh the previews with Python and Pillow:

```powershell
python scripts/refresh_directory_images.py --repositories C:/gh
python scripts/generate_directory.py
```

The previews are 512 × 512 pixels, downsampled from 2048 × 2048 originals without
cropping or changing the object. Gallery names link to canonical part records;
images link to larger local previews. Objects are not shown to a common scale.

The examples are M3 × 10 mm countersunk and socket-cap screws, an M3 hex nut,
an M3 flat washer, and an M6 × 25 mm fully threaded hex-head set screw.

## Repository table samples

`data/directory_samples.json` also configures the directory table's Sample column.
Existing gallery previews are reused for core and hardware. Additional mechanical,
breakout and extension-lead samples are reduced to at most 512 pixels without
cropping; their source evidence is in `sample_sources.json`. The extension-lead
image depicts its holder, and the breakout image depicts a mounting plate.

Electronics and electronic projects reference their published 300-pixel images
directly, verified through GitHub on 16 November 2026. Their local repositories
are neither read nor modified. Bearings has no published sample in this inventory
and is labelled accordingly.
