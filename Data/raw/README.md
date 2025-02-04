# 📂 IMDb Raw Data

This directory contains the **raw IMDb datasets** required to build the CineMate movie database. Due to their large size, these files are **not included in this repository**. If necessary, you can manually download them from the official IMDb source.

---

## **📥 Download Instructions**
IMDb provides **non-commercial access** to its dataset via TSV (tab-separated values) files. Follow these steps to download the required files:

### **1️⃣ Go to the IMDb Dataset Repository**
🔗 [IMDb Datasets Download Page](https://datasets.imdbws.com/)

### **2️⃣ Download the Required Files**
Save the following files inside `Data/raw/`:
- `title.basics.tsv.gz` → Movie metadata (titles, genres, release years)
- `title.ratings.tsv.gz` → IMDb ratings (average rating, votes)
- `title.akas.tsv.gz` → Alternative titles (regional versions)
- `title.crew.tsv.gz` → Director and writer information
- `title.principals.tsv.gz` → Main cast & crew details
- `name.basics.tsv.gz` → Actors, directors, and known movies

### **3️⃣ Extract the Files**
After downloading, extract the `.gz` files using:
```bash
gunzip title.basics.tsv.gz
gunzip title.ratings.tsv.gz
gunzip title.akas.tsv.gz
gunzip title.crew.tsv.gz
gunzip title.principals.tsv.gz
gunzip name.basics.tsv.gz
```

# 🎯 Alternative: Use the Preprocessed Dataset

If you do not need to process the raw IMDb data, you can directly use the cleaned and preprocessed dataset located at:

📄 `Data/processed/movies_dataset_final.csv`

This file contains:
- Standardized movie metadata
- Cleaned missing values
- English titles for non-English movies
- IMDb ratings and votes
- Processed for embedding-based search

Simply load it in your script:

```
import pandas as pd
df = pd.read_csv("Data/processed/movies_dataset_final.csv")
```
