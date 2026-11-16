# OOMP version 5 repository audit

Audited 16 November 2026. GitHub discovery searched both pages of `user:oomlout oomp in:name` (190 results) and selected `version_5` plus the existing `verison_5` spelling. This found 13 repositories. Scope is the public `oomlout` account, not all forks or private repositories. The reproducible directory inventory is [repositories.json](../data/repositories.json).

**Later ownership update:** the user has reverted the electronics changes and is
handling `oomp_electronic_version_5` and `oomp_electronic_project_version_5`
elsewhere. Do not touch either repository's files. Earlier rollout counts below
are historical; they do not authorize reinstating those changes. The base
directory continues to link both projects.

## Local repositories

Eleven downstream checkouts were found alongside the base library in `C:/gh`. The baseline installs a portable renderer, repository configuration, documentation command and secondary maintenance README. Full catalogues receive part pages; exports keep their existing lightweight layout. Existing specialist part notes are retained. The normal `working.run` path refreshes documentation last where that path exists; the dedicated command can also run after specialist entry points.

| Repository | Local metadata records | Attention still needed after the baseline |
| --- | ---: | --- |
| [Core library](https://github.com/oomlout/oomlout_oomp_version_5) | — | Maintain the directory inventory and distribute renderer changes to installed copies. |
| [Bearings](https://github.com/oomlout/oomp_bearing_version_5) | 0 | Populate and build actual records, then choose a representative image. Do not present source scripts as a finished catalogue. |
| [Mechanical](https://github.com/oomlout/oomp_mechanical_version_5) | 164 | Adapt dimension summaries for couplers, magnets and timing pulleys. Preserve the existing specialist README generator, source evidence and navigation. Run the documentation command after standalone specialist rebuilds. |
| [Electronics](https://github.com/oomlout/oomp_electronic_version_5) | 3,881 | Review component-family units and representative images; preserve board explorers, KiCad links and matching evidence. Existing uncommitted README/build changes were present before this task. |
| [Breakouts](https://github.com/oomlout/oomp_electronic_breakout_version_5) | 105 | Review pinouts, mounting dimensions and board variants; finish existing in-progress asset changes before publishing. Existing README edits and deleted assets were present before this task. |
| [Bolts, nuts and washers](https://github.com/oomlout/oomp_hardware_bolt_version_5) | 253 | Curate dimensional summaries and verified supplier links by hardware family. Existing changes to `working_three_d_model.py` are separate work. |
| [Screws](https://github.com/oomlout/oomp_hardware_screw_version_5) | 833 | Review thread, head, drive and length summaries; preserve nominal/display-model conventions and supplier provenance. |
| [Extension lead](https://github.com/oomlout/oomp_electrical_extension_lead_uk_socket_6_outlet_pro_elec_2068_version_5) | 2 | Improve product-specific description and image coverage using the actual manufacturer record. Do not infer electrical installation instructions. |
| [Electronics visual browser](https://github.com/oomlout/oomp_electronic_verison_5_pretty) | exported tree | Keep the published misspelling in links. Preserve its catalogue/explorers and apply upstream exporter changes, since this repository is a generated product. |
| [Electronics YAML](https://github.com/oomlout/oomp_electronic_version_5_only_yaml) | 3,881 | Publish the populated local export when ready; GitHub reported 0 KiB and its root README was unavailable. Retain the two-file part contract. |
| [Bolts YAML](https://github.com/oomlout/oomp_hardware_bolt_version_5_only_yaml) | 253 | Keep root documentation synchronized from the parent export pipeline; no part READMEs. |
| [Screws YAML](https://github.com/oomlout/oomp_hardware_screw_version_5_only_yaml) | 833 | Keep root documentation synchronized from the parent export pipeline; no part READMEs. |

Counts describe local `parts/*/working.yaml` snapshots, not a claim that all assets are complete or published. Navigation-only records are excluded from rendered catalogue counts.

## GitHub repository without a local checkout

[Electronic projects](https://github.com/oomlout/oomp_electronic_project_version_5) already has a useful picture-led introduction, project navigation, interactive board explorers and production guides. Its root still includes extensive setup and build instructions. It would benefit from moving that material into a secondary generator guide, retaining its existing project-specific pages, and adapting its source templates to the four-section structure where appropriate. Inspect its current instructions and generator before rollout; a generic hardware adapter would lose board-specific information. This repository was inspected remotely, not modified.

## GitHub publication priorities

1. Bearings and electronics YAML need publication/coverage attention first: GitHub returned 0 KiB and no root README at audit time, while local source/export folders exist.
2. Electronic projects is the additional remote-only candidate for a source-aware documentation refresh.
3. The other catalogues and exports benefit from publishing the local baseline after their existing uncommitted work has been reconciled. No push is performed by this documentation task.

## Source changes to retain

Each installed repository owns `documentation.json`, `oomp_documentation.py` and `action_documentation.py`; regenerate via `python action_documentation.py`. Full catalogue `working.py` orchestration refreshes documentation after assets. The three parent `working_only_yaml.py` exporters refresh an installed destination's root after copying files. Electronics' `generate_pretty_repository.py` refreshes an installed pretty destination after rebuilding its tree. These hooks are conditional on installed configuration for exported destinations, so existing uninstalled destinations remain supported.

Keep documentation-only generation separate from CAD/AI actions. The baseline verifies presentation structure and source preservation; it is not dimensional, electrical or fabrication validation.
