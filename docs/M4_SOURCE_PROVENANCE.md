# M4 one-factor-at-a-time sensitivity provenance

**Included CSV:** `results/m4_sensitivity/IEEE_Access_M4_Sensitivity_OAT.csv`

- Sourced from the author's 16 November 2026 upload `IEEE_Access_M4_Sensitivity_OAT(1).csv` and copied into the candidate unchanged.
- 46 data rows, 23 per development environment (NF-ToN-IoT-v2; NF-CSE-CIC-IDS2018-v2).
- Parameters varied one factor at a time: `delta_tc`, `mgr_low`, `mgr_high`, `gamma`, `k_min`, `top_k`, plus baseline.
- Counts satisfy `selected = TP + FP`; recorded precision and recall agree with their numerators and denominators wherever defined.

**Included script:** `analysis/IEEE_Access_M4_Sensitivity_Audit.py`

- Restored from the complete 99-line plain-text source returned by the current Project Library `IEEE_Access_M4_Sensitivity_Audit.py`. Python syntax checked; size 3,902 UTF-8 bytes.
- **Byte-for-byte equality with the original Python file was not independently certified**, because authorized original file-byte export from Project Library was unavailable. The restored script is thus an auditable text-source recovery, not a verified binary extraction.
- It requires the original active-source entity CSVs and NumPy. The current release candidate does not include those tables and does not claim a fresh full-input rerun of the M4 grid.

**Interpretation boundary:** The script implements a *strong-isolation-candidate* policy and reports `WEAK_ISOLATION` / zero **strong candidates** for NF-CSE-CIC-IDS2018-v2. Algorithm 1 v2 additionally reports a *descriptive* `P95_REFERENCE_WEAK` cohort (11,571), which is not a positive strong-candidate verdict. These have different selection contracts. Preserve both as separate historical outputs; do not silently relabel one as the other.

The output CSV does not contain source-IP columns or identifiable production telemetry.
