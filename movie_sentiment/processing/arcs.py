
import sys
import os
import pandas as pd
import pickle
from os.path import exists

from score_calculator.movie_raw_score import movie_raw_score


def generate_all_arcs():
    ''' Generates a dictionnary with the arcs of all movies.
    Same parameters as in the split_movie_script can be applied
    '''

    DICT_PICKLE_FILE = './processed_data/arcs_dict.pickle'

    # getting the list of file names of all scripts
    path = './raw_data/screenplay_data/data/raw_texts/raw_texts/'
    movie_list = os.listdir(path)

    arcs = {}

    for index, movie_file in enumerate(movie_list):

        # printing progress
        sys.stdout.write('\r')
        sys.stdout.write(f"{index+1}/{len(movie_list)} movies arcs generated")
        sys.stdout.flush()

        # get the arc from the movie
        arc_score = movie_raw_score(
            movie_title=movie_file,
            type='words',
            pad=50,
            lower=False,
            group_chunk=10
        )

        # get the movie name and movie id from file name (id is not used but could be later)
        movie_name, movie_id = movie_file.strip('.txt').split('_')

        # add to the dictionnary
        arcs[movie_name] = arc_score

    # Save in pickle file

    with open('arcs_dict.pickle', 'wb') as handle:
        pickle.dump(arcs, handle, protocol=pickle.HIGHEST_PROTOCOL)

    return arcs


def get_all_arcs():

    DICT_PICKLE_FILE = './processed_data/arcs_dict.pickle'

    if os.path.exists(DICT_PICKLE_FILE) == True:
        with open(DICT_PICKLE_FILE, 'rb') as handle:
            arcs = pickle.load(handle)

    else:
        arcs = get_all_arcs()

    return arcs