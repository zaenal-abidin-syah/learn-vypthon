from vpython import *
import numpy as np
import time

clockR = 2
clockT =clockR / 10
majorTickL = clockR / 7
majorTickT = 2*np.pi*clockR / 400
majorTickW = clockT*1.2

minorTickL = clockR / 12
minorTickT = 2*np.pi*clockR / 600
minorTickW = clockT*1.2



minuteHandL = clockR-majorTickL
minuteHandT = minuteHandL / 50
minuteHandOffside = clockT/2 +minuteHandT

hourHandL = .75*minuteHandL
hourHandT = 1.25 * minuteHandT
hourHandOffside = clockT/2 + hourHandT

secondHandL = clockR-majorTickL
secondHandT = minuteHandL / 100
secondHandOffside = clockT * 1.5 +secondHandT


hubR = clockT/2

hourangle = np.pi/2
minuteangle = np.pi/2
secondangle = np.pi/2
# minuteInc = .001745
minuteInc = .0001

secondInc = minuteInc * 60
hourInc = minuteInc / 12


for theta in np.linspace(0, 2*np.pi, 13):
  majorTick = box(axis=vector(clockR*np.cos(theta), clockR*np.sin(theta), 0), color=color.black, length=majorTickL, width=majorTickW, height=majorTickT, pos=vector((clockR-majorTickL/2)*np.cos(theta), (clockR-majorTickL/2)*np.sin(theta), 0))
for theta in np.linspace(0, 2*np.pi, 61):
  minorTick = box(axis=vector(clockR*np.cos(theta), clockR*np.sin(theta), 0), color=color.black, length=minorTickL, width=minorTickW, height=minorTickT, pos=vector((clockR-minorTickL/2)*np.cos(theta), (clockR-minorTickL/2)*np.sin(theta), 0))

minuteHand = arrow(color=color.red, axis=vector(0, 1, 0), shaftwidth=minuteHandT, length=minuteHandL, pos=vector(0,0,minuteHandOffside))
hourHand = arrow(color=color.red, axis=vector(0, 1, 0), shaftwidth=hourHandT, length=hourHandL, pos=vector(0,0,hourHandOffside))
secondHand = arrow(color=color.red, axis=vector(0, 1, 0), shaftwidth=secondHandT, length=secondHandL, pos=vector(0,0,secondHandOffside))
hub = cylinder(axis=vector(0,0,1) ,color=color.red, radius=hubR, length=2*clockT)


clockFace = cylinder(axis=vector(0,0,1), color=vector(0,0,.8), length=clockT, radius=clockR, pos=vector(0,0, -clockT/2))

while True:
  rate(16)
  hour = time.localtime(time.time())[3]
  minute = time.localtime(time.time())[4]
  second = time.localtime(time.time())[5]
  if hour > 12:
    hour = hour - 12
  # hourangle = hourangle - hourInc
  # minuteangle = minuteangle - minuteInc
  secondangle = - second/60 * 2 * np.pi + np.pi / 2
  minuteangle = - minute/60 * 2 * np.pi + np.pi / 2
  hourangle = - (hour/12) * 2 * np.pi + np.pi / 2

  hourHand.axis = vector(hourHandL * np.cos(hourangle), hourHandL * np.sin(hourangle), 0)
  minuteHand.axis = vector(minuteHandL * np.cos(minuteangle), minuteHandL * np.sin(minuteangle), 0)
  secondHand.axis = vector(secondHandL * np.cos(secondangle), secondHandL * np.sin(secondangle), 0)