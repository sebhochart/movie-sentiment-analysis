import streamlit as st

import numpy as np
import pandas as pd
from processing.arcs import get_all_dyn_arcs

st.set_page_config(page_title="Movie Sentiment Analysis",
                   page_icon="🎥",
                   layout="wide")

st.title(':movie_camera: Movie Sentiment Analysis :movie_camera:')

columns = st.columns(3)

movie_titles = sorted(list(get_all_dyn_arcs().keys()))


columns[0].subheader('Select a movie')
select_movie = columns[0].selectbox('', movie_titles )
# select_movie = st.text_input('Select a movie', autocomplete=movie_titles )

columns[1].markdown('## movie poster')
columns[1].markdown('## curve from classification')

columns[2].markdown('## recomendations')
