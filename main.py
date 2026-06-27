import streamlit as st
import pickle
import numpy as np
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
from omdb import fetch_movie_details
from style import get_css, get_sidebar_html, render_movie_card_html

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
# STREAMLIT UI — Premium Dark Emerald Redesign
# ------------------------------------------------

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CineMatch — Film Discovery",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Inject CSS ─────────────────────────────────────────────────────────────────
st.markdown(get_css(), unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown(get_sidebar_html(), unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# HERO SECTION
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero">
    <div class="hero-eyebrow">Content-Based Recommendation Engine</div>
    <h1 class="hero-title">Movie <span>Recommendation</span> System</h1>
    <p class="hero-subtitle">
        Discover your next favourite film through intelligent content-based
        recommendations powered by Natural Language Processing.
    </p>
    <div class="hero-rule"></div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# SELECTOR CARD
# ══════════════════════════════════════════════════════════════════════════════
# Centre the card using columns
_, card_col, _ = st.columns([1, 2.8, 1])

with card_col:
    st.markdown("""
    <div class="selector-card">
        <span class="selector-card-label">Step 1 — Choose a Film</span>
        <div class="selector-card-title">What are you watching tonight?</div>
        <p class="selector-card-desc">
            Select any film from our library of 45,000+ titles and we'll surface
            the ten most similar movies based on genre, themes, cast and tone.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Movie dropdown (Streamlit-native, CSS-overridden)
    movie_list = sorted(df['title'].dropna().unique().tolist())
    selected_movie = st.selectbox(
        label="Choose a movie",
        options=movie_list,
        label_visibility="collapsed",
    )

    recommend_clicked = st.button("✦  Get Recommendations", use_container_width=True)

# ══════════════════════════════════════════════════════════════════════════════
# RECOMMENDATIONS
# ══════════════════════════════════════════════════════════════════════════════
if recommend_clicked:
    # ── Loading state ──────────────────────────────────────────────────────
    with st.spinner("Analysing cinematic DNA  ·  curating recommendations…"):
        results = recommend(selected_movie)

    if not results:
        st.markdown("""
        <div class="empty-state">
            <div class="empty-state-icon">🎞</div>
            <div class="empty-state-text">
                We couldn't find recommendations for that title.<br>
                Try searching for a different film.
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # ── Section header ────────────────────────────────────────────────
        st.markdown(f"""
        <div class="reco-header">
            <div class="reco-eyebrow">Handpicked for you</div>
            <div class="reco-title">Because you watched &ldquo;{selected_movie}&rdquo;</div>
            <div class="reco-subtitle">{len(results)} recommendations · ranked by content similarity</div>
        </div>
        """, unsafe_allow_html=True)

        # ── Movie grid — 3 × 3 ────────────────────────────────────────────
        # Show top 9 results in a spacious, symmetrical 3-column grid
        grid_results = results[:9]
        num_cols = 3
        for row_start in range(0, len(grid_results), num_cols):
            row_movies = grid_results[row_start : row_start + num_cols]
            cols = st.columns(num_cols, gap="large")

            for col_idx, movie in enumerate(row_movies):
                with cols[col_idx]:
                    # Render card HTML (poster + metadata + truncated plot)
                    st.markdown(
                        render_movie_card_html(movie),
                        unsafe_allow_html=True,
                    )


        # ── Footer divider ────────────────────────────────────────────────
        st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# APP FOOTER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="app-footer">
    Crafted with ♥ using Python &amp; Streamlit &nbsp;·&nbsp;
    Data from <a href="https://www.themoviedb.org/" target="_blank">TMDB</a>
    &amp; <a href="https://www.omdbapi.com/" target="_blank">OMDb</a>
</div>
""", unsafe_allow_html=True)