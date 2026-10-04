# Kaggle-Projects
All Projects that I use to train my skills using Kaggle's vast database

## Reproduce the notebooks

Validated on Python 3.11.15 with the exact package versions in requirements.txt. Create an isolated virtual environment, install those requirements, then run:

    python scripts/validate_notebooks.py

The runner executes both notebooks from clean kernels, validates their structure, stops on any cell error, and saves executed copies under validation-output/. CSV files already included in this repository are used; no API credentials or dataset download is required. Full five-fold tuning can take several minutes.

Source notebooks keep outputs cleared; executed copies and dated results in each project README provide validation evidence.
