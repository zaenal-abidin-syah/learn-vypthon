from vpython import *
import random

# Buat jendela VPython
scene = canvas(title='Five Randomly Moving Balls', width=800, height=600, center=vector(0,0,0))

# Fungsi untuk menghasilkan warna acak
def random_color():
    return vector(random.random(), random.random(), random.random())

# Fungsi untuk menghasilkan kecepatan acak di sumbu x dan y
def random_velocity():
    return vector(random.uniform(-1, 1), random.uniform(-1, 1), 0)

# Buat bola-bola
balls = []
for i in range(5):
    ball = sphere(pos=vector(random.uniform(-5, 5), random.uniform(-5, 5), 0),
                  radius=0.5,
                  color=random_color())
    ball.velocity = random_velocity()
    balls.append(ball)

# Menandai bola hijau
green_ball = balls[0]
green_ball.color = vector(0, 1, 0)  # Bola hijau

# Loop untuk menggerakkan bola
dt = 0.01
while True:
    rate(200)  # Tentukan kecepatan animasi
    
    # Cek apakah semua bola selain bola hijau sudah berhenti
    all_others_stopped = all(mag(ball.velocity) == 0 for ball in balls if ball != green_ball)
    
    for ball in balls:
        if ball == green_ball:
            if all_others_stopped:
                ball.velocity = vector(0, 0, 0)  # Hentikan bola hijau
            ball.pos += ball.velocity * dt
            
            # Memantul dari dinding di antara sumbu x dan y
            if abs(ball.pos.x) >= 5:
                ball.velocity.x *= -1
            if abs(ball.pos.y) >= 5:
                ball.velocity.y *= -1
            
            # Tetap di sumbu x dan y
            ball.pos.z = 0
        else:
            # Deteksi tabrakan dengan bola hijau
            if mag(ball.pos - green_ball.pos) <= (ball.radius + green_ball.radius):
                ball.velocity = vector(0, 0, 0)  # Bola lainnya berhenti
            else:
                ball.pos += ball.velocity * dt

                # Memantul dari dinding
                if abs(ball.pos.x) >= 5:
                    ball.velocity.x *= -1
                if abs(ball.pos.y) >= 5:
                    ball.velocity.y *= -1
                ball.pos.z = 0  # Tetap di sumbu x dan y
