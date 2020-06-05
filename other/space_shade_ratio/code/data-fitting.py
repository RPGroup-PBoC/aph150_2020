### IMPORT PACKAGES ###

import numpy as np
from scipy.optimize import curve_fit
import scipy.stats as ss
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import math as m

if __name__ == "__main__":
    ### IMPORT EXPERIMENTAL DATA ###
    # The following experiemntal data was extracted from the following paper:
    # Lambour R, Rajan N, Morgan T, Kupiec I & Stansberry E. (2004). Assessment 
    # of orbital debris size estimation from radar cross-section measurements. 
    # Advances in Space Research 34(5): 1013-20. doi: 10.1016/j.asr.2003.02.043

    # Histogram data for each bin of size 1 cm. yData[i] represents the estimated
    # number of observed orbital debris in the study with an equivalent sphere
    # diameter betweeen i and i+1 cm. 
    yData = [0, 0, 9.36329588, 162.9213483, 333.3333333, 331.4606742, 479.4007491, 
           205.9925094, 93.6329588, 125.4681648, 161.0486891, 228.4644195, 114.2322097,
           91.76029963, 44.94382022, 43.07116105, 52.43445693, 71.16104869, 31.83520599,
           58.05243446, 86.1423221, 14.98127341, 9.36329588, 13.10861423, 9.36329588, 
           9.36329588, 11.23595506, 13.10861423, 26.21722846, 13.10861423, 11.23595506, 
           16.85393258, 11.23595506, 9.36329588, 14.98127341, 16.85393258, 35.58052434, 
           1.872659176, 20.59925094, 9.36329588, 1.872659176]

    # Bin boundaries for equivalent sphere diameter measurements (in cm).
    xBins = np.arange(start=1, stop=42, step=1) - 0.5
    
    # Generate a sample data set in order to actually visualize the data, based on the
    # x values xBins and y values yData from above.
    yDataSample = []
    for i in range(len(yData)):
        for j in range(int(yData[i])):
            yDataSample.append(xBins[i])
            
    # Initialize the plot environment.
    plt.figure(figsize=(6, 4), dpi=300, facecolor='w', edgecolor='k')
                
    ### GENERATE STATISTICAL MODEL THROUGH FITTING PARAMETERS ###
    # Plot the experimental data as a histogram.
    entries, bin_edges, patches = plt.hist(yDataSample, bins=xBins, density=True, label='Data', 
                                           alpha=1, color='yellow', edgecolor='black', linewidth=1.2)

    # Calculate the arithmetic mean centers of the bins.
    bin_middles = 0.5 * (bin_edges[1:] + bin_edges[:-1])

    # Fit function to an expected Poisson distribution with parameter lamb.
    def fit_function(k, lamb):
        return ss.poisson.pmf(k, lamb)

    # Perform the curve.
    parameters, cov_matrix = curve_fit(fit_function, bin_middles, entries, [2])

    # Generate and format the plot.
    plt.plot(
        np.arange(0, 41),
        fit_function(x_plot, *parameters),
        marker='o', linestyle='-',
        label='Poisson Fit Result',
    )
    plt.xlabel('Equivalent Sphere Diameter (cm)', fontsize=14)
    plt.ylabel('Proportion of Samples', fontsize=14)
    plt.legend()
    
    print(*parameters)
    # Generate and save the final image
    plt.savefig('aph150-final-figure.png', bbox_inches='tight')
