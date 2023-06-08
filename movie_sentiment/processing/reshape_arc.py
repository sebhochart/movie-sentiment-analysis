import numpy as np
import math
from movie_sentiment.params import *

def reshaping_arc(processed_script, intervals=30):
    '''gets the processed script and splits it into a defined
    number of intervals using the mean of those intervals'''

    if MIN_LENGHT_ARCS > len(processed_script):
        return None

    limits = np.arange(0,len(processed_script), math.floor(len(processed_script)/intervals))
    reshaped_script = []

    for i in range(0, intervals):
        if i == intervals-1:
            reshaped_script.append(np.mean(processed_script[limits[i]:]))
        else:
            reshaped_script.append(np.mean(processed_script[limits[i]:limits[i+1]]))

    return reshaped_script
