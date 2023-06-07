import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os

#from preprocessing.scripts import split_movie_script
from movie_sentiment.ml_logic.vader import model as vadar
#from movie_sentiment_plot import movie_sentiment_plot

def movie_raw_score(movie_title, type, pad, lower, group_chunk):

    movie_script_splitted = split_movie_script(movie_title, type=type, \
                                               pad=pad, lower=lower, rm_stopwords=False, \
                                               lemmatize=False)

    movie_script_scored = vadar(movie_script_splitted, group_chunk)

    return movie_script_scored
