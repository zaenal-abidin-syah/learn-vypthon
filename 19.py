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

mySpeed =1
run = 1
def runRadio(x):
    global run
    if x.checked == True:
        run = 1
    if x.checked == False:
        run = 0
scene.append_to_caption('\n\n')
radio(bind=runRadio, text='Run')


def bigBall(x):
    global mRadius
    if x.checked == True:
        mRadius = mRadius * 2
        marble.radius = mRadius
    if x.checked == False:
        mRadius = mRadius / 2
        marble.radius = mRadius

scene.append_to_caption('\n\n')

    
checkbox(bind=bigBall, text='Big Ball')

def ballColorRed():
    marble.color = color.red

button(bind=ballColorRed, text='Red', color=color.black, background=color.red)

def ballColorGreen():
    marble.color = color.green

button(bind=ballColorGreen, text='Green', color=color.black, background=color.green)
def ballColorBlue():
    marble.color = color.blue

button(bind=ballColorBlue, text='Blue', color=color.black, background=color.blue)


def ballOpacity(x):
    op = x.value
    marble.opacity = op
slider(bind=ballOpacity, vertical=False, min=0, max=1, value=1, text='Ball opacity')

def speed(x):
    global mySpeed
    if x.selected == '1':
        mySpeed = 1
    if x.selected == '2':
        mySpeed = 2
    if x.selected == '3':
        mySpeed = 3
    if x.selected == '4':
        mySpeed = 4
    if x.selected == '5':
        mySpeed = 5
    
    

menu(bind=speed, choices=['1', '2', '3', '4', '5'])
while True:
    rate(10)
    xPos = xPos + deltaX * run * mySpeed
    yPos = yPos + deltaY * run * mySpeed
    zPos = zPos + deltaZ * run * mySpeed

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