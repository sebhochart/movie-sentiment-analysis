import pandas as pd
from nltk.tokenize import word_tokenize, sent_tokenize

def split_movie_script(movie_file, sentence=True):
    ''' Gets a movie script as an input, cleans \n and returns a DataFrame of sentences of the script
    '''

    path = './raw_data/screenplay_data/data/raw_texts/raw_texts/'

    # reading the movie script
    movie_script = open(path + movie_file,'r').read()

    # cleaning \n chars
    movie_script_cleaned = ' '.join(movie_script.split('\n'))

    # returning the DataFrame of sentences
    return pd.DataFrame(sent_tokenize(movie_script_cleaned))
