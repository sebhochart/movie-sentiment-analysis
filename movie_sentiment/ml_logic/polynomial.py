# libraries used for the polynomial plotting
import numpy as np
import matplotlib.pyplot as plt
from movie_sentiment.ml_logic.movie_score import movie_score
from sklearn.metrics import r2_score

def script_2_polynomial(script_score, plot = False):
    '''
    This function receives the script_score (1d array) and tries to fit it on a polynomial of degree3 or 5.
    Returns the polinomial coefficients as a list on length max_degree + 1.

    plot: if you want to see the score and fit plot, change to True
    '''

    degree = 3
    x_fit = np.arange(script_score.shape[0])
    coefficients = np.polyfit( x=np.arange(script_score.shape[0]), y=script_score, deg=degree)
    y_fit = np.polyval(coefficients, x_fit)

    r2 = r2_score(script_score, y_fit)
    #print('Initial R2 of the fit = ', f'{r2:.2f}')

    max_degree = 10
    while r2 < 0.75 and degree < max_degree:

        degree += 1
        coefficients = np.polyfit( x=np.arange(script_score.shape[0]), y=script_score, deg=degree)
        y_fit = np.polyval(coefficients, x_fit)
        r2 = r2_score(script_score, y_fit)
        #print('Improved R2 of the fit = ', f'{r2:.2f}')


    #print('Final R2 of the fit = ', f'{r2:.2f}', f'poly degree={degree}')
    #print('Next movie!')

    if plot == True:

        #plotting the actual score and the fitted curve
        plt.plot(x_fit, script_score)
        plt.plot(x_fit, y_fit, 'r')
        plt.ylim(-1,1)
        labels = ['Score', f'Fit (R2={r2:.2f})']
        plt.legend(labels)

    coefficients = [0]*(max_degree+1 - coefficients.shape[0]) + list(coefficients)


    return coefficients
