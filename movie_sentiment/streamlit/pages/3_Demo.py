import streamlit as st
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
from movie_sentiment.processing.arcs import get_all_dyn_arcs


st.set_page_config(page_title="Movie Sentiment Analysis - Demo",
                   page_icon="🎥",
                   layout="wide")
with st.container():

    with st.container():

        st.title('Movie Sentiment Analysis')

        movie_titles = sorted(list(get_all_dyn_arcs().keys()))
        select_movie = st.selectbox('Select a movie', movie_titles )

        #API Set up
        movie_sent_url = 'https://movsentapi-qthbj7hd7q-ew.a.run.app/arc'
        movie_sent_url_local = 'http://127.0.0.1:8000/arc'
        params = dict(
            movie_title=select_movie,
            recommendation=True
            )
        api_reponse = requests.get(movie_sent_url_local, params=params).json()

        # the API response
        movie_arc = api_reponse['arc']
        movie_recom = api_reponse['recom']
        movie_poster = api_reponse['image']
        movie_score = api_reponse['classificatin_score']
        movie_cluster = api_reponse['classification_cluster']



        with st.spinner('Wait for it...'):
            time.sleep(2.5)



    with st.container():

        col1, col2 = st.columns([1,2.5])

        col1.subheader(select_movie)
        # poster
        col1.image(movie_poster)

        col2.subheader('Movie arc')
        #plotting the arc
        col2.line_chart(movie_arc)

        # plot info
        movie_score_str = f"Arc score: {movie_score}"
        col2.write(movie_score_str)
        movie_cluster_str = f"This movie has a {movie_cluster} arc."
        col2.write(movie_cluster_str)


    # recommendation container
    with st.container():
        st.header(f'Did you like {select_movie}? checkout our recommendations!')
        # recommendations
        #API Set up
        movie_sent_url = 'https://movsentapi-qthbj7hd7q-ew.a.run.app/recom'
        movie_sent_url_local = 'http://127.0.0.1:8000/recom'
        params = dict(
            movie_title=select_movie
            )
        api_reponse = requests.get(movie_sent_url_local, params=params).json()

        st.dataframe(api_reponse)
