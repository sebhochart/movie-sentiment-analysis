#API
from fastapi import FastAPI
from ..processing.arcs import get_all_dyn_arcs
from ..poster_api import get_poster
from ..ml_logic.recommendation import get_movies_recommendation
from ..ml_logic.classification import get_movie_classification


app = FastAPI()
ALL_ARCS = get_all_dyn_arcs()

# Define a root `/` endpoint
@app.get('/')
def index():
    return {'message': 'Welcome to the Movie Sentiment Analysis API! Checkout the documentation at .../docs'}


@app.get('/arc')
def arc(movie_title, recommendation = True):

    if movie_title in ALL_ARCS.keys():
        movie_arc = ALL_ARCS[movie_title]

        recom_list = ['set the reccomendation parameter to True to receive recommndations']
        if recommendation:

            recom_list = get_movies_recommendation(movie_title=movie_title, n = 5)

        response_image = get_poster(movie_title)

        classification_info = get_movie_classification(movie_title)


        return {'arc' : movie_arc,
                'recom' : recom_list,
                'image' : response_image,
                'classification_cluster' : classification_info[0],
                'classificatin_score': classification_info[1]}
    else:
        return {'message' : 'Movie not found in our db 😭, Try another movie!',
                }
