import numpy as np
import seaborn as sns
import pandas as pd
from movie_sentiment.processing.scripts import split_movie_script
from movie_sentiment.ml_logic.vader import model as vadar


def movie_score(movie_title, chunk_type, pad, group_chunk, window_size):
    '''
    Given a movite_title, this function calculates the arc score for that movie.
    type, pad are used by the movie_script_splitted
    group_chunk by Vader
    window_size by moving_average function

    The values for stopword and lemmatize must be changed manually in the code.

    The function returns: a numpy array of the moving average of the movie script scores
    '''

    movie_script_splitted = split_movie_script(movie_title, chunk_type=chunk_type, \
                                               pad=pad, lower=False, rm_stopwords=False, \
                                               lemmatize=False)
    movie_script_scored = vadar(movie_script_splitted, group_chunk)
    moving_average_score = moving_average( movie_script_scored['compound'], window_size)

    return moving_average_score


def moving_average(data, window_size):
    weights = np.repeat(1.0, window_size) / window_size
    moving_avg = np.convolve(data, weights, 'valid')
    return moving_avg

def movie_score_dyn_avg(movie_title, chunk_type, pad, group_chunk, window_size):
    '''
    Given a movite_title, this function calculates the arc score for that movie.
    type, pad are used by the movie_script_splitted
    group_chunk by Vader
    window_size by moving_average function

    The values for stopword and lemmatize must be changed manually in the code.

    The function returns: a numpy array of the moving average of the movie script scores
    '''

    movie_script_splitted = split_movie_script(movie_title, chunk_type=chunk_type, \
                                               pad=pad, lower=False, rm_stopwords=False, \
                                               lemmatize=False)
    movie_script_scored = vadar(movie_script_splitted, group_chunk)
    moving_average_score = dynamic_moving_average( movie_script_scored['compound'], window_size)

    return moving_average_score

def dynamic_moving_average(data, window_size):
    size = len(data)
    moving_avg = []
    j = 0
    #first average
    for i in range(size):
        if i <= window_size:
            weight = np.repeat(1.0, len(data[:i])) / len(data[:i])
            moving_avg.append(np.ma.average(data[:i],weights=weight))
        elif i <= size-window_size:
            weight = np.repeat(1.0, window_size) / window_size
            moving_avg.append(np.ma.average(data[i-window_size:i], weights=weight))
        elif i > size-window_size:
            #second average
            new_window = window_size-j
            weight = np.repeat(1.0, new_window) / new_window
            moving_avg.append(np.ma.average(data[i-new_window:i], weights=weight))
            if j == (window_size-10):
                pass
            else:
                j+=1
    return moving_avg[11:]
