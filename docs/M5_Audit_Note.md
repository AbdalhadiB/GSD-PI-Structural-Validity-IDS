# IEEE Access Paper 2 — M5 inferential audit (working revision)

## Scope and provenance
- Benchmark-only, source-level active cohorts.
- NF-ToN-IoT-v2 and NF-CSE-CIC-IDS2018-v2: rerun from complete original `out_degree` and `src_is_attacker` columns in entity tables, with prescribed selection thresholds 214 and 22 respectively.
- WTMC2021: audited aggregate N=47 active sources, A=8 attackers, selected n=3, TP=3 from `GSD_PI_Harmonized_Results_2026-11-13.csv`; original full per-source degree/attack vector is not supplied, so **no WTMC ranking curve is calculated**.
- No original source IPs are copied into any exported artifacts.

## Exact calculations
- Wilson (95% score) for precision TP/n and recall TP/A.
- Exact one-sided hypergeometric p: `hypergeom.sf(TP-1, N, A, n)`, null uniformly samples `n` distinct sources from `N` with `A` attackers.
- Lift for the active-source cohort: `(TP/n)/(A/N)`.
- ToN and CSE top-k precision: rank by descending unique-destination out-degree. For a tied cutoff, output exact attainable TP_min/TP_max under any ordering among equal-degree sources. Curves k=1..200; additional checkpoints up to 20,000 or available N in supplementary CSV. No outcome-based k optimization.

## Results

| Dataset | TP/n | 95% Wilson precision | TP/A | 95% Wilson recall | Expected TP random | Exact p | Lift |
|---|---|---|---|---|---|---|---|
| WTMC2021 | 3/3 | [0.4385,1] | 3/8 | [0.1368,0.6943] | 0.5106 | 0.003454 | 5.875x |
| NF-ToN-IoT-v2 | 10/11 | [0.6226,0.9838] | 10/31 | [0.1857,0.4986] | 0.014775 | 4.134e-29 | 676.804x |
| NF-CSE-CIC-IDS2018-v2 | 301/11,571 | [0.02327,0.02907] | 301/648 | [0.4264,0.5030] | 33.3886 | 6.350e-205 | 9.015x |

## Interpretation limits
1. Wilson CIs treat entities as independent; hosts may be correlated because of shared roles, infrastructure, or coordinated activity. They do not quantify capture-to-capture deployment variability.
2. Hypergeometric p-values test **source-label exchangeability** against a same-size random set. Tiny p-values show departure from this null, not a deployable detector, and cannot prove GSD-PI's label-free predictions.
3. NF-CSE-CIC presents the sharp contrast: very strong random-null evidence but just 2.60% precision and 11,270 labeled false-positive candidates.
4. WTMC n=3 has wide confidence bounds; its row is from previously audited aggregate data, not a new source-level rerun.
5. The two complete Top-k curves are **post-hoc diagnostics**, not the fixed Algorithm 1 outputs. The CSE policy n=11,571 lies well outside the 1–200 rank panel.
6. Production AbuseIPDB labels do not establish a verified negative class and are excluded from M5 inference pending M6.
7. No entity-cluster/temporal block bootstrap was calculated: source-level CSVs do not include an independent sampling/capture grouping suitable for such inference. Do not claim it.

## Papers and files
- `IEEE_Access_Paper2_M1_M5_Audited_Working_Revision.docx`: added Results Section V-K, Table XVI, Fig. 4 and limitations paragraph.
- `IEEE_Access_M1_M5_Response_Audited_Working.docx`: consolidated M5 response; other comments are still works in progress.
- `M5_Operating_Point_Wilson_ExactNull.csv`: operating-point audit with exact p-values.
- `M5_TieAware_PrecisionAtK.csv`: complete tie-aware rank grid, limited to two source-table datasets.
- `M5_PrecisionAtK_ToN.png`, `M5_PrecisionAtK_CSE.png`: separately generated figure panels.
- `m5_reproduce.py`: re-executable source-level numerical audit.

**Status:** M5 statistical evidence implemented, with an explicitly acknowledged WTMC rank-data limitation and cluster-dependence caveat. Not a clean, final IEEE resubmission. M6 and subsequent methodological comments remain unresolved.
