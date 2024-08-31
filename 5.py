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
yPos = 0
zPos = 0
deltaX = .1
deltaY = .1
deltaZ = .1
# marble.pos = vector(0, 0, 10)
while True:
    rate(10)
    xPos = xPos + deltaX
    yPos = yPos + deltaY
    zPos = zPos + deltaZ

    xrme = xPos + mRadius
    xlme = xPos - mRadius
    ycme = yPos + mRadius
    ywme = yPos - mRadius
    zfme = zPos + mRadius
    zbme = zPos - mRadius


    
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
    if zfme >= fwe or zbme <= bwe:
        deltaZ = deltaZ * -1
    marble.pos = vector(xPos, yPos, zPos)