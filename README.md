# 🎬 Movie Recommendation System

A **content-based movie recommendation system** built with NLP and TF-IDF, deployed as an interactive **Streamlit** web application. Select any movie from a dataset of 45,000+ films and instantly get the top 10 most similar recommendations.

---

## 📌 Table of Contents

- [Demo](#-demo)
- [How It Works](#-how-it-works)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Dataset](#-dataset)
- [Model Details](#-model-details)
- [Contributing](#-contributing)

---

## 🚀 Demo

The app provides a simple dropdown to select a movie and a button to get recommendations:

```
Select a movie → Click "Recommend" → Get Top 10 Similar Movies
```

> **Run locally:** `streamlit run main.py`

---

## 🧠 How It Works

This is a **content-based filtering** system — it recommends movies based on the textual similarity of their content (plot, genre, tagline), not user ratings or collaborative data.

### Pipeline

```
movies_metadata.csv
        │
        ▼
  Data Cleaning & EDA
  (drop duplicates, handle nulls)
        │
        ▼
  Feature Engineering
  tags = overview + genres + tagline
        │
        ▼
  NLP Preprocessing
  (lowercase → remove punctuation →
   stopword removal → lemmatization)
        │
        ▼
  TF-IDF Vectorization
  (50,000 features, unigrams + bigrams)
        │
        ▼
  Serialize Artifacts → .pkl files
        │
        ▼
  Streamlit App (main.py)
  loads pickles → cosine similarity
  at query time → returns top N
```

---

## 🛠 Tech Stack

| Library | Version | Purpose |
|---|---|---|
| `streamlit` | 1.58.0 | Interactive web UI |
| `scikit-learn` | 1.9.0 | TF-IDF vectorizer + cosine similarity |
| `pandas` | 3.0.3 | Data loading & manipulation |
| `numpy` | 2.5.0 | Array operations |
| `nltk` | latest | Stopword removal & lemmatization (notebook only) |
| `uv` | latest | Fast Python package manager |

- **Python**: 3.13
- **Package Manager**: [`uv`](https://github.com/astral-sh/uv)

---

## 📁 Project Structure

```
Movie recommendation/
│
├── main.py                  # Streamlit app — loads models & serves UI
├── notebook.ipynb           # Full EDA, preprocessing & model training notebook
│
├── movies_df.pkl            # Cleaned & processed DataFrame (~29 MB)
├── tfidf_matrix.pkl         # Sparse TF-IDF feature matrix (~19 MB)
├── tfidf_vectorizer.pkl     # Fitted TfidfVectorizer object (~2 MB)
├── indices.pkl              # Title → DataFrame index mapping (~1.4 MB)
│
├── movies_metadata.csv      # Raw dataset (45,466 movies, 24 columns)
│
├── pyproject.toml           # Project metadata & dependencies (uv)
├── requirements.txt         # Pinned dependency list
├── .python-version          # Python 3.13
├── .gitignore
├── LICENSE
└── README.md
```

> 💡 Pre-built `.pkl` model artifacts are included so you can run the app immediately without re-training. To retrain from scratch, run all cells in `notebook.ipynb`.

---

## 🏁 Getting Started

### Prerequisites

- Python 3.13+
- [`uv`](https://github.com/astral-sh/uv) (recommended) **or** `pip`

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/movie-recommendation.git
cd movie-recommendation
```

### 2. Install dependencies

**With `uv` (recommended):**
```bash
uv sync
source .venv/bin/activate   # macOS / Linux
# .venv\Scripts\activate    # Windows
```

**With `pip`:**
```bash
pip install -r requirements.txt
```

### 3. Launch the app

```bash
streamlit run main.py
```

The app will open at `http://localhost:8501`.

> ✅ No dataset download or retraining needed — the pre-built model files are included in the repo.

---

## 📊 Dataset

**Source:** [The Movies Dataset — Kaggle](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)

| Property | Value |
|---|---|
| File | `movies_metadata.csv` |
| Raw rows | 45,466 movies |
| Columns | 24 (title, overview, genres, tagline, budget, revenue, etc.) |
| After cleaning | 45,447 rows |

**Features used for recommendations:**

| Column | Description |
|---|---|
| `overview` | Plot summary |
| `genres` | Genre labels (e.g., `Animation Comedy Family`) |
| `tagline` | Marketing tagline |

---

## 🔬 Model Details

### Text Representation

A `tags` column is created by concatenating `overview`, `genres`, and `tagline` per movie, then preprocessed with NLTK:

```python
text = text.lower()
text = re.sub(r'[^a-z\s]', ' ', text)               # remove punctuation & numbers
words = [w for w in text.split() if w not in stop_words]  # remove stopwords
words = [lemmatizer.lemmatize(w) for w in words]    # lemmatize to root form
```

### TF-IDF Vectorizer

```python
TfidfVectorizer(
    max_features=50000,   # vocabulary cap
    ngram_range=(1, 2),   # unigrams + bigrams
    stop_words='english'  # additional English stopword filter
)
# Output shape: (45,447 movies × 50,000 features)
```

### RAM-Safe Similarity

Instead of pre-computing the full 45K × 45K cosine similarity matrix (~8 GB RAM), similarity is computed **on-the-fly** for only the queried movie:

```python
sim_scores = linear_kernel(tfidf_matrix[idx], tfidf_matrix).flatten()
```

This keeps memory usage minimal regardless of dataset size.

---

## 🤝 Contributing

Contributions are welcome! Some ideas:

- [ ] Fetch and display movie posters via the TMDB API
- [ ] Incorporate cast/crew data for richer recommendations
- [ ] Add a hybrid model combining TF-IDF with collaborative filtering
- [ ] Deploy to Streamlit Cloud / Hugging Face Spaces

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

*Built with ❤️ using Python, scikit-learn, and Streamlit*
