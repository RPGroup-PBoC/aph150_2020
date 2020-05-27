"""
This script uses the matplotlib plotting library to generate a plot of the
integrated irradiance factors of all stars of a given magnitude over the range
of visible magnitudes. It also computes the average brightness of the sky from
the integrated irradiance factor of the sky and prints it to the console.
"""
#%%
import numpy as np
from matplotlib import pyplot as plt

# Load in the data.
data = np.recfromcsv('../star_magnitudes_tidy.csv')

# Compute the irradiance factors for each magnitude band.
magnitudes = data['apparent_magnitude']
factors = 10**(-0.4*magnitudes)

# Compute the integrated irradiance factors in each band.
integrated = data['count'] * factors

# Compute the integrated irradiance factor and integrated magnitude of the sky
sky_factor = integrated.sum()
sky_magnitude = -2.5 * np.log10(sky_factor)

# Compute the angular area of the entire sky (arcsec^2)
sky_area = 4 * np.pi * (180/np.pi)**2 * (3600)**2

# Compute the average sky brightness (mag/arcsec^2)
sky_brightness = sky_magnitude + 2.5 * np.log10(sky_area)
result_txt = "The average brightness of the sky due to starlight is " + \
             "{:.2f}".format(sky_brightness) + " mag/arcsec^2"

# Generate the plot.
plt.plot(magnitudes, integrated)
plt.xlabel('apparent magnitude' + '\n\n\n' + result_txt)
plt.ylabel('integrated irradiance factor')
plt.title('Contribution to sky brightness of stars by magnitude')
plt.grid()
plt.savefig('../media/irradiance_factors.png', bbox_inches='tight')
# %%
