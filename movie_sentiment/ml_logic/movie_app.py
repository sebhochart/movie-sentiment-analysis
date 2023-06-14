#API
from fastapi import FastAPI
import pandas as pd
import numpy as np
from ..processing.arcs import get_all_dyn_arcs
from ..poster_api import get_poster
from ..ml_logic.recommendation import get_movies_recommendation
from ..ml_logic.classification import get_movie_classification
from ..ml_logic.polynomial import script_2_polynomial


app = FastAPI()
ALL_ARCS = get_all_dyn_arcs()

# Define a root `/` endpoint
@app.get('/')
def index():
    return {'message': 'Welcome to the Movie Sentiment Analysis API! Checkout the documentation at .../docs'}

@app.get('/movies_list')
def movies_list():
    return {'movies' : list(ALL_ARCS.keys()) }


@app.get('/arc')
def arc(movie_title, recommendation, polynomial):



    if movie_title in ALL_ARCS.keys():

        recom_list = ['Set the recommendation parameter to True to receive recommndations']
        movie_arc = ['No movie arc returned']
        response_image = ['No image returned']
        classification_info = ('No cluster','No Score')
        y_fit = ['Set the polynomial parameter to True to get the polynomial fit coefficients']



        movie_arc = ALL_ARCS[movie_title]



        if recommendation == 'active':
            recom_func_response = get_movies_recommendation(movie_title=movie_title, n = 6)
            recom_list = recom_func_response['movie_names']


        if polynomial == 'active':
            movie_arc_array = np.array(movie_arc)
            coeffs = script_2_polynomial(movie_arc_array, plot = False)
            x_fit = np.linspace(start=0, stop=movie_arc_array.shape[0], num=movie_arc_array.shape[0])
            y_fit = list(np.polyval(coeffs, x_fit))

        response_image = get_poster(movie_title)
        classification_info = get_movie_classification(movie_title)

        return {'arc' : movie_arc,
                'recom' : recom_list,
                'image' : response_image,
                'classification_cluster' : classification_info[0],
                'classificatin_score': classification_info[1],
                'poly_fit' : y_fit}
    else:

        message = 'Movie not found in our db 😭, Try another movie!'
        return {'arc' : message,
                'recom' : message,
                'image' : message,
                'classification_cluster' : message,
                'classificatin_score': message,
                'poly_fit' : message}


@app.get('/recom')
def recom_df(movie_title):

    recom_list = []
    recom_similarity_score = []


    recom_func = get_movies_recommendation(movie_title=movie_title, n = 6)
    recom_list = recom_func['movie_names']
    recom_similarity_score = recom_func['movie_scores']
    arc_list = []
    poster_list = []
    cluster_score_list = []
    cluster_list = []

    for movie in recom_list:
        movie_arc = ALL_ARCS[movie]
        arc_list.append(movie_arc)

        movie_poster = get_poster(movie)
        poster_list.append(movie_poster)
        classification_data = get_movie_classification(movie)
        movie_cluster_score = classification_data[1]
        cluster_score_list.append(movie_cluster_score)
        movie_cluster = classification_data[0]
        cluster_list.append(movie_cluster)


    result = {
        "Poster" : poster_list,
        "Title" : recom_list,
        "Similarity Score" : recom_similarity_score,
        "Arc" : arc_list,
        "Cluster" : cluster_list,
        "Cluster Score" : cluster_score_list,
        }

    result = pd.DataFrame(result).sort_values(by="Similarity Score", ascending=False)

    return result
