import streamlit as st
import pandas as pd
import requests
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import get_close_matches

# =====================================================
# CONFIG
# =====================================================

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

st.set_page_config(
    page_title="Bollywood Movie Recommendation",
    layout="centered"
)

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data():
    df = pd.read_csv("finalmaster_dataset_movie_cleaned.csv")
    df['title'] = df['title'].fillna('').str.lower().str.strip()
    df['genres'] = df['genres'].fillna('').str.lower()
    df['cast'] = df['cast'].fillna('').str.lower()
    df['rating'] = df['rating'].fillna(0)
    return df

df = load_data()

# =====================================================
# FEATURE ENGINEERING
# =====================================================

@st.cache_resource
def create_matrices(df):
    tfidf_genre = TfidfVectorizer(stop_words='english')
    tfidf_cast = TfidfVectorizer(stop_words='english')

    genre_matrix = tfidf_genre.fit_transform(df['genres'])
    cast_matrix = tfidf_cast.fit_transform(df['cast'])

    return genre_matrix, cast_matrix

genre_matrix, cast_matrix = create_matrices(df)

# =====================================================
# HELPER FUNCTIONS
# =====================================================

def find_closest_title(title):
    matches = get_close_matches(title, df['title'], n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_similarity_vector(idx, mode):
    matrix = genre_matrix if mode == "genre" else cast_matrix
    return cosine_similarity(matrix[idx], matrix).flatten()

# =====================================================
# RECOMMENDATION FUNCTION
# =====================================================

def recommend(movie_title, mode="genre", top_n=10):
    movie_title = movie_title.lower().strip()

    movie_title = find_closest_title(movie_title)
    if not movie_title:
        return None

    idx = df[df['title'] == movie_title].index[0]
    sim_scores = get_similarity_vector(idx, mode)

    scores = list(enumerate(sim_scores))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = []
    for i, score in scores:
        if i == idx:
            continue

        recommendations.append({
            "title": df.iloc[i]['title'],
            "genres": df.iloc[i]['genres'],
            "cast": df.iloc[i]['cast'],
            "rating": df.iloc[i]['rating'],
            "similarity": round(score * 100, 2)
        })

        if len(recommendations) == top_n:
            break

    return recommendations

# =====================================================
# TMDB POSTER FETCH (FIXED)
# =====================================================

@st.cache_data(show_spinner=False)
def get_poster(movie_title):
    if not TMDB_API_KEY:
        return None

    url = "https://api.themoviedb.org/3/search/movie"

    try:
        response = requests.get(
            url,
            params={
                "api_key": TMDB_API_KEY,
                "query": movie_title
            },
            timeout=5
        )
        response.raise_for_status()
        data = response.json()

        if data.get("results") and len(data["results"]) > 0:
            poster_path = data["results"][0].get("poster_path")
            if poster_path:
                return IMAGE_BASE_URL + poster_path

    except Exception as e:
        return None

    return None

# =====================================================
# UI
# =====================================================

st.title("🎬 Bollywood Movie Recommendation System")
st.markdown("Choose recommendation type: **Genre** or **Actor similarity**")

movie_name = st.text_input("🎥 Enter a movie name")

recommend_type = st.radio(
    "Choose recommendation type",
    ["Genre Based", "Actor Based"]
)

if st.button("Recommend"):
    if not movie_name.strip():
        st.warning("Please enter a movie name.")
    else:
        mode = "genre" if recommend_type == "Genre Based" else "actor"

        with st.spinner("Finding recommendations..."):
            results = recommend(movie_name, mode=mode)

        if not results:
            st.error("Movie not found. Try another name.")
        else:
            st.success(f"Top {len(results)} recommendations")

            cols = st.columns(2)

            for idx, r in enumerate(results):
                with cols[idx % 2]:
                    poster = get_poster(r["title"])

                    if poster:
                        st.image(poster, use_container_width=True)
                    else:
                        st.write("🎬 Poster not available")

                    st.markdown(f"### {r['title'].title()}")
                    st.write(f"**Genres:** {r['genres']}")
                    st.write(f"**Cast:** {r['cast']}")
                    st.write(f"⭐ Rating: {r['rating']}")
                    st.write(f"🎯 Similarity: {r['similarity']}%")
                    st.divider()