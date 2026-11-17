# GSD–PI Algorithm 1 v2 — execution evidence quality audit

**Audit date:** 2026-11-16  
**Scope:** the four user-uploaded artifacts (executed Colab notebook and three CSV outputs).  
**Source manuscript for comparison:** `Paper2_N1_N5_N8_Editorial_2026-11-15.docx`.

## 1. Findings

- The notebook contains 6 cells, including executed audit output. Its saved output confirms unit tests passed and the run completed for both development datasets.
- `GSD_PI_Audit_v2.csv`: 2 observations; `GSD_PI_Baselines_v2.csv`: 12 observations; `GSD_PI_Sensitivity_v2.csv`: 24 observations.
- Dataset-level counts and precision/recall/lift/tail-density arithmetic passed independent recalculation; Wilson precision intervals have not been assessed against the original source records, but are reported numerically in the output.
- A conditional exact hypergeometric same-size random-set calculation using the aggregates yields p-values matching those reported in the manuscript, but does not independently validate source labeling or sample independence.

| Dataset | N active | Labeled attackers | S | TP | FP | FN | Precision | Recall | Lift | Exact random-set p |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| NF-ToN-IoT-v2 | 23,079 | 31 | 11 | 10 | 1 | 21 | 0.909091 | 0.322581 | 676.80× | 4.134e-29 |
| NF-CSE-CIC-IDS2018-v2 | 224,568 | 648 | 11,571 | 301 | 11,270 | 347 | 0.026013 | 0.464506 | 9.02× | 6.350e-205 |

## 2. Manuscript correction

The P97 baseline for NF-CSE-CIC-IDS2018-v2 in the latest manuscript **Table VI** was printed as `d_out ≥ 31` with 6,829 selected. In the executed baseline CSV the **P97 percentile is 36.0**, with the same 6,829 selected and 257 true positives. The corrected manuscript therefore replaces this one cell with **`d_out ≥ 36`**. No other document part changed.

## 3. Sensitivity scope and limitations

The uploaded `GSD_PI_Sensitivity_v2.csv` varies `gamma_min` in {2,3,4,5} and `k_min` in {2,3,5}: 4×3 = 12 parameter combinations per dataset, 24 rows overall. ToN recovers 11 candidates/10 attacker-labeled at gamma_min 2, 3, 4 and abstains at gamma_min 5; CSE remains P95_REFERENCE_WEAK for all 12 combinations. This alone **does not** substantiate the manuscript's full one-at-a-time M4 grid for `delta_TC`, `top_k`, weak/strong MGR boundaries, or `k_min=12`; those require separate code/output evidence.

The notebook reads original **source-entity** tables (`src_key`, `out_degree`, `src_is_attacker`), not raw flow traces. The source-entity CSVs themselves, their version/cryptographic checksums, and the process that generated them are not included in this evidence package; therefore the audit is **not** an independent end-to-end replication. The full M5 Precision@k curve (k=1–200) and stage-level D7 runtime data are not contained in these four uploaded files.

A P95_REFERENCE_WEAK output is a **descriptive reference**, not a validated or endorsed detector, even though the CSV reports post-hoc reference-set statistics.

## 4. Security / publication readiness

No source-IP identifiers appear in the exported aggregate CSVs. A string-level check of notebook source code did not reveal inline API credentials; this is not a substitute for a complete private-data/security review before public publication. Do not publish raw source-IP joins or unredacted operational logs. Avoid claiming a versioned archival DOI until the corresponding release actually exists.

## 5. SHA-256 of submitted evidence files

- `GSD_PI_Algorithm1_Aligned_IEEE_Access_v2 (1).ipynb`: `9c28cb1da1a23116e9b8c5b8c07444d4f1c4089a03732e2e171aef7ee1fd09cc`
- `GSD_PI_Audit_v2.csv`: `d3a499055fd0df6ccc580fe0f44506295433d5373c6ddaf1440cd8e96bdd3d86`
- `GSD_PI_Baselines_v2.csv`: `d3baa5b483ee4598a27ecd2a4d0b3fcbc92f5479ac69be826002cb775000e75e`
- `GSD_PI_Sensitivity_v2.csv`: `4d42ae3c7dd78b94ba552fd35e21fc6a891ec7016265d8b99cd721474e0221f6`

## Verdict

**PASS for the two dataset-level operating-point outputs, the uploaded Top-k/P95/P97 baselines, and the narrow gamma_min/k_min sensitivity matrix.**

**NOT YET COMPLETE as the sole repository archive for M4, M5, D7, or the entire revised manuscript.**
