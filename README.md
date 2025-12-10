# Validation for DIST-S1

## Installation

We use mamba to manage our python environment for reproducibility

```zsh
mamba env create -f environment.yml  # click yes
mamba activate dist-s1-val
python -m ipykernel install --name dist-s1-val --user  # to create a jupyter kernel matching the environment
```


## Usage

## Generating Tables for Validation

We generate (unconfirmed) product in the cloud. This simply means that the alert signals we capture are not analyzed over time.
In this repository, we:

1. Download the products
2. Perform the necessary confirmation
3. Generate a table that can be used for the final DIST-S1 validat

## Product Validation 

TBD


## Results
The overall global accuracies are in DISTperformannce.ipynb

Block accuracies and pixel accuracies are in the results folder.

The block table compared against all the reference change: https://github.com/OPERA-Cal-Val/dist-s1-validation/blob/main/results/blockaccuracy_ALLsub_high_firstprovconf_DIST-S1.csv
And against just vegetation loss: https://github.com/OPERA-Cal-Val/dist-s1-validation/blob/main/results/blockaccuracy_VLsub_high_firstprovconf_DIST-S1.csv

The statistics for the tables labeled "_high_" (linked above) are all for high magnitude product vs any reference change for users (commission) and high magnitude reference vs any magnitude product for producers (omission).

Note the tables area named blockaccuracy_REFERENCETYPE_MAGNITUDE_CONFIDENCELEVELS_DIST-S1 (e.g. blockaccuracy_ALLsub_high_firstprovconf_DIST-S1).

The pixel information can be found in similarly named tables (with lookback being how many days back in the reference table change is looked for for current disturbances): https://github.com/OPERA-Cal-Val/dist-s1-validation/blob/main/results/pointmatrix_VLsub_firstprovconf_DIST-S1_lookback30.csv
