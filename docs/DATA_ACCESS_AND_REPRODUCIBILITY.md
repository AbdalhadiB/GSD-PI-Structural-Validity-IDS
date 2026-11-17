# Source data access and units

| Dataset | Unit/graph in this release | Data supplied? | Interpretive restriction |
|---|---|---|---|
| NF-ToN-IoT-v2 / NF-CSE-CIC-IDS2018-v2 | Positive-degree source IP, distinct destination IP out-degree | No original source-entity tables; only aggregate outputs | Benchmark dataset captures are independent despite sharing a feature schema |
| WTMC2021 | Separate 47 active-source full-capture graph and 593 source–window companion units | Executed notebook, no raw capture | Do not pool RCI across different units or use 19,060 all-node denominator for source-base-rate lift |
| CTU-13 scenario 1 | Positive-degree sources, source labels with unknown category | Aggregates + executed notebook | Parser must recognize `flow=`; many sources have unknown status |
| CIDDS-001 OpenStack | Active source, distinct destination IP out-degree | Pooled and four temporal weekly aggregate outputs | Weeks are dependent partitions of one capture; many selected sources Normal-only |
| Operational HTTPS service | Source IP→requested path bipartite graph | **No raw/individual production data** | Different graph meaning; only aggregate within-schema temporal descriptions; not matched benchmark validity |

**Reproduction level:** Source-based script execution requires acquisition of original datasets, verification of licenses and setup of expected local/Drive paths. This repository is a revision-evidence collection, not an instant one-click raw-data reproduction.
