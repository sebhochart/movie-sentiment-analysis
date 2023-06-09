
import sys
import os
import pandas as pd
import pickle
from os.path import exists

from movie_sentiment.ml_logic.movie_score import movie_score, movie_score_dyn_avg
from movie_sentiment.ml_logic.polynomial import script_2_polynomial
from movie_sentiment.params import *
from movie_sentiment.processing.reshape_arc import reshaping_arc


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

        # check if the arc has the minimum required size
        if len(arc_score) >= MIN_LENGHT_ARCS:

            # get the movie name and movie id from file name (id is not used but could be later)
            movie_name, movie_id = movie_file.strip('.txt').split('_')

            # add to the dictionnary
            arcs[movie_name] = arc_score

    # Save in pickle file
    print('Saving in pickle file')
    with open(DICT_PICKLE_FILE, 'wb') as handle:
        pickle.dump(arcs, handle, protocol=pickle.HIGHEST_PROTOCOL)

    print('Saved in pickle file')

    return arcs

def generate_all_arcs_new_avg():
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
        arc_score = movie_score_dyn_avg(
            movie_file,
            chunk_type='sentence',
            pad=50,
            group_chunk=10,
            window_size=50
        )

        # check if the arc has the minimum required size
        if len(arc_score) >= MIN_LENGHT_ARCS:

            # get the movie name and movie id from file name (id is not used but could be later)
            movie_name, movie_id = movie_file.strip('.txt').split('_')

            # add to the dictionnary
            arcs[movie_name] = arc_score

    # Save in pickle file
    print('Saving in pickle file')
    with open(DICT_PICKLE_FILE_DYN_AVG, 'wb') as handle:
        pickle.dump(arcs, handle, protocol=pickle.HIGHEST_PROTOCOL)

    print('Saved in pickle file')

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

def get_all_dyn_arcs():

    if os.path.exists(DICT_PICKLE_FILE_DYN_AVG) == True:
        print('Loading data from pickle file')
        with open(DICT_PICKLE_FILE_DYN_AVG, 'rb') as handle:
            arcs = pickle.load(handle)

    else:
        print('Generating data for movie arcs')
        arcs = generate_all_arcs()

    return arcs


def get_all_polynomials(dyn_avg=False):
    '''Creates a DataFrame of polynomial values of movie arcs to feed our model
    Columns of the DataFrame are 'movie_name' and then ids
    '''
    if dyn_avg == False:
        arcs = get_all_arcs()
    else:
        arcs = get_all_dyn_arcs()
    poly = []

    # creating a list with the movie name and the coefficients
    for key, value in arcs.items():
        row = script_2_polynomial(value)
        row.insert(0, key)
        poly.append(row)

    # creating the columns name of the DataFrame
    columns_id= [x for x in range(len(poly[0]) - 1)]
    columns_id.insert(0, 'movie_name')

    # returning the DataFrame
    return pd.DataFrame(poly, columns=columns_id)

def get_all_reshaped_arcs(dyn_avg=False):
    '''Creates a DataFrame of polynomial values of movie arcs to feed our model
    Columns of the DataFrame are 'movie_name' and then ids
    '''
    if dyn_avg == False:
        arcs = get_all_arcs()
    else:
        arcs = get_all_dyn_arcs()
    reshaped = []

    # creating a list with the movie name and the coefficients
    for key, value in arcs.items():
        row = reshaping_arc(value)
        if row == None:
            pass
        else:
            row.insert(0, key)
            reshaped.append(row)

    # creating the columns name of the DataFrame
    columns_id= [x for x in range(len(reshaped[0]) - 1)]
    columns_id.insert(0, 'movie_name')

    # returning the DataFrame
    return pd.DataFrame(reshaped, columns=columns_id)
