# Frozen-policy output semantics

Three separate quantities must not be conflated:

1. **Structural isolation status:** descriptive state derived from the tail degree distribution (`MGR`, percentile collapse and admissible gaps). `MGR < 2` is **weak isolation**; `2 ≤ MGR < 5` is **boundary/inconclusive**; `MGR ≥ 5` identifies a candidate for stronger tail isolation, subject to the frozen rule and admissibility checks. None asserts maliciousness.
2. **Emitted set for evaluation:** Algorithm 1 v2 records a **P95 reference** (`P95_REFERENCE_WEAK`) when TC is false and MGR < 2. The benchmark NF-CSE-CIC-IDS2018-v2 yields threshold `d_out ≥ 22`, 11,571 sources and 301 attacker-labeled sources; this is a *benchmark reference*, not an endorsed security alert rule.
3. **Strong-candidate-only output:** the M4 sensitivity/OAT policy calls this environment `WEAK_ISOLATION` and emits **zero strong candidates**. That is not a contradiction in observed source degrees, but a distinct reporting contract. Never append one file's `selected` to another file's selected totals without recording the different semantics.

In particular, some earlier CTU/D7 notebook functions emit `P95_STABLE` for non-collapsed settings regardless of low MGR. The aligned v2 notebook instead labels this low-MGR branch as `P95_REFERENCE_WEAK`. Historical notebooks are retained as **executed evidence**, not asserted to be a single bit-identical implementation of v2. Rewriting previously executed notebooks would invalidate their provenance; harmonization should occur in future source updates, with versioned tests and rerun logs.

**M4 traceability update (16 Nov 2026):** The author-uploaded one-factor-at-a-time `IEEE_Access_M4_Sensitivity_OAT.csv` is now included under `results/m4_sensitivity/` (46 rows; six parameter axes). The 99-line `IEEE_Access_M4_Sensitivity_Audit.py` is reconstructed from the file text available in the Project Library and is supplied under `analysis/`. Both its structure and syntax were checked, but original-script binary/commit identity and a fresh full-input rerun remain unverified. The separately included `GSD_PI_Sensitivity_v2.csv` varies only `gamma_min` and `k_min`.
