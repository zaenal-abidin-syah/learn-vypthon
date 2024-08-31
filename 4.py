from vpython import *
wallThickness = .1
widthRoom = 15
heightRoom = 10
depthRoom = 6

mRadius = .75
floor = box(color=color.white, pos=vector(0, -heightRoom/2, 0), size=vector(widthRoom, wallThickness, depthRoom))
ceiling = box(color=color.white, pos=vector(0, heightRoom/2, 0), size=vector(widthRoom, wallThickness, depthRoom))
backWall = box(color=color.white, pos=vector(0, 0, -depthRoom/2), size=vector(widthRoom, heightRoom, wallThickness))
leftWall = box(color=color.white, pos=vector(-widthRoom/2, 0, 0), size=vector(wallThickness, heightRoom, depthRoom))
rightWall = box(color=color.white, pos=vector(widthRoom/2, 0, 0), size=vector(wallThickness, heightRoom, depthRoom))
marble = sphere(radius=mRadius, color=color.red)
xPos = 0

deltaX = .1
while True:
    rate(10)
    xPos = xPos + deltaX

    xrme = xPos + mRadius
    xlme = xPos - mRadius

    
    rwe = widthRoom/2 - wallThickness/2
    lwe = -widthRoom/2 + wallThickness/2

    if xrme >= rwe or xlme <= lwe:
        deltaX = deltaX * -1
    marble.pos = vector(xPos, 0, 0)