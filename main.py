import streamlit as st
import pickle
import numpy as np
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
from omdb import fetch_movie_details

# ------------------------------------------------
# LOAD PICKLE FILES
# ------------------------------------------------
df = pickle.load(open("movies_df.pkl", "rb"))
tfidf_matrix = pickle.load(open("tfidf_matrix.pkl", "rb"))
indices = pickle.load(open("indices.pkl", "rb"))  # can return series/arrays
tfidf = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# ------------------------------------------------
# FIX B: Safe way to convert any index to a single int
# ------------------------------------------------
def _get_single_index(idx):
    # idx might be: int, numpy.int64, list, array, pandas Series
    if isinstance(idx, (list, tuple, np.ndarray, pd.Series)):
        return int(idx[0])  # pick the first match
    return int(idx)

# ------------------------------------------------
# RECOMMEND FUNCTION (RAM SAFE + ERROR SAFE)
# ------------------------------------------------
def recommend(title, n=10):
    if title not in indices:
        return []

    raw_idx = indices[title]
    idx = _get_single_index(raw_idx)

    # similarity scores
    sim_scores = linear_kernel(tfidf_matrix[idx], tfidf_matrix).flatten()

    # sort
    sorted_idx = np.argsort(sim_scores)[::-1]

    # remove selected movie
    sorted_idx = sorted_idx[sorted_idx != idx]

    # top recommendations
    sorted_idx = sorted_idx[:n]

    recommendations = []

    for i in sorted_idx:
        if 0 <= i < len(df):
            movie_title = df.iloc[i]["title"]

            # Fetch details from OMDb
            movie = fetch_movie_details(movie_title)

            recommendations.append(movie)

    return recommendations


# ------------------------------------------------
# STREAMLIT UI
# ------------------------------------------------
st.title("🎬 Movie Recommendation System (NLP + TF-IDF)")
st.write("Select a movie and get top recommendations instantly!")

# movie dropdown
movie_list = df['title'].values
selected_movie = st.selectbox("Choose a movie:", movie_list)

if st.button("Recommend"):
    results = recommend(selected_movie)

    st.subheader("🎬 Top Recommendations")

    cols = st.columns(5)

    for idx, movie in enumerate(results):

        with cols[idx % 5]:

            st.image(movie["poster"], use_container_width=True)

            st.markdown(f"**{movie['title']}**")

            st.caption(f"⭐ {movie['rating']}")

            st.caption(f"📅 {movie['year']}")

            st.caption(movie["genre"])