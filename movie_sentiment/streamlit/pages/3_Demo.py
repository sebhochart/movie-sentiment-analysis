import streamlit as st

import numpy as np
import pandas as pd
from movie_sentiment.processing.arcs import get_all_dyn_arcs

st.set_page_config(page_title="Movie Sentiment Analysis - Demo",
                   page_icon="🎥",
                   layout="wide")

st.title('Movie Sentiment Analysis')

movie_titles = sorted(list(get_all_dyn_arcs().keys()))
select_movie = st.selectbox('Select a movie', movie_titles )

# columns = st.columns(3)


# columns[0].subheader('Select a movie')
# select_movie = columns[0].selectbox('', movie_titles )

# # select_movie = st.text_input('Select a movie', autocomplete=movie_titles )

# columns[1].markdown('## movie poster')
# columns[1].markdown('## curve from classification')

# columns[2].markdown('## recomendations')
