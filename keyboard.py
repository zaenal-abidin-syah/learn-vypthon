from vpython import *

# Membuat scene
scene = canvas(title="Gerakkan Bola dengan Keyboard")

# Membuat bola
bola = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.red)

# Kecepatan gerakan bola
kecepatan = 0.1

# Fungsi untuk menangani input dari keyboard
def gerak_bola(evt):
    key = evt.key
    if key == 'left':
        bola.pos.x -= kecepatan
    elif key == 'right':
        bola.pos.x += kecepatan
    elif key == 'up':
        bola.pos.y += kecepatan
    elif key == 'down':
        bola.pos.y -= kecepatan

# Mengikat fungsi gerak_bola dengan event keydown
scene.bind('keydown', gerak_bola)

# Loop utama
while True:
    rate(100)
