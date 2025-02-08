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
        print("⚠️ Missing embeddings! Generating them now...")
        dataset_path = "../Data/processed/movies_dataset_final.csv"
        movie_df = load_movie_dataset(dataset_path)
    
        embedder = MovieEmbedder()
        embeddings = embedder.generate_embeddings(movie_df)
        embedder.save_embeddings_metadata(embeddings, movie_df)

        print("✅ Embeddings generated successfully!")

def run_chatbot():
    """
    Initializes and runs the CineMate chatbot.
    """
    print("\n🎬 CineMate - Your Personal Movie Assistant 🎥")
    print("🔍 Find movies based on their plot, genre, director, or actors.")
    print("💬 Type 'exit' anytime to quit.\n")

    check_embeddings()  # Ensure embeddings exist before running

    bot = MovieChatbot()
    bot.chat()

if __name__ == "__main__":
    run_chatbot()