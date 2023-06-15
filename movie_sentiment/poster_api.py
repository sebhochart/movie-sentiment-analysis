import requests


def get_poster(movie_name):
    '''use OMDb API to get the posters of the movies'''

    url = f'http://www.omdbapi.com/?i=tt3896198&apikey=128f29af&t={movie_name}'

    api_response = requests.get(url).json()

    if api_response['Response'] == "True":
        response = api_response['Poster']
    else:
        response = 'movie_sentiment/streamlit/img/default-movie.png'
        'https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg'

    return response
