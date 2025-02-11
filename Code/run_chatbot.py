import os
from Core.data_loader import load_movie_dataset
from Core.embedder import MovieEmbedder
from Core.chatbot import MovieChatbot

def check_embeddings():
    """
    Checks if embeddings and FAISS index exist, and generates them if missing.
    """
    embeddings_path = "../Data/embeddings/faiss_index.bin"
    metadata_path = "../Data/embeddings/movie_metadata.pkl"

    if not os.path.exists(embeddings_path) or not os.path.exists(metadata_path):
        print("⚠️ Embeddings not found, generating them now...")
        dataset = load_movie_dataset("../Data/movies.csv")
        embedder = MovieEmbedder()
        embeddings = embedder.generate_embeddings(dataset["plot"].fillna("No description available").tolist())
        metadata = dataset.to_dict(orient="records")
        embedder.save_faiss_index(embeddings, metadata, embeddings_path, metadata_path)
        print("✅ Embeddings successfully generated and stored.")

if __name__ == "__main__":
    check_embeddings()
    chatbot = MovieChatbot()
    while True:
        user_query = input("Ask about a movie: ")
        if user_query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = chatbot.chat(user_query)
        print("Bot:", response, flush=True)