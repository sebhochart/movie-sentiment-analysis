#API
from fastapi import FastAPI
from ..processing.arcs import get_all_dyn_arcs
from ..poster_api import get_poster
from ..ml_logic.recommendation import get_movies_recommendation


app = FastAPI()
ALL_ARCS = get_all_dyn_arcs()

# Define a root `/` endpoint
@app.get('/')
def index():
    return {'ok': True}


@app.get('/arc')
def arc(movie_title, recommendation = True):

    movie_arc = ALL_ARCS[movie_title]

    recom_list = []
    if recommendation == True:
        recom_list = get_movies_recommendation(movie_title)

    response_image = get_poster(movie_title)

    return {'arc' : movie_arc,
            'recom' : recom_list,
            'image' : response_image}
