# CineMate
Movie Recommendation Chatbot




## Directory structure

CineMate/
│── 📂 Code/               # All Python scripts (organized for modularity)
│   │──data_loader.py       # Loads movies_dataset_final.csv
│   │── embedder.py          # Generates & stores embeddings
│   │── retriever.py         # Retrieves movies using FAISS
│   │── chatbot.py           # Chatbot logic with full metadata
│   │── run_chatbot.py       # ✅ Runs everything correctly
│
│── 📂 Data/              				# Organized dataset storage
│   │── 📂 raw/           				# Raw datasets (before processing)
│   │   │── README.md 						# Raw IMDb dataset download instructions
│   │   │── empire_top_100_movies.csv 		# List of [100 best movies of all times](https://www.empireonline.com/movies/features/best-movies-2/)
│   │   │── movie_data.pkl					# Movies information retrieved from OMDB
│   │
│   │── 📂 processed/     				# Cleaned & prepared movie dataset
│   │   │── movies_dataset_final.csv		# Movies dataset retrieved from OMDB and cleaned from missing values
│   │
│   │── 📂 embeddings/    				# Vectorized movie embeddings
│   │   │── faiss_index.bin				# FAISS index for fast retrieval
│   │   │── movie_embeddings.pkl			# Precomputed embeddings for movies
│
│── 📂 notebooks/         				# Jupyter notebooks for dataset preparation
│   │── Part_1-Data_Cleaning.ipynb
│   │── Part_2-Dataset_Preparation.ipynb
│
│── 📜 README.md          				# Project documentation  