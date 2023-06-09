import requests
from PIL import Image
import requests
from io import BytesIO

def get_poster(movie_name):
    '''use OMDb API to get the posters of the movies'''

    url = f'http://www.omdbapi.com/?i=tt3896198&apikey=128f29af&t={movie_name}'

    api_response = requests.get(url).json()['Poster']
    response_image = requests.get(api_response)

    return Image.open(BytesIO(response_image.content))

def get_poster_url(movie_name):
    '''use OMDb API to get the posters of the movies'''

    url = f'http://www.omdbapi.com/?i=tt3896198&apikey=128f29af&t={movie_name}'

    api_response = requests.get(url).json()['Poster']
    response_image = requests.get(api_response)

    return response_image
