import pandas as pd
import os

def load_movie_dataset(dataset_path: str) -> pd.DataFrame:
    """
    Loads the cleaned movie dataset.

    Parameters:
        dataset_path (str): Path to the processed movie dataset CSV file.

    Returns:
        pd.DataFrame: The loaded movie dataset.
    """
    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"Error: The dataset file '{dataset_path}' does not exist.")

    # Load dataset
    movie_df = pd.read_csv(dataset_path)

    # Create an 'embedding_text' column for similarity search
    movie_df['embedding_text'] = (
        "Plot: " + movie_df['plot'].fillna('') + ". " +
        "Genre: " + movie_df['genre'].fillna('') + ". " +
        "Director: " + movie_df['director'].fillna('') + ". " +
        "Actors: " + movie_df['actors'].fillna('')
    )

    return movie_df