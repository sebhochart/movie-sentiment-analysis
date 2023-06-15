import requests
import pandas as pd
import pickle
from movie_sentiment.params import *


# def get_poster(movie_name):
    # '''use OMDb API to get the posters of the movies'''

    # url = f'http://www.omdbapi.com/?i=tt3896198&apikey=128f29af&t={movie_name}'

    # api_response = requests.get(url).json()

    # if api_response['Response'] == "True":
    #     response = api_response['Poster']
    # else:
    #     response = 'https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg'

    # return response

def get_poster(movie_name):

    with open(IDS_PICKLE_FILE, 'rb') as handle:
        ids = pickle.load(handle)

    movies_df = pd.DataFrame.from_dict(ids, orient='index', columns=['movie_name'])
    movie_id = str(min(list(movies_df[movies_df['movie_name']==movie_name].index)))

    while len(movie_id) < 7:
        movie_id = f'0{movie_id}'

    url = f'http://www.omdbapi.com/?i=tt{movie_id}&apikey=128f29af'

    api_response = requests.get(url).json()

    if api_response['Response'] == "True":
        response = api_response['Poster']
    else:
        response = 'https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg'

    return response
