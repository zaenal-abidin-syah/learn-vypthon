from vpython import *
import numpy as np

cylinder1 = cylinder(color=color.cyan, length=6, pos=vector(0, 3, 0))
cylinder2 = cylinder(color=color.orange, length=6, pos=vector(0, -3, 0))
c1Length = .1
c2Length = .1
c1Delta = .1
c2Delta = .1

while True:
    rate(50)
    c1Length = c1Length + c1Delta
    c2Length = c2Length + c2Delta
    cylinder1.length = c1Length
    cylinder2.length = c2Length
    if c1Length >= 6 or c1Length <= .1:
        c1Delta = c1Delta * -1
    if c2Length >= 6 or c2Length <= .1:
        c2Delta = c2Delta * -1