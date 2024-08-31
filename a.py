from vpython import *
import random

def warna():
    return [color.blue, color.yellow]

# Fungsi untuk menghasilkan kecepatan acak di sumbu x dan y
def random_velocity():
    return vector(random.uniform(-1, 1), random.uniform(-1, 1), 0)


# Buat bola-bola
balls = []
for i in range(2):
    ball = sphere(pos=vector(random.uniform(-5, 5), random.uniform(-5, 5), 0),
                  radius=0.5,
                  color=warna()[i])
    ball.velocity = random_velocity()
    balls.append(ball)

# Menandai bola hijau
green_ball = sphere(pos=vector(random.uniform(-5, 5), random.uniform(-5, 5), 0),
                  radius=0.5,
                  color=color.green)

def move_green_ball(evt):
    if evt.key == 'left':
        green_ball.pos.x -= 0.1
    elif evt.key == 'right':
        green_ball.pos.x += 0.1
    elif evt.key == 'up':
        green_ball.pos.y += 0.1
    elif evt.key == 'down':
        green_ball.pos.y -= 0.1

# Bind the function to the keyboard events
scene.bind('keydown', move_green_ball)


# Loop untuk menggerakkan bola
dt = 0.01
while True:
  rate(500)  # Tentukan kecepatan animasi
  
  # Cek apakah semua bola selain bola hijau sudah berhenti
  all_others_stopped = all(mag(ball.velocity) == 0 for ball in balls if ball != green_ball)
  for ball in balls:
    if abs(ball.pos.x) >= 5:
      ball.velocity.x *= -1
    if abs(ball.pos.y) >= 5:
      ball.velocity.y *= -1
    if mag(ball.pos - green_ball.pos) <= (ball.radius + green_ball.radius):
      # pass
      ball.velocity = vector(0, 0, 0) 
    else:
      ball.pos += ball.velocity * dt

    for i in balls:
      if i != ball:
        if mag(ball.pos - i.pos) <= (ball.radius + i.radius):
            if i == green_ball:
              i.velocity.x = random.uniform(-1, 1); 
              i.velocity.y = random.uniform(-1, 1);
            else:
              ball.velocity.x *= -1
              ball.velocity.y *= -1
              i.velocity.x *= -1
              i.velocity.y *= -1
           
