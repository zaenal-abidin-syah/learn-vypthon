from vpython import *
# from time import *
ball = sphere(radius=1, color=color.white)
rChan = 0
gChan = 0
bChan = 0
rInc = 0.002
gInc = 0.007
bInc = 0.015
while True:
    rate(250)
    rChan = rChan + rInc
    gChan = gChan + gInc
    bChan = bChan + bInc
    ball.color = vector(rChan, gChan, bChan)
    if rChan >= 1 or rChan <= 0:
        rInc = rInc * -1
    if gChan >= 1 or gChan <= 0:
        gInc = gInc * -1
    if bChan >= 1 or bChan <= 0:
        bInc = bInc * -1
    