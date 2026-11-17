# Dependencies

The notebooks contain their own Colab install cells and some refer to Google Drive / Kaggle paths. Do not treat this list as a locked environment or universal installer:

- Python 3.10+ (selected D7 profiling run recorded Python 3.13.18)
- numpy; pandas; scipy; matplotlib
- duckdb; psutil; requests (used by profiling/external-data notebooks)
- Google Colab / google.colab for browser notebook and Drive integration where used

D7's actual versions and resource measurements: `results/d7_profiling/d7_profile_environment.json`. The exact transitive dependencies and immutable container hashes were not recorded, so bitwise reproducibility is not claimed.
