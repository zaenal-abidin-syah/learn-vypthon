from vpython import *
import numpy as np

clockR = 2
clockT =clockR / 10
majorTickL = clockR / 7
majorTickT = 2*np.pi*clockR / 400
majorTickW = clockT*1.2

minorTickL = clockR / 12
minorTickT = 2*np.pi*clockR / 600
minorTickW = clockT*1.2


for theta in np.linspace(0, 2*np.pi, 13):
  majorTick = box(axis=vector(clockR*np.cos(theta), clockR*np.sin(theta), 0), color=color.black, length=majorTickL, width=majorTickW, height=majorTickT, pos=vector((clockR-majorTickL/2)*np.cos(theta), (clockR-majorTickL/2)*np.sin(theta), 0))
for theta in np.linspace(0, 2*np.pi, 61):
  minorTick = box(axis=vector(clockR*np.cos(theta), clockR*np.sin(theta), 0), color=color.black, length=minorTickL, width=minorTickW, height=minorTickT, pos=vector((clockR-minorTickL/2)*np.cos(theta), (clockR-minorTickL/2)*np.sin(theta), 0))



clockFace = cylinder(axis=vector(0,0,1), color=vector(0,0,.8), length=clockT, radius=clockR, pos=vector(0,0, -clockT/2))