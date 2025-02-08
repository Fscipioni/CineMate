import faiss
import pickle
import numpy as np
import torch
from sentence_transformers import SentenceTransformer
import os

class MovieRetriever:
    def __init__(self, model_name="intfloat/e5-large-v2", index_path="../Data/embeddings/faiss_index.bin", metadata_path="../Data/embeddings/movie_metadata.pkl"):
        """
        Loads FAISS index and metadata for similarity search.
        """
        self.model = SentenceTransformer(model_name, device="cuda" if torch.cuda.is_available() else "cpu")

        if not os.path.exists(index_path) or not os.path.exists(metadata_path):
            raise FileNotFoundError("Error: FAISS index or metadata not found. Run the embedding generator first.")

        self.index = faiss.read_index(index_path)

        # Load movie metadata
        with open(metadata_path, "rb") as f:
            self.movie_metadata = pickle.load(f)

    def search_movies(self, query, top_k=5):
        """
        Finds similar movies based on user input.

        Parameters:
            query (str): User search query.
            top_k (int): Number of similar movies to return.

        Returns:
            List of full movie metadata dictionaries.
        """
        query_embedding = self.model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_embedding, top_k)

        results = [self.movie_metadata[idx] for idx in indices[0]]
        return results 