import pandas as pd
import torch
import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer
import os

class MovieEmbedder:
    def __init__(self, model_name="intfloat/e5-large-v2"):
        """
        Initializes the embedding model and FAISS index.
        """
        self.model = SentenceTransformer(model_name, device="cuda" if torch.cuda.is_available() else "cpu")
        self.index = None  

    def generate_embeddings(self, movie_plots):
        return self.model.encode(movie_plots, convert_to_numpy=True)

    def save_faiss_index(self, embeddings, metadata, index_path, metadata_path):
        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(embeddings)
        faiss.write_index(index, index_path)
        with open(metadata_path, "wb") as f:
            pickle.dump(metadata, f)