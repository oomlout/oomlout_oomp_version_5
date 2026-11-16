# OOMP catalogue refresh and maintenance

## Implemented baseline

`oomp_documentation.py` is the shared reference generator; each installed repository carries the same source and its own `documentation.json`. It produces concise roots, existing-image previews, exact metadata and preserved technical notes. `action_documentation.py` is an independent documentation-only command. This baseline does not replace specialist CAD, electronics, navigation or manufacturer evidence pipelines.

## Complete a family refresh

1. Inspect the repository's instructions, status, population code, templates and build entry points. Preserve unrelated work.
2. Confirm the canonical active part set and the original evidence for dimensions, compatibility and manufacturer identifiers. Distinguish unavailable outputs from unbuilt records.
3. Supply a useful family description and representative image. Improve per-family descriptions and dimensional summaries in the generating code, not just README outputs.
4. Retain existing navigation and explorers. For new taxonomy navigation, use natural numeric ordering, directory links and canonical assets; do not copy renders or YAML into navigation leaves.
5. Run specialist generators first and documentation last. Full refreshes cover every active record; filtered builds must not erase other records. Keep lightweight mirror exports compatible with their two-file contract.
6. Check relative links, metadata escaping, marker handling, absent images and deterministic regeneration. Inspect at least one part from each family visually. Preserve sourced assembly instructions; do not fill missing ones with guesses.
7. Commit only this work. Record outputs and remaining coverage honestly. Publishing, history rewriting and CAD redesign are separate actions.

## Next improvements beyond the baseline

Family-specific units and dimension tables, verified manufacturer links, curated representative images, natural taxonomy navigation and source-backed assembly instructions require repository-specific review. The audit distinguishes these from the shared documentation installation. Do not call a generic metadata page a completed engineering review.
