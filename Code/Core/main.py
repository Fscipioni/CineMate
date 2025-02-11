from Core.chatbot import MovieChatbot

if __name__ == "__main__":
    chatbot = MovieChatbot()
    while True:
        user_input = input("Ask about a movie: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = chatbot.chat(user_input)
        print("Bot:", response, flush=True)
