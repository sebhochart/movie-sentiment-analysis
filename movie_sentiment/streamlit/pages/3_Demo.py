import streamlit as st
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
#from movie_sentiment.processing.arcs import get_all_dyn_arcs

 #API Set up
movie_sent_url = 'https://movsentapi-qthbj7hd7q-ew.a.run.app/arc'
movie_sent_url_local = 'http://127.0.0.1:8000/movies_list'
api_reponse = requests.get(movie_sent_url_local).json()

# the API response
movies_list = api_reponse['movies']

st.set_page_config(page_title="Movie Sentiment Analysis - Demo",
                   page_icon="🎥",
                   layout="wide")

with open('movie_sentiment/streamlit/pages/3_style.css') as style_css:
    st.markdown(f'<style>{style_css.read()}</style>', unsafe_allow_html=True)


with st.container():

    #movie arc section
    with st.container():

        st.title('Movie Sentiment Analysis')

        with st.spinner('Wait for it...'):
            time.sleep(3)

        movie_titles = sorted(movies_list)
        select_movie = st.selectbox('Select a movie', movie_titles )

        #API Set up
        movie_sent_url = 'https://movsentapi-qthbj7hd7q-ew.a.run.app/arc'
        movie_sent_url_local = 'http://127.0.0.1:8000/arc'
        params = dict(
            movie_title=select_movie,
            recommendation='active',
            polynomial='active'
            )

        api_reponse = requests.get(movie_sent_url_local, params=params).json()

        # the API response
        movie_arc = api_reponse['arc']
        movie_recom = api_reponse['recom']
        movie_poster = api_reponse['image']
        if movie_poster == "N/A":
            movie_poster = 'https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg'
        movie_score = api_reponse['classificatin_score']
        movie_cluster = api_reponse['classification_cluster']
        movie_poly_fit = api_reponse['poly_fit']




    with st.container():

        col1, col2 = st.columns([1,2.5])

        col1.subheader(select_movie)
        #col1.write("2003 - add meta data here")
        # poster
        col1.image(movie_poster)

        col2.subheader('Movie arc')
        #plotting the arc

        movie_arc_plot = {
            'Actual arc' : movie_arc,
            'Polynomial fit' : movie_poly_fit}

        movie_arc_plot_df = pd.DataFrame(movie_arc_plot)
        col2.line_chart(movie_arc_plot_df)
        # with col2:
        #     sns.lineplot(data=movie_arc_plot_df, pallete= ['#708D81', '#F4D58D' ])



        #col2.line_chart(movie_poly_fit)

        # plot info
        percentage_score = "{:.0%}".format(movie_score)
        movie_cluster_str = f"This movie has {percentage_score} similarity with **{movie_cluster}** arc."
        col2.write(movie_cluster_str)


    # recommendation container
    with st.container():
        st.header(' ')
        st.header(f'Did you like {select_movie}?')
        st.subheader('Checkout our recommendations!')

        with st.spinner('Wait for it...'):
            time.sleep(2)
        # recommendations
        #API Set up
        movie_sent_url = 'https://movsentapi-qthbj7hd7q-ew.a.run.app/recom'
        movie_sent_url_local = 'http://127.0.0.1:8000/recom'
        params = dict(
            movie_title=select_movie,
            )
        api_reponse = requests.get(movie_sent_url_local, params=params).json()
        api_reponse = pd.DataFrame(api_reponse)


        with st.container():
            col1, col2, col3, col4, col5= st.columns([2,3,1,2,3])

            col1.image(api_reponse.iloc[0,0])
            col2.subheader(f'{api_reponse.iloc[0,1]} - {api_reponse.iloc[0,2]}')
            col2.line_chart(api_reponse.iloc[0,3], height=250, use_container_width=True)

            col4.image(api_reponse.iloc[1,0])
            col5.subheader(f'{api_reponse.iloc[1,1]} - {api_reponse.iloc[1,2]}')
            col5.line_chart(api_reponse.iloc[1,3], height=250, use_container_width=True)


        with st.container():
            col1, col2, col3, col4, col5= st.columns([2,3,1,2,3])

        with st.container():
            col1, col2, col3, col4, col5= st.columns([2,3,1,2,3])

            col1.image(api_reponse.iloc[2,0])
            col2.subheader(f'{api_reponse.iloc[2,1]} - {api_reponse.iloc[2,2]}')
            col2.line_chart(api_reponse.iloc[2,3], height=250, use_container_width=True)

            col4.image(api_reponse.iloc[3,0])
            col5.subheader(f'{api_reponse.iloc[3,1]} - {api_reponse.iloc[3,2]}')
            col5.line_chart(api_reponse.iloc[3,3], height=250, use_container_width=True)


        with st.container():
            col1, col2, col3, col4, col5= st.columns([2,3,1,2,3])

        with st.container():
            col1, col2, col3, col4, col5= st.columns([2,3,1,2,3])

            col1.image(api_reponse.iloc[4,0])
            col2.subheader(f'{api_reponse.iloc[4,1]} - {api_reponse.iloc[4,2]}')
            col2.line_chart(api_reponse.iloc[4,3], height=250, use_container_width=True)

            col4.image(api_reponse.iloc[5,0])
            col5.subheader(f'{api_reponse.iloc[5,1]} - {api_reponse.iloc[5,2]}')
            col5.line_chart(api_reponse.iloc[5,3], height=250, use_container_width=True)
