#API
from fastapi import FastAPI
import pandas as pd
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


@app.get('/recom')
def recom_df(movie_title):

    recom_list = get_movies_recommendation(movie_title=movie_title, n = 5)
    arc_list = []
    poster_list = []
    score_list = []
    cluster_list = []

    for movie in recom_list:
        movie_arc = ALL_ARCS[movie]
        arc_list.append(movie_arc)

        movie_poster = get_poster(movie)
        poster_list.append(movie_poster)
        classification_data = get_movie_classification(movie)
        movie_score = classification_data[1]
        score_list.append(movie_score)
        movie_cluster = classification_data[0]
        cluster_list.append(movie_cluster)


    result = {
        "Title" : recom_list,
        "Arc" : arc_list,
        "Poster" : poster_list,
        "Score" : score_list,
        "Cluster" : cluster_list
        }


    return pd.DataFrame(result)
