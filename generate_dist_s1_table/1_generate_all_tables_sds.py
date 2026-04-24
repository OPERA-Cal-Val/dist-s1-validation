from pathlib import Path

import papermill as pm
from tqdm.auto import tqdm
import pandas as pd

with open("products_in_s3.txt") as f:
    products = list([line.strip() for line in f.readlines()])

df = pd.DataFrame({"opera_id": products})
df["mgrs_tile_id"] = df["opera_id"].map(lambda x: x.split("_")[3][1:])
df = df.sort_values(by="opera_id").reset_index(drop=True)

mgrst_tile_ids = df.mgrs_tile_id.unique().tolist()

out_nbs = Path("out_nbs_sds")
out_nbs.mkdir(exist_ok=True)

for mgrs_tile_id in tqdm(mgrst_tile_ids):
    print(f"Generating table for {mgrs_tile_id}")
    pm.execute_notebook(
        "1_generate_dist_s1_table_sds.ipynb",
        out_nbs / f"1_generate_dist_s1_table__{mgrs_tile_id}.ipynb",
        parameters=dict(MGRS_TILE_ID=mgrs_tile_id),
    )
