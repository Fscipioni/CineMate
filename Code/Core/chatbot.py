from Core.retriever import MovieRetriever
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class MovieChatbot:
    def __init__(self, llm_model="tiiuae/falcon-7b-instruct"):
        """
        Initializes the chatbot with a movie retriever and an LLM.
        """
        self.retriever = MovieRetriever()
        self.device = "mps" if torch.backends.mps.is_available() else "cpu"

        self.tokenizer = AutoTokenizer.from_pretrained(llm_model)
        self.model = AutoModelForCausalLM.from_pretrained(llm_model, torch_dtype=torch.float16, device_map=self.device)

    def chat(self, user_query):
        """
        Processes user query, retrieves relevant movie, and formulates a response.
        """
        movie = self.retriever.retrieve_movie(user_query)
        if not movie:
            return "I'm sorry, I couldn't find a relevant movie for your query."
        
        prompt = f"Tell me about the movie: {movie['title']}. {movie['plot']}"
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        with torch.no_grad():
            response_ids = self.model.generate(**inputs, max_new_tokens=50)
        return self.tokenizer.decode(response_ids[0], skip_special_tokens=True)