import numpy as np
from vpython import *

# Piston = cylinder(length=3, radius=1, color=color.blue, opacity=1)
Mysphere = sphere(radius=1, color=color.red, opacity=.5)

while True:
    for myRadius in np.linspace(.1, 1, 1000):
        rate(250)
        Mysphere.radius = myRadius
    for myRadius in np.linspace(1, .1, 1000):
        rate(250)
        Mysphere.radius = myRadius
    # for i in np.linspace(1, 6, 1000):
    #     rate(250)
    #     Piston.length = i
    # for i in np.linspace(6, 1, 1000):
    #     rate(250)
    #     Piston.length = i
    # warna_warna = [
    #     color.green,
    #     color.red,
    #     color.magenta,
    #     color.blue
    # ]
    # for opacity in np.linspace(1, 0, 1000):
    #     rate(250)
    #     Piston.opacity = opacity
    #     Piston.color = warna
        
    # for opacity in np.linspace(0,1, 1000):
    #     rate(250)
    #     Piston.opacity = opacity

    # for warna in warna_warna:
    #     for opacity in np.linspace(1, 0, 1000):
    #         rate(250)
    #         Piston.opacity = opacity
    #     Piston.color = warna
        
    #     for opacity in np.linspace(0,1, 1000):
    #         rate(250)
    #         Piston.opacity = opacity

