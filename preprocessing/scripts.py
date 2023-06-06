import pandas as pd
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

def split_movie_script(movie_file, type='sentence', pad=500, lower=False, rm_stopwords=False, lemmatize=False):
    ''' Gets a movie script name as an input. Cleans \n chars.
    If type == sentence, returns a dataFrame of the sentences of the script
    If type == words, returns a dataFrame of chunks of pad words from the script (with punctuation, no tokenization, no lemmatization)

    If lower == True: all words are lowercased
    If rm_stopwords == True and sentence == False: stop words are removed
    If lemmatize == True and sentence == False: text is lemmatized (verbs and nouns)
    '''

    path = './raw_data/screenplay_data/data/raw_texts/raw_texts/'

    # reading the movie script
    movie_script = open(path + movie_file,'r').read()

    # cleaning \n chars
    movie_script_cleaned = ' '.join(movie_script.split('\n'))

    # returning the DataFrame of sentences
    if type == 'sentence':

        # removing capitalization
        if lower==True:
            movie_script_cleaned = movie_script_cleaned.lower()

        return pd.DataFrame(sent_tokenize(movie_script_cleaned))

    # returning a DataFrame of n=pad words
    if type == 'words':

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
