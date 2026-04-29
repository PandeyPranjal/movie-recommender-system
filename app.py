import streamlit as st
import pickle
import pandas as pd
from src.recommender import recommend

# Load data
data = pd.read_csv('data/movies.csv')
similarity = pickle.load(open('models/similarity.pkl', 'rb'))

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