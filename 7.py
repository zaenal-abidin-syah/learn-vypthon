from vpython import *
import numpy as np

sphere1 = sphere(color=color.white, radius=1, opacity=.3)
sphere2 = sphere(color=color.red, radius=.7, opacity=1)

cylinder1 = cylinder(color=color.white, radius=.5, length=3.5, opacity=.3)
cylinder2 = cylinder(color=color.red, radius=.3, opacity=1)
for i in np.linspace(1, 3, 10):
    mybox =box(color=color.white, opacity=.4, pos=vector(i, 0, .4), size=vector(.1, .7, .3))

while True:
    for length in np.linspace(1, 3, 1000):
        rate(250)
        cylinder2.length = length
    for length in np.linspace(3, 1, 1000):
        rate(250)
        cylinder2.length = length
