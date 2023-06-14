import requests
#from PIL import Image
import requests
#from io import BytesIO

def get_poster(movie_name):
    '''use OMDb API to get the posters of the movies'''

    url = f'http://www.omdbapi.com/?i=tt3896198&apikey=128f29af&t={movie_name}'

    api_response = requests.get(url)

    response = 'https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg'
    if api_response.status_code == 200:
        # Successful response
        response = api_response.json()['Poster']
        print(response)
        print("Poster API request was successful!")


        #print("API request failed with status code:", api_response.status_code)



    #return Image.open(BytesIO(response_image.content))
    return response
