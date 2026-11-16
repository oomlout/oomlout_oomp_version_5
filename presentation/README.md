# OOMP documentation workflow

OOMP documentation has three levels: the base directory helps readers choose a repository; a catalogue introduces its family; each canonical part page identifies one exact record. Setup and regeneration belong in `README_GENERATOR.md`.

Read [the style contract](STYLE.md), [the implementation and rollout guide](CATALOGUE_REFRESH.md), and [the repository audit](REPOSITORIES.md), and [validation results](VALIDATION.md).

## Regenerate

Run `python scripts/generate_directory.py` in the base repository. The directory source is `data/repositories.json`; GitHub discovery is a deliberate maintenance step, not a network dependency of rendering.

The base directory table uses repository name/code as its primary order and link
label. Variant entries in `data/repositories.json` have `parent` and
`variant_label` fields and appear only as sublinks under their parent row.
The Sample column is configured in `data/directory_samples.json`; the five-image
hardware gallery remains configured in `data/directory_gallery.json`.
Run `python scripts/refresh_directory_images.py` to rebuild small previews from
the full-detail hardware renders and the additional local table samples. This
optional image step requires Pillow and reads only the explicitly allowed bolt,
screw, mechanical, breakout and extension-lead source repositories. Electronics
and electronic projects use small published image URLs from their own READMEs;
their local files are never read or modified by this image step. Normal README
generation uses the checked-in configuration and does not read other checkouts.

**Ownership boundary:** `oomp_electronic_version_5` and
`oomp_electronic_project_version_5` are maintained elsewhere. Do not modify or
regenerate their files. The user reverted the earlier electronics rollout;
historical validation results do not describe its current state. Keep their
directory links; the installer and base documentation generator reject these two repositories.

Installed catalogues have a self-contained `oomp_documentation.py`, a repository-specific `documentation.json`, and `action_documentation.py`. Run `python action_documentation.py` after the normal build. The local engine copy makes the checkout portable; update it from this repository when changing the contract. Python and PyYAML are required.

The generator reads existing `parts/*/working.yaml` and assets only. It never invokes AI, CAD, upstream fetches, or the asset deletion scripts. It preserves previous part notes in a collapsed block at the same location so relative links retain their meaning. Subsequent runs update only its marked block. Root introduction edits belong in `documentation.json`; setup edits belong in `README_GENERATOR.md`.

Lightweight YAML mirrors receive root documentation only. Their `parts` entries must remain exactly `working.yaml` and `image.png`; never install part READMEs there. Electronics' pretty repository is an exported presentation product; change its upstream exporter as well as any local documentation command.

## Verification

Run the generator twice and confirm the second run changes no bytes. Check generated links against the actual filesystem, inspect the representative image, and run the unit tests in the base repository. Preserve specialized manufacturer evidence, supplier references, electronics explorers, model conventions and build instructions. Do not claim a generic record has a verified assembly procedure.
