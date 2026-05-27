# GSD-PI-Structural-Validity-IDS
Pre-deployment diagnostic framework for graph-based intrusion detection (Paper 2)
# Topology-Conditioned Structural Validity: A Pre-Deployment 
# Diagnostic Framework for Graph-Based Intrusion Detection

## Overview
This repository contains the implementation code supporting the 
paper: "Topology-Conditioned Structural Validity: A Pre-Deployment 
Diagnostic Framework for Graph-Based Intrusion Detection."

## Repository Contents

| File | Description |
|------|-------------|
| `paper2_gsd_analysis.ipynb` | Complete GSD/PI analysis pipeline: downloads NF-UQ-NIDS-v2, computes GSD indicators, runs KDIS detection, validates cross-paradigm invariance |
| `figure3_ccdf.py` | Figure 3 generation: CCDF comparison of NF-ToN-IoT-v2 vs NF-CSE-CIC-IDS2018-v2 |

## Datasets
- **NF-UQ-NIDS-v2**: Available via [Kaggle](https://www.kaggle.com/datasets/dhoogla/nfuqnidsv2)
- **WTMC2021**: Available via [GitHub](https://github.com/GintsEngelen/WTMC2021-Code)
- **UNSW-NB15**: Available from [UNSW Cyber Range Lab](https://research.unsw.edu.au/projects/unsw-nb15-dataset)

## Requirements
pandas, numpy, matplotlib, scikit-learn

## Companion Study
The companion paper (KDIS framework) repository is available at:  
https://github.com/AbdalhadiB/KDIS-HGBF-ZeroDay-IDS

## Authors
Abdulhadi Albluwi, Mohamed I. Marie, Helal A. Suleiman  
Department of Information Systems, Faculty of Computers and 
Artificial Intelligence, Helwan University
