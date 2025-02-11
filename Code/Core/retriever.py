import faiss
import pickle
import numpy as np
import torch
from sentence_transformers import SentenceTransformer
import os

class MovieRetriever:
    def __init__(self, model_name="intfloat/e5-large-v2", index_path="../Data/embeddings/faiss_index.bin", metadata_path="../Data/embeddings/movie_metadata.pkl"):
        device = "mps" if torch.backends.mps.is_available() else "cpu"
        self.model = SentenceTransformer(model_name, device=device)
        self.index = faiss.read_index(index_path)
        
        with open(metadata_path, "rb") as f:
            self.metadata = pickle.load(f)

    def retrieve_movie(self, query, top_k=1):
        """
        Retrieves the closest matching movie for a given query.
        """
        query_embedding = self.model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_embedding, top_k)
        if indices[0][0] >= len(self.metadata):
            return {}
        return self.metadata[indices[0][0]]