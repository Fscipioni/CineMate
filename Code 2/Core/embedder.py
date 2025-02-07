import pandas as pd
import torch
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
from .data_loader import load_movie_dataset

class MovieEmbedder:
    def __init__(self, model_name="intfloat/e5-large-v2"):
        """
        Initializes the embedding model and FAISS index.
        """
        self.model = SentenceTransformer(model_name, device="cuda" if torch.cuda.is_available() else "cpu")
        self.index = None  # FAISS index will be created later

    def generate_embeddings(self, movie_df):
        """
        Generates embeddings for the movie dataset.

        Parameters:
            movie_df (pd.DataFrame): The movie dataframe with metadata.

        Returns:
            np.ndarray: Numpy array of movie embeddings.
        """
        print("Generating embeddings...")
        embeddings = self.model.encode(movie_df["embedding_text"].tolist(), convert_to_numpy=True)
        return embeddings

    def save_embeddings(self, embeddings, movie_df, index_path="../Data/embeddings/faiss_index.bin", metadata_path="../Data/embeddings/movie_metadata.pkl"):
        """
        Stores embeddings in FAISS and saves movie metadata separately.

        Parameters:
            embeddings (np.ndarray): Generated embeddings.
            movie_df (pd.DataFrame): Movie dataset with metadata.
        """
        d = embeddings.shape[1]  # Embedding dimensions
        self.index = faiss.IndexFlatL2(d)
        self.index.add(embeddings)

        # Save FAISS index
        faiss.write_index(self.index, index_path)

        # Store full metadata (excluding embeddings)
        movie_metadata = movie_df[['tconst', 'title', 'year', 'genre', 'director', 'actors', 
                                   'plot', 'country', 'awards', 'rating', 'votes']].to_dict(orient='records')

        with open(metadata_path, "wb") as f:
            pickle.dump(movie_metadata, f)

        print(f"Embeddings and metadata saved successfully!")

# if __name__ == "__main__":
#     dataset_path = "../Data/processed/movies_dataset_final.csv"
#     movie_df = load_movie_dataset(dataset_path)

#     embedder = MovieEmbedder()
#     embeddings = embedder.generate_embeddings(movie_df)
#     embedder.save_embeddings(embeddings, movie_df)