from pathlib import Path

import papermill as pm

confirmed_products_dir = Path(
    "../../dist-s1-research/marshak/Zg_validation_variation/val_products_transformer_optimized-max10_processed_2026-02-05"
)
dist_s1_ts_dirs = list(confirmed_products_dir.glob("*/"))


out_nbs = Path("out_nbs")
out_nbs.mkdir(exist_ok=True)

for ts_dir in dist_s1_ts_dirs:
    print(f"Generating table for {ts_dir}")
    pm.execute_notebook(
        "1_generate_dist_s1_table.ipynb",
        out_nbs / f"1_generate_dist_s1_table__{ts_dir.name}.ipynb",
        parameters=dict(TS_DIR=str(ts_dir)),
    )
