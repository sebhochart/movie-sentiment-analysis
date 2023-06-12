import streamlit as st
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from movie_sentiment.processing.arcs import get_all_dyn_arcs


st.set_page_config(page_title="Movie Sentiment Analysis - Demo",
                   page_icon="🎥",
                   layout="wide")

st.title('Movie Sentiment Analysis')

movie_titles = sorted(list(get_all_dyn_arcs().keys()))
select_movie = st.selectbox('Select a movie', movie_titles )

# columns = st.columns(3)

movie_sent_url = 'https://movsentapi-qthbj7hd7q-ew.a.run.app/arc'

params = dict(
    movie_title="Up",
    recommendation=True
    )
api_reponse = requests.get(movie_sent_url, params=params).json()

movie_arc = api_reponse['arc']
movie_recom = api_reponse['recom']
movie_poster = api_reponse['image']

st.markdown(movie_arc)
#plt.plot(movie_arc)




# columns[0].subheader('Select a movie')
# select_movie = columns[0].selectbox('', movie_titles )

# # select_movie = st.text_input('Select a movie', autocomplete=movie_titles )

# columns[1].markdown('## movie poster')
# columns[1].markdown('## curve from classification')

# columns[2].markdown('## recomendations')
