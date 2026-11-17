# Unresolved items before immutable release

**Blocking for full D7/N8 provenance claim**

- **M4 files added:** Six-parameter OAT CSV was uploaded by the author and included unchanged; the 99-line script was restored from the Project Library text. Before claiming byte-for-byte archival provenance, optionally compare the script against the owner's original `.py` or its Git commit hash. No new run against the complete entity tables has been performed for this package update.
- Inspect `docs/POLICY_SEMANTICS.md` and ensure the manuscript and reviewer response consistently distinguish *P95 reference*, *strong structural candidate* and *abstention*.
- Add required provenance for the original source-entity tables, including source/origin, generation script and version/checksum if known. Do not guess any hash.
- Confirm notebook reproducibility in a **new environment** if claiming full independent execution. Existing Colab runs and CSV verification show saved evidence only.
- Review repository files for confidential content and author permissions a final time, including rendered notebook outputs.
- **License confirmed:** The repository already contains an MIT `LICENSE` file with `Copyright (c) 2026 Abdalhadi Albalawi`. Keep it intact. Before archival release, verify all coauthor credit/citation metadata and permissions for third-party material separately.
- After author approval, create GitHub Release, archive that exact release in Zenodo, verify DOI and update the final manuscript's Code Availability statement.

**Not mandatory to rerun large data merely for packaging**

- D7's measured single-run wall-clock and peak process RSS are already recorded; do not present them as stable runtime benchmarks.
- M5 exact-null and confidence interval results match the manuscript's retrospective statistics; the tests assume source-level conditional exchangeability.
- Figure 2 image is not a vector/recomputable plot without its source plotting code/data. The `figures/static` PNG is explicitly a static artifact.
- The missing degree-stratified representative AbuseIPDB sample from M6 remains unperformed. This release does not claim M6 was experimentally closed.
