## HOW BRIGHT IS A CITY?

[//]: # "Why is question interesting? What kind of impact? Public discourse?"

We don't often think about light as an emission, but it shouldn't be surprising
that humans are responsible for a significant portion of nighttime luminance.
The Fish and Wildlife Commission recognizes that light pollution can severely
disturb the habits and habitats of local wildlife. Also, light pollution in
urban centers is known to obscure the stars at night.

[//]: # "What does the data say?"

There are many ways to measure light. The SI unit quantifying light in the
visible spectrum is the lumen (lm), which measures the total output of a light
source. Light is not always radiated uniformly, so the candela (cd) measures the
distribution of luminous flux over solid angle measured in steradians (sr).
One candela is one lumen per steradian. Finally, the preferred unit for
brightness is cd/m², where we then divide by the source's surface area.
Cinzano et al. produced the first atlas mapping sky brightness
due to artificial lighting over the entire world, showing just how much local
city lights can affect the night sky. Below is an image showing the complete
world atlas (wherever data was available) and a zoomed-in map of just the US.
Each color corresponds to a range of sky brightness values as follows:
- Blue: 27.7-83.2 μcd/m²
- Green: 83.2-252 μcd/m²
- Yellow: 252-756 μcd/m²
- Orange: 756-2268 μcd/m²
- Red: 2268-6804 μcd/m²
- White: >6804 μcd/m²

![](media/cinzano_atlas_world.jpeg)

![](media/cinzano_atlas_us.jpeg)

Notably, 252 μcd/m² was chosen as the cutoff between green and yellow because
that was Cinzano's number for average natural sky brightness (so in all levels
beyond green, less than half of the light coming from the sky is natural) While
this data is illuminating, so to say, it does not answer our fundamental
question, since these maps report the effect of a city's light emissions on
local sky brightness, but not the brightness of the city itself. For more
information, we look towards R. H. Garstang's 1986 paper on estimating night sky
illumination due to local cities, which finds good agreement with data when each
person in a city is assumed to put off about 1000 lm / 2π sr ≈ 160 cd.
Multiplying this by the average population density of US cities
(1,600/km²) will then give us the total luminous output of the average city
divided by its area, which we established is exactly its brightness. Performing
this calculating, we see that a city's brightness is 256,000 μcd/m² on average.
Dividing this by the average natural sky brightness, we see that on average,
**a city is about 1,000 times brighter than all the night sky.**

[//]: # "Use estimates to validate data"

Now that we have numbers, let's give them a sanity check to see how realistic
this all is. We'll start by estimating the average sky brightness due to all the
stars in the sky. The National Solar Observatory provides data on how many stars
there are in each apparent magnitude class. The apparent magnitude scale is
exponential, so we must convert these magnitudes into linear factors before
we add them up. After totaling them up and averaging over the entire sky, we get
a surface brightness of 23.12 mag/arcsec². To convert this to the units we've
been using, we need to establish a scale factor for the brightness of a star.
Using data from C. W. Allen's 1973 textbook "Astrophysical Quantities", we can
derive the following conversion formula from mag/arcsec² to μcd/m²:

![equation](https://latex.codecogs.com/gif.latex?b%20%3D%201.08864%20%5Ctimes%2010%5E%7B11%7D%20%5Ccdot%2010%5E%7B-0.4S%7D)

Applying this to our quantity above tells us that the average brightness of the
sky due to every star visible from the Earth is 61.50 μcd/m², which is only a
factor of 4 off from Cinzano's number, which includes other light sources like
airglow.

As for Garstang's per-person luminance numbers, a quick look over various lamps
available for sale shows that luminous output ranges between 200-4,000 lm per
lamp. Taking the geometric mean of 900 lm and letting this light spread
uniformly over angles gives us an estimate of 70 cd per lamp. Assuming that each
person in a city own only a few lamps gives us numbers well in agreement with
Garstang's parametric fit.

[//]: # "Final thoughts on impact"

As human settlements cover an increasingly large portion of the Earth's surface,
a truly dark night sky becomes increasingly more rare. Cinzano calculates that
artificial sky brightness already exceeds natural sky brightness for 43% of the
Earth's population. The precise effects of this are still under debate, and the
study of light pollution is still a very young science, but for those living in
densely populated cities, the impact of human presence is readily apparent: you
just have to look up.
