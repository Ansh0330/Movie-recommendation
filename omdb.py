import requests
import streamlit as st

API_KEY = st.secrets["OMDB_API_KEY"]


@st.cache_data(show_spinner=False)
def fetch_movie_details(movie_title):
    url = "https://www.omdbapi.com/"

    params = {
        "apikey": API_KEY,
        "t": movie_title
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Movie not found
        if data.get("Response") == "False":
            return {
                "title": movie_title,
                "year": "N/A",
                "poster": "assets/images.png",
                "rating": "N/A",
                "runtime": "N/A",
                "genre": "Unknown",
                "plot": "No description available."
            }

        # Poster not available
        poster = data.get("Poster")
        if poster == "N/A" or not poster:
            poster = "./assets/images.png"

        return {
            "title": data.get("Title", movie_title),
            "year": data.get("Year", "N/A"),
            "poster": poster,
            "rating": data.get("imdbRating", "N/A"),
            "runtime": data.get("Runtime", "N/A"),
            "genre": data.get("Genre", "Unknown"),
            "plot": data.get("Plot", "No description available.")
        }

    except Exception:
        return {
            "title": movie_title,
            "year": "N/A",
            "poster": "assets/images.png",
            "rating": "N/A",
            "runtime": "N/A",
            "genre": "Unknown",
            "plot": "No description available."
        }