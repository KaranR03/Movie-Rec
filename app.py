import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3523854faccab32db9b8b8d4e835f54a&language=en-US'.format(movie_id))
    data = response.json()

    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def fetch_description(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3523854faccab32db9b8b8d4e835f54a&language=en-US'.format(movie_id))
    data = response.json()

    return data['overview']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append((movies.iloc[i[0]].title, fetch_poster(movie_id), fetch_description(movie_id)))
    return recommended_movies

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Enter the Name of the Movie you like to be recommended",
    movies['title'].values)



if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    num_columns = 5
    num_recommendations = len(recommendations)
    num_rows = (num_recommendations + num_columns - 1) // num_columns


    for i in range(num_rows):
        cols = st.columns(num_columns)
        for j in range(num_columns):
            index = i * num_columns + j
            if index < num_recommendations:
                movie_name, poster_url, description = recommendations[index]
                with cols[j]:
                    st.text(movie_name)
                    if st.image(poster_url, use_column_width=True, caption=movie_name):
                        st.write(description)
