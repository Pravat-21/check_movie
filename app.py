import streamlit as st
import pickle
import pandas as pd
import requests

similarity=pickle.load(open("similarity.pkl",'rb'))

def fetch_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=308f33cc9df0a0b9c4662bc7aeedf51b&language=en-US".format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data["poster_path"]


def recommended_movie(movie):
    movie_index=movies[movies["title"]==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended=[]
    recommended_poster=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        # fatching the poster

        recommended.append(movies.iloc[i[0]].title)  
        recommended_poster.append(fetch_poster(movie_id))

    return recommended,recommended_poster

movie_dict=pickle.load(open("movies_dict.pkl",'rb'))
movies = pd.DataFrame(movie_dict)



st.title("Movie Recommendation System")
selected_movie_name=st.selectbox(
    "Welcome to the movie search",
    movies["title"].values 
)
if st.button("Recommend"):
    name,poster=recommended_movie(selected_movie_name)
    col1, col2, col3 ,col4,col5= st.columns(5)

    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col2:
        st.text(name[1])
        st.image(poster[1])
    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])





