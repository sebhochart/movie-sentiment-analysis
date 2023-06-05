import pandas as pd
from nltk.tokenize import word_tokenize, sent_tokenize

def split_movie_script(movie_file, sentence=True, pad=500):
    ''' Gets a movie script name as an input. Cleans \n chars.
    If sentence == True, returns a dataFrame of the sentences of the script
    If sentence = False, returns a dataFrame of chunks of n=pad words from the script (with punctuation, no tokenization, no lemmatization)
    '''

    path = './raw_data/screenplay_data/data/raw_texts/raw_texts/'

    # reading the movie script
    movie_script = open(path + movie_file,'r').read()

    # cleaning \n chars
    movie_script_cleaned = ' '.join(movie_script.split('\n'))

    # returning the DataFrame of sentences
    if sentence == True:
        return pd.DataFrame(sent_tokenize(movie_script_cleaned))

    # returning a DataFrame of n=pad words
    else:

        # split by word (keeping punctuation)
        movie_script_words = movie_script_cleaned.split(' ')

        # removing empty words
        while '' in movie_script_words:
            movie_script_words.remove('')

        # creating the chunks
        chunks = []
        for i in range(0, len(movie_script_words), pad):
            chunks.append(' '.join(movie_script_words[i:i+pad]))

        return pd.DataFrame(chunks)
