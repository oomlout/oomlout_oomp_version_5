# oomp_version_5

Python helpers for building and enriching OOMP-style part identifiers and related metadata.

This repository contains the core utilities used here to:

- build OOMP IDs from `taxonomy_1` to `taxonomy_15`
- generate short aliases from hashes
- derive BIP-39 word variants from MD5 values
- write per-part YAML files
- stage simple AI/template-driven asset generation workflows

## What It Does

At a high level, the code in this repo helps turn structured part metadata into repeatable identifiers and companion fields.

Main capabilities supported by the checked-in code:

- `oomp.py` builds part IDs, names, hash fields, short codes, and per-part `working.yaml` files
- `oomp_bip39.py` converts a 128-bit MD5 hex value into BIP-39-derived word variants
- `oomp_word.py` maps a 6-character hash fragment to a 3-word OOMP mnemonic
- `oomp_populate_helper.py` writes `parts_source/<oomp_id>/working.yaml` entries and can copy matching source assets when present
- `oomp_helper.py` prepares automation steps for image/icon generation, tracing, research prompts, and Jinja-based output files via `oomlout_roboclick`

## Repo Layout

- [`oomp.py`](oomp.py)  
  Core part-processing helpers. This is the main file to inspect first.

- [`oomp_bip39.py`](oomp_bip39.py)  
  BIP-39 conversion utilities built from the bundled word list.

- [`oomp_word.py`](oomp_word.py)  
  Custom 3-word mnemonic lookup for 6 hex characters.

- [`oomp_populate_helper.py`](oomp_populate_helper.py)  
  Helpers for writing populated part folders under `parts_source/`.

- [`oomp_helper.py`](oomp_helper.py)  
  Automation helpers for prompt-driven graphics, tracing, and Jinja output generation.

- [`source/bip_39_wordlist.txt`](source/bip_39_wordlist.txt)  
  Bundled source data for BIP-39 word generation.

- [`data/oomp_repo_list.yaml`](data/oomp_repo_list.yaml)  
  A checked-in related-repo list containing one OOMP repo URL.

## Setup

This repo is a plain Python workspace rather than a packaged library. 

External Oomlout modules referenced by the code:


- `oomlout_roboclick` from [`oomlout/oomlout_roboclick`](https://github.com/oomlout/oomlout_roboclick)

Notes:

- Functions in [`oomp.py`](oomp.py) also call `oomp_create_parts`, but that import is commented out in the current file. Those code paths appear to rely on another local or companion module not included here.
- No lockfile or pinned versions are present, so dependency versions are not defined in this repo.


Notes:

- [`requirements.txt`](requirements.txt) only includes dependencies that can be supported directly from the checked-in imports here.
- The Oomlout-specific modules are still listed separately because this repo does not define their package names or installation source.
- `oomlout_roboclick` is sourced from [`oomlout/oomlout_roboclick`](https://github.com/oomlout/oomlout_roboclick), which contains the `oomlout_roboclick.py` module used by [`oomp_helper.py`](oomp_helper.py).


## Related Repos

- [`oomlout/oomlout_roboclick`](https://github.com/oomlout/oomlout_roboclick)  
  Provides the `oomlout_roboclick` module imported by [`oomp_helper.py`](oomp_helper.py)

