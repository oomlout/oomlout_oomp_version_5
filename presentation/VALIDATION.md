# Documentation rollout validation

Validated 16 November 2026 after installing the final shared renderer.

Historical snapshot: the user subsequently reverted the electronics rollout.
Electronics and electronic projects are now maintained elsewhere and excluded
from further changes here. These results are not a claim about their current files.

- 11 local downstream repositories updated with generator source, configuration and outputs.
- 5,238 full-catalogue part pages generated; YAML mirrors retain their two-file part layout.
- 20,138 generated local links checked with zero failures. Retained legacy notes are outside this link audit.
- Ten base unit tests passed, including deterministic generation, note preservation, malformed markers, lightweight exports and repeatable installer hooks.
- A real part page in each populated full catalogue was regenerated again without byte changes.
- Installed Python generators and modified orchestration/export modules compiled successfully.
- The base directory's local links and staged whitespace checks passed; its representative render was visually inspected.

This validates documentation generation, not CAD geometry, electrical suitability, manufacturer data or remote link availability inside retained notes. No CAD, AI or asset-deletion pipelines were executed.

The base changes are committed. Downstream generator/output changes remain local and uncommitted, preserving separation from pre-existing work in electronics, breakouts and bolts. No repositories were pushed. The electronic-project repository was inspected on GitHub only and is listed as a follow-up in [the audit](REPOSITORIES.md).

| Local repository | Records | Generated local links checked |
| --- | ---: | ---: |
| `oomp_bearing_version_5` | 0 | 1 |
| `oomp_mechanical_version_5` | 164 | 660 |
| `oomp_electronic_version_5` | 3,881 | 14,721 |
| `oomp_electronic_breakout_version_5` | 105 | 379 |
| `oomp_hardware_screw_version_5` | 833 | 3,336 |
| `oomp_electronic_verison_5_pretty` | 0 | 2 |
| `oomp_hardware_bolt_version_5` | 253 | 1,016 |
| `oomp_electronic_version_5_only_yaml` | 3,881 | 4 |
| `oomp_hardware_screw_version_5_only_yaml` | 833 | 4 |
| `oomp_hardware_bolt_version_5_only_yaml` | 253 | 4 |
| `oomp_electrical_extension_lead_uk_socket_6_outlet_pro_elec_2068_version_5` | 2 | 11 |
