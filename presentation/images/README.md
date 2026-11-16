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
