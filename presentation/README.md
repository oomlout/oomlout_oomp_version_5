# OOMP documentation workflow

OOMP documentation has three levels: the base directory helps readers choose a repository; a catalogue introduces its family; each canonical part page identifies one exact record. Setup and regeneration belong in `README_GENERATOR.md`.

Read [the style contract](STYLE.md), [the implementation and rollout guide](CATALOGUE_REFRESH.md), and [the repository audit](REPOSITORIES.md).

## Regenerate

Run `python scripts/generate_directory.py` in the base repository. The directory source is `data/repositories.json`; GitHub discovery is a deliberate maintenance step, not a network dependency of rendering.

Installed catalogues have a self-contained `oomp_documentation.py`, a repository-specific `documentation.json`, and `action_documentation.py`. Run `python action_documentation.py` after the normal build. The local engine copy makes the checkout portable; update it from this repository when changing the contract. Python and PyYAML are required.

The generator reads existing `parts/*/working.yaml` and assets only. It never invokes AI, CAD, upstream fetches, or the asset deletion scripts. It preserves previous part notes in a collapsed block at the same location so relative links retain their meaning. Subsequent runs update only its marked block. Root introduction edits belong in `documentation.json`; setup edits belong in `README_GENERATOR.md`.

Lightweight YAML mirrors receive root documentation only. Their `parts` entries must remain exactly `working.yaml` and `image.png`; never install part READMEs there. Electronics' pretty repository is an exported presentation product; change its upstream exporter as well as any local documentation command.

## Verification

Run the generator twice and confirm the second run changes no bytes. Check generated links against the actual filesystem, inspect the representative image, and run the unit tests in the base repository. Preserve specialized manufacturer evidence, supplier references, electronics explorers, model conventions and build instructions. Do not claim a generic record has a verified assembly procedure.
