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
