#API
from fastapi import FastAPI
from ..processing.arcs import get_all_dyn_arcs
from ..poster_api import get_poster_url



app = FastAPI()

arcs = get_all_dyn_arcs()

# Define a root `/` endpoint
@app.get('/')
def index():
    return {'ok': True}


@app.get('/arc')
def arc(movie_title):
    movie_arc = arcs[movie_title]
    image_url = get_poster_url[movie_title]
    recom_list =

    return {movie_title: [movie_arc, image_url, recom_list] }
