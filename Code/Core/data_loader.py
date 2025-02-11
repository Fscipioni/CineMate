import pandas as pd
import os

def load_movie_dataset(dataset_path: str) -> pd.DataFrame:
    """
    Loads the cleaned movie dataset for embedding generation.
    """
    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"Error: The dataset file '{dataset_path}' does not exist.")
    return pd.read_csv(dataset_path)