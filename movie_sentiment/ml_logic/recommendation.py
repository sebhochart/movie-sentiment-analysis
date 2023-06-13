import pandas as pd
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

from movie_sentiment.processing.recommendation import arcs_for_reco, meta_for_reco
from movie_sentiment.params import *


def get_movies_recommendation(movie_title, n=6):
    '''Returns n movie recommendations based on the arc, the genre and movie keywords
    The output is a dictionnary containing a list of recommended movies and a list of the recommendation scores
    '''

    # get arc and metadata dataframes ready for recommentation
    df_arcs = arcs_for_reco()
    df_meta = meta_for_reco()

    # get the data of the movie we want to get recommendations for
    movie_arcs = np.array(df_arcs.loc[movie_title]).reshape(1, -1)
    movie_meta = np.array(df_meta.loc[movie_title]).reshape(1, -1)

    # compute similarities with all movies
    similarity_score1 = cosine_similarity(df_arcs, movie_arcs)
    similarity_score2 = cosine_similarity(df_meta, movie_meta)

    # store the scores in a DataFrame
    scores_df1 = pd.DataFrame(similarity_score1, index = df_arcs.index)
    scores_df1.sort_values(0, ascending=False, inplace=True)
    scores_df1.columns = ['arcs']

    scores_df2 = pd.DataFrame(similarity_score2, index = df_meta.index)
    scores_df2.sort_values(0, ascending=False, inplace=True)
    scores_df2.columns = ['meta']

    scores_df = pd.merge(scores_df1, scores_df2, left_index=True, right_index=True)

    # compute the global score and sort by higher scores
    scores_df['total'] = (scores_df['arcs'] + scores_df['meta']) / 2.0
    scores_df.sort_values(by=['total'], ascending=False, inplace=True)

    # removing the movie we are scoring so it's not recommended
    scores_df.drop([movie_title], inplace=True)

    # get the top n movies and their scores
    movie_names = scores_df[:n].index
    movie_scores = round(scores_df[:n]['total'], 2)

    recommended_movies = {
        'movie_names' : movie_names.to_list(),
        'movie_scores' : movie_scores.to_list()
    }

    return recommended_movies
