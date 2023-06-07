
import sys
import os
import pandas as pd
import pickle
from os.path import exists

from movie_sentiment.ml_logic.movie_score import movie_score
from movie_sentiment.ml_logic.polynomial import script_2_polynomial
from movie_sentiment.params import *


def generate_all_arcs():
    ''' Generates a dictionnary with the arcs of all movies.
    Same parameters as in the split_movie_script can be applied
    '''

    # getting the list of file names of all scripts
    movie_list = os.listdir(RAW_SCRIPTS_PATH)

    arcs = {}

    for index, movie_file in enumerate(movie_list):

        # printing progress
        sys.stdout.write('\r')
        sys.stdout.write(f"{index+1}/{len(movie_list)} movies arcs generated")
        sys.stdout.flush()

        # get the arc from the movie
        arc_score = movie_score(
            movie_file,
            chunk_type='sentence',
            pad=50,
            group_chunk=10,
            window_size=50
        )

        # get the movie name and movie id from file name (id is not used but could be later)
        movie_name, movie_id = movie_file.strip('.txt').split('_')

        # add to the dictionnary
        arcs[movie_name] = arc_score

    # Save in pickle file
    print('Saving in pickle file')
    with open(DICT_PICKLE_FILE, 'wb') as handle:
        pickle.dump(arcs, handle, protocol=pickle.HIGHEST_PROTOCOL)

    return arcs


def get_all_arcs():

    if os.path.exists(DICT_PICKLE_FILE) == True:
        print('Loading data from pickle file')
        with open(DICT_PICKLE_FILE, 'rb') as handle:
            arcs = pickle.load(handle)

    else:
        print('Generating data for movie arcs')
        arcs = generate_all_arcs()

    return arcs


def get_all_polynomials():

    arcs = get_all_arcs()
    poly = {}

    for key, value in arcs.items():
        poly[key] = script_2_polynomial(value)

    return pd.DataFrame(poly)
