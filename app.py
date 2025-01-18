import streamlit as st
import pickle
import pandas as pd
import requests
from io import BytesIO

# Function to fetch poster from API
def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=40d78fbc064f4c7ef0f40b0795b72df7&&language=en-US'.format(movie_id)
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))  # Fetch poster URL
    return recommended_movies, recommended_movies_posters

# Download .pkl files from GitHub Releases
@st.cache_data
def load_data():
    # Replace with your GitHub release download URLs
    movie_dict_url = "https://github.com/atheeq2003/Movie-Recommendation-System/releases/download/files/movie_dict.pkl"
    similarity_url = "https://github.com/atheeq2003/Movie-Recommendation-System/releases/download/files/similarity.pkl"

    # Download movie_dict.pkl
    response = requests.get(movie_dict_url)
    movies_dict = pickle.load(BytesIO(response.content))

    # Download similarity.pkl
    response = requests.get(similarity_url)
    similarity = pickle.load(BytesIO(response.content))

    return pd.DataFrame(movies_dict), similarity

# Load movie data and similarity matrix
movies, similarity = load_data()

# Streamlit UI
st.title('Movie Recommender System')

# Dropdown to select a movie
selected_movie_name = st.selectbox('Choose a movie to recommend similar movies: ', movies['title'].values)

# Recommend button logic
if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    # Create dynamic columns for recommendations
    cols = st.columns(len(names))
    for i, col in enumerate(cols):
        with col:
            st.text(names[i])  # Display movie name
            st.image(posters[i])  # Display movie poster
