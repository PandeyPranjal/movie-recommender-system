# 🎬 Movie Recommendation System

## 📌 Overview
A content-based movie recommendation system that suggests similar movies based on user input using machine learning techniques.

---

## ⚙️ Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Streamlit  

---

## 🚀 Features
- Recommends movies based on similarity  
- Handles incorrect user input using fuzzy matching  
- Interactive web interface built with Streamlit  

---

## 🧠 How It Works
- Combined features: genres, keywords, cast, director  
- Converted text into vectors using TF-IDF  
- Calculated similarity using cosine similarity  
- Returned top similar movies  

---

## ▶️ Run Locally

```bash
git clone https://github.com/pandeypranjal/movie-recommender-system.git
cd movie-recommender-system
pip install -r requirements.txt
streamlit run app.py
