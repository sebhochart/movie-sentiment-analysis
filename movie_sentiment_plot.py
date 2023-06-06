import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def movie_sentiment_plot(movie_df, score='compound'):
    fig = sns.scatterplot(x= movie_df.index, y = movie_df[score])
    plt.xlabel('Text chunks')
    plt.ylabel(f'{score} score')
    plt.show()
