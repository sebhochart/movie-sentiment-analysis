import pandas as pd
import numpy as np
import pickle
import os

from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD

from movie_sentiment.processing.arcs import get_all_reshaped_arcs
from movie_sentiment.params import *


def arcs_for_reco(standardize=True):
    '''Creates a DataFrame of arcs for all movies used in the recommendation algorithm
    Arcs are standardized if standardize=True
    '''

    arcs = get_all_reshaped_arcs(dyn_avg=True)

    # standardize the arcs if necessary
    if standardize == True:

        X = arcs.drop(columns='movie_name')

        s_scaler = StandardScaler()
        s_scaler.fit(X.T)
        scaled = s_scaler.transform(X.T)
        X_scaled = pd.DataFrame(scaled.T, columns=X.columns)

        columns_ids = [i for i in range(30)]

        for i in columns_ids:
            arcs[i] = X_scaled[i]

    # define movie_name as index
    df_arcs = arcs.set_index('movie_name')

    return df_arcs


def compute_meta_for_reco():
    '''Creates a DataFrame of metas for all movies used in the recommendation algorithm.
    Saves in a pickle file if it doesn't exist.
    '''
    # read metadata
    movie_meta = pd.read_csv(METADATA_PATH)

    # keep necessary columns
    movie_meta = movie_meta[['imdbid', 'title', 'keywords', 'genres']]

    # old code for genres + keywords
    movie_meta['meta'] = movie_meta['genres'] + ', ' + movie_meta['keywords']
    movie_meta['meta'] = movie_meta['meta'].str.replace(',', '')
    movie_meta['meta'] = movie_meta['meta'].fillna('')

    #use only genres
    movie_meta['genres'] = movie_meta['genres'].fillna('')

    # convert to numerical vectors
    count = CountVectorizer()
    count_matrix = count.fit_transform(movie_meta['genres'])
    count_df = pd.DataFrame(count_matrix.toarray(), index=movie_meta.index.tolist())

    # reduce to 20 dimensions (200 for genres + keywords)
    svd = TruncatedSVD(n_components=20)
    df_meta = svd.fit_transform(count_df)

    # convert to DataFrame
    df_meta = pd.DataFrame(df_meta, index=movie_meta.imdbid.tolist())

    # get id, movie name matching
    with open(IDS_PICKLE_FILE, 'rb') as handle:
        ids = pickle.load(handle)

    # match ids with movie names
    for key, value in ids.items():
        if key in df_meta.index:
            df_meta.loc[key,'movie_name'] = value

    # set movie name as index
    df_meta.set_index('movie_name', inplace=True)

    # Save in pickle file
    print('Saving in pickle file')
    with open(RECO_META_PICKLE_FILE, 'wb') as handle:
        pickle.dump(df_meta, handle, protocol=pickle.HIGHEST_PROTOCOL)

    print('Saved in pickle file')

    return df_meta


def meta_for_reco():
    '''Loads from pickle file the DataFrame of metas for all movies used in the recommendation algorithm.
    Generates the data if it doesn't exist.
    '''

    if os.path.exists(RECO_META_PICKLE_FILE) == True:
        print('Loading metadata from pickle file')
        with open(RECO_META_PICKLE_FILE, 'rb') as handle:
            df_meta = pickle.load(handle)

    else:
        print('Generating preprocessed meta data for all movies')
        df_meta = compute_meta_for_reco()

    return df_meta
