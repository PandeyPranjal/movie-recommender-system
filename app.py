import streamlit as st
import pickle
import pandas as pd
from src.recommender import recommend
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

@st.cache_data
def compute_similarity(data):

    # 🔥 FIX: handle missing values FIRST
    features = ['genres', 'keywords', 'tagline', 'cast', 'director']
    
    for feature in features:
        data[feature] = data[feature].fillna('')

    # Combine features
    combined_features = (
        data['genres'] + " " +
        data['keywords'] + " " +
        data['tagline'] + " " +
        data['cast'] + " " +
        data['director']
    )

    # Vectorization
    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(combined_features)

    return cosine_similarity(feature_vectors)

# Load data
data = pd.read_csv('data/movies.csv')
similarity = compute_similarity(data)

st.title("🎬 Movie Recommendation System")

movie_name = st.text_input("Enter your favourite movie")

if st.button("Recommend"):
    if movie_name:
        recommendations, matched_movie = recommend(movie_name, data, similarity)

        if matched_movie:
            st.success(f"Showing results for: {matched_movie}")
            
            st.subheader("Recommended Movies:")
            for movie in recommendations:
                st.write(movie)
        else:
            st.error("Movie not found. Please try another name.")
    
    else:
        st.warning("Please enter a movie name")