import pandas as pd
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def model(movie_script, n=1):

    #group chuncks in the amount requested by n
    movie_grouped = []
    test_list = np.arange(0, len(movie_script), n)
    for t in test_list:
        aux = ''
        sentences = movie_script.iloc[t:t+n,0]
        for sen in sentences:
            aux += sen
        movie_grouped.append(aux)
    movie_grouped = pd.DataFrame(movie_grouped, columns=['script'])

    #run model
    analyzer = SentimentIntensityAnalyzer()
    movie_grouped['result'] = movie_grouped.script.apply(lambda x: analyzer.polarity_scores(x))
    movie_grouped['neu'] = movie_grouped.result.apply(lambda x: x['neu'])
    movie_grouped['neg'] = movie_grouped.result.apply(lambda x: x['neg'])
    movie_grouped['pos'] = movie_grouped.result.apply(lambda x: x['pos'])
    movie_grouped['compound'] = movie_grouped.result.apply(lambda x: x['compound'])
    movie_grouped = movie_grouped.drop(columns='result')
    return movie_grouped
