import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.spines as sps
import seaborn as sns


def plot_two_lines(dataframe, col_one, col_two):
    '''Plots two line graphs completly formated'''

    fig, ax = plt.subplots(figsize=(4,1.5))
    ax = sns.set_context('paper', font_scale=0.5)
    ax = sns.set_style("white",{'axes.edgecolor': '#ced4da',
                                 'axes.labelcolor': '#ced4da',
                                 'text.color': '#6c757d'})
    ax = sns.despine()
    ax = sns.lineplot(dataframe[col_one], color='#001427', label=col_one, linewidth=0.5)
    ax = sns.lineplot(dataframe[col_two], color= '#8d0801', label=col_two, linewidth=0.5)
    ax = plt.xlabel('')
    ax = plt.ylabel('')
    ax = sps.Spines(color='#6c757d')
    ax = plt.tick_params(labelbottom=False, labelleft=False)
    ax = plt.legend(ncols=2, frameon=False)
    return fig

def plot_one_line(dataframe):
    '''Plots one line graph completly formated'''

    fig, ax = plt.subplots(figsize=(4,2.5))
    ax = sns.set_context('paper', font_scale=0.5)
    ax = sns.set_style("white",{'axes.edgecolor': '#ced4da',
                                 'axes.labelcolor': '#ced4da',
                                 'text.color': '#6c757d'})
    ax = sns.despine()
    ax = sns.lineplot(dataframe, color= '#8d0801', linewidth=0.7)
    ax = plt.xlabel('')
    ax = plt.ylabel('')
    ax = sps.Spines(color='#6c757d')
    ax = plt.tick_params(labelbottom=False, labelleft=False)
    return fig
