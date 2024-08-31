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
marble = sphere(radius=mRadius, color=color.green)
xPos = 0
yPos = 0
zPos = 0
deltaX = .2
deltaY = .2


marble1 = sphere(radius=mRadius, color=color.red)
xPos1 = 2
yPos1 = 3
zPos1 = 0
deltaX1 = .1
deltaY1 = .1

marble2 = sphere(radius=mRadius, color=color.yellow)
xPos2 = -2
yPos2 = 2
zPos2 = 0
deltaX2 = -.1
deltaY2 = .1

marble3 = sphere(radius=mRadius, color=color.blue)
xPos3 = -2
yPos3 = 3
zPos3 = 0
deltaX3 = .1
deltaY3 = -.1


marble4 = sphere(radius=mRadius, color=color.purple)
xPos4 = 4
yPos4 = 2
zPos4 = 0
deltaX4 = .1
deltaY4 = .1


stop1 = False
stop2 = False
stop3 = False
stop4 = False

while True:
    rate(10)
    xPos = xPos + deltaX
    yPos = yPos + deltaY

    xrme = xPos + mRadius
    xlme = xPos - mRadius
    ycme = yPos + mRadius
    ywme = yPos - mRadius


    
    
    
    xPos1 = xPos1 + deltaX1
    yPos1 = yPos1 + deltaY1

    xrme1 = xPos1 + mRadius
    xlme1 = xPos1 - mRadius
    ycme1 = yPos1 + mRadius
    ywme1 = yPos1 - mRadius

    xPos2 = xPos2 + deltaX2
    yPos2 = yPos2 + deltaY2

    xrme2 = xPos2 + mRadius
    xlme2 = xPos2 - mRadius
    ycme2 = yPos2 + mRadius
    ywme2 = yPos2 - mRadius

    xPos3 = xPos3 + deltaX3
    yPos3 = yPos3 + deltaY3

    xrme3 = xPos3 + mRadius
    xlme3 = xPos3 - mRadius
    ycme3 = yPos3 + mRadius
    ywme3 = yPos3 - mRadius

    xPos4 = xPos4 + deltaX4
    yPos4 = yPos4 + deltaY4

    xrme4 = xPos4 + mRadius
    xlme4 = xPos4 - mRadius
    ycme4 = yPos4 + mRadius
    ywme4 = yPos4 - mRadius


    rwe = widthRoom/2 - wallThickness/2
    lwe = -widthRoom/2 + wallThickness/2
    cwe = heightRoom/2 - wallThickness/2
    wwe = -heightRoom/2 + wallThickness/2
    fwe = depthRoom/2 - wallThickness/2
    bwe = -depthRoom/2 + wallThickness/2

    if xrme >= rwe or xlme <= lwe:
        deltaX = deltaX * -1
    if ycme >= cwe or ywme <= wwe:
        deltaY = deltaY * -1
    marble.pos = vector(xPos, yPos, 0)

    if xrme1 >= rwe or xlme1 <= lwe:
        deltaX1 = deltaX1 * -1
    if ycme1 >= cwe or ywme1 <= wwe:
        deltaY1 = deltaY1 * -1
    marble1.pos = vector(xPos1, yPos1, 0)

    if xrme2 >= rwe or xlme2 <= lwe:
        deltaX2 = deltaX2 * -1
    if ycme2 >= cwe or ywme2 <= wwe:
        deltaY2 = deltaY2 * -1
    marble2.pos = vector(xPos2, yPos2, 0)

    if xrme3 >= rwe or xlme3 <= lwe:
        deltaX3 = deltaX3 * -1
    if ycme3 >= cwe or ywme3 <= wwe:
        deltaY3 = deltaY3 * -1
    marble3.pos = vector(xPos3, yPos3, 0)

    if xrme4 >= rwe or xlme4 <= lwe:
        deltaX4 = deltaX4 * -1
    if ycme4 >= cwe or ywme4 <= wwe:
        deltaY4 = deltaY4 * -1
    marble4.pos = vector(xPos4, yPos4, 0)

    if ((xrme > xrme1 > xlme) or (xrme > xlme1 > xlme)) and ( (ycme > ycme1 > ywme) or (ycme > ywme1 > ywme)):
        deltaX1 = 0
        deltaY1 = 0
        stop1 = True
    if ((xrme > xrme2 > xlme) or (xrme > xlme2 > xlme)) and ( (ycme > ycme2 > ywme) or (ycme > ywme2 > ywme)):
        deltaX2 = 0
        deltaY2 = 0
        stop2 = True


    if ((xrme > xrme3 > xlme) or (xrme > xlme3 > xlme)) and ( (ycme > ycme3 > ywme) or (ycme > ywme3 > ywme)):
        deltaX3 = 0
        deltaY3 = 0
        stop3 = True

    if ((xrme > xrme4 > xlme) or (xrme > xlme4 > xlme)) and ( (ycme > ycme4 > ywme) or (ycme > ywme4 > ywme)):
        deltaX4 = 0
        deltaY4 = 0
        stop4 = True
    
    if stop1 and stop2 and stop3 and stop4:
        deltaX = 0
        deltaY = 0

