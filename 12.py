from vpython import *
import numpy as np


arraowL = 2
arraowT = .02
theta = 0
pntT = .04
# xArrow = arrow(color=color.red, axis=vector(1,0,0), length=arraowL, shaftwidth=arraowT)
# yArrow = arrow(color=color.yellow, axis=vector(0,1,0), length=arraowL, shaftwidth=arraowT)
# zArrow = arrow(color=color.green, axis=vector(0,0,1), length=arraowL, shaftwidth=arraowT)
pArrow = arrow(color=color.orange, axis=vector(arraowL*np.cos(theta), arraowL*np.sin(theta), 0), length=arraowL, shaftwidth=pntT)

while True:

  for angle in np.linspace(0, 2*np.pi, 1000):
    rate(50)
    pArrow.axis = vector(arraowL*np.cos(angle), arraowL*np.sin(angle), 0)
    pArrow.length = arraowL