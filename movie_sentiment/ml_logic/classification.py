import pandas as pd
import numpy as np
import pickle
import os

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity

from movie_sentiment.processing.arcs import get_all_reshaped_arcs
from movie_sentiment.params import *


def classify_movie_arcs():
    '''This function classifies all movie arcs with a Kmeans algorithm and saves the result in a pickle file.
    It returns a DataFrame with:
    - the class of each movie
    - the score of similarity between each arc and its associated centroid
    and the centroid arcs.
    '''

    # get the reshaped arcs with dynamic average
    arcs = get_all_reshaped_arcs(dyn_avg=True)

    # define X for classification
    X = arcs.drop(columns='movie_name')

    # standard scale per movie (with transpose)
    s_scaler = StandardScaler()
    s_scaler.fit(X.T)
    scaled = s_scaler.transform(X.T)

    X_scaled = pd.DataFrame(scaled.T, columns=X.columns)

    # run a PCA
    pca = PCA()
    pca.fit(X_scaled)

    # project our data in the PCA space
    X_proj = pca.transform(X_scaled)
    X_proj = pd.DataFrame(X_proj, columns=[f'PC{i}' for i in range(1, X_scaled.shape[1]+1)])

    # fit a Kmeans model with the projected data
    km = KMeans(n_clusters=6, random_state=42)
    km.fit(X_proj)

    # save the 6 types of arcs (Kmeans cendroids)
    arc_kmeans = []
    for i in range(6):
        arc_kmeans.append(pca.inverse_transform(km.cluster_centers_[i]))

    # save the result of the classification in a dataframe
    classified_arcs = arcs.copy()
    classified_arcs['classification'] = km.labels_

    # replace with scaled data to compute similarity with centroid
    for i in range(30):
        classified_arcs[i] = X_scaled[i]

    # compute the similarity between each scaled arc and the centroid arc from the classification
    classification_scores = []

    for index, row in classified_arcs.iterrows():
        arc_columns = [i for i in range(30)]
        arc = row[arc_columns]
        centroid_arc = arc_kmeans[row['classification']]

        similarity = cosine_similarity(np.array(arc).reshape(1, -1), np.array(centroid_arc).reshape(1, -1))
        similarity = round(similarity[0][0], 2)

        classification_scores.append(similarity)

    # add the classification 'score' in the df
    classified_arcs['classification_score'] = classification_scores

    # keep only classification result and score
    classification_df = classified_arcs[['movie_name', 'classification', 'classification_score']].set_index('movie_name')

    # Save df in pickle file
    print('Saving df in pickle file')
    with open(CLASSIFIED_ARCS_PICKLE_FILE, 'wb') as handle:
        pickle.dump(classification_df, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print('Df saved in pickle file')

    # Save centroids in pickle file
    print('Saving centroids in pickle file')
    with open(CENTROID_ARCS_PICKLE_FILE, 'wb') as handle:
        pickle.dump(arc_kmeans, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print('Centroids saved in pickle file')

    return classification_df, arc_kmeans


def get_movie_arcs_classified():
    '''This function returns a DataFrame of classified arcs with:
    - the class of each movie
    - the score of similarity between each arc and its associated centroid
    The data is loaded from the pickle file if it exists, otherwise classification is ran.'''

    if (os.path.exists(CLASSIFIED_ARCS_PICKLE_FILE) == True) and (os.path.exists(CENTROID_ARCS_PICKLE_FILE) == True):
        print('Loading df from pickle file')
        with open(CLASSIFIED_ARCS_PICKLE_FILE, 'rb') as handle:
            classification_df = pickle.load(handle)

        print('Loading centroids from pickle file')
        with open(CENTROID_ARCS_PICKLE_FILE, 'rb') as handle:
            arc_kmeans = pickle.load(handle)

    else:
        print('Generating classification for all movies')
        classification_df, arc_kmeans = classify_movie_arcs()

    return classification_df, arc_kmeans


def get_movie_classification(movie_name):
    '''This function takes as an input the name of the movie and returns a tuple with:
    - the class
    - the classification score
    '''

    # loads all the movies classification
    classification_df = get_movie_arcs_classified()[0]

    # get classification and score for the movie asked
    classification = classification_df.loc[movie_name, 'classification']
    classification_score = classification_df.loc[movie_name, 'classification_score']

    # returns a tuple of class and score
    return ARCS_SHAPES[classification], classification_score
