from pathlib import Path

import papermill as pm


confirmed_products_dir = Path("confirmed_products")
product_dirs = list(confirmed_products_dir.glob("*/"))
mgrs_tiles = [product_dir.name for product_dir in product_dirs]


out_nbs = Path("out_nbs")
out_nbs.mkdir(exist_ok=True)

for mgrs_tile_id in mgrs_tiles:
    print(f"Generating table for {mgrs_tile_id}")
    pm.execute_notebook(
        "1_generate_dist_s1_table.ipynb",
        out_nbs / f"1_generate_dist_s1_table__{mgrs_tile_id}.ipynb",
        parameters=dict(MGRS_TILE_ID=mgrs_tile_id),
    )
