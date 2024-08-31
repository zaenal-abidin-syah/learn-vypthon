from vpython import *
# membuat canvas
myCanvas = canvas(title="Gerak Benda", width=800, height=600, center=vector(0,0,0))

bola = sphere(color=color.green, radius=1)
kecepatan = .01

def tekan_kunci(event):
  s=event.key
  if s == 'up':
    bola.pos.y += kecepatan
  if s == 'down':
    bola.pos.y -= kecepatan
  if s == 'right':
    bola.pos.x += kecepatan
  if s == 'left':
    bola.pos.x -= kecepatan
  
scene.bind('keydown', tekan_kunci)

while True:
  pass