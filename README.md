# GSD–PI — Degree-Based Intrusion Screening (IEEE Access Revision)

**Manuscript:** *Structural Feasibility versus Attack Selectivity: A Pre-Deployment GSD–PI Diagnostic for Degree-Based Intrusion Screening*  
**Original IEEE Access manuscript:** `Access-2026-50411`  
**Status:** **RELEASE CANDIDATE — evidence curated, not an independently verified end-to-end reproduction.**  
**Prepared:** 16 November 2026.

## Purpose and scope

This repository candidate collects executable notebooks, measured aggregate results, statistical controls, and documentation supporting the revised GSD–PI manuscript. The structural diagnostic operates on **active source-IP out-degree** for benchmark *IP→IP* communication graphs; it does not establish that any selected source is malicious and does not evaluate graph neural networks. The website production *IP→requested-path* graph is **not interchangeable** with benchmark graphs; no identifiable production logs or external-IP reputation records are included here.

## Structure

| Location | Evidence | Reviewer concern |
|---|---|---|
| `notebooks/01_algorithm/` + `results/algorithm1/` | Executed corrected Algorithm 1 notebook and operating-point, baseline and narrow sensitivity CSV outputs | M1–M3 |
| `notebooks/02_wtmc/` | Executed WTMC2021 dual-protocol audit; *source cohort and source–window units are separate* | D3 |
| `notebooks/03_external/` + `results/m4_external/` | CTU-13 corrected parser, CIDDS-001 external tests and weekly aggregate outputs | M4 |
| `notebooks/04_behavioral/` + `results/d1_hybrid/` | Full-source, BENIGN-label-assisted B-channel audit | D1 |
| `notebooks/05_profiling/` + `results/d7_profiling/` | Runtime profiling notebook, measured stages and environment | D7 |
| `analysis/IEEE_Access_M4_Sensitivity_Audit.py` + `results/m4_sensitivity/` | Six-parameter one-factor-at-a-time sensitivity on the two development datasets; strong-candidate-only semantics | M4 |
| `analysis/m5_reproduce.py` + `results/m5_statistical/` + `figures/m5/` | Wilson intervals, exact hypergeometric null and tie-aware precision@k | M5 |
| `figures/static/` | Figure 2 enhanced raster image only (not code/data reproduction) | N4 |
| `exploratory/ugr16/` | Exploratory UGR'16 aggregate only, **not** a held-out independent validation | context |

## Quick start

1. Use Google Colab (or an equivalent Python environment) and load a notebook from `notebooks/`. Dependencies vary by notebook and are installed/read in their code; environment details for D7 are saved in `results/d7_profiling/d7_profile_environment.json`.
2. For Algorithm 1, obtain original `entity_table_NF-ToN-IoT-v2 (1).csv` and `entity_table_NF-CSE-CIC-IDS2018-v2.csv` (source-entity tables, **not provided**). Configure `INPUT_DIR` in the notebook. Run the built-in tests before the two dataset evaluations. Expected operating-point aggregate results are in `results/algorithm1/GSD_PI_Audit_v2.csv`.
3. WTMC2021/CTU-13/CIDDS-001 notebooks may download public datasets or reference Google Drive paths; inspect those source paths and legal/data-use permissions before rerunning.
4. `analysis/m5_reproduce.py` depends on full benchmark source-level degree and ground-truth files, which are **not** redistributed. Saved aggregate M5 statistics and curves are provided separately.
5. Compare your outputs against existing aggregate files and inspect `docs/` for methodological limitations. Use `SHA256SUMS.txt` for the released candidate's file-integrity hashes.

## Interpretation safeguards

- **Do not interpret `P95_REFERENCE_WEAK` as a positive security-validity verdict.** It is a *descriptive P95 reference* in a low-isolation, non-collapsed environment. The M4 one-factor-at-a-time isolation audit can report zero *strong candidates* for the same environment; those are different output semantics, not identical decision records. See `docs/POLICY_SEMANTICS.md`.
- Structural thresholds can be computed without labels. Attack-selectivity statistics, Wilson intervals and exact random-set tests are **retrospective** and label-conditioned.
- The duration-based behavioral B-channel is calibrated with **BENIGN-labeled flows**, and is not a prospective label-free behavioral detector.
- Small selected sets and source dependence limit precision/recall inference. The hypergeometric test assumes source-label exchangeability; it is not causal evidence.
- External data vary in ground-truth completeness; CTU-13 and CIDDS-001 unknown annotations are not benign labels.
- Runtime and RSS refer to **one measured rerun**, not a robust performance distribution or historical experimental time.
- The source-entity inputs and data provenance checksums are not bundled in this staged candidate. The complete M4 OAT CSV supplied by the author and the 99-line Python script reconstructed from the Project Library text are included; original script byte identity cannot independently be certified. See `docs/M4_SOURCE_PROVENANCE.md`. See `docs/OPEN_ITEMS_BEFORE_RELEASE.md`.

## Data protection

No production access logs, original visitor IP addresses, IP-level AbuseIPDB lookup files, secret API tokens, or benchmark per-source private joins are included. The D3 notebook's displayed output was redacted of two benchmark source-IP literals; **only those display strings were changed**, not executable code, numeric results or state. See `docs/REDACTION_NOTICE.md`.

## Citation, version and license

The manuscript is in revision and this candidate has no Zenodo DOI yet. Do **not** quote an archival DOI until the public archive actually exists. **No license has been selected**: before publishing, the author should select an appropriate software/data license, add full confirmed author/affiliation metadata, and produce a GitHub Release from the reviewed state. See `docs/PUBLISHING_CHECKLIST.md`.
