from vpython import *
import numpy as np


arraowL = 2
arraowT = .02
pntT = .04
theta = 0
bRadius = .05
xArrow = arrow(color=color.red, axis=vector(1, 0, 0), length=arraowL, shaftwidth=arraowT)
yArrow = arrow(color=color.green, axis=vector(0, 1, 0), length=arraowL, shaftwidth=arraowT)
zArrow = arrow(color=color.blue, axis=vector(0, 0, 1), length=arraowL, shaftwidth=arraowT)
pArrow = arrow(color=color.orange, axis=vector(1, 0, 0), length=arraowL, shaftwidth=pntT)
ball = sphere(make_trail=True, trail_color=color.orange ,color=color.red, radius=bRadius, pos=vector(arraowL, 0, 0))

while True:

  for angle in np.linspace(0, 2*np.pi, 1000):
    rate(100)
    pArrow.axis = vector(arraowL*np.cos(angle), arraowL*np.sin(angle), 0)
    pArrow.length = arraowL
    ball.pos = vector(arraowL*np.cos(angle), arraowL*np.sin(angle), 0)
  for angle in np.linspace(0, 5*np.pi/2, 1000):
    rate(100)
    pArrow.axis = vector(arraowL*np.cos(angle), 0, arraowL*np.sin(angle))
    pArrow.length = arraowL
    ball.pos = vector(arraowL*np.cos(angle), 0, arraowL*np.sin(angle))
  for angle in np.linspace(0, 2*np.pi, 1000):
    rate(100)
    pArrow.axis = vector(0, arraowL*np.sin(angle), arraowL*np.cos(angle))
    pArrow.length = arraowL
    ball.pos = vector(0, arraowL*np.sin(angle), arraowL*np.cos(angle))
  for angle in np.linspace(np.pi/2, 2*np.pi, 1000):
    rate(100)
    pArrow.axis = vector(arraowL*np.cos(angle), 0, arraowL*np.sin(angle))
    pArrow.length = arraowL
    ball.pos = vector(arraowL*np.cos(angle), 0, arraowL*np.sin(angle))