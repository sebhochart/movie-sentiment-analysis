import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from movie_sentiment.ml_logic.movie_score import movie_score
from sklearn.metrics import r2_score

def script_2_polynomial(script_score, plot = False):
    '''
    This function receives the script_score (1d array) and tries to fit it on a polynomial of degree3 or 5.
    Returns the polinomial coefficients as a numpy array.

    plot: if you want to see the score and fit plot, change to True
    '''

    x_fit = np.arange(script_score.shape[0])
    coefficients = np.polyfit( x=np.arange(script_score.shape[0]), y=script_score, deg=3)
    y_fit = np.polyval(coefficients, x_fit)

    r2 = r2_score(script_score, y_fit)

    if r2 < 0.75:
        coefficients = np.polyfit( x=np.arange(script_score.shape[0]), y=script_score, deg=5)
        y_fit = np.polyval(coefficients, x_fit)
        r2 = r2_score(script_score, y_fit)

    print('R2 of the fit = ', f'{r2:.2f}')

    if plot == True:
        #plotting the actual score and the fitted curve
        plt.plot(x_fit, script_score)
        plt.plot(x_fit, y_fit, 'r')
        plt.ylim(-1,1)
        labels = ['Score', f'Fit (R2={r2:.2f})']
        plt.legend(labels)

    return coefficients
