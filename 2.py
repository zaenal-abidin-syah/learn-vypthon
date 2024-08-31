from vpython import *

floors = box(color=color.white, pos=vector(0, -5, 0), size=vector(10, .1, 10))
ceiling = box(color=color.white, pos=vector(0, 5, 0), size=vector(10, .1, 10))
backWall = box(color=color.white, pos=vector(0, 0, -5), size=vector(10, 10, .1))
leftWall = box(color=color.white, pos=vector(-5, 0, 0), size=vector(.1, 10, 10))
rightWall = box(color=color.white, pos=vector(5, 0, 0), size=vector(.1, 10, 10))
marble = sphere(radius=.75, color=color.green)
marble1 = sphere(radius=.75, color=color.red)
marble2 = sphere(radius=.75, color=color.white)
marble3 = sphere(radius=.75, color=color.yellow)
marble4 = sphere(radius=.75, color=color.blue)
xPos = 0
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
deltaX = .1
while True:
    rate(10)
    xPos = xPos + deltaX
    if xPos > 5 or xPos < -5:
        deltaX = deltaX * -1
    marble.pos = vector(xPos, 0, 0)
    if marble1.