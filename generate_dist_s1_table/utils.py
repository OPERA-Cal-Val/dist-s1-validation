import zipfile
from pathlib import Path
from dist_s1 import run_sequential_confirmation_of_dist_products_workflow


def unzip_file(zip_path, extract_to):
    zip_path = Path(zip_path)
    extract_to = Path(extract_to)
    
    subdirectory_name = zip_path.stem
    
    full_extract_path = extract_to / subdirectory_name
    full_extract_path.mkdir(parents=True, exist_ok=True)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(full_extract_path)
    
    return full_extract_path


def unzip_dist_s1_prod(zip_path: Path, unconfirmed_products_dir=None):
    mgrs_tile_id = zip_path.name.split('_')[3][1:]    

    if unconfirmed_products_dir is None:
        unconfirmed_products_dir = Path(f'unconfirmed_products')
    unconfirmed_products_dir.mkdir(parents=True, exist_ok=True)
    dst_dir = Path(f'unconfirmed_products/{mgrs_tile_id}')
    unzip_file(zip_path, dst_dir)
    return zip_path.name

def wrap_run_sequential_confirmation_of_dist_products_workflow(mgrs_tile_id, unconfirmed_products_dir=None, confirmed_products_dir=None):
    if unconfirmed_products_dir is None:
        unconfirmed_products_dir = Path('unconfirmed_products')
    unconfirmed_products_dir.mkdir(parents=True, exist_ok=True)

    if confirmed_products_dir is None:
        confirmed_products_dir = Path('confirmed_products')
    confirmed_products_dir.mkdir(parents=True, exist_ok=True)
    
    run_sequential_confirmation_of_dist_products_workflow(
        unconfirmed_products_dir / mgrs_tile_id, 
        confirmed_products_dir / mgrs_tile_id
    )