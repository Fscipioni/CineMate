from Core.retriever import MovieRetriever

class MovieChatbot:
    def __init__(self):
        """
        Initializes the chatbot with a movie retriever.
        """
        self.retriever = MovieRetriever()

    def generate_movie_response(self, movie):
        """
        Generates a formatted response for a recommended movie.

        Parameters:
            movie (dict): Movie metadata.

        Returns:
            str: Formatted movie description.
        """
        title = movie.get("title", "Unknown Title")
        year = movie.get("year", "Unknown Year")
        genre = movie.get("genre", "Unknown Genre")
        director = movie.get("director", "Unknown Director")
        actors = movie.get("actors", "Unknown Actors")
        country = movie.get("country", "Unknown Country")
        awards = movie.get("awards", "No awards information available")
        rating = movie.get("rating", "N/A")
        votes = movie.get("votes", "N/A")

        return (
            f"🎬 *{title}* ({year}) is a *{genre}* movie from {country}.\n"
            f"🎥 Directed by {director}, starring {actors}.\n"
            f"🏆 {awards}.\n"
            f"⭐ IMDb Rating: {rating} (based on {votes} votes)."
        )

    def chat(self):
        """
        Runs the interactive chatbot session.
        """
        print("🎥 Welcome to CineMate! Type 'exit' to quit.")
        while True:
            query = input("\n🔍 Ask for a movie recommendation: ")
            if query.lower() == "exit":
                print("👋 Goodbye!")
                break

            recommendations = self.retriever.search_movies(query)

            if not recommendations:
                print("⚠️ No matching movies found. Try a different query!")
                continue

            print("\n🎬 Recommended Movies:")
            for movie in recommendations:
                print(self.generate_movie_response(movie))
                print("\n" + "-" * 50)

if __name__ == "__main__":
    bot = MovieChatbot()
    bot.chat()