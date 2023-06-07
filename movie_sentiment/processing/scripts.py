import pandas as pd
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import os
import sys
import movie_sentiment.params

def split_movie_script(movie_file, chunk_type='sentence', pad=500, lower=False, rm_stopwords=False, lemmatize=False):
    ''' Gets a movie script name as an input. Cleans \n chars.
    If chunk_type == sentence, returns a dataFrame of the sentences of the script
    If chunk_type == words, returns a dataFrame of chunks of pad words from the script (with punctuation, no tokenization, no lemmatization)

    If lower == True: all words are lowercased
    If rm_stopwords == True and type == words: stop words are removed
    If lemmatize == True and type == words: text is lemmatized (verbs and nouns)
    '''

    file_path = './raw_data/screenplay_data/data/raw_texts/raw_texts/'

    # reading the movie script
    movie_script = open(file_path + movie_file, 'r', encoding='iso8859-1').read()

    # cleaning \n chars
    movie_script_cleaned = ' '.join(movie_script.split('\n'))

    # returning the DataFrame of sentences
    if chunk_type == 'sentence':

        # removing capitalization
        if lower==True:
            movie_script_cleaned = movie_script_cleaned.lower()

        return pd.DataFrame(sent_tokenize(movie_script_cleaned))

    # returning a DataFrame of n=pad words
    if chunk_type == 'words':

        # split by word (keeping punctuation)
        movie_script_words = movie_script_cleaned.split(' ')

        # removing empty words
        while '' in movie_script_words:
            movie_script_words.remove('')

        # removing capitalization
        if lower==True:
            movie_script_words = [word.lower() for word in movie_script_words]

        # removing stopwords
        if rm_stopwords == True:
            stop_words = set(stopwords.words('english'))
            movie_script_words = [word for word in movie_script_words if not word in stop_words]

        # lemmatize
        if lemmatize == True:
            movie_script_words = [WordNetLemmatizer().lemmatize(word, pos='v') for word in movie_script_words]
            movie_script_words = [WordNetLemmatizer().lemmatize(word, pos='n') for word in movie_script_words]

        # creating the chunks
        chunks = []
        for i in range(0, len(movie_script_words), pad):
            chunks.append(' '.join(movie_script_words[i:i+pad]))

        return pd.DataFrame(chunks)


def get_all_movie_scripts(chunk_type='sentence', pad=500, lower=False, rm_stopwords=False, lemmatize=False):
    ''' Generates a dictionnary of all movies preprocessed.
    Same parameters as in the split_movie_script can be applied
    '''

    # getting the list of file names of all scripts
    path = './raw_data/screenplay_data/data/raw_texts/raw_texts/'
    movie_list = os.listdir(path)

    scripts = {}

    for index, movie_file in enumerate(movie_list):

        # printing progress
        sys.stdout.write('\r')
        sys.stdout.write(f"{index+1}/{len(movie_list)} movies processed")
        sys.stdout.flush()

        # split the script in chunks
        movie_script = split_movie_script(
            movie_file,
            chunk_type=chunk_type,
            pad=pad,
            lower=lower,
            rm_stopwords=rm_stopwords,
            lemmatize=lemmatize
        )

        # get the movie name and movie id from file name (id is not used but could be later)
        movie_name, movie_id = movie_file.strip('.txt').split('_')

        # add to the dictionnary
        scripts[movie_name] = movie_script

    return scripts
